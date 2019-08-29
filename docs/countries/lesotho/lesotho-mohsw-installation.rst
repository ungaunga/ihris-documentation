Installation Instructions
=========================

This page contains installation instructions on installing iHRIS Lesotho Customizations
{{otherversions|Linux (Ubuntu) Installation}} 

 *Warning:*  See [[Installing iHRIS on Ubuntu 10.4 (Lucid)]] after completing these instructions to get iHRIS working on the latest release of Ubuntu.

<center>'''Need help?'''  Try our [[Project Communication]]</center>

Getting Ready
^^^^^^^^^^^^^

Here are instructions for installing the iHRIS Suite on an Linux (Ubuntu) system.  If you need help installing Ubuntu you may want to take a look at
these directions for installing a  `Server <http://www.howtoforge.com/perfect-server-ubuntu8.04-lts>`_  or a  `Desktop <http://www.howtoforge.com/the-perfect-desktop-ubuntu-8.04-lts-hardy-heron>`_  system.

 **Note:**   Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with **sudo**  it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

 **Note:**   Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

 **Note:**   Some commands will launch the **gedit**  file editor.  Look at the  `documentation <https://help.ubuntu.com/community/gedit>`_  if you need additional help.

We begin by install a  `Lamp <http://en.wikipedia.org/wiki/LAMP_%28software_bundle%29>`_  server
(You can find more help  `here <https://help.ubuntu.com/community/ApacheMySQLPHP>`_ ):

.. code-block:: bash

    sudo tasksel install lamp-server
    

If you have never used mysql on your system, you will be asked to set the 'root' password for mysql.  We will refer to this password as XXXXX below.

 **Important** : Make sure your email system is correctly configured.  Under a default Ubuntu installation, you can do this with one of two commands:

.. code-block:: bash

    sudo apt-get install postfix
    sudo dpkg-reconfigure postfix
    

Follow the on-screen instructions to set up email on your system.  For additional help with installing Postfix, look at these  `instructions <https://help.ubuntu.com/community/PostfixBasicSetupHowto>`_ .  On Debian systems, the same commands can be used, but <tt>exim4</tt> is the default MTA instead of <tt>postfix</tt>

If you are using another Linux distribution, make sure your system can send email properly before continuing.

Configuring MYSQL
^^^^^^^^^^^^^^^^^
Make sure you have in /etc/mysql/my.cnf the following values set:

.. code-block:: bash

    sudo gedit /etc/mysql/my.cnf
    

.. code-block:: ini

    query_cache_limit       = 4M
    query_cache_size        = 64M
    

It appears that they were reduced with Karmic

Configuring PHP
^^^^^^^^^^^^^^^

Next, you'll need to increase the memory limit for PHP. You can do this by editing the /etc/php5/apache2/php.ini. 

.. code-block:: bash

    sudo gedit /etc/php5/apache2/php.ini
    

Change the following line:

.. code-block:: ini

    memory_limit = 32M
    

to:

.. code-block:: ini

    memory_limit = 128M
    

Installing Pear and PECL Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:

.. code-block:: bash

    sudo apt-get install php-pear php-apc  php-mdb2 php-mdb2-driver-mysql 
    sudo pear install text_password console_getopt
    

During certain activities like installation and upgrades you may need more memory than APC uses by default.  The php-apc package should have installed a file in /etc/php5/conf.d/apc.ini.  Edit this file:

.. code-block:: bash

    sudo gedit /etc/php5/conf.d/apc.ini
    

Then add the following lines:

.. code-block:: ini

    apc.shm_size=100
    apc.slam_defense = Off
    

See  `slam defense <http://pecl.php.net/bugs/bug.php?id=16843>`_  and  `this <http://t3.dotgnu.info/blog/php/user-cache-timebomb>`_ .

You'll need to restart Apache after making this change.

.. code-block:: bash

    sudo /etc/init.d/apache2 restart
    

There are two optional packages you may wish to install:

.. code-block:: bash

    sudo apt-get install php5-gd php5-tidy
    

which are used to for inserting images into PDF output of reports and for exporting XML files in a nicely formatted manner

FileInfo
~~~~~~~~
 **Note:**  If you're running Ubuntu 10.4 (Lucid Lynx) then you do not need to install Fileinfo.

The pecl package *FileInfo*  is used to verify the validity of file types used for uploading (e.g. for uploaded images or documents)

.. code-block:: bash

    sudo apt-get install libmagic-dev php5-dev
    sudo pecl install Fileinfo
    

If this doesn't work, you can also try:

.. code-block:: bash

    sudo pear install pecl/Fileinfo
    echo extension=fileinfo.so | sudo tee /etc/php5/apache2/conf.d/fileinfo.ini
    

