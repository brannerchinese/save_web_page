#! /usr/bin/env python
# move_file.py
# David Prager Branner
# 20140702

"""Read file and move out of the way."""

import os
import shutil

def move(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
    except FileNotFoundError:
        print('File {} not found.'.format(filename))
        return None
    if not os.path.exists('saved_downloads'):
        os.mkdir('saved_downloads')
    try:
        shutil.move(filename, 'saved_downloads')
    except shutil.Error as e:
        print('File {} could not be saved. Error:\n    {}.'.
            format(filename, e))
        return None
    print('Content saved to file `saved_downloads/' + filename + '`.\n')
    return content
