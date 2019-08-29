Linux (Ubuntu) Installation - Supporting Software for iHRIS 4.3+ - 14.04
========================================================================

This document describes the needed installation and configuration of supporting software for iHRIS on Ubuntu 14.04 LTS, Trusty Tahr for iHRIS versions 4.3 and later.
{{otherversions|Linux (Ubuntu) Installation - Supporting Software}}

Getting Ready
^^^^^^^^^^^^^

Here are instructions for installing the supporting software for iHRIS on a Linux (Ubuntu) system.  If you need help installing Ubuntu you may want to take a look at
these directions for installing a  `Server <http://www.howtoforge.com/perfect-server-ubuntu-14.04-apache2-php-mysql-pureftpd-bind-dovecot-ispconfig-3>`_  or a  `Desktop <http://www.howtoforge.com/the-perfect-desktop-ubuntu-14.04-lts-trusty-tahr>`_  system.  For a server setup, we recommend using a LTS (long term support) version of Ubuntu.

 **Note:**   Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with **sudo**  it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

 **Note:**   Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

 **Note:**   Some commands will launch the **gedit**  file editor.  Look at the  `documentation <https://help.ubuntu.com/community/gedit>`_  if you need additional help.

We begin by install a  `Lamp <http://en.wikipedia.org/wiki/LAMP_%28software_bundle%29>`_  server
(You can find more help  `here <https://help.ubuntu.com/community/ApacheMySQLPHP>`_ ).  You will also need to install the PHP5 MySQL Native Driver to replace the default PHP5 MySQL driver.

.. code-block:: bash

    sudo tasksel install lamp-server
    sudo apt-get install php5-mysqlnd
    

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
    

It appears that they were reduced with Karmic.

To configure MySQL so iHRIS can create needed functions:

.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:

.. code-block:: mysql

    SET GLOBAL log_bin_trust_function_creators = 1;
    exit
    

Installing Pear and PECL Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:

.. code-block:: bash

    sudo apt-get install php-pear php5-gd php5-tidy php5-intl
    sudo pear install text_password
    

If the command for installing text_password, does not work for you <br> Download and Install the  `package <http://www.ubuntuupdates.org/package/core/precise/universe/base/php-text-password>`_  manually as follows:

.. code-block:: bash

    cd /tmp
    wget http://security.ubuntu.com/ubuntu/pool/universe/p/php-text-password/php-text-password_1.1.1-1_all.deb
    

Installed the deb

.. code-block:: bash

    sudo dpkg -i php-text-password_1.1.1-1_all.deb 
    

UUID
^^^^
We need to install the UUID module for PHP.  We need to install from PECL.  This can be done by first installing the php5-dev pageckage and the uuid packges.

.. code-block:: bash

    

Now install UUID from PECL:

.. code-block:: bash

    sudo pecl install uuid
    

It will ask a few questions and you can just press enter to take the default answers.<br>

We'll also need to create the ini file to load UUID into PHP.

.. code-block:: bash

    sudo gedit /etc/php5/mods-available/uuid.ini
    

It should look like this:

.. code-block:: ini

    extension=uuid.so
    

We'll also need to enable this for Apache and CLI by creating 2 symlinks for the uuid file:

.. code-block:: bash

    sudo ln -s /etc/php5/mods-available/uuid.ini /etc/php5/apache2/conf.d/30-uuid.ini
    sudo ln -s /etc/php5/mods-available/uuid.ini /etc/php5/cli/conf.d/30-uuid.ini
    

APCu
^^^^
We need to install the APCu module for PHP.  There are unfortunately some issues with php5-apcu, so we need to install from PECL.  

.. code-block:: bash

    sudo pecl install apcu-4.0.11
    

It will ask a few questions and you can just press enter to take the default answers.<br>

If pecl install apcu-4.0.11 does not work for you <br> Remove any existing php5-apcu

.. code-block:: bash

    sudo apt-get remove php5-apcu
    

