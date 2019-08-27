Module Structure
================================================

This tutorial describes the iHRIS Module Structure.  An iHRIS module is a collection of various types of "code" by the features that they provide to the system.  These modules can be part of the core I2CE system and handle things like user 
authentication or database access, or they can provide new functionality to iHRIS, such as leave management.



What is a Module?
^^^^^^^^^^^^^^^^^
The iHRIS Suite is based on the Intrahealth Informatics Core Engine (I2CE) which use a module structure to encapsulate and maintain "code" into manageable pieces organized by the functionality provided.  By "code" we mean the entire collection of php, html, javascript, xml, image files, css, flash, etc that provide the functionality of a web-based application.


A module is versioned to keep track of the changes to functionality and API that a module has.

=Why Modules?=


* The main reason to use a module system is to increase code manageability.  The various components of the iHRIS Suite (Qualify, Manage, and Plan) are used in a variety of settings each requiring their own customizations.



* Each of the iHRIS Suite's components (Qualify, Manage, Plan) share some common functionality and the module system ensures proper code re-use.



* The module system lets many customizations to be encapsulated without having to change the underlying code base.   This allow a local developer to make their changes without worrying about about having to redo those changes anytime the core system is updated.



* As modules are organized by the functionality that they provide to the system, a developer can quickly find the relevant code to change by looking at the relevant modules.



* Customizations to the software encapsulated in a module can be easily shared among developers.

=The I2CE Module=
The is the "top"-most module.  Every module implicitly has this a requirement.  It is the core module which provides the minimal functionality including magic data, file search, the templating system, and the module factory.   It has no requirements.

 *I2CE* provides many optional sub-modules.  For example:


* Admin -- Provides a module management system.
* Background Process -- Provides a platform independent means to launch and monitor background processes
* Custom Reports -- Provides the Custom Reporting functionality
* Flash Charts -- provides a  php interface to the maani flash charting system
* Forms -- provides the basic form and field structure used by our software
* MooTools -- provides a php interface to the MooTools javascript library
* Tasks and Roles -- provides a task based management system for user roles

=The Site Module=
The "bottom"-most module is the **Site Module.**  This module is the one that is loaded by the **index.php** file and tells the system which modules we are used by your system.  It is the appropriate place to perform basic customizations to the system, for example changing the image displayed on the login page or to display your organizations name.  See for example [[Customizing iHRIS Manage]]

=Module Configuration File=
A module exists by defining its configuration files.  There is one top-level node <I2CEConfiguration> under which there are two possible nodes:


