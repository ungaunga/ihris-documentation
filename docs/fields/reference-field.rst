Reference Field
================================================

This describe the magic data structure used for defining a [[Class: I2CE_FormField_REFERENCE | REFERENCE ]] field.  These options all live under
 /modules/forms/formClasses/$formClass/fields/$field
for the given form class $formClass and field name $field.



Magic Data Structure
^^^^^^^^^^^^^^^^^^^^


* meta: required parent node.
* *form: optional parent node.  subnodes are scalar nodes whose values are the forms that this field can reference.
* *any_form: optional scalar node.  if evaluates to true, then any form can be selected regardless to what is listed under the sibling node, 'form'
* *display: required parent node.  names of sub-nodes are the names of the forms that this field can reference.
* **$refForm: required parent node.  The name of the node, $refForm, is a form that this field can reference.
* ***default: required parent node.  The default display for the referenced form
* ****printf: required (translatable) scalar node.  A string which will get passed to printf to display the node.  Example is "%s %s" which contains two substitutions
* ****printf_args: required parent node:  Sub-nodes should be ordered integers.  requires 0..n sub-nodes if the printf contains (n+1) substutions.
* *****0: required scalar node the name of the first field whose display value is passed to printf
* *****1: requried scalar node the name of the next field whose display value is passed to printf
* *****...
* *****n: requried scalar node the name of the last field whose display value is passed to printf
* ***$display: optional parent node.  Another named display for this field.  Sub-nodes are exactly the same as those defined for default


HTML Template
^^^^^^^^^^^^^
To display the default 


.. code-block:: xml

       <span type='form' name='$form+$field'/>
    


To select another display, $display:


.. code-block:: xml

       <span type='form' name='$form+$field' show='$display'/>
    



Editing the Field Value
^^^^^^^^^^^^^^^^^^^^^^^
For the moment, the field is not editable.  Rather its value should be set by a page's logic.

At a later point, we can make the value set via the selection of a primary form (or other?) in from a report.

[[Category:Fields]]
