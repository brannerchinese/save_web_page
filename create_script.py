#! /usr/bin/env python
# create_script.py
# David Prager Branner
# 20140702, works

import os
import sys

script_text = 'safari_download_webpage_script.txt'
script_name = 'safari_download_webpage.scpt'
if len(sys.argv) > 1:
    url_file = sys.argv[1] + '.ignore'
else:
    url_file = 'url.ignore'
if os.path.exists(script_name):
    print('File {} already exists; exiting.'.format(script_name))
    sys.exit()
if not os.path.exists(url_file):
    print('File {} not found; exiting.'.format(url_file))
    sys.exit()
else:
    with open(script_text, 'r') as f1, open(url_file, 'r') as f2:
        contents = f1.read()
        url = f2.read()
    if os.path.exists('name_to_save_as.ignore'):
        with open('name_to_save_as.ignore', 'r') as f:
            name_to_save_as = f.read()
    else:
        # Get path only of URL.
        name_to_save_as = url.split('/')[-1].split('.')[0]
    contents = contents.replace('URL here', url)
    contents = contents.replace('PATH here', name_to_save_as)
    with open(script_name, 'w') as f:
        f.write(contents)
    print('File {} created.'.format(script_name))
