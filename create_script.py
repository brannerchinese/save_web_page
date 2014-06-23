#! /usr/bin/env python
# create_script.py
# David Prager Branner
# 20140623

import os
import sys

script_text = 'safari_save_page_script.txt'
script_name = 'safari_save_page.scpt'
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
    contents = contents.replace('URL here', url)
    with open(script_name, 'w') as f:
        f.write(contents)
    print('File {} created.'.format(script_name))
