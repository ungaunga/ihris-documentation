Linux (Ubuntu) Installation - 4.0.9
===================================

This page contains installation instructions on installing iHRIS version 4.0.9 manually.
{{otherversions|Linux (Ubuntu) Installation}}

''Warning:'' See [[Installing iHRIS on Ubuntu 10.4 (Lucid)|Installing iHRIS on Ubuntu 10.4 or 10.10]] after completing these instructions to get iHRIS working on the latest release of Ubuntu.


<center>'''Need help?'''  Try our [[Project Communication]]</center>
== Getting Ready ==

Here are instructions for installing the iHRIS Suite on an Linux (Ubuntu) system.  If you need help installing Ubuntu you may want to take a look at
these directions for installing a [http://www.howtoforge.com/perfect-server-ubuntu8.04-lts Server] or a [http://www.howtoforge.com/the-perfect-desktop-ubuntu-8.04-lts-hardy-heron Desktop] system.

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
It appears that they were reduced with Karmic

== Configuring PHP ==

Next, you'll need to increase the memory limit for PHP. You can do this by editing the /etc/php5/apache2/php.ini. 
<source lang="bash">
sudo gedit /etc/php5/apache2/php.ini
</source>

Change the following line:
<source lang="ini">
memory_limit = 32M
</source>
to:
<source lang="ini">
memory_limit = 128M
</source>

== Installing Pear and PECL Packages ==

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:
<source lang="bash">
sudo apt-get install php-pear php-apc  php-mdb2 php-mdb2-driver-mysql 
sudo pear install text_password console_getopt
</source>

During certain activities like installation and upgrades you may need more memory than APC uses by default.  The php-apc package should have installed a file in /etc/php5/conf.d/apc.ini.  Edit this file:

<source lang="bash">
sudo gedit /etc/php5/conf.d/apc.ini
</source>

Then add the following lines:

<source lang="ini">
apc.shm_size=100
apc.slam_defense = Off
</source>
See [http://pecl.php.net/bugs/bug.php?id=16843 slam defense] and [http://t3.dotgnu.info/blog/php/user-cache-timebomb this].

You'll need to restart Apache after making this change.
<source lang="bash">
sudo /etc/init.d/apache2 restart
</source>

There are two optional packages you may wish to install:
<source lang="bash">
sudo apt-get install php5-gd php5-tidy
</source>
which are used to for inserting images into PDF output of reports and for exporting XML files in a nicely formatted manner

===FileInfo===
'''Note:''' If you're running Ubuntu 10.4 (Lucid Lynx) or later then you do not need to install Fileinfo.

The pecl package ''FileInfo'' is used to verify the validity of file types used for uploading (e.g. for uploaded images or documents)
<source lang="bash">
cd /tmp
wget http://pecl.php.net/get/Fileinfo
sudo pecl install Fileinfo*
echo extension=fileinfo.so | sudo tee /etc/php5/apache2/conf.d/fileinfo.ini
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

== Downloading the Software ==
To download the software you enter these commands:
<source lang="bash">
sudo mkdir -p /var/lib/iHRIS/lib/4.0.9
cd /var/lib/iHRIS/lib
sudo ln -s /var/lib/iHRIS/lib/4.0.9 /var/lib/iHRIS/lib/4.0
cd /var/lib/iHRIS/lib/4.0.9
sudo wget http://launchpad.net/ihris-manage/4.0/4.0.9/+download/ihris-manage-full-4.0.9.tar.bz2
sudo tar -xjf ihris-manage-full-4.0.9.tar.bz2
</source>

== Database Setup ==

To create the needed database you can do:
<source lang="bash">
mysql -u root -p
</source>
Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:
<source lang="mysql">
CREATE DATABASE ihris_manage;
GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost identified by 'PASS';
SET GLOBAL log_bin_trust_function_creators = 1;
exit
</source>
Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

If you want to install iHRIS Qualify (or iHRIS Plan) just replace everywhere you see manage with qualify (or plan). 

In version 4.0.1 of iHRIS we create mysql functions.  If you are having trouble creating routines see [http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging this].

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
[[Image:Phpmyadmin_create_user.gif|center|frame|Creating iHRIS_Manage Database and User]]  

For security, make sure the password you choose is different than the root password for MySQL.  Let us refer to this password as YYYYY.

== Creating a Site Configuration File ==

We are going to start by modifying the ''BLANK'' site for iHRIS Manage.  If you wish to install iHRIS Qualify or iHRIS Plan, you can follow the same instructions below but change ''manage'' to ''qualify'' or ''plan.''  To copy the ''BLANK'' site:
<source lang="bash">
sudo mkdir -p /var/lib/iHRIS/sites
sudo cp -R /var/lib/iHRIS/lib/4.0/ihris-manage/sites/blank /var/lib/iHRIS/sites/manage
</source>

===Set Email Address (Optional)===
You may optionally choose to  change the email address feedback is sent to by editting the site configuration file:
<source lang="bash">
sudo gedit /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml
</source>
changing:
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

== Making the Site Available == 

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
<tr><td>$i2ce_site_dsn</td><td rowpan='2'>mysql://ihris_manage:YYYYY@localhost/ihris_manage</td></tr>
<tr><td>$i2ce_site_module_config</td><td>/var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml</td></tr>
</table>
In $i2ce_site_dsn,  YYYYY is the password you set above.
</center>
Save and quit.

Finally, we make iHRIS Manage site we just created available via the webserver:
<source lang="bash">
sudo ln -s /var/lib/iHRIS/sites/manage/pages /var/www/manage
</source>
===Pretty URLs===
This is an optional step to make URLs cleaner by removing the index.php.
<source lang="bash">
sudo cp /var/www/manage/htaccess.TEMPLATE /var/www/manage/.htaccess
sudo gedit /var/www/manage/.htaccess
</source>
We need to look for the line RewriteBase and change it to the web directory we want to use we are using,  ''/manage''.  

Change the line that looks like:
<source lang="apache">
    RewriteBase /iHRIS/manage-BLANK
</source>
to:
<source lang="apache">
    RewriteBase /manage
</source>
You may now save and quit.

==Finishing Up==
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/manage
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the ''i2ce_admin'' with the password you used to connect to the database (YYYYY that you set above).

== Files ==
Here are samples of the files we edited above. '''WARNING THESE ARE OUT OF DATE AND REFER TO AN OLD VERSION OF THE SOFTWARE'''
<ul>
<li> [[Media:default.txt | /etc/apache2/sites-available/default]] </li>
<li> [[Media:IHRIS-Manage-Site_xml.txt | /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml]] </li>
<li> [[Media:htaccess.txt | /var/www/manage/.htaccess ]] </li>
<li> [[Media:Config_values_php.txt | /var/www/manage/config.values.php]] </li>
</ul>

[[Category:Developer Resources]]
