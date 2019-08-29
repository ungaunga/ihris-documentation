Senegal Installation Instructions
=================================

This page contains installation instructions on installing iHRIS Manage Customizations for Senegal Ministry of Health

Getting Ready
^^^^^^^^^^^^^


First you should install Ubuntu and all the supporting software required by iHRIS by following the [[Linux (Ubuntu) Installation - Supporting Software]] instructions.

 **Note:**  Installing on ext4 filesystem?  see  `this <http://ubuntuforums.org/showthread.php?t=1313834>`_ 

 **Note:**   Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with **sudo**  it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

 **Note:**   Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

 **Note:**   Some commands will launch the **gedit**  file editor.  Look at the  `documentation <https://help.ubuntu.com/community/gedit>`_  if you need additional help.



Install Additional Supporting Software
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Enter these commands on your terminal to install Bazaar (bzr) and PHPMyAdmin



.. code-block:: bash

    sudo apt-get install bzr bzrtools phpmyadmin
    



Downloading the Full iHRIS Suite
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Before proceeding with iHRIS Manage or iHRIS Qualify installation, we will want to download the most recent version of the full iHRIS Suite.  To download the software you enter these commands:


.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/lib/4.1.5
    sudo ln -s /var/lib/iHRIS/lib/4.1.5 /var/lib/iHRIS/lib/4.1
    cd /var/lib/iHRIS/lib/4.1.5
    sudo wget http://launchpad.net/i2ce/4.1/4.1.5/+download/ihris-suite-4.1.5.tar.bz2
    sudo tar -xjf ihris-suite-4.1.5.tar.bz2
    




Download Senegal Customizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You just enter these commands on your terminal:



.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/sites/4.1/
    cd /var/lib/iHRIS/sites/4.1
    sudo bzr branch lp:~ihris-senegal-team/ihris-senegal/sn-manage
    



Create Database
^^^^^^^^^^^^^^^

To create the needed database you can do:


.. code-block:: bash

    mysql -u root -p
    

Enter the password you set when installing MySQL.  You will now be able to send commands to MySQL and the prompt should always begin with 'mysql> '.  Type these commands:


.. code-block:: mysql

    CREATE DATABASE ihris_manage_senegal;
    GRANT ALL PRIVILEGES ON ihris_manage_senegal.* TO ihris_senegal@localhost identified by 'PASS';
    exit
    

Substitute PASS with something appropriate.  We'll refer to this password as YYYYY.


Edit config.values.php
^^^^^^^^^^^^^^^^^^^^^^
Before editing this file, you have to create a directory under pages, where your local site configuration values will be set. And then you will copy both the config.values.php and the htaccess.TEMPLATE files there.



.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/sites/4.1/sn-manage/pages/local
    cd /var/lib/iHRIS/sites/4.1/sn-manage/pages
    sudo cp config.values.php local/
    sudo cp htaccess.TEMPLATE .htaccess
    

Then you go edit the file in local


.. code-block:: bash

    sudo gedit local/config.values.php
    

When editing this file, you have to make to sure you change the values as they are set on your computer. The **$i2ce_site_i2ce_path**  is the path where we can reach the latest I2CE source codes.

Set the correct database username and password on the line **$i2ce_site_dsn** , if these are not well set, the site will try to update and fail on the way. Set the **$i2ce_site_module_config**  to /var/lib/iHRIS/sites/4.1/sn-manage/iHRIS-Manage-Senegal.xml.

Your file should look something like this with any comments that were already there:



.. code-block:: php

    $i2ce_site_i2ce_path = "/var/lib/iHRIS/lib/4.1/I2CE";
    
    $i2ce_site_dsn = 'mysql://ihris_senegal:YYYYYY@localhost/ihris_manage_senegal' ;
    
    $i2ce_site_module_config = "/var/lib/iHRIS/sites/4.1/sn-manage/iHRIS-Manage-Senegal.xml";
    


You save and quit.

Finally, make the Senegal site you just installed available via the webserver:


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/sites/4.1/sn-manage/pages /var/www/sn-manage
    


To install the system you simply browse to:
<center>
http://localhost/sn-manage
</center>
and wait for the site to initialize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database.

