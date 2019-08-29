Printed Forms with Reports (ODT)
================================

The printed forms module is used to print "standardized" or "official" forms based upon the reports in the system.  For example, it might be the registration number for a nurse. The output will be an Open Office Document. This document can be read readily by Microsoft Word 2003.

Depending on your needs, you may wish to look at these other methods for standardized form generation:


* [[Printed Forms]]
* [[Printed Forms form Relationships (ODT)]]
* [[Standardized Letters (ODT)]]



What are Printed Forms?
^^^^^^^^^^^^^^^^^^^^^^^

Printed forms allow you to create an OpenDocument Text (ODT) template that can be filled in with your report data.  This is based on the [[Standardized Letters (ODT)|Standardized Letters]] that can be used for an individual record.


Adding a Printed Form to a Report View
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There are two steps to adding a printed form to a report view.  First you need to create the template file, then create a module with the template file and the configuration for the report view.  For an example, you can look in the iHRIS Manage demo site modules directory for SampleStaffPrintedForm.


Creating an ODT Template
~~~~~~~~~~~~~~~~~~~~~~~~

The template file needs placeholders for the fields you wish to display.  There are also some other placeholders for special data.  All the placeholders are surrounded by **{{{**  and **}}}** .  Any formatting you apply to the placeholder will apply to the final output.  You also need to signify where the block of text is that you want to repeat for each row of the database.  You will surround this block with **[!-- BEGIN report_row --]**  and **[!--END report_row --]** .  See below for details when using a table for your output.

Here are the placeholders you can use in your file.  Special placeholders being with **++** .  Field placeholders match the **form+field**  name in the report view.  The header placeholders can be used anywhere in the document.  Some may apply only inside or outside the loop for the report.

{| border="1" cellspacing="0" cellpadding="5" align="center"
! Placeholder
! Applies
! Description
|- 
| {{{++report_title}}}
| Outside Row Loop
| The title of the report.
|-
| {{{++report_description}}}
| Outside Row Loop
| The description of the report.
|-
| {{{++report_limit}}}
| Outside Row Loop
| The selected report limits when this report was generated.
|-
| {{{++user_name}}}
| Outside Row Loop
| The user name of the user who generated the report.
|-
| {{{++time}}}
| Outside Row Loop
| The time the report was run.
|-
| {{{++header+'''form+field'''}}}
| Any
| The header for the given field.
|-
| {{{++row_num}}}
| Inside Row Loop
| The current row number for the record.
|-
| {{{'''form+field'''}}}
| Inside Row Loop
| The value for the given field in the report view.
|-
| {{{'''form+field+width=2.0in,maxheight=3.0in}}}
| Inside Row Loop
| If the form field is an image, then extra dimensional formatting information can be provided.
|-
| {{{'''++limit+form+mapfield'''}
| Inside Row Loop
| If a limit has been set for one of the the form in this report via a MAP field, then this is the display name of the form that mapfield maps to.
|-
| {{{'''++limit+form+mapfield+field'''}
| Inside Row Loop
| If a limit has been set for one of the the form in this report via a MAP field, then this is the display value of field for the mapped form that mapfield maps to.
|}

This is the example from the sample module.  You can download the  `source file <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/download/head:/staffform.odt-20120126055155-qjun6vhyfw79qnhf-4/StaffForm.odt>`_  for this to see the formatting.


.. code-block::

    {{{++report_title}}}
    {{{++report_description}}}
    {{{++report_limit}}}
    Report printed by {{{++user_name}}} at {{{++time}}}.
    [!-- BEGIN report_row --]
    {{{++row_num}}}. {{{person+surname}}}, {{{person+firstname}}}
    {{{++header+facility+name}}}: {{{facility+name}}}			{{{++header+work+telephone}}}: {{{work+telephone}}}
    {{{++header+position+title}}}: {{{position+title}}}			{{{++header+work+email}}}: {{{work+email}}}
    {{{++header+department+name}}}: {{{department+name}}}
    
    [!-- END report_row --]
    


When you want to repeat a row in a table for the rows in your report, you need to change the BEGIN and END statements to be **[!-- BEGIN row.report_row --]**  and **[!-- END row.report_row --]** .  See the  `table example <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/download/head:/stafftableform.odt-20120126055155-qjun6vhyfw79qnhf-5/StaffTableForm.odt>`_  from the sample module for an actual file.  The example below has been truncated for space.

{| border="1" cellspacing="0" cellpadding="5" align="center"
! #
! {{{++header+person+surname}}}
! {{{++header+person+firstname}}}
! {{{++header+work+email}}}
|-
| [!-- BEGIN row.report_row --]{{{++row_num}}}
| {{{person+surname}}}
| {{{person+firstname}}}
| {{{work+email}}}[!-- END row.report_row --]
|}


Creating the Module
~~~~~~~~~~~~~~~~~~~

Once you have created the ODT template file, you'll need to create a module to place the file and configure the printed forms for your report.  The module needs an odt_templates directory where you can place your ODT file as well as the module configuration file.  You should require the CustomReports-PrintedReportsODT module so the *Forms Print*  button will appear on your report view.

For your configuration file, you will need to create a node under the report view this template applies to.  All the fields you use in the template must be enabled in the report view.  The **printed_forms**  node should be in the top level of your report view and then a unique name for this printed form template.  Below that you need to define the **template**  which is the name of the template file in the odt_templates directory and **displayName**  for what appears when the user wants to view this template.  The configuration for the sample module is below with two printed forms defined.  This sample also requires the ihris-manage-CustomReports-staff-reports module since that's where the staff_directory report view is defined.



.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="sample-staff-list-printed-form">
      <metadata>
        <displayName>Sample Staff Printed Forms</displayName>
        <description>Sample staff printed forms generated from the staff_directory report view.</description>
        <requirement name="ihris-manage-CustomReports-staff-reports">
          <atLeast version="4.1" />
          <lessThan version="4.2" />
        </requirement>
        <requirement name="CustomReports-PrintedReportsODT">
          <atLeast version="4.1" />
          <lessThan version="4.2" />
        </requirement>
        <path name="odt_templates">
          <value>./odt_templates</value>
        </path>
      </metadata>
      <configurationGroup name="sample-staff-list-printed-form"     
                          path="/modules/CustomReports/reportViews/staff_directory/printed_forms">
        <configurationGroup name="staff_form">
          <configuration name="template">
            <value>StaffForm.odt</value>
          </configuration>
          <configuration name="displayName" locale="en_US">
            <value>Staff Form</value>
          </configuration>
        </configurationGroup>
        <configurationGroup name="staff_table">
          <configuration name="template">
            <value>StaffTableForm.odt</value>
          </configuration>
          <configuration name="displayName" locale="en_US">
            <value>Staff Table</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    </I2CEConfiguration>
    



