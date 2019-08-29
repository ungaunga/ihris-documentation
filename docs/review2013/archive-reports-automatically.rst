Archive Reports Automatically
=============================

This tutorial shows you how to archive reports automatically.  

Please make sure you have enabled the Report Archive module before proceeding.

The first step is to determine the list of reports that you want archived.  More precisely it is the report views that you want saved. You should also determien the frequency that you want them archive them on.  In this example, based on iHRIS Botswana,  we show you how to setup monthly archiving of selected reports.

==Getting the Report Views==
You should first create a list of the report views that you want to archive.  For each of the report views that you want you can get the name/index of the report view from the URL.  Form example, if the report you are interested is at:
 http://localhost/iHRIS-manage/CustomReports/show/facility_list
then the name of the report view is 
 facility_list

In the example below we will suppose our list of reports views we wish to archive are:
 facility_list 11238232 search_people

Note: this saves the default "export" of the report, which is usually an spreadsheet.  So if you select a report view which is a graph, you will archive the underlying data rather than the graph itself.

==Creating A Shell Script==
In your site customizations, create a new top-level directory called "cron."  For example if you site is at:
 /var/lib/iHRIS/sites/mySite
you can do:
<source lang='bash'>
cd /var/lib/iHRIS/sites/mySite
mkdir -p cron
</source>

Now we want to create a shell script that will archive our reports from the command line.  To so:
<source lang='bash'>
 cd /var/lib/iHRIS/sites/mySite/cron
 gedit archive_reports.sh
</source>
This will open up an editor.  You want to add the following:
<source lang='bash'>
#!/bin/bash
reports="facility_list 11238232 search_people"
for report in $reports 
do
    echo Archiving with /usr/bin/php ../pages/index.php --page=/CustomReports/archive/$report --nocheck=1
    /usr/bin/php ../pages/index.php --page=/CustomReports/archive/$report --nocheck=1
done
</source>
then save and exit.  What this does is run through the list of report views (contained in the variable report) and archives them each individually



See iHRIS Botswana for an [http://bazaar.launchpad.net/~ihris+botswana/ihris-manage/4.0/view/head:/cron/archive_reports.sh example].

==Committing to bzr (Optional)==
Of course we should commit our new shell script to bzr:
<source lang='bash'>
cd /var/lib/iHRIS/sites/mySite
bzr add cron
bzr commit -m "added shell script to handle archiving reports"
</source>

==Setting Up the Cron job==
Now we need to tell our server to run the our new script, archive_reports.sh each month.  To do so we do:
<source lang='bash'>
export VISUAL=gedit
crontab -e
</source>
which will open up gedit.  We want to add the following line to the end of the file:
<source lang='bash'>
0 4 1 * * cd /var/lib/iHRIS/sites/mySite/cron && bash archive_reports.sh
</source>
save and quit.  This says that we will run the command on the first day of the month of every month at 4:00am.

==Adding a New Report==
Simply edit the file /var/lib/iHRIS/sites/mySite/cron.archive_reports.sh and add in the report view to the list of report views in the reports variable.

Don't forget to do "bzr commit cron/archive_reports.sh -m 'added age distribution report'"

[[Category:Reports]][[Category:Review2013]]
