Creating an iHRIS ISO
================================================

 **Note:** This contains out of date information

While I haven't yet found a way to create a single installation CD containing everything needed to install the complete system, the following method creates an "Update CD" for Ubuntu LTS that contains all the packages necessary to install iHRIS Manage as well as all Operating System Updates.  I used these steps to create `this ISO image <http://www.intrahealth.org/debian/ihris-installer.iso>`_.

I recommend using a freshly installed Ubuntu LTS system for this.  Using VMWare or `VirtualBox OSE <http://www.virtualbox.org/>`_ is useful for this.  Ubuntu's Gutsy release includes the <tt>virtualbox-ose</tt> that provides a GUI for setting up 

* Install apt-move (<tt>aptitude install apt-move</tt>).  This tool will take the package cache and build Debian archive that we can burn to disk.
* Change the <tt>COPYONLY</tt> in <tt>/etc/apt-move.conf</tt> so that it reads <tt>COPYONLY=yes</tt>
* Add the IntraHealth repository by editting <tt>/etc/apt/sources.list</tt> and adding the line: <tt>deb http://www.intrahealth.org/debian/ ./</tt>
* Download all the updates without installing them.  We avoid installing them to save time.  (<tt>apt-get update; apt-get --download-only update</tt>)
* Download all packages necessary to install ihris-manage and mysql-server. (<tt>apt-get --download-only ihris-manage mysql-server</tt>)
* Create the repository. (<tt>apt-move update</tt>)
* Set up Disk metadata. (<tt>mkdir /mirrors/debian/.disk; echo 'IntraHealth Updates' > /mirrors/debian/.disk/info</tt>)
* (Skipped: Creating a GPG key and signing the Release.  I want to have an official IntraHealth Key for this.  And I erased the one I used.)
* Create the ISO. (<tt>aptitude install mkisofs; mkisofs -r -A 'IntraHealth Update' -o intrahealth-update.iso /mirrors/debian/</tt>)
* Burn the ISO to Disk


On the target system
^^^^^^^^^^^^^^^^^^^^


* Add the disk's key to Apt's keyring.
* Add the disk to the list of disks available (<tt>apt-cdrom add</tt>)
* Install mysql-server (<tt>aptitude install mysql-server</tt>)
* Install ihris-manage (<tt>aptitude install ihris-manage</tt>)

(TODO: Figure out the keyring.  I would like to have one that "just works", but I want to do this the right way.)
[[Category:Archived Pages]]