* The [[#metadata|<metadata>]] tag is required.
* The [[#Configuration (Magic) Data|<configurationGroup>]] tag is optional.
The <I2CEConfiguration> tag has a required attribute **name** whose values should be a unique short name to describe this module such as *I2CE*, *ihris-manage* or *mercury_javascript_popup.*  
The DTD which describes the format of the configuration file is located in *I2CE/lib/I2CE_Configuration.DTD*.  As an example:
 <?xml version="1.0"?>  
 <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
 <I2CEConfiguration name='mercury_javascript_popup'>     
   <metadata>
     <span style='color:tomato'>Some stuff defined [[#metadata|below]] </span>
   </metadata>
   <configurationGroup name='mercury_javascript_popup'>
     <span style='color:tomato'>Some stuff defined [[#Configuration (Magic) Data|below]] </span>
   </configurationGroup>
 </I2CEConfiguration>


metadata
^^^^^^^^
The DTD has for the <metadata> tag allows the following nodes:
 <nowiki><!ELEMENT metadata (</nowiki>[[#displayName|displayName]],[[#className|className]]?,[[#category|category]]?,[[#description|description]]?,[[#creator|creator]]?,[[#email|email]]?,[[#link|link]]?,
   [[#version|version]],([[#enable|enable]]|[[#requirement|requirement]]|[[#conflict|conflict]]|[[#path|path]])*,[[#priority|priority]]?<nowiki>)></nowiki>
For the most part, the orders of these tags matter due to limitations in the structure of DTDs.  The exceptions is that the <enabled>, <requirement>, <conflict> and <path> tags can be listed in any order amongst themselves.

displayName
~~~~~~~~~~~
This tag is requireed it is human readable name of this module which is displayed, for example, in the *Configure Modules* pa
 Example: <displayName>Popup Box</displayName>

className
~~~~~~~~~
The tag is optional and it associates a class for the module.  See [[#The Module Class]] for specific information about the module's class
 Example: <className>I2CE_Module_JavascriptPopup</className>

category
~~~~~~~~
This is an optional tag that is used to group similar modules together by category in the *Configure Modules* page.
 Example: <category>Javascript Library</category>

description
~~~~~~~~~~~
This is an optional tag which gives a description of this module which is displayed in the *Configure Modules* page.
 Example: <description>Provides a javascript popup box</description>

creator
~~~~~~~
This is an optional tag which shows the creator in the *Configure Modules* page.
 Example: <creator>Freddy Mercury</creator>

link
~~~~
This is an optional tag which gives a URL for the module in the '''Configure Modules'' page.
 Example: <link>http://en.wikipedia.org/wiki/Freddie_Mercury</link>

version
~~~~~~~
This is a required tag which you can use to version your module.
 Example: <version>1.0.0</version>

requirement
~~~~~~~~~~~
This is an optional tag, of which you can have as many as you want.  Each tag needs to have the attribute **name** whose the value is the name of a module required by this module.  This tag can have up to four possible sub-tags:


* atLeast
* atMost
* lessThan
* greaterThan
each of which need to have the attribute **version** with a value of a version of the module. As an example:
 <requirement name='I2CE'>
  <atLeast version='3.1'/>
  <lessThan version='3.2'/>
 </requirement>
says that our module requires that I2CE have version at least 3.1 and less than version 3.2.

In order for a module to be loaded, it must successfully meet all of its requirements.


conflict
~~~~~~~~
This is an optional tag of which you can have as many as you wish.  This is opposite of the [[#requirement|<requirement>]] tag and lists all the modules that this module conflicts with.  As an example:
 <conflict name='plant_javascript_popup'>
 </conflict>
 <conflict name='ringo_javascript_popup'>
   <lessThan version=3.2/>
 </conflict>
Says that our module conflicts's with all versions of `Robert Plant <http://en.wikipedia.org/wiki/Robert_Plant>`_'s javascript popup, but only conflicts with [http://en.wikipedia.org/wiki/Ringo_starr|Ringo Starr]'s popup for versions less that 3.2.

A module will fail to load if it conflicts with any other modules that are already loaded.


enable
~~~~~~
This tag is optional of which you can have as many as you wish.  This tag requires the attribute **name** with the value the short name of a module. This tag is weaker than the [[#requirement|<requirement>]] tag in that it will try to enable the named module, but it will not cause the cause this module to fail to load if it can't.  It also differs from the <requirement> and <conflict> tags as there is no version information (under the subtags atLeast,atMost, lessThan, greaterThan). As an example:
 <enable name='alex_patterson_javascript_paginator'/>
Says that if the `Alex Patterson <http://en.wikipedia.org/wiki/Alex_Patterson>`_'s javascript paginator module is able to loaded, then load it.  Otherwise don't worry about it.


path
~~~~
This is an optional tag of which there can be as many as you wish. Each <path> tag requires the attribute **name** and can have as many sub-tags **<value>** as you wish.   The <path> tag enables a module to specify directories to be added to the file search utility group by category.  The categories are specified by the name attribute and some commonly used names are:


* templates These are the directories to search for html template files
* images These are the directories to search for image files
* css These are the directories to search for CSS files
* scripts These are the directories to search for javascript files
* classes These are the directories to search for files containing php classes.  The convention here is that MyClass is located in the file MyClass.php
* modules These are the directories to look for (sub-)modules of the current module.
For more information about the paths allowed, see [[File Search Paths]]


priority
~~~~~~~~
This tag is optional.  If not set, the priority of a module is 50.
 Example: <priority>50</priority>
Here are some standard priorities:


* I2CE 0
* sub-modules of I2CE 50
* ihris-common 100
* sub-modules of ihris-common 150
* ihris-manage, ihris-qualify, ihris-plan 200
* sub-modules ihris-manage, ihris-qualify, ihris-plan 250
* a site module 400


Configuration (Magic) Data
^^^^^^^^^^^^^^^^^^^^^^^^^^
The <configurationGroup> node is optional.  If it is present it has to have the attribute **name** which has the same value as the attribute **name** in the containing <I2CEConfiguration> tag.  

All magic data is relative to the path defined by the this configurationGroup.  There are three options:


* The attribute path is not present.  In the following example, the magic data is stored under */modules/mercury_javascript_path.*
 Example:
  <configurationGroup name='mercury_javascript_popup'>
    <span style='color:red'>SOME STUFF GOES HERE</span>
 </configurationGroup>


* The attribute path is present.  In the following example, the magic data is stored under */some/other/place.*
 Example:
  <configurationGroup name='mercury_javascript_popup' path='/some/other/place'>
    <span style='color:red'>SOME STUFF GOES HERE</span>
  </configurationGroup> 


* The module is 'I2CE'.  The magic data is stored relative to */I2CE*

This <configurationGroup> node does double duty.  It provides the configuration data that is stored into magic data.  It also provides, via the *Admin* module,  a treed menu system to edit the magic data set by this system.  This allows for dynamic customizations of your site.

See [[Configuration (Magic) Data]] for more detailed information.


The Module Class
^^^^^^^^^^^^^^^^
The module class is in intended to provide php functionality to the class.  The module class is named by the optional <className> tag in the <metadata> section of the module configuration file.   It needs to exist in the *classes* paths of the module and it needs to subclass **I2CE_Module** which is found in *i2ce/lib/I2CE_Module.php.*

There are three basic types of functionality it provides.  The first are methods to be called when a method is enabled, upgraded or disabled.  The second is to provide hooks into the system.  The third is to provide fuzzy methods.

Enabling/Disabling a Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~
There are several methods used to initialize, enable, disable  and upgrade a module which are called by the module factory.  All of these methods expect that the module returns true to indicate success.


* When a module is enabled the method **action_enable()** is called.
* Before a module is enabled for the first time **action_initialize()** is called.  <br/> This is the appropriate place to do things like ensure that any tables in the database the module expects to have are created.  <br/> For example, the module 'I2CE' has its own class 'I2CE_Module_Core' which does the following:
* *Checks that the user database table is there, if not it creates it.
* *Makes sure that there is an administrative user for the system.  If not, it creates it.
* *Checks that the config table for magic data is present, if not it creates it.
* When a module is disabled the method **action_disabled()** is called.
* When the version in the configuration file changes **upgrade($old_vers,$new_vers)** is called.


Hooked Methods
~~~~~~~~~~~~~~
There are certain specific places in the code that may naturally lend themselves to be hooked in for greater functionality. 
A module may hook into the sytem at various points.  To add a hook at some point you add either the
line:
          I2CE_ModuleFactory::callHooks('some_hook_name',$some_argument);
or the line:
          I2CE_ModuleFactory::callHooks('some_hook_name');
I2CE_ModuleFactory will take care of calling all modules that register hooks for that point,with either the one or no arguments as appropriate.  All hooked methods are called (in order of priority).  The result of each hooked methods appended to an array which is then returned back from the callHooks() method.

A module registers the methods to call via its getHooks() method which returns an array with keys the hook name and value the method name in the module's class.


Fuzzy Methods
~~~~~~~~~~~~~
A fuzzy method is a method that a module provides to some other PHP class extended I2CE_Fuzzy via the __call() method. There are three reasons to use fuzzy methods:


* PHP cannot do multiple-inheritance for classes which makes it difficult to combine functionality of two classes into one.  One can always do an interface, but then one has to rewrite a lot of code.
* The second is to provide modular functionality that can be turned on and off.
* The functionality of a class may need to change depending if the class is called from a webserver or from the command line.
The later reason is why they are *fuzzy:*  the methods may or not be present in the class depending on which modules you have turned on.
The fuzzy methods that a module provides are defined by arrays returned from the methods getMethods() and getCLIMethods().  The results of these methods are processed every time the module is enabled or a change is detected to the module's class source file.  When a module is disabled, the fuzzy methods it provides are removed from the class.

For example the module''FormWorm'''s getMethod() returns:
 array('I2CE_Page->addFormWorm'=>'addFormWorm',
       'I2CE_Template->addFormWorm'=>'addFormWorm'
       )
when the module FormWorm is turned on, this provides the methods addFormWorm() to both the class I2CE_Page and I2CE_Template as well as any child classes of these.  The general form for this array is:
   CLASS->CLASSMETHOD => MODULEMETHOD
where CLASSMETHOD is a fuzzy method provided to the class CLASS.  This fuzzy method is implemented by calling MODULEMETHOD on the instance of the module's class.  The first argument to MODULEMETHOD will be the class that the fuzzy method was called and the remaining arguments are the arguments that CLASSMETHOD was called with.

For example, if $page is an instanceof I2CE_Page then the call:
  $page->addFormWorm($arg1,$arg2) 
results that the module factory will takes its instance, $module, of the I2CE_Module_FormWorm and call:
  $module->addFormWorm($page, $arg1,$arg2);

Fuzzy method will only have access to the public methods and variables of the calling class (I2CE_Page in this example).  Incidentally, this encourages the development of a good API for the calling class.

Like the other components of a module (such as template files), fuzzy methods are prioritized and only the one of the lowest priority is called.  You can see the documentation for the classes I2CE_Module and I2CE_ModuleFactory for more information.
[[Category:Modules]][[Category:Review2013]]
