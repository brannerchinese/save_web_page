#! /usr/bin/env python
# download_webpage.py
# David Prager Branner
# 20140623

import subprocess
import os
import datetime
import time
import sys
import extract_content as E

# Get base name of file to save.
if os.path.exists('name_to_save_as.ignore'):
    with open('name_to_save_as.ignore', 'r') as f:
        name_to_save_as = f.read()
elif os.path.exists('url.ignore'):
    # Get path only of URL.
    with open('url.ignore', 'r') as f:
        url = f.read()
        name_to_save_as = url.split('/')[-1].split('.')[0]
else:
    print('''Neither 'name_to_save_as.ignore' nor'''
            ''' 'url.ignore' found.\nExiting.''')
    sys.exit()
#
# Run script.
s = ['osascript', 'safari_download_webpage.scpt']
subprocess.check_output(s, stderr=subprocess.STDOUT)
while not os.path.exists(name_to_save_as):
    time.sleep(.5)
# Get current date as string; use to rename file.
date_and_time = datetime.datetime.today()
the_date = date_and_time.strftime('%Y%m%d-%H%M')
filename = name_to_save_as +  '_' + the_date + '.ignore'
os.rename(name_to_save_as, filename)
#
# Extract desired content.
print(E.extract(filename))
