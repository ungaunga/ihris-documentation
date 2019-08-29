Installing ApacheDS On Ubuntu
=============================

=Prerequisites=
==Java Environment==
ApacheDS needs a java environment and the version 2 of ApacheDS requires at least JVM version 7.

To confirm the version of java installed run 

<code> java -version </code>

You'll get an output that looks like:

<code>
java version "1.7.0_15"

OpenJDK Runtime Environment (IcedTea7 2.3.7) (7u15-2.3.7-0ubuntu1~12.04.1)

OpenJDK 64-Bit Server VM (build 23.7-b01, mixed mode)
</code> 

This one runs JRE version 7update15

If Java environment is not installed, we will need to install it by running this command from the terminal
<code> sudo apt-get install openjdk-7-jdk </code>


=Installing and Configuring ApacheDS on Ubuntu 12.04=

==Installation==

We first of all need to download the installation file for ApacheDS from [http://directory.apache.org this webpage].

When you open the page, you should see two projects ApacheDS and Apache Studio. Click on ApacheDS project which should take you to the ApacheDS project home page.

From here access the Downloads page and download the most recent version.
Choose to download the Debian (.deb) installer and it should take you to the download page. Depending on your PC select to download 64-bit or 32-bit installer. I selected 32-bit installer.

After the file is downloaded, go to your downloads folder. If you dowloaded to the default Downloads directory run from terminal the following command:

<code>cd /home/`whoami`/Downloads</code> and it should take you to the Downloads folder.

To install ApacheDS issue the following command:

<code>sudo dpkg -i apacheds-2.0.0-M11-i386.deb</code> (typing the apacheds and pressing the tab should complete the file name)

Answer the prompts to install ApacheDS.

==Starting ApacheDS==

To start ApacheDS server run the following command from terminal 
<code>sudo /etc/init.d/apacheds-2.0.0-M11-default start</code>
and it should respond with the message <code>Starting ApacheDS - default...</code>


To check for its status run <code>sudo /etc/init.d/apacheds-2.0.0-M11-default status</code>

==Configuring ApacheDS==

In case we need to change any configuration parameters, we can edit all from one place by opening a file located here
<code> sudo pico /var/lib/apacheds-2.0.0-M11/default/conf/config.ldif</code>
[[Category:Provider Registry]]
