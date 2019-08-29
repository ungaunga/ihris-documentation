IHRIS Plan Installation - 1.0.4
===============================


Supporting Software
^^^^^^^^^^^^^^^^^^^
Please install the [[Linux (Ubuntu) Installation - Supporting Software | supporting software]] before proceeding.


Downloading
^^^^^^^^^^^
iHRIS Plan is based on version 3.1 of the iHRIS Suite.  

You can download the most recent 3.1 version of the iHRIS Suite and iHRIS Plan at:
  https://launchpad.net/ihris-plan/1.0/1.0.4/+download/ihris-plan-full-1_0_4.tar.bz2
You should downloaded the software to /var/lib/iHRIS/lib/3.1/.  You can do this by the following commands:


.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/lib/3.1
    cd /var/lib/iHRIS/lib/3.1
    sudo wget https://launchpad.net/ihris-plan/1.0/1.0.4/+download/ihris-plan-full-1_0_4.tar.bz2
    sudo tar -xjf ihris-plan-full-1_0_4.tar.bz2
    



Database Setup
^^^^^^^^^^^^^^

To create the needed database you can do:


.. code-block:: bash

    mysql -u root -p
    

Enter the password you set above (XXXXX) for MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:


.. code-block:: mysql

    CREATE DATABASE ihris_plan;
    GRANT ALL PRIVILEGES ON ihris_plan.* TO ihris_plan@localhost identified by 'PASS';
    exit
    

Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.



Creating a Site Configuration File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We are going to start by modifying the *BLANK*  site for iHRIS Plan.  To copy the *BLANK*  site:


.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/sites
    sudo cp -R /var/lib/iHRIS/lib/3.1/ihris-plan/sites/blank /var/lib/iHRIS/sites/plan
    



Update the Path to Modules
~~~~~~~~~~~~~~~~~~~~~~~~~~
You need to tell the site where to find all the core modules.  You can do this by editing the site configuration file:


.. code-block:: bash

    sudo gedit /var/lib/iHRIS/sites/plan/iHRIS-Plan-BLANK.xml
    

changing:
changing:


.. code-block:: xml

        <path name='modules'>
          <value>./modules</value>
          <value>../../../</value>
        </path>
    

to:


.. code-block:: xml

        <path name='modules'>
          <value>./modules</value>
          <value>/var/lib/iHRIS/lib/3.1</value>
        </path>
    




Set Email Address (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You may optionally choose to  change the email address feedback is sent to by editting the site configuration file:


.. code-block:: bash

    sudo gedit /var/lib/iHRIS/sites/plan/iHRIS-Plan-BLANK.xml
    

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

    sudo gedit /var/lib/iHRIS/sites/plan/pages/config.values.php
    

We now need to uncomment and set the value of a few variables.  Commented lines will begin with two slashes (//) that you'll need to remove.

They are:
<center>
<table border='1' padding='2'>
<tr><th> Variable Name </th><th> Value</th></tr>
<tr><td> $i2ce_site_i2ce_path </td><td> /var/lib/iHRIS/lib/3.1/I2CE </td></tr>
<tr><td> $i2ce_site_database </td><td> ihris_plan </td></tr>
<tr><td> $i2ce_site_database_user  </td><td> ihris_plan </td></tr>
<tr><td> $i2ce_site_database_password  </td><td> YYYYY (the password you set above) </td></tr>
<tr><td>$i2ce_site_module_config </td><td> /var/lib/iHRIS/sites/plan/iHRIS-Plan-BLANK.xml </td></tr>
</table>
</center>
Save and quit.

Finally, we make iHRIS Plan site we just created available via the webserver:


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/sites/plan/pages /var/www/plan
    


If you are running Ubuntu 14.04 LTS you need to run this command instead


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/sites/plan/pages /var/www/html/plan
    


Pretty URLs
~~~~~~~~~~~
This is an optional step to make URLs cleaner by removing the index.php.


.. code-block:: bash

    sudo cp /var/www/plan/htaccess.TEMPLATE /var/www/plan/.htaccess
    sudo gedit /var/www/plan/.htaccess
    


 **For Ubuntu 14.04 LTS** 


.. code-block:: bash

    sudo cp /var/www/html/plan/htaccess.TEMPLATE /var/www/html/plan/.htaccess
    sudo gedit /var/www/html/plan/.htaccess
    


We need to look for the line RewriteBase and change it to the web directory we want to use we are using,  */plan* .  

Change the line that looks like:


.. code-block:: apache

        RewriteBase /iHRIS/plan-BLANK
    

to:
<source lang="apache">
    RewriteBase /plan
</source>
You may now save and quit.


Finishing Up
^^^^^^^^^^^^
Now we are ready to begin the site installation.  Simply browse to:
<center>
http://localhost/plan
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database (YYYYY that you set above).

[[Category:Installation]][[Category:iHRIS Plan]][[Category:Review2013]]
