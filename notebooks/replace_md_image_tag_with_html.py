# Run this with python replace_nd_image_tags_with_html
import re
from pathlib import Path
from argparse import ArgumentParser

import nbformat as nbf


def markdown_cells(nb):
    """
    Iterator for markdown cells in notebook.

    Parameters
    ----------

    nb : nbformat notebook object
        Notebook in which to replace links.
    """
    for cell in nb['cells']:
        if cell['cell_type'] == "markdown":
            yield cell


def find_links(text, image_only=False):
    """
    Find Markdown links in text and return a match object.

    Markdown links are expected to have the form [some txt](A-url.ext)
    or ![Alt text](cool-image.png).

    Parameters
    ----------

    text : str
        Text in which to search for links.

    image_only : bool
        If ``True``, find only markdown image links, i.e. those that
        begin with an exclamation mark.

    Returns
    -------

    list
        List of ``re.Match`` objects, one for each link found. Each object
        has two named groups, 'link_text', which contains the the part between
        the square brackets, and 'link',which is the URL (or file name for an
        image).
    """
    if image_only:
        markdown_link = \
            re.compile(r"!\[(?P<link_text>.+?\n*?.*?)\]\((?P<link_url>.+?)\)",
                       flags=re.MULTILINE)
    else:
        markdown_link = \
            re.compile(r"!?\[(?P<link_text>.+?\n*?.*?)\]\((?P<link_url>.+?)\)",
                       flags=re.MULTILINE)
    groups = [m for m in markdown_link.finditer(text)]
    return groups


def replace_image_link(nb):
    """
    Replace markdown image links in a notebook with an
    HTML image tag.

    Parameters
    ----------

    nb : nbformat notebook object
        Notebook in which to replace links.

    Notes
    -----

    The text between the brackets is the put into the alt attribute
    of the image tag
    .
    """
    updated_notebook = False
    for cell in markdown_cells(nb):
        link_matches = find_links(cell['source'], image_only=True)
        new_source = cell['source']
        for link_match in link_matches:
            to_replace = link_match.group()
            alt_text = link_match.groupdict()['link_text']
            img_link = link_match.groupdict()['link_url']
            replacement_text = f'<img src="{img_link}" alt="{alt_text}">'
            new_source = new_source.replace(to_replace, replacement_text)
        if link_matches:
            cell['source'] = new_source
            updated_notebook = True

    return updated_notebook


def fix_notebooks_in_folder(folder_path):
    """
    Change all of the markdown image links to to HTML image tags in
    every notebook contained in this folder and its children.
    """
    p = Path(folder_path)

    notebooks = p.glob('**/*.ipynb')

    for notebook in notebooks:
        if '.ipynb_checkpoints' in str(notebook):
            # Don't care about checkpoints, so skip them
            continue
        nb = nbf.read(notebook, 4)
        if replace_image_link(nb):
            print(f'Rewriting {notebook}')
            nbf.write(nb, notebook)


if __name__ == '__main__':
    parser = ArgumentParser(description="Replace markdown image links with "
                                        "HTML image tags.")

    parser.add_argument('folder', nargs='?', default='.',
                        help="Folder in which to search for notebooks to "
                             "convert tags in")
    args = parser.parse_args()

    fix_notebooks_in_folder(args.folder)
