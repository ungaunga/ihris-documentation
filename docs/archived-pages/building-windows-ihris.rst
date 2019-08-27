Building Windows iHRIS
================================================


Overview
^^^^^^^^
This page describes how to build a customized windows installer.  The installer is built on a windows machine using the `Cygwin <http://www.cygwin.com>`_ linux like environment for windows.  

It is *highly recommended* that you build the installer in the default installation directory which is: 
 C:\Program Files\ihris-suite
so you should un-install the ihris-suite if you have installed on the computer that wish to build the installer on and remove this directory.  All the files paths/directories below are assuming you made this choice.  This is done so that when the installer is run, it does not have to spend time to reconfigure itself to its new location.


Installing Cygwin
^^^^^^^^^^^^^^^^^
In order to build a windows installer, you must have a `cygwin <http://www.cygwin.com>`_ installed on your computer.  To do this, download and run `setup.exe <http://www.cygwin.com/setup.exe>`_.  You can find detailed instructions `here <http://cygwin.com/cygwin-ug-net/setup-net.html>`_.  You will
need to install the following packages:


* wget
* make
* tar
* unzip
You may wish to follow this `tutorial <http://www.physionet.org/physiotools/cygwin/>`_ for installing cygwin, except you should install the following package instead of the one listed in their Step 9.


Getting the installer files
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Open a cygwin shell.  You can do this by clicking on the cygwin icon on your desktop, or by going to *Start*->''Programs''->''Cygwin''->''Cygwin Bash Shell''.   A window will appear with a prompt **$**.  At the prompt enter the following commands
 cd /cygdrive/c/Program\ Files
 bzr checkout lp:offline-ihris/4.0 ihris-suite
 cd ihris-suite 
Edit the make file:
 nano Makefile 
to update the following lines (replacing X with the minor version):
 i2ce-LAUNCHPAD=4.0.X-release
 ihris-common-LAUNCHPAD=4.0.X-release
 ihris-manage-LAUNCHPAD=4.0.X-release
 ihris-qualify-LAUNCHPAD=4.0.X-release
 textlayout-LAUNCHPAD=4.0.X-release
and now you may run:
 make all

Assuming all goes well, you should have a windows installer under:
 C:\Program Files\ihris-suite\Output\iHRIS-4.0.X.exe
The version may be different.


Customizing The Installer
^^^^^^^^^^^^^^^^^^^^^^^^^
Before you begin customizing the installer, you should see if [[Using Alternate Sites in Windows iHRIS]] will meet your needs.  You will want to build a custom installer if you have large amounts of data that you want shared among multiple installations, if you have customized your site so that is significantly different from the standard wamp installation, or if you want have a custom home page.

All of these customizations are done by adding some files under *C:\Program Files\ihris-suite* before you enter the command *make* as above.


Running SQL Scripts/Importing Data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In order that the installer runs fast, each of the sites (Manage, Qualify, Plan) are pre-initialized in the installer so that the database is already populated.  You may wish also to pre-initialize the installer by running a sql script (or few) to import large amounts of data into your custom installation -- for example if you did a mysqldump of data that should be shared among district offices.  You may add sql scripts to be in the following directories:
 C:\Program Files\ihris-suite\databases\ihris-manage
 C:\Program Files\ihris-suite\databases\ihris-plan
 C:\Program Files\ihris-suite\databases\ihris-qualify
These scripts are run after the site has been (pre-)initialized.


Building a Customized Site Into the Installer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
For any of the components of the iHRIS Suite, you can build a custom site into the installer.  This is done by putting a custom site in the locations:
 C:\Program Files\ihris-suite\site\ihris-manage
 C:\Program Files\ihris-suite\site\ihris-manage
 C:\Program Files\ihris-suite\site\ihris-qualify
(depending on which site you have a customization for).

Once you have a custom site built, say on a linux server, you will need to prepare the site for the windows installer.  To do this, copy your custom sites to the appropriate directory above.   Then you will need to roughly follow the directions in [Using Alternate Sites in Offline iHRIS], especially paying attention to the files that end with *.install*.  You will also need to copy your site configuration file to *ihris-manage-wamp.xml* which is the configuration file used to pre-initialize your site.  You will need to make sure that the paths to i2ce are correct.  Edit *ihris-manage-wamp.xml* and make sure you have something akin to:
 <path name='modules'>
   <value>./../../lib/ihris/</value>
 </path>
You will also need to edit *pages/local/config.values.php* so that it the *$i2ce_site_i2ce_path* is as follows:
 $i2ce_site_i2ce_path = "../../../lib/ihris/i2ce";
Finally, make sure that you do not have any "pages/.htaccess" files and that the "pages/config.values.php" file does not have any values set.

If you are making an install CD/USB Disk on Key for your custom installer as in [Using Alternate Sites in Offline iHRIS], you will not need to copy your site directory over, nor will you need to specify the command line parameter /manageSITE as it is already built into the installer.


Changing the Home Page
~~~~~~~~~~~~~~~~~~~~~~
The default home page for the apache web server that will be running on the installed machine is contained in the directory
  C:\Program Files\ihris-suite\home
If you wish to change the home page provided, create the directory
  C:\Program Files\ihris-suite\althome
and make sure that it contains *index.html*.  When you build the installer, it will use this web root.
[[Category:Archived Pages]]
