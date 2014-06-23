## Download webpage

Download a page from a site to which you can log in. (Apple OS 10.)

This is an AppleScript workaround when programmatic log-in is too complicated because of CSRF protections and authentication protocols. 

### To run

This is a Python3 program. No special modules are needed.

 1. Prepare the AppleScript.
   2. Save the URL to a text file called `url.ignore`. (The `.ignore` is marked in to be ignored in `.gitignore`.)
   2. Save the base name to be used for downloaded files to `name_to_save_as.ignore`. If this file is not found, then the "path" (the last section before the `.html` extension) of the URL will be used.
 1. Run the AppleScript (this section can be done repeatedly, as needed).
   2. Log in with Safari, using your credentials for the site in question.

**Incomplete.**

[end]
