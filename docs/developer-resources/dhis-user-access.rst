DHIS User Access
================================================

The is an authentication mechanism which authenticates users against the DHIS2 style authentication mechansim


This user access mechansim  is implemented by the [[Class: I2CE_UserAccess_DHIS | I2CE_UserAccess_DHIS]] class.

Configuration
^^^^^^^^^^^^^

To use the default user authentication, you need to enable the module and set an initialization string.


Enabling the Module
~~~~~~~~~~~~~~~~~~~
To enable, just make sure you have:


.. code-block:: xml

     <requirement name='UserAccess_DHIS'>
       <atLeast version='4.0'/>
       <lessThan version='4.1'/>
     </requirement>
    



Initialization String
~~~~~~~~~~~~~~~~~~~~~

The initialization string is sent to I2CE::initialize() in the index.php as the fourth argument, *$user_access_init*.  This string must be prefixed with the '''DHIS://''.  What follows take any of the following formats:


* null:  The is the default value and means that we use the default tables (below) within the current database
* a non JSON-encoded string:  For example 'dhis.' Then this is the name of the database that the *users* and *usersinfo*  tables reside in.
* a JSON encoded string: The data to  is a JSON enocode string of optional configuration value for the user access.  The JSON encoded data has the following keys:
* *userDB: The name of the database where the *users* and *userinfo* tables lie
* *passTable: An alternate table to use instead of *users* .  If set, it does not use the value of userDB
* *detailTable: An alternate table to use instead of *userinfo*  If set, it does not use the value of userDB
* *logTable:  An alternate table to use instead of *user_log_dhis*
* *accessTable: An alternate table to use instead if *access_dhis*

For example:
 DHIS://dhis_database_name
would be a minimal initialization string needed to authenticate against.


Database Structure
^^^^^^^^^^^^^^^^^^

It uses the following tables in your database:


* access_dhis.  The table which associates a user's id to its role.  It has the following columns:
* *user: int(11)
* *role: varchar(255)
* users  The list of all user's known to DHIS and the iHRIS Suite.  It has the following columsn:
* *id: int(11)
* *username: varchar(20)
* *password: varchar(50)



* userinfo  The details all user's known to DHIS and the iHRIS Suite.  It has the following columns:
* *id: int(11)
* *firstname: varchar
* *lastname: varchar
* *email: varchar
* *phone: varchar

In addition, the table **user_log_dhis** keeps track of the user activity.

[[Category:Developer Resources]]
