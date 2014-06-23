#! /usr/bin/env python
# create_script.py
# David Prager Branner
# 20140623

import os
import contextlib

script_text = 'safari_save_page_script.txt'
script_name = 'safari_save_page.scpt'
url_file = 'url.ignore'
if not os.path.exists(script_name) and os.path.exists(url_file):
    with open(script_text, 'r') as f1, open(url_file, 'r') as f2:
        contents = f1.read()
        url = f2.read()
    contents = contents.replace('qqq', url)
    with open(script_name, 'w') as f:
        f.write(contents)
