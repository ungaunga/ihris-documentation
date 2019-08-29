SDMX-HD Data Export -- Kenya
============================

==Background Information==
iHRIS and DHIS are established systems in Kenya.  The Ministry maintains a facility list, the Master Facility List (MFL).  There are approximately 7000 facilities. In addition iHRIS is considered the canonical source of the job list, of which there are approximately 300.  In the case of Kenya, it was decided that exporting data at the level of job provided too much granularity.  It was decided to create a "Job Group" of approximately 20 groups to categorize the jobs.  This list was defined by the Ministry, but will be maintained in iHRIS.  At this time, no gender disaggregation has been requested by the ministry.

===Expected Data Use Scenarios===
Export (#hws, job group, facility)

==Where's the code==
There are two code branches in use:
#The general interoperability tools which assist in producing the DSD, and other various xml files for various input sources (spreadsheets), can be found at [https://code.launchpad.net/~his-interop/his-transform-tools/trunk lp:his-transform-tools ] 
#The data lists and needed transforms for Kenya can be found at [https://code.launchpad.net/~his-interop/kenya-sdmx-hd/trunk lp:kenya-sdmx-hd]
Access control is via the [https://launchpad.net/~his-interop HIS Interoperability team]

==Code Structure==

There are four main directories in lp:kenya-sdmx-hd.  In lp:lp:his-transform-tools there is a PHP script "runme.php" which processes these four directories according to the following logic.
*inputs:  this contains a series of [[#.csv|Linking the Data]] files which are the data lists.  As an intermediary step, runme.php produces a file lists.xml which converts the .csv or excel spreadsheets into a simple xml file for further XSLT processing.  
**inputs/job.csv:  This is a .csv dump of the hippo_job table from iHRIS.   As new jobs are added/job titles are edited, the hippo_table file can simply be exported and then the runme.php script will update the DSD with the new job code lists.  
**inputs/jobgroup.csv  This is/will be a .csv dump of the hippo_cl_jobgroup table which maintains the list of jobgroups in iHRIS.  
*transforms:   The files here are used to generate the DSD, the xsd's and what other xml based files needed by the various systems.
*transforms_dsd.  This directory contains the XSL which will operate directly on the DSD. 
*outputs -- this is where are the results are.  


Note, runme.php of this is setup to to work without any assumptions about about which systems are involved.  It can happily handle openMRS, iHRIS and DHIS all reporting on similar but not necessarily identical data.

==lists.xml==
As an intermediary step, runme.php converts the .csv files and excel files into one large .xml file for processing.  It has the structure as defined [[SDMX-HD Data Export -- Zanzibar#lists.xml | here]]

Each worksheet in each Excel spreadsheet is made into a ''List'' with the name of that worksheet.

==The DSD==
This is generated from [[SDMX-HD Data Export -- Zanzibar#lists.xml | lists.xml]] via the file:
#transforms/DSD/DSD.xml.xsl

==Schema==
The DSD will define two KeyFamilys.  The validator for exports via CrossSectionalDataSets is produced via:
*transforms/schemas/KF_HW_JOBGROUP_FAC.xsd.xsl
*transforms/schemas/KF_HW_JOB_FAC.xsd.xsl

==iHRIS==
All the transforms and setup files are maintained in transforms/iHRIS.  The results are in outputs/iHRIS.  The directory outputs/iHRIS is a container module for the four modules that are required for reporting.  One module adds in the jobgroup data list.  One module maps each job to a jobgroup.  There are two reporting modules.  One is for (#hws,fac,job) one is for (#hws,fac, job group).  DHIS is primarily interested in the later report.

===iHRIS: Pre-Installation===
You will need to add to php libraries/modules to perform XSLT and zipping:
<source lang='bash'>
sudo apt-get install apt-get libphp-pclzip php5-xsl
sudo /etc/init.d/apache2 restart && sudo /etc/init.d/memcached restart
</source>

===iHRIS: Code Installation===
You can follow these instructions to get the HIS Intereoperability tools for Kenya:
<source lang='bash'>
cd /var/lib/iHRIS/
mkdir -p interop
sudo chown `whoami`:`whoami` interop
cd /var/lib/iHRIS/interop
bzr branch lp:kenya-sdmx-hd
sudo ln -s /var/lib/iHRIS/interop/kenya-sdmx-hd/outputs/iHRIS /var/lib/iHRIS/lib/4.0.16/kenya-interop
</source>
Note, you should adjust the /var/lib/iHRIS/lib/4.0.16 path in the last line according to your installation.

===iHRIS: Enabling the Modules===
The kenya interoperabiltiy modules should now be available to the system:
*Go to "Configure System"
*Go to "Configure Modules"
*Check the check box next to "Kenya HIS Interoperability"
*Click the "Enable" button
Please note, this ''should'' be all that you have to do, but there is a bug in the enabling of modules.  So please follow the next steps.
*Click on the "Sub-modules" link to the right of "Kenya HIS Interoperability"
*Check all four of the check boxes that can be checked:
**CodeList Job Group SDMX-HD
**CodeList Job Group Map SDMX-HD
**HW by Facility and Job Report 
**HW by Facility and Job Group Report)
*Click on the "Enable" button"

===iHRIS: Export Report===
Once you have enabled the module, you should be able to export the SDMX-HD report for (#hws,jobgroup, facility) by simply clicking on the report named, '''SDMX-HD Export: Health workers by job group per facility'''

==DHIS2==
==Issues to Address==
#Please add to me

[[Category:SDMX-HD]][[Category:Kenya]]
