Data Interoperability
=====================

This article describe the data-interoperability features present in version 3.2 and later.
==Data Structure==
The data structures defined below are all declared to the iHRIS system by defining them in the configuration XML files for the various [[Module Structure | modules]].  
===Forms and Fields===
The individual data elements of the system are called fields, all of which are associated to a sub-class of I2CE_FormField.  This class describes how the data defined for this field should be represented as a string as well as how it should be displayed to the end-user in either a read-only or edit context.  Examples include dates, times, integers, mapped values (see below), strings, multi-line strings, currencies, and binary data.

Individual data elements, or fields, are collected together in forms.   An instance of a form are the values associated with a particular unique ID. You may think of a form as a row in database table, and a field as a column of that table. For example a person form may be defined as:
*person
**firstname (string)
**surname (string)
**date_of_birth (date -- month/day/year)
while an instance would be:
*person
**id=9234
**firstname := 'Jill'
**surname := 'Schwartz'
**date_of_birth := '04/04/1974'
===Mapped Fields===
There are special fields, which subclass I2CE_FormField_MAPPED, whose values are references to other forms which subclass I2CE_List.  For example, we could amend the above 'person' form to include a field 'place_of_birth' which take values in any of the following list forms (and their fieldss):
*country
**name (string)
*region
**name (string)
**country (map, with values in 'country')
*district
**name (string)
**region ((map, with values in 'region')
*county
**name (string)
**districy (map, with values in 'district')

===Parent/Child Relationship===
A second type of relationship between forms is the parent/child relationship.  You may specify a form has having one or more forms as a child.  For example, suppose we defined the 'salary' form as follows:
*salary
**start_date (date -- month/day/year)
**end_date (date -- month/day/year)
**amount (currency)
then an instance of a 'person' form may many instances of the 'salary' form as children which reflects their change in salary over time.

==Importing Data==
One fundamental means available to the system of importing data from other information systems is through defining various [[Form Storage Mechanisms|storage mechanisms]] for the form data.

==Exporting Data==
The essential means by which data can be made to other systems is through the custom reporting system, which consists of two major components, the form relationship and the report.  An alternative is to use the cached tables.
===Cache Tables===
To increase speed of access time, as well as to easily inspect the data,  all the data for various forms are cached to individual tables within the database.  Each form has its own cache table, with the default prefix ''hippo_.''  For example, the data in the ''person'' form is cached into the ''hippo_person'' table.  The columns of the table are the fields of the form, as well as one for the id and parent form. There is a row for each instance of a form.  

Dumping the hippo (cached) tables is one method to get at the raw data of the forms.
===Form Relationships===
A form relationship describe the basic relationships of the various forms within the system.  A form relationship begins by choosing a primary form for the relationship.   Once a primary form has been chosen for the relationship, you may limit the instances of the forms chosen by describing a limit as in [[Limiting Forms]].

For any form in a form relationship, you can adjoin an additional form which somehow links to that form.  That link can either be either through the parent/child relationship or through the mapped values relationship.  Any ''joined'' form can then be limited as the primary form was.  

Form relationships can either be defined using [[Configuration (Magic) Data | configuration (XML)]] data, or via the on-line GUI tool.


Please take a look at the following [[Custom Reporting -- Creating Form Relationships#Example|example]].

===Custom Reports===
Once a form relationship has been defined, a report can built by selecting the data fields which are relevant to this report.  The system will then create a table in the database which holds the data in the report, the columns of which are the selected fields, and the rows of which are each the collection of forms satisfying the form relationship.

Currently, this data can be view through the web browser, exported to a CSV file, exported to a HTML file,  printed as PDF, and viewed with charting software.  There are plans to make available the data via other formats, such as the Indicator Exchange Format (IXF).  The various exports of the data are defined by subclassing I2CE_CustomReport_Display as appropriate.

[[Category:Interoperability]]
