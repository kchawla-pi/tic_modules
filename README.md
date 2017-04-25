# tic_modules
For The Imaging Collective (TIC): Module to ease addition of new modules to python path &amp; creating installable module packages.

Guiding objective:
Make it easier for tic members to build cleaner code.
Build a set of general purpose functions which can be reused.
Add documentation, for developers and end users.
Add redundancy: automatic file and path search and add, exception handling, helpful messaging.
-----Design outline-----

Module purpose:
Phase 1.
a. To automate the creation of tic packages.
b. To automate the addition of tic paths to sit-packages.
c. To automate Thesetting up and deployment of a mechanism for different tic releases)(virtual env are on possibility).

Phase 2.
a. To replace shell scripts with python scripts and functions.

1a. To automate the creation of tic packages.
Time allotted- 1week. Start:2017/04/12 End: 2017/04/19
[Overestimated ease of good implementation.]
------------------------------------------------------------------------------------------
Phase 1a. To automate the creation of tic packages --

Functions;

i) Path related. get_path.py

 - Get path entered by user at terminal. DONE 20170425
 - Check if path is relative or absolute. DONE 20170425
 - If relative, find the absolute path. DONE 20170425
 - Either way, check if abs path exists. DONE 20170425
 - Get cwd if no path. DONE 20170425
 - Optional args?? Later. DONE (2) 20170425
 - Sufficient documentation for collaboration. DONE 20170425
 - Modify to be used as import-able module. DESIGN PLANNING 20170425
 - Modify to easily accept file as input for batch commands. DESIGN PENDING 20170425

ii) if no path errors, walk tree RUDIMENTARY IMPLEMENTATION. ARCHIVED. 20170425

------------------------------------------------------------------------------------------




