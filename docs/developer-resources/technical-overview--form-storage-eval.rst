Technical Overview: Form Storage -- Eval
========================================

This form storage mechanism is present in version >= 4.0.3.


Form Storage Options
^^^^^^^^^^^^^^^^^^^^

The options specifying a php-eval storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/eval
It has the following structure:



* records:  The function to call to get the list of available records/form ids.  As of version 4.2, the variable $mod_time, if non-negative, should be checked to retrieve only the records changed since a given time.
* parent: optional parent node
* *populate: optional scalar node.  if set, it is the php code used to get the parent id of the current id.  the current id can be accessed as $id
* fields: optional parent node containing a sub node for each field indexed by the $fieldName
* *$fieldName: optional parent node
* **populate: optional scalar node.  if set, it is the php code used to get the db-value of the field for the current id.  the current id can be accessed as $id


