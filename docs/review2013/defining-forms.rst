Defining Forms
==============

This page describes how to define and customize forms and fields in iHRIS by defining them in [[Configuration (Magic) Data|magic data]].    Before reading this article, please read the [[Forms and Form Classes|overview]] of forms and fields to become acquainted with the iHRIS data model. 


==Forms==
Forms are the basic way to group data.  A form $form, such as 'person', is stored under:
 /modules/forms/forms/$form
which contains the following children:
*class: Required.  The class which implements the logic, such as validation, for the form.  Example is 'iHRIS_Person'.
*displayName: Optional.  An end-user name for this form.  For example 'person' might have a display name 'Person'
*storage: Optional.  Defaults to 'entry.'  It is the [[Form Storage Mechanisms|storage mechanism]] that the form should use
*meta: Optional.  A node with lots of children where information about displaying this form are saved. The data here is used by the implementing form class
**description: A description of this form.  It is displayed, for example, when creating a form relationship
**child_forms: An list of any forms that are child forms of this form.
**child_form_data:  Optional. Meta data that are associated with child forms.  There is possibly a node for each of the child forms.  

The nodes in child forms data allow you to specify different groupings for child forms.  For example the form 'training_course' has as a child form 'scheduled_training_course.'   We may want to group the 'scheduled_training_courses' into ''open'' and ''closed.'' Then we can select to only display the open or closed scheduled training courses by specifying the limits as below.  We can also chose to specify the order that the scheduled training  courses are displayed in.  For example:
 'default'  => Array [
  'scheduled_training_course' => Array [
   'order' => 'start_date,end_date' 
  ] 
 ]
 'open' => Array [
  'scheduled_training_course' => Array [
   'limits' => Array [
     'operator' => 'FIELD_LIMIT'
     'field' => 'start_date'
     'style' => 'greaterthan_now'
   ]
   'order' => 'start_date,end_date'
  ] 
 ]
 'closed' => Array [
   'scheduled_training_course' => Array [
    'limits' => Array [
      'operator' => 'FIELD_LIMIT'
      'field' => 'start_date'
      'style' => 'lessthan_now'
    ]
    'order' => 'start_date,end_date'
  ] 
 ]
The limits are specified according to [[Limiting Forms|this]] structure.  The 'order' is a list of the fields to sort by.  In the above we sort first by 'start_date' and then by 'end_date.'  If we wanted to sort by a field in descending order we would prefix a -.

==Componentized Forms==
If you are setting up an aggregating instance of iHRIS Manage (or Qualify) some of your forms will be componentized.  This means that the data for each of these forms is being managed by distinct localities (e.g. regions or districts or even departments) and you wish to aggregate this de-centralized data.  Whether or not a form is localized is determined the [[Form Storage Mechanisms|form storage mechanism]] being used.  If a form is componentized, then any id's that reference that form are appended with an '@' and the name of the component.

==Form Classes==
A form class $formClass is defined under:
 /modules/forms/formClasses/$formClass

It has sub-nodes:
*fields: Optional.  Contains information about the fields provided by this class
*extends: Required.  Which class this form class extends.  This needs to be either I2CE_Form or a subclass of it.

===Dynamic Creation===
If there is no file ''$formClass.php'' then the class is created dynamically as:
 class $formClass extends $extendClass {}
where $extendClass is the value under the 'extends' node.

===Lists===
The form class I2CE_List is a special form which allows you to deal easily with lists of data.  Any mapped field should take values in a form whose implementing class is a subclass of I2CE_List.

I2CE_List has a subclass I2CE_SimpleList whose only field is 'name'.  Examples of simple lists are:
*gender
*marital_status
*language

===Magic Data for Lists===
A list is defined by its magic data in a form class, $listClass.  Under the magic data node:
 /modules/forms/formClasses/$listClass/meta
as follows:
*list: An optional parent node.  Each child node is a named "display" for this list  which can be referenced in .html templale files.   
**default: Optional parent node.  When displaying a field, if no display is specified, the data under the node "default" is used to determine the display.
***display_string:  The printf style display string used to display this form in a drop down or tree select. Defaults to "%s".  <p/>The printf substitutions is according to [http://www.php.net/manual/en/function.sprintf.php this].  Please note that if there is more than one field to be substituted, you should use references/arguments so that translators can handle this appropriately.   So instead of "%s %s" you would use "%1$s %2$s"
***display_args: The fields which are passed to display_string to be printed.  Defaults to having one child with key 0 and value "name" (although this field may not exist!)
****0:  Scalar node.  The name of a field in this form.
****1:  Scalar node.  The name of a field in this form.
****2:  Scalar node.  The name of a field in this form.
****...:  There should be the same number of children as there are referenced substitutions in display_string
***sort_fields:  Optional parent node. The ordering that should be applied when displaying this list.  Children are scalar nodes with keys integers and values the name of the field.  Defaults to having one child with key 0 and value "name" (although this field may not exist!)
**$display1: Optional parent node.  Structure is the same as the "default" above.
**$display2: Optional parent node.  Structure is the same as the "default" above.

==Fields==
Information on [[Form Fields]]

[[Category:Forms]][[Category:Review2013]]
