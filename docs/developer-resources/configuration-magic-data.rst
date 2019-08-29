Configuration (Magic) Data
==========================

Magic Data is a mechanism intended to handle dynamic site-level configuration data.  It is the basis of much of the functionality provided by the IntraHealth Informatics Core Engine (I2CE), including how pages are served and how custom reports are made.  

<span style='color:red'>Warning:</span>The API for Magic Data has been fairly significantly updated from version 3.1 to version 4.0.  Although this article applies to the version 4.0 API, much of it is relevant to version 3.1.  See some of the [[#Changes from 3.1|Changes]]
=What is Magic Data?=

Magic Data is a rooted tree structure with benefits.  If you wish you may think of it as the analogue of the Windows Registry for your web application.  You may also think of it as a nested array.

There are two parts two parts to magic data.  The magic data node class, defined in *I2CE/lib/I2CE_MagicDataNode*  and the storage mechanisms for magic data.  You may use magic data without using a storage mechanism, in which case the magic data saved does on persist across sessions.  By default uses the following storage mechanisms for Magic Data:

* Database:  The data is stored into a table in the database.  In I2CE, this is set to be the *config*  table.
* APC: The data is stored in to a memory cache provided by  `apc <http://pecl.php.net/package/APC>`_  which persists across apaches session.

As APC is faster, reads are first done from APC. If the data is not found there, it is read from the database.  Data is written first to the database and then to APC.

=Scalar and Non-Scalar=
There are two main types of nodes scalar and a parent node  

A scalar node does not have any children. It does have a value which is a possibly empty string.  A scalar node can be marked as being localized.  In which case the value returned depends on the localization preferences for the user.

A parent node can have as many children as it wants.  Each child of a parent node must have distinct [[#Names and Paths|names]].  It does not have a value.  It is not localizable.

=Names and Paths=
With the exception of the root node, every magic data node has a name.  For a name, any numeric value is allowed.  Any non-empty string is valid as long as it does not start with '=' does not contain a '/' and is not '.' or '..'.  However, it is best if you limit the strings to contain the following characters only:
 _-+.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

Absolute Paths
^^^^^^^^^^^^^^
Magic Data nodes can be referenced by their path which is a concatenation of their names by '/.'

The root node has path '/'.

If the root node has a child with name 'some', it is referenced by the path '/some'

If some is a parent node with a child with name 'thing', then that child is referenced by the path '/some/thing'

Relative Paths
^^^^^^^^^^^^^^
Paths can also be relative.  In the example above, if you were at the node '/some' then could reference the other nodes by:

* './' references '/some'
* '../' references '/'
* './thing' references the node '/some/thing'

=Defining Magic Data in Configuration Files=
A convenient way to get magic data loaded into the system is to do so through a [[Module Structure#Module Configuration File|module configuration file]] by specifying a <configurationGroup> node after the <metadata> node.  This section serves double duty.  It allows you to specify magic data as well as to provide a way to edit the data for the module.

The <configurationGroup> node is optional. If it is present it has to have the attribute name which has the same value as the module name, whhich is the name attribute in the containing <I2CEConfiguration> tag.

All magic data is relative to the path defined by the this configurationGroup. There are three options:

* The attribute path is not present. In the following example, the magic data is stored under /modules/mercury_javascript_path.
 Example:
  <configurationGroup name='mercury_javascript_popup'>
    <span style='color:red'>SOME STUFF GOES HERE</span>
 </configurationGroup>

* The attribute path is present. In the following example, the magic data is stored under /some/other/place.
 Example:
 <configurationGroup name='mercury_javascript_popup' path='/some/other/place'>
   <span style='color:red'>SOME STUFF GOES HERE</span>
 </configurationGroup> 

* The module is 'I2CE'. The magic data is stored relative to /I2CE

In the remainder of this section we will describe <span style='color:red'>WHAT STUFF GOES THERE</span> which are [[#<configurationGroup>|<configurationGroup>]] and [[#<configuration>|<configurations>]] tags.

<configurationGroup>
^^^^^^^^^^^^^^^^^^^^
A <configurationGroup> can several subtags in this order::

* An optional <displayName>. A name displayed in the module configuration for this grouping of data
* An optional <description>. A description of the functionality of the grouping.
* An optional [[#<version>|<version>]] tag.
* Any number (including zero) of [[#<status>|<status>]] tags.
* Any number (including zero) of <configurationGroup> or [[#<configuration>|<configuration>]] tags.

<configuration>
^^^^^^^^^^^^^^^
A <configuration> can several subtags in this order::

* An optional <displayName>. A name displayed in the module configuration for this grouping of data
* An optional <description>. A description of the functionality of the grouping.
* An optional [[#<version>|<version>]] tag.
* Any number (including zero) of [[#<value>|<value>]] tags.

Attributes
^^^^^^^^^^
There are several attributes that both a [[#<configuration>|<configuration>]] and a [[#<configurationGroup>|<configurationGroup>]] may have:

* name: This is a required attribute.  Every child <configuration> or <configurationGruop> of a <configurationGroup> should have a distinct name.  If the path attribute is not set, it is also says that this configuration node should apply to the magic data node with the given name and which is a child magic data node of the parent configurationGroup node.
* path: This is optional. It may be an absolute or relative path in magic data and describes the magic data at which this value should be stored at.   If it is a relative path, it is relative to the magic data path of its parent node.
* locale: This is optional.  If this is set, it means that the values under this node should be consider to be localizable.
* config: This is optional.  If set, it sets the I2CE_Swiss object used to display the data in the configure modules menu.
A <configuration> may also have the following attributes:

* type: Defaults to 'string' and describes the type of data that is being set by the <value> tags of this node.
* values: Defaults to 'single' and describes if the data being set by this node should be an array of values or a single value based on what is stored in the <values> node

<value>
^^^^^^^
The <value> tag is a sub-tag of a [[#<configuration>|<configuration>]] tag.  It contains the value(s) which are stored in the magic data and depends on the *type*  and *values*  [[#Attributes|attributes]].

Some common types and values are:

* type='string' values='single':  The magic data node is a scalar type with value the contents of the single <value> tag.
* type='string' values='many':  The magic data node is a parent type.  The magic data node has a child node of scalar type for each <value> tag.
* type='delimited': The magic data node is a parent type.  The value tags are expected to be of the form <value>'key':'value'</value> in which case a child magic data node is created of scalar type with name 'key' and value 'value'
* type='boolean':  The values in the <value> tag are interpreted as booleans:  F,f,False,false,0, etc. are stored in magic data is 0.  Otherwise the value stored is 1.

<version>
^^^^^^^^^
The same magic data can be accessed by multiple modules configuration files.  Suppose that a module moduleA requires a module moduleB and that they both set /some/data to have values valA and valB respectively.  Suppose that both modules have version 1.0.
 <span style='color:tomato'>Excerpt from moduleA's configuration file</span>
 <configurationGroup name='some' path='/some'>
  <configuration name='data' >
    <value>valA</value>
  </configuration>
  <configuration name='data2'> 
    <value>valA2</value>
  </configuration>
 </configurationGroup>
 <span style='color:tomato'>Excerpt from moduleB's configuration file</span>
 <configurationGroup name='some' path='/some'>
  <configuration name='data'>
    <value>valB</value>
  </configuration>
  <configuration name='data2'> 
    <value>valB2</value>
  </configuration>
 </configurationGroup>

On site intialization, since moduleA requires moduleB, the value is first set to valB is first set by moduleB.  It is then overwritten to be the value valA by moduleA.   Similarly, after initialization, the value of '/some/data2' is 'valA2'

Suppose that version of moduleB is increased to version 1.1 but there are no other changes to the configuration file.  This will cause the configuration file to be reprocessed.  The *configurator*  will remember that has already processed all the data up to and including version 1.0.  Thus it will not re-read the or overwrite what is already stored in magic data.

Suppose now that moduleB  wants to change the value it stores at /some/data to be newValB, as well as create a new value at /some/other_data  We would need to increase the version number of the module to 1.2 and add a <version> tag so that the configurator knows that in upgrading the module to version 1.2, we should reread the configuration data for anything greater than the previously loaded version of 3.1:
 <configurationGroup name='some' path='/some'>
  <configuration name='data'>
    <version>1.2</version>
    <value>newValB</value>
  </configuration>
  <configuration name='other_data'>
    <version>1.2</version>
    <value>The new stuff</value>
  </configuration>
  <configuration name='data2'> 
    <value>valB2</value>
  </configuration>
 </configurationGroup>
Now the value at /some/data will be updated to be 'newValB' and we will add in the value 'The new stuff' at '/some/other_data.'  The value at '/some/data2' remains unchanged and is 'valA2.'

<status>
^^^^^^^^
A status tag consists of key value pairs:
 <status>key:value</status>
Although you can use anything for the key (as long as it does not have a ':' in it!), the keys which have meaning are:

* version: Functions just like [[#<version>|<version>]]
* overwrite: The value can be either true of false.  Defaults to false.  If true the magic data will be overwritten even if the version has not.
* merge:  The value can be either true of false.  Defaults to false. If true, the values read in are merged into the existing values by *array_merge()*
* mergerecursive:  The value can be either true of false.  Defaults to false. If true, the values read in are merged into the existing by *I2CE_Util::merge_recursive().*
* uniquemerge:  The value can be either true of false.  Defaults to false except in the case where a <configuration> node has type='string' and values='many.'  If true, the values read in are merged into the existing values by *I2CE_Util::merge_recursive()*  and only the unique values are kept by *I2CE_Util::array_unique().*
* visible: The value can be either true of false.  Defaults to true.  If true, this node is displayed in the module configuration menu.
* advanced:  The value can be either true of false.  Defaults to false.  If true, this is considered an an advanced option for the module configuration menu
* required: The value can be either true of false.  Defaults to true.  It says the the resulting values at the <configuration> node must be set
* showIndex: The value can be either true of false.  Defaults to true.  In which case we show the index in the module configuration menu

The values of the status keys are inherited as you go down a node.

=Using Magic Data in PHP=
Each node of magic data is an instance of the class **I2CE_MagicDataNode** .  The "public variables" of a node are its child nodes which is done by making use of the *__get()*  method.  I2CE_MagicDataNode implements the RecusriveIterator, ArrayAccess, SeekableIterator, and Countable Interfaces.

I2CE has a root magic data instance which can be retrieved by:
 $config=I2CE::getConfig();

Basic Access
^^^^^^^^^^^^
Suppose $data is a magic data node, with a children named 'my_list' and 'amount' which are parent type and scalar type respectively.  Suppose that the child node 'amount' has value 10.  Suppose that there is no child named 'bad.'  The children can be accessed in many ways:
<center>
{| class='wikitable' border="1" cellspacing="5" cellpadding="2"
|-
! Access Method
! Result
! Notes
|-
| $data->my_list
| I2CE_MagicDataNode
| This is the 'my_list' node
|-
| $data->amount
| 10
|
|-
| $data->bad
| I2CE_MagicDataNode
| The node did not exist, so it was created.  <br/>It has an indeterminate type at the moment.
|-
| $data['my_list']
| I2CE_MagicDataNode
| the 'my_list' node
|-
| $data['amount']
| 10 
| the value of the 'amount' node
|-
| $data['bad']
| I2CE_MagicDataNode
| We created the non-existent 'bad' node and returned it
|-
|}
</center>

Refined Access
^^^^^^^^^^^^^^
To get more refined access to magic data nodes you may use the **traverse(** $path,$create=false,$return_value=true''')''' function:
<center>
{| class='wikitable' border="1" cellspacing="5" cellpadding="2"
| $data->traverse('my_list',false,false)
| I2CE_MagicDataNode
| This is the 'my_list' node
|-
| $data->traverse('bad',false,false)
| null
| The second argument says not to create a node that doesn't exist
|-
| $data->traverse('amount',false,false)
| I2CE_MagicDataNode
| The is the 'amount' node
|-
| $data->traverse('my_list',false,true)
| I2CE_MagicDataNode
| This is the 'my_list' node
|-
| $data->traverse('amount',false,true)
| 10
| The value of the 'amount' node 
|-
| $data->traverse('bad',false,true)
| null
| The second argument says not to create a node that doesn't exist 
|-
| $data->traverse('my_list',true,true)
| I2CE_MagicDataNode
| This is the 'my_list' node
|-
| $data->traverse('amount',true,true)
| 10
| The value of the 'amount' node 
|-
| $data->traverse('bad',true,true)
| I2CE_MagicDataNode
| We created the non-existent 'bad' node and returned it
|}
</center>

If a node has scalar type, you can get its value by *getValue()* .  If you call *getAsArray()*  on it, it will also return its value.

If a node has parent or indeterminate type, calling *getValue()*  returns the node itself.  If you call *getAsArray()*  on it it will return a nested array.  The keys at each depth are the child node's names.   The values are either an array or a sting, depending on if that child is scalar or not.

Checking Existence and Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^
You can use the following method to see if a Magic Data node, exists and what its type is:

* '''pathExists('''$path''')'''
* '''is_scalar('''$path=null''')'''
* '''is_parent('''$path=null''')'''
* '''is_indeterminate('''$path=null''')'''
* '''is_root('''$path=null''')'''
Here, we the path defaults to *null* , the value that method is called on the node itself (this would be the same as calling it on $path='./').

You may do something like:
 function set_node_to_scalar($node) {
   if (!$node instanceof I2CE_MagicDataNode) {
     echo "Why are you giving me garbage data?\n";
     return false;
   } 
   if ($node->is_scalar()) {
     echo "This node is already a scalar.  It has a value " . $node->getValue(). "\nI don't need to do anything.\n";
     return true; 
   } else {
     echo "This node is a parent node.  Although it may or may not have children, I can't set it to be scalar.\n";
     return false;
   } else{
     //$node->is_indeterminate() will return true
     echo "This node is indeterminate. Setting it to be scalar\n";
     $node->set_scalar();
     return true;
   }
 }
Two other useful functions are

* **getAsArray(** $path=null''')''' which return the node and all of its children (recursively) as an array
* **setIfIsSet(** &$var,$path,$as_array=false''')''' which will check to see if $path exists.  If it does not, it returns false.  If it does, it returns true and calls either getValue() or getAsArray() on the node referred to by the path.

Child Names and Iterators
^^^^^^^^^^^^^^^^^^^^^^^^^
To get the names of the child nodes of a node, we use the **getKeys()**  method.
Suppose that we magic data set up as follows:
<center>
{| class='wikitable' border="1" cellspacing="5" cellpadding="2"
|-
! Path
! Type
! Value
|-
| /
| parent
| <span style='color:red'>NONE</span>
|-
| /color
| scalar
| red
|-
| /modules
| parent
| <span style='color:red'>NONE</span>
|-
| /modules/modA
| parent
| <span style='color:red'>NONE</span>
|-
| /modules/modB
| parent
| <span style='color:red'>NONE</span>
|-
| /modules/modA/favorite_clay_animation
| scalar
| Mr. Bill
|}
</center>
You may also something similar as:
 echo "I like the color " . $config->color . "\n";
 $keys = $config->getKeys();
 foreach ($keys as $key) {
   if ($config->is_parent($key)) {
     echo "The node named $key under at " . $config->getPath(false) . " is a parent node.  It has children " . implode(',', $config->$key->getKeys()) . ".\n";
   } else if ($config->is_scalar($key)) {
    echo "The node named $key under at " . $config->getPath(false) . " is a scalar with value " . $config->$key ".\n";
   }
 }
which would result in:
 I like the color red.
 The node named modules under / is a parent node.  It has children modA,modB.
 The node named color under / is a scalar node with value red.

As a magic data node is an iterator, we can do things like:
 foreach ($config as $key=>$node) {
   if ($node instanceof I2CE_MagicDataNode) {
    echo "The node named $key under at " . $config->getPath(false) . " is a parent node.  It has children " . implode(',', $node->getKeys()) . ".\n";
   } else {
    echo "The node named $key under at " . $config->getPath(false) . " is a scalar with value " . $node .".\n";
   }
 }
which would result in:
 The node named modules under / is a parent node.  It has children modA,modB.
 The node named color under / is a scalar node with value red.
or:
 $modules = $config->modules;
 foreach ($modules as $module=>$data) {
   if ($data->is_scalar('favorite_clay_animation')) {
      echo "The module $module thinks " . $data->favorite_clay_animation . " is a super star!\n";
   }
 }
would result in:
  The module modA things Mr. Bill is a super star!

=Changes from 3.1=

* Removed the __ from method calls.
* Relaxed the rules for the names of Magic Data nodes.
* Implemented the various interfaces
* Added in support for localization of values

