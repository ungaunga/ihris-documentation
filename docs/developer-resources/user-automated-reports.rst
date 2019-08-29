User Automated Reports
======================

You can link a report view to a user to email the details of that report on a regular basis.  This requires that the [[Cron Jobs]] be configured on your location system.

Enable the Module
^^^^^^^^^^^^^^^^^
You now need to enable the UserCronReports module.  You can do this from the **Configure System**  page under **Configure Modules** .  It will be under iHRIS Common.  You can also add the requirement to your site configuration as follows:

.. code-block:: xml

    <requirement name="UserCronReports">
      <atLeast version="4.2" />
      <lessThan version="4.3" />
    </requirement>
    

Advanced users can also enable the modules from a terminal by running the following command from your pages directory:

.. code-block:: bash

    php index.php --update=1 --enable=UserCronReports
    

You will need to restart memcached and your server after doing this from the command line to refresh the APC.

.. code-block:: bash

    sudo service memcached restart
    sudo service apache2 restart
    

Using the Module
^^^^^^^^^^^^^^^^

Now you can add Reports to a user from the Administer Users page.  Simply select a user to edit and then click the "Add Automatic Report" on the left side of the user information display.  You can select the report view and how frequently the email should be sent.  You must have your mail system enabled as well as the php-mail and php-mail-mime packages.  You can install these with the command:

.. code-block:: bash

    sudo apt-get install php-mail php-mail-mime
    

