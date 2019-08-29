Decentralized iHRIS Deployment:Options for Data Transfer
========================================================

In the decentralized iHRIS deployment, there exists one challenge on the options for data transfer from the peripheral sites to the central sites.

 `This <http://wiki.ihris.org/wiki/Decentralized_iHRIS_Structure>`_  article details the way you can achieve the decentralized structure.


Database Settings and Transfer Options
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In setting up the database, 

* Each peripheral site is going to have its own database set as explained in the installation manual.
* The central database will be pre-loaded with standard lists only.
* There have to be a database for each peripheral site at the central server where we will restore the dumped sql ('''mysqldump''') file from the peripheral sites. Then, following the structure of  `this file <http://bazaar.launchpad.net/%7Eihris%2Bcssc/ihris-manage/data-import-4.0/annotate/head%3A/sites/FormStorage_central.xml>`_  the central system is going to read data from the different peripheral databases created at the central site for aggregating.

Manual Data Transfer
~~~~~~~~~~~~~~~~~~~~
One option would be to have a person move to the peripheral site and dump the database into a file and then take this file with them to the central site where it is going to be integrated into the central database as explained in [[Decentralized_iHRIS_Deployment:Options_for_Data_Transfer#Database Settings and Transfer Options]].

As iHRIS was developed with the idea of being deployed in developing countries in mind where in most cases there is a very limited or there not an internet connectivity, so the manual process of transferring data in this case would obviously be manual: one having to travel all the way to the different peripheral sites to collect the data in a flash disk and bring them to the central site.


Automated/Remote Data Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* '''Requirements'''
The main requirements for the automated system of doing the backup and transfer of data is only possible when there is internet connection at the peripheral site and that the appliance at the peripheral site has to be fixed with a Public IP Address. The public IP address can be obtained from any ISP (Internet Service Provider) in the country. It is the public IP address makes it possible to access the appliance from any point around the world.



* '''The Process'''
* *Using cron jobs
* *:The system administrator sets up a cron job at each peripheral site which will run at a specified time to do the backup of the database and transfer this backup file to the central site where it is going to be added to the central database.
* *Manually running the backup procedure
* *:Instead of using the cron jobs, the system administrator can just run the dump process for each peripheral site and transfer the file to the central site via SSH.


Launchpad Customizations
^^^^^^^^^^^^^^^^^^^^^^^^
Launchpad customizations will only be for the two sites, the peripheral site (regional) and the central site.
Each peripheral site installs the same customizations (the regional customizations) ad sets the variables based on their preferences including the database names and the passwords and the module configurations.

There are not going to be specific customizations for each regional (peripheral site) in the country.