Configuring Apache Web Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will see later we are using the apache rewrite module.  To enable the module:

.. code-block:: bash

    sudo a2enmod rewrite
    

Now we need to make sure we can use the *.htaccess*  file.

.. code-block:: bash

    sudo gedit /etc/apache2/sites-available/default
    

Change:
<source lang="apache">
<Directory /var/www/>
	Options Indexes FollowSymLinks MultiViews
	AllowOverride None
	Order allow,deny
	allow from all
</Directory>
</source>
to:
<source lang="apache">
<Directory /var/www/>
	Options Indexes FollowSymLinks MultiViews
	AllowOverride All
	Order allow,deny
	allow from all
</Directory>
</source>
Save and quit.

Let us restart the Apache webserver using:
<source lang="bash">
sudo /etc/init.d/apache2 restart 
</source>

Ubunutu 10.4 Lucid
^^^^^^^^^^^^^^^^^^

If you are using Lucid 10.4 Ubuntu, make sure that you following these [[Installing iHRIS on Ubuntu 10.4 (Lucid) | **important instructions** ]]

Downloading the Main iHRIS Manage Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To download the software you enter these commands:
<source lang="bash">
sudo mkdir -p /var/lib/iHRIS/lib/4.0.7
cd /var/lib/iHRIS/lib/4.0.7
sudo wget http://launchpad.net/ihris-manage/4.0/4.0.6/+download/ihris-manage-full-4_0_7.tar.bz2
sudo tar -xjf ihris-manage-full-4_0_7.tar.bz2
</source>

Downloading the Lesotho Customizations of iHRIS Manage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To download the software you enter these commands:
<source lang="bash">
sudo apt-get install bzr
sudo mkdir -p /var/lib/iHRIS/lesotho
sudo chown `whoami`:`whoami` /var/lib/iHRIS/lesotho
cd /var/lib/iHRIS/lesotho
bzr branch lp:ihris-manage-lesotho 4.0
cd /var/lib/iHRIS/lesotho/4.0
bzr bind lp:ihris-manage-lesotho
</source>

MOHSW Site
^^^^^^^^^^

Database Setup
~~~~~~~~~~~~~~

To create the needed database you can do:
<source lang="bash">
mysql -u root -p
</source>
Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:
<source lang="mysql">
CREATE DATABASE manage_lesotho_mohsw_4_0;
GRANT ALL PRIVILEGES ON manage_lesotho_mohsw_4_0.* TO ihris@localhost identified by 'PASS';
SET GLOBAL log_bin_trust_function_creators = 1;
exit
</source>
Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

If you are having trouble creating routines see  `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_ .
For security, make sure the password you choose is different than the root password for MySQL.  Let us refer to this password as YYYYY.

Setting the Password
~~~~~~~~~~~~~~~~~~~~

Now we need to set the password **PASS**  in the main configuration file.  Run the commands:
<source lang="bash">
mkdir -p /var/lib/iHRIS/lesotho/4.0/sites/MOHSW/pages/local/
cp /var/lib/iHRIS/lesotho/4.0/sites/MOHSW/pages/config.values.php /var/lib/iHRIS/lesotho/4.0/sites/MOHSW/pages/local/config.values.php
gedit /var/lib/iHRIS/lesotho/4.0/sites/MOHSW/pages/local/config.values.php
</source>
and change:
<source lang="php">
/**
 * the dsn to connect to your databse
 */
$i2ce_site_dsn = 'mysql://ihris:MYSQLPASSWORD@localhost/manage_lesotho_mohsw_4_0' ;
</source>
to:
<source lang="php">
/**
 * the dsn to connect to your databse
 */
$i2ce_site_dsn = 'mysql://ihris:PASS@localhost/manage_lesotho_mohsw_4_0' ;
</source>
Save and Quit.  Here PASS is what you chose above.

Making the Site Available
~~~~~~~~~~~~~~~~~~~~~~~~~

We make iHRIS Manage site available via the webserver:
<source lang="bash">
sudo ln -s /var/lib/iHRIS/lesotho/4.0/sites/MOHSW/pages /var/www/ihris-MOHSW
</source>

Finishing Up
~~~~~~~~~~~~
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/ihris-MOHSW
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database ('''YYYY''' that you set above).

CHAL Site
^^^^^^^^^

Database Setup
~~~~~~~~~~~~~~

To create the needed database you can do:
<source lang="bash">
mysql -u root -p
</source>
Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:
<source lang="mysql">
CREATE DATABASE manage_lesotho_chal_4_0;
GRANT ALL PRIVILEGES ON manage_lesotho_chal_4_0.* TO ihris@localhost identified by 'PASS';
SET GLOBAL log_bin_trust_function_creators = 1;
exit
</source>
Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

In version 4.0.1 of iHRIS we create mysql functions.  If you are having trouble creating routines see  `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_ .
For security, make sure the password you choose is different than the root password for MySQL.  Let us refer to this password as YYYYY.

