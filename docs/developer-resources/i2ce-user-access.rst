I2CE User Access
================

This is default authentication mechanism used by the iHRIS Suite. 


This user access mechansim  is implemented by the [[Class: I2CE_UserAccess | I2CE_UserAccess]] class.
==Configuration==

To use the default user authentication, you need to enable the module and possibly set an initialization string.

===Enabling the Module===
To enable, just make sure you have:
<source lang='xml'>
 <requirement name='UserAccess'>
   <atLeast version='4.0'/>
   <lessThan version='4.1'/>
 </requirement>
</source>

===Initialization String===

The initialization string is sent to I2CE::initialize() in the index.php as the fourth argument, ''$user_access_init''.  This string is designed to be backwards compatible with the I2CE::intialize() method prior to version 4.0.3 and can take any of the following formats:
*null:  The is the default value and means that we use the default tables (below) within the current database
*a JSON encoded string: The data to  is a JSON enocode string of optional configuration value for the user access.  The JSON encoded data has the following keys: 
**userDB: The name of the database where the ''user'' table lies
**detailTable: An alternate table to use instead of ''user'' 
**logTable:  An alternate table to use instead of ''user_log''
**accessTable: An alternate table to use instead if ''access''

==Database Structure==

It uses the following tables in your database:
*access.  The table which associates a user's id to its role.  It has the following columns:
**user: int(11)
**role: varchar(255)
*user  The list of all user's known to the iHRIS Suite.  It has the following columsn:
**id: int(11)
**username: varchar(20)
**password: varchar(50)
**firstname: varchar(50)
**lastname: varchar(100)
**email: varchar(100)
**creator: int(11)  the user id that created this account

In addition, the table '''user_log''' keeps track of the user activity.

[[Category:Developer Resources]]
