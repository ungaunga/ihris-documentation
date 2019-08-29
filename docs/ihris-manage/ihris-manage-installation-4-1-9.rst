IHRIS Manage Installation - 4.1.9
=================================

Once you have downloaded iHRIS, follow these instructions to install the blank site.  This assumes you have downloaded the software to /var/lib/iHRIS/lib/4.1.9/.  For instructions on installing Ubuntu and downloading the software see the [[Linux (Ubuntu) Installation - 4.1.9]] instructions.


Database Setup
^^^^^^^^^^^^^^

To create the needed database you can do:


.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:


.. code-block:: mysql

    CREATE DATABASE ihris_manage;
    GRANT ALL PRIVILEGES ON ihris_manage.* TO ihris_manage@localhost identified by 'PASS';
    exit
    

Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.

If you want to install iHRIS Qualify (or iHRIS Plan) just replace everywhere you see manage with qualify (or plan). 

In version 4.1.9 of iHRIS we create mysql functions.  If you are having trouble creating routines see  `this <http://www.ispirer.com/wiki/sqlways/troubleshooting-guide/mysql/import/binary-logging>`_ .

Alternatively, you may choose to install phpmyadmin to administer database through the web


.. code-block:: bash

    sudo apt-get install phpmyadmin
    

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


Creating a Site Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are going to start by modifying the *BLANK*  site for iHRIS Manage.  If you wish to install iHRIS Qualify or iHRIS Plan, you can follow the same instructions below but change *manage*  to *qualify*  or *plan.*   To copy the *BLANK*  site:


.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/sites
    sudo cp -R /var/lib/iHRIS/lib/4.1.9/ihris-manage/sites/blank /var/lib/iHRIS/sites/manage
    



Set Email Address (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You may optionally choose to  change the email address feedback is sent to by editting the site configuration file:


.. code-block:: bash

    sudo gedit /var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml
    

changing:


.. code-block:: xml

    <configuration name='email' path='to' values='single'>
      <displayName>Email Address</displayName>
      <value>BLANK</value>
    </configuration>
    

to:


.. code-block:: xml

    <configuration name='email' path='to' values='single'>
      <displayName>Email Address</displayName>
      <value>my_email@somewhere.com</value>
    </configuration>
    



Making the Site Available
^^^^^^^^^^^^^^^^^^^^^^^^^

We will now edit the configuration to let the site know about the database user and options:


.. code-block:: bash

    sudo gedit /var/lib/iHRIS/sites/manage/pages/config.values.php
    

We now need to uncomment and set the value of a few variables.  Commented lines will begin with two slashes (//) that you'll need to remove.

They are:
<center>
<table border='1' padding='2'>
<tr><th>Variable Name</th><th>Value</th></tr>
<tr><td>$i2ce_site_i2ce_path</td><td>/var/lib/iHRIS/lib/4.1.9/I2CE</td></tr>
<tr><td>$i2ce_site_dsn</td><td rowpan='2'>mysql://ihris_manage:YYYYY@localhost/ihris_manage</td></tr>
<tr><td>$i2ce_site_module_config</td><td>/var/lib/iHRIS/sites/manage/iHRIS-Manage-BLANK.xml</td></tr>
</table>
In $i2ce_site_dsn,  YYYYY is the password you set above.
</center>
Save and quit.

Finally, we make iHRIS Manage site we just created available via the webserver:


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/sites/manage/pages /var/www/manage
    


If you are running Ubuntu 14.04 LTS you need to run this command instead


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/sites/manage/pages /var/www/html/manage
    


Pretty URLs
~~~~~~~~~~~
This is an optional step to make URLs cleaner by removing the index.php.


.. code-block:: bash

    sudo cp /var/www/manage/htaccess.TEMPLATE /var/www/manage/.htaccess
    sudo gedit /var/www/manage/.htaccess
    


 **For Ubuntu 14.04 LTS** 


.. code-block:: bash

    sudo cp /var/www/html/manage/htaccess.TEMPLATE /var/www/html/manage/.htaccess
    sudo gedit /var/www/html/manage/.htaccess
    

We need to look for the line RewriteBase and change it to the web directory we want to use we are using,  */manage* .  

Change the line that looks like:


.. code-block:: apache

        RewriteBase /iHRIS/manage-BLANK
    

to:


.. code-block:: apache

        RewriteBase /manage
    

You may now save and quit.


Finishing Up
^^^^^^^^^^^^
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/manage
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database (YYYYY that you set above).


Files
^^^^^
Here are samples of the files we edited above. **WARNING THESE ARE OUT OF DATE AND REFER TO AN OLD VERSION OF THE SOFTWARE** 
<ul>
<li> [[Media:default.txt | /etc/apache2/sites-available/default]] </li>
<li> [[Media:IHRIS-Manage-Site_xml.txt | /var/lib/iHRIS/sites/manage/iHRIS-Manage-Site.xml]] </li>
<li> [[Media:htaccess.txt | /var/www/manage/.htaccess ]] </li>
<li> [[Media:Config_values_php.txt | /var/www/manage/config.values.php]] </li>
</ul>
[[Category:Installation]][[Category:iHRIS Manage]][[Category:Review2013]]
