Single User Access
==================

The is an authentication mechanism which authenticates users against a single user.  It is present in version **4.1**  of iHRIS. It uses an internal administrative account 'i2ce_admin' with password as defined below, as well a single user.  This can be useful for a "Demonstration" or a "Stand-Alone" application. 

This user access mechanism  is implemented by the [[Class: I2CE UserAccess Single | I2CE_UserAccess_Single]] class.


Enabling the Module
^^^^^^^^^^^^^^^^^^^
To enable, just make sure you have:


.. code-block:: xml

     <requirement name='UserAccess_LDAP_Hybrid'>
       <atLeast version='4.0'/>
       <lessThan version='4.1'/>
     </requirement>
    



Initialization String
^^^^^^^^^^^^^^^^^^^^^

The initialization string is sent to I2CE::initialize() in the index.php as the fourth argument, *$user_access_init* .  This string must be prefixed with the '''Single://''.  What follows take any of the following formats:


* null:  The is the default value and means that we use the defaults below
* a JSON encoded string: The data to  is a JSON enocode string of optional configuration value for the user access.  The JSON encoded data has the following keys:



* *admin_user: The username for an administrative account. If not set, it uses 'i2ce_admin'
* *admin_pass: It is the password for an administrative account with username 'admin_user'. T  If this value is not set, it is the same password used for the database connection.
* *admin_details: associative array of the details for the admin user.  Defaults to be as follows:
* **email: root@localhost
* **locale: en_US
* *auto_login:  defaults to 0 (false).  If true we will do an autologin of the specified user
* *auto_login_user: The user we wish to login with
* *username: the username for the single user (can be the same as that set by admin_user).  Defaults to guest
* *userrole: the role of the single user
* *usedid:  the id for the user.  defaults to 1
* *user_details: associative array of the details for the admin user.  Defaults to be as follows:
* **email: root@localhost
* **locale: en_US
* **firstname: (Empty)
* **lasttname: (Empty)



Example
^^^^^^^
The following would do an auto login of a guest user with the planner role
  Single://{"auto_login":1, "auto_login_user":guest ,"userrole": "planner", "userdetails" :{"lastname","Health Workforce Planner"}}

[[Category:Developer Resources]]
