Linux (Ubuntu) Installation - Supporting Software - 13.04
=========================================================

This document describes the needed installation and configuration of supporting software for iHRIS on Ubuntu 13.04, Raring Ringtail.
{{otherversions|Linux (Ubuntu) Installation - Supporting Software}}

Getting Ready
^^^^^^^^^^^^^

Here are instructions for installing the supporting software for iHRIS on a Linux (Ubuntu) system.  If you need help installing Ubuntu you may want to take a look at
these directions for installing a  `Server <http://www.howtoforge.com/perfect-server-ubuntu-10.04-lucid-lynx-ispconfig-2>`_  or a  `Desktop <http://www.howtoforge.com/the-perfect-desktop-ubuntu-10.04-lucid-lynx>`_  system.  For a server setup, we recommend using a LTS (long term support) version of Ubuntu.

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
    

It appears that they were reduced with Karmic.

To configure MySQL so iHRIS can create needed functions:


.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:


.. code-block:: mysql

    SET GLOBAL log_bin_trust_function_creators = 1;
    exit
    



Configuring PHP
^^^^^^^^^^^^^^^

Next, you'll need to set memory limit for PHP to 128M if it is not. You can do this by editing the /etc/php5/apache2/php.ini. 


.. code-block:: bash

    sudo gedit /etc/php5/apache2/php.ini
    




.. code-block:: ini

    memory_limit = 128M
    



Installing Pear and PECL Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:


.. code-block:: bash

    sudo apt-get install php-pear  php-mdb2 php-mdb2-driver-mysql  php5-gd php5-tidy php5-intl
    sudo pear install text_password console_getopt
    

You will additionally need MDB2 and MDB2 MySQL driver Pear packages if they are not already installed. Install using


.. code-block:: bash

    sudo pear install MDB2
    sudo pear install MDB2_Driver_mysql
    


Pear may complain: Failed to download pear/MDB2 within preferred state "stable", latest release is version 2.5.0b5, stability "beta", use "channel://pear.php.net/MDB2-2.5.0b5" to install. Simply copy the channel url being shown and install the latest beta


APC
^^^
We need to install the APC module for PHP.


.. code-block:: bash

    sudo apt-get install php-apc
    


During certain activities like installation and upgrades you may need more memory than APC uses by default.  We also want to turn of the *slam defense.*   We need to edit the configuration file file for apc:


.. code-block:: bash

    sudo gedit /etc/php5/mods-available/apc.ini
    

It should look like this:


.. code-block:: ini

    extension=apc.so
    apc.write_lock=1
    apc.shm_size=100M
    apc.slam_defense=0
    

See  `slam defense <http://pecl.php.net/bugs/bug.php?id=16843>`_  and  `this <http://t3.dotgnu.info/blog/php/user-cache-timebomb>`_ .


You'll need to restart Apache after making this change.


.. code-block:: bash

    sudo /etc/init.d/apache2 restart
    



Debian Squeeze
--------------
If you are using Debian Squeeze, then the value of *apc.shm_size*  should be:


.. code-block:: bash

    apc.shm_size=100
    



Configuring Apache Web Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You will see later we are using the apache rewrite module.  To enable the module:


.. code-block:: bash

    sudo a2enmod rewrite
    

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

Let us restart the Apache webserver using:
<source lang="bash">
sudo /etc/init.d/apache2 restart 
</source>


Install Memcached
^^^^^^^^^^^^^^^^^

With version 4.0.4 and greater of iHRIS you can use memcached to improve performance 

Note:  Memcached is used to cache data from the database.  Thus if you are an a sitaution
where you would need to restart the webserver by
 sudo /etc/init.d/apache2 restart
you should now do
 sudo /etc/init.d/apache2 restart && sudo /etc/init.d/memcached restart

To install,  simply do
<source lang='bash'>
 sudo apt-get install php5-memcached memcached
</source>

[[Category:Developer Resources]]
