Linux (Ubuntu) Installation - 4.0.2
===================================

This page contains installation instructions on installing iHRIS version 4.0 manually.
{{otherversions|Linux (Ubuntu) Installation}}

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
The pecl package *FileInfo*  is used to verify the validity of file types used for uploading (e.g. for uploaded images or documents)

.. code-block:: bash

    sudo apt-get install libmagic-dev php5-dev
    sudo pecl install Fileinfo
    

If this doesn't work, you can also try:

.. code-block:: bash

    sudo pear install pecl/Fileinfo
    echo extension=fileinfo.so | sudo tee /etc/php5/apache2/conf.d/fileinfo.ini
    

Database Setup
^^^^^^^^^^^^^^

To create the needed database you can do:

.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:

.. code-block:: mysql

    CREATE DATABASE ihris_manage;
    GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost identified by 'PASS';
    SET GLOBAL log_bin_trust_function_creators = 1;
    exit
    

Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

If you want to install iHRIS Qualify (or iHRIS Plan) just replace everywhere you see manage with qualify (or plan). 

In version 4.0.1 of iHRIS we create mysql functions.  If you are having trouble creating routines see  `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_ .

Alternatively, you may choose to install phpmyadmin to administer database through the web
<source lang="bash">
sudo apt-get install phpmyadmin
</source>
A screen will come up asking if you want to install for apache2 or lighttpd.  Highlight apache2 and press the spacebar to select it.  It will ask for the root password (XXXXX) and you may also opt to create a phpmyadmin user to extra features.  Select a password for this user as well.

Now browse to:
<center>
http://localhost/phpmyadmin
</center>
login with the user 'root' and password XXXXX that you set above.  Once logged in you will create a database and user called ihris_manage.  To
do this, click on  the 'Privileges' link and select 'Add a new User'. Then fill out the form as follows:

.. image:: images/Phpmyadmin_create_user.gif
    :align: center

  

For security, make sure the password you choose is different than the root password for MySQL.  Let us refer to this password as YYYYY.

Downloading the Software
^^^^^^^^^^^^^^^^^^^^^^^^
To download the software you enter these commands:
<source lang="bash">
sudo mkdir -p /var/lib/iHRIS/lib/4.0.2
cd /var/lib/iHRIS/lib
sudo ln -s 4.0.2 4.0
cd /var/lib/iHRIS/lib/4.0.2
sudo wget http://launchpad.net/ihris-manage/4.0/4.0.2/+download/ihris-manage-full-4_0_2.tar.bz2
sudo tar -xjf ihris-manage-full-4_0_2.tar.bz2
</source>

Creating a Site Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are going to start by modifying the *BLANK*  site for iHRIS Manage.  If you wish to install iHRIS Qualify or iHRIS Plan, you can follow the same instructions below but change *manage*  to *qualify*  or *plan.*   To copy the *BLANK*  site:
<source lang="bash">
sudo mkdir -p /var/lib/iHRIS/sites
sudo cp -R /var/lib/iHRIS/lib/4.0/ihris-manage/sites/blank /var/lib/iHRIS/sites/manage
</source>

We now need to edit the site configuration file:
<source lang="bash">
sudo gedit /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml
</source>
by changing:
<source lang="xml">
<path name='modules'>
  <value>./modules</value>
  <!-- If this site module is not installed under the iHRIS Manage
       file structure, then remember to include a path to the rest of
       the modules here. e.g. 
   -->
</path>
</source>
to: 
<source lang="xml">
<path name='modules'>
  <value>./modules</value>
  <value>/var/lib/iHRIS/lib/4.0</value>
</path>
</source>
You may choose to  change the email address feedback is sent to by changing:
<source lang="xml">
<configuration name='email' path='to' values='single'>
  <displayName>Email Address</displayName>
  <value>BLANK</value>
</configuration>
</source>
to:
<source lang="xml">
<configuration name='email' path='to' values='single'>
  <displayName>Email Address</displayName>
  <value>my_email@somewhere.com</value>
</configuration>
</source>

Making the Site Available
^^^^^^^^^^^^^^^^^^^^^^^^^

We will now edit the configuration to let the site know about the database user and options:
<source lang="bash">
sudo gedit /var/lib/iHRIS/sites/manage/pages/config.values.php
</source>
We now need to uncomment and set the value of a few variables.  Commented lines will begin with two slashes (//) that you'll need to remove.

They are:
<center>
<table border='1' padding='2'>
<tr><th>Variable Name</th><th>Value</th></tr>
<tr><td>$i2ce_site_i2ce_path</td><td>/var/lib/iHRIS/lib/4.0/I2CE</td></tr>
<tr><td>$i2ce_site_database</td><td>ihris_manage</td></tr>
<tr><td>$i2ce_site_database_user</td><td>ihris_manage</td></tr>
<tr><td>$i2ce_site_database_password</td><td>YYYYY (the password you set above)</td></tr>
<tr><td>$i2ce_site_module_config</td><td>/var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml</td></tr>
</table>
</center>
Save and quit.

Finally, we make iHRIS Manage site we just created available via the webserver:
<source lang="bash">
sudo ln -s /var/lib/iHRIS/sites/manage/pages /var/www/manage
sudo cp /var/www/manage/htaccess.TEMPLATE /var/www/manage/.htaccess
sudo gedit /var/www/manage/.htaccess
</source>
We need to look for the line RewriteBase and change it to the web directory we want to use we are using,  */manage* .  

Change the line that looks like:
<source lang="apache">
    RewriteBase /iHRIS/manage-BLANK
</source>
to:
<source lang="apache">
    RewriteBase /manage
</source>

You may now save and quit.
You will see we are using the apache rewrite module.  To enable the module:
<source lang="bash">
sudo a2enmod rewrite
</source>
Now we need to make sure we can use the *.htaccess*  file.
<source lang="bash">
sudo gedit /etc/apache2/sites-available/default
</source>
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

Finishing up
^^^^^^^^^^^^
Let us restart the Apache webserver using:
<source lang="bash">
sudo /etc/init.d/apache2 restart 
</source>
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/manage
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *administrator*  with the default password *administator.* 

Files
^^^^^
Here are samples of the files we edited above:
<ul>
<li> [[Media:default.txt | /etc/apache2/sites-available/default]] </li>
<li> [[Media:IHRIS-Manage-Site_xml.txt | /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml]] </li>
<li> [[Media:htaccess.txt | /var/www/manage/.htaccess ]] </li>
<li> [[Media:Config_values_php.txt | /var/www/manage/config.values.php]] </li>
</ul>

