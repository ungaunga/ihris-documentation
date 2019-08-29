Create a Calendar Display Page
==============================

In the current development code of iHRIS Common, a module was created to assist with displaying a month view of a calendar name **Calendar** .  This will be in the 4.1.7 or greater release of iHRIS.  You can use this module to create your own calendar views of data in your site.  All you need to do is create a page that extends **iHRIS_PageCalendar** .


Create a Module
^^^^^^^^^^^^^^^
First you will need to create your module.  For an example, you can refer to the  `InstanceCalendar <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-train/4.1-dev/files/head:/modules/InstanceCalendar/>`_  module in iHRIS Train.  For detailed information on creating a module, refer to the [[Module Structure]] documentation.


Required Modules
~~~~~~~~~~~~~~~~
You will need to require the Calendar module.


.. code-block:: xml

        <requirement name="Calendar">
          <atLeast version="4.1" />
        </requirement>
    



Task Configuration(Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
You may also want to define a task for your new page so you can allow certain roles to view this page.  You may also use an existing task or role for the page permissions if you don't want to create a new one.  This is an optional step.  Replace *CAN_VIEW_CALENDAR_TASK*  with the task name you want to create.  You should also set the value of the task to something more relevant to your system.  You will also need to assign this task to a role or as part of another task.  The [[Tasks and Roles]] document will give further details on using tasks and roles.



.. code-block:: xml

        <configurationGroup name="tasks" path="tasks/task_description" locale="en_US">
          <configuration name="CAN_VIEW_CALENDAR_TASK">
            <value>View the Calendar</value>
          </configuration>
        </configurationGroup>
    



Page Configuration
~~~~~~~~~~~~~~~~~~
Now you need to create the page configuration for your new page.  The [[Pages and Templates]] document will give more details on creating pages.  You will need to define the class you will be creating later as well as some optional arguments.

In addition to the standard page args (title, tasks, defaultHTMLFile), you can also use any of these to control how your calendar is displayed.
{| border="1" cellspacing="0" cellpadding="5" align="center"
! min_year
| The minimum year in the year selector for changing the displayed month.
|- 
! max_year
| The maximum year in the year selector for changing the displayed month.
|-
! min_year_increment
| The number of years before the current year for the minimum value of the year selector.
|- 
! max_year_increment
| The number of years after the current year for the maximum value of the year selector.
|}

Here is an example page configuration.  Replace any values in ALL_CAPS with the values specific for your system.



.. code-block:: xml

        <configurationGroup name="page" path="/I2CE/page">
          <configurationGroup name="CALENDAR_PAGE">
            <displayName>CALENDAR_PAGE_NAME</displayName>
            <description>CALENDAR_PAGE_DESCRIPTION</description>
            <configuration name="style" values="single">
              <value>shell</value>
            </configuration>
            <configuration name="class" values="single">
              <value>iHRIS_PageCalendarCUSTOMIZED</value>
            </configuration>
            <configurationGroup name="args">
              <displayName>Page Options</displayName>
              <configuration name="title" values="single" locale="en_US">
                <value>CALENDAR_PAGE_TITLE</value>
              </configuration>
              <configuration name="tasks" values="many">
                <value>CAN_VIEW_CALENDAR_TASK</value>
              </configuration>
              <configuration name="defaultHTMLFile" values="many">
                <status>required:true</status>
                <value>CUSTOM_CALENDAR_TEMPLATE.html</value>
              </configuration>
            </configurationGroup>
          </configurationGroup>
        </configurationGroup>
    



Create the Template
^^^^^^^^^^^^^^^^^^^
Your template can have any text in it that you would like to display.  The main thing is to include a div with an id of **calendar** .  The template needs to match the defaultHTMLFile set in the module.

For example:


.. code-block:: html4strict

    <div id="siteContent">
      <h1>MY CALENDAR</h1>
      <div id="calendar" />
    </div>
    


You will also want to create a template for what can go in each cell of the dates where you want to place text.  You will be loading this template in your custom page so it can be anything you would like.  You may associate a form with this page or simply set some text depending on what you are displaying.


Create the Page Class
^^^^^^^^^^^^^^^^^^^^^
Now you need to create the page class for your new page.  This will need to extends the **iHRIS_PageCalendar**  class.



.. code-block:: php

    class iHRIS_PageCalendarCUSTOMIZED extends iHRIS_PageCalendar {
    }
    


You can put your customizations in the action method, but be sure to call the parent action method before doing anything so the page will be set up.



.. code-block:: php

        /**
         * Perform the actions of this page.
         * @return boolean
         */
        protected function action() {
            if ( parent::action() ) {
                // YOUR CODE HERE
            } else {
                return false;
            }
            return true;
        }
    


In your code, you will need to get the data you wish to display in the calendar.  To get the values of the month and year that are being displayed, you can access the **$this->month**  and **$this->year**  variables.  To find the correct node to add your text, you can use find the element by the ID.  Each date in the calendar has the ID in the format **YYYY_MM_DD** .  For example, May 16, 2013 would be 2013_05_16.  If you have a template called CALENDAR_TEMPLATE_DAY.html, you can use the following code to append it to the May 16th cell.  This assumes that the DAY template uses &lt;p&gt; as the root element.  If you have a form object ('''$formObj''') then you can also set that on the new node to display and &ltspan type="form"&gt; elements.  You can also use setDisplayDataImmediate to set the value of any named elements such as &lt;span name="REPLACE_TEXT_HERE"&gt;.



.. code-block:: php

    $day_node = $this->template->appendFileById( 'CALENDAR_TEMPLATE_DAY.html', 'p', '2013_05_16' );
    $this->template->setForm( $formObj, $day_node );
    $this->template->setDisplayDataImmediate( "REPLACE_TEXT_HERE", "MY TEXT TO DISPLAY", $day_node );
    


For a larger example, you can look at the  `Instance Calendar <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-train/4.1-dev/view/head:/modules/InstanceCalendar/lib/iHRIS_PageCalendarInstance.php#L33>`_  in iHRIS Train.


Enable Module
^^^^^^^^^^^^^
Now you are finished and you only need to enable your new module in your and access the new page you created as well as add in the appropriate links.


