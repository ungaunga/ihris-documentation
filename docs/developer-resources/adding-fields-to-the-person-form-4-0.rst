Adding Fields to the Person Form - 4.0
======================================

This tutorial applies to version 4.0 of iHRIS Manage.  To see this tutorial for different versions of the software see the following:{{otherversions|Adding Fields to the Person Form}}

In this tutorial, we will look at adding a new fields to the person form to iHRIS Manage. We will add two fields, one called "Favorite Color" which will be a drop-down list of values, and one will be "Favorite Animal" which will be a free-text field.  There are many ways to skin my favorite animal, a cat.  Likewise, there are many ways to add a field to a form.  In order to better maintain the code and the customizations we are making, we will do so by creating a sub-module **Demo_ManagePerson**  of the Demo site-module which contain the all of our changes.  To look at a similar customization, look at [ `CSSC <http://bazaar.launchpad.net/~ihris%2Bcssc/ihris-manage/4.0-central/files>`_ ]'s customizations and in particular under *modules/Person.* 

 **<span style='color:red'>Warning:</span>**   In this tutorial we will be modifying the Demo site of *ihris-manage*  directly.  This is not the recommended method for doing this in a production environment.  


Pre-Requisites
^^^^^^^^^^^^^^
It is recommended to read over the following articles and to refer to them as you read through this tutorial:


* [[Module Structure]]
* [[Configuration (Magic) Data ]]
* [[Forms and Form Classes]]


Directories
^^^^^^^^^^^
You may wish to look at [[Customizing iHRIS Manage]] for an overview of some of the directories that are relevant for customizations. We will make our customizations to the iHRIS Manage Demo site. On unix you might be working under:
;<Base Dir>:/var/lib/iHRIS
;<Site Dir>:/var/lib/iHRIS/4.0/ihris-manages/sites/Demo
If you have installed Windows iHRIS Manage you will be working under the directories:
;<Base Dir>:C:\Program Files\ihris-suite
;<Site Dir>:C:\Program Files\ihris-suite\sites\ihris-manage


Creating a New Module
^^^^^^^^^^^^^^^^^^^^^
The looking at:


* **<SITE DIR>** /iHRIS-Manage-Demo.xml for Linux
* **<SITE DIR>** /iHRIS-Manage-Demo.xml for Windows
we see that we can put sub-modules into the subdirectory *modules*  of the site directory, which already exists.  So lets do (on unix):
 mkdir **<SITE DIR>** /modules/DemoPerson
which will contains our **DemoPerson**  sub-module.  Then save to the file:
 **<SITE DIR>** /modules/DemoPerson/DemoPerson.xml
the following contents:
 <?xml version="1.0"?>       
 <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
 <I2CEConfiguration name='DemoPerson'>      
  <metadata>
    <displayName>Demo Person</displayName>   
    <category>Form</category>
    <description>Sets up the Demo Person form with extra fields for favorite animals and favorite color</description>
    <version>4.0.0</version> 
    <requirement name='Person'>
      <atLeast version='4.0'/>
      <lessThan version='4.1'/>
    </requirement>
    <path name='templates'>
       <value>./templates</value>
    </path>
    <priority>300</priority>  <!-- greater priority than ihris manage=200, but less than the site == 400 -->
  </metadata>
 </I2CEConfiguration>
This is (almost) the minimal amount of things we need to do create a new module.  Right now, there is no functionality, but we have said that the module *DemoPerson*  requires the module *Person,*  which is incidentally a sub-module of ihris-common.  We also set the priority for the module, so that we know that the template files we will create will take precedence over anything in the modules ihris-manage or ihris-common.


Forms and Form Classes and Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There are really two parts to defining a "form", a form and a form class.  The forms are referenced by their *shortname,*  for example *person.*  The second is referenced by the name of a PHP class, for example, *iHRIS_Person* .  

All of the magic data for forms lives under */modules/forms.*   The magic data to define forms is under */modules/forms/forms*  and for form classes under */modules/forms/formClasses.* 
For example, the configuration file  **<BASE DIR>** /ihris-common/modules/Person/Person.xml defines the *Person*  module.  Here you will see two nodes:
 <configrationGroup name='person'>
 </configurationGroup>
and
 <configrationGroup name='iHRIS_Person'>
 </configurationGroup>
