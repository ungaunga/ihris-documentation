LDAP User Access
================

The is an authentication mechanism which authenticates users against an LDAP server and stores the role in the server.  It does not create an administrative account on module initialization on the LDAP server, however it uses an internal administrative account 'i2ce_admin' with password as defined below.

This user access mechanism  is implemented by the [[Class: I2CE UserAccess LDAP | I2CE_UserAccess_LDAP]] class.

Configuration
^^^^^^^^^^^^^

To use the default user authentication, you need to enable the module and set an initialization string.


Enabling the Module
~~~~~~~~~~~~~~~~~~~
To enable, just make sure you have:


.. code-block:: xml

     <requirement name='UserAccess_LDAP'>
       <atLeast version='4.0'/>
       <lessThan version='4.1'/>
     </requirement>
    



Initialization String
~~~~~~~~~~~~~~~~~~~~~

The initialization string is sent to I2CE::initialize() in the index.php as the fourth argument, *$user_access_init* .  This string must be prefixed with the '''LDAP://''.  What follows take any of the following formats:


* null:  The is the default value and means that we use the default DN (distinguished name) for querying and authenticating users
* a JSON encoded string: The data to  is a JSON enocode string of optional configuration value for the user access.  The JSON encoded data has the following keys:
* *host: Defaults to 'localhost'  The hostname where the openLDAP server lives
* *port: The port openLDAP is listening on. Defaults to 389
* *ldap_user: The user to attempt to bind the ldap connection to.  Defaults to 'admin'. If empty we do an anonymous connection
* *ldap_pass: The password to attempt to bind the ldap connection with. If this value is not set, it is the same password used for the database connection.
* *ldap_user_dn: The dn to bind the ldap_user against.  If not set, then the value of dn below is used
* *dn: The DN used to query against.  Defaults to 'dc=localhost'
* *people: The oranzataional unit under which users live.  Defaults to 'ou=People'.
* *person_comp: The qualifier to query people against.  Defaults to 'cn'
* *person_objectClass: defaults to 'inetOrgPerson'
* *password_field: the field the user's password is stored.  Defaults to 'userPassword'
* *encrypt:  how the password is stored on the openLDAP server. Default is SHA.   Possible values are:
* **'bind' authentication is through a bind to the ldap server
* **'plaintext'
* **'SHA'
* **'SSHA'
* **'MD5'
* *salt: the salt to use for encryption (if needed).  Defaults to none.
* *p_details: associative array of the user details that are querriable against People.Defaults as follows:
* **firstname:givenName
* **lastname:sn
* **email:mail
* **commonname:cn
* **locale:Preferred Local
* *p_detail_names: associative array of the display names of user details that are querriable against People.Defaults as follows:
* **firstname:Firstname
* **lastname:Surname
* **commonname:Common Name
* **email:E-mail
* **locale:preferredLanguage
* *can_change_pass: defaults to true
* *can_create_user: defaults to true
* *can_edit_user: defaults to true
* *admin_user: The LDAP internal (not stored on LDAP) username for an administrative account. If not set, it uses 'i2ce_admin'
* *admin_pass: It is the password for an administrative account with username 'administrator'. This account is not authenticated against LDAP.  If this value is not set, it is the same password used for the database connection.
* *admin_details: associative array of the details for the admin user.  Defaults to be as follows:
* **firstname: System
* **lastname: Administrator
* **email: root@localhost
* **locale: en_US
* **commonname: Admin
* *apps: The oragnaization unit for apps. Defaults to 'Application'
* *app: The application name used to check for user roles in.  If not set, it will use the site module's name
* *roles: The qualifier to query user roles against.  Defaults to 'Roles'.
* *ids: The qualifier to query user roles against.  Defaults to 'Ids'.

For example:
 LDAP://
would be a minimal initialization string needed to authenticate against.  For the examples below, you would use:
  LDAP://{"dn": "dc=moh,dc=example,dc=org"}


LDAP Directory Structure
^^^^^^^^^^^^^^^^^^^^^^^^

Example Entries
~~~~~~~~~~~~~~~
A user could be represented as:
    
    dn: uid=litlfred, ou=People, dc=moh,dc=example,dc=gov
    sn: Leitner
    givenName: Carl
    cn: Carl Leitner
    userPassword: {SSHA}DkMTwBl+a/3DQTxCYEApdUtNXGgdUac3
    email: cleitner@intrahealth.org





User roles be unique on the pair (username, software-component)
and there may be software component specific information to share,

    dn: uid=litlfred, cn=ihris-manage, ou=Application, dc=moh,dc=example,dc=gov
    role: hr_staff
    appid: 25
    #preferred locale is specific to ihris-manage based on the available locales
    locale: he_IL
    locale: en_US
    
    dn: uid=litlfred, cn=ihris-qualify, ou=Application, dc=moh,dc=example,dc=gov
    role: admin
    appid: 25
    #preferred locale is specific to ihris-qualify based on the available locales
    locale: en_US
  
    dn: uid=litlfred, cn=dhis2, ou=Application, dc=moh,dc=example,dc=gov
    role: guest
    appid: 42


Passwords
~~~~~~~~~
We will use SHA and salted SSHA.  For a php implementation  `see this <http://www.php.net/manual/en/function.sha1.php#40226>`_  and  `this <http://www.openldap.org/faq/data/cache/347.html>`_ 


openLDAP Server Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This describes how to set up openLDAP for use with openMRS, DHIS and iHIS on an ubuntu machine. First, see  `this <https://help.ubuntu.com/8.04/serverguide/C/openldap-server.html>`_  tutorial.


Install slapd
~~~~~~~~~~~~~
Here are the steps I followed:
 sudo apt-get install slapd ldap-utils

 sudo dpkg-reconfigure slapd


* choose to Omit OpenLDAP server configuration?: No
* DNS Domain Name: moh.example.gov
* Organization Name: moh.example.gov
* Choose HDB as the storage format
* Do you want the database to be removed...: no
* set the admin password to XXXXX.  This should be set in the initialization string above
* allow LDAPv2: no
 
Now, let us make openLDAP only listen on  `localhhost <http://www.linuxquestions.org/questions/linux-server-73/openldap-listen-on-localhost-662589/>`_ 
 sudo gedit /etc/default/slapd
and specify:
 SLAPD_SERVICES="ldap://127.0.0.1:389/"
then restart
 sudo /etc/init.d/slapd restart


Once Initialized
~~~~~~~~~~~~~~~~

In our scenario above initializing the UserAccess_LDAP module we will have:


.. code-block:: text

    dn: dc=localhost
    objectClass: top
    objectClass: dcObject
    objectClass: organization
    o: localhost
    dc: localhost
    
    dn: cn=admin,dc=localhost
    objectClass: simpleSecurityObject
    objectClass: organizationalRole
    cn: admin
    description: LDAP administrator
    
    dn: ou=People,dc=localhost
    objectClass: organizationalUnit
    ou: People
    
    dn: ou=Application,dc=localhost
    objectClass: organizationalUnit
    ou: Application
    
    dn: ou=ihris-manage-site-demo,ou=Application,dc=localhost
    objectClass: organizationalUnit
    ou: ihris-manage-site-demo
    
    dn: ou=Roles, ou=ihris-manage-site-demo, ou=Application,dc=localhost
    objectClass: organizationalUnit
    ou: Roles
    
    dn: ou=Ids, ou=ihris-manage-site-demo, ou=Application,dc=localhost
    objectClass: organizationalUnit
    ou: Ids
    


Here is a sample user with their role and id.



.. code-block:: text

    dn: uid=administrator,ou=People,dc=localhost
    givenName: Site
    sn: Administrator
    cn: Site Admin
    mail: administrator@example.com
    preferredLanguage: en_US
    objectClass: inetOrgPerson
    uid: administrator
    
    
    dn: ou=administrator,ou=Roles, ou=ihris-manage-site-demo,ou=Application,dc=localhost
    ou: administrator
    objectClass: applicationProcess
    cn: admin
    
    dn: ou=administrator,ou=Ids, ou=ihris-manage-site-demo,ou=Application,dc=localhost
    ou: administrator
    objectClass: applicationProcess
    cn: 1
    
    


[[Category:Developer Resources]]
