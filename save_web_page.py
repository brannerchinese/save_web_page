#! /usr/bin/env python
# save_web_page.py
# David Prager Branner
# 20140623

import subprocess
import os
import datetime
import time

# Get base name of file to save
with open('name_to_save_as.ignore', 'r') as f:
    name_to_save_as = f.read()
# Run script.
s = ['osascript', 'safari_save_page.scpt']
# s = ['sudo', 'osascript', 'safari_save_page.scpt']
x = subprocess.check_output(s, stderr=subprocess.STDOUT)
while not os.path.exists(name_to_save_as + '.html'):
    time.sleep(.5)
# Get current date as string.
date_and_time = datetime.datetime.today()
the_date = date_and_time.strftime('%Y%m%d-%H%M')
# Rename and move.
os.rename(name_to_save_as + '.html', 
        name_to_save_as +  '_' + the_date + '.ignore')

