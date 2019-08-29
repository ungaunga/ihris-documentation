Building Meta Packages
======================

The meta packages, a set of iHRIS packages with the suffix <tt>-all</tt> are maintained in the  `ihris-meta <https://code.launchpad.net/~intrahealth+informatics/+junk/ihris-meta>`_  branch on Launchpad.

After checking them out use <tt>debuild -uc -us -b</tt> in each subdirectory to build the package.   Pay attention to the lintian output and make sure you've addressed or at least understand all the complaints.

[[Category:Developer Resources]]
