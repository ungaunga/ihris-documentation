NMCN Installation Instructions
==============================

This page contains installation instructions on installing iHRIS Qualify Nursing Midwifery Council of Nigeria Customizations
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
sudo wget http://launchpad.net/i2ce/4.0/4.0.7/+download/ihris-suite-4_0_7.tar.bz2
sudo tar -xjf ihris-suite-4_0_7.tar.bz2
</source>

Downloading the NMCN of iHRIS Qualify
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Launchpad First Steps
~~~~~~~~~~~~~~~~~~~~~
First you should create an account on  `Launchpad <https://launchpad.net/>`_  if you not have already done so.  We will refer to this account as **LAUNCHPAD_USER.** 

Since we will want to contribute to the code, we will need to create a  `ssh public key <https://help.launchpad.net/YourAccount/CreatingAnSSHKeyPair>`_  on your Ubuntu machine to add to Launchpad:
 sudo apt-get install openssh-client
 ssh-keygen -t rsa
When prompted, press Enter to accept the default file name for your key. Next, enter then confirm a password to protect your SSH key.  

Your key pair is now stored in ~/.ssh/id_rsa.pub (public key) and ~/.ssh/id_rsa (private key). Now you need to upload the public portion of your SSH key to Launchpad. To do this, open in your web browser:
 https://www.launchpad.net/~'''LAUNCHPAD_USER'''
You will see a place that says *SSH Keys*  with an exclamation point **(!)**  in a yellow circle next to it.  Click on the **(!)**  scroll down until you see *Add an SSH Key*  and a text box.  We will paste our public key into this text box.  To do so type in a terminal:
 gedit ~/.ssh/id_rsa.pub
you can now copy the contents of gedit (the public key) into the text box in the web browser.  Now simply click on the button *Import Public Key* 

For every computer/account that you use you will need to repeat these steps to create and import a public key.

Bazaar First Steps
~~~~~~~~~~~~~~~~~~
First we need to make sure the  `Bazaaar <http://bazaar-vcs.org/en/>`_  (bzr) version control software is installed:
  sudo apt-get install bzr bzrtools
You may wish to read the  `five minute tutorial <http://doc.bazaar-vcs.org/latest/en/mini-tutorial/index.html>`_  at this point.  You should also let bzr know how you are:
  bzr whoami "'''Your Name <your@email.add.ress>'''"

Getting the NMCN Customizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To download the software you enter these commands:
<source lang="bash">
sudo apt-get install bzr
sudo mkdir -p /var/lib/iHRIS/NMCN
sudo chown `whoami`:`whoami` /var/lib/iHRIS/NMCN
cd /var/lib/iHRIS/NMCN
bzr branch lp:~ihris-nigeria/ihris+nmc+nigeria/NMCN-4.0 4.0
cd /var/lib/iHRIS/NMCN/4.0
bzr bind lp:~ihris-nigeria/ihris+nmc+nigeria/NMCN-4.0
</source>

Setting up the NMCN Site and Database
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Database Setup
~~~~~~~~~~~~~~

To create the needed database you can do:
<source lang="bash">
mysql -u root -p
</source>
Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:
<source lang="mysql">
CREATE DATABASE qualify_NMCN_4_0;
GRANT ALL PRIVILEGES ON qualify_NMCN_4_0.* TO ihris@localhost identified by 'PASSWORD';
SET GLOBAL log_bin_trust_function_creators = 1;
exit
</source>

Substitute **PASSWORD**  with something appropriate.  

If you are having trouble creating routines see  `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_ .

Setting the Password
~~~~~~~~~~~~~~~~~~~~

Now we need to set the password **PASSWORD**  in the main configuration file.  Run the commands:
<source lang="bash">
mkdir -p /var/lib/iHRIS/NMCN/4.0/pages/local/
cp /var/lib/iHRIS/NMCN/4.0/pages/config.values.php /var/lib/iHRIS/NMCN/4.0/pages/local/config.values.php
gedit /var/lib/iHRIS/NMCN/4.0/pages/local/config.values.php
</source>
and the PASSWORD in the following line to what you chose above:
<source lang="php">
/**
 * the dsn to connect to your database
 */
$i2ce_site_dsn = 'mysql://ihris:PASSWORD@localhost/qualify_NMCN_4_0' ;
</source>
Now Save and Quit.

Making the Site Available
~~~~~~~~~~~~~~~~~~~~~~~~~

We make iHRIS Manage site available via the webserver:
<source lang="bash">
sudo ln -s /var/lib/iHRIS/NMCN/4.0/sites/MOHSW/pages /var/www/NMCN
</source>

Finishing Up
~~~~~~~~~~~~
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/NMCN
</center>
and wait for the site to initialize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database ('''YYYY''' that you set above).

Updating Customizations
^^^^^^^^^^^^^^^^^^^^^^^
To update the customizations from launchpad, ensure that port 22 is open on the server and do:
 cd /var/lib/iHRIS/NMCN/4.0
 bzr update

