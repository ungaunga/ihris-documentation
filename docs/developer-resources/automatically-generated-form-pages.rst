Automatically Generated Form Pages
==================================

 **Note: This document is out of date and is scheduled for revision.** 

Starting with the 4.1.6 release of iHRIS you will now have the ability to generate pages to edit and view forms entirely in magic data, avoiding the need to create or edit .html files as well as .php files.

Below we present the types of pages made available and the magic data options need to configure them.  This magic data should live under /I2CE/page/$pageName  or /modules/$moduleName/page/$pageName.  



I2CE_PageFormAuto
^^^^^^^^^^^^^^^^^
This is the simplest page used to edit a single form which is not a child form of another form.  The magic data used to define this page is as follows:


* class: required scalar node with value 'I2CE_PageFormAuto/
* style: optional scalar node.  See [[Pages_and_Templates#Page_Styles | page styles]] for more information.  Recommended value is 'shell'.
* args: required parent node
* *primary_form: required scalar node.  The name of the form to edit
* *title: Required scalar node.  The page title.
* *auto_template:required parent node
* **disabled.  Optional scalar node.  If set and evaluates to true, then we do not use the auto generation to display this page.  Instead we would fall back to using .html template methods.
* **task: Optional scalar node.  A task the user must have in order to edit this form.
* **view_link:  Optional scalar node.  The link to view this form once the form has been successfully saved. If not set, it will default to 'view_$form.html?id='  where $form is as in primary_form.
* **display_order: optional scalar node.  It should be a comma separated list of field names and is used to specify the order in which the fields are displayed.  Example would be 'firstname,surname,nationality'
* **display_name: Optional scalar node.  Defaults to the display name of the form.  It is the text put in the black header row of the edit table.
* **title:  Optional scalar node.  If not set it uses the values of args/title.  This is main text displayed at the top of the page's content.
* ***fields:Optional parent node.  Keys of children are field names
* ****$field: optional parent node.
* *****enabled:  Optional scalar node.  Defaults to 1.  If set to 0, this field is not displayed.
* *****attributes: Optional parent node.  Keys are names of attributes that we want to set for displaying this node
* ******showhead: Optional scalar node.  Specifies the header to display for this form field.  Defaults to 'default'

An minimal example to create a page to edit the person form would look like:

.. code-block::

    array(
     'class'=>'I2CE_PageFormAuto',
     'style'=>'shell',
     'args'=>Array(
       'primary_form'=>'person',
       'auto_template'=>array(),
       'title'=>'Add/Edit Person'  
     )
    )
    



I2CE_PageFormAutoView
^^^^^^^^^^^^^^^^^^^^^
This is a page used to view a form and optionally any child forms.  The page will be compiled automatically from its configuration without requiring the creation of template files in the module. The magic data used to define this page is as follows:



* style: optional scalar node.  See [[Page and Templates#Page Styles | page styles] for more information. Recommended value is 'shell'
* class: required scalar node.  Value is 'I2CE_PageViewChildren'
* args
* *primary_form: required scalar node.  The name of the form to edit
* *title: Required scalar node.  The page title.
* *auto_template
* **task: optional scalar node.  if present it is a task assigned to view this form that the user needs to have
* **title: Optional scalar value node. Title/large text of the page displayed.  Detaults to "View <FORM DISPLAY NAME>"
* **form_display_name.  Optional scalar node.  Display name for the form.
* **fields: Optional parent node.  Child nodes have keys which are the fields names
* ***$fieldname: Optional Parent Node for the field $fieldname
* ****enabled:  Optional scalar node.  Defaults to 1/true, except in the case of i2ce_hidden or remap which defualts to 0/false.  If true, then the field is displayed on the page.  The default behaviour  can be overridren by setting 'default_disabled'
* ****attributes: Optional Parent Node.  Key's are the names of attributes which are processed by on the DOM Node created for the field here in the processDOM() method for the form field http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.2-dev/view/head:/modules/Forms/modules/Fields/lib/I2CE_FormField.php#L830   Note: these attributes are not centrally documented, but by example on various wiki pages.By default conatins the attributes @showhead="default" and @auto_link="1"
* ****is_method: Optional scalar node.  Defaults to false.  If true, the we try to process the display of this form field using an alternative method attached to the formfield object.
* **display_order: scalar value node. comma seperated list.
* **default_disabled.  Optional scalar node.  Defaults to 0/false.  Set to 1/true if you want to by default not display all fields
* **action_links:  optional parent node.  child nodes correspond to links that can be  performed on the form.  By default, these links will be displayed when  ajax loading a child form
* ***$action. Optional parent node fo an action
* ****formfield:  formfied used to append it's value to the base url.  Typically should  be "{$primary_form}+id" where $primary_form is as above.
* ****href: base url for the aciton
* ****text: scalar node used in the link display
* ****task: scalar node for the task required to see this link
* **edit_links:  optional parent node. cdhile nodes corespond to links used to navigate  away from the the form.  For example to a parent form.  By default,  these links will not be displayed when ajax loading a child form
* ***$action. Optional parent node fo an action
* ****formfield:   formfied used to append it's value to the base url.  Typically should   be "{$primary_form}+id" where $primary_form is as above.
* ****href: base url for the aciton
* ****text: scalar node used in the link display
* ****task: scalar node for the task required to see this link
* **child_forms: optional parent node.   keys for child nodes are the names of child forms
* ***$childform: the name of a child form.  optional parent node
* ****title: Optional scalar node.  Used as title to group all of these child forms under.  Defaults to display name of the child form.
* ****printf:   Required scalar node.  A printf string such as "%s %s" used to display  basic information on each child form of this type
* ****printf_args: Optional parent node.  Values are the fields whose display value are used to subsitute in printf above.
* ****where: optional parent node that describes the limits placed on the form.  Structure is the same as used in report relationships to add a where cluase
* ****limits: Optional node that describes any limits (start and max) on the child forms loaded
* ****task: scalar node for the task required to see this link
* ****link: Optional scalar node used to view the child form's data.  If present, will be loaded under ajax.
* ****link_filter: MooTools CSS filter used to select the ajax content loaded
* ****action_links: optional parent node.  Named dctions associated to the group of these child forms
* *****$action. Optional parent node fo an action
* ******formfield: formfied used to append it's value to the base url.  Typically should be "{$primary_form}+id" where $primary_form is as above.
* ******href: base url for the aciton
* ******text: scalar node used in the link display
* ******task: scalar node for the task required to see this link


I2CE_PageFormParent
^^^^^^^^^^^^^^^^^^^
This is a page used to edit the child form of a parent form.  The magic data used to define this page is as follows:


* class: required scalar node.  Value is 'I2CE_PageFormParent'
* style: optional scalar node.  See [[Page and Templates#Page Styles | page styles] for more information. Recommended value is 'shell'
* args: required parent node
* *title: required scalar node.  The page title
* *primary_form: required scalar node.  The child form that we are editing
* *view_link:optional scalar node. The link to view the form.  Defaults to "view_$form?id="
* *parent_form: required scalar node.  THe parent form of the child form that we are editing
* *parent_view_link:optional scalar node. The link to view the parent form.  Defaults to "view_$parentForm?id=".  This is the page we are directed to on a succesful save
* *auto_template:optional parent node.  If not set, we fall back to .html files for displaying and editing.
* **disabled. Optional scalar node. If set and evaluates to true, then we do not use the auto generation to display this page. Instead we would fall back to using .html template methods.
* **task: Optional scalar node. A task the user must have in order to edit this form.
* **display_order: optional scalar node. It should be a comma separated list of field names and is used to specify the order in which the fields are displayed. Example would be 'firstname,surname,nationality'
* **display_name: Optional scalar node. Defaults to the display name of the form. It is the text put in the black header row of the edit table.
* **title: Optional scalar node. If not set it uses the values of args/title. This is main text displayed at the top of the page's content.
* **fields:Optional parent node. Keys of children are field names
* ***$field: optional parent node.
* ****enabled: Optional scalar node. Defaults to 1. If set to 0, this field is not displayed.
* *****attributes: Optional parent node. Keys are names of attributes that we want to set for displaying this node
* ******showhead: Optional scalar node. Specifies the header to display for this form field. Defaults to 'default'


I2CE_PageViewChildren
^^^^^^^^^^^^^^^^^^^^^
This is a page used to view a form any optionally any child forms.  The magic data used to define this page is as follows:


* class: required scalar node.  Value is 'I2CE_PageViewChildren'
* style: optional scalar node.  See [[Page and Templates#Page Styles | page styles] for more information. Recommended value is 'shell'
* args: required parent node
* *title: required scalar node.  The page title
* *primary_form: required scalar node.  The child form that we are editing
* *auto_template:optional parent node.  If not set, we fall back to .html files for displaying and editing.
* **disabled. Optional scalar node. If set and evaluates to true, then we do not use the auto generation to display this page. Instead we would fall back to using .html template methods.
* **append_node. optional scalar node.  Defaults to 'siteContent'  where we should append our auto generated template.
* **task: Optional scalar node. A task the user must have in order to edit this form.
* **display_order: optional scalar node. It should be a comma separated list of field names and is used to specify the order in which the fields are displayed. Example would be 'firstname,surname,nationality'
* **display_name: Optional scalar node. Defaults to the display name of the form. It is the text put in the black header row of the edit table.
* **title: Optional scalar node. If not set it uses the values of args/title. This is main text displayed at the top of the page's content.
* **fields:Optional parent node. Keys of children are field names
* ***$field: optional parent node.
* ****enabled: Optional scalar node. Defaults to 1. If set to 0, this field is not displayed.
* *****attributes: Optional parent node. Keys are names of attributes that we want to set for displaying this node
* ******showhead: Optional scalar node. Specifies the header to display for this form field. Defaults to 'default'
* **children:optional parent node.
* ***disabled. Optional scalar node. If set and evaluates to true, then we do not use the auto generation to display this page. Instead we would fall back to using .html template methods.
* ***fields: TO BE CONTINUED



[[Category:Developer Resources]]
