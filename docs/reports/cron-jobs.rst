Cron Jobs
=========

If you would like certain function to be run on a regular basis you can set up a cronjob on your server to check the cron system within iHRIS.  You can then configure your own code to run at regular intervals.

Creating Your Custom Code
^^^^^^^^^^^^^^^^^^^^^^^^^
First you need to enable the **cron**  module for your site in the metadata section.  You can do this by adding the following line to the module where you are configuring your custom code.  See the [[Module Structure]] documentation for how to create a new module.

.. code-block:: xml

    <requirement name="cron">
      <atLeast version="4.1" />
      <lessThan version="4.2" />
    </requirement>
    

You will also need a module class defined for your module in the metadata section.

.. code-block:: xml

    <className>iHRIS_Module_MYMODULE</className>
    

Now you need to define some command line hooks in your site module.  Edit the module class definition (be sure to change MYMODULE to a more appropriate name).

.. code-block:: php

    class iHRIS_Module_MYMODULE extends I2CE_Module {
    
       /**
        * Return the array of command line hooks available in this module.
        * @return array
        */
       public static function getCLIHooks() {
          return array(
                 'cronjob_five' => 'cronjob_five',
                 );
       }
    
       /**
        * Perform any actions done at 5 minute intervals for the site.
        */
       public function cronjob_five() {
          // write the code here you want to happen every 5 minutes.
       }
    
    }
    

For the CLIHooks array, the array key is the name of the hook and these must be from a valid list of available times.  The second is the name of the method in the module that should be called.  Currently the available hooks are:

{| border="1" cellspacing="0" cellpadding="5" align="center"
! Hook Name
! Timing
! Explanation
! Timeout
|- 
| cronjob_five
| Five Minutes
| Will run after 5 minutes have passed since the last time this was run.
| If still running after 15 minutes will try to run again.
|- 
| cronjob_ten
| Ten Minutes
| Will run after 10 minutes have passed since the last time this was run.
| If still running after 30 minutes will try to run again.
|- 
| cronjob_fifteen
| Fifteen Minutes
| Will run after 15 minutes have passed since the last time this was run.
| If still running after 45 minutes will try to run again.
|- 
| cronjob_thirty
| Thirty Minutes
| Will run after 30 minutes have passed since the last time this was run.
| If still running after 90 minutes will try to run again.
|- 
| cronjob_hourly
| One Hour
| Will run at the first time checked after the hour changes.
| If still running after 3 hours will try to run again.
|- 
| cronjob_daily
| One Day
| Will run at the first time checked after the day changes.
| If still running after 2 days will try to run again.
|- 
| cronjob_weekly
| Once a Week
| Will run at the first time after the week rolls over on Sunday.
| There is no timeout and it will try to run every week.
|- 
| cronjob_monthly
| Once a Month
| Will run on the first day of the month as soon as the day start.
| There is no timeout and it will try to run every month.
|}

Any of the daily, weekly and monthly crons will run soon after midnight depending on what other cronjobs may be running.  You can configure the server to run these at different times if you'd prefer.

Configuring the Server
^^^^^^^^^^^^^^^^^^^^^^
Then you need to create a cronjob on the server to run your commands on a regular basis to check the iHRIS cron system that will run all appropriate functions at the requested times.

This can be run from any user, but ideally the one that set up the iHRIS directory.  Run this command from the command line to open an editor and set up the cron job:

.. code-block:: bash

    crontab -e
    

There may be some explanation text and possibly other cronjobs already listed.  Add the following line to check the iHRIS cron every minute.  You can also do this at other intervals, but the longer the interval is the longer the possible delay in running the iHRIS functions.  You will need to replace SITE_DIRECTORY with the location of your site on the system.  You can also manually run this command to test output and remove the --silent option.

.. code-block:: vim

    * * * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --nocheck=1)
    

Running at Specific Times
~~~~~~~~~~~~~~~~~~~~~~~~~
You can also configure the cronjob to run certain cronjobs at certain times if you don't want them to run at midnight.  All the minute based jobs will check every minute.  The hourly job will check at 15 minutes past the hour, the daily job will check at 6AM, the weekly job will check at noon and the monthly job will check at 5PM.  Note that with a setup like this if it fails to run for any reason, then the required amount of time must pass before it is checked again.  Also note that the weekly cron is configured to only run on Sundays, but that can be changed by configuring the cron job types configured in the cron module.  Be careful about changing any of these values because you may get unexpected results.  All the configuration can be found in magic data under /modules/admin/cron/types.

.. code-block:: vim

    * * * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=five --nocheck=1)
    * * * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=ten --nocheck=1)
    * * * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=fifteen --nocheck=1)
    * * * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=thirty --nocheck=1)
    15 * * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=hourly --nocheck=1)
    0 6 * * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=daily --nocheck=1)
    0 12 * * 0 (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=weekly --nocheck=1)
    0 17 1 * * (cd SITE_DIRECTORY/pages; php index.php --page=/admin/cron --silent=true --type=monthly --nocheck=1)
    

