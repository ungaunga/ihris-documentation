Installation Documentation
==========================

The system was created with the goal of running on a LAMP architecture - that is the Linux operating system, MySQL database, and Apache webserver with PHP coding. Our development took place on the latest release of Ubuntu Linux (8.10) however, the system should work on most Linux distributions as well as some other operating systems in which OpenMRS, Apache, PHP, and Java can run.

OpenMRS is the core of the system and must be installed first. There is a great wealth of documentation on the installation, administration, and use of OpenMRS which is freely available. However, the specific documentation on the installation of the system can be found below.

If you would like to install OpenMRS as an appliance (meaning, an instance that runs in a virtual machine such as VMWare refer to the [http://openmrs.org/wiki/OpenMRS_Appliance OpenMRS Appliance Installation].

If you would rather install the system on a clean Linux box, refer to the [http://openmrs.org/wiki/Installing_An_OpenMRS_Server_On_Linux Installing An OpenMRS Server On Linux] Document.

== Installing the web application ==

Step-by-step instructions for installing the application on Ubuntu Hardy.  For purposes of these instructions, we'll assume you're server is installed to respond to http://example.com/

 $ sudo aptitude install --without-recommends libapache2-mod-jk \
                 tomcat5.5 bzr subversion cabextract lcab \
                 smarty-gettext php5-mysql libapache2-mod-php5 \
                 mysql-server php5-cli ant-optional sun-java6-jdk \
                 tomcat5.5-admin 
 $ bzr branch lp:rwanda-pilot ~/rwanda-pilot
 $ sudo mv ~/rwanda-pilot /var/www
 $ chmod 1777 /var/www/rwanda-pilot/public_html/templates_c
 $ svn co http://svn.openmrs.org/openmrs/tags/1.3.2/ ~/openmrs

The following steps are necessary to build openmrs since we used svn to check out openmrs:

 $ cd ~/openmrs
 $ JAVA_HOME=/usr/lib/jvm/java-6-sun ant

The following steps configure tomcat and set up an environment for it:

 $ sudo sed -i 's/^#(TOMCAT5?_SECURITY)=.*/\1_SECURITY=no/' \
       /etc/default/tomcat5.5
 $ sudo sed -i 's/^#(CATALINA|JAVA)_OPTS=.*/\1_OPTS="-Djava.awt.headless=true -Xmx128M"/'\
       /etc/default/tomcat5.5
 $ sudo sed -i 's,^#JAVA_HOME=.*,JAVA_HOME=/usr/lib/jvm/java-6-sun,' \
       /etc/default/tomcat5.5
 $ sudo sh -c 'cat > /etc/apache2/conf.d/openmrs'<<EOF
 JkWorkersFile   /etc/libapache2-mod-jk/workers.properties
 JkLogFile       /var/log/apache2/mod_jk.log
 JkLogLevel      info
 JkMount /openmrs* ajp13_worker
 EOF
 $ sudo sh -c 'cat > /etc/apache2/conf.d/lmi' <<EOF
 Alias /lmi /var/www/rwanda-pilot/public_html
 EOF
 $ sudo sh -c 'cat > /etc/libapache2-mod-jk/workers.properties' <<EOF
 workers.tomcat_home=/usr/share/tomcat5
 workers.java_home=/usr/lib/jvm/java-6-sun/jre/
 ps=/
 worker.list=ajp13_worker
 worker.ajp13_worker.port=8009
 worker.ajp13_worker.host=localhost
 worker.ajp13_worker.type=ajp13
 worker.ajp13_worker.lbfactor=1
 worker.loadbalancer.type=lb
 worker.loadbalancer.balance_workers=ajp13_worker
 EOF
 $ mysql -u root
    < ~/openmrs/metadata/model/1.3.2-createdb-from-scratch-with-demo-data.sql 
 $ mysql -u root openmrs \
    < ~/openmrs/metadata/model/update-to-latest-db.mysqldiff.sql 
 $ patch -p0 <<EOF
 --- /etc/tomcat5.5/tomcat-users.xml     2008-12-09 15:57:57.000000000 -0500
 +++ tomcat-users.xml    2008-12-09 16:07:16.000000000 -0500
 @@ -7,5 +7,4 @@
    <user username="tomcat" password="tomcat" roles="tomcat"/>
    <user username="both" password="tomcat" roles="tomcat,role1"/>
    <user username="role1" password="tomcat" roles="role1"/>
 -  <user username="openmrs" password="openmrs" roles="admin,manager,tomcat"/>
  </tomcat-users>
 EOF
 $ sudo /etc/init.d/tomcat5.5 restart
 $ sudo /etc/init.d/apache2 restart

Finally, get openmrs running in tomcat:

 $ cd ~/openmrs
 $ sudo ln -s ~/openmrs /usr/share/tomcat5.5/.OpenMRS
 $ patch -p0 <<EOF
 === modified file 'properties.xml'
 --- properties.xml      2008-05-09 15:53:35 +0000
 +++ properties.xml      2008-12-09 18:11:28 +0000
 @@ -8,13 +8,13 @@
         <property name="webapp.description" value="An Open-Source EMR System" />
  
         <!-- Properties for running unit tests and webapp [un]deploy with tomcat -->
 -    <property name="tomcat.home" value="C:/Program Files/Apache Software Foundation/Tomcat 5.5"/>
 -    <property name="catalina.home" value="C:/Program Files/Apache Software Foundation/Tomcat 5.5"/>
 +    <property name="tomcat.home" value="/usr/share/tomcat.5.5"/>
 +    <property name="catalina.home" value="/usr/share/tomcat.5.5"/>
      <property name="tomcat.server" value="localhost" />
 -       <property name="tomcat.port" value="8080" />
 +       <property name="tomcat.port" value="8180" />
      <property name="tomcat.manager.url" value="http://${tomcat.server}:${tomcat.port}/manager" />
 -    <property name="tomcat.username" value="test" />
 -    <property name="tomcat.password" value="test" />
 +    <property name="tomcat.username" value="openmrs" />
 +    <property name="tomcat.password" value="openmrs" />
      
      <!-- Documentation settings -->
      <property name="doc.title" value="${ant.project.name} API" /> 
 EOF
 $ ant install

The following commands install the form entry module which, even though it is essential for OpenMRS use, is not included in the primary installation.

 $ mkdir ~/openmrs/modules 
 $ cd ~/openmrs/modules
 $ wget http://modules.openmrs.org/modules/download/formentry/formentry-3.3.4.omod
 $ sudo chown -R tomcat55 ~/openmrs/modules
 $ sudo /etc/init.d/tomcat5.5 restart

Navigate to http://example.com/openmrs/admin/modules/module.list and make sure the formentry module is enabled.

=== Debian ===

Similar steps work on Debian but some changes may be needed.  The contents of /etc/default/tomcat5.5 differ slightly and tomcat-users.xml is in /var/lib/tomcat.5.5 instead of /etc/tomcat55.  Also, see http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=402229
[[Category:Last Mile Initiative]]
