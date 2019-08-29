Custom Reporting -- Exporting Reports From the Command Line
===========================================================

Sometimes you may want to export reports from the command line on a regular basis.  This document will explain how to run commands from the command line to do this.  You can also include these commands in a script in a cron job if you'd like.  **Note:**  This currently requires revision 3014 of I2CE that fixes some issues with command line reports.  This is currently in development, but will be in the 4.1.4 release.


The Pages Directory
^^^^^^^^^^^^^^^^^^^

Before running any of these commands you'll need to be in the pages directory for your site.  Replace PATH with the PATH to your site directory.



.. code-block:: bash

    cd PATH/pages
    



Update the Report Cache
^^^^^^^^^^^^^^^^^^^^^^^

The report cache is updated based on the times you've set when the site is accessed.  However, you may want to cache any reports before running them on the command line.  You use the "report" name for this, not the report view.  Replace REPORT with your report name.



.. code-block:: bash

    php index.php --page=/CustomReports/generate/REPORT
    



Export Report as CSV
^^^^^^^^^^^^^^^^^^^^

To export your report as a CSV file, run this command and replace REPORTVIEW with the report view you wish to see.



.. code-block:: bash

    php index.php --page=/CustomReports/show/REPORTVIEW/Export --post=export_style=CSV > FILENAME.csv
    



Export Report as PDF
^^^^^^^^^^^^^^^^^^^^

To create a PDF of your report, run this command and replace REPORTVIEW with the report view you wish to see.



.. code-block:: bash

    php index.php --page=/CustomReports/show/REPORTVIEW/PDF --post='paper_size=LETTER&paper_orientation=P' > FILENAME.pdf
    


[[Category:Custom Reporting]][[Category:Review2013]]
