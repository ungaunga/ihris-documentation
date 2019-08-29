Technical Overview: Form Storage -- SDMX CrossSectional
=======================================================

This is a form storage mechanism designed to read data from an SDMX-HD code list file.  This form storage mechanism is present in version >= 4.0.6.

This is a read-only form storage mechanism.  



 **This form storage mechanism requires PHP 5.3 or greater** 

Form Storage Options
^^^^^^^^^^^^^^^^^^^^

The options specifying a SDMX Cross Sectional storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/SDMX_CrossSectional
It has the following structure:



* file:  Required scalar node.  The SDMX file that the data should be read from.  This can either be an absolutely given file path,  a relative file path, or the URL of a  stream handled by php.  If it is a relative file path, then it uses the SDMXHD [[File Search Paths | file search]] category.  The file can also be a path to a scalar node in magic data as indicated by 'mdn://path/in/magic/data'
* namespace: Optional scalar node. defaults to 'ns'.
* parent: optional parent node.  The data defining how to associate a parent id DOM Node.
* *attribute: Required scalar node.  The name of the attribute which contains the parent.  If neither 'query' or this is set, there is not parent data. 'query' takes precendence.
* *eval:  Optional scalar node.  If set it is a code php code which modifies the id, stored in the $val variable.  For example '$val = strtoupper($val);'
* *map_data: Optional parent node.  .It is used to map the given field via a SDMX-HD Code List that is in the system
* **list: Required scalar node.  The list that we want this field to take values in
* **codelist: Required scalar node: The name of the SDMX-HD code list which this attribute takes values in, in other words the value we wish to map from.
* **mapping_form: Optional scalar node. The name of the form which contains the mapping data between the SDMX-HD Code List and the list we wish to map to.  If the module **Lists-LinkTo-List**  is enabled and the value is not set then it defaults to *list_linkto_list_XXXX*   where XXXX is the form storage mechanism of the list.  If set, the form should subclass I2CE_ListLink_List.



* fields: Optional parent node.  Specifies how the data of the your form is associate to a row of your table.  Each child of this node is the name of a field $field of your form.
* *$field:  Optional parent node with the following child nodes.
* **attribute: Required scalar node.  The name of the attribute which contains the parent.  If neither 'query' nor this is set, there is not data.  'query' takes precendence
* **eval: Optional scalar node.  If set it is a code php code which modifies the id, stored in the $val variable.  For example '$val = strtoupper($val);'
* **map_data: Optional parent node.  .It is used to map the given field via a SDMX-HD Code List that is in the system
* ***list: Required scalar node.  The list that we want this field to take values in
* ***codelist: Required scalar node: The name of the SDMX-HD code list which this attribute takes values in, in other words the value we wish to map from.
* ***mapping_form: Optional scalar node. The name of the form which contains the mapping data between the SDMX-HD Code List and the list we wish to map to.  If the module **Lists-LinkTo-List**  is enabled and the value is not set then it defaults to *list_linkto_list_XXXX*   where XXXX is the form storage mechanism of the list.  If set, the form should subclass I2CE_ListLink_List.

[[Category:Developer Resources]]
