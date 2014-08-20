#! /usr/bin/env python
# move_file.py
# David Prager Branner
# 20140819

"""Read file and move out of the way."""

import os
import shutil
import sys

def retrieve(filename):
    """Return content of file."""
    try:
        with open(filename, 'rb') as f:
            content = f.read()
    except FileNotFoundError:
        print('File {} not found.'.format(filename))
        content = None
    except UnicodeDecodeError:
        print('Unicode error in file {}.'.format(filename))
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
        print('''\n    File {} could not be saved. Error:'''
                '''\n    "{}."\n    Exiting.'''.format(filename, e))
        os.remove(filename)
        sys.exit()
    return content

