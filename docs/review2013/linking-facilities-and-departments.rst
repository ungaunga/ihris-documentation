Linking Facilities and Departments
==================================

In iHRIS Manage, the module ''ihris-manage-PersonPosition'' defines the '''position''' form which contains the field '''department''' and the required field '''facilty''' which are both independent lists.  In this tutorial, we will discuss how customize iHRIS Manage so that, when editing a position, the departments displayed are dependent on the facility chosen.

This tutorial applies to iHRIS Manage 4.0, although the concepts involved can be applied to iHRIS Qualify as well.  Please refer to these articles:
*[[Defining Forms]]
*[[Forms and Form Classes]]
for background information on forms.  You can see these changes in the [http://bazaar.launchpad.net/~ihris%2Bzanzibar/ihris-manage-zanzibar/central-4.0/files/head%3A/modules/ZNZPosition/ Zanzibar-position] module.

==Overview==
Our goal is to have the departments for a position to depend on the facility chosen for the position.  There are two ways that one could do this.
===Option A===
To the ''department'' form, we could add a required field ''facility'' which links to the ''facility'' form.  In this, way we would now have every department associated to a facility.

There are a few issues with this option:
*Suppose you have to hospitals, ''Central Hospital'' and ''Coastal Hospital''.  Each would presumably have a department such as ''Emergency.''  In this option, you would have to create an Emergency Department for each of the Hospitals.  It would then make it difficult to run a report such as "list all employees in all facilities which work in the emergency department"  because it really is "list all employees in all facilities which work in a department with the name ''Emergency.''"   In particular, since we are entering "Emergency" multiple times, there is an increased potential for a spelling mistake which would affect data quality.
*At least for the moment, there is no built in way to first select a facility and then select a department within a form.

Due to these weaknesses, we will not implement Option A in this tutorial.

===Option B===
We could create a new list form '''facility_department''' which contains two required fields, ''facility'' and ''department'' which map the for lists of the same name.   Then in the position form, we no longer link to the list ''facility'' or ''department'' but to the list ''facility_department.'' 
This has the following advantages over Option A:
*We only have to enter the department ''Emergency'' once as we can associate it to many facilities via the ''facility_department'' form
*As facility_department is a tiered list (first select a facility, and the select a department) we can use in the built in display methods when selecting the department in the position.

We will implement option B in this tutorial.

==Creating the module==
We will encapsulate all of our customizations into a module ''my-position'' in order to:
*encapsulate the customizations conceptually
*ease maintenance
*ease sharing of the code
You may wish to review the [[Module Structure]] before continuing.

In your site directory, create a sub-directory 'modules' if it does not already exist and make sure you have an appropriate:
<source lang='xml'>
 <path name='modules'>
   <value>./modules</value>
 </path>
</source>
in your site configuration file.

Within the modules directory, create a new directory called ''my_position.''  Within the ''my_position'' directory, and create the file ''my_position.xml'' and add the following:
<source lang='xml'>
 <?xml version="1.0"?>
<!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
<I2CEConfiguration name='my-position'>     
  <metadata>
    <displayName>Customized iHRIS Position</displayName>   
    <category>Site</category>
    <description>Customized version of the position form to list departments by facility</description>
    <version>4.3.0.1</version>
    <requirement name='ihris-manage-Job'>
      <atLeast version='4.3'/>
      <lessThan version='4.4'/>
    </requirement>
    <requirement name='ihris-manage-PersonPosition'>
      <atLeast version='4.3'/>
      <lessThan version='4.4'/>
    </requirement>
    <path name='classes'>
      <value>./lib</value>
    </path>
    <path name='templates'>
      <value>./templates</value>
    </path>
  </metadata>
  <configurationGroup name='my-position' path='/'>
  </configurationGroup>
 </I2CEConfiguration>
</source>

==Turning off the existing fields==
Let us first look at the changes to "turn off" the facility and department fields in the position form.  

The position form is implemented by the class ''iHRIS_Position'' in the ''ihris-manage-PerosnPosition'' module.  Instead of removing them from the existing iHRIS_Position form, we will specify them as not being required and not saved in the database.  We also remove the reference to them in the html template files for position.
===Magic Data/Configuration Changes===
We will create a new form class ''My_Position'' which extends the ''iHRIS_Position'' form class and set the ''position'' form to use this class:
<source lang='xml'>
 <configurationGroup name='forms' path='/modules/forms/forms'>
   <configurationGroup name='position'>
        <!--Set the position form to use the My_Position class which we will define below-->
        <displayName>Position</displayName>
        <description>The Position Form</description>
        <configuration name='class' values='single'>
          <displayName>Class Name</displayName>
          <description>The name of the class providing the form</description>
          <value>My_Position</value>
        </configuration>
      </configurationGroup>
 </configurationGroup>
 <configurationGroup name='forms' path='/modules/forms/formClasses'>
      <configurationGroup name='My_Position'>     
        <!--"turn off" the facility and department fields for position -->
        <configuration name="extends">
          <displayName>The class this form extends</displayName>
          <value>iHRIS_Position</value>
        </configuration>
        <configurationGroup name="fields">
          <configurationGroup name="department">
            <displayName>The field 'department'</displayName>
            <configuration name='required' type='boolean'>
              <value>false</value>
            </configuration>
            <configuration name='in_db' type='boolean'>
              <value>false</value>
            </configuration>
          </configurationGroup>
          <configurationGroup name="facility">
            <displayName>The field 'department'</displayName>
            <configuration name='required' type='boolean'>
              <value>false</value>
            </configuration>
            <configuration name='in_db' type='boolean'>
              <value>false</value>
            </configuration>
          </configurationGroup>
      </configurationGroup>
 </configurationGroup>
</source>

===Template File Changes===
Create a directory called 'templates' in the 'my_position' directory and copy these files:
*templates/en_US/lists_form_position.html    
*templates/en_US/view_position.html
from the ihris-manage-PersonPosition module into the this directory.  On the new copy lists_form_position.html remove the lines:
<source lang='xml'>
  <span type="form" name="facility" showhead="default"></span>
  <span type="form" name="department" showhead="default"></span>
</source>
On the new copy of ''view_position.html'' remove the lines:
<source lang='xml'>
  <span type="form" name="position:facility" showhead="default" class="even"></span>
  <span type="form" name="position:department" showhead="default"></span>
</source>
and the line:
<source lang='xml'>
  <li task='can_edit_database_list_position'>
     <span type="form" name="position:facility" 
            href="lists?type=position&amp;field=facility&amp;forms%3Aposition%3A0%3Afields%3Afacility=" 
     >Select another Position</span>
  </li>
</source>

==Creating the facility_department==
We will create a new form ''facility_department'' which is implemented by the form class ''My_Facility_Department'' which contains the mapped fields facility and department.
===Magic Data/Configuration Changes===
All of these changes are in the ''my_position.xml'' file.

First, we need to create the form class 'My_Facility_Department'.  To do this, we add in the following under the configurationGroup named 'formClasses':
<source lang='xml'>
 <configurationGroup name='My_Facility_Department'>
 <!-- pairs up facilities with a department list-->
  <configuration name="extends">
   <displayName>The class this form extends</displayName>
   <value>I2CE_List</value>
  </configuration>
  
  <configurationGroup name="meta" path="meta/list/default">
    <configuration name="display_string">
      <value>%s, %s</value>
    </configuration>
    <configuration name="display_args" type="delimited" values="many">
      <value>0:facility</value>
      <value>1:department</value>
    </configuration>
    <configuration name="sort_fields" type="delimited" values="many">
      <value>0:facility</value>
      <value>1:department</value>
    </configuration>
  </configurationGroup>

  <configurationGroup name="fields">
   <configurationGroup name='facility'>
    <configuration name="formfield">
     <displayName>The form field type</displayName>
     <value>MAP</value>
    </configuration>
    <configuration name="required" type="boolean">
     <displayName>This field is required to be set</displayName>
     <value>true</value>
    </configuration>
   </configurationGroup>
   <configurationGroup name='department'>
    <configuration name="formfield">
     <displayName>The form field type</displayName>
     <value>MAP</value>
    </configuration>
    <configuration name="unique" type="boolean">
     <displayName>This field is requried to be unique</displayName>
     <value>true</value>
    </configuration>
    <configuration name="unique_field">
     <displayName>This field is required to be unique for each facility</displayName>
     <value>facility</value>
    </configuration>
    <configuration name="required" type="boolean">
     <displayName>This field is required to be set</displayName>
     <value>true</value>
    </configuration>
   </configurationGroup>
 </configurationGroup>
</configurationGroup>
</source>

Next, let us add in the 'facility_department' form.  To do this, we add in the following under the configurationGroup named 'forms':
<source lang='xml'>
 <configurationGroup name='facility_department'>
  <displayName>Facility Department</displayName>
  <description>The Facility Department Form</description>
  <configuration name='class' values='single'>
  <displayName>Class Name</displayName>
   <description>The name of the class providing the form</description>
   <value>My_Facility_Department</value>
  </configuration>
  <configuration name='display' values='single'>
    <displayName>Display name</displayName>
    <description>The display name for this form</description>
     <value>Facilitiy/Department</value>
  </configuration>
  <configuration name="storage" values='single'>
    <displayName>Storage Details</displayName>
    <description>The storage mechanism for this form.</description>
    <value>magicdata</value>
  </configuration>
 </configurationGroup>
</source>
Next, we need to add in the 'facility_department' as a mapped field to the 'My_Position' class.  To do this, we add in the following:
<source lang='xml'>
          <configurationGroup name="facility_department">
            <configuration name="formfield">
              <displayName>The form field type</displayName>
              <value>MAP</value>
            </configuration>
            <configuration name="headers" type="delimited">
              <displayName>The headers for this field.</displayName>
              <value>default:Department</value>
            </configuration>        
            <configuration name="required" type="boolean">
              <displayName>This field is requried to be set</displayName>
              <value>true</value>
            </configuration>
              <configurationGroup name="meta">
                <configurationGroup name="display">
                  <configurationGroup name="default">
                    <configuration name="fields">
                      <!-- the says that the default display is to first show/select the facility and then the facility_deparment-->
                      <value>facility_department:facility</value>
                    </configuration>
                  </configurationGroup>
                </configurationGroup>
              </configurationGroup>         
          </configurationGroup>
</source>
under the ''fields'' node for ''My_Position''.

Finally, we want to create a 'task' that deals with editing and viewing the 'facility_department' list.  We will want to make sure that the edit task implies the view task.  We will also want to add these tasks to the the edit/view organization list task. To do so, we add in the following:
<source lang='xml'>
    <configurationGroup name='tasks' path='/I2CE/tasks/task_description'>
      <configuration name='can_edit_database_list_facility_department'>
        <value>Edit the facility/department list</value>
      </configuration>
      <configuration name='can_view_database_list_facility_department'>
        <value>View the facility/department list</value>
      </configuration>   
    </configurationGroup>

    <configurationGroup name='tasks_trickle_down' path='/I2CE/tasks/task_trickle_down/' >   
      <configuration name='can_edit_database_list_facility_department' values='many'>     
        <value>can_edit_organization_database_lists</value>
        <value>can_view_database_list_facility_department</value>
      </configuration>
      <configuration name='can_edit_all_organization_database_lists' values='many'>     
        <value>can_edit_database_list_facility_department</value>
      </configuration>
      <configuration name='can_view_all_organization_database_lists' values='many'>     
        <value>can_view_database_list_facility_department</value>
      </configuration>
    </configurationGroup>
</source>

===Template File Changes===
In your copy of the view_postion.html file, add the following:
<source lang='xml'>
  <!-- Show the facility_department with the default header -->
  <span type="form" name="position:facility_department" showhead="default" class="even"></span>
</source>
and:
<source lang='xml'>
  <li task='can_edit_database_list_position'>
    <span type="form" 
          name="position:facility_department" 
          href="lists?type=position&amp;field=facility_department&amp;forms%3Aposition%3A0%3Afields%3Afacility_department=">
      Select another Position
    </span>
  </li>
</source>
where you deleted the similar lines above.

In your copy of the file list_form_position.html add in the the following line:
<source lang='xml'>
 <span type="form" name="facility_department" showhead="default"></span>
</source>
where you deleted the lines above.
===Templates for facility_department===
We need to create two templates to view and edit the facility_department form.  We will put these in the 'my_postion/templates' directory.
Create the file 'lists_form_facility_department.html' and add the following:
<source lang='xml'>
<tbody id="list_fields">
  <tr>
    <td class="formdata">
      <span type="form" name="facility_department:facility" showhead="default" addlink="lists?add=1&amp;type=facility"></span>
    </td>
    <td class="formdata">
      <span type="form" name="facility_department:department" showhead="default" addlink="lists?add=1&amp;type=department"></span>
    </td>
  </tr>
</tbody>
</source>
Now create the file 'view_list_facility_department.html' and add the following:
<source lang='xml'>
 <div id="list_display" task='can_view_database_list_facility_department'>
  <div class="editRecord">
    <p>Edit This Information</p>
    <ul>
      <li task='can_edit_database_list_facility_department'><span type="form" name="facility_department:id" href="lists?type=facility_department&amp;id=" >Update this Information </span></li>
      <li><a href="lists?type=facility_department&amp;field=facility" >Select another Facility/Department</a></li>
    </ul>
  </div> <!-- editRecord -->
  
  <div class="dataTable">
    <table border="0" cellspacing="0" cellpadding="0">
      <tr>
        <th colspan="2">Associate Departments to A Facility</th>
      </tr>
      <span type="form" name="facility_department:facility" showhead="default" addlink="lists?add=1&amp;type=facility"></span>
      <span type="form" name="facility_department:department" showhead="default" addlink="lists?add=1&amp;type=department"></span>


      

    </table>
  </div> <!-- dataTable -->
  
</div> <!-- list_display -->
</source>

===The Facility Departments class===
When a field maps to the facility_department form we want the display to be first the facility and then the department.  In order to do this, we need to create the My_Facility_Department class as a file.  To do so, first create the directory 'lib' in the 'my_position' directory.  In this new directory, create a file 'My_Facility_Department.php' and add the contents:
<source lang='php'>
 class My_Facility_Department extends I2CE_List {
     /**
     * The main field name used for display a description of a record.
     */
    const MAIN_FIELD = "facility";
    /**
     * The secondary field name used for displaying a description of a record in combination with the MAIN_FIELD.
     */
    const SEC_FIELD = "department";
    /**
     * The sort field name to be used for sorting the display list.  This can't be used with the SEC_FIELD option for display.
     */
 }
</source>
(In an upcoming step, we shall remove this step and allow you to specify it in magic data.)

===Edit Database List Templates===
We finally want to customize our Edit Database Lists page so that the new list, ''facility_department''  shows up.  First, create the directory ''templates'' in your site directory, if it doesn't already exist, and ensure that your site configuration file has the line:
<source lang='xml'>  
 <path name='templates'>
   <value>./templates</value>
 </path>
</source>
Now, copy the files lists.html from the iHRIS Manage to this new directory.  Edit the new copy and add the line:
<source lang='xml'>
 <li task='can_edit_database_list_facility_department'><a href="lists?type=facility_department&amp;field=facility">Associate Departments To A Facility</a></li>
</source>
just after the similar line for Department.

Next, change the line:
<source lang='xml'>
 <li task='can_edit_database_list_position'><a href="lists?type=position&amp;field=facility">Positions (by Facility)</a></li>
</source>
to:
<source lang='xml'>
 <li task='can_edit_database_list_position'><a href="lists?type=position&amp;field=facility_department">Positions (by Facility/Department)</a></li>
</source>

==Enabling the Module==
You can now enable your module by adding the following:
<source lang='xml'>
 <requirement name='my-position'>
   <atLeast version='4.0'/>
   <lessThan version='4.1'/>
 </requirement>
</source>
to your site configuration file.

==Reporting and Form Relationship== 
Because the form relationships have changed:
*Old: the ''position'' form links to the ''facility'' and ''department'' forms.
*New: the ''position'' form links to the ''facility_department'' form which in turn links to the ''facility'' and ''department'' forms.
our form relationship used to define the staff reports need to be changed.  Rather than detailing these changes in this tutorial you may look at them [http://bazaar.launchpad.net/~ihris%2Bzanzibar/ihris-manage-zanzibar/central-4.0/files/head%3A/modules/ZNZReports/Reports/StaffReports/ here]

[[Category:Forms]][Category:iHRIS Manage]][[Category:Review2013]]
