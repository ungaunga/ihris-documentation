Botswana Installation Instructions
==================================


Bazaar
^^^^^^
The bazaar branch for the Botswana instructions are located  `here <https://code.launchpad.net/~ihris+botswana/ihris-botswana/4.1>`_  and can be obtained by


.. code-block:: bash

    bzr branch lp:ihris-botswana
    


DropBox Folder
^^^^^^^^^^^^^^
The source code from bazaar is copied over to the "bzr_branches" folder.  In this folder there are several sub-folders:


* botswana-4.1.3  The folder Carl uses for testing and development
* sovellobw_4.1 The folder used for testing and development
* production_server_customizations These are the customizations that we copy over to the main server and used for production.  The files directory should never be edited. Instead you should do a bzr pull.  Any error messages or warnings need to be resolved before updating the server
* *If you are working outside the MOH you can do "bzr pull lp:ihris-botswana"
* *If you are making customizations while in the MOH then you want to pull from the sub-directory of bzr_branches where those customizations are.  For example "bzr pull ../sovellobw_4_1".


Live/Production Server Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* IP Address: 10.171.5.9
* Username: $username
* Production Database:$BWManage_Prod
* Current iHRIS base Library: /var/lib/iHRIS/lib/4.1-dev  (last updated Feb 14th, 2013)
* Site customization directory: /var/lib/iHRIS/sites/botswana_feb_11_2013
* Site config file: /var/lib/iHRIS/sites/botswana_feb_11_2013/pages/local/config.values.php
* WWW path: There is a link /var/www/ihris -> /var/lib/iHRIS/sites/botswana_feb/pages/


Updating the Server
^^^^^^^^^^^^^^^^^^^
The server should only be updated after hours.

Copying over the site customizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
When you are on your computer (not the server) you can copy them over by:


.. code-block:: bash

    cd bzr_branches/production_server_customizations
    scp -r ./ $username@10.171.5.9:/tmp/psc_`date +"%Y-%m-%d"`
    

This will copy the contents of the production_sever_customizations directory to a the directory "/tmp/psc_2013-02-15" if the day is February 15th, 2013.


Manual Backup
~~~~~~~~~~~~~
Before updating the live server you should make a database backup:


.. code-block:: bash

    ssh -l bwihris 10.171.5.9
    mysqldump -u root -p BWManage_Prod_Feb_14_2013 | bzip2 -9 > backup_`date +"%Y-%m-%d"`.sql.bz2
    

which will create a file called "backup_2013-02-15.sql.bz2" if the day is February 15th, 2013.


Pulling in the Customizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We only copied the customizations from the bzr_branches directory to a temporary directory like "/tmp/psc_2013-02-15".  Now we need to pull them into the production server's site directory.  On the server you can do this by:


.. code-block:: bash

    cd /var/lib/iHRIS/sites/botswana_feb_11_2013/
    bzr pull /tmp/psc_`date +"%Y-%m-%d"`
    

You should see a message such as:

.. code-block::

     M  templates/lists.html
     M  templates/view.html
    All changes applied successfully.
    Now on revision 43.
    



Starting server update
~~~~~~~~~~~~~~~~~~~~~~
You can update the site by browsing to http://10.171.5.9/ihris


