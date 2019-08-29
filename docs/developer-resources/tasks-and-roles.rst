Tasks and Roles
===============

iHRIS uses a task- and role-based security mechanism to limit access to various parts of the system.  A user is assigned a role, and a role is a collection of tasks that the role can perform.

This article describes how roles and tasks are defined in Magic Data and used by the iHRIS system. 

=Roles=
A role is a collection of [[#Tasks|tasks]] that can be assigned to a user's account.


* Role names are defined in [[Configuration (Magic) Data|magic data path]] /I2CE/formsData/forms/role/
* The roles are defined as entries of the role form and we need to add the last_modified value
* A role $role has a $display_name defined at /I2CE/formsData/forms/role/$role/fields/name/$display_name

For example, this XML says that the role hr_staff is displayed as 'HR Staff' and it is assignable.:

 <configurationGroup name="roles" path="//I2CE/formsData/forms/role/">
   <configurationGroup path="hr_staff">
     <configuration name="last_modified">
       <value>2013-01-15 1:23:45</value>
     </configuration>
   <configurationGroup name="fields">
     <configuration name="name">
       <value>HR Staff</value>
     </configuration>
     <configuration name="assignable">
       <value>1</value>
     </configuration>
   </configurationGroup>
 </configurationGroup>

=Tasks=
A task can be both a collection of sub-tasks that this task has and description of some action that can be checked for permission. Task information is stored in magic data under /I2CE/tasks/.  To create a task you create a scalar type child node of /I2CE/tasks/task_description.  That name node of the node is the name used to reference the task.  The value of the node is the description of the task displayed in the Task and Role Management page.  For example, the magic data node /I2CE/tasks/task_description may look something like:


* custom_report_admin => Allows administration of the Custom Reporting System
* custom_reports_can_access => Allows minimal access to the Custom Reporting System
* custom_reports_delete => Allows deletion of data about custom reports
* custom_reports_can_access_relationships => Allows access to the Custom Report Relationships
You can define the sub tasks of a task $task by specifying /I2CE/tasks/task_trickle_down_task.  For example, the magic data node /I2CE/tasks/task_trickle_down/custom_reports_admin may look like:


* 0 => custom_reports_can_access
* 1 => custom_reports_delete_reports
which says that the 'custom_report_admin' task has all the tasks and rights defined by 'custom_reports_can_access' and 'custom_reports_delete_reports.'

The tasks that are assigned to a role $role are the values of the children under /I2CE/tasks/role_trickle_down/$role

A user with the role 'admin' has all tasks.

=Uses of Tasks and Roles=
The tasks and roles are used in several places:


* The main [[Pages and Templates#Page Logic|I2CE_Page]] class checks for basic permission for the page.
* Several pages perform checks for specific roles and tasks in their action() method.
* Just before displaying the HTML the I2CE_Template, class verifies that all tasks, roles and permissions are satisfied on each node.

=Task and Role Administration=
For deployment across many computers, tasks and roles should be set up in an appropriate module [[Module Structure#Module Configuration File|configuration file]].

For setting tasks and roles dynamically, the module 'tasks-roles' provides the page named 'roles' and the page named 'tasks' that allows creating new roles and tasks as well as defining the permission inheritance.

To enable the task-roles module go to Configure Modules -> Pages -> Sub-Modules -> Tasks and Roles.

=Permissions and the Permission Parser=
The permission parser allows logical expressions to combine severals types permissions, such as *task* , *roles* , into a *permission string* .

We can assign tasks, roles and permissions to DOM nodes by:


* Setting the attribute *role* .   <br/>If the values is X, this results in the permission string *role(X)*  which is passed to the permission parser
* Setting the attribute *task* . <br/>If the values is X, this results in the permission string *task(X)*  which is passed to the permission parser
* Setting the attribute *permission.*
If the node fails any of the role, task or permission checks it will remove the node


Permission Types: task and role
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The task and role type permissions are formed by surrounding a role name with role() or a task name with task().  For example, you can create the following *permission string* :
 (task(can_edit_database_list_facility_type) & task(can_edit_database_list_fav_color) || role(admin)
By default, tasks and roles are 'OR'ed together so the following are all the same:


* task(can_edit_database_list_facility_type) or task(can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type) | task(can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type)  task(can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type,can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type|can_edit_database_list_fav_color)


Permission Type: module
^^^^^^^^^^^^^^^^^^^^^^^
Any public function of a [[Module Structure#The Module Class|module class]] can be called by the permission parser.  For example, suppose that the module 'my_module' has a method 'my_method()' then we can use as the permission string with [[#Arguments|arguments]]:
 module('my_module','my_method', [arg1], ... , [argN])
which would results in the call:
 $module->my_method($arg1,..,$argN)
where $module is the instance of the module class for the module 'my_module.'


Permission Type: form
^^^^^^^^^^^^^^^^^^^^^
The 'forms' module adds in the form type.  The permission string with [[#Arguments|arguments]]:
 form('form_name', 'form_method', [arg1] , .., [argN])
results in the call:
 $form->form_method($arg1,..,$argN)
where $form is the result of getting the form by the name of 'form_name' via  [[Pages and Templates#Template Data|template data]] for node (if there was any) the permission string was assigned to.


Arguments
^^^^^^^^^
A permission type (such as role, task, form or module) in a permission string behaves essentially like a function.  Suppose that we have the general shape for a piece of a permission string:
 type([arg1],[arg2],...,[argN])
Then this results in the method call:
 $permissionParsrer->hasPermission_$type($node,$args)
where $node is the DOMNode the permission string was called on and $args is the array($arg1,..$argN).  The permission parser turns [argM] into $argM according to the following rules:


* if [argM] starts with a $ then it refers to template data and the following rules apply:
* *The string has the form $abcd. The value of $argM becomes the template display data with name 'abcd.'
* *The string has the form ${WXYZ}abcd.  The value of $argM becomes the template data with category 'WXYZ' and with name 'abcd.'
* <NODE> becomes the instance of DOMNode (if any) that the permission string was called on
* <TEMPLATE> becomes the instance of I2CE_Template (if any) that the permission parser was called on
* <USER> becomes the instance of I2CE_User that is this session
* if [argM] starts with a single quote ' then it is a string until the next non-escaped ' is found
* if [argM] starts with a double quote " then is is a string until the next non-escaped " is found. <br/>In addition the following substitution rules apply:
* *any substring starting with $ and consisting of alpha-numeric characters, - or _ is interpreted as template display data to be substituted<br> For example "my name is $name" becomes "my name is Joe" if the template data named 'name' and with type DISPLAY is "Joe"
* *any substring starting with {$ is read until an enclosing } is found.  The string between the ${ and } is the name of DISPLAY template data which is then substituted.
* *To prevent the above, { and $ may be escaped with a \
* any other string of alpha-numeric characters (and a few permitted punctuation marks) is interpreted as a string

Arguments may be separated by a comma a space or a |.


New Types
^^^^^^^^^
A module can add in a [[Module Structure#Fuzzy Methods|fuzzy method]] of the form *hasPermision_$type*  to the *I2CE_PermissionParser*  class to enable a new permission type.  For example the 'forms' module does this by adding in a new permission type 'form.'

[[Category:Developer Resources]]
