Turn Off Background Processes
=============================

Background processes are run at configured intervals as users access the site.  The main use of background processes is to keep report caches up to date for your site.  On sites with large amounts of data you may want to disable running background processes and manually set up a  `cron job <http://en.wikipedia.org/wiki/Cron>`_  to cache reports on a predefined interval instead of as users access the site.  This may speed up access on some pages when users begin to access your site after a longer lull in activity.  See the How To [[Configuring Report Generation Timing]] and [[Configuring Form Cache Generation Timing]] for more information on the settings to control report generation.

Here is a sample cron-job entry to generate all reports every night at 2:00am.

.. code-block:: text

     0 2 * * * /usr/bin/php **/var/www/manage** /index.php --page=/CustomReports/generate --nocheck=1 > /dev/null 2>&1
    

