Limiting Forms
==============

Data in iHRIS is stored in forms and fields.   Sometimes you may wish to limit a search for a particular form by some property of its fields.  For example, you may wish to search for a person with first name "Jill."  This article describes the structure of how various limits are applied to forms.  

The iHRIS system will take this abstract representation of a form limit and translate it to appropriate PHP or SQL code as needed. 

Uses
^^^^
The limit data structure is used in, for example:


* I2CE_Form::search()
* I2CE_Form::listFields()
* Form Relationships
* Report Limits

The methods of I2CE_Form add in the ability to limit values based on the storage mechanism.  If you wish to create a new form storage mechanism with search capabilities, you will need to either produce some code to parse the limiting data structure described below or, if you storage mechanism is accessible to the database, you may simply subclass I2CE_FormStorage_Helper_DB.

Limit Styles
^^^^^^^^^^^^
There are many ways that you may wish to limit the values of a particular field, we refer to these as a **limit style.**   For example, *equals*  or *like.* 

Recall that every field is has a type, such as INT or INT_LIST, which translates to a class, such as I2CE_FormField_INT or I2CE_FormField_INT_LIST, all of which sub-class I2CE_FormField.   A type is made available to some sub-class (as well as well of all of its sub-classes) of I2CE_FormField.

Most of these limit style, and their attendant code, can be found in the module **form-limits.**  


Structure of Limiting Data
^^^^^^^^^^^^^^^^^^^^^^^^^^
We allow, on a per-form basis, logical compounds of limits of any field through a nested array (or magic data) structure.  The structure of a limit *expression node*  is as follows:


* operator: Required. Tells us what type of node this expression node is.  Valid values are 'FIELD_LIMIT', 'AND', 'XOR', 'OR', and 'NOT'
* operand: Used only in the case of 'AND', 'XOR', 'OR' and 'NOT' in which case it is required. It is a sub-array/sub-node consisting of zero or more *limit expression nodes.*   In the case of 'NOT' there is the further limitation that the number is exactly one.
* field: Used only need in the case of 'FIELD_LIMIT' in which case it is required.  It is the name of the field for this form we are limiting on.
* style: Used only need in the case of 'FIELD_LIMIT' in which case it is required.  It is the limit style.
* data: Used only need in the case of 'FIELD_LIMIT.' It is a associative array of data used to limit the data by.  If not set, it should be interpreted as the empty array.

