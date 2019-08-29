LiveCD Notes
============

See  `the Ubuntu LiveCD page <https://help.ubuntu.com/community/LiveCDCustomization>`_  for details.  This page just outlines the steps particular to the iHRIS LiveCD


New Notes -- Sierra Leone
^^^^^^^^^^^^^^^^^^^^^^^^^


* install php-xsl gstreamer0.10-ffmpeg gstreamer0.10-plugins-bad php5-uuid


Source
^^^^^^

The image used to create this CD is stored on ihrisdev under <tt>/home/mah/ihris-live</tt>.  Use rsync to copy the structure there to your work area.

   sudo env SSH_AUTH_SOCK=$SSH_AUTH_SOCK rsync -a --numeric-ids \
            --progress hrisdev.intrahealth.org:/home/mah/ihris-live/ ihris-live/


Scripts
^^^^^^^

I've written a few simple scripts to automate some of the tedious steps.  These are located directly under ihris-live:

<tt>edit-chroot</tt>
:: This will drop you into a properly configured chroot that is, for all intents and purposes, the filesystem that the LiveCD will use.  After you exit, you'll be returned to your command prompt.

 **NOTE:**  If you try to run MySQL from chroot, you'll run into problems if you already have an instance of MySQL running on your workstation since it will try to listen on the same port.  Other processes, like Apache will also cause conflicts.
<tt>make-iso</tt>
:: After running <tt>edit-chroot</tt>, use this script to create the ISO.

The other scripts should not be necessary for regular use.


Of Note
^^^^^^^

A user is created from the contents of <tt>/etc/skel</tt> when the LiveCD begins running.  Anything you put in here will be in the LiveCD user's environment.  Here is a list of notable modifications to this environment:


Mark's Image
~~~~~~~~~~~~
 `R-Kiosk plugin <https://addons.mozilla.org/en-US/firefox/addon/1659>`_ 
::A <tt>.mozilla</tt> directory is set up with the R-Kiosk plugin installed.  I had to edit the <tt>.mozilla/firefox/d0i2gqoj.default/extensions/{4D498D0A-05AD-4fdb-97B5-8A0AABC1FC5B}/install.rdf</tt> file and change <tt>em:maxVersion</tt> from “3.0” to “3.0.*” to get the kiosk plugin to work on boot-up

<tt>.xsession</tt> file
::Firefox is started without a window manager running.  When it exits, the user is (currently) returned to the GDM login screen.


Steps for how Mark made the image
---------------------------------



* Source: http://mirrors.kernel.org/ubuntu-releases/jaunty/ubuntu-9.04-desktop-i386.iso
 # mkdir tmp
 # mount -o loop ubuntu-9.04-desktop—i386.iso tmp
 # mkdir extract-cd
 # tar -C tmp -c . | tar -C extract-cd -x 
 # umount tmp
 # rmdir tmp
 # aptitude install squashfs-tools
 # unsquashfs -dest edit extract-cd/casper/filesystem.squashfs
 # sudo ./edit-chroot
 # dpkg-query -W --showformat='${Package}\n' | grep openoffice | xargs aptitude purge -y
 # aptitude purge gnome-games gnome-games-data ubuntu-desktop gimp libgimp2.0 gimp-data gimp-help-en xsane \
                  evolution evolution-common evolution-plugins evolution-indicator evolution-exchange \
                  ekiga evolution-data-server \
                  evolution-documentation-en evolution-data-server \
                  evolution-documentation-en f-spot gnome-games-data \
                  gnome-games pidgin gnome-games pidgin-otr pidgin-libnotify
 # echo deb http://ppa.launchpad.net/intrahealth+informatics/ppa/ubuntu jaunty main > /etc/apt/sources.list.d/ihris.list
 # echo deb http://archive.ubuntu.com/ubuntu jaunty multiverse >> /etc/apt/sources.list.d/ihris.list 
 # apt-key adv --recv-keys --keyserver pgp.mit.edu AD9110AD7B0B5CB8EA7004C62380F43F6EC21546 


* policy-rc.d is used to tell init scripts not to run (See  `the spec <http://people.debian.org/~hmh/invokerc.d-policyrc.d-specification.txt>`_ )
 # cat > /usr/sbin/policy-rc.d
  #!/bin/sh
  exit 101
  ^D
 # chmod +x /usr/sbin/policy-rc.d
 # aptitude update
 # aptitude dist-upgrade
 # aptitude install flashplugin-installer


