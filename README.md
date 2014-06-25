## Download Webpage

Check for changes on a page from a protected website to which you can log in. (Apple OS 10, only.)

This is a workaround using AppleScript and Safari, when programmatic log-in is complicated because of CSRF protections and authentication protocols. Your authentication information is not used, and no files having the same names as the data-files involved are present in this repository (in fact, they are excluded in the `.gitignore` file).

### To run

This is a Python3 project. No special modules are needed for the main programs, but `bs4` (BeautifulSoup4) is needed for the optional `extract_content.py` program.

We first generate a script using content the user supplies, then run the script to open a webpage and download it to disk. Finally, if desired, we extract the desired content using an HTML parser.

 1. Prepare the AppleScript.
   2. Save the URL to a text file called `url.ignore`. (The `.ignore` is marked in to be ignored in `.gitignore`.) The program will exit if this file is not found.
   2. Run the program `create_script.py`; it will generate the script `safari_save_page.scpt` using the URL you have specified.
 1. Log into the website with Safari, using your credentials for the site in question. This step is unconnected to the running of the programs here, but it must be done so that the browser will supply your cookie information to the site.
 1. Run the AppleScript (this section can be done repeatedly, as needed).
   2. Save the base name to be used for downloaded files to `name_to_save_as.ignore`. If this file is not found, then the "path" (the last section before the `.html` extension) of the URL will be used. If neither is found, the program exits.
   2. In order to ensure correct permissions for writing the webpage, and to make it executable from the command line, set

        ```
sudo chown root download_webpage.py
sudo chmod a+x download_webpage.py
        ```

     Then run as

        ```
./download_webpage.py
        ```

     Note that if you don't have root privileges, you will not be able to run either this program or (independently) the script.
     
     The program should open Safari, load and then download the page you have specified, close Safari, and rename the page with the current date and time.
 1. Extract any desired information and compare with the previously downloaded version.
   2. For some users it may be enough simply to run a `diff` on two different downloads of the same file, or even to compare them visually. In my own case, I needed to extract the principal content of the page. For this purpose, a program `extract_content.py` is supplied. It is called from within `download_webpage.py` and prints the content I am looking for. Users can alter this file for their own purposes; those who don't need this material can remove the last line of `download_webpage.py`.
   2. Program `extract_content.py` compares the just-downloaded content to the data saved from the previous download, if found, and then moves the downloaded file to a directory `saved_downloads`. If the new data is different from the old, return the added material and save the new data for the next run.

[end]
