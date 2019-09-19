Custom Reporting - Exporting Relationships and Reports to a Module
==================================================================


A tool has been created that will allow you to simply export a relationship and all related reports and reportViews
into a module that you can then share with others.  

Enabling the Tool
^^^^^^^^^^^^^^^^^

The tool is part of the exportReport module.  This module can be found under Pages->Admin->exportReport.  You can also enable this with

.. code-block:: bash

    php index.php --update=1 --enable=exportReport

from the ''pages'' directory of your site.

Using the Tool
^^^^^^^^^^^^^^

Change to the pages sub-directory of the site directory.  The site directory is where your site module file is, e.g. iHRIS-Manage-Demo.xml.  Now type this command:

.. code-block:: bash

    php index.php --page=admin/exportReport

When it runs it will ask if you wish to include the relationship in the module.  If you created a new relationship, then type **Y** (Yes).  If you want to export new reports or report views then type **N** (No).

Next it will display a list of all reports that use the given relationship.  Type the number next to the report(s) you wish to include.  Just type one number at a time followed by enter.  When you've selected all you wish to include type **q** followed by enter.

For each report you selected, it will now display the list of report views for that report.  Again you select the report views you want to include in your module and type **q** followed by enter when you are finished.

A file will be created called CustomReports-full-**XXX**.xml in your current directory.  The **XXX** will be replaced by the relationship you chose.  If the file already exists it will append numbers like:  CustomReports-full-**XXX**001.xml.

Now you can create a directory in your site modules directory for your new module and then move the configuration file there.  Finally enable the module in your site config file if you want it to be enabled by default.

Options
^^^^^^^
There are a few other default options you can override that will affect the completed module.

* Set the version to be used for the module. You can set this when you've made changes 
  and need to make a new module file based on an existing module using --version option ``--version=4.0.3.2``
* Set the module name for the module and the filename that will be created using --module command option. ``--module=MyReport-relationship`` 
* Set the display name for the module using --display option ``--display="My Report Module"``
* Set the description for the module using --description. ``--description="This is my report relationship and report/report view definitions."``

The display and description will appear in the Configure Modules page to further define the module you have created.

In one command:

.. code-block:: bash

    php index.php ----page=admin/exportReport --version=4.3.3.1 --module=healthworkers-per-cadre --display="Health Workers per Cadre" --description="This relationship is for reports that breaks down health workers by cadre"

Testing
^^^^^^^
When testing you have to consider two cases: Are you going to test on the same machine you used to export these reports? Or are you going to test on a different machine?

Testing on the same site
++++++++++++++++++++++++

If you are going to test on the same site you used to create these reports, remember you'll still have these reports (relationships, reports and reportViews) that you created from the Browser.
The export tool however inserts lines ``<conflict>`` tags that will delete all entries created from the the Graphical User Interface. For some reasons sometime this does not work properly. So you may need to go delete them manually from the Magic Data Browser by going through 
``Configure System -> Browse Magic Data -> modules -> CustomReports -> relationships`` from here you delete the relationship that you are sure you exported to the XML file.
You should repeat the same for reports and reportViews.
Then enable your module in the site config file and initialize the upgrade from the browser.

**Warning** you have to be extra careful not to delete anything that does not relate to what you have exported.

Testing on a different machine/site
+++++++++++++++++++++++++++++++++++

This does't necessarily need to be on a different machine, it could just be another iHRIS instance running on the same machine.
You will need to delete the ``<erase>`` tag entries in the final module file and then enable it on the site config.
