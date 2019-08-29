MLSCN Installation Instructions
===============================

This page contains installation instructions on installing iHRIS Manage Customizations for Medical Laboratory Science Council of Nigeria

Getting Ready
^^^^^^^^^^^^^


First you should install Ubuntu and all the supporting software required by iHRIS by following the [[Linux (Ubuntu) Installation - Supporting Software]] instructions.

 **Note:**  Installing on ext4 filesystem?  see  `this <http://ubuntuforums.org/showthread.php?t=1313834>`_ 

 **Note:**   Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with **sudo**  it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

 **Note:**   Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

 **Note:**   Some commands will launch the **gedit**  file editor.  Look at the  `documentation <https://help.ubuntu.com/community/gedit>`_  if you need additional help.



Download MLSCN Customizations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You just enter these commands on your terminal:



.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/MLSCN
    cd /var/lib/iHRIS/MLSCN
    bzr branch lp:~ihris-nigeria/ihris+nmc+nigeria/MLSCN-4.1 4.1
    



Create Database
^^^^^^^^^^^^^^^



.. code-block:: bash

    mysql -u root -p -Be 'create database ihris_manage_mlscn'
    

When prompted, you will have to type your MySQL password


Edit config.values.php
^^^^^^^^^^^^^^^^^^^^^^
Before editing this file, you have to create a directory under pages, where your local site configuration values will be set. And then you will copy both the config.values.php and the htaccess.TEMPLATE files there.



.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/MLSCN/4.1/pages/local
    sudo cd /var/lib/iHRIS/MLSCN/4.1/pages
    sudo cp config.values.php local
    sudo cp htaccess.TEMPLATE local/.htaccess
    

Then you go edit the file in local


.. code-block:: bash

    sudo gedit local/config.values.php
    

When editing this file, you have to make to sure you change the values as they are set on your computer. The **$i2ce_site_i2ce_path**  is the path where we can reach the latest I2CE source codes.

Set the correct database username and password on the line **$i2ce_site_dsn** , if these are not well set, the site will try to update and fail on the way. In most cases you don't have to change the **$i2ce_site_module_config**  value if you followed the right procedure when downloading the customizations in the step above.

You save and quit.

Finally, make MLSCN site you just installed available via the webserver:


.. code-block:: bash

    sudo ln -s /var/lib/iHRIS/MLSCN/4.1/pages /var/www/MLSCN
    


To install the system you simply browse to:
<center>
http://localhost/MLSCN
</center>
and wait for the site to initalize itself.  Congratulations!  You may log in as the *i2ce_admin*  with the password you used to connect to the database.

[[Category:Nigeria]]
