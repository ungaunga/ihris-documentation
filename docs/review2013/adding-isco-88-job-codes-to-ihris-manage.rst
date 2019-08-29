Adding ISCO 88 Job Codes to iHRIS Manage
========================================

The ISCO 88 Job Codes can be found [http://BLAH here] and represent an international standard for classifying jobs.  They are broken up hierachically into  major, sub-major , minor groups under which the job codes (called unit) are under the minor groups.

We will create a module for each of the major groups, all of which will sit under a meta-module.

Getting The Data
^^^^^^^^^^^^^^^^
The data file with all of the codes compiled can be found in the launchpad [http://BLAH bzr] repository for I2CE. All of the codes, names, and descriptions were downloaded from the International Labor Organization's  `website <http://www.ilo.org/public/english/bureau/stat/isco/isco88/index.htm>`_ .

Creating The XML Magic(Configuration) Data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The ISCO 88 codes are going to be separated into 10 different xml files, each representing a major group. Each xml file will contain the number and description of the major number followed by all the sub-major, minor, and then unit. The php code is provided  `here <http://bazaar.launchpad.net/~intrahealth%2Binformatics/ihris-manage/3.2-dev/files/head%3A/modules/ManageJob/modules/isco_88/tools/>`_  and needs to be in the same directory as the isco88 codes file to run.

Creating The Modules
^^^^^^^^^^^^^^^^^^^^
Since this data is related to Jobs in iHRIS Manage, we will put everything as sub-modules under the **ihris-manage-Job** . This can be found in the directory:
 [BASE INSTALLATION PATH]/ihris-manage/modules/ManageJob
All instructions below assume that you are in this directory.

The first thing we will need to do is to enable sub-modules for *ihris-manage-Job *  (you may wish to read the [[Module Structure | module structure]] overview before proceeding).  To do this
 gedit Job.xml
and make sure the following lines are in the appropriate place in the metadata section:

.. code-block:: xml

    <path name='modules'>
      <value>./modules</value>
    </path>
    

Now we add the modules directory
 mkdir modules

Creating The Meta-Module
~~~~~~~~~~~~~~~~~~~~~~~~
We will create a meta-module to contain general information about the ISCO Codes
 cd [BASE INSTALLATION PATH]/ihris-manage/modules/ManageJob/modules
 mkdir isco_88
 cd isco_88
 mkdir modules
 gedit ISCO_88.xml
Add the following contents and save:

.. code-block:: xml

    <?xml version="1.0"?>       
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name='isco-88'>      
      <metadata>
        <displayName>ISCO 88 Job Codes</displayName>   
        <description>The ISCO 88 Job Codes</description>
        <version>3.2.0</version>
        <path name='modules'>
          <value>./modules</value>
        </path>
     </metadata>
     <configurationGroup name='isco-88' path='/'>
    
       <configurationGroup name='isco_88_forms' path='/modules/forms/formClasses'>
         <!--we will add a form class for each of the isco 88 groupings -->
         <!--each form class will extend the class I2CE_List -->
         <!--each form class will provide the field 'name' and 'description' of which name is required -->
         <!--the forms will map to each other in a heirachical relationship as follows:
             iHRIS_ISCO_88_Sub_Major has a field isco_88_major which will map to the isco_88_major form
             iHRIS_ISCO_88_Minor has a field isco_88_sub_major which will map to the isco_88_sub_major form
             iHRIS_ISCO_88_Unit has a field isco_88_minor which will map to the isco_88_minor form
             -->
         <!--we will specify a header (or title) for each of the fields we add in the forms -->
         <!--the corrseponding forms are defined in the block  following this one -->
            <configurationGroup name='iHRIS_ISCO_88_Major'>
              <configuration name="extends">
                <!-- This form class extends I2CE_List class  -->
                <value>I2CE_List</value>
              </configuration>
              <configurationGroup name="fields">
                <!-- The fields defined for this form -->
                <configurationGroup name="name">
                  <configuration name="formfield">
                    <!-- The field type is string-->
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Major Group</value>
                  </configuration>
                  <configuration name="required" type="boolean">
                    <!--This field is requried -->
                    <value>true</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="description">
                  <configuration name="formfield">
                    <!-- The field type is a multi-line string -->
                    <value>STRING_MLINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Description</value>
                  </configuration>
                </configurationGroup>
              </configurationGroup>
            </configurationGroup>
            <configurationGroup name='iHRIS_ISCO_88_Sub_Major'>
              <configuration name="extends">
                <!-- this form class extends I2CE_List -->
                <value>I2CE_List</value>
              </configuration>
              <configurationGroup name="fields">
                <!-- The fields defined for this form -->
                <configurationGroup name="name">
                  <configuration name="formfield">
                    <!--The field type is string_line -->
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Sub-Major Group</value>
                  </configuration>
                  <configuration name="required" type="boolean">
                    <!--This field is requried -->
                    <value>true</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="description">
                  <configuration name="formfield">
                    <!--The field type is multi-line string -->
                    <value>STRING_MLINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Description</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="isco_88_major">
                  <configuration name="formfield">
                    <!--The field  is a mapped  value -->
                    <value>MAP</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Major Group</value>
                  </configuration>
                </configurationGroup>
              </configurationGroup>
            </configurationGroup>
            <configurationGroup name='iHRIS_ISCO_88_Minor'>
              <configurationGroup name="fields">
                <!-- The fields defined for this form -->
                <configurationGroup name="name">
                  <configuration name="formfield">
                    <!--The field type is string -->
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Minor Group</value>
                  </configuration>
                  <configuration name="required" type="boolean">
                    <!--This field is requried -->
                    <value>true</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="description">
                  <configuration name="formfield">
                    <!--The field type is mult-line string -->
                    <value>STRING_MLINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Description</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="isco_88_sub_major">
                  <configuration name="formfield">
                    <!--The field is a mapped value -->
                    <value>MAP</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Sub-Major Group</value>
                  </configuration>
                </configurationGroup>
              </configurationGroup>
            </configurationGroup>
            <configurationGroup name='iHRIS_ISCO_88_Unit'>
              <configurationGroup name="fields">
                <!-- The fields defined for this form-->
                <configurationGroup name="name">
                  <configuration name="formfield">
                    <!--The field type is string -->
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Unit</value>
                  </configuration>
                  <configuration name="required" type="boolean">
                    <!--This field is requried -->
                    <value>true</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="description">
                  <configuration name="formfield">
                    <!--The field type is a mult-line string -->
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Description</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="isco_88_sub_major">
                  <configuration name="formfield">
                    <!--The field is a mapped-value -->
                    <value>MAP</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <!-- The headers for this field. -->   
                    <value>default:Minor Group</value>
                  </configuration>
                </configurationGroup>
              </configurationGroup>
            </configurationGroup>
        </configurationGroup>
    
    
       <configurationGroup name='isco_88_forms' path='/modules/forms/forms'>
         <!--we will add a form for each of the isco 88 groupings -->
            <configurationGroup name='isco_88_major'>
              <configuration name='class' values='single'>
                <!-- The name of the class providing the form -->
                <value>iHRIS_ISCO_88_Major</value>
              </configuration>
              <configuration name='display' values='single'>
                <!-- The display name for this form -->
                <value>ISCO 88 Major</value>
              </configuration>
              <configuration name="storage" values='single'>
                <!-- The storage mechanism for this form. --!>
                <value>magicdata</value>
              </configuration>
            </configurationGroup>
            <configurationGroup name='isco_88_sub_major'>
              <configuration name='class' values='single'>
                <!-- The name of the class providing the form -->
                <value>iHRIS_ISCO_88_Sub_Major</value>
              </configuration>
              <configuration name='display' values='single'>
                <!-- The display name for this form -->
                <value>ISCO 88 Sub-Major</value>
              </configuration>
              <configuration name="storage" values='single'>
                <!-- The storage mechanism for this form. --!>
                <value>magicdata</value>
              </configuration>
            </configurationGroup>
            <configurationGroup name='isco_88_minor'>
              <configuration name='class' values='single'>
                <!-- The name of the class providing the form -->
                <value>iHRIS_ISCO_88_Minor</value>
              </configuration>
              <configuration name='display' values='single'>
                <!-- The display name for this form -->
                <value>ISCO 88 Minor</value>
              </configuration>
              <configuration name="storage" values='single'>
                <!-- The storage mechanism for this form. -->
                <value>magicdata</value>
              </configuration>
            </configurationGroup>
            <configurationGroup name='isco_88_unit'>
              <configuration name='class' values='single'>
                <!-- The name of the class providing the form -->
                <value>iHRIS_ISCO_88_Unit</value>
              </configuration>
              <configuration name='display' values='single'>
                <!-- The display name for this form -->
                <value>ISCO 88 Unit</value>
              </configuration>
              <configuration name="storage" values='single'>
                <!-- The storage mechanism for this form. -->
                <value>magicdata</value>
              </configuration>
            </configurationGroup>
         </configurationGroup>
    
    
    
    
       <configurationGroup name='isco_88_field' path='/modules/forms/formClasses/iHRIS_Job/fields/isco_88_unit'>
         <!--Add the isco_88_unit field into iHRIS_Job which will point to the isco_88_units/job codes we have-->
         <configuration name="formfield">
           <!-- This is a mapped value-->
           <value>MAP</value>
         </configuration>
         <configuration name="headers" type="delimited">
           <!-- The headers for this field. -->   
           <value>default:ISCO 88 Code</value>
         </configuration>
         <configurationGroup name="display">
           <configurationGroup name="default">
             <configuration name="fields">
               <!--This describes the default display and select isco_88_unit field.  We start
                   in the lowest part of the hierarchy of forms, isco_88_unit and proceed up to the top
                   part, the isco_88_major. The forms are separated by colons.  
                   When a value is selected, the full hierarchy is displayed. 
                   When a value is displayed, we only display the the isco_88_unit data, as the
                   other forms' display is suppressed by the [ ] -->
               <value>isco_88_unit:[isco_88_minor]:[isco_88_sub_major]:[isco_88_major]</value>
             </configuration>
           </configurationGroup>
         </configurationGroup>
       </configurationGroup>
     </configurationGroup>
    </I2CEConfiguration>
    

Creating The Sub-Modules
~~~~~~~~~~~~~~~~~~~~~~~~
We are going to create a sub-module for each of the Major Groups.  

The template for the configuration file is:

.. code-block:: xml

    <?xml version="1.0"?>       
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name='isco-88-major-XX'>      
      <metadata>
        <displayName>ISCO 88 Job Codes</displayName>   
        <description>The ISCO 88 Job Codes</description>
        <version>3.2.0</version>
        <requirement name='isco-88'> 
           <atLeast version='3.2'/>
           <lessThan version='3.3'/>
        </requirement>
     </metadata>
     <configurationGroup name='isco-88-major-XX' path='/'> 
       <!--Form Data Goes here -->
     </configurationGroup>
    </I2CEConfiguration> 
    

where **XX**  is the Major Group number.

For each Major Group number *XX* , we will do:
 mkdir [BASE INSTALLATION PATH]/ihris-manage/modules/ManageJob/modules/isco_88/modules/isco_88_major_XX
and put the generated configuration file in this directory.

