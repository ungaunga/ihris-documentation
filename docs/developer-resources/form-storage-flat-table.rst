Form Storage -- Flat Table
==========================

The *Flat Table*  storage mechanism allows you to map any flat table that you have in your database into a form.  

Specifying Flat Storage
^^^^^^^^^^^^^^^^^^^^^^^
To specify that the form $form has a flat table storage mechanism set by setting
 modules/forms/forms/$form/storage
to have value **flat.** 

Form Storage Options
^^^^^^^^^^^^^^^^^^^^
The flat storage mechanism is defined so that, by default, it can read in the cached "hippo_" tables of form data.  If you situation, is not exactly this, then you can take advantage of the options as described in this section.

The options specifying a flat table storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/flat
It has the following structure:

* table: Optional scalar node. The table to use.  E.g. my_table, `my weird_table`, `some_other_database`.`table`.  You are responsible for back-tics if required. If it is not set, it determines the table name from the table_prefix set in the [[Technical Overview: Form Storage -- Flat Table#Global Options|global options]].
* id: Optional parent node.  The data defining how to associate an id per row of this table.  If it is not set, the the data is populate from the column 'id.'
* *col: Optional scalar node.  Specifies a column of the table to be used as the id.  You are responsible for back-tics.
* *function: Optional scalar node.  Specifies a SQL function  whose result will the id for the form. 'col' takes precedence.
* *form_prepended: Optional scalar node. Defaults to true. If true, it means the form name has been prepended to the id.  Otherwise, it assume that the column is just the id.   If true, this form is not writable.
* fields: Optional parent node.  Specifies how the data of the your form is associate to a row of your table.  Each child of this node is the name of a field $field of your form.  By default, all fields of a form are populated, and are all assumed to come from the column with that field name.
* *$field:  Parent node with the following child nodes.
* **col: Optional scalar node.  Specifies a column of the table to be used as the id. You are responsible for back-tics.
* **function: Optional scalar node.  Optional scalar node.  Specifies a SQL function  whose result will as the value for the field. 'col' takes precedence.
* **enabled: Optional scalar node.  If present and evaluates to false, it means we should not populate this field.
* parent: Optional parent node.  If not present, we assume the parent is populated from the column 'parent'.  It has the following child nodes:
* *enabled: Optional scalar node.  If present and evaluates to false, it means getParent() should return the trivial parent id, '0'.
* *col: Optional scalar node.  Specifies a "column" of the table to be used as the id for the parent. You are responsible for back-tics.
* *function: Optional scalar node.  Optional scalar node.  Optional scalar node.  Specifies a SQL function  whose result will as the value for the parent form's id. 'col' takes precedence.
* writable: Optional scalar node.  Defines the write access to the table.  If not present or its value cast to false, then the table is not consider to be writable.  If its value casts to true, then it is considered writable and the save() method will actually do something.
* last_modified: Optional parent node.  If not present, we assume the last modified time is populated from the column 'last_modified'.  It has the following child nodes:
* *enabled: Optional scalar node.  If present and evaluates to false, it means the modified time is always taken to be NULL
* *col: Optional scalar node.  Specifies a "column" of the table to be used as the modified time.  Column should have type datetime. You are responsible for back-tics.
* *function: Optional scalar node.  Optional scalar node.  Optional scalar node.  Specifies a SQL function  whose result (of type datetime) will as the value for the modified time. 'col' takes precedence.

Global Options
^^^^^^^^^^^^^^
There are global options for specifying a the mapping between components and databases
 /modules/forms/storage_options/flat
This has the structure:

* table_prefix: Optional scalar node.  The value pre-pended to a form name to give the table name where the data is stored.  If not set it is 'hippo_', the prefix used for the caching of  form data to flat tables.  For example the person form would use the table 'hippo_person'.

Example
^^^^^^^
To read in the cached *hippo_person*  tables for the person forms from a cached table we would set:
 /modules/forms/forms/person/storage => 'flat'

Writing
^^^^^^^
Only fields which are columns are writable.  If the data specifying the id is not writable, then the form is not writable.

 **Warning:**  It is assumed that the columns associated to each field (besides the id) is either allowed to be null or has a default value, otherwise the column is not writable.  Basically we need to allow that for a new form, each column can be saved in an independent.

 **Warning:**  The id column cannot have 'form_prepended' set to true for the field to be writable