* if kernel was upgraded (look under chroot's /boot)
* * aptitude purge old version
* * outside of chroot:
 # cp edit/boot/vmlinuz* extract-cd/casper/vmlinuz
 # cp edit/boot/initrd* extract-cd/casper/initrd.gz


* If proc or sys won't umount from the chroot, try turning off klog
* `Download <http://www.capacityproject.org/hris/hris-toolkit/hris-toolkit.zip>`_  and extract toolkit to extract-cd/ihris-live/toolkit
* `Download <http://www.ibiblio.org/litlfred/ihris/ihris_demo.zip>`_  and extract touch demo to extract-cd/ihris-live/demo
* Get the updated Resources PDFs from Carol and extract to extract-cd/ihris-live/resources



EOP Image
~~~~~~~~~
It is on hrisdev:~/litlfred/eop_live_dvd.tar.gz  (gzipped w/ --rsyncable)
It is based on mark's image with the changes as detailed below.
I updated make-iso to clean out the log and temporary files.


* under chroot:
* *uncomment all the #deb lines in /etc/apt/sources.list
* *apt-get install flashplugin-nonfree evince
* created edit/usr/share/i2ce/lib/3.0
* unpacked the ihris-suite-full-3.1.4.tgz in edit/usr/share/i2ce/lib/3.0
* database setup **chroot** :
* *kill mysqld *before*  chroot.
* *sudo ./edit-chroot (the rest of this bullet is under chroot)
* *start mysqld (mysql root user has no password)
* *a2enmod rewrite
* *edit /etc/apache2/sites-available/000-default so that /var/www has overide all set
* *ihris_* tables in database were dropped.
* *for each of the $software in manage,qualify,plan
* **ln -s /usr/share/i2ce/lib/3.0/ihris-$software/sites/Demo/pages /var/www/$software
* **cd /var/www/$software
* **cp htaccess.template .htaccess  -- and edit to so docuement root is /$software
* **mkdir -p local
* **cp config.values.php local/config.values.php
* **vi local/config.values.php:
* ***setup the database user, password, path to i2ce, path to site config file
* **php index.php
* extract-cd/isolinx/splash.pcx -- changed unbuntu icon to ihris
* under in edit/
* *etc/skel
* **removed the .xsession file from mark's image
* **The r-kiosk plugin  from mark's was removed.
* **in .mozilla/firefox/d0i2gg0j.default/pref.js:
* ***added in "user_pref("toolkit.networkmanager.disable", true);" so that firefox does not keep switching to work-offline mode
* **in .mozilla/firefox/d0i2gg0j.default/extensions.ini:
* ***removed the line enabling the r-kiosk
* **changed examples.desktop to:
 [Desktop Entry]
 Version=1.0
 Type=Link
 Name=iHRIS Demo
 Comment=Live iHRIS Demo
 URL=http://localhost
 Icon=/var/www/ihris_logo.png


* *var/www has:
* **index.html which links the demo, toolkit, resources and the iHRIS software
* **supporting image files for index.html
* **ihris_logo.png (used in the desktop link above)
* **demo/  - a directory containing the touch demo
* **resource/ - a directory with the hr strengthening news briefs
* **toolkit/ - a directory containing the hris strengthening toolkit
* added in extract-cd/
* *autorun.inf
* *autorun.ico
* *index.html a file identicial to the one in edit/var/www/index.html except:
* ** clicking on manage, qualify, etc says to reboot with the dvd in the drive
* **added the magical <!-- saved from url=(0016)http://localhost --> so that explored does not complain
* *supporting image files for index.html
* *demo/  - a directory containing the touch demo
* *resource/ - a directory with the hr strengthening news briefs
* *toolkit/ - a directory containing the hris strengthening toolkit
* *isolinux/lang:
* **created and added the line 'en' so that the defaul language is english
* **set the timeout to 50 (5 seconds)
* *isolinux/test.cfg -- changed the menu option so that 'Try iHRIS Live' is the only thing shown
* *isolinux/langlist -- removed everything except
* *isolinux/isolinx.cfg  set timeout to 50 (5 seconds)
* under sudo ./edit-chroot
* *apt-get clean
* *dpkg-reconfigure gdm (gdm was spitting us out to busybox)
* *mkinitramfs -o /initrd.img 2.6.28-15-generic (don't know if this was needed but probably was)



EOP label
~~~~~~~~~
http://www.ihris.org/w/upload/IHRIS_Live_CD_402.pdf


Always update the Illustrator file with the current version info. Carol has the Illustrator file as it cannot be uploaded to this wiki.


To Do
^^^^^


* fixup the desktop icon to launch the ihris suite (done by carl).
* Change the progress bar boot branding ( `usplash <http://news.softpedia.com/news/Change-Ubuntu-Bootsplash-Theme-55237.shtml>`_ )
* skip the gdm user login
* set a desktop  `background <https://help.ubuntu.com/community/LiveCDCustomization#Custom%20Background%20for%20GNOME>`_
* add in a page/add to index.html about contacting us, the projects, where to find the software.
* remove emacs backup ~ files.
* redo the ihris icon on the boot image (extract-cd/isolinux/splash.pcx) so that the icon looks better on a black backround.  maybe also change the text to say iHRIS instead of ubuntu.  do we need other branding here e.g. capacity/usaid?
* when all the .deb demo packages for ihris are done, use those to populate the database
* make it boot  `faster <http://lichota.net/~krzysiek/projects/kubuntu/dapper-livecd-optimization/>`_
* incorporate the wiki
* make a usb version w/ reserved space for a permanent storage
[[Category:Project Team Resources]][[Category:NeedsReview]]
