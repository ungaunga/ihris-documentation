Magic Data Storage Mechanisms
=============================

Magic data provides a central mechanism for configuring iHRIS.  This magic data is stored in a database table.  Due to frequent access of the data, a caching mechanism is needed to keep the database load down.  For this reason, several magic data storage mechanisms have been created.

You can add database storage mechanisms to I2CE_MagicData.  The last one that is added is the "permanent" storage mechanism methods.  All others that are added are used to cache the data stored in the permanent storage mechansim.

==Database==
This magic data storage mechanism is intended to be used as the "permanent" storage mechanism.  By default it is stored into the database table 'config'

==APC==
There is magic data storage mechanism based on the Pear APC module and implemented by the class I2CE_MagicDataStorageAPC.  It caches data in the memory segment between reqeusts with a timeout of 5 minutes.  Data cached by Apache is not cached on the command line.

To clear the cache manually you can use php-apc web interface.

==Memcached==
This is an in-memory cache of key-value pairs with limits of 1MB for value size.

==SysV==
This magic data storage mechanism is no longer being maintained.

There is magic data storage mechanism based on SysV I2CE_MagicDataStorageSysV.  It is not available in windows. It creates shared memory segments to cache the data between requests.  It's advantage over APC is that the same shared segments can be accessed via the command line.  There is no time-out for the data stored.

To clear manually from the command line the shared memory segments
 ipcs -m | grep www-data | awk '{print "ipcrm -m "$2}' | sudo bash
[[Category:Magic Data]][[Category:Review2013]]