The later defines some of the fields associated with the class iHRIS_Person, and the former tells us the class that the *person*  form uses is *iHRIS_Person.* 

Now if we look at the configuration file **<BASE DIR>** /ihris-manage/iHRIS-Manage-Configuration.xml we will see two things: that ihris-manage requires the module *Person* ,  and we will also see a similar *<configurationGroup name='person'>*  node.  This time the *person*  form now uses the class *iHRIS_ManagePerson.*   Since *ihris-manage*  requires *Person* , the class associated to the form person is loaded from iHRIS-Manage-Configuration.xml and not from Person.xml

If we look further in the this file, we will see the *<configurationGroup name='iHRIS_ManagePerson'>*  node which defines the *iHRIS_ManagePerson*  class.   Here you will notice two things:


* iHRIS_ManagePerson extends iHRIS_Person, so it has all of the same fields of iHRIS_Person
* iHRIS_ManagePerson adds in the field named *password*  with type 'STRING_PASS' but that this field is not saved to the database


Adding the Fields to Magic Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We will add the two fields **fav_color**  and **fav_animal**  to the DemoPerson class.  Since we wish for *fav_color*  to be a drop-down list, we will also need to create a form called *fav_color*  which will contain the colors we wish.  To setup these forms and fields, we are going to have to add in configuration (magic) data.  Add to:
 **<SITE DIR>** /modules/DemoPerson/DemoPerson.xml
the following just after the **</metadata>**  tag:
 <configurationGroup name='DemoPerson' path='/'>
   <span style='color:olive'><status>overwrite:true</status></span>
   <configurationGroup name='forms' path='/modules/forms/forms'>
     <configurationGroup name='fav_color'>
        <span style='color:tomato'><nowiki><!-- define the 'fav_color' form --></nowiki></span>
        <configuration name='class' values='single'>  
          <value>I2CE_SimpleList</value>
          <span style='color:tomato'><nowiki><!-- fav_color uses the 'I2CE_SimpleList' form defined in i2ce/modules/Forms/modules/Lists--></nowiki></span>
        </configuration>
        <configuration name='display' values='single'>         
          <value>Favorite Color</value>  
          <span style='color:tomato'><nowiki><!-- the name of this form that is displayed to a user is 'Favorite Color'--></nowiki></span>
        </configuration>
     </configurationGroup>
     <configurationGroup name='person'>
       <span style='color:tomato'><nowiki><!-- the form 'person' is defined in ihris-common/modules/Person/Person.xml. --></nowiki></span>
       <configuration name='class'> 
          <value>DemoPerson</value>
          <span style='color:tomato'><nowiki><!-- Here we are changing the form class it uses to be 'DemoPerson' which is defined below --></nowiki></span>
       </configuration>
     </configurationGroup>
   </configurationGroup>
   <configurationGroup name='formClasses' path='/modules/forms/formClasses'>
     <configurationGroup name='DemoPerson'>
        <span style='color:tomato'><nowiki><!-- We are defining the DemoPerson class --></nowiki></span>
        <configuration name='extends'>
           <value>iHRIS_ManagePerson</value>
            <span style='color:tomato'><nowiki><!-- The DemoPerson class extends the 'iHRIS_ManagePerson' class defined in <BASE DIR>/iHRIS-Manage-Configuration.xml --></nowiki></span>
        </configuration>
        <configurationGroup name='fields'>
           <span style='color:tomato'><nowiki>< !-- Under here we add in the new fields that DemoPerson has --></nowiki></span>
           <configurationGroup name='fav_animal'>
              <span style='color:tomato'><nowiki><!-- The data definining the 'fav_animal' field of DemoPerson --></nowiki></span>
             <configuration name='formfield'>
               <value>STRING_LINE</value>
               <span style='color:tomato'><nowiki><!-- Set the field to have type 'STRING_LINE' which is a single line of text e.g. an <input type='text'> in a form--></nowiki></span>
             <configuration>
             <configuration name='headers' type='delimited' values='many'> 
               <value>default:Favorite Animal</value> 
               <span style='color:tomato'><nowiki><!-- Set the default header for this field to be 'Favorite Animal'--></nowiki></span>
             </configuration>
           </configurationGroup>
           <configurationGroup name='fav_color'>
             <span style='color:tomato'><nowiki><!-- The data definining the 'fav_color' field of DemoPerson --></nowiki></span>
             <configuration name='formfield'>
               <value>MAP</value>
               <span style='color:tomato'><nowiki><!-- Set the field to have type MAP. By default, this field will be one of the ids of the form fav_color--></nowiki></span>
             <configuration>
             <configuration name='headers' type='delimited' values='many'> 
               <value>default:Favorite Color</value> 
               <span style='color:tomato'><nowiki><!-- Set the default header for this field to be 'Favorite Color'--></nowiki></span>
             </configuration>       
          </configurationGroup>
        </configurationGroup>
     </configurationGroup>
   </configurationGroup>
 </configurationGroup>
