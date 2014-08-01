#! /usr/bin/env python
# extract.py
# David Prager Branner
# 20140801

"""Report whether the list of names is changed or not."""

import bs4
import ast
import shutil
import os
import move_file

def main(content, filename='last_found_names.ignore'):
    names = extract(content)
    difference = compare(names, filename)
    if difference:
        return False, difference
    else:
        return True

def extract(content):
    """From a downloaded HTML file produce a list of entity-names."""
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
    return names

def compare(names, filename):
    """Report difference between content of `names` and `filename`."""
    # Compare to previously found data.
    content = move_file.retrieve(filename)
    if content:
        last_found_names = ast.literal_eval(content)
    else:
        last_found_names = set()
    # We use `difference` to show what is in `names` because we assume that
    # `names` is more often the newer data.
    difference = names.difference(last_found_names)
    if difference:
        with open(filename, 'w') as f:
            f.write(str(names))
    return difference
