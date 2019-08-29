Linux (Ubuntu) Installation - 4.0.18
====================================

This page contains installation instructions on installing iHRIS version 4.0.18 manually.
{{otherversions|Linux (Ubuntu) Installation}}

You may wish to see instructions on how to install [[Installing the Debian Packages |debian packages]] for a simpler installation process.

 *Warning:*  See [[Installing iHRIS on Ubuntu 10.4 (Lucid)|Installing iHRIS on Ubuntu 10.4 or 10.10]] after completing these instructions to get iHRIS working on the latest release of Ubuntu.

<center>'''Need help?'''  Try our [[Project Communication]]</center>

Getting Ready
^^^^^^^^^^^^^

First you should install Ubuntu and all the supporting software required by iHRIS by following the [[Linux (Ubuntu) Installation - Supporting Software]] instructions.

Optionally, you can install [[HowTo: Install Memcached|Memcached]] to speed up your site.

 **Note:**   Unless specifically mentioned, all the commands below are run using a terminal.  You can start this in Ubuntu by going to Applications -> Accessories -> Terminal.  Any time a command begins with **sudo**  it will prompt for your password because this will be run with administrative privileges.  When you run sudo multiple times, only the first time will ask for your password.

 **Note:**   Some installation commands will prompt for inputs in the terminal window, usually with a blue background.  The mouse doesn't work to click on options here.  You can use Tab to move between options and the space bar to check or uncheck selections.

 **Note:**   Some commands will launch the **gedit**  file editor.  Look at the  `documentation <https://help.ubuntu.com/community/gedit>`_  if you need additional help.

Downloading the Software
^^^^^^^^^^^^^^^^^^^^^^^^
To download the software you enter these commands:

.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/lib/4.0.18
    cd /var/lib/iHRIS/lib/4.0.18
    sudo wget http://launchpad.net/i2ce/4.0/4.0.18/+download/ihris-suite-4.0.18.tar.bz2
    sudo tar -xjf ihris-suite-4.0.18.tar.bz2
    

Installing the Software
^^^^^^^^^^^^^^^^^^^^^^^

Follow the [[iHRIS Manage Installation]] instructions for iHRIS Manage.

Follow the [[iHRIS Qualify Installation]] instructions for iHRIS Qualify.

