Linux (RedHat-Fedora) Installation
================================================


Getting Ready
^^^^^^^^^^^^^

Here are instructions for installing the iHRIS Suite on an Linux (RedHat or Fedora) system.  If you need help installing a RedHat distribution, visit:



* `Fedora Documentation <http://docs.fedoraproject.org/>`_
* `RedHat Documentation <http://www.redhat.com/docs/>`_

The following steps assume you have root-level access to your Linux machine. Root-level access is achieved by any of the following steps



* Login to your server directly as the root user.
* Use "su" at the command prompt to switch to the root user.
* Prepend the "sudo" command to each command listed here to execute as root.

First, if your Linux installation includes SELinux, disable it using by modifying /etc/sysconfig/selinux to read:

 SELINUX=disabled

Now, install a `Lamp <http://en.wikipedia.org/wiki/LAMP_%28software_bundle%29>`_ server.


.. code-block::

    yum install httpd mysql-server php php-devel php-mysql php-xml
    


Please ensure your system can send email properly before continuing. RedHat and Fedora typically will have a configured version of sendmail installed by default.


Configuring PHP
^^^^^^^^^^^^^^^

Next, you'll need to increase the memory limit for PHP. You can do this by editing the /etc/php.d/php.ini. Change the following line:


.. code-block::

    memory_limit = 32M
    


to:


.. code-block::

    memory_limit = 128M
    



Installing Pear and PECL Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to install a few Pear and PECL packages for PHP.  For the Pear packages you can do:


.. code-block::

    yum install php-pear php-pecl-apc
    pear install MDB2 MDB2#mysql text_password console_getopt
    


During certain activities like installation and upgrades you may need more memory than APC uses by default. To increase the memory limit, edit /etc/php.d/php.ini and change:


.. code-block::

    apc.shm_size=32
    


to


.. code-block::

    apc.shm_size=100
    


There are two optional packages you may wish to install:

.. code-block::

    yum install php-gd php-tidy
    


These packages are used to for inserting images into PDF output of reports and for exporting XML files in a nicely formatted manner.

The pecl package *FileInfo* is used to verify the validity of file types used for uploading (e.g. for uploaded images or docuemnts). You can install this with the following commands:

 yum install file-devel
 pecl install Fileinfo
 echo extension=fileinfo.so >> /etc/php.ini

Finally, edit /etc/php.ini and set your timezone:

 date.timezone = America/New_York

Change "America/New_York" to match your locality -- the county and city spellings should match the directory structure found in /usr/share/zoneinfo/.

After installing these supplemental packages, be sure to restart apache with the following command:

 apachectl restart


Database Setup
^^^^^^^^^^^^^^

Manual Setup
~~~~~~~~~~~~
To create the needed database you can do:
 /etc/init.d/mysqld start
 mysql -u root
 mysql> CREATE DATABASE ihris_manage;
 mysql> GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost identified by 'PASS';
where you substitute PASS with something appropriate.
If you want to install iHRIS Qualify (or iHRIS Plan) just replace everywhere you see manage with qualify (or plan). 

In version 4.0.1 of iHRIS we create mysql functions.  If you are having trouble creating routines see `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_.

On Fedora systems, you'll also need to execute these commands to ensure database connectivity functions correctly:

 ln -s /var/lib/mysql/mysql.sock /var/run/mysqld/mysqld.sock


Downloading the Software
^^^^^^^^^^^^^^^^^^^^^^^^
To download the software you enter these commands:

.. code-block::

    cd /var/lib
    mkdir iHRIS
    cd /var/lib/iHRIS
    mkdir 4.1.5
    ln -s 4.1.5 4.1
    ln -s 4.1 current
    cd /var/lib/iHRIS/4.1
    wget http://launchpad.net/ihris-manage/4.1/4.1.5/+download/ihris-manage-full-4_1_5.tar.bz2
    tar -xjf ihris-manage-full-4_1_5.tar.bz2
    



Creating a Site Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are going to start by modifying the *BLANK* site for iHRIS Manage.  If you wish to install iHRIS Qualify or iHRIS Plan, you can follow the same instructions below but change *manage* to *qualify* or *plan.*  To copy the *BLANK* site:

.. code-block::

    cd /var/lib/iHRIS/
    mkdir sites
    cp -R /var/lib/iHRIS/current/ihris-manage/sites/blank /var/lib/iHRIS/sites/manage
    mv /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml  /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml
    


We now need to edit the site configuration file:

.. code-block::

    vim /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml
    

by changing:

.. code-block::

        <path name='modules'>
          <value>./modules</value>
          <!-- If this site module is not installed under the iHRIS Manage
               file structure, then remember to include a path to the rest of
               the modules here. 
               e.g. <value>..</value>
            -->
        </path>
    

to: 

.. code-block::

       <path name='modules'>
          <value>./modules</value>
          <value>/var/lib/iHRIS/current</value>
        </path>
    

You may choose to  change the email address feedback is sent to by changing:

.. code-block::

          <configuration name='email' path='to' values='single'>
          <displayName>Email Address</displayName>
            <value>BLANK</value>
          </configuration>
    

to:

.. code-block::

          <configuration name='email' path='to' values='single'>
          <displayName>Email Address</displayName>
            <value>my_email@somewhere.com</value>
          </configuration>
    

You may also choose to change *BLANK* everywhere with your organization's name.  For best results, please choose one word, possilby with a dash, such as *Sample*, *MOH*, or *MOH-Taifeki.*  To make this change, hit the replace icon, fill in *blank* under *Search for* and *MOH-Taifeki* under *Replace With,* then hit replace all.


Making the Site Available
^^^^^^^^^^^^^^^^^^^^^^^^^

We will now edit the configuration to let the site know about the database user and options:

.. code-block::

    vim /var/lib/iHRIS/sites/manage/pages/config.values.php
    

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

.. code-block::

    ln -s /var/lib/iHRIS/sites/manage/pages /var/www/html/manage
    cp /var/www/html/manage/htaccess.TEMPLATE /var/www/html/manage/.htaccess
    vim  /var/www/html/manage/.htaccess
    

We need to look for the line RewriteBase and change it to the web directory we want to use we are using,  */manage*.  You may now save and quit.
You will see we are using the apache rewrite module.  To enable the module:

.. code-block::

    a2enmod rewrite
    

Now we need to make sure we can use the *.htaccess* file.

.. code-block::

    vim /etc/httpd/conf/httpd.conf
    

Change:

.. code-block::

            <Directory /var/www/html/>
    		Options Indexes FollowSymLinks MultiViews
    		AllowOverride None
    		Order allow,deny
    		allow from all
            </Directory>
    

to:

.. code-block::

            <Directory /var/www/html>
    		Options Indexes FollowSymLinks MultiViews
    		AllowOverride All
    		Order allow,deny
    		allow from all
            </Directory>
    

Save and quit.


Finishing up
^^^^^^^^^^^^
Let us restart the Apache webserver using:

.. code-block::

    /etc/init.d/httpd restart 
    

Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/manage
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *administrator* with the default password *administator.*



Files
^^^^^
Here are samples of the files we edited above:
<ul>
<li> [[Media:default.txt | /etc/httpd/sites-available/default]] </li>
<li> [[Media:IHRIS-Manage-Site_xml.txt | /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml]] </li>
<li> [[Media:htaccess.txt | /var/www/manage/.htaccess ]] </li>
<li> [[Media:Config_values_php.txt | /var/www/manage/config.values.php]] </li>
</ul>
[[Category:Installation]][[Category:Review2013]]