For example for a person, we may have:
 array(
   'operator'=>'AND',
   'operand'=>array(
     0=>array(
       'operator'=>'FIELD_LIMIT',
       'field'=>'surname',
       'style'=>'like',
       'data'=>array(
         'value'=>'N%th'
       )
     )
     1=>array(
       'operator'=>'NOT',
       'operand'=>array(
         0=>array(
           'operator'=>'OR',
           'operand'=>array(
             0=>array(
               'operator'=>'FIELD_LIMIT',
               'field'=>'othername',
               'style'=>'equals',
               'data'=>array(
                 'value'=>'Mike'
                )
             ),
             1=>array(
               'operator'=>'FIELD_LIMIT',
               'field'=>'othername',
               'style'=>'equals',
               'data'=>array(
                'value'=>'Michael'
               )
             )
           )
         )
       )
     )
   )

would be interpreted in SQL as:
 ((`person+surname` LIKE 'N%th') AND ( NOT (( `person+othername` = 'Mike') OR (`person+othername` = 'Michael'))))
Unfortunately, with such a statement, you would not find  `Mike Nesmith <http://en.wikipedia.org/wiki/Michael_Nesmith#The_Monkees>`_ .


Existing Styles
^^^^^^^^^^^^^^^
These are the limit styles provided by *form-limits*  version 3.2.0.  Please see the class itself for more up-to-date information.


* I2CE_FormField
* *null: No data array.
* *not_null: No data array.
* *null_not_null: Choose if a value is null or not.  Data array has key 'value' which is either (evaluates to) true for null, or (evaluates to) false for not null.
* *max_parent: No data array.  Only valid in form relationship context.
* *min_parent: No data array.  Only valid in form relationship context.
* *max_parent_form: No data array.  Only valid in form relationship context.
* *min_parent_form: No data array.  Only valid in form relationship context.
* I2CE_FormField_BOOL
* *truefalse: No data array.
* *true: No data array.
* *false: No data array.
* I2CE_FormField_DB_DATE
* *greaterthan_now: No data array.
* *lessthan_now: No data array.
* I2CE_FormField_DATE_Y
* *greaterthan:  Data array has key 'year' which is a year (integer).
* *greaterthan_equals:  Data array has key 'year' which is a year (integer).
* *equals:  Data array has key 'year' which is a year (integer).
* *lessthan_equals:  Data array has key 'year' which is a year (integer).
* *less_than: Data array has key 'year' which is a year (integer).
* *between:  Data array has keys 'min' and 'max' each of which is an array containing the key 'year' which is a year (integer).
* I2CE_FormField_DATE_YMD
* *greaterthan:  Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *greaterthan_equals:  Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *equals:  Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan_equals:  Data array has key 'year' which is a year (integer),  'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *less_than: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *between:  Data array has keys 'min' and 'max' each of which is an array containing the key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* I2CE_FormField_DATE_MD
* *greaterthan:  Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *greaterthan_equals:  Data array has key'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *equals:  Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan_equals:  Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *less_than: Data array has key  'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *between:  Data array has keys 'min' and 'max' each of which is an array containing the key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* I2CE_FormField_DATE_HMS:
* *greaterthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *greaterthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *lessthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *lessthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *between: Data array has keys 'min' and 'max' each of which is an array which contains the keys 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* I2CE_FormField_DATE_TIME:
* *greaterthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *greaterthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *between: Data array has keys 'min' and 'max' each of which is an array which contains the keys 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).



* I2CE_FormField_DB_INT
* *between. Data array has keys 'min' and 'max.'
* *equals. Data array has key 'value' which is a scalar.
* *in. Data array has key 'value' which is a an array of scalar values.
* *greaterthan. Data array has key 'value' which is a scalar.
* *greaterthan_equals. Data array has key 'value' which is a scalar.
* *lessthan. Data array has key 'value' which is a scalar.
* *lessthan_equals. Data array has key 'value' which is a scalar.
* I2CE_FormField_DB_STRING
* *between. Data array has keys 'min' and 'max.'
* *equals. Data array has key 'value' which is a scalar.
* *in. Data array has key 'value' which is a an array of scalar values.
* *greaterthan. Data array has key 'value' which is a scalar.
* *greaterthan_equals. Data array has key 'value' which is a scalar.
* *lessthan. Data array has key 'value' which is a scalar.
* *lessthan_equals. Data array has key 'value' which is a scalar.
* *like. Data array has key 'value' which is a scalar.
* *lowerlike. Data array has key 'value' which is a scalar.  match is case insensitive
* *contains. Data array has key 'value' which is a scalar.  match is case insensitive
* I2CE_FormField_DB_TEXT
* *between. Data array has keys 'min' and 'max.'
* *equals. Data array has key 'value' which is a scalar.
* *in. Data array has key 'value' which is a an array of scalar values.
* *greaterthan. Data array has key 'value' which is a scalar.
* *greaterthan_equals. Data array has key 'value' which is a scalar.
* *lessthan. Data array has key 'value' which is a scalar.
* *lessthan_equals. Data array has key 'value' which is a scalar.
* *like. Data array has key 'value' which is a scalar.
* *lowerlike. Data array has key 'value' which is a scalar.  match is case insensitive
* *contains. Data array has key 'value' which is a scalar.  match is case insensitive
* I2CE_FormField_YESNO
* *yesno: No data array.
* *yes: No data array.
* *no: No data array.


