Using Alternate Sites in Windows iHRIS
======================================

==Overview ==

Version 3.1 of Windows iHRIS installs the default sites, but there is a command line argument that lets you specify an alternate directory to use for your site. This was added so that a country can reuse the installer and just specify an alternate site for whatever component they want. The idea is that the administator at a central office will specify their site with all of its customizations. Then they can just distribute to district offices a CD or a USB key with our installer and their site and a windows batch file to run the installer with the appropriate command line option, e.g:

       iHRIS-3.1.2 /components=ihrismanage /manageSITE=C:\manage_site /mysqlpass=something /silent

which will silently install the Windows iHRIS suite to ''C:\Program Files\ihris-suite'' and copy the contents of ''C:\manage_site'' to ''C:\Program Files\ihris-suite\sites\manage''.

Since you are allowed to get as complicated as they want with your site module, the site can then load whatever data you need, e.g., all the positions, facilities, district information, etc.  However, your site must be ''compatible'' with the standard wamp installation.  There is not a strict definition on what this means, rather your site should not very too much from the standard blank installation.  This is because the installer comes with a database pre-configured/pre-installed with what is essentially a blank installation.  Your site module will be an update to this installation.

==Making a Compatible Module==
We will look at the changes needed to make the [[http://bazaar.launchpad.net/~ihris%2Buganda/ihris-uganda/ug-manage/files/5?start_revid=5 Uganda customization ]] of iHRIS Manage compatible for the windows installer.  Let us assume that you already have a copy of these files sitting at ''c:\manage_installer\site''.  

===Adding Database Access===
Browse to the [[http://bazaar.launchpad.net/~intrahealth%2Binformatics/offline-ihris/3.1/files wamp installer]] on Launchpad, 
and download the file ''source/local_configs/config.values.php_ihris-manage.install''.  This file should be saved to ''C:\manage_installer\site\pages\local\config.values.php.install''.  You don't need to worry about editing this file, as the installer will substitute values as appropriate.

===Changes to the site module file===
The first thing we will need to do is to move the file ''c:\manage_installer\site\iHRIS-Manage-UG.xml'' to ''c:\manage_installer\site\ihris-manage-Wamp.xml.install''.  Now, open the file ''c:\manage_installer\site\ihris-manage-Wamp.xml.install'' with your favorite editor.  
====Change the site module name====
We need to change the name of the site module to be the name of the site module that the WAMP install expects.  We do this by changing the line:
<pre>
    <I2CEConfiguration name='ihris-manage-site-ug'>
</pre>
to:
<pre>
    <I2CEConfiguration name='ihris-manage-site-wamp'>
</pre>
and the line 
<pre>
    <configurationGroup name='ihris-manage-site-ug'>
</pre>
to:
<pre>
    <configurationGroup name='ihris-manage-site-wamp'>
</pre>
====Adding in paths====
Now we need to add in a paths to point to the ihris installation.  Look for the lines
<pre>
    <path name='modules'>
      <value>./modules</value> 
    </path>
</pre>
and change them to:
<pre>
    <path name='modules'>
      <value>./modules</value> 
      <value>WAMPROOTREGULAR\lib\ihris</value>
    </path>
</pre>
Note the ''WAMPROOTREGULAR'' will be changed to the installation directory (''C:\Program Files\ihris'' by default) by the installer.
====Adding in Configuration Data====
Just after the lines (that you changed):
<pre>
 <configurationGroup name='ihris-manage-site-wamp'>
   <displayName>iHRIS Manage Uganda Site</displayName>
   <status>advanced:false</status> 
</pre>
We need to add in the following lines:
<pre>
   <status>overwrite:true</status>
   <configuration values='single' name='mime_types' path='/modules/FileDump/mime_types'>
      <displayName>The location of the mime.types file</displayName>
      <description>The mime.types file is a standard file on a unix system, usually located in /etc/mime.types, which
      describes the type of a file based on its extension.
      </description>
      <status>required:true</status>   
      <value>WAMPAPACHEROOT\conf\mime.types</value>
    </configuration>
    <configuration name='php_executable' path='/modules/BackgroundProcess/php_executable/windows' values='single'>
      <displayName>Windows Binary</displayName>
      <description>The binary to use to execute a php script from the command line in windows</description>
      <value>WAMPPHPROOT\php.exe</value>
    </configuration>
    <configuration name='log_dir' values='single' path='/modules/BackgroundProcess/log_dir'>
      <displayName>Log Directory</displayName>
      <description>The directory that we attempt to ouput error messages from the background process to </description>
      <status>required:false</status>
      <value>WAMPROOTREGULAR\tmp\I2CE_BackgroundProcess</value>
    </configuration>
</pre>
The ''WAMPPHPROOT'' will be replaced by the installer with the directory ih which the php executable resides, while ''WAMPAPACHEROOT'' will be replaced with directory in which the installer put Apache.

==Testing==
Verify that your changes worked by running
 C:\manage_installer\iHRIS-3.1.2 /components=ihrismanage /manageSITE=site /log=install.log
If something failed, please send us a copy of the file ''c:\manage_installer\install.log'' as well as the contents of the directory ''c:\manage_installer\site'' so that we can trouble-shoot.

==Making a USB Disk-On-Key==
So you have tested out the windows installation, and you want to load the installer with your site on a USB Flash Drive (or CD) to be distributed to various districts.   You want make an installer, that they pop-in and it will install iHRIS Manage automatically.  Let's create a directory , say ''C:\manage_installer'',  which will put the contents of our USB drive.  

First the pretty stuff -- browse to the [[http://bazaar.launchpad.net/~intrahealth%2Binformatics/offline-ihris/3.1/files wamp installer]] on Launchpad, and download the file ''home/ihris-suite.ico'' to ''C:\manage_installer\autorun.ico''.

Now create a file called ''C:\manage_installer\autorun.inf'' with the contents:
<pre>
[autorun]
open=install.bat
icon=autorun.ico
action=Install Uganda iHRIS Manage
shell\install=Install Uganda iHRIS Manage
shell\install\command=install.bat
shell=install
label=Windows iHRIS Manage Installer
</pre>

Now create a file called ''C:\manage_installer\install.bat'' with the contents:
<pre>
iHRIS-3.1.2 /silent /components=ihrismanage /manageSITE=site /mysqlpass=WHATEVER /smtp=smtp.myserver.org /tasks=quicklaunchicon,desktopicon
</pre>

When the user pops in the USB-drive (or CD) it will install your customized version of iHRIS Manage.  It will set the root mysql password to ''WHATVER'' (see [[Windows Security]]) and set the smtp server to be used to ''smtp.myserver.org''.  Additionally, it will add an icon to the desktop and quicklauch bar.

==Command Line Options==
The Windows installer was made using [[http://www.innosetup.com/isinfo.php Inno Setup]] and so there are some command line options for the installer that it provides automatically.  These can be found described [[http://www.chmlib.com/ISetup/topic_setupcmdline.htm here]] and we have used several of them above.  There are four optional components which can be specified by ''/components''
#ihrismanage  -- The iHRIS Manage Software
#ihrisqualify -- The iHRIS Qualify Software
#ihrisplan -- The iHRIS Plan Software
#phpmyadmin -- phpMyAdmin
There are also three tasks which can be specified via ''/tasks''
#autostart -- Starts up mysql and apache when the computer is turned on 
#quicklaunchicon  -- Adds an icon to quick launch bar to run the software
#desktopicon -- Adds a desktop icon to launch the software

Some additional options are:
*/smtp=XXXX   -- the smtp server used for outgoing mail
*/mysqlpass=XXXX -- the root password used for mysql
*/LocalInstall=X -- either 0 or 1.  If set to 1, the defualt, then software is only available on the machine it is installed on (localhost). If set to 0, then the software is available to any computer on the network.

There are some others such as specifying the port that mysql and apache are listening on:
*/apacheport  -- Defaults to 8081
*/mysqlport -- Defaults to 8082
[[Category:Archived Pages]]
