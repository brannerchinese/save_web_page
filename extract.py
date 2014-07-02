#! /usr/bin/env python
# extract.py
# David Prager Branner
# 20140702

"""Extract content from a (certain but unnamed) HTML file."""

import bs4
import ast
import shutil
import os

def extract(filename):
    """From a downloaded HTML file produce a list of entity-names."""
    # Read file and move out of the way.
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        return None
    if not os.path.exists('saved_downloads'):
        os.mkdir('saved_downloads')
    shutil.move(filename, 'saved_downloads')
    # Parse and extract data
    soup = bs4.BeautifulSoup(content)
    x = soup.body.div.next_siblings
    x = list(x)[1]
    x = x.div.next_siblings # len(list(x)) = 5
    x = list(x)[3] # len(list(x)) = 7
    # x.ul is list of entities, with names as child-strings.
    names = set([x.strip() for item in x.ul
            if type(item) != bs4.NavigableString
            for x in item.find('text')])
    # Compare to previously found data.
    try:
        with open('last_found_names.ignore', 'r') as f:
            last_found_names = ast.literal_eval(f.read())
    except FileNotFoundError:
        last_found_names = set()
    if last_found_names == names:
        answer = True
    else:
        with open('last_found_names.ignore', 'w') as f:
            f.write(str(names))
            answer = False
    return answer, names.difference(last_found_names)
