Forms and Form Classes
======================

Records are stored in the Intrahealth Informatics Core Engine (I2CE) in forms, which consist of collection fields.   You can think of a form as table in a database and a field as a column of that table.  

The logic of a form is handled by a *Form Class*  which extends **I2CE_Form.**   The logic of a field is handled by a class extending *I2CE_FormField.* 



Referencing in Templates
^^^^^^^^^^^^^^^^^^^^^^^^
The [[Pages and Templates|templating]] system allows easy reference to data stored in a form in an html template.  For example to reference a person's firstname you can use:
 <nowiki><p  id='my_person'>You are looking at <span type='form' name='person:firstname'/> <span type='form' name='person:surname'/>!</p></nowiki>
Would be  turned into
 <nowiki><p id='my_person'>You are looking at Joe Smith!</p></nowiki>
if there was a 'person' form set at or above the node with id 'my_person'.  The html is modified by the templating system.  In version 3.1, this is done by the 'processForms()' method of the *forms*  module class, *I2CE_Module_Forms* , by [[Module Structure#Hooked Methods|hooking]] into the hook 'process_templatedata_FORM' defined in I2CE_Module_TemplateData.

It is the responsibility of the page to make sure the appropriate form is assigned to the appropriate node in the template.


Forms and Their Classes
^^^^^^^^^^^^^^^^^^^^^^^

A form $form is linked to a form classes by specifying the data at */modules/forms/forms/$form/class* 
to be the name of the form class.  For example:
 I2CE::getConfig()->modules->forms->person->class = 'I2CE_ManagePerson';

The classes may or may not exist as files.  If there is logic that a form needs to perform, for instance on its *validate()*  and *save()*  methods it will exist.  Otherwise, they exist virtually.   Starting in version 3.2 such a virtual class is generated 'on-the-fly' by making use of the *__autoload()*  method.


Fields and Their Clases
^^^^^^^^^^^^^^^^^^^^^^^
All fields of a form have a name and a type.  The name of the fields is how the field is referenced by the form as a public variable by using the *__get()*  and *__set()*  methods.  For example:
 if ($person instanceof I2CE_Person)  {
  echo "$person->firstname . "\n";
 }

The types effect how the data is stored in the database and how the data is displayed and entered in the system.  The following are a list of common types:


* BOOL  A boolean True/False value
* CURRENCY A currency value
* DATE_HMS A hour, minute, second time
* DATE_MD A month and date
* DATE_TIME A time
* DATE_Y A year
* DATE_YMD A year, month and date
* INT An integer value
* INT_LIST A list of integers
* INT_GENEREATE An integer which automatically increments
* STRING_LINE A line of text
* STRING_MLINE Several lines of text
* STRING_PASS A password
* STRING_TEXT A lot of text
* YESNO A Yes/No value
A $type is handled by the class I2CE_FormField_$type

<!--  =Forms and Their Fields=
The structure of forms, their classes and fields and where they are defined in can be easily browsed at:


* `Form and Field Browser <http://open.intrahealth.org/ihris-docs/form_documentor/>`_  Applies to development version 3.2
(bad link) -->

=How the Data is Stored=
Although you may loosely think of a form as being a table in the database, it is not quite so.

Version 3.1
^^^^^^^^^^^
In version 3.1 all data stored in forms is stored in the 'entry' and 'last_entry' tables.  These tables keep a history of the changes made to the data based on the user that changed the data, the type of the change, and the time of the change.   The 'entry' table has all of the history, while the 'last_entry' table only contains the most recent changes to a field.



Version 3.2
^^^^^^^^^^^
Starting in this version we are enabling multiple storage mechanisms for a form.  The default storage mechanism will still be through the 'entry' and 'last_entry' table.   

In addition we will enable storage to specified database tables to allow the administrator to easily incorporate outside data sources into the Custom Reporting utility.  This will be either read-only or read-write as the user specified.

We also allow storage in Magic Data.  This is primarily intended for list data that a administrator wishes to maintain centrally in a module and then ship out to regional offices.  In addition, the lists stored in Magic Data will be localizable.

[[Category:Developer Resources]]
