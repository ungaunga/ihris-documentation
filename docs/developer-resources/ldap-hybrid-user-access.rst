LDAP Hybrid User Access
=======================

The is an authentication mechanism which authenticates users against an LDAP server and stores the role in the database.  It does not create an administrative account on module initialization on the LDAP server, however it uses an internal administrative account 'i2ce_admin' with password as defined below.  It is designed so that default values will work well with authenticating against a read-only active directory server.

This user access mechanism  is implemented by the [[Class: I2CE UserAccess LDAP DB | I2CE_UserAccess_LDAP_DB]] class.

Configuration
^^^^^^^^^^^^^

To use the default user authentication, you need to enable the module and set an initialization string.

Enabling the Module
~~~~~~~~~~~~~~~~~~~
To enable, just make sure you have:

.. code-block:: xml

     <requirement name='UserAccess_LDAP_Hybrid'>
       <atLeast version='4.0'/>
       <lessThan version='4.1'/>
     </requirement>
    

Initialization String
~~~~~~~~~~~~~~~~~~~~~

The initialization string is sent to I2CE::initialize() in the index.php as the fourth argument, *$user_access_init* .  This string must be prefixed with the '''LDAP://''.  What follows take any of the following formats:

* null:  The is the default value and means that we use the default DN (distinguished name) for querying and authenticating users
* a JSON encoded string: The data to  is a JSON enocode string of optional configuration value for the user access.  The JSON encoded data has the following keys:
* *userDB:  The name of the database where the *user_table*  table lies.  Defaults to current database
* *user_table: Defaults to 'user_ldap' the table where user roles and id's are stored
* *host: Defaults to 'localhost'  The hostname where the openLDAP server lives
* *port: The port openLDAP is listening on. Defaults to 389
* *ldap_user: The user to attempt to bind the ldap connection to.  Defaults to in which case we we do an anonymous connection
* *ldap_pass: The password to attempt to bind the ldap connection with.
* *ldap_user_dn: The dn to bind the ldap_user against.  If not set, then the value of dn below is used
* *dn: The DN used to query against.  Defaults to 'dc=localhost'
* *people: The oranzataional unit under which users live.  Defaults to 'ou=People'.
* *person_comp: The qualifier to query people against.  Defaults to 'uid'
* *person_objectClass: defaults to 'inetOrgPerson'
* *password_field: the field the user's password is stored.  Defaults to 'userPassword'
* *encrypt:  how the password is stored on the openLDAP server. Default is bind.   Possible values are:
* **'bind' authentication is through a bind to the ldap server
* **'plaintext'
* **'SHA'
* **'SSHA'
* **'MD5'
* *salt: the salt to use for encryption (if needed).  Defaults to none.
* *p_details: associative array of the user details that are querriable against People.Defaults as follows:
* **email:mail
* **commonname:cn
* **locale:Preferred Local
* *p_detail_names: associative array of the display names of user details that are querriable against People.Defaults as follows:
* **commonname:Common Name
* **email:E-mail
* **locale:preferredLanguage
* *can_change_pass: defaults to false
* *can_create_user: defaults to false
* *can_edit_user_details: defaults to false
* *can_edit_role: defaults to true
* *admin_user: The LDAP internal (not stored on LDAP) username for an administrative account. If not set, it uses 'i2ce_admin'
* *admin_pass: It is the password for an administrative account with username 'administrator'. This account is not authenticated against LDAP.  If this value is not set, it is the same password used for the database connection.
* *admin_details: associative array of the details for the admin user.  Defaults to be as follows:
* **email: root@localhost
* **locale: en_US
* **commonname: SysAdmin

For example:
 LDAP_DB://
would be a minimal initialization string needed to authenticate against.  For the examples below, you would use:
  LDAP_DB://{"dn": "dc=moh,dc=example,dc=org"}

LDAP Directory Structure
^^^^^^^^^^^^^^^^^^^^^^^^

Passwords
~~~~~~~~~
We will use SHA and salted SSHA.  For a php implementation  `see this <http://www.php.net/manual/en/function.sha1.php#40226>`_  and  `this <http://www.openldap.org/faq/data/cache/347.html>`_ 

