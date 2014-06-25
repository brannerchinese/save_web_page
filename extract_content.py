#! /usr/bin/env python
# extract_content.py
# David Prager Branner
# 20140624, works

import bs4
import ast

def extract(filename):
    """From a downloaded HTML file produce a list of entity-names."""
    with open(filename, 'r') as f:
        content = f.read()
    soup = bs4.BeautifulSoup(content)
    x = soup.body.div.next_siblings
    x = list(x)[1]
    x = x.div.next_siblings
    # len(list(x)) = 5
    x = list(x)[3]
    # len(list(x)) = 7
    # x.ul is list of entities, with names as child-strings.
    names = set([x.strip() for item in x.ul
            if type(item) != bs4.NavigableString
            for x in item.find('text')])
    with open('last_found_names.txt', 'r') as f:
        last_found_names = ast.literal_eval(f.read())
    if last_found_names == names:
        answer = True
    else:
        with open('last_found_names.txt', 'w') as f:
            f.write(str(names))
            answer = False
    return answer, names.difference(last_found_names)
