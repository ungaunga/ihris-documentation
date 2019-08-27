Installing Ghana Sites
================================================

This page contains installation instructions iHRIS Customized sites for Ghana.
{{otherversions|Linux (Ubuntu) Installation}}  
Instructions cover both: installing the **Central** (National) site and the **Regional** site.

The two files below

* [[Media:IHRIS_Decentralized_Implementation.odp | Decentralized iHRIS Implementation:]] Gives a high level overview of how iHRIS Manage can be implemented in a decentralized setting using different Data Models (''An OpenDocument Presentation'')
* [[Media:Creating_Standard_List_Modules.odp | Creating Standard List Modules:]] This is a hands on tutorial on how to create standardized data lists into modules by exporting them from the Magic Data Browser of iHRIS Manage. (''An OpenDocument Presentation'')

Before you start following up these instructions, please make sure your computer is installed with Ubuntu and all the required software for installing ''''iHRIS Suite'''' 

Depending on the version of iHRIS Suite you want to install, you can select it from `here <http://wiki.ihris.org/wiki/Linux_%28Ubuntu%29_Installation_%28versions%29>`_

 *Warning:* See [[Installing iHRIS on Ubuntu 10.4 (Lucid)]] after completing these instructions to get iHRIS working on the latest release of Ubuntu.

<center>'''Need help?'''  Try our [[Project Communication]]</center>

Getting Ready
^^^^^^^^^^^^^

Assuming that you are installing version `4.0.19 <http://wiki.ihris.org/wiki/Linux_%28Ubuntu%29_Installation_-_4.0.19>`_, you should follow the procedures on the page up to downloading the software.


Downloading the Software
^^^^^^^^^^^^^^^^^^^^^^^^
To download the software you enter these commands:


.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/lib/4.0.19
    cd /var/lib/iHRIS/lib/4.0.19
    sudo wget http://launchpad.net/i2ce/4.0/4.0.19/+download/ihris-suite-4.0.19.tar.bz2
    sudo tar -xjf ihris-suite-4.0.19.tar.bz2
    



Downloading the Ghana Sites Customizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. code-block:: bash

    sudo apt-get install bzr
    sudo mkdir -p /var/lib/iHRIS/ghana
    sudo chown `whoami`:`whoami` /var/lib/iHRIS/ghana
    cd /var/lib/iHRIS/ghana
    bzr branch lp:~ihris+ghana/ihris-manage-ghana/combined-sites 4.0
    cd /var/lib/iHRIS/ghana/4.0
    bzr bind lp:~ihris+ghana/ihris-manage-ghana/combined-sites
    



National (Central) Site setup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Database Setup
~~~~~~~~~~~~~~
To create the needed database you can do:


.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:


.. code-block:: mysql

    CREATE DATABASE ghana_ihris_manage_national;
    GRANT ALL PRIVILEGES ON ghana_ihris_manage_national.* TO ihris_ghana@localhost identified by 'PASS';
    SET GLOBAL log_bin_trust_function_creators = 1;
    exit
    

Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

If you are having trouble creating routines see `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_.
For security, make sure the password you choose is different than the root password for MySQL.  Let us refer to this password as YYYYY.


Setting the Password
~~~~~~~~~~~~~~~~~~~~

Now we need to set the password **PASS** in the main configuration file.  Run the commands:


.. code-block:: bash

    mkdir -p /var/lib/iHRIS/ghana/4.0/sites/national/pages/local/
    cp /var/lib/iHRIS/ghana/4.0/sites/national/pages/config.values.php /var/lib/iHRIS/ghana/4.0/sites/national/pages/local/config.values.php
    gedit /var/lib/iHRIS/ghana/4.0/sites/national/pages/local/config.values.php
    

and change:


.. code-block:: php

    /**
     * the dsn to connect to your databse
     */
    //$i2ce_site_dsn = 'mysql://john:pass@localhost/database' ;
    

to:


.. code-block:: php

    /**
     * the dsn to connect to your databse
     */
    $i2ce_site_dsn = 'mysql://ihris_ghana:PASS@localhost/ghana_ihris_manage_national' ;
    

Save and Quit.  Here PASS is what you chose above.


Making the Site Available
~~~~~~~~~~~~~~~~~~~~~~~~~

We make iHRIS Manage site available via the webserver:


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/ghana/4.0/sites/national/pages /var/www/ghananational
    



Finishing Up
~~~~~~~~~~~~
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/ghananational
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin* with the password you used to connect to the database ('''YYYY''' that you set above).


Regional Site setup
^^^^^^^^^^^^^^^^^^^

Database Setup
~~~~~~~~~~~~~~
To create the needed database you can do:


.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:


.. code-block:: mysql

    CREATE DATABASE ghana_ihris_manage_regional;
    GRANT ALL PRIVILEGES ON ghana_ihris_manage_regional.* TO ihris_ghana@localhost identified by 'PASS';
    SET GLOBAL log_bin_trust_function_creators = 1;
    exit
    

Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

If you are having trouble creating routines see `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_.
For security, make sure the password you choose is different than the root password for MySQL.  Let us refer to this password as YYYYY.


Setting the Password
~~~~~~~~~~~~~~~~~~~~

Now we need to set the password **PASS** in the main configuration file.  Run the commands:


.. code-block:: bash

    mkdir -p /var/lib/iHRIS/ghana/4.0/sites/regional/pages/local/
    cp /var/lib/iHRIS/ghana/4.0/sites/regional/pages/config.values.php /var/lib/iHRIS/ghana/4.0/sites/regional/pages/local/config.values.php
    gedit /var/lib/iHRIS/ghana/4.0/sites/regional/pages/local/config.values.php
    

and change:


.. code-block:: php

    /**
     * the dsn to connect to your databse
     */
    //$i2ce_site_dsn = 'mysql://john:pass@localhost/database' ;
    

to:


.. code-block:: php

    /**
     * the dsn to connect to your databse
     */
    $i2ce_site_dsn = 'mysql://ihris_ghana:PASS@localhost/ghana_ihris_manage_regional' ;
    

Save and Quit.  Here PASS is what you chose above.


Making the Site Available
~~~~~~~~~~~~~~~~~~~~~~~~~

We make iHRIS Manage site available via the webserver:


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/ghana/4.0/sites/regional/pages /var/www/ghanaregional
    



Finishing Up
~~~~~~~~~~~~
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/ghanaregional
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin* with the password you used to connect to the database ('''YYYY''' that you set above).


Updating Customizations
^^^^^^^^^^^^^^^^^^^^^^^
To update the customizations from launchpad, do:
 cd /var/lib/iHRIS/ghana/4.0
 bzr update
[[Category:Ghana]]
