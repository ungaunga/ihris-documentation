Supporting Software
===================

 *This documentation is current as of iHRIS version 3.1 (August 15, 2008).* 

The server has been installed with Ubuntu 8.04 LTS, a long-term release that will be supported for five years. The IP address is #.#.#.# and can be accessed from inside the local network. All references below will use this address and should be updated if it is changed. 

General documentation on Ubuntu can be found at  `the Ubuntu website <http://help.ubuntu.com/8.04/>`_ .


Server Information
^^^^^^^^^^^^^^^^^^


Updates
~~~~~~~
Install software updates using the Update Manager (System → Administration → Update Manager). It will display any packages that need updating, and those packages can then be installed. Install new packages using Synaptic Package Manager (System → Administration → Synaptic Package Manager).


MySQL
~~~~~
MySQL can be administered using terminal commands (Applications → Accessories → Terminal). See  `documentation on MySQL <http://dev.mysql.com/doc/refman/5.0/en/index.html>`_ .
 
MySQL can also be administered using PHP MyAdmin at http://#.#.#.#/phpmyadmin/. The administrative login is XXXX and the password is XXXXXXX. The password can be changed via the privileges link with PHP MyAdmin.


Apache 2
~~~~~~~~
The installed web server is Apache 2. See  `documentation <http://httpd.apache.org/docs/2.2/>`_ . The configuration files are located in /etc/apache2/ on the server. The log files are saved in /var/log/apache2/. The files displayed by the web server are in /var/www/.


PHP 5
~~~~~

PHP 5 is installed to run the iHRIS Plan software. See  `documentation <http://www.php.net/manual/en/>`_ .

