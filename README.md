## Download Webpage

Check for changes on a page from a protected site to which you can log in. (Apple OS 10.)

This is a  workaround using AppleScript and Safari, when programmatic log-in is complicated because of CSRF protections and authentication protocols. 

### To run

This is a Python3 program. No special modules are needed.

 1. Prepare the AppleScript.
   2. Save the URL to a text file called `url.ignore`. (The `.ignore` is marked in to be ignored in `.gitignore`.) The program will exit if this file is not found.
   2. Run the program `create_script.py`; it will generate the script `safari_save_page.scpt` using the URL you have specified.
 1. Run the AppleScript (this section can be done repeatedly, as needed).
   2. Save the base name to be used for downloaded files to `name_to_save_as.ignore`. If this file is not found, then the "path" (the last section before the `.html` extension) of the URL will be used. If neither 
   2. Log in with Safari, using your credentials for the site in question.
   2. In order to ensure correct permissions for writing the webpage, and to make it executable from the command line, set

        ```
sudo chown root download_webpage.py
sudo chmod a+x download_webpage.py
        ```

     Then run as

        ```
./download_webpage.py
        ```

     Note that if you don't have root privileges, you will not be able to run this program.
     
     The program should open Safari, load and then download the page you have specified, close Safari, and rename the page with the current date and time.
 1. Compare with the previously downloaded version.

**Incomplete.**

[end]
