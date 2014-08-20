#! /usr/bin/env python
# download_webpage.py
# David Prager Branner
# 20140801, works

import subprocess
import os
import time
import sys
import move_file
import importlib
import make_date

"""Run script to download webpage and report any changed content."""

def main():
    # Get base name of file to save.
    if os.path.exists('name_to_save_as.ignore'):
        with open('name_to_save_as.ignore', 'r') as f:
            name_to_save_as = f.read()
    else:
        # Get path only of URL.
        if len(sys.argv) > 1:
            url_file = sys.argv[1] + '.ignore'
        else:
            url_file = 'url.ignore'
        try:
            with open(url_file, 'r') as f:
                url = f.read()
        except:
            print('''Neither 'name_to_save_as.ignore' nor'''
                    ''' "''' + url_file + '''" found.\nExiting.''')
            sys.exit()
        name_to_save_as = url.split('/')[-1].split('.')[0]
    #
    # Run script.
    s = ['osascript', 'safari_download_webpage.scpt']
    subprocess.check_output(s, stderr=subprocess.STDOUT)
    while not os.path.exists(name_to_save_as):
        time.sleep(.5)
    # Get current date as string; use to rename file.
    the_date = make_date.make_date()
    filename = name_to_save_as +  '_' + the_date + '.ignore'
    os.rename(name_to_save_as, filename)
    #
    # Extract and return changed content.
    print('Content unchanged?', end=' ')
    content = move_file.move(filename)
    if not content:
        sys.exit()
    # If an extraction program has been named, use it.
    if len(sys.argv) > 2:
        E = importlib.import_module(sys.argv[2])
        print(E.main(content))
    # Otherwise report only the change in file-size.
    else:
        # Store size only to ..._last_found_size.txt
        size = len(content)
        size_filename = name_to_save_as + '_last_found_size.ignore'
        try:
            with open(size_filename, 'rb') as f:
                last_size = int(f.read())
        except FileNotFoundError:
            print('No previous file {} found.'.format(size_filename))
            last_size = 0
        with open(size_filename, 'w') as f:
            f.write(str(size))
        print('Change in size: {}'.format(size - last_size))

if __name__ == '__main__':
    main()
