Creating and Using Modules
==========================

Warning.  Some of this information is out of date as it was written for version 2.1
= Overview =
There is now a plugin system for I2CE.  This will allow addding of various components
to the I2CE/ihris-XXX systems.  

All modules live in the subdirectory 'modules' (in ihris-common,ihris-manage,ihris-qualify or in a site directory).  
        
If you want to add a module, you create subdirectory  under 'modules' for that module.
There needs to be one class in that directory which:

* a) is a subclass of I2CE_Module
* b) contains some module metadata (which looks much like the metadata for a wordpress plugin)
There is a configuration page that allows you to disable/enable/purge modules.  (Purging is deleting
any tables/data from the database that the module created.  It is up to the module author to write
the method which is a part of the I2CE_PurgingModule interface). 
        
Suppose that we have a module living under the sub-directory 'Example' of the directory 'modules'.
When a module is enabled the following is performed:

* a) if the module has never been initialized, it calls the action_initialize method of the module
* b) it adds 'Example' directory to the above class search path
* c) it adds 'Example/images'  to the image search path
* d) it adds 'Example/scripts' to the scripts search path
* e) it adds 'Example/css' to the scripts search path
* f) it adds 'Example/templates' to the template search path
The search paths are added so we can really localize all of the module to one directory.  All of the
search paths are added with a order of (plus or minus) 1000.  We also add all the paths with an
additional '/local/' which take priority over the b)-f) above so that we can test/change things locally
without having to worry about chaning the main code/data of the module.
When a module is disabled, it removes all of the above search paths

A module may hook into the sytem at various points.  To add a hook at some point you add either the
line:
          I2CE_ModuleFactory::instance()->callModuleHooks('some_hook_name',$some_argument);
or the line:
          I2CE_ModuleFactory::instance()->callModuleHooks('some_hook_name');
I2CE_ModuleFactory will take care of calling all modules that register hooks for that point,with either 
the one or no arguments as appropriate.  The method callModuleHooks() returns
an array containing the return values of the hooked methods for each of the hooked methods.

A module registers the methods to call via its get_hooks() method.
A module may set a priority for each hooked method.  Then I2CE_ModuleFactory processes these
hooks in order of increasing priority. The default priority is 10000.
                
        
A module may make pages available to the system.  The pages are defined in an I2CE_Module via
the get_pages() method.   The serving of pages is handled by I2CE_ModulePageControler which
(see the Demo page module.php in the corresponding ihris-manage commit).

If a module needs to perform some action on an enable or disable, it can use the action_enable()
and action_disable() methods.  These methods should return true if the action succeeded.  You 
should returns false, to indicate that there was an error, in which case the module will not
change its enabled status.

= Hooks =
The following hooks are enabled so far

* <b>process_error</b> has arguemnets array('message'=> string: the message,'type'=>int :error type,'template'=>I2CE_Template : the template (if it has been created)).  It is called in the I2CE raiseError() method and us used to process any errors raised. If false is received by any of the hooked methods, it prevents a re-direction on an error of type E_USER_ERROR.
* <b>pre_page_display</b> has an argument of type I2CE_Page : the page.  It is called in I2CE_Page's display() method before the I2CE_Template's display() method is called.
* <b>post_page_display</b> has an argument of type I2CE_Page : the page.  It is called in I2CE_Page's display() method after the I2CE_Template's display() method is called.
* <b>pre_process_forms</b> has an argument of array('template'=>I2CE_Template: the template, 'user'=>I2CE_User : the user).  It is called in I2CE_Template's display() methods just before the &lt;span type='form'&gt; methods are processed.
* <b>post_process_forms</b> has an argument of array('template'=>I2CE_Template: the template, 'user'=>I2CE_User : the user).  It is called in I2CE_Template's display() methods just after the &lt;span type='form'&gt; methods are processed.
* <b>post_template_process_display</b> has an argument  array('template'=>I2CE_Template: the template, 'user'=>I2CE_User : the user).  It is called in I2CE_Template's display() methods just before the DOM is dumped to out as HTML.
* <b>post_configure</b> takes no arguments.   It is called at the end of all the configuration files loading.

