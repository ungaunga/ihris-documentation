Senegal Tutorial - Add a Field to the Demographic Form
======================================================

This tutorial explains how to customize iHRIS Manage to support adding the field "Number of Spouses" to the demographic form.

=Assumptions=
For this tutorial we will assume you have your site installed in:  
: /var/lib/iHRIS/sites/4.1/sn-manage/
The iHRIS core modules will be assumed to be:  
: /var/lib/iHRIS/lib/4.1/

=Create a Module=
First we need to create a new module in the site modules directory.


.. code-block:: bash

    mkdir /var/lib/iHRIS/sites/4.1/sn-manage/modules/Senegal-demographic
    


Now we need to create the basic information for the module configuration file.


.. code-block:: bash

    cd /var/lib/iHRIS/sites/4.1/sn-manage/modules/Senegal-demographic
    gedit Senegal-demographic.xml
    


We will need to set up the standard meta information for the module like this:



.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="Senegal-demographic">
      <metadata>
        <displayName>iHRIS Demographic Customizations for Senegal</displayName>
        <category>Site</category>
        <description>Module to customize the demographic form for Senegal.</description>
        <creator>Intrahealth Informatics</creator>
        <email>hris@capacityproject.org</email>
        <link>https://launchpad.net/ihris-senegal</link>
        <version>4.1.5.1</version>
        <path name="configs">
          <value>./configs</value>
        </path>
        <path name="templates">
          <value>./templates</value>
        </path>
        <requirement name="ihris-manage-PersonDemographic">
          <atleast version="4.1" />
        </requirement>
        <priority>450</priority>
      </metadata>
      <configurationGroup name="Senegal-demographic" path="/I2CE">
      </configurationGroup>
    </I2CEConfiguration>
    


=Add a New Field=
Now we need to modify the configuration file to include the changes for the Demographic form.  Place this inside the main configurationGroup in the site configuration file (Senegal-demographic.xml).  This is for an English version of the field, you can change the locale to be "fr_FR" and set the value to be in French if desired.



.. code-block:: xml

        <configurationGroup name="formClasses" path="/modules/forms/formClasses/iHRIS_ManageDemographic">
          <version>4.1.5.1</version>
          <configurationGroup name="fields">
            <displayName>The fields defined for this form</displayName>
            <configurationGroup name="num_spouses">
              <displayName>The field 'num_spouses'</displayName>
              <configuration name="formfield">
                <displayName>The form field type</displayName>
                <value>INT</value>
              </configuration>
              <configuration name="headers" type="delimited" locale="en_US">
                <displayName>The headers for this field.</displayName>
                <value>default:Number of Spouses</value>
              </configuration>
            </configurationGroup>
          </configurationGroup>
        </configurationGroup>
    


=Update the Templates=
Now we need to copy the existing template files to the module to add the new field.  The template we want to modify is in the iHRIS Manage source code in the ManagePersonDemographic module.  We will create the templates directory and then copy the files to be modified.  To copy the French version of the page you can replace en_US with fr in the following commands.



.. code-block:: bash

    mkdir -p templates/en_US
    cp /var/lib/iHRIS/lib/4.1/ihris-manage/modules/ManagePersonDemographic/templates/en_US/view_demographic.html templates/en_US/
    cp /var/lib/iHRIS/lib/4.1/ihris-manage/modules/ManagePersonDemographic/templates/en_US/form_demographic.html templates/en_US/
    


Now we edit the view page to add the new field.


.. code-block:: bash

    gedit templates/en_US/view_demographic.html
    


Make the file appear as below:


.. code-block:: html4strict

    <div task='person_can_view_child_form_demographic'>
      <div class="editRecord">
        <p>Edit This Information</p>
        <ul>
          <li task='person_can_edit_child_form_demographic'>
    	<span type="form" ifset="demographic:id" name="demographic:id" href="demographic?id=" parent="true">
    	  Update this Information
    	</span>
          </li>
        </ul>
      </div> <!-- editRecord -->
    
      <div class="dataTable">
        <table border="0" cellspacing="0" cellpadding="0">
          <tbody>
    	<tr>
    	  <th colspan="2">Demographic Information</th>
    	</tr>
    	<span type="form" name="demographic:birth_date" showhead="default"></span>
    	<span type="form" name="demographic:gender" showhead="default" class="even"></span>
    	<span type="form" name="demographic:marital_status" showhead="default"></span>
    	<span type="form" name="demographic:dependents" showhead="default" class='even'></span>
    	<span type="form" name="demographic:num_spouses" showhead="default"></span>
          </tbody>
        </table>
      </div> <!-- dataTable -->
    </div>
    


Save this file and now edit the form template:


.. code-block:: bash

    gedit templates/en_US/form_demographic.html
    


Add the num_spouses field here as well:



.. code-block:: html4strict

    <tbody>
    <tr>
        <th colspan="2">Demographic Information</th>
    </tr>
    <tr id="list_fields">
        <td>
            <span type="form" name="demographic:birth_date" showhead="default"></span>
            <span type="form" name="demographic:gender" showhead="default"></span>
        </td>
        <td>
            <span type="form" name="demographic:marital_status" showhead="default"></span>
            <span type="form" name="demographic:dependents" showhead="default"></span>
            <span type="form" name="demographic:num_spouses" showhead="default"></span>
        </td>
    </tr>
    </tbody>
    
    


Now save this file.  The module is now complete.

=Enable the New Module=
Now we need to enable the module in the site configuration file.  Edit the site configuration file with this command.



.. code-block:: bash

    cd /var/lib/iHRIS/sites/4.1/sn-manage
    gedit iHRIS-Manage-Senegal.xml
    


In the section where modules are enabled, add the following line:



.. code-block:: xml

      <enable name="Senegal-demographic" />
    


Now when you access the site it should update and your new field will now appear on the demographic form.


