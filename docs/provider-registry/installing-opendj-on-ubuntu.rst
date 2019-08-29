Installing OpenDJ On Ubuntu
===========================

=Installation=

Prerequisites
^^^^^^^^^^^^^
We are going to install OpenDJ on Ubuntu 12.04 from a command line.
Like ApacheDS, OpenDJ also requires a Java environment to run. OpenDJ requires at least Java version 6.0 installed on the machine that it is going to run.

Downloading OpenDJ software
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The software can be downloaded from the  `OpenDJ download page <http://www.forgerock.org/opendj.html>`_ . We are going to download the most recent version 2.5.

Installing OpenDJ
^^^^^^^^^^^^^^^^^

We are going to install OpenDJ in the **/opt**  directory of our system. So we will create the OpenDJ installation directory here

.. code-block::

    sudo mkdir -p /opt/OpenDJ
    sudo chown -R `whoami`:`whoami` /opt/OpenDJ
    

Download and unzip OpenDJ by running the following commands from the terminal

.. code-block::

    cd /opt/OpenDJ
    wget http://download.forgerock.org/downloads/opendj/2.5.0-Xpress1/OpenDJ-2.5.0-Xpress1.zip
    unzip OpenDJ-2.5.0-Xpress1.zip
    mv OpenDJ-2.5.0-Xpress1 2.5.0
    cd 2.5.0
    

To install OpenDJ in interactive mode, run the setup --cli from the terminal 

 **Note:**  you will have to remember the password you set in [xxxx] as it is the one you'll be using to access the server

.. code-block::

    $ /opt/OpenDJ/2.5.0/./setup --cli
     
    OpenDJ 2.5.0
    Please wait while the setup program initializes...
     
    What would you like to use as the initial root user DN for the Directory
    Server? [cn=Directory Manager]: [cn=admin ENTER]
    Please provide the password to use for the initial root user:[xxxx]
    Please re-enter the password for confirmation:[xxxx]
     
    Provide the fully-qualified directory server host name that will be used when
    generating self-signed certificates for LDAP SSL/StartTLS, the administration
    connector, and replication [sovello-1x88]: [ENTER]
     
    On which port would you like the Directory Server to accept connections from
    LDAP clients? [1389]: [ENTER]
     
    On which port would you like the Administration Connector to accept
    connections? [4444]: [ENTER]
     
    Do you want to create base DNs in the server? (yes / no) [yes]
     
    Provide the base DN for the directory data: [dc=moh,dc=gov,dc=rw]
    Options for populating the database:
     
        1)  Only create the base entry
        2)  Leave the database empty
        3)  Import data from an LDIF file
        4)  Load automatically-generated sample data
     
    Enter choice [1]: [1] (As we don't have to load anything now, all data will be loaded later)
     
    Please specify the path to the LDIF file containing the data to import: [ENTER]
     
    Do you want to enable SSL? (yes / no): [no]
     
    Do you want to enable Start TLS? (yes / no): [no]
     
    Do you want to start the server when the configuration is completed? (yes /no): [yes]
     
     
    Setup Summary
    =============
    LDAP Listener Port:            1389
    Administration Connector Port: 4444
    LDAP Secure Access:            disabled
    Root User DN:                  cn=admin
    Directory Data:                Create New Base DN dc=moh,dc=gov,dc=rw.
    Base DN Data: Only Create Base Entry (dc=moh,dc=gov,dc=rw)
    
    Start Server when the configuration is completed
    
    
    What would you like to do?
    
        1)  Set up the server with the parameters above
        2)  Provide the setup parameters again
        3)  Print equivalent non-interactive command-line
        4)  Cancel and exit
    
    Enter choice [1]: [1]
    
    See /tmp/opendj-setup-3175331027381066326.log for a detailed log of this operation.
    
    Configuring Directory Server ..... Done.
    Creating Base Entry dc=moh,dc=gov,dc=rw ..... Done.
    Starting Directory Server ........ Done.
    
    To see basic server configuration status and configuration you can launch /opt/OpenDJ/2.5.0/bin/status
    

