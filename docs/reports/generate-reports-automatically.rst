Generate Reports Automatically
==============================

This tutorial shows you how to generate reports automatically in the background with a [[Cron Jobs|cron job]].

By default, iHRIS will launch automatically a background process to generate reports.   However, this may be less than ideal on systems with higher load or a larger number of records.  Instead, you may wish to schedule reports to be run at specific times.  For example:


* The search report should be run hourly -- this way new people added to the system will show up in the search page
* Other reports should be run on a nightly basis

The first step is to determine the list of reports that you want to generate.   You should also determine the frequency that you want them archive them on.  In this example, based on iHRIS Botswana,  we show you how to setup generation of hourly search reports and other reports nightly.


Turn Off Background Report Generation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
See [[Configuring Report Generation Timing]].  


Getting the Report Name
^^^^^^^^^^^^^^^^^^^^^^^
You should first create a list of the reports that you want to generate  For each of the report views that you want you can get the name/index of the report from the URL.  The easiest way to do this is go to 


* Configure System
* Reports
Now scroll over the "generate" link next to report that you are interested in with your mouse, and you should see a URL like:
  http://localhost/iHRIS/manage/CustomReports/generate/search_people
Then "search_people" is the name of the report.
 

Creating A Shell Script (Hourly)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In your site customizations, create a new top-level directory called "cron."  For example if you site is at:
 /var/lib/iHRIS/sites/mySite
you can do:


.. code-block:: bash

    cd /var/lib/iHRIS/sites/mySite
    mkdir -p cron
    


Now we want to create a shell script that will archive our reports from the command line.  To so:


.. code-block:: bash

     cd /var/lib/iHRIS/sites/mySite/cron
     gedit generate_reports_hourly.sh
    

This will open up an editor.  You want to add the following:


.. code-block:: bash

    #!/bin/bash
    reports="search_people"
    for report in $reports 
    do
        echo Archiving with /usr/bin/php ../pages//index.php --page=/CustomReports/generate_force/$report --nocheck=1
        /usr/bin/php ../pages//index.php --page=/CustomReports/generate_force/$report --nocheck=1
    done
    

then save and exit.  What this does is run through the list of reports (contained in the variable report) and generate them each individually

See iHRIS Botswana for an  `example <http://bazaar.launchpad.net/~ihris+botswana/ihris-manage/4.0/view/head:/cron/generate_reports_hourly.sh>`_ .


Creating A Shell Script (Nightly)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In your site customizations, create a new top-level directory called "cron."  For example if you site is at:
 /var/lib/iHRIS/sites/mySite
you can do:


.. code-block:: bash

    cd /var/lib/iHRIS/sites/mySite
    mkdir -p cron
    


Now we want to create a shell script that will archive **all**  reports from the command line.  To do so:


.. code-block:: bash

     cd /var/lib/iHRIS/sites/mySite/cron
     gedit generate_reports_nighly.sh
    

This will open up an editor.  You want to add the following:


.. code-block:: bash

    #!/bin/bash
    do
        echo Archiving with /usr/bin/php ../pages//index.php --page=/CustomReports/generate_force/ --nocheck=1
        /usr/bin/php ../pages//index.php --page=/CustomReports/generate_force --nocheck=1
    done
    

then save and exit.  This time, since we are generating all the reports, we did not need to list out each of the individual reports as the command will automatically try to generate them all.


Committing to bzr (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Of course we should commit our new shell script to bzr:


.. code-block:: bash

    cd /var/lib/iHRIS/sites/mySite
    bzr add cron
    bzr commit -m "added shell script to handle generation of reports"
    



Setting Up the Cron job
^^^^^^^^^^^^^^^^^^^^^^^
Now we need to tell our server to run the our new script, archive_reports.sh each month.  To do so we do:


.. code-block:: bash

    export VISUAL=gedit
    crontab -e
    

which will open up gedit.  We want to add the following line to the end of the file:


.. code-block:: bash

    50 * * * * cd /var/lib/iHRIS/sites/mySite/cron && bash generate_reports_hourly.sh
    10 2 * * * cd /var/lib/iHRIS/sites/mySite/cron && bash generate_reports_nightly.sh
    
    

save and quit.  

This says that we will run nightly report at 2:10 every morning.  The hourly report will get run at ten minutes before every hour.

Note, if you also set up [[Archive Reports Automatically |archiving of reports]] you will want to make sure that the nightly report generation has enough time to complete before starting the archiving.


Adding a New Report
^^^^^^^^^^^^^^^^^^^
Simply edit the file /var/lib/iHRIS/sites/mySite/cron/generate_reports_hourly.sh and add in the report to the list of reports in the reports variable.

Don't forget to do "bzr commit cron/generate_reports_hourly.sh -m 'added open position report'"


