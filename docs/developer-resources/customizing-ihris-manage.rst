Customizing iHRIS Manage
========================



Customizing iHRIS Manage
^^^^^^^^^^^^^^^^^^^^^^^^

iHRIS Manage can be customized in many places. Any of the HTML templates or CSS files can be modified to change the look, and new forms can be created or simply modified to add new fields. 

iHRIS Manage is installed in the [home] directory. The core engine (I2CE) and iHRIS Common are also installed in this directory.



iHRIS Package Directory Structure
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This section explains the layout of all the required packages for iHRIS. By default, any customized sites you create will be under the ihris-manage/sites directory. However, this directory can be placed anywhere on the file system. You can simply copy this directory somewhere else to make your changes. You'll just need to make sure the configuration file knows where to load the iHRIS Manage configuration file and the Apache document root has a link to the pages sub-directory.


I2CE/
~~~~~
This directory contains the class files and configuration for the core engine. All the iHRIS Manage files are built off of these core classes. No changes should need to be made to these files unless there are bugs that need to be fixed. The configuration file should be included by the ihris-common configuration file. In the documentation below this will be referred to as the I2CE directory.



* **I2CE/lib/**  - This directory contains all the I2CE class files.


ihris-common/
~~~~~~~~~~~~~
This directory contains all the shared files for all iHRIS packages. No changes should need to be made to these files unless there are bugs that need to be fixed. It contains the common configuration file that should be included by the iHRIS Manage (or Qualify or Plan) configuration file. In the documentation below this will be referred to as the iHRIS Common directory.



* **ihris-common/lib/**  - This directory contains all the shared classes. These are mostly a few form (I2CE_Form) objects and some specific page (I2CE_Page) objects that can be reused.



* **ihris-common/images/**  - This directory contains the shared images that all iHRIS packages use, mainly style and report graphics.



* **ihris-common/templates/**  - This directory includes all the HTML template files that the iHRIS Common classes load. To customize any of these files, simply copy them to your site templates directory, and that will be loaded instead.


ihris-manage/
~~~~~~~~~~~~~
This directory contains the shared files for all iHRIS Manage installations and the iHRIS Manage configuration file. The only files that should be changed are files under the sites directory. In the documentation below this will be referred to as the iHRIS Manage directory.



* **ihris-manage/lib/**  - This directory contains all the form and page class files for all iHRIS Manage installations. These classes can be customized by extending them in the site lib directory and adding an entry to the site configuration file to register the new class with the I2CE_FormFactory instead of the default class.



* **ihris-manage/templates/**  - This directory includes all the iHRIS Manage-specific template files. To make any changes, simply copy the file to the site templates directory with the same name, and that file will be loaded instead.



* **ihris-manage/sites/**  - This directory is where multiple installations of iHRIS Manage can be installed. The Demo directory can be copied anywhere on the file system to be customized. The pages directory needs to be linked to the Apache document root somewhere for the site to display.



* **ihris-manage/sites/Demo/**  - This is the demonstration installation of iHRIS Manage. Changes can be made directly to these files, or this whole directory structure can be copied for your installation. In the documentation below this will be referred to as the site directory.



* **ihris-manage/sites/Demo/lib/**  - This is where you can place any custom class files for your installation. By default this directory is empty since it uses all the default classes from ihris-manage and ihris-common.



* **ihris-manage/sites/Demo/templates/**  - Your custom templates will go here. A few files are included already, such as the main.html file that all pages use to display your site.



* **ihris-manage/sites/Demo/pages/**  - This directory includes all the PHP files that are under the Apache document root to be displayed for your site. They create instances of I2CE_Page classes and display them.



* **ihris-manage/sites/Demo/css/**  - This includes all the CSS files for your site. These are can a reference to a custom css file in the main.html template file.  You can also copy a css file from another module into this directory and make changes to it.  It will then take precedence over the original one



* **ihris-manage/sites/Demo/images/**  - This is where you can place any custom images for use on your site. Any images added in here will take precedence over any images found in ther modules.  Any template files you create can reference these images like so:

.. code-block::

    <img src=”file/yourfile.jpg”>
 
where *yourfile.jpg*  is the new file you've added in the *ihris-manage/site/Demo/images*  directory.


Sample Customizations
^^^^^^^^^^^^^^^^^^^^^
 

Making HTML Customizations
~~~~~~~~~~~~~~~~~~~~~~~~~~
First, we can make some changes to the main template, which starts all pages. This is located in the site templates directory and is called “main.html”. 


* Change the title element to “My HR” or whatever you would like it to be.
* A little further down are two paragraph elements with the ids of “siteName” and “siteTag.” Change the siteName to “My HR” and the siteTag to “iHRIS Manage.”
* Near the bottom of the page is a div element with the id of “siteFooter.” You can add any text or images here, such as Ministry or USAID/Capacity Project logos. Any images placed here should be in the site pages/images directory.

Any other templates that are in the iHRIS Common or iHRIS Manage template directories should be copied to the site templates directory if you want to customize them. Then make the changes to that file.


Adding a New Field to a Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Please see [[Adding Forms and Fields]] and [[Adding Fields to the Person Form]].


Additional Documentation
^^^^^^^^^^^^^^^^^^^^^^^^

Additional documentation will be added as it is completed to the  `Capacity iHRIS Suite Project page on the wiki <http://wiki.ihris.org/wiki/index.php/Capacity_Project%27s_iHRIS_Suite>`_ . Each PHP file should have documentation. 

Code changes and development are hosted at  `Launchpad <http://launchpad.net/ihris-suite/>`_ . You can also ask questions and report bugs at this location.