=Loading HPD schema and Provider schema to OpenDJ=

We are going to load the provider schema for RHEA and the schema for the HPD Profile.
We need to download the code for the Provider registry for Rwanda and then we will copy the schema files from there to OpenDJ.

.. code-block::

    cd /var/lib/iHRIS/
    bzr branch lp:rhea-pr
    cd /opt/OpenDJ/2.5.0/bin
    ./stop-ds
    cp /var/lib/iHRIS/rhea-pr/ldap/openldap/* /opt/OpenDJ/2.5.0/config/schema
    ./start-ds
    

=Loading Provider sample data=
You need to move to the bin directory of OpenDJ and execute these commands from the terminal

.. code-block::

    cd /opt/OpenDJ/2.5.0/bin
    ./stop-ds
    ./import-ldif -l /var/lib/iHRIS/rhea-pr/ldap/admin_pass.ldif --backendID userRoot --includeBranch cn=admin,dc=moh,dc=gov,dc=rw
    ./import-ldif -l /var/lib/iHRIS/rhea-pr/ldap/base_organizational_units.ldif --backendID userRoot --includeBranch dc=moh,dc=gov,dc=rw
    ./import-ldif -l /var/lib/iHRIS/rhea-pr/ldap/ihris_sample_export.ldif --backendID userRoot --includeBranch dc=moh,dc=gov,dc=rw
    ./start-ds
    

At any time you can check the status of OpenDJ LDAP server by running <pre>/opt/OpenDJ/2.5.0/bin/./status</pre>
When OpenDJ is running the output is like

.. code-block::

    sovello@sovello-1x88:~$ /opt/OpenDJ/2.5.0/bin/./status 
    
    
    >>>> Specify OpenDJ LDAP connection parameters
    
    Administrator user bind DN [cn=Directory Manager]: cn=admin
    
    Password for user 'cn=admin': 
    
              --- Server Status ---
    Server Run Status:        Started
    Open Connections:         1
    
              --- Server Details ---
    Host Name:                sovello-1x88
    Administrative Users:     cn=admin
    Installation Path:        /opt/OpenDJ/2.5.0
    Version:                  OpenDJ 2.5.0-Xpress1
    Java Version:             1.6.0_27
    Administration Connector: Port 4444 (LDAPS)
    
              --- Connection Handlers ---
    Address:Port : Protocol : State
    -------------:----------:---------
    --           : LDIF     : Disabled
    0.0.0.0:161  : SNMP     : Disabled
    0.0.0.0:636  : LDAPS    : Disabled
    0.0.0.0:1389 : LDAP     : Enabled
    0.0.0.0:1689 : JMX      : Disabled
    
              --- Data Sources ---
    Base DN:     dc=example,dc=com
    Backend ID:  exampleData
    Entries:     173
    Replication: Disabled
    
    Base DN:     dc=moh,dc=gov,dc=rw
    Backend ID:  userRoot
    Entries:     1964
    Replication: Disabled
    

and when stopped, the output looks like this one:

.. code-block::

    sovello@sovello-1x88:~$ /opt/OpenDJ/2.5.0/bin/./status 
    
              --- Server Status ---
    Server Run Status:        Stopped
    Open Connections:         <not available> (*)
    
              --- Server Details ---
    Host Name:                sovello-1x88
    Administrative Users:     cn=admin
    Installation Path:        /opt/OpenDJ/2.5.0
    Version:                  OpenDJ 2.5.0-Xpress1
    Java Version:             <not available> (*)
    Administration Connector: Port 4444 (LDAPS)
    
              --- Connection Handlers ---
    Address:Port : Protocol : State
    -------------:----------:---------
    --           : LDIF     : Disabled
    0.0.0.0:161  : SNMP     : Disabled
    0.0.0.0:636  : LDAPS    : Disabled
    0.0.0.0:1389 : LDAP     : Enabled
    0.0.0.0:1689 : JMX      : Disabled
    
              --- Data Sources ---
    Base DN:     dc=example,dc=com
    Backend ID:  exampleData
    Entries:     <not available> (*)
    Replication: Disabled
    
    Base DN:     dc=moh,dc=gov,dc=rw
    Backend ID:  userRoot
    Entries:     <not available> (*)
    Replication: Disabled
    
    * Information only available if server is running and you provide valid
    authentication information when launching the status command.
    
    

For help on any command in the bin directory you can run 

.. code-block::

    ./command_name --help for example
    ./import-ldif --help
    

=Installing OpenDJ DSML gateway=

Prerequisites
^^^^^^^^^^^^^
DSML need to run in Apache Tomcat. 
So we first need to install Apache Tomcat the most recent version is 7.
Run this command from the terminal 

.. code-block::

    sudo apt-get install tomcat7
    

Installing Tomcat this way doesn't need you to go set up the environment variables for it. dpkg takes care of all the stuff.
After it finishes you can access the Tomcat server from this url [http://localhost:8080 http://localhost:8080] in your browser.

If the installation was successful you should see a **It Works**  with some other details.

Downloading OpenDJ DSML gateway
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This OpenDJ DSML gateway runs independently of OpenDJ Directory server. It can be downloaded from the  `Archive of stable community releases page <http://www.forgerock.org/opendj-archive.html>`_ 

You can also download it from the command line.

.. code-block::

    wget http://download.forgerock.org/downloads/opendj/2.5.0-Xpress1/OpenDJ-2.5.0-Xpress1-DSML.war
    

Installing and Configuring
^^^^^^^^^^^^^^^^^^^^^^^^^^

The name of the **war**  needs to be changed to dsml.war.

Issue the following commands on the terminal to install/deploy the war file.

.. code-block::

    sudo service tomcat7 stop
    sudo cp path/to/dsml.war /var/lib/tomcat7/webapps/
    sudo service tomcat7 start
    

If it worked correctly, a folder **dsml**  will be created in /var/lib/tomcat7/webapps/'''dsml'''

For the DSML Gateway to work, the file WEB-INF/web.xml has to be edited. At minimum, the LDAP port number is to be the one you set during installation. (If need be, for HTTP Basic Auth and have the user IDs mapped to entries in the directory, for example, this has to be set to ldap.authzidtypeisid=true.) 

.. code-block::

    sudo pico /var/lib/tomcat7/webapps/WEB-INF/web.xml
    

Then edit this part

.. code-block::

      <context-param>
        <description>The port number of the OpenDJ server; e.g., 389</description>
        <param-name>ldap.port</param-name>
        <param-value>389</param-value>
      </context-param>
    

to

.. code-block::

      <context-param>
        <description>The port number of the OpenDJ server; e.g., 389</description>
        <param-name>ldap.port</param-name>
        <param-value>1389</param-value>
      </context-param>
    

Restart tomcat to take your changes into account.

.. code-block::

    sudo service tomcat7 restart
    

Testing OpenDJ DSML Gateway
^^^^^^^^^^^^^^^^^^^^^^^^^^^
To test DSML gateway we were to access [http://localhost:8080/dsml/DSMLServlet http://localhost:8080/dsml/DSMLServlet] however, the DSMLServlet url only accepts POST requests. so we would be presented with an error.

We can test the DSML Gateway using *Jxplorer* ' which we will need to install and run

.. code-block::

    sudo apt-get install jxplorer
    

After it finishes open it and then go to *File -> Connect*  or simply click the **Connect**  icon from the toolbar and fill in the details as seen from the picture below:

[[image:Jxplorer_parameters.png|center|JXplorer Parameters to access OpenDJ LDAP Server]]

If it works OK, we should see this screen.
[[image:Logged_in.png|center|Sample Data loaded on server]]

