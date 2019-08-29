Installing the Debian Packages
==============================

'''DEPRECATED'''' This page is out of date.  Please see
   http://wiki.ihris.org/wiki/Installing_iHRIS_4.2



'''EXPERIMENTAL''' Directions for debian installation.  

Caveats:
*Tested on Ubuntu Lucid (10.04) and  Meerkat (10.10)

==Special Instructions for Ubuntu Lucid (10.04) and Maverick (10.10)==
<source lang='bash'>
sudo add-apt-repository ppa:chris-lea/php-pecl-extras 
</source>


==Installing The Standard iHRIS Sites==

The are four possible sites you can install.  

When you install your site you will be asked to enter the administrative password for mysql.  This is probably the same password of the account you logged into the computer with)

Once you are done the site administrator has username i2ce_admin with password the one chose when you installed the site.

===iHRIS Manage===
The standard iHRIS Manage site.
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-manage-site
</source>
will install to http://localhost/iHRIS/manage
===iHRIS Manage Demo===
The standard iHRIS Manage site with demo data.
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-manage-site-demo
</source>
will install to http://localhost/iHRIS/manage-demo
===iHRIS Qualify===
The standard iHRIS Qualify site.
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-qualify-site
</source>
will install to http://localhost/iHRIS/qualify
===iHRIS Qualify Demo===
The standard iHRIS Qualify site with demonstration data.
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-qualify-site-demo
</source>
will install to http://localhost/iHRIS/qualify-demo

==Installing Other Sites==
===Qualify for Nursing and Midwifery Council of Nigeria===
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
sudo apt-add-repository ppa:ihris-nigeria/ihris
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-qualify-nmcn 
</source>
Now browse to http://localhost/NMCN

===Manage for MOH Mali===
(Not tested)
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
echo "deb http://ppa.launchpad.net/ihris+mali/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihrismali.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D498888F
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-manage-mali-site
</source>

Now browse to http://localhost/mali-manage

===Manage for MOH Zanzibar===
<source lang='bash'>
echo "deb http://ppa.launchpad.net/intrahealth+informatics/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6EC21546  
echo "deb http://ppa.launchpad.net/ihris+zanzibar/ihris/ubuntu " `lsb_release -cs` " main"  | sudo tee  /etc/apt/sources.list.d/ihris_zanzibar.list
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 67A06201
sudo apt-get update
sudo apt-get install --install-recommends ihris+ihris-manage-site-zanzibar 
</source>
Now browse to http://localhost/iHRIS/zanzibar

==Details==
*The i2ce/ihris library is installed under /usr/lib/iHRIS/lib/4.0
*All sites are installed under /var/lib/iHRIS/sites/4.0, for example /var/lib/iRHIS/sites/4.0/ihris-manage-site-demo
*There is no link (ln -s) under /var/www to the pages directory, instead the site is made available by /etc/apache2/conf.d/ihris-manage-site-demo.conf

[[Category:Installation]][[Category:Review2013]]
