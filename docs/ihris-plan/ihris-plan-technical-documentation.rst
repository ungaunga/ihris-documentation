IHRIS Plan Technical Documentation
==================================

 *This is sample documentation for iHRIS Plan when installed in a country setting. This documentation is current as of iHRIS Plan version 1.0 (August 15, 2008).* 

iHRIS Plan is built on the IntraHealth Informatics Core Engine (I2CE) with iHRIS Common (ihris-common) module version 3.1. The iHRIS Plan version is 1.0. Everything is written in PHP 5 and is installed in /var/lib/iHRIS/. Documentation is located at http://wiki.ihris.org/wiki/index.php/Capacity_Project's_iHRIS_Suite, and development and future release source code are at https://launchpad.net/ihris-plan or https://launchpad.net/ihris-suite for all the iHRIS software.

The application can be accessed at http://#.#.#.#/iHRIS/plan/. The database being used is {DatabaseName}.

The site files for this installation are in /var/lib/iHRIS/sites/{site_name}. Any customizations should be made here so that software updates won't affect these customizations. The files to be added to the web server are linked from /var/www/iHRIS/plan to /var/lib/iHRIS/sites/{site_name}/pages.

If you have any problems with the iHRIS application or the server, email the ihris-developers list at ihris-developers@lists.intrahealth.org. Subscribe to the list or view the archives at http://lists.intrahealth.org/mailman/listinfo/ihris-developers/.



Backups
^^^^^^^

There are two backup drives on the server. One is a 160GB internal drive mounted as /backup. The second is a 1TB external drive mounted as /external.
 
Every night the database is dumped to a file called /var/lib/iHRIS/backup/{DatabaseName}.sql. Then the entire /var/lib/iHRIS directory is synchronized to /backup/ihris-plan/sync/. This is an exact copy of the site from the night before if any files need to be restored. Every week the sync/ directory is archived in /backup/ihris-plan/backup-plan-YYYY-MM-DD.tar.bz2. Every night the /var/lib/iHRIS directory is archived to the /external drive as /external/backup/ihris-plan/backup-plan-YYYY-MM-DD.tar.bz2.

The backup directories should be checked regularly to make sure recent archive files are being created.



Restoring the Database
^^^^^^^^^^^^^^^^^^^^^^

To restore the database from the backup, find the {DatabaseName}.sql file in the sync directory or one of the archives on the /external or /backup directories. It will be in the backup subdirectory of the archives or /backup/ihris-plan/sync/backup. Open a terminal, change to the directory with the .sql file you wish to restore and run the following command:


.. code-block::

    mysql -u root -p {DatabaseName} < {DatabaseName}.sql


This will then ask for a password, which is given above in the MySQL section unless it has been changed. This will completely overwrite everything in the {DatabaseName} database, so make sure this is what you want to do. 

To be sure, make a manual backup of the database using PHP MyAdmin. Go to http://172.24.48.88/phpmyadmin/ and login as the root user. Click on the {DatabaseName} database on the left menu or select it from the dropdown. Click the Operations tab. Type in a new database name under the Copy Database section. This name can be any name that isn't an existing database on the server. Make sure Structure and Data is checked as well as CREATE DATABASE before copying. 

To restore from a manually copied database, go to the Operations tab for the {DatabaseName} database and rename it. Then go to the Operations tab for the copied database and rename it to {DatabaseName}.

You can also restore from the {DatabaseName}.sql file using PHP MyAdmin. If you have the file on your machine, go to the Import tab, browse to the file and click Go. This won't work if the file is very large, though. You can also create a manual backup to save to your local computer using the Export tab. There are many options for the format there, but you'll need to choose SQL if you wish to export the table structure. The file exported here can also be used to import to the database.



