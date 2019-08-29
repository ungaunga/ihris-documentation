Upgrading From 3.1
==================

These are directions for upgrading iHRIS Manage from version 3.1 under Ubuntu.  

First Steps
^^^^^^^^^^^

Get The Source Code
~~~~~~~~~~~~~~~~~~~
You can either get the [[Linux (Ubuntu) Installation#Downloading the Software | released]] or the [[Using Bazaar to Contribute Code#Getting The Code | development code]].  Suppose that **[base_path]**  is the directory which contains i2ce, common, manage etc.

Backup Database
~~~~~~~~~~~~~~~
We should back up the database.  Go into phpmyadmin, select your database, click on operations, and copy the 
database to a new name **[database_name]** .

Logging
~~~~~~~
Open up a new terminal on the machine.  
 cd [base_path]/i2ce/tools
 php apache_tail.php 0

Main Configuration
^^^^^^^^^^^^^^^^^^
Copy the existing site directory over to a new directory and update the **config.values.php**  to:

* set the *$i2ce_site_database*  to **[database_name]** , the name of the new database
* set  *$i2ce_site_i2ce_path*  to **[base_path]/i2ce** , the directory where the new version of I2CE is located

If you have URL Rewriting turned on, you will want to update your **.htaccess**  file.  Look for the line RewriteBase and change it 
to the web directory you are using.

Site Configuration File
^^^^^^^^^^^^^^^^^^^^^^^

Versions
~~~~~~~~
We need to go through your site configuration (XML) file and look for any *conflicts*  and any *requirements*  with version info from 3.1 and update them to the new version.  For example, if you have something that looks like:
 <requirement name='ihris-manage'>
   <atLeast version='3.1'/>
   <lessThan version='3.2'/>
 </requirement>
it should be, for the 3.2 development version:
 <requirement name='ihris-manage'>
   <atLeast version='3.2'/>
   <lessThan version='3.3'/>
 </requirement>
or for the 4.0 release version:
 <requirement name='ihris-manage'>
   <atLeast version='4.0'/>
   <lessThan version='4.1'/>
 </requirement>
for the release version.

You should probably update the 
 <version>3.1.X</version>
to be:
 <version>3.2.0</version>
or:
 <version>4.0.0</version>
as appropriate.

Modules
~~~~~~~
There were new modules created in the 3.2/4.0 code base for iHRIS Manage.  Here are modules that did not exist in 3.1 which you probably want to enable in 3.2 or 4.0:
 <enable name='PersonContact'/>
 <enable name='ihris-manage-PersonDemographic'/>
 <enable name='PersonEducation'/>
 <enable name='PersonEmployment'/>
 <enable name='PersonID'/>
 <enable name='PersonLanguage'/>
 <enable name='PersonNotes'/>
You may also want:
 <enable name='stub'/>  
 <enable name="FileDump"/>
 <enable name="StretchPage"/>
 <enable name="messageBox"/>
 <enable name="messageNotice"/>
 <enable name="localeSelector"/>

Changes to HTML Templates
^^^^^^^^^^^^^^^^^^^^^^^^^
There have been some changes to template files to better support localization. 

Some of these changes may be in the *main.html*  and the *welcome.html*  files in the site templates folder.

Welcome Role
~~~~~~~~~~~~

Change things like:

.. code-block:: xml

     Logout as <span name='welcome_role'/>
    

to:

.. code-block:: xml

     <span printf="'Log out as %s',ihris-common->getUserRole()" />
    

Welcome Name
~~~~~~~~~~~~
Change things like:

.. code-block:: xml

     Welcome, <span name='welcome_name'>,
    

to:

.. code-block:: xml

     <span printf="'Welcome, %s',ihris-common->getUserNames()" />
    

