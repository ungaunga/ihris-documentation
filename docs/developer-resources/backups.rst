Backups
================================================

Once you've installed iHRIS, you will need to run backups to make sure you don't lose any data if something happens to your hardware.  Backups should be moved to a separate machine ideally at another location in case a disaster occurs where the server is located.


Backup User
^^^^^^^^^^^
You can use the same database user that you use to connect to the database for iHRIS, but you may also just want to create a read only user to use for backups.  You can do this in PHPMyAdmin by creating a new user (we'll call it **backup** for this, but you can name it anything you'd like).  You can generate a password in PHPMyAdmin or set one you'd like to use.  You should restrict access to localhost in most cases.  The backup user will need SELECT and LOCK TABLES privileges.  You can do this per database or on every database on your server depending on your security needs.  You can also create the user using mysql from the terminal.  Just run the following command in the terminal:



.. code-block:: bash

    mysql -u root -p
    


You'll need to enter the root password for the MySQL server and then you can run this command:



.. code-block:: sql

    GRANT LOCK TABLES,SELECT ON *.* TO 'backup'@'localhost' IDENTIFIED BY 'PASSWORD';
    


Just replace PASSWORD with the password you want to use for the backup user.


Full Backup Script
^^^^^^^^^^^^^^^^^^
You can now create a shell script to run the database backup and alternatively clean up any old backups so you don't run out of disk space.  This will backup every table in the given database so it will be larger since it will back up the form and report caches.  This will make restoration faster though as you won't need to recreate these caches.  Here is an example script:



.. code-block:: bash

    #!/bin/bash
    
    DATABASE=YOUR_DB
    BACKUP_DIR=/var/lib/iHRIS/sites/backups
    DB_USER=backup
    DB_PASS=PASSWORD
    
    
    SUFFIX=`date +%F`
    
    cd $BACKUP_DIR
    mysqldump -u $DB_USER -p$DB_PASS $DATABASE > backup_${DATABASE}_${SUFFIX}.sql
    bzip2 -f backup_${DATABASE}_${SUFFIX}.sql
    
    ## Uncomment the following line to remove backup files older than 7 days except
    ## from the first day of the month.
    #find $BACKUP_DIR -name "backup_${DATABASE}*.sql.bz2" -mtime +7 -not -name "backup_${DATABASE}*-01.sql.bz2" -exec rm {} \;
    


You will need to replace **YOUR_DB** with the database you'd like to backup.  You will need to set the DB_USER and DB_PASS based on how you created your backup user.  You will also need to create the BACKUP_DIR and set it to where you'd like your backups to go.  From a terminal you can create the directory with this command (replacing the directory with the one you've chosen):



.. code-block:: bash

    mkdir -p /var/lib/iHRIS/sites/backups
    


You can create this script in your site in a cron directory.  To avoid having this file be added to launchpad, you can place it in a local directory, for example:  SITE_DIR/cron/local/do_backups.sh

You will also need to be sure your script is executable by running this from a terminal:


.. code-block:: bash

    chmod a+x SITE_DIR/cron/local/do_backups.sh
    



Setting Up the Cron
^^^^^^^^^^^^^^^^^^^
For more information on using the cron system, see the `Ubuntu Cron HowTo <https://help.ubuntu.com/community/CronHowto>`_.

Now you'll need to set up the cron to run your backup script nightly.  From the previous example the script will be at SITE_DIR/cron/local/do_backups.sh.  To edit your cron you can type the following in a terminal:


.. code-block:: bash

    crontab -e
    


You will see a file to edit similar to this.



.. code-block:: text

    # Edit this file to introduce tasks to be run by cron.
    #
    # Each task to run has to be defined through a single line
    # indicating with different fields when the task will be run
    # and what command to run for the task
    #
    # To define the time you can provide concrete values for
    # minute (m), hour (h), day of month (dom), month (mon),
    # and day of week (dow) or use '*' in these fields (for 'any').#
    # Notice that tasks will be started based on the cron's system
    # daemon's notion of time and timezones.
    #
    # Output of the crontab jobs (including errors) is sent through
    # email to the user the crontab file belongs to (unless redirected).
    #
    # For example, you can run a backup of all your user accounts
    # at 5 a.m every week with:
    # 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
    #
    # For more information see the manual pages of crontab(5) and cron(8)
    #
    # m h  dom mon dow   command
    


You will need to add a new line to the bottom of this file.  For example to run your script at 1AM every morning:



.. code-block:: text

    0 1 * * * SITE_DIR/cron/local/do_backups.sh
    



Backup Without Caches
^^^^^^^^^^^^^^^^^^^^^
If you have limited space, you may want to backup on the main data and not any cached database tables.  This will reduce the size of your backup file.  There is a sample script in I2CE/tools/backup_exclude_caches.php.  You will just need to configure your $db_user and $db_pass variables as well as the $backupdir.  By default, this script will backup all databases on your server so you can set a list of databases to backup using the $include_only array.

This script doesn't do any automatic deletion of backup files so you may need to set up something separate to do this.

You can copy this script to your SITE_DIR/cron/local directory as well and make your customizations.  To add this to the cron you would need to include the PHP executable to run the script:



.. code-block:: text

    0 1 * * * php SITE_DIR/cron/local/backup_exclude_caches.php
    


[[Category:Developer Resources]]
