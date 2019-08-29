Linux (Ubuntu) Installation - 4.0.22
====================================

This page contains installation instructions on installing iHRIS version 4.0.22 manually.
{{otherversions|Linux (Ubuntu) Installation}}

<center>'''Need help?'''  Try our [[Project Communication]]</center>

You may wish to see instructions on how to install [[Installing the Debian Packages |debian packages]] for a simpler installation process.

== Supporting Software ==

First you should install Ubuntu and all the supporting software required by iHRIS by following the [[Linux (Ubuntu) Installation - Supporting Software]] instructions.

'''Note:''' Installing on ext4 filesystem?  see [http://ubuntuforums.org/showthread.php?t=1313834 this]

'''Note:'''  Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with '''sudo''' it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

'''Note:'''  Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

'''Note:'''  Some commands will launch the '''gedit''' file editor.  Look at the [https://help.ubuntu.com/community/gedit documentation] if you need additional help.

== Downloading the Full iHRIS Suite ==
Before proceeding with iHRIS Manage or iHRIS Qualify installation, we will want to download the most recent version of the full iHRIS Suite.  To download the software you enter these commands:
<source lang="bash">
sudo mkdir -p /var/lib/iHRIS/lib/4.0.22
cd /var/lib/iHRIS/lib/4.0.22
sudo wget http://launchpad.net/i2ce/4.0/4.0.22/+download/ihris-suite-4.0.22.tar.bz2
sudo tar -xjf ihris-suite-4.0.22.tar.bz2
</source>

== Installing the Software ==

Follow the [[iHRIS Manage Installation - 4.0.22|iHRIS Manage Installation]] instructions for iHRIS Manage.

Follow the [[iHRIS Qualify Installation - 4.0.22|iHRIS Qualify Installation]] instructions for iHRIS Qualify.

Follow the [[IHRIS Plan Installation - 1.0.4|iHRIS Plan Installation]] instructions for iHRIS Plan.  (You do not need to download the full iHRIS Suite above)

[[Category:Developer Resources]]
