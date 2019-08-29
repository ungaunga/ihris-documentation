Technical Overview: Form Storage -- CSV
=======================================

This is a form storage mechanism designed to read data from a CSV file.  It is primarily designed to import data.  This form storage mechanism is present in version >= 4.0.3.

This is a read-only form storage mechansim.  By default it will read in the CSV dump of a *hippo_XXX*  as exported by phpmyadmin according to the following options:

* Export: CSV
* Fields Terminated By: ,
* Fields Enclosed By: "
* Fields Escaped By: \
* Lines Terminated By: AUTO
* Replace NULL By:
* Put fields names in the first row: Checked
* Compression: None
Here is a [[Media:csv_options.png | screen shot]]

Form Storage Options
^^^^^^^^^^^^^^^^^^^^

The options specifying a CSV storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/CSV
It has the following structure:

* file:  The CSV file that the data should be read from.  This can either be an absolutely given file path, a relative file path, or the URL of a  stream handled by php.  If it is a relative file path, then it uses the CSV  [[File Search Paths | file search]] category. The file can also be a path to a scalar node in magic data as indicated by 'mdn://path/in/magic/data' .
* delimiter: The delimited used to split a line (one character only).  Defaults to '''',''''
* enclosure: the field enclosure character (one character only). Defaults to ''''"''''
* has_header:  Whether or not the first row is a header row. Defaults to true.
* use_header: Defaults to true.  If true and has_header is set to true,  then the columns are referenced by the column header.  This header names are case insensitive and ignore any white space padding.  If evaluates to false, then the columns are assumed to be numerically indexed.
* id: Optional parent node.  The data defining how to associate an id per line of this file.
* *index: If set, and *use_header*  or *has_header*  is false, it is the numeric index of the column that this data is saved in.
* *header: Applies if *use_header*  and *has_header*  are true.   If set it is the header name of index of the column that this data is saved in.  By default it is "id"
* *form_prepended: Optional scalar node. Defaults to true. If true, it means the form name has been prepended to the id.  Otherwise, it assume that the column is just the id.
* parent: optional parent node.  The data defining how to associate a parent id per line of this file.
* *enabled: Optional scalar node.  If present and evaluates to false, it means getParent() should return the trivial parent id, '0'.
* *index: If set, and *use_header*  or *has_header*  is false, it is the numeric index of the column that this data is saved in.
* *header: Applies if *use_header*  and *has_header*  are true.   If set it is the header name of index of the column that this data is saved in.  By default it is "parent"
* fields: Optional parent node.  Specifies how the data of the your form is associate to a row of your table.  Each child of this node is the name of a field $field of your form.  By default, all fields of a form are populated, and are all assumed to come from the column with that field name  "$form+$field"
* *$field:  Optional parent node with the following child nodes.
* **enabled: Optional scalar node.  If present and evaluates to false, it means we should not populate this field.
* **index: If set, and *use_header*  or *has_header*  is false, it is the numeric index of the column that this data is saved in.
* **header: Applies if *use_header*  and *has_header*  are true.   If set it is the header name of index of the column that this data is saved in.  By default it is "$field"

Global Options
^^^^^^^^^^^^^^
There are global options for CSV form storage. They are specified at:
 /modules/forms/storage_options/CSV
This has the structure:

* closeCSV: defaults to false.  If true, we close the CSV file between access.  Otherwise, we allow PHP to handle closing the file resource at the end of the script's call.

