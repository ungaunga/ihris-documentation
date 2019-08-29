Standardized Letters (ODT)
==========================

The printed forms module is used to print "standardized" or "official" forms based upon the data in the system.  For example, it might be the registration number for a nurse. The output will be an Open Office Document. This document can be read readily by Microsoft Word 2003.

This module first appears in version 4.0.14 of the iHRIS Suite.

Depending on your needs, you may wish to look at these other methods for standardized form generation:

* [[Printed Forms]]
* [[Printed Forms form Relationships (ODT)]]
* [[Printed Forms with Reports (ODT)]]

Source Data
^^^^^^^^^^^
The source data for the printed form will be  based on a [[Custom Reporting -- Creating Form Relationships|form relationship]].

Magic Data Details
^^^^^^^^^^^^^^^^^^
All standardized forms will be stored under the magic data node:
 /modules/PrintedForms/forms

* relationship: Required scalar node. the name of the form relationship that this form is based off of.  It needs to be the name of a child node of */modules/CustomReports/relationships*
* displayName: Optional scalar node.  The name of the printed letter as displayed to the end user.
* archive: Optional scalar node.  If set it should be a named form in the relationship.  If it is a valid named form, then it will enable archiving of this printed letter as a child form of the corresponding named form.  You should ensure that this form has *generated_doc*  as a valid [[Defining Forms | child form]].
* template: Required scalar node.  The name of a .odt file that will be used as a template to generate this report.   It should be located in a directory/path registered in the category ODT_TEMPLATES
* render: Required scalar node.   Needs to be set to ODT

Text Subsitutions
~~~~~~~~~~~~~~~~~
Whenever the text **{{{XXXXXX}}}**  is found in the open office document, it will attempt to substitute the text according to the following rules if **XXXXXXX** ' matches the following forms:

* '''formname'''+'''field''': a report form fields to substitute into the printf.  E.g. "person+surname,person+fisrtname,registation+number":
* *In the case that **formname+field**  is a image (I2CE_FormField_IMAGE) then it will try to put the image in the file.  You can adjust the image's  height and width by *{{{formname+field+height=2.0in,maxwidth=1.0in}}} or * {{{formname+field+width=1.0in,maxheight=2.0in}}}''  **Note:**  This feature will only be a part of version 4.0.17.
* +'''relationshipFunction''':  The evaluation of the named function in the the form relationship.  Example +age65 which be the year the person turns 65 in the staff relationship
* ++date('''XYZ'''): The data formatted according to **XYZ**   (unquoted) via  `strfrtime <http://us2.php.net/manual/en/function.strftime.php>`_  functions.  Example ++date(%Y) is the four digit year
* ++date:  The date.  This is the same as ++date(%x).
* ++user:  The name of the user printing the form
* ++eval('''XYZ'''):  Evaluate the php code **XYZ** .  Example is ++eval(strftime("%Y")+60)  would add 60 to the current year

Example
^^^^^^^
This module is in use in Botswana to generate a data verification form, based on the "botswana_staff" report.  The two parts are:

* Registering the template file "verify.odt" with the botswana staff report.   `Here <http://bazaar.launchpad.net/~ihris+botswana/ihris-manage/4.0/view/head:/modules/StandardLetters/StandardLetters.xml>`_  is the configuration .xml.  The important bits are:
* *lines 12-14:  register a new path with category "ODT_TEMPLATE" to look for .odt files in
* *line 17:  Tells us we are working under the magic data node "/modules/PrintedForms/forms"
* *lines 18-34: registers the "verify" standard letter with the following infomration:
* **lines 19-21: the report relationship we are using is "botswana_staff"
* **lines 22-24: tells us that this standardized form should be generated from an open office, odt, document
* **lines 26-27: tells us that when you archive this form, it should be saved as a child form of the person form
* **lines 28-30: the display name, "Personnel Data Verification", that is shown for when this standard form is added to a page
* **lines 31-33: the name of the template .odt file that is used to generate this standard form.  In this case it is "verify.odt."  The system will search any paths registered in the categoru "ODT_TEMPLATE" to find this form.
* The open office[ ` template document <http://bazaar.launchpad.net/~ihris+botswana/ihris-manage/4.0/download/head:/verify.odt-20110511123858-wxc39k20ylvlfzur-23/Verify.odt>`_ ]

