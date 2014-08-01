#! /usr/bin/env python
# move_file.py
# David Prager Branner
# 20140801

"""Read file and move out of the way."""

import os
import shutil

def retrieve(filename):
    """Return content of file."""
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print('File {} not found.'.format(filename))
        content = None
    return content

def move(filename):
    """Move file and return its content."""
    content = retrieve(filename)
    if not os.path.exists('saved_downloads'):
        os.mkdir('saved_downloads')
    try:
        shutil.move(filename, 'saved_downloads')
    except shutil.Error as e:
        print('File {} could not be saved. Error:\n    {}.'.
            format(filename, e))
        content = None
#    print('Content saved to file `saved_downloads/' + filename + '`.\n')
    return content

