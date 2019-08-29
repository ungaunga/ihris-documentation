Installing Software Raid (MDAMD) on the Appliance
=================================================

==Create a Bootable USB Drive==
First, you will need to download
 open.intrahealth.org/livecd.iso
and burn it to a USB stick:
 [Ubuntu Start Menu]
 [System]
 [Administration]
 [Startup Disk Creator]
==Booting==
No2 boot the appliance with the USB Disk inserted.  Note, you may have to go into the BIOS and select that the USB boots before the hard drives, or press [F10] right a system startup to get the boot menu.

At the beginning of the boot is the boot menu ( GRUB boot loader) where you need to do:
 [F6] (Other Options)
 Select to Disable dmraid
 [Esc]
 Choose to install Ubuntu/iHRIS
==Setting Up Partitions==
Continue as usual until the partition disks screen
 [Ctrl]-[Alt]-[F1]  ''will take you to a prompt''
Here you do
 sudo apt-get install mdadm
You will need to create partitions via fdisk.  If iHRIS has been installed on the appliance before, partitions may already exist.  In this case we will need to remove them first
 sudo fdisk /dev/sda
  ''#(Optional: Removing existing partitions)''
    p (print the partition table -- you should see something like the following but with different numbers)
         Device Boot      Start         End      Blocks   Id  System
        /dev/sda1   *           1       18662   149902483+  83  Linux
        /dev/sda2           18663       19457     6385837+   5  Extended
        /dev/sda5           18663       19457     6385806   82  Linux swap / Solaris
       (we want now to remove each of these partitions, 1 2 and 5)
    d (delete partition)
    1 (select partition 1 to delete)
    d (delete partition)
    2 (select partition 1 to delete)
    d (delete partition)
    5 (select partition 1 to delete)
    
  ''#Creating new partitions''
    n  (new partition)
    p  (primary)
    1 (partition 1)
    1 (first cylinder)
    9242 (last cylinder)
    a (toggle boot partition flag)
    1  (select the first partition to be bootable)
    n  (new partition) 
    p  (extended)
    2 (partition 2)
    9243 (first cylinder)
    9729 (last cylinder)
    n    (new parition)
    l    (logical partition)
    9243 (first cylinder)
    9729 (last cylinder)
    t (set partition type)
    5 (parition 5)
    82 (swap)
    p (print to make sure everything matches below)
    w  (write and exit)
Now we need to repeat the creation of partitions for the second hard disk ( /dev/sdb ).  There shouldn't be any existing partitions here so we won't need to delete them first.
 sudo fdisk /dev/sdb
  ''#Creating new partitions''
    n  (new partition)
    p  (primary)
    1 (partition 1)
    1 (first cylinder)
    9242 (last cylinder)
    a (toggle boot partition flag)
    1  (select the first partition to be bootable)
    n  (new partition) 
    p  (extended)
    2 (partition 2)
    9243 (first cylinder)
    9729 (last cylinder)
    n    (new parition)
    l    (logical partition)
    9243 (first cylinder)
    9729 (last cylinder)
    t (set partition type)
    5 (parition 5)
    82 (swap)
    p (print to make sure everything matches below)
    w  (write and exit)
 ..blah blah..
and the partitions should be identical:
 /dev/sda1 start 1 end 9242 id 83 (linux)
 /dev/sda2 start 9243 end 9728 id 5 (extended)
 /dev/sda5 start 9243 end 9728 id 82 (swap)
 /dev/sdb1 start 1 end 9242 id 83 (linux)
 /dev/sdb2 start 9243 end 9728 id 5 (extended)
 /dev/sdb5 start 9243 end 9728 id 82 (swap)

==Assembling the Raid Array==
Now assemble the software raid array
 sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sda1 /dev/sdb1
 sudo mdadm --create /dev/md1 --level=1 --raid-devices=2 /dev/sda5 /dev/sdb5
on success it should say "mdadm: array /dev/md0 started"

==Selecting to Install on the RAID array==
To return to installed:
 [Alt]-[F7]
From the partition manager thing, click "Back" and then "Forward" so that is will rescan the disks
 Select 'Specify the partitions manually'
 Click "Forward"
 Right click on /dev/md0 and create a new partition table
 Under /dev/md0 you should see "free space".  Right click and use as "ext3" with mount point "/"
 Right click on /dev/md1 and create a new partition table
 Under /dev/md1 you should see "free space".  Right click and use as swap
 Click "Forward"
==Boot Loader Options==
When you get to the "Ready to Install" Screen select:
 [Advanced]
 Make sure install boot loader is checked
 Choose '/dev/md0' under "Device for bot loader installation"

==Installing the Boot loader on the Raid Array==
Just before the installation is finished, it tries to install grub, the boot loader, onto the /dev/md0 our raid disk.  It may fail by saying:
 executing grub-install /dev/md0 failed.  This is a fatal error.
There is a [https://bugs.edge.launchpad.net/ubuntu/+source/grub2/+bug/462171 bug report].  Luckily there is a [http://ubuntu-ky.ubuntuforums.org/showthread.php?p=9638149 workaround]:
 [Ctrl]-[Alt]-[F1]
 sudo parted /dev/sda set <partition_number> bios_grub on
 grub-install --modules=raid --no-floppy /dev/sda
 [Alt]-[F7]


==Known Issue for Karmic==
http://www.ubuntu.com/testing/karmic/beta?info=EXLINK
with possible workaround http://www.brandonchecketts.com/archives/booting-from-a-software-raid-device-on-ubunto-karmic-910

==Automatic boot on failure==
Optionally, and not recommended, you can have the Appliance continue to boot if one of the hard drive failse by editting this file /etc/initramfs-tools/conf.d/mdadm change "BOOT_DEGRADED=false" to "BOOT_DEGRADED=true"

The reason that this is recommended is that we will have no way of knowing that one of the hard drives failed and then the second one may fail.

==LCD Menu== 
 sudo usblcd spash /home/lcdmenu/bin/splash.txt



After rebooting, maybe modify /etc/fstab and set
  /dev/md0 to "relatime" instead of defaults

==Background==
https://help.ubuntu.com/community/Installation/SoftwareRAID#Formatting
[[Category:iHRIS Appliance]]
