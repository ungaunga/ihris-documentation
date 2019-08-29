Customizing Packaged iHRIS
==========================

== Experimental Packages == 

To install snapshots of the current development — which may or may not work — add the following line to <tt>/etc/apt/sources.list.d/ihris.list</tt>:

 deb http://ihrisdev.intrahealth.org/debian . main

If you want to change any of the database parameterso, then modify the file in <tt>/etc/i2ce/Demo/config.values.php</tt>.


* You should have the bare-bones installation running.

===Trying the iHRIS Manage Demo===

If you'd like to install the complete demonstration site, you can grab the i2ce-ihris-manage-site-demo from Launchpad:

 sudo apt-get install i2ce-ihris-manage-site-demo

To complete the set up, follow these steps (also in <tt>/usr/share/i2ce-ihris-manage-site-demo/README.debian</tt>):

1. This package expects MySQL to be installed locally by default. Verify that it is, or add the MySQL host to <tt>/etc/i2ce/ihris-manage-demo.apache</tt> as the value of the environment variable <tt>I2CE_DB_PROTOCOL</tt>.

For example, if your MySQL host is reachable at “mysql-host”, you would put

        SetEnv I2CE_DB_PROTOCOL mysql-host

in <tt>/etc/i2ce/ihris-manage-demo.apache</tt>.

2. Create the database for the iHRIS demonstration.  By default, the demo expects to use a database named “ihris” with the user “ihris” and the password “ihris”.

To create the database, use the following commands:

 mysqladmin -uroot -p create ihris
 echo "GRANT ALL ON ihris.* to ihris@localhost \
       IDENTIFIED BY 'ihris'" | mysql -uroot -p

3. Symlink <tt>/etc/i2ce/ihris-manage-demo.apache</tt> to <tt>/etc/apache2/conf</tt> and restart apache:

 sudo ln -s /etc/i2ce/ihris-manage-demo.apache /etc/apache2/conf.d
 sudo /etc/init.d/apache2 restart

4. Point your browser to the URL.  By default, an alias is created at http://YOUR_SERVER/ihris/manage/Demo/. If you're installing this on your local machine, then you would probably use http://127.0.0.1/ihris/manage/Demo/.

5. You will be prompted to update the site.  Click “OK”.

[[Category:Archived Pages]]
