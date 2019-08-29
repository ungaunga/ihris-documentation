Linux (Ubuntu) Installation - Supporting Software - 13.04
=========================================================

This document describes the needed installation and configuration of supporting software for iHRIS on Ubuntu 13.04, Raring Ringtail.
{{otherversions|Linux (Ubuntu) Installation - Supporting Software}}
== Getting Ready ==

Here are instructions for installing the supporting software for iHRIS on a Linux (Ubuntu) system.  If you need help installing Ubuntu you may want to take a look at
these directions for installing a [http://www.howtoforge.com/perfect-server-ubuntu-10.04-lucid-lynx-ispconfig-2 Server] or a [http://www.howtoforge.com/the-perfect-desktop-ubuntu-10.04-lucid-lynx Desktop] system.  For a server setup, we recommend using a LTS (long term support) version of Ubuntu.

'''Note:'''  Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with '''sudo''' it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

'''Note:'''  Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

'''Note:'''  Some commands will launch the '''gedit''' file editor.  Look at the [https://help.ubuntu.com/community/gedit documentation] if you need additional help.

We begin by install a [http://en.wikipedia.org/wiki/LAMP_%28software_bundle%29 Lamp] server
(You can find more help [https://help.ubuntu.com/community/ApacheMySQLPHP here]):
<source lang="bash">
sudo tasksel install lamp-server
</source>
If you have never used mysql on your system, you will be asked to set the 'root' password for mysql.  We will refer to this password as XXXXX below.

'''Important''': Make sure your email system is correctly configured.  Under a default Ubuntu installation, you can do this with one of two commands:
<source lang="bash">
sudo apt-get install postfix
sudo dpkg-reconfigure postfix
</source>

Follow the on-screen instructions to set up email on your system.  For additional help with installing Postfix, look at these [https://help.ubuntu.com/community/PostfixBasicSetupHowto instructions].  On Debian systems, the same commands can be used, but <tt>exim4</tt> is the default MTA instead of <tt>postfix</tt>

If you are using another Linux distribution, make sure your system can send email properly before continuing.

==Configuring MYSQL==
Make sure you have in /etc/mysql/my.cnf the following values set:
<source lang="bash">
sudo gedit /etc/mysql/my.cnf
</source>
<source lang="ini">
query_cache_limit       = 4M
query_cache_size        = 64M
</source>
It appears that they were reduced with Karmic.

To configure MySQL so iHRIS can create needed functions:
<source lang="bash">
mysql -u root -p
</source>
Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:
<source lang="mysql">
SET GLOBAL log_bin_trust_function_creators = 1;
exit
</source>

== Configuring PHP ==

Next, you'll need to set memory limit for PHP to 128M if it is not. You can do this by editing the /etc/php5/apache2/php.ini. 
<source lang="bash">
sudo gedit /etc/php5/apache2/php.ini
</source>

<source lang="ini">
memory_limit = 128M
</source>

== Installing Pear and PECL Packages ==

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:
<source lang="bash">
sudo apt-get install php-pear  php-mdb2 php-mdb2-driver-mysql  php5-gd php5-tidy php5-intl
sudo pear install text_password console_getopt
</source>
You will additionally need MDB2 and MDB2 MySQL driver Pear packages if they are not already installed. Install using
<source lang="bash">
sudo pear install MDB2
sudo pear install MDB2_Driver_mysql
</source>

Pear may complain: Failed to download pear/MDB2 within preferred state "stable", latest release is version 2.5.0b5, stability "beta", use "channel://pear.php.net/MDB2-2.5.0b5" to install. Simply copy the channel url being shown and install the latest beta

==APC==
We need to install the APC module for PHP.
<source lang='bash'>
sudo apt-get install php-apc
</source>

During certain activities like installation and upgrades you may need more memory than APC uses by default.  We also want to turn of the ''slam defense.''  We need to edit the configuration file file for apc:
<source lang="bash">
sudo gedit /etc/php5/mods-available/apc.ini
</source>
It should look like this:
<source lang="ini">
extension=apc.so
apc.write_lock=1
apc.shm_size=100M
apc.slam_defense=0
</source>
See [http://pecl.php.net/bugs/bug.php?id=16843 slam defense] and [http://t3.dotgnu.info/blog/php/user-cache-timebomb this].


You'll need to restart Apache after making this change.
<source lang="bash">
sudo /etc/init.d/apache2 restart
</source>

====Debian Squeeze====
If you are using Debian Squeeze, then the value of ''apc.shm_size'' should be:
<source lang='bash'>
apc.shm_size=100
</source>

==Configuring Apache Web Server==

You will see later we are using the apache rewrite module.  To enable the module:
<source lang="bash">
sudo a2enmod rewrite
</source>
Now we need to make sure we can use the ''.htaccess'' file.
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

==Install Memcached==

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