The <span style='color:tomato'>tomato</span> colored text are comments which you may leave out if you wish.

The <span style='color:olive'>olive</span> colored text can be removed before release, but it is useful for development purposes.  It ensures that any changes that you make to the configuration file will be updated.


Customizing the Template Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the previous step, we enabled the two fields to be saved to the database.   We now need to edit the user interface to show the fields where appropriate.  There are three areas we need to add these fields:


* [[#Displaying the Favorites|Displaying]] a person's record shows their favorite animal and color
* [[#Editing the Favorites|Editing]] a person's record lets you update favorite animal and color
* [[#Add to the Database Lists|Add]] a place in the *Administer Database*  page to and in the allowed colors


Displaying the Favorites
~~~~~~~~~~~~~~~~~~~~~~~~
The page titled *View Person*  and referenced in the URL as **view**  is first provided in the *Person*  sub-module of *ihris-common.*   Here, looking at **<BASE DIR>** /ihris-common/modules/Person/Person.xml we see that the page *view*  loads the default template file **view.html**  which can be found in **<BASE DIR>** /ihris-common/modules/Person/templates/view.html.

The *ihris-manage*  module overides the *view.html*  by providing it in **<BASE DIR>** /templates/view.html

Since the *view.html*  file is not specific to the DemoPerson module, it is not appropriate to put our modified version in the DemoPerson sub-moudule. Instead we will put in the templates directory of the Demo site module. Here is the (unix) command:
 cp **<BASE DIR>** /ihris-manage/templates/view.html **<SITE DIR>** /templates/view.html

To display the favorite animal and color of a person after their nationality, open up the newly created **<SITE DIR>** /templates/view.html.  Find the line:
 <nowiki><span type="form" name="person:nationality" showhead="default" class="even"></span></nowiki>
and add the following to lines just after it:
 <nowiki><span type="form" name="person:fav_color" showhead="default" ></span></nowiki>
 <nowiki><span type="form" name="person:fav_animal" showhead="default" class="even"></span></nowiki>


Editing the Favorites
~~~~~~~~~~~~~~~~~~~~~
In the *View Person,*  the first *Update This Information*  link lets us changes the person's basic information such as name and nationality.  We will add the fields to change their favorite color and animal to this page.  Clicking on the link and looking at the URL, we see that this page is named **person.**  

We start by looking at the *Person*  sub-module of *ihris-common*  to find correct template file to edit.  Looking at **<BASE DIR>** /ihris-common/modules/Person/Person.xml, we see that *person*  page is loads the default html template file *form_person.html.*   This file is found in **<BASE DIR>** /ihris-common/modules/Person/templates/form_person.html.  It is not overidden by *ihris-manage* . 

Since this template file is specific to a person and does not involve any other forms, we will put this in our *DemoPerson*  module.  We will create a templates sub-directory and copy this file over to this directory.  Here are the (unix) commands:
  mkdir **<SITE DIR>** /modules/DemoPerson/templates
  cp **<BASE DIR>** /ihris-common/modules/Person/tempaltes/form_person.html **<SITE DIR>** /modules/DemoPerson/templates/form_person.html

Now we open the newly created **<SITE DIR>** /modules/DemoPerson/templates/form_person.html and find the following line:
 <nowiki><span type="form" name="othername" showhead="default"></span></nowiki>
and add the following:
 <nowiki><span type="form" name="fav_color" showhead="default"></span></nowiki>
 <nowiki><span type="form" name="fav_animal" showhead="default"></span></nowiki>
just after it.


Add to the Database Lists
~~~~~~~~~~~~~~~~~~~~~~~~~
The lists stored in the database are managed though the page titled *Administer Database*  and referenced by **lists** .  We need to add a link to administer the *Favorite Color*  list.  

This basic functionality of the *list*  page is provided by *I2CE*  by the *Lists*  sub-module of the *Forms*  sub-module.  Here the *lists*  page is handled by the class in **<BASE DIR>** /I2CE/modules/Forms/modules/Lists/lib/I2CE_PageFormLists, and we we see that a template file **lists.html**  is loaded.  The **lists.html**  is a template file which contains all of the database lists that we wish to administer.  (Technically, we should have a file *<BASE DIR>* /I2CE/modules/Forms/modules/Lists/templates/lists.html but we forgot to add it.)

The *lists*  pages is extended in *ihris-common*  through the class at **<BASE DIR>** /ihris-common/lib/iHRIS_PageFormLists. We also notice there is a template file **<BASE DIR>** /ihris-common/templates/lists.html that has all the lists provided by *ihris-common* .

The *ihris-manage*  module overrides the *lists.html*  provided by *ihris-common*  by providing its own at **<BASE DIR>** /ihris-manage/tempalte/lists.html.  You will see that it has all the lists provided by *ihris-common*  as well the new lists provided by *ihris-manage.*   This is the template file we will modify for our site to add it the *Favorite Color*  list.  

Since the *lists.html*  file is not specific to the *DemoPerson*  module, it is not appropriate to put our modified version in the *DemoPerson*  sub-moudule.  Instead we will put in the templates directory of the Demo site module.  Here is the (unix) command:
 cp **<BASE DIR>** /ihris-manage/templates/lists.html **<SITE DIR>** /templates/lists.html
Now open the file **<SITE DIR>** /templates/lists.html and add the following line:
 <nowiki><li task='can_edit_database_list_fav_color' ><a  href="lists?type=fav_color">Favorite Color</a></li></nowiki>
in the <nowiki><ul></nowiki> block under **Employee Lists.** 

You will notice, that we have a *task*  attribute in the <nowiki><li></nowiki> tag.  A user with the role *HR Manager*  or *Administrator*  can edit any database list.  However, for purposes of an example, we will add this task which we can assign to a user with the *Training Manager*  role.  This we do in the [[#Setting the Edit Database List Favorite Color Task (Optional)| next section]]

Creating Edit Favorite Color Template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We need to create a template called 'view_list_fav_color.html' in our templates directory which will contain:


.. code-block:: xml

    <!-- WARNING:  If you do not create the tasks as decribed below, you will need to remove the task attribute from this div -->
    <div id="list_display" class='recordsData' task="can_view_database_list_fav_color">
            
            <div class="editRecord">
            <p>Edit This Information</p>
                    <ul>
                            <li task='can_edit_database_list_fav_color'><span type="form" name="fav_color:id" href="lists?type=fav_color&amp;id=" >Update this Information </span></li>
                            <li><a href="lists?type=emp_status">Select another Favorite Color</a></li>
                    </ul>
            </div> <!-- editRecord -->
            
            <div class="dataTable">
            <table border="0" cellspacing="0" cellpadding="0">
                    <tr>
                            <th colspan="2">Favorite Color</th>
                    </tr>
                    <span type="form" name="fav_color:name" showhead="default"></span>
            </table>
            </div> <!-- dataTable -->
            
    </div> <!-- list_display -->
    



Setting the Edit Database List Favorite Color Task (Optional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the last section, we made use of a task *can_edit_database_list.*   In this section we perform the **optional**  task of addding this to the configuration data.  

Insert the following code into **<SITE DIR>** /modules/DemoPerson/DemoPerson.xml just after the <span style='color:olive'><status>overwrite:true</status></span> tag:
 <configurationGroup name='tasks' path='/I2CE/tasks/task_description'>
    <span style='color:tomato'><nowiki><!-- This node has all of the tasks available to the system and a description of what they are --></nowiki></span>
    <configuration name='can_edit_database_list_fav_color'>
       <span style='color:tomato'><nowiki><!-- This is the task that we added to edit the database list associated with the form fav_color
           The class I2CE_PageFormList checks for the existence of "can_edit_database_list_$formname" for editing the list in the action() method--></nowiki></span>
       <value>Edit the Favorite Color list</value>
       <span style='color:tomato'><nowiki><!-- The description of the task.  It is displayed in the task/role management page --></nowiki></span>
    </configuration>
    <configuration name='can_view_database_list_fav_color'>
       <span style='color:tomato'><nowiki><!-- This is the task that we added to view an existing entry in the database list associated with the form fav_color
           The class I2CE_PageViewList checks for the existence of "can_view_database_list_$formname" for editing the list in the action() method--></nowiki></span>
       <value>View the training course status list</value>
       <span style='color:tomato'><nowiki><!-- The description of the task.  It is displayed in the task/role management page --></nowiki></span>
    </configuration>
 </configurationGroup>
 <configurationGroup name='tasks_trickle_down' path='/I2CE/tasks/task_trickle_down/' >
   <span style='color:tomato'><nowiki><!-- This node is used to describes all the sub-tasks that are a specific task has--></nowiki></span>
   <configuration name='can_view_database_list_fav_color' values='many'> 
     <span style='color:tomato'><nowiki><!--If we can view the database list for 'fav_color' we want to make sure we have permission to view 
         database lists in general. 
         The 'many' attribute says to treat this like an array of values --></nowiki></span>
     <value>can_view_database_lists</value>
   </configuration>
   <configuration name='can_edit_database_list_fav_color' values='many'> 
     <span style='color:tomato'><nowiki><!-- If we can edit the database list 'fav_color' we need to make sure we can view it as well as edit 
         database lists in general.
         The 'many' attribute says to treat this like an array of values --></nowiki></span>
     <value>can_view_database_list_fav_color</value>
     <value>can_edit_database_lists</value>
   </configuration>
 </configurationGroup>
 <configurationGroup name='role_trickle_down' path='/I2CE/tasks/role_trickle_down'>
   <span style='color:tomato'><nowiki><!-- This node is used to describes all the tasks that are assigned to various role --></nowiki></span>
   <configuration name='training_manager' values='many'>
     <span style='color:tomato'><nowiki><!-- This node defines the tasks that are assigned to the 'training_manager' role.  
         The 'many' attribute says to treat this like an array of values --></nowiki></span>  
     <status>uniquemerge:true</status>
     <span style='color:tomato'><nowiki><!-- We want to merge the existing tasks for the training_manager role to the ones we define below.
         The existing values for 'training_manager' are defined in <BASE DIR>/ihris-common/modules/TrainingCourse/TrainingCourse.xml --></nowiki></span>
     <value>can_edit_database_list_fav_color</value>
     <span style='color:tomato'><nowiki><!-- Here we assign the 'can_edit_database_list_fav_color' to the 'training_manager' role --></nowiki></span>
   </configuration>
 </configurationGroup>


Enabling the Module
^^^^^^^^^^^^^^^^^^^
Now that we have everything good to go, we just need to enabled the 'DemoPerson' module in the site.  Open up the file:
 **<SITE DIR>** /iHRIS-Manage-Demo.xml
and add in the following:
 <requirement name='DemoPerson'> 
  <atLeast version='4.0'>
  <lessThan version='4.1'>
 </requirement>

in the <metadata> section after the requirement for *ihris-manage.*  Also, ensure you have:


.. code-block:: xml

       <path name='modules'>
          <value>./modules</value>
       </path>
    




Changing The Favorite Animal Header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Suppose that you want to change the header for the fav_animal field from "Favorite Animal" to "Favorite Mammal."  To do this, we need to update the module [[Configuration (Magic) Data#<version>|version]] as well as add in a <version> tag where we have changed the header.  The changes are highlighted.  In the <metatdata> section we have:
  <metadata> 
  <displayName>Demo Person</displayName> 
  <category>Form</category> 
  <description>Sets up the Demo Person form with extra fields for favorite animals and favorite color</description>    
   <span style='color:olive'><version>4.0.1</version>  </span>
  <requirement name='Person'> 
     <atLeast version='4.0'/> 
    <lessThan version='4.1'/> 
  </requirement> 
  <path name='templates'> 
    <value>./templates</value> 
  </path> 
  <priority>300</priority> 
 </metadata>
and in the defintiion of field 'fav_animal' we have:
      <configuration name='headers' type='delimited' values='many'> 
         <span style='color:olive'><version>4.0.1</version>
         <value>default:Favorite Mammal</value>              </span>
      </configuration>



<center>'''Happy Debugging'''</center>


