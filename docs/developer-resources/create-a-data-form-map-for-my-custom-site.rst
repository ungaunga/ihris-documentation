Create a Data Form Map For My Custom Site
=========================================

When you create a custom site, you may be adding new forms and fields.  In which case, the data maps for iHRIS Manage and Qualify are no longer accurate.   You will want to generate your own form map.



Required Software
^^^^^^^^^^^^^^^^^
Creating a data form map is easy once you have the proper programs installed on your system.  To do so run:


.. code-block:: bash

    sudo apt-get install graphviz imagemagick
    



Enabling the Module
^^^^^^^^^^^^^^^^^^^
The ability to create a data map is provided by the "" module.  To enable via the web interface:


* Click on "Configure System"
* Click on "Configure Modules"
* Click on "Sub-Modules" next to "I2CE Forms"
* Click on  the check box next to "Form Documentor"
* Click the "Enable" button on the bottom of the page.


Enable the Module (Command Line)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Go to the *pages*  directory of your site and enter
 php index.php  --update=1 --enable=formDocumentor


Creating a Map
^^^^^^^^^^^^^^
Go to your site directory, for example:


.. code-block:: bash

    cd /var/www/iHRIS-manage
    


Now run:


.. code-block:: bash

     php index.php --page=/formDocumentor/dot
    


You will be then be prompted to select which forms that you want to include in the map.   You can select either the individual numbers or a range of numbers.  I suggest that you do *not*  include the forms starting with **cl_**  as it will get messy, and these are related to SDMX-HD.  Other forms you may want to skip are **uuid,**   **contact,**  **role**  and **user** 

When you finish, you should have a file in the **/tmp**  directory.



