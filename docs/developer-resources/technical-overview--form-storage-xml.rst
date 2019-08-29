Technical Overview: Form Storage -- XML
=======================================

This is a form storage mechanism designed to read data from an xml list file.  This form storage mechanism is present in version >= 4.0.6.

It assumes that each distinct instance of a forms can be read from a distinct node.

This is a read-only form storage mechanism.  

 **This form storage mechanism requires PHP 5.3 or greater** 

Form Storage Options
^^^^^^^^^^^^^^^^^^^^

The options specifying a XML storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/XML
It has the following structure:

* file:  Required scalar node.  The xml file that the data should be read from.  This can either be an absolutely given file path,  a relative file path, or the URL of a  stream handled by php.  If it is a relative file path, then it uses the  [[File Search Paths | file search]] category named below. The file can also be a path to a scalar node in magic data as indicated by 'mdn://path/in/magic/data'
* search: Required scalar node. The search category.
* basequery: Required scalar node.  The xpath query to get the base node of the data
* dataquery:  Required scalar node. The xpath query to get the data nodes.
* id: Optional parent node.  The data defining how to associate an id <'''namespace''':OBS_VALUE/>.
* *query: Optional scalar node.  A xpath query, relative to the data node, for which the text content is this id's base value.  Needs to return exactly one DOMNode.
* *attribute: Optional scalar node.  The name of the attribute which contains the id.  If not set the id is the numeric document order of OBS_VALUE nodes starting at 1.
* *eval:  Optional scalar node.  If set it is a code php code which modifies the id, stored in the $id variable.  For example '$id = strtoupper($id);'
* *form_prepended: Optional scalar node. Defaults to true. If true, it means the form name (with a |) has been prepended to the id and we need to strip it out to get the id.  If ieval is also set, and this is true, the form is stripped before passing to the eval.
* parent: optional parent node.  The data defining how to associate a parent id DOM Node
* *query: Optional scalar node.  A xpath query, relative to the data node, for which the text content is this field's base value.  Needs to return exactly one DOMNode.
* *attribute: Optional scalar node.  The name of the attribute which contains the parent.  If neither 'query' or this is set, there is not parent data. 'query' takes precendence.
* *eval:  Optional scalar node.  If set it is a code php code which modifies the id, stored in the $val variable.  For example '$val = strtoupper($val);'
* fields: Optional parent node.  Specifies how the data of the your form is associate to a row of your table.  Each child of this node is the name of a field $field of your form.
* *$field:  Optional parent node with the following child nodes.
* **query: Optional scalar node.  A xpath query, relative to the data node, for which the text content is this field's base value.  Needs to return exactly one DOMNode.
* **attribute: Optional scalar node.  The name of the attribute which contains the parent.  If neither 'query' nor this is set, there is not data.  'query' takes precendence
* **eval: Optional scalar node.  If set it is a code php code which modifies the id, stored in the $val variable.  For example '$val = strtoupper($val);'