Download and install appropriate php5-apcu  `package <http://mirrors.kernel.org/ubuntu/pool/universe/p/php-apcu>`_  manually as follows
<source lang='bash'>
cd /tmp
wget http://mirrors.kernel.org/ubuntu/pool/universe/p/php-apcu/php5-apcu_4.0.6-1_i386.deb
</source>

Install the package as follows
<source lang='bash'>
sudo dpkg -i php5-apcu_4.0.6-1_i386.deb
</source>

During certain activities like installation and upgrades you may need more memory than APC uses by default.  We also want to turn off the *slam defense.*   We need to edit the configuration file file for apcu:
<source lang="bash">
sudo gedit /etc/php5/mods-available/apcu.ini
</source>
It should look like this:
<source lang="ini">
extension=apcu.so
apc.enabled=1
apc.write_lock=1
apc.shm_size=100M
apc.slam_defense=0
apc.enable_cli=1
</source>
See  `slam defense <http://pecl.php.net/bugs/bug.php?id=16843>`_  and  `this <http://t3.dotgnu.info/blog/php/user-cache-timebomb>`_ .

We'll also need to enable this for Apache and CLI by creating 2 symlinks for the apcu file:

<source lang='bash'>
sudo ln -s /etc/php5/mods-available/apcu.ini /etc/php5/apache2/conf.d/20-apcu.ini
sudo ln -s /etc/php5/mods-available/apcu.ini /etc/php5/cli/conf.d/20-apcu.ini
</source>

You'll need to restart Apache after making this change.
<source lang="bash">
sudo /etc/init.d/apache2 restart
</source>

Debian Squeeze
~~~~~~~~~~~~~~
If you are using Debian Squeeze, then the value of *apc.shm_size*  should be:
<source lang='bash'>
apc.shm_size=100
</source>

Set ZendOpcache options
~~~~~~~~~~~~~~~~~~~~~~~
Edit the opcache config file with this command:
<source lang="bash">
sudo gedit /etc/php5/mods-available/opcache.ini
</source>
It should look like this for a production system:
<source lang="ini">
; configuration for php ZendOpcache module
; priority=05
zend_extension=opcache.so
opcache.memory_consumption=128M
opcache.interned_strings_buffer=8
opcache.max_accelerated_files=4000
opcache.revalidate_freq=60
opcache.fast_shutdown=1
opcache.enable_cli=1
</source>
For a development system you should modify revalidate_freq from 60 to 2:
<source lang="ini">
opcache.revalidate_freq=2
</source>

Configuring Apache Web Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Changed Document Root
~~~~~~~~~~~~~~~~~~~~~
In Ubuntu 14.04, the default document root has changed from **/var/www**  to **/var/www/html**  so when installing any iHRIS applications you will need to use the new directory to place the symlinks.  If you are upgrading you may or may not need to update these depending on if you replaced the Apache configuration files during the upgrade.

Enable Rewrite Module
~~~~~~~~~~~~~~~~~~~~~

You will see later we are using the apache rewrite module.  To enable the module:
<source lang="bash">
sudo a2enmod rewrite
</source>

Enable .htaccess Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now we need to make sure we can use the *.htaccess*  file.
<source lang="bash">
sudo gedit /etc/apache2/apache2.conf
</source>
Change:
<source lang="apache">
<Directory /var/www/>
        Options Indexes FollowSymLinks
	AllowOverride None
	Require all granted
</Directory>
</source>
to:
<source lang="apache">
<Directory /var/www/>
	Options Indexes FollowSymLinks MultiViews
	AllowOverride All
	Require all granted
</Directory>
</source>
Save and quit.

Restart Apache
~~~~~~~~~~~~~~
Let us restart the Apache webserver using:
<source lang="bash">
sudo service apache2 restart 
</source>

Install Memcached
^^^^^^^^^^^^^^^^^

With version 4.0.4 and greater of iHRIS you can use memcached to improve performance 

Note:  Memcached is used to cache data from the database.  Thus if you are an a sitaution
where you would need to restart the webserver by
 sudo service apache2 restart
you should now do
 sudo service apache2 restart && sudo service memcached restart

To install,  simply do
<source lang='bash'>
 sudo apt-get install php5-memcached memcached
</source>

