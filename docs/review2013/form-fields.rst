Form Fields
===========

This article describes the main data types, or form fields, used by iHRIS. These fields are defined in Magic Data; this page describes the details of how they should be defined.  

Magic Data for Defining Fields
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Each form class $formClass contains a list of fields.  A field $field in $formClass is defined at:
 /modules/forms/formClasses/$formClass/fields/$field
which has the following sub-nodes

* formfield: Required. Needs should be on of the field [[#Field Types|type]] such as INT
* in_db: Optional.  It should be either 0 or 1. If not set, defaults to 1.  If 1, then this field should be saved into the database
* required: Optional.  It should be either 0 or 1. If not set, defaults to 0. If 1, then this field needs to be set before it can be considered valid
* unique: Optional.  It should be either 0 or 1. If not set, defaults to 0.  If 1, then the value of this field needs to be unique among all instances of the form
* headers: Optional.  It is itself a parent node, each child node is a string value.  You can choose a different header by specifying the header attribute in a template file.
* *default: Optional scalar node.  The default title/header displayed for the field.  This header is used if no header attribute is specified in the tempalte.
* *$display1: Optional scalar node.  Same as 'default'
* *$display2: Optional scalar node.  Same as 'default'
* *...

Field Types
~~~~~~~~~~~
Each field has a type.  The types define how they are displayed to the end user in both an edit and view only context. It also contains information about the type of column the data should be saved in a database.
The available types are:

* [[Class: I2CE_FormField_BOOL |BOOL]] is implemented by the class I2CE_FormField_BOOL is a choice between true and false
* [[Class: iHRIS_FormField_CURRENCY | CURRENCY]] is implemented by the class iHRIS_FormField_CURRENCY and is a currency type and an amount
* [[Class: I2CE_FormField_DATE_HMS |DATE_HMS]] is implemented by the class I2CE_FormField_DATE_HMS is a time only
* [[Class: I2CE_FormField_DATE_MD | DATE_MD]] is implemented by the class I2CE_FormField_DATE_MD is a month and day
* [[Class: I2CE_FormField_DATE_TIME | DATE_TIME]] is implemented by the class I2CE_FormField_DATE_TIME is a year, month, day and time
* [[Class: I2CE_FormField_DATE_YMD | DATE_YMD]] is implemented by the class I2CE_FormField_DATE_YMD and is a year, month and day
* [[Class: I2CE_FormField_DATE_Y | DATE_Y]] is implemented by the class I2CE_FormField_DATE_Y and is a year
* [[Class: I2CE_FormField_INT_GENERATE | INT_GENERATE]] is implemented by the class I2CE_FormField_INT_GENERATE  and is integer sequence that will populate the next value in the sequence
* [[Class: I2CE_FormField_INT | INT]] is implemented by the class I2CE_FormField_INT is an integer
* [[Class: I2CE_FormField_INT_LIST | INT_LIST]] is implemented by the class I2CE_FormField_INT_LIST is an array of integers
* [[Class: I2CE_FormField_INT_RANGE | INT_RANGE]] is implemented by the class I2CE_FormField_INT_RANGE is a ranged drop down of integers and was introduced in version **4.1** .  The range is specified by setting start (defaults to 0), end (defaults to 10) and step (defaults to 1) in the meta section of the field's options.
* [[Class: I2CE_FormField_MAP | MAP]] is implemented by the class I2CE_FormField_MAP and is the name and id of a list form
* [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]] is implemented by the class I2CE_FormField_MAP_MULT  and is an array of names and ids for list forms
* [[Class: I2CE_FormField_REFERNCE | REFERENCE]] is a field which is a reference to another form and whose display value is based on the fields in that referenced form.  You can see the defintion [[Reference Field | here]]
* [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]] is implemented by the class I2CE_FormField_STRING_LINE and is a string
* [[Class: I2CE_FormField_STRING_MLINE | STRING_MLINE]] is implemented by the class I2CE_FormField_STRING_MLINE and is multi-line string
* [[Class: I2CE_FormField_STRING_PASS | STRING_PASS]] is implemented by the class I2CE_FormField_STRING_PASS is a password value
* [[Class: I2CE_FormField_STRING_TEXT | STRING_TEXT]] is implemented by the class I2CE_FormField_STRING_TEXT is a large multi-line string
* [[Class: I2CE_FormField_YESNO | YESNO]] is implemented by the class I2CE_FormField_YESNO and is a choice between Yes and No

Map Fields
^^^^^^^^^^
A MAP or MAP_MULT takes values in a list, which is any form whose implementing class subclasses I2CE_List.  There are some special options for how these lists are displayed.

Meta Magic Data for MAP Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A field of type MAP or MAP_MULT can specify the following 'default'  sub-node.  
Under the magic data node:
 /modules/forms/formClasses/$formClass/fields/$field/meta
