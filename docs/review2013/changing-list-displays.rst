Changing List Displays
======================

There are many lists in the system and there are many options on how to display them.  Here we look at customizing the display of the Position list by dropping the use of the Position Code completely and adding in the Position Type to the display

__TOC__
==Setting the Display Value==
The default position list display is set in the configuration .xml file for the ''ihris-manage-PersonPosition'' module.  You can see where this is defined in magic data on lines [http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/view/head:/modules/ManagePersonPosition/PersonPosition.xml#L789 795-811].  Here we are defining the "default" list display at the magic data node:
 /modules/forms/formClasses/iHRIS_Position/meta/list/default
The three important parts here are:
*The "display_string" which is "%s: %s (%s, %s)".   Whenever you see a '%s' you in the display string we expect to substitute a field of the form into the string.  For more details, see the explanation of the [http://www.php.net/manual/en/function.sprintf.php printf format].
*The "display_args" which are the fields that are passed to the display string.  These are substituted in order into the display string.
**0:code
**1:title
**2:facility
**3:department
*The order in which the list is displayed.   We are specifying that we first sort by the position code. Then, if two positions have the same code for some reason (or no code at all), then we sort by the title
**0:code
**1:title


==Displaying Drop-Downs in a Tree==
We often deal with hierarchical data, for example you have have a collection of facility and each facility contains a set of positions.   When choosing a position it would be nice if we could first select the facility and then the position.  

For example the person-position form, which is used to record a person holding a position, links to the position form.  The person-position form uses the form class iHRIS_PersonPosition.  Setting the hierarchical display (tree view) is accomplished on lines [http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/view/head:/modules/ManagePersonPosition/PersonPosition.xml#L713 713-720] for the iHRIS-PersonPosition form.  Here we are saying that the magic data node:
 /modules/forms/formClasses/iHRIS_PersonPosition/fields/position/display/default/fields
has the value
 facility:position
The means that we first display the facilities and then then positions that are under that facility.


==Limiting the Displayed Positions==
When selecting a position in a drop-down list, we have already seen how to change how the list is displayed.  We can also automatically add "limits" to the list.    The position form contains a field status, which can be one of "Open", "Closed" or "Discontinued."  When setting the person position, we only want to choose from the open positions.  This is accomplished by adding a "default" limit to the position field of the person-position form as can be seen on lines [http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/view/head:/modules/ManagePersonPosition/PersonPosition.xml#L684 694-712].  

Pleaes, note also that one lines 

Here we are defining the contents of the magic data node under:
 /modules/forms/formClasses/iHRIS_PersonPosition/fields/meta/limits/default
Since the position list is a tree view, there are two forms that we need to use when populating the position list, the facility form and the position form.  For each of these forms we can specify a set of limits that apply when we create our tree-view.  In this case, we are only interested in limiting the positions to the open positions, in the words the positions whose position_status field is open.  Thus we set the magic data node:
   /modules/forms/formClasses/iHRIS_PersonPosition/fields/meta/limits/default/position
to be the limit:
<source lang='php'>
array(  
 'operator'=>'FIELD_LIMIT',
 'field'=>'status',
 'style'=>'equals',
 'data'=>array(
    'value'=>'position_status|open'
  )
)
</source>

==Creating a module==
Suppose that you wanted to customized the position list so that it no longer displays the position code.   We could create a module containing our "position" customizations that would require the "ihris-manage-PersonPosition" module and define a new display as in the following:
<source lang='xml'>
<?xml version="1.0"?>
<!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
<I2CEConfiguration name="my-Position">
  <!-- creating a new module called my-Position.  We will need to require this module in our site module-->
  <metadata>
    <displayName>My Position</displayName>
    <category>Application Component</category>
    <description>Module for my customized position form </description>
    <creator>Intrahealth Informatics</creator>
    <email>hris@capacityproject.org</email>
    <link>https://launchpad.net/ihris-manage</link>
    <version>4.1.0</version>
    <requirement name="ihris-manage-PersonPosition">
      <!-- We will be customizing by extending the existing PersonPosition class which is defined in the ihris-manage-PersonPosition module.  
           Thus we need  to require it here-->
      <atLeast version="4.1" />
      <lessThan version="4.2" />
    </requirement>
    <path name="templates">
      <!-- Since we are removing the position code, we will want to make customized .html templates which do not reference the "postion+code".  
           We will store them in the templates subdirectory of this module -->
      <value>./templates</value>
    </path>
    <!-- set the priority of this module higher than the "ihris-manage-PersonPostion" modules (which is 350) so that we load this module's 
         templates over the ihris-manage-PersonPosition templates-->
    <priority>380</priority>
  </metadata>
  <configurationGroup name="my-Position" path="/I2CE">
     <configurationGroup name='MyPosition' path="/modules/forms/forms/position">
          <configuration name="class" values="single">
            <!-- Specifies that the form position will use the customized MyPosition form class -->
            <value>MyPosition</value>
          </configuration>
     </configurationGroup>
     <configurationGroup name='MyPositionClass' path="/modules/forms/formClasses/MyPosition">
          <!-- Definition of the custom MyPosition form class -->
          <configuration name="extends">
            <displayName>The class this form extends</displayName>
            <!-- Specify that we are modifying the iHRIS_Position class -->
            <value>iHRIS_PersonPosition</value>
          </configuration>
          <configurationGroup name="meta" path="meta/list/default">
            <configuration name="display_string">
              <value>%s (%s, %s) %s</value>
            </configuration>
            <configuration name="display_args" type="delimited" values="many">
              <!-- The display of the list will look like:  Title (Facility, Department) Type-->
              <value>0:title</value>
              <value>1:facility</value>
              <value>2:department</value>
              <value>3:pos_type</value>
            </configuration>
            <configuration name="sort_fields" type="delimited" values="many">
              <!-- Sort on title, then facility, then department -->
              <value>0:title</value>
              <value>1:facility</value>
              <value>2:department</value>
            </configuration>
          </configurationGroup>
     </configurationGroup>
  </configurationGroup>
</I2CEConfiguration>
</source>
Note:  we have set the versions based on 4.1 of the software, this may be different for you if you are using version 4.0.

==Customized Templates==
There are two files under "templates/en_US" of the "ihris-manage-PersonPosition" module that reference the "code" field which we are not using anymore.  These are "lists_form_postion.html" and "view_position.html."   We will need to create the "templates/en_US" sub-directories of our modules, copy these two files into it and  modify them by removing the reference to the code field.  Here is the result for "list_form_position.html:"
<source lang='xml'>
<tbody id="list_fields">
        <tr>
        <td class="formdata">
                <span type="form" name="position:job" showhead="default" 
                        onchange="if ( document.getElementById('forms[position][0][0][fields][title]').value == '' &amp;&amp; this.selectedIndex != 0 ) document.getElementById('forms[position][0][0][fields][title]').value = this.options[this.selectedIndex].text;" 
                        addlink="position?add=1&amp;type=job" addtask='position_can_edit'></span>
                <span type="form" name="position:title" showhead="default"></span>
                <span type="form" name="position:description" showhead="default"></span>
                <span type="form" name="position:proposed_salary" showhead="default"></span>
                <span type="form" name="position:source" showhead="default"></span>
                <span type="form" name="position:posted_date" showhead="default"></span>
                <span type="form" name="position:comments" showhead="default"></span>
        </td><td class="formdata">
       <!-- We can either delete this line completely or comment it out.  <span type="form" name="position:code" showhead="default"></span> -->
                <span type="form" name="position:supervisor" showhead="default"></span>
                <span type="form" name="position:facility" showhead="default"></span>
                <span type="form" name="position:department" showhead="default"></span>
                <span type="form" name="position:pos_type" showhead="default"></span>
                <span type="form" name="position:proposed_hiring_date" showhead="default"></span>
                <span type="form" name="position:proposed_end_date" showhead="default"></span>
                <span type="form" name="position:status" showhead="default" noedit="true"></span>
                <span type="form" name="position:interview_comments" showhead="default"></span>
    </td>
    </tr>
</tbody>

</source>

[[Category:Customizations]][[Category:Review2013]]
