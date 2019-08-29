Magic Data Storage -- SysV
==========================

To clear from the command line the shared memory segments
 ipcs -m | grep www-data | awk '{print "ipcrm -m "$2}' | sudo bash
[[Category:Magic Data]]