We can specify some further information which affects how a field is used as follows:

* form: an optional parent node.  The child nodes are all scalar nodes which specify the forms that this field can take values in.  If not set, the name of the form is assumed to be the name of the field, $field.
* display: An optional parent node.  Each child node is a "named" display for that field which can be referenced in .html templale files.
* *default: Optional parent node.  When displaying a field, if no display is specified, the data under the node "default" is used to determine the display.
* **fields:  Optional scalar node.  This node describe the hierarchy of how the data should be displayed, for example, in a tree view of the data, when selecting the value of this field. It has the general structure "mapform1+mapfield1:mapform2+mapfield2:...:mapformN".  If the *+mapFieldX*  is not present, then we use *mapFormX+1*  for the value of *mapFieldX* .  If the 'fields' entry is is not set, then it is the mapped form is the the name of field.  <br/> When we select a value for the field, we start by displaying all the values for *mapFormN* .  Under each one of these values, we display all values for *mapFormN-1*  whose field *mapFieldN-1*  is *mapFormN*   is and continue down until we get to *mapForm1* .  <br/> If *mapFormXX+mapFieldXX*  is surrounded in square brackets, [ ],  then we don't display the data for that mapped form.
* **orders: An optional parent node.  Child nodes have names which are forms which are selectable by the field:
* ***$form1: Optional parent node. Children are scalar nodes with keys integers and values the name of the field.  If this node is set, then it will override any values that are set under the magic data node: /modules/forms/formClasses/$form1/meta/list/default/sort_fields.  <p/>'''Note''': even if this is $display1, then it will still look at default/sort_fields rather than $display1/sort_fields)
* ***$form2: Optional parent node.  Same structure as in $form1.
* ***...:
* *$display1: Optional parent node. Structure is the same as the "default" display.
* *$display2: Optional parent node. Structure is the same as the "default" display.
* *...
* limits:  Optional parent node.  Child nodes describe any limits that should be applied when populating the list or tree of valid entries
* *default: Optional parent node.  Limits that apply to the default display.  Child nodes are named for each of the selectable forms referenced in list of forms 'form' above.
* **$form1:  Optional parent node.  Limits that apply when reading the data from $form1 in the database.  The structure of this node is the same structure as [[Limiting Forms]]
* **$form2: Optional parent node.  Limits that apply when reading the data from $form2 in the database.  The structure of this node is the same structure as [[Limiting Forms]]
* **...
* *$display1: Optional parent node.  Limits that apply to the display $display1.  Same structure as 'default'
* *...

See also:  [[Defining Forms#Lists | Defining List Forms]]

Meta Magic Data Example
~~~~~~~~~~~~~~~~~~~~~~~
For example, iHRIS_Person has a mapped field, 'residence'.  It's meta node contains the following sub-nodes:

.. code-block:: php

    'form' => Array [
              0 => county
              1 => district
              ],
    'display' => Array [
          'default' => Array [
            'fields' => county:district:[region]:country 
            ] 
        ],
    'limits' => Array [
        'default'=> Array [
            'country'=> Array[
                'operator'=>'FIELD_LIMIT',
                'field'=>'location',
                'style'=>'yes'
             ]
         ] 
    ] 
    

You can also see the  `.xml <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0-dev/view/head:/modules/Person/Person.xml#L208>`_  used to define this in the magic data for the Person module in iHRIS Common.

In this case, the 'forms' node tell us that any member of the county or district list may be chosen as the residence for a person.

In the above example, when selecting a residence for a person, you first choose the country, then the region, then the district.  You may further specify the county.  When displaying a selected residence it will display either:
 District, Country
or
 County, Country District
depending if you have selected the district or county.

Automatically Generated Integers (INT_GENERATE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Automatically generated integers (or INT_GENERATE) are used when a form needs an incremented number to use for an ID but the data entrant may not know what the next available value is.  The user can check a checkbox to increment to the next value or if necessary can type in the number if it is known.  As of version 4.0.2 INT_GENERATE is only supported when the form uses the entry form storage mechanism.  It uses the field_sequence table to keep track of the current maximum value for each form field.

In the field_sequence table there will be an entry with the form field id and the highest value that has been used.  The system checks two possibilities for determining the next available number.  It looks at the field_sequence table if a row exists there for the form field and in the last_entry table for the highest assigned value.  Whichever is higher is then incremented by one and saved to the field_sequence table so it can be accessed the next time a record is added.

If you want to start at 1000 you can just add the form field id and 1000 to field_sequence.  You only need to add something to the field_sequence table if you want it to start higher than the currently saved values.  For example, if you imported data that ranges from 100-400 but you want the generated numbers to start at 1000 then you’ll need to add a row to the field_sequence table.  But if you just want the next number to be 401 then you don’t need to do anything.

