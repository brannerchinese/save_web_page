## Download webpage

Download a page from a site to which you can log in.

This is a workaround when programmatic log-in is too complicated because of CSRF protections and authentication protocols. 

### To run

This is a Python3 program. No special modules are needed.

 1. Log in with Safari, using your credentials for the site in question.
 1. Save the URL to a text file called `url.ignore`. (The `.ignore` is marked in to be ignored in `.gitignore`.)
 1. Save the base name to be used for downloaded files to `name_to_save_as.ignore`. If this file is not found, then the "path" (the last section before the `.html` extension) of the URL will be used.

**Incomplete.**

[end]
