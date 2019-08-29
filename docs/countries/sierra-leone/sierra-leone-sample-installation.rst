Sierra Leone Sample Installation
================================

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
sudo mkdir -p /var/lib/iHRIS/sites
sudo chown `whoami`:`whoami` /var/lib/iHRIS/sites
cd /var/lib/iHRIS/sites
bzr branch lp:~intrahealth+informatics/ihris-manage/SL-sample
cd /var/lib/iHRIS/sites/SL-sample
bzr bind lp:~intrahealth+informatics/ihris-manage/SL-sample
</source>


Setting Up The Site
^^^^^^^^^^^^^^^^^^^

Database Setup
~~~~~~~~~~~~~~

To create the needed database you can do:
<source lang="bash">
mysql -u root -p
</source>
Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:
<source lang="mysql">
CREATE DATABASE manage_SL;
GRANT ALL PRIVILEGES ON manage_SL.* TO ihris@localhost identified by 'manage';
SET GLOBAL log_bin_trust_function_creators = 1;
exit
</source>

If you are having trouble creating routines see  `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_ .


Making the Site Available
~~~~~~~~~~~~~~~~~~~~~~~~~

We make iHRIS Manage site available via the webserver:
<source lang="bash">
sudo ln -s /var/lib/iHRIS/sites/SL-sample/pages /var/www/ihris-SL
</source>


Finishing Up
~~~~~~~~~~~~
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/ihris-SL
</center>
and wait for the site to initialize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password **manage** 


Updating Customizations
^^^^^^^^^^^^^^^^^^^^^^^
To update the customizations from launchpad, ensure that port 22 is open on the server and do:
 cd /var/lib/iHRIS/site/SL-sample
 bzr update

