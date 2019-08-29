Software Repository Mirror
==========================

This article describes how to create a repository of the Ubuntu software.  This would be useful for downloading the Ubuntu software library to a hard drive for installation of Ubuntu when there is a slow internet connection (or none at all).

This has been adapted from [https://help.ubuntu.com/community/Debmirror these instructions].  You will need a 200GB external hard drive that you can reformat.

'''WARNING:''' This has not been fully tested.  Please correct or send feedback to "litlfred@ibiblio.org"

==Preparing the Hard Drive==
In the directions below we will assume that you have a brand new hard drive.  We will be formatting the hard drive (partition) which means that all of the data on the hard drive will be lost.
'''PLEASE MAKE SURE YOU KNOW EXACTLY WHAT YOU ARE DOING IN EACH STEP'''

To format the partition, we will first need to set the partition type 

===Determining the Hard Drive Paritition===
To format the hard drive, we first to know what "partition" it is using.  Ubuntu should automatically mount the hard drive should automatically once you plug it in.  To determine run the command:
 mount | grep media
Running this on my machine, I see output
 '''/dev/sdb1''' on /media/3539-6663 type vfat (rw,nosuid,nodev,uid=1000,gid=1000,shortname=mixed,dmask=0077,utf8=1,showexec,flush,uhelper=udisks)
Which means the '''/dev/sdb1''' is the partition we will need to use.

If you see more than one line in the output then '''STOP''' as these directions may not be correct.  If you see more than one line here, you probably have more than one external hard drive or flash disk connected.  Remove all extra hard drive and rerun the "grep" command.  If you still see more than one line, '''Please''' contact one of the of the iHRIS developers for more help.

===Change The Hard Drive Partition Type===
We will need to run the "fdisk" command interactively on the hard drive device.  If the parition was /dev/sdb1, the hard drive device is /dev/sdb (remove the number from the partition).  Here is a sample interaction.  You should type in everything in bold (changing /dev/sdb as neeeded):
 litlfred@cumin:/tmp$ '''sudo fdisk /dev/sdb'''
 Command (m for help): '''p'''
 
 Disk /dev/sdb: 1015 MB, 1015808000 bytes
 13 heads, 36 sectors/track, 4239 cylinders, total 1984000 sectors
 Units = sectors of 1 * 512 = 512 bytes
 Sector size (logical/physical): 512 bytes / 512 bytes
 I/O size (minimum/optimal): 512 bytes / 512 bytes
 Disk identifier: 0x0008db47
 
    Device Boot      Start         End      Blocks   Id  System
 /dev/sdb1            2048     1983999      990976    6  FAT16
 
 Command (m for help): '''t'''
 Selected partition 1
 Hex code (type L to list codes): '''83'''
 Changed system type of partition 1 to 83 (Linux) 
 
 Command (m for help): '''p''' 
 
 Disk /dev/sdb: 1015 MB, 1015808000 bytes
 13 heads, 36 sectors/track, 4239 cylinders, total 1984000 sectors
 Units = sectors of 1 * 512 = 512 bytes
 Sector size (logical/physical): 512 bytes / 512 bytes
 I/O size (minimum/optimal): 512 bytes / 512 bytes
 Disk identifier: 0x0008db47 
 
    Device Boot      Start         End      Blocks   Id  System
 /dev/sdb1            2048     1983999      990976   83  Linux
 
 Command (m for help): '''w'''
 The partition table has been altered! 
 
 Calling ioctl() to re-read partition table.
 
 WARNING: If you have created or modified any DOS 6.x
 partitions, please see the fdisk manual page for additional
 information.
 Syncing disks.

===Formatting The Hard Drive as ext3===
Simply do:
 sudo mkfs.ext3  /dev/sdb1


===Labelling the hard drive===
Now we want to make a lablel for our newly formatted hard drive so that we can refer to it easily later:
 sudo tune2fs -L ihris /dev/sdb1

===Testing===
Unplug the hard drive and plug it back in.  There should be a USB disk icon on your Desktop with the label "ihris".  Also, running:
 mount | grep media
you should see somethine like:
 /dev/sdc1 on /media/ihris type ext3 (rw,nosuid,nodev,uhelper=udisks)
Don't worry if your partition has changed from /dev/sdb1 to something else like /dev/sdc1

==Creating the Software Repository==
You should now have you hard drive prepared and mounted under /media/ihris.  If not '''STOP'''
===Mirroring===
We will be mirroring (which means to create an identical copy of) the online Ubuntu repositories and the [https://launchpad.net/~intrahealth+informatics/+archive/ihris iHRIS PPA] on Launchpad.  All of the packages for Ubuntu and iHRIS will be saved into a subdirectories of our hard drive which we create with:
 sudo mkdir -p /media/ihris/ubuntuMirror/mirror
 sudo mkdir -p /media/ihris/ubuntuMirror/mirroriHRIS

We will also need to install the debmirror software:
 sudo apt-get install debmirror

===mirrorbuild.sh===
Save the script below to /media/ihris/ubuntuMirror/mirrorbuild.sh by copying and pasting with gedit:
 sudo gedit  /media/ihris/ubuntuMirror/mirrorbuild.sh
This is what you should copy and paste
<source lang='bash'>
#!/bin/bash
## Setting variables with explanations.
basePath="/media/ihris/ubuntuMirror/"

# Don't touch the user's keyring, have our own instead
export GNUPGHOME=${basePath}keyring

# Outpath=              # Directory to store the mirror in
outPath=${basePath}mirror

# Minimum Ubuntu system requires main, restricted
# Section=      -s      # Section (One of the following - main/restricted/universe/multiverse).
section=main,restricted,universe

# Release of the system (Dapper, Edgy, Feisty, Gutsy), and the -updates and -security ( -backports can be added if desired)
release=oneiric,oneiric-updates,oneiric-security,precise,precise-updates,precise-security

# You can change this to a faster/closer mirror if you wish
server=us.archive.ubuntu.com


#start the mirror of iHRIS packages on launchpad ppa http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu
debmirror       -a i386,amd64 --no-source -s main -h ppa.launchpad.net -r  intrahealth+informatics/ihris/ubuntu -d natty --progress -e http ${outPath}iHRIS
#start the mirroring of ubuntu
debmirror       -a i386,amd64 --no-source -s $section -h $server -d $release --progress -e http $outPath

</source>
'''Note''', when Ubuntu 12.04 (LTS Precise) is soon released, you should comment out the line about the release in the above section.

===Trusting the Ubuntu Archives===
We need to create a directory for our key ring and up our mirroring software to trust all of Ubuntu's software archives.  This can be done with:
 sudo mkdir -p /media/ihris/ubuntuMirror/keyring 
 sudo chmod 700 /media/ihris/ubuntuMirror/keyring 
 sudo  gpg --keyring /usr/share/keyrings/ubuntu-archive-keyring.gpg --export --homedir /media/ihris/ubuntuMirror/keyring/ \
 | sudo gpg --no-default-keyring --keyring trustedkeys.gpg --import --homedir /media/ihris/ubuntuMirror/keyring/

===Trusting the iHRIS Launchpad PPA===
To trust the iHRIS PPA on Launchpad we do:
 sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546
 sudo  gpg --keyring  /etc/apt/trusted.gpg  --export  6EC21546 --homedir /media/ihris/ubuntuMirror/keyring/ \
 | sudo gpg --no-default-keyring --keyring trustedkeys.gpg --import --homedir /media/ihris/ubuntuMirror/keyring/

==Downloading the Software Repository==
To create your own mirror you can now simply use the command
 sudo sh /media/ihris/ubuntuMirror/mirrorbuild.sh

This is the same command that you can use to update your mirror.

==Installing Software From The Mirrors==
First we refresh the list of available packages that apt-get knows about
 echo "deb file:///media/ihris/ubuntuMirror/mirror" `lsb_release -cs` "main universe " | sudo tee /media/ihris/ubuntuMirror/sources.list
 echo "deb file:///media/ihris/ubuntuMirror/mirroriHRIS natty main  " | sudo tee  -a /media/ihris/ubuntuMirror/sources.list
 sudo apt-get -o Dir::Etc::sourceparts=nonexistent -o Dir::Etc::sourcelist=/media/ihris/ubuntuMirror/sources.list update
Now we can install package '''XXXXX''' from our hard drive by:
 sudo apt-get -o Dir::Etc::sourceparts=nonexistent -o Dir::Etc::sourcelist=/media/ihris/ubuntuMirror/sources.list install '''XXXXX'''

[[Category:Installation]][[Category:Review2013]]
