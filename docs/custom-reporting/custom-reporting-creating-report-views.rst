Custom Reporting -- Creating Report Views
=========================================

This document applies to the iHRIS Suite version 4.0. For version 3.1, the methods are similar although not identical.


Intended Users
^^^^^^^^^^^^^^
The report view were intended to be as simple as possible to create and view for the end user.

You may wish to review the [[Custom Reporting -- An Overview#Tasks | tasks]] for custom reporting.


Creating and Editing A Report View
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Click on "Configure System" on the home page.  Then, under "Manage Reports" click on "Report Views."   Now you can choose either to edit an existing Report View or Create a New View.

To create a new Report View, you need to select the [[Custom Reporting -- Creating Reports|Report]] on which this view is based off of.  You will also be prompted to name this report and provide a description.  


Choosing Fields
~~~~~~~~~~~~~~~
You will have a list of the fields available from the selected Report.  You can choose, with a checkbox, which of these fields you want displayed in the Report View.  You can also change the name (header) for the fields.

Ordering Fields
~~~~~~~~~~~~~~~
You can choose the order in which the fields are listed by dragging and dropping the different fields.


Setting The Default Display
^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can set the default display for a Report View as follows:


* Display the intended Report View
* Choose any limiting options you wish
* Choose any sorting you wish
* Select the "Set as Default" checkbox
* Click on the intended display button (e.g. "Print" or "View")
You can clear the default view from the Edit Report Views Page.

Adding Related Report Views
^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may wish to create a quick "Jump" from one report view to another that will be shown at the bottom of the HTML Display.  You can do so when editing the Report View.


Aggregating Data
^^^^^^^^^^^^^^^^

In Report Views, there is an option for the fields "Choose a
method to aggregated this data".    This is used when you to aggregate the data in a report view to get the
total number of something.    

The "Staffing Norm 2010" report in the iHRIS Manage Demo is an example of this.

Here, you have a report view with the fields Job, Cadre, Facility, Facility Type, Filled Positions (really the internal id of the position form), and Staffing Norm.

The Filled Positions is selected to aggregate as "Total."   If "Total was not selected, the report would look something like:


* ER Nurse, Nurse, Rushonga Hospital, Hospital, position|23213, 5
* ER Nurse, Nurse, Rushonga Hospital, Hospital, position|24324, 5
* ER Nurse, Nurse, Rushonga Hospital, Hospital, position|22344, 5
* ER Nurse, Nurse, Marjoram Hospital, Hospital, position|21224, 2
* ER Nurse, Nurse, Marjoram Hospital, Hospital, position|29924, 2

What the "Total" on the "Filled Position" column does is to group the data together based on the other columns and count how many positions there are.  So the report looks something like:


* ER Nurse, Nurse, Rushonga Hospital, Hospital, 3, 5
* ER Nurse, Nurse, Marjoram Hospital, Hospital, 2, 2


Displaying A Report View
^^^^^^^^^^^^^^^^^^^^^^^^
Simply select "Create Reports" from the home page and select the report you wish to use.

The Different Displays
^^^^^^^^^^^^^^^^^^^^^^

HTML Display
~~~~~~~~~~~~
This presents a interactive display of the data which allows you to limit and sort the data.  If no default has been set for the Report View, this is the display that is used.

Limiting By Fields
------------------
Based on the fields that you chose to limit by in [[Custom Reporting -- Creating Reports]] you can limit the data shown by the different fields in the report.  For example, you could limit a staff list by those employees in a given facility or a given district.

Sorting By Fields
-----------------
You can choose the sorting order by clicking on the headers for each of the columns (fields).  Clicking once makes it ascending order, twice is descending order, and a third time turns off the sort for that field.  You can also click on the header of a second column.  This will allow you to sort by two columns.  For example you could sort by Department, then Surname, then First Name.


Print(PDF) Display
~~~~~~~~~~~~~~~~~~
In this display you can choose to view your report as a PDF file.  You can choose paper size and orientation.

To customize the colors and graphics, margins, spacing, you should modify the magic (configuration) data at:
 /modules/CustomReports/displays/PDF/display_options


Export Display
~~~~~~~~~~~~~~
In this display, you can export all of your data to a file.  The file types are:


* 'html': exports the data into an html table
* 'csv': a  `comma separated values <http://en.wikipedia.org/wiki/Comma-separated_values>`_  file.  this is suitable for import in to Excel or a database.
* 'tab': a  `tab separated values <http://en.wikipedia.org/wiki/Delimiter-separated_values>`_  file.   this is suitable for import in to Excel or a database.

Chart Display
~~~~~~~~~~~~~
[[Category:Custom Reporting]][[Category:Review2013]]
