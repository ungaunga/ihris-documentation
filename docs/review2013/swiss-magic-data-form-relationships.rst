Swiss Magic Data -- Form Relationships
================================================

In this article we over view the [[Swiss Magic Data Editor|swiss magic]] structure used to create the web interface to define [[Custom Reporting -- Creating Form Relationships|form relationships]].  Recall that a swiss node of type XXX is implemented by the class I2CE_Swiss_XXX.  All the classes mentioned are contained in the 
 I2CE/modules/Forms/modules/FormRelationships/lib
directory.



FormRelationship_Base
^^^^^^^^^^^^^^^^^^^^^
This is the base class which is sub-classed by all of the Swiss classes used to edit form Relationships.


FormRelationships
^^^^^^^^^^^^^^^^^
The **root swiss node** of a the form relationship editor has type *FormRelationships.*  
It has the following functionality:


* It is a container node which contains all of the form relationships.
* Creates a new form relationship with a given "Display Name" and "Short Name" by creating a new child magic data node.  The new relationship can be based on:
* *Choosing a primary form
* *Choosing an existing relationship to copy from.

All children of this swiss node have type [[#FormRelationship]].


FormRelationship
^^^^^^^^^^^^^^^^
This is the swiss node that contains all the information about a particular form relationship.

It has the following functionality:


* Specify the form
* Specify the display name of this form in the relationship
* Specify the description of this form in the relationship
* links to the [[#FormRelationship_Joins|joined forms]] menu
* links to the menu for [[#FormRelationship_Where|limiting]] this form
* links to the menu [[#FormRelationship_ReportingFunctions|sql functions]] menu

The child swiss nodes are named:


* 'reporting_functions' with type [[#FormRelationship_ReportingFunctions]]
* 'joins' with type [[#FormRelationship_Joins]]
* 'where' [[#FormRelationship_Where]]


FormRelationship_Joins
^^^^^^^^^^^^^^^^^^^^^^
This is the swiss node that contains all information about forms joined to the form of the parent swiss node.
It has the functionality:


* Join in a form related the the form defined by parent swiss node
All children of this swiss node have type [[#FormRelationship_Join]].

FormRelationship_Join
^^^^^^^^^^^^^^^^^^^^^
This is the swiss node that represents a form joined into the form relationship.  

It subclasses  [[#FormRelationship]] and has almost the same functionality and children. The difference is that:


* It does not link to the SQL Functions menu
* It shows how this form is joined to the parent form in the relationship (the primary form does not need this as it has no parent)
* It allows you to "drop empty rows."  <br/> **Note:** The language should be cleaned up here as we use form relationships outside of the Custom
Reporting scenario.  It means that a set of forms potentially satisfying a form relationship is will fail to satisfy the relationship if there is no form  matching the where clause at this node.


FormRelationship_Where
^^^^^^^^^^^^^^^^^^^^^^
This provides a where (sub)-clause for a form relationship.  It has the following functionality:



* if not specified, allow you to specify the "type" of the node as either a logical operator (AND, OR, NOT, XOR) or as a limit on a field in the form
* if specifed, allows you to change the "type"

There is one child swiss node 'operands' which has type [[#FormRelationship_Where_Operands]]

 **Note:** The functionality of this swiss node should probably be moved to a sub-module of the FormLimits modules


FormRelationship_Where_Operands
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This node is used in the case where the parent swiss node is one of the logical operators AND, OR, NOT or XOR.
It has the following functionality:


* Displays the existing operands
* Adds a new operand for the logical operators if possible (NOT has only one operand)
* Allows you to remove an operand

All children of this node are of type [[#FormRelationship_Where]]

 **Note:** The functionality of this swiss node should probably be moved to a sub-module of the FormLimits modules


FormRelationship_ReportingFunctions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This swiss node is a container for all of the SQL functions that are defined for the form relationship. It has the following functionality:


* display the existing sql functions in the relationship
* adds in a place for a new sql function determined by "Short Name," a "Display Name" and a "Description"

All children of this node have type [[#FormRelationship_ReportingFunctions]].

 **Note:**  This functionality should probably be moved to be a sub-module of Forms.


SQLFunction
^^^^^^^^^^^
This swiss node is used to define a SQL function in a relationship.  It has the following functionality:


* edit the display name
* edit the description
* edit the SQL function which is applied to any of the form fields in the relationship
* choose the return type of the SQL function to be any of the (non-abstract) subclasses of I2CE_FormField.

 **Note:**  This functionality should probably be moved to be a sub-module of Forms.
[[Category:Magic Data]][[Category:Review2013]]
