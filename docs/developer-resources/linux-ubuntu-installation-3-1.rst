Linux (Ubuntu) Installation - 3.1
=================================

This page contains installation instructions on installing iHRIS version 3.1 manually.
{{otherversions|Linux (Ubuntu) Installation}}
== Getting Ready ==

Here are instructions for installing the iHRIS Suite on an Linux (Ubuntu) system.  If you need help installing Ubuntu you may want to take a look at
these directions for installing a [http://www.howtoforge.com/perfect-server-ubuntu8.04-lts Server] or a [http://www.howtoforge.com/the-perfect-desktop-ubuntu-8.04-lts-hardy-heron Desktop] system. 

We begin by install a [http://en.wikipedia.org/wiki/LAMP_%28software_bundle%29 Lamp] server
(You can find more help [https://help.ubuntu.com/community/ApacheMySQLPHP here]):
<pre>
sudo tasksel install lamp-server
</pre>
If you have never used mysql on your system, you will be asked to set the 'root' password for mysql.  We will refer to this password as XXXXX below.

'''Important''': Make sure your email system is correctly configured.  Under a default Ubuntu installation, you can do this with one of two commands:
<pre>
sudo aptitude install postfix
sudo dpkg-reconfigure postfix
</pre>
Follow the on-screen instructions to set up email on your system.  On Debian systems, the same commands can be used, but <tt>exim4</tt> is the default MTA instead of <tt>postfix</tt>

If you are using another Linux distribution, make sure your system can send email properly before continuing.

== Installing Pear and PECL Packages ==

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:
<pre>
sudo apt-get install php-pear php-apc
sudo pear  install MDB2 MDB2#mysql text_password console_getopt
</pre>

During certain activities like installation and upgrades you may need more memory than APC uses by default.  The php-apc package should have installed a file in /etc/php5/conf.d/apc.ini.  Edit this file and add the following line:

<pre>
apc.shm_size=100
</pre>

You'll need to restart Apache after making this change.

There are two optional packages you may wish to install:
<pre>
sudo apt-get install php5-gd php5-tidy
</pre>
which are used to for inserting images into PDF output of reports and for exporting XML files in a nicely formatted manner

== Database Setup ==

To create the needed database you can do:
 mysql -u root -p
 mysql> CREATE DATABASE ihris_manage;
 mysql> GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost identified by 'PASS';
where you substitute PASS with something appropriate.
If you want to install iHRIS Qualify (or iHRIS Plan) just replace everywhere you see manage with qualify (or plan). 

In version 4.0.1 of iHRIS we create mysql functions.  If you are having trouble creating routines see [http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging this].

Alternatively, you may choose to install phpmyadmin to administer database through the web
<pre>
sudo apt-get install phpmyadmin
</pre>
Now browse to:
<center>
http://localhost/phpmyadmin
</center>
login with the user 'root' and password XXXX that you set above.  Once logged in you will create a database and user called ihris_manage.  To
do this, click on  the 'Privileges' link and select 'Add a new User'. Then fill out the form as follows:
[[Image:Phpmyadmin_create_user.gif|center|frame|Creating iHRIS_Manage Database and User]].  For security, make sure the password
you choose is different than the root password for mysql.  Let us refer to this password as YYYYY.

== Downloading the Software ==
To download the software you enter these commands:
<pre>
cd /var/lib
sudo mkdir iHRIS
cd /var/lib/iHRIS
sudo mkdir 3.1.4
sudo ln -s 3.1.4 3.1
sudo ln -s 3.1 current
cd /var/lib/iHRIS/3.1.4
sudo wget http://launchpad.net/i2ce/3.1/3.1.4/+download/ihris-suite-3_1_4.tar.bz2
sudo tar -xjf ihris-suite-3_1_4.tar.bz2
</pre>

== Creating a Site Configuration File ==

We are going to start by modifying the ''BLANK'' site for iHRIS Manage.  If you wish to install iHRIS Qualify or iHRIS Plan, you can follow the same instructions below but change ''manage'' to ''qualify'' or ''plan.''  To copy the ''BLANK'' site:
<pre>
cd /var/lib/iHRIS/
sudo mkdir sites
sudo cp -R /var/lib/iHRIS/current/ihris-manage/sites/blank /var/lib/iHRIS/sites/manage
sudo mv /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml  /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml
</pre>

We now need to edit the site configuration file:
<pre>
sudo gedit /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml
</pre>
by changing:
<pre>
    <path name='modules'>
      <value>./modules</value>
      <!-- If this site module is not installed under the iHRIS Manage
           file structure, then remember to include a path to the rest of
           the modules here. 
           e.g. <value>..</value>
        -->
    </path>
</pre>
to: 
<pre>
   <path name='modules'>
      <value>./modules</value>
      <value>/var/lib/iHRIS/current</value>
    </path>
</pre>
You may choose to  change the email address feedback is sent to by changing:
<pre>
      <configuration name='email' path='to' values='single'>
      <displayName>Email Address</displayName>
        <value>BLANK</value>
      </configuration>
</pre>
to:
<pre>
      <configuration name='email' path='to' values='single'>
      <displayName>Email Address</displayName>
        <value>my_email@somewhere.com</value>
      </configuration>
</pre>
You may also choose to change ''BLANK'' everywhere with your organization's name.  For best results, please choose one word, possilby with a dash, such as ''Sample'', ''MOH'', or ''MOH-Taifeki.''  To make this change, hit the replace icon, fill in ''blank'' under ''Search for'' and ''MOH-Taifeki'' under ''Replace With,'' then hit replace all.

== Making the Site Available == 

We will now edit the configuration to let the site know about the database user and options:
<pre>
sudo gedit /var/lib/iHRIS/sites/manage/pages/config.values.php
</pre>
We now need to uncomment and set the value of a few variables.  They are:
<center>
<table border='1' padding='2'>
<tr><th> Variable Name </th><th> Value</th></tr>
<tr><td>  $i2ce_site_i2ce_path </td><td> /var/lib/iHRIS/current/I2CE </td></tr>
<tr><td> $i2ce_site_database </td><td> ihris_manage </td></tr>
<tr><td> $i2ce_site_database_user  </td><td> ihris_manage </td></tr>
<tr><td> $i2ce_site_database_password  </td><td> YYYYY (the password you set above) </td></tr>
<tr><td>$i2ce_site_module_config </td><td> /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml </td></tr>
</table>
</center>
Save and quit.

Finally, we make iHRIS Manage site we just created available via the webserver:
<pre>
sudo ln -s /var/lib/iHRIS/sites/manage/pages /var/www/manage
sudo cp /var/www/manage/htaccess.TEMPLATE /var/www/manage/.htaccess
sudo gedit /var/www/manage/.htaccess
</pre>
We need to look for the line RewriteBase and change it to the web directory we want to use we are using,  ''/manage''.  You may now save and quit.
You will see we are using the apache rewrite module.  To enable the module:
<pre>
sudo a2enmod rewrite
</pre>
Now we need to make sure we can use the ''.htaccess'' file.
<pre>
sudo gedit /etc/apache2/sites-available/default
</pre>
Change:
<pre>
        <Directory /var/www/>
		Options Indexes FollowSymLinks MultiViews
		AllowOverride None
		Order allow,deny
		allow from all
        </Directory>
</pre>
to:
<pre>
        <Directory /var/www/>
		Options Indexes FollowSymLinks MultiViews
		AllowOverride All
		Order allow,deny
		allow from all
        </Directory>
</pre>
Save and quit.

== Finishing up ==
Let us restart the Apache webserver using:
<pre>
sudo /etc/init.d/apache2 restart 
</pre>
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/manage
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the ''administrator'' with the default password ''administator.''


== Files ==
Here are samples of the files we edited above:
<ul>
<li> [[Media:default.txt | /etc/apache2/sites-available/default]] </li>
<li> [[Media:IHRIS-Manage-Site_xml.txt | /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml]] </li>
<li> [[Media:htaccess.txt | /var/www/manage/.htaccess ]] </li>
<li> [[Media:Config_values_php.txt | /var/www/manage/config.values.php]] </li>
</ul>

[[Category:Developer Resources]]
