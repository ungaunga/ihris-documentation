Swiss Magic Data Editor
=======================

Most of the configuration of the iHRIS software is handled by defining [[Configuration (Magic) Data|magic data]].   To handle structured editing and display of this configuration/magic data and avoid corruption of data,  a set of PHP classes, the Swiss Magic data editors, was developed.   These are used, for example, in defining form relationships and reports.

The Swiss Magic editors hierarchically edit and view the configuration data.  This article describes the structure of the Swiss Magic PHP classes.

Features
^^^^^^^^

* Provides different ways of traversing the configuration magic data hierarchy via different factories
* Lots of AJAX goodness built in to display sub-menus within the current menu
* Used in the "Form Relationship" builder and the "Custom Reporting" tool
* Used in the "Configure Modules" tool
* Processing and Displaying of data is already localized.  You only need to call "renameInputs()" to rename any of your html form elements.

Examples
^^^^^^^^

* [[Swiss Magic Data -- Form Relationships|Form Relationships]]
* Reports
* Report Views

The Swiss Node
^^^^^^^^^^^^^^
A **swiss node**  is a subclass of I2CE_Swiss.  You can think of the I2Ce_Swiss classes as defining a GUI widget for interacting with magic data. Associated to a swiss node is:

* a magic data node
A swiss node has the following functions:

* display values saved at its magic data node
* create a user interface to edit the values at its magic data node
* process an associative array of values to update the magic data node
* determine the *types*  of its child swiss nodes.  A node of type $type is a node of class I2CE_Swiss_$type.

Methods To Implement
~~~~~~~~~~~~~~~~~~~~
When creating a new Swiss type you only need to implement these methods:

* displayValues() The method used to display the data associated with swiss node.  Can be defined for different actions.  There are two main actions:
* *view: The action to display a read-only view of the magic data at that node.
* *edit: The action to display an edit view of the magic data data at that node.
* processValues() The method used to process an associated array of values and update the magic data.  Needs to be defined
* getChildType()  Gets the type of the swiss child with the given name.

Useful Methods
~~~~~~~~~~~~~~
The following methods should be used 

* getStorage()  Gets the magic data node associate to the swiss node.
* getChild() Gets the child swiss node with the given name.
* renameInputs()  Needs to be called to rename all html input/select/textarea form elements of the given DOMNode are associated to that swiss node.
* addAjaxLink() Adds a link to child swiss node.  If the browser is AJAX happy, it will do so in a AJAX manner.  Otherwise it is simply a link
* get/set/hasField()  Convenience methods to access the named (scalar) magic data child node.

The Swiss Factories
^^^^^^^^^^^^^^^^^^^
The Swiss Factory handles:

* provides the appropriate magic data node associated to a swiss node
* creates the appropriate child swiss nodes
* traverses the swiss nodes when given a path
* pre-process GET/POST variables and passes them to the appropriate swiss node.
* handles errors in updating values based on GET/POST values.
* implements the Iterator and Count Interface

The Swiss Factory is determined by:

* the root magic data node
* the root swiss node class

There are two factories available Swiss Magic and Swiss Config.  These have corresponding I2CE_Page sub-classes to access the web interface.

Swiss Magic Factory
^^^^^^^^^^^^^^^^^^^
This is is the swiss factory do create dynamic content in I2CE.  This includes:

* Custom Form Relationships
* Custom Reports
* Custom Report Views

Parent and Children
~~~~~~~~~~~~~~~~~~~
Any (non-scalar) magic data node can serve as the root swiss node.  

The children of a swiss node are in one to one correspondence with the child nodes of the corresponding magic data node.  The names of the child swiss nodes are the same as the names of the child magic data nodes.

Page Access
~~~~~~~~~~~
This factory can be accessed in the web interface as in instance of the I2CE_Page_SwissMagic class.  This is done for:

* Form Relationships
* Custom Reports
* Custom Report Views

Swiss Config Factory
^^^^^^^^^^^^^^^^^^^^

This is the Swiss Factory designed for the configure modules tool.

Parent And Children
~~~~~~~~~~~~~~~~~~~
In this factory the child swiss nodes of a given swiss class are defined by a [[Configuration (Magic) Data|module configuration XML#Defining Magic Data in Configuration Files]] file.   The root parent swiss node is the main *<configurationGroup>*  in the configuration XML file.  

The child swiss nodes associated to a given *<configurationGroup>*  are exactly the child *<configuration>* s and *<configurationGroup>* s on that node.  The names of the child swiss nodes are the names of the child *<configuration>*  and *<configurationGroup>*  nodes.

The magic data node associated to a swiss node is the exactly the magic data node associated to the given *<configuration>*  or *<configurationGroup>*  node as defined by the **path**  and **name**  attributes.

Page Access
~~~~~~~~~~~
For the "Configure Modules" page, each module instantiates the a swiss factory by the an instance of the I2CE_Page_SwissConfig class.  