Setting the Password
~~~~~~~~~~~~~~~~~~~~

Now we need to set the password **PASS**  in the main configuration file.  Run the commands:
<source lang="bash">
mkdir -p /var/lib/iHRIS/lesotho/4.0/sites/CHAL/pages/local/
cp /var/lib/iHRIS/lesotho/4.0/sites/CHAL/pages/config.values.php /var/lib/iHRIS/lesotho/4.0/sites/CHAL/pages/local/config.values.php
gedit /var/lib/iHRIS/lesotho/4.0/sites/CHAL/pages/local/config.values.php
</source>
and change:
<source lang="php">
/**
 * the dsn to connect to your databse
 */
$i2ce_site_dsn = 'mysql://ihris:MYSQLPASSWORD@localhost/manage_lesotho_chal_4_0' ;
</source>
to:
<source lang="php">
/**
 * the dsn to connect to your databse
 */
$i2ce_site_dsn = 'mysql://ihris:PASS@localhost/manage_lesotho_chal_4_0' ;
</source>
Save and Quit.  Here PASS is what you chose above.

Making the Site Available
~~~~~~~~~~~~~~~~~~~~~~~~~

We make iHRIS Manage site available via the webserver:
<source lang="bash">
sudo ln -s /var/lib/iHRIS/lesotho/4.0/sites/CHAL/pages /var/www/ihris-CHAL
</source>

Finishing Up
~~~~~~~~~~~~
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/ihris-CHAL
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database ('''YYYY''' that you set above).

Updating Customizations
^^^^^^^^^^^^^^^^^^^^^^^
To update the customizations from launchpad, ensure that port 22 is open on the server and do:
 cd /var/lib/iHRIS/lesotho/4.0
 bzr update

Importing Data
^^^^^^^^^^^^^^

Importing Data for MoHSW
~~~~~~~~~~~~~~~~~~~~~~~~
First thing we will do is to make sure the Lesotho customizations are up to date.  You can do this (as indicated above) by:
 cd /var/lib/iHRIS/lesotho/4.0
 bzr update
Once you are done you can enter
 bzr revno
to check the revision number of the customizations.  It should be (at least) *34* . 

You need to save the cleaned data from Rosaline for the MOHSW on the desktop under the filename **lesotho_cleaned.csv** 

To import the data:
 cd /var/lib/iHRIS/lesotho/4.0/tools
 php import_clean.php

* It will ask you if you want to run in test mode. You can answer **N** .
* It will ask you if the first column of the **lesotho_cleaned.csv**  file is a comment.  You can answer **N**
* You can expect the script to take about an hour to run.  You need to keep an eye on it as it will ask you occasionally if you wish to create some missing standardized data such as sub-programme.

 **VERY IMPORTANT:**  Once the data has been imported you need to clear the webserver's cache.  To do so browse to:
 http://localhost/ihris-MOHSW/clear_cache.php

Once the data has been imported, it will create a new file on the desktop **lesotho_cleaned.bad.''DATE_TIME''.csv**  which will contain a list of all the records it had problems with.

Importing Data for CHAL
~~~~~~~~~~~~~~~~~~~~~~~
First thing we will do is to make sure the Lesotho customizations are up to date.  You can do this (as indicated above) by:
 cd /var/lib/iHRIS/lesotho/4.0
 bzr update
Once you are done you can enter
 bzr revno
to check the revision number of the customizations.  It should be (at least) **38** . Since you have updated the code, you will need to browse to:
 http://localhost/ihris-CHAL
in order to do a site update.

You need to save the cleaned data from Rosaline for the MOHSW on the desktop under the filename **lesotho_cleaned_CHAL.csv** 

To import the data:
 cd /var/lib/iHRIS/lesotho/4.0/tools
 php import_CHAL.php

* It will ask you if you want to run in test mode. You can answer **N** .
* It will ask you if the first column of the **lesotho_cleaned_CHAL.csv**  file is a comment.  You can answer **N**
* You can expect the script to take about an hour to run.  You need to keep an eye on it as it will ask you occasionally if you wish to create some missing standardized data such as sub-programme.

 **VERY IMPORTANT:**  Once the data has been imported you need to clear the webserver's cache.  To do so browse to:
 http://localhost/ihris-CHAL/clear_cache.php

Once the data has been imported, it will create a new file on the desktop **lesotho_cleaned_CHAL.bad.''DATE_TIME''.csv**  which will contain a list of all the records it had problems with.

