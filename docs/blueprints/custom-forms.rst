Custom Forms
================================================

Provide a means to design forms from the [[Swiss Magic Data Editor|web interface]].

Form Classes Swiss Magic Data Editor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Define and edit the form Classes available in the system.

I2CE_Swiss_FormClasses
~~~~~~~~~~~~~~~~~~~~~~
This is the root swiss node for the form classes interface.
Will be associated (via the I2CE_Page_SwissMagic) to the /modules/forms/formClasses magic data node.

Functionality:


* lists all the available form classes
* * i2xe_swiss is an itereator so you can do a foreach ($this as $name=>$swissChild)
* allow the creation of a new form class by specifying:
* *the class name. this will the name of the child node added to magic data.
* *the class that it extends (Defaults to I2CE_Form). should be a drop down list of the available classes.  You need to validate this class before you create the child magic data node

All of this children have type I2CE_Swiss_FormClass


I2CE_Swiss_FormClass
~~~~~~~~~~~~~~~~~~~~
This is the the swiss node associated to each of the subclasses of I2CE_Form.
Correponds to the magic data node /modules/forms/formClasses/$formClass
If has the following functionality:


* links to the [[#I2Ce_Swiss_FormClass_Fields|fields]] menu
The child 'fields' has type [[#I2CE_Swiss_FormClass_Fields|FormClass_Fields]]


I2CE_Swiss_FormClasss_Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Container swiss node to  hold all of the fields.  
Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields.
Functionality:


* lists all the fields in this class
* allow you to add a new field to this class by specifying
* *a short name for the field.
* **This will be the name $name of the child magic data node to create
* *the subclass of I2CE_FormField which implements this field
* **look at code behind [[Swiss Magic Data -- Form Relationships#SQLFunction|sql functions]] to get the list of valid dorm field classes
* **the populating of the drop down for form field class should be handled i think by i2ce_swiss_formclasses_field
* *A default header

Each child of this node has type FormClass_Field


I2CE_Swiss_FormClass_Field
~~~~~~~~~~~~~~~~~~~~~~~~~~
This is the swiss node responsible for defining the field in a form class.
Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields/$field.
Functionality:


* specify the 'formfield' this is (almost) the subclass of I2CE_FormField which this field takes values in.
* *Really it is the key of the key/value pairs options under /modules/forms/FORMFIELD (e.g. DATE_Y, STRING_LINE)
* *Probably want to add meta data to formfield so that the user knows DATE_Y, STRING_LINE, STRING_MLINE are supposed to do.
* allows you to specify if this field is stored in the DB. (defaults to true)
* *use I2CE_Swiss->get/setField() $field='in_db'
* allows you to specify if this field is required. (defaults to false
* *use I2CE_Swiss->get/setField() $field='required'
* links to the [[#I2CE_Siwss_FormClass_Field_Headers| headers]] menu
* allows to specify the default values (either the fields default or default_eval)


I2CE_Swiss_FormClass_Field_Headers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Specifies the headers for a form field. 
Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields/$field/headers.
Functionality:


* specify the 'default' header.
* *use get/setField() with $field = 'default'
* specify any other named header named $name.
* *use I2CE_Swiss->get/setField() with $field = $nam


I2CE_Swiss_FormClass_Field_Meta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Container node for the meta data associated to a field.
Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields/$fields/meta.

Functionality:


* If the form field subclass I2CE_FormField_MAPPED then links to the [[#I2CE_Swiss_FormClass_Field_Meta_Displays|displays]] menu
* If the form field subclass I2CE_FormField_MAPPED then links to the [[#I2CE_Swiss_FormClass_Field_Meta_Limits|limits]] menu
* If the form field subclass I2CE_FormField_MAPPED then links to the [[#I2CE_Swiss_FormClass_Field_Meta_Form|selectable forms]] menu


I2CE_Swiss_FormClass_Field_Meta_SelectableForms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields/$fields/meta/form and is the list of the forms that a mapped field can take values in:
Functionality:


* list the existing valid forms (note, if there are none than the valid form is the field name itself)
* add a valid form (NOT a form class)
* *The valid forms are those forms whose implementing form class extends I2CE_List
* *The list of available forms are accessed as keys of  /modules/forms/forms


I2CE_Swiss_FormClass_Field_Meta_Displays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Container node for the various displays of mapped fields. 
Corresponds to the magic data node. /modules/forms/formClasses/$formClass/fields/$fields/meta/displays.

Functionality:


* lists any existing displays
* allows the creation of any new display by specfiying a shortname.  By default it should fill in the shortname to be 'default'

All children have type FormClass_Field_Meta_Display


I2CE_Swiss_FormClass_Field_Meta_Display
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Handles setting the displays for mapped fields.

 **NEED TO FILL IN WHAT IS VALID HERE (e.g. county:district:[region]:country)**

Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields/$fields/meta/displays/$display.




I2CE_Swiss_FormClass_Field_Meta_Limits
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Container node for the limits on  various displays of mapped fields. 
Corresponds to the magic data node. /modules/forms/formClasses/$formClass/fields/$fields/meta/limitss.

Functionality:


* lists any existing limits
* allows the creation of any new limit by specfiying a shortname.  By default it should fill in the shortname to be 'default'

All children have type FormClass_Field_Meta_Limit


I2CE_Swiss_FormClass_Field_Meta_Limit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Handles setting the limit for mapped fields.

This should funcionality should be merged with that of [[Swiss Magic Data -- Form Relationships#FormRelationship_Where]].

Corresponds to the magic data node /modules/forms/formClasses/$formClass/fields/$fields/meta/limits/$limit.

It is used, for example when displaying the list of valid countries for a the location field of person.


I2CE_Swiss_Forms
^^^^^^^^^^^^^^^^
 **NEED TO SPEC THIS OUT**


* Define a form
* *choose the form class
* *choose a short name
* *give a description
* *set the [[Form Storage Mechanisms|data storage mechanism]]

[[Category:Blueprints]]
