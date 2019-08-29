Adding Forms and Fields
=======================

This will describe how to add a new module to iHRIS Manage to add in two new forms for tracking Professional Development for an employee.  These instructions could be modified for iHRIS Qualify with a few minor changes.  There will be one form for Professional Development for courses to be logged for employees.  Any number of these forms can be associated with an employee.  There will also be a link to Add Continuous Professional Development.  Only one of these forms will be associated with an employee.  It can be used to save the current training needs requested by the employee for professional and personal development.


Step 1: Create the module
^^^^^^^^^^^^^^^^^^^^^^^^^

Change into your site's modules directory and create a new directory called ProfDevelopment and change into this directory.  Create lib and templates directory in the ProfDevelopment directory.  Create and edit a new file called ProfDevelopment.xml (in the ProfDevelopment directory) with the following contents:



.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name='ProfDevelopment'>     
      <metadata>
        <displayName>Professional Development</displayName>   
        <className>iHRIS_Module_ProfDevelopment</className>
        <category>Site</category>
        <description>Adds in two new forms for tracking professional development</description>
        <version>3.1.4</version>
        <path name='classes'>
          <value>./lib</value>
        </path>
        <path name='templates'>
          <value>./templates</value>
        </path>
        <priority>325</priority>
      </metadata>
      
      <configurationGroup name='ProfDevelopment' path='/I2CE'>
        <displayName>Professional Development</displayName>
    
        <configurationGroup name='tasks' path='/I2CE/tasks/task_description' locale='en_US'>
          <configuration name='person_can_view_child_form_person_profdev'>
            <value>Can view person_profdev child form of a person</value>
          </configuration>
          <configuration name='person_can_edit_child_form_person_profdev'>
            <value>Can edit person_profdev child forms of a person</value>
          </configuration>
          <configuration name='person_can_view_child_form_person_continuous_profdev'>
            <value>Can view person_continuous_profdev child form of a person</value>
          </configuration>
          <configuration name='person_can_edit_child_form_person_continuous_profdev'>
            <value>Can edit person_continuous_profdev child forms of a person</value>
          </configuration>
        </configurationGroup>
        
        <configurationGroup name='tasks_trickle_down' path='/I2CE/tasks/task_trickle_down/'>
          <configuration name='person_can_view_child_form_person_profdev' values='many'> 
            <value>person_can_view</value>
          </configuration>
          <configuration name='person_can_edit_child_form_person_profdev' values='many'> 
            <value>person_can_view_child_form_person_profdev</value>
            <value>person_can_view</value>
          </configuration>
          <configuration name='person_can_view_child_form_person_continuous_profdev' values='many'> 
            <value>person_can_view</value>
          </configuration>
          <configuration name='person_can_edit_child_form_person_continuous_profdev' values='many'> 
            <value>person_can_view_child_form_person_continuous_profdev</value>
            <value>person_can_view</value>
          </configuration>
          <configuration name='person_can_view_child_forms' values='many'> 
    	 <value>person_can_view_child_form_person_profdev</value>
    	 <value>person_can_view_child_form_person_continuous_profdev</value>
          </configuration>
          <configuration name='person_can_edit_child_forms' values='many'> 
    	 <value>person_can_edit_child_form_person_profdev</value>
     	 <value>person_can_edit_child_form_person_continuous_profdev</value>
          </configuration>
        </configurationGroup>
    
        
        <configurationGroup name='forms' path='/modules/forms'>
          <displayName>Forms</displayName>
          <description>Information about the forms made available by ProfDevelopment</description>
          
          <configurationGroup name='forms'>
            <displayName>Forms available to the form factory</displayName>
            <status>advanced:true</status>
            <status>required:true</status>
    
            <!-- This section is to add a new form called person_profdev with the associated
                 class.  The class will be defined in the classes section below. -->
            <configurationGroup name='person_profdev'>
              <displayName>Person Professional Development</displayName>
              <description>The Person Professional Development Form</description>
              <configuration name='class' values='single'>
                <displayName>Class Name</displayName>
                <description>The name of the class providing the form</description>
                <value>iHRIS_PersonProfDevelopment</value>
              </configuration>
              <configuration name='display' values='single'>
                <displayName>Display name</displayName>
                <description>The display name for this form</description>
                <value>Person Professional Development</value>
              </configuration>
            </configurationGroup> <!-- person_profdev -->
    
            <!-- This section is to add a new form called person_continuous_profdev with the associated
                 class.  The class will be defined in the classes section below. -->
            <configurationGroup name='person_continuous_profdev'>
              <displayName>Person Continuous Professional Development</displayName>
              <description>The Person Continuous Professional Development Form</description>
              <configuration name='class' values='single'>
                <displayName>Class Name</displayName>
                <description>The name of the class providing the form</description>
                <value>iHRIS_PersonContinuousProfDev</value>
              </configuration>
              <configuration name='display' values='single'>
                <displayName>Display name</displayName>
                <description>The display name for this form</description>
                <value>Person Continuous Professional Development</value> 
              </configuration> 
            </configurationGroup> <!-- person_continuous_profdev -->
    
    
            <!-- This section will modify the existing information for the person form to include
                 two new child forms which are the new forms created for this module. -->
            <configurationGroup name='person_meta' path='/modules/forms/forms/person/meta'>
              <displayName>MetaData on the form</displayName>
              <configuration name='child_forms' values='many' > 
                <status>uniquemerge:true</status>
                <displayName>Child Forms</displayName>
                <value>person_profdev</value>
                <value>person_continuous_profdev</value>
              </configuration>
            </configurationGroup> <!-- person_meta -->
            
          </configurationGroup> <!-- End /modules/forms/forms-->
          
          
          <configurationGroup name="formClasses" >
            <displayName>Form Class Configuration</displayName>
    
    
            <!-- This section will define the person_profdev form class with all the fields and field types. 
                 This class will be created dynamically since no extra funcationality needs to be added for it. -->
            <configurationGroup name="iHRIS_PersonProfDevelopment">
              <displayName>Configuration for the class 'iHRIS_PersonProfDevelopment'</displayName>
              <configuration name="extends">
                <displayName>The class this form extends</displayName>
                <value>I2CE_Form</value>
              </configuration>
              <configurationGroup name="fields">
                <displayName>The fields defined for this form.</displayName>
    
                <configurationGroup name="year">
                  <displayName>The fields 'year'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>DATE_Y</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Year</value>
                  </configuration>
                  <configuration name="default_eval">
                    <displayName>The default value for this field as an eval() string</displayName>
                    <value>I2CE_Date::now()</value>
                  </configuration>
                </configurationGroup> <!-- year -->
                <configurationGroup name="course">
                  <displayName>The fields 'course'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Course</value>
                  </configuration>
                </configurationGroup> <!-- course -->
                <configurationGroup name="duration">
                  <displayName>The fields 'duration'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>INT</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Duration (in Days)</value>
                  </configuration>
                </configurationGroup> <!-- duration -->
                <configurationGroup name="certification">
                  <displayName>The fields 'certification'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Certification</value>
                  </configuration>
                </configurationGroup> <!-- certification -->
    
              </configurationGroup> <!-- fields -->
            </configurationGroup> <!-- iHRIS_PersonProfDevelopment -->
    
            <!-- This section will define the person_continuous_profdev form class with all the 
                 fields and field types. 
                 This class will be created dynamically since no extra funcationality needs to be added for it. -->
            <configurationGroup name="iHRIS_PersonContinuousProfDev">
              <displayName>Configuration for the class 'iHRIS_PersonContinuousProfDev'</displayName>
              <configuration name="extends">
                <displayName>The class this form extends</displayName>
                <value>I2CE_Form</value>
              </configuration>
              <configurationGroup name="fields">
                <displayName>The fields defined for this form.</displayName>
    
                <configurationGroup name="work_training_1">
                  <displayName>The fields 'work_training_1'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Training Priority 1</value>
                  </configuration>
                </configurationGroup> <!-- work_training_1 -->
                <configurationGroup name="work_training_2">
                  <displayName>The fields 'work_training_2'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Training Priority 2</value>
                  </configuration>
                </configurationGroup> <!-- work_training_2 -->
                <configurationGroup name="work_training_3">
                  <displayName>The fields 'work_training_3'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Training Priority 3</value>
                  </configuration>
                </configurationGroup> <!-- work_training_3 -->
    
                <configurationGroup name="personal_training_1">
                  <displayName>The fields 'personal_training_1'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Priority 1</value>
                  </configuration>
                </configurationGroup> <!-- personal_training_1 -->
                <configurationGroup name="personal_training_2">
                  <displayName>The fields 'personal_training_2'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Priority 2</value>
                  </configuration>
                </configurationGroup> <!-- personal_training_2 -->
                <configurationGroup name="personal_training_3">
                  <displayName>The fields 'personal_training_3'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <value>STRING_LINE</value>
                  </configuration>
                  <configuration name="headers" type="delimited">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Priority 3</value>
                  </configuration>
                </configurationGroup> <!-- personal_training_3 -->
    
              </configurationGroup> <!-- fields -->
           </configurationGroup> <!-- iHRIS_PersonContinuousProfDev-->
    
          </configurationGroup> <!-- End /modules/forms/formClasses -->
          
        </configurationGroup> <!-- End /modules/forms -->
        
        
        <configurationGroup name='page'>
          <displayName>Pages</displayName>
          <description>Information about various pages made available by the system</description>
          <status>required:true</status>
    
    
          <!-- This section will create the person_profdev page so that new professional development
               forms can be created and assigned to a person's record. -->
          <configurationGroup name='person_profdev'>
            <displayName>Person Professional Development Page</displayName>
            <description> The page 'person_profdev' which has the action of: Add/Update Professional Development</description>
            <configuration name='class' values='single'>
              <displayName>Page Class</displayName>
              <description>The class responsible for displaying this page</description>
              <status>required:true</status>
              <value>iHRIS_PageFormParentPerson</value>
            </configuration>
            <configuration name='style' values='single'>
              <displayName>Page Style</displayName>
              <description>The Page Style</description>
              <value>ihris_common_page_form_parent_person</value>
            </configuration>
            <configurationGroup name='args'>
              <displayName>Page Options</displayName>
              <description>The options that control the access and display of all pages</description>
              <configuration name='title' values='single'>
                <displayName>Page Title</displayName>
                <description>Page Title</description>
                <status>required:true</status>
                <value>Add/Update Professional Development</value>
              </configuration>
              <configuration name='page_form' values='single'>
                <displayName>Form</displayName>
                <description>The form this page is using</description>
                <status>required:true</status>
                <value>person_profdev</value>
              </configuration>
            </configurationGroup>
          </configurationGroup> <!-- person_profdev -->
    
          <!-- This section will create the person_continuous_profdev page so that a new continuous professional 
               development form can be created and assigned to a person's record. -->
          <configurationGroup name='person_continuous_profdev'>
            <displayName>Person Continuous Professional Development Page</displayName>
            <description> The page 'person_continuous_profdev' which has the action of: Add/Update Continuous Professional Development</description>
            <configuration name='class' values='single'>
              <displayName>Page Class</displayName>
              <description>The class responsible for displaying this page</description>
              <status>required:true</status>
              <value>iHRIS_PageFormParentPerson</value>
            </configuration>
            <configuration name='style' values='single'>
              <displayName>Page Style</displayName>
              <description>The Page Style</description>
              <value>ihris_common_page_form_parent_person</value>
            </configuration>
            <configurationGroup name='args'>
              <displayName>Page Options</displayName>
              <description>The options that control the access and display of all pages</description>
              <configuration name='title' values='single'>
                <displayName>Page Title</displayName>
                <description>Page Title</description>
                <status>required:true</status>
                <value>Add/Update Continuous Professional Development</value>
              </configuration>
              <configuration name='page_form' values='single'>
                <displayName>Form</displayName>
                <description>The form this page is using</description>
                <status>required:true</status>
                <value>person_continuous_profdev</value>
              </configuration>
            </configurationGroup>
          </configurationGroup> <!-- person_continuous_profdev -->
    
    
        </configurationGroup> <!-- page -->
        
        
      </configurationGroup> <!-- ProfDevelopment -->
    </I2CEConfiguration>
    
    



Step 2: Create the Module Class
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We need to create a new class in the lib directory called iHRIS_Module_ProfDevelopment.php with the following content.  This is so the new forms will show up on the view person page.


.. code-block:: php

    <?php
    class iHRIS_Module_ProfDevelopment extends I2CE_Module {
        public static function getMethods() {
            return array(
                'iHRIS_PageView->action_person_profdev' => 'action_person_profdev'
                'iHRIS_PageView->action_person_continuous_profdev' => 'action_person_continuous_profdev'
                );
        }
    
    
        public function action_person_profdev($obj) {
            if (!$obj instanceof iHRIS_PageView) {
                return;
            }
            return $obj->addChildForms('person_profdev', 'siteContent');
        }
        public function action_person_continuous_profdev($obj) {
            if (!$obj instanceof iHRIS_PageView) {
                return;
            }
            return $obj->addChildForms('person_continuous_profdev', 'siteContent');
        }
    }
    ?>
    


Copy the view.html template file from the ihris-manage templates directory to the site templates directory.  Make the following changes.  The changes are surround by comments.  This should be in the site in case multiple modules update the view.html template.



.. code-block:: html4strict

        <span task="person_can_edit_child_form_demographic" type="form" name="person:id" href="demographic?parent=" ifset="!demographic:id">Add Demographic Information</span>
      <!-- New professional development section for the Professional Development module -->    
        <span type='module' name='ProfDevelopment' ifenabled='true'>
          <span task="person_can_edit_child_form_person_continuous_profdev" type="form" name="person:id" href="person_continuous_profdev?parent=" ifset="!person_continuous_profdev:id">Add Continuous Professional Development</span>
        </span>
      <!-- End of Professional Development additions -->
    




.. code-block:: html4strict

      <div class="recordsData">
        <h3><a name="jump_qualification">Qualifications</a></h3>
        <p class="editRecordsData"><a href="" class="hide" title="Hide" onclick="return hideDiv('qualification', this);">Hide</a>
        <span role='hr_staff' type="form" name="person:id" href="person_language?parent=" text="Add Language Proficiency"></span>
        <span type='module' name='simple-competency' ifenabled='true'>
          <span role='hr_staff' type="form" name="person:id" href="person_competency?parent=">Add Competency</span>
          <span role='hr_staff' type="form" name="person:id" href="person_competency_history?parent=">Competency Evaluations</span>
        </span>
        </p>
        
        <div id="qualification">
          
          <div id="person_language" />
          <div id="person_competency" />
          
        </div> <!-- qualification -->
        
        <br style="clear: both;" />
      </div> <!-- recordsData -->
    
    
      <!-- New professional development section for the Professional Development module -->
      <span type="module" name="ProfDevelopment" ifenabled="true">
      <div class="recordsData">
        <h3><a name="jump_profdev">Professional Development</a></h3>
        <p class="editRecordsData" id="profdev_links"><a href="" class="hide" title="Hide" onclick="return hideDiv('profdev', this );">Hide</a>
        <span task='person_can_edit_child_form_person_profdev' type="form" name="person:id" href="person_profdev?parent=">Add Professional Development</span>
        </p>
    
        <div id="person_profdev"></div>
        <div id="person_continuous_profdev"></div>
        <br style="clear: both;" />	
      </div> <!--  recordsData -->
      </span>
      <!-- End of Professional Development additions -->
    


Copy the menu_view_person.html template file from the ihris-manage templates directory to the site templates directory.  Make the following changes:



.. code-block:: html4strict

    <li><a href="#jump_qualification" onclick="if(prevAnchor) prevAnchor.className=''; this.className='active'; prevAnchor=this;">Qualifications</a></li>
    <!-- Additions for the Professional Development module -->
    <span type="module" name="ProfDevelopment" ifenabled="true">
      <li><a href="#jump_profdev" onclick="if(prevAnchor) prevAnchor.className=''; this.className='active'; prevAnchor=this;">Professional Development</a></li>
    </span>
    <!-- End of additions -->
    



Step 3: Add in the Professional Development templates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the templates directory create the following files and contents:


view_person_profdev.html
~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: html4strict

    <div>
    	<div class="editRecord">
    	<p>Edit This Information</p>
    		<ul>
    			<li task='person_can_edit_child_form_person_profdev'><span type="form" name="person_profdev:id" href="person_profdev?id=" parent="true">Update this Information</span></li>
    		</ul>
    	</div> <!-- editRecord -->
    	
    	<div class="dataTable">
    	<table border="0" cellspacing="0" cellpadding="0">
    		<tr>
    		    <th colspan="2">Other Training</th>
    		</tr>
    		<span type="form" name="person_profdev:year" showhead="default"></span>
    		<span type="form" name="person_profdev:course" showhead="default" class="even"></span>
    		<span type="form" name="person_profdev:duration" showhead="default"></span>
    		<span type="form" name="person_profdev:certification" showhead="default" class="even"></span>
    	</table>
    	</div> <!-- dataTable -->
    </div>
    



form_person_profdev.html
~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: html4strict

    <tbody id="person_form">
    <tr>
        <th colspan="2">Other Training (of more than 7 days)</th>
    </tr>
    <tr>
    	<td>
    		<span type="form" name="person_profdev:year" showhead="default"></span>
    		<span type="form" name="person_profdev:course" showhead="default"></span>
    	</td><td>
    		<span type="form" name="person_profdev:duration" showhead="default"></span>
    		<span type="form" name="person_profdev:certification" showhead="default"></span>
        </td>
    </tr>
    </tbody>
    



view_person_continuous_profdev.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: html4strict

    <div>
          <div class="editRecord">
    	<p>Edit This Information</p>
    	<ul>
    	  <li role='person_can_edit_child_form_person_continuous_profdev'><span type="form" ifset="person_continuous_profdev:id" name="person_continuous_profdev:id" href="demographic?id=" parent="true">Update this Information</span></li>
    	</ul>
          </div> <!-- editRecord -->
          
          <div class="dataTable">
    	<table border="0" cellspacing="0" cellpadding="0">
    	  <tbody>
    	    <tr>
    	      <th colspan="2">Training needs that would improve everyday work</th>
    	    </tr>
    	   	<span type="form" name="person_continuous_profdev:work_training_1" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:work_training_2" showhead="default" class="even"></span>
    	   	<span type="form" name="person_continuous_profdev:work_training_3" showhead="default"></span>
            <tr>
              <th colspan="2">Training needs for personal development</th>
            </tr>
    	   	<span type="form" name="person_continuous_profdev:personal_training_1" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:personal_training_2" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:personal_training_3" showhead="default"></span>
    	  </tbody>
    	</table>
          </div> <!-- dataTable -->
    
    </div>
    



form_person_continuous_profdev.html
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: html4strict

    <tbody>
    <tr>
        <th>Training needs that would improve everyday work</th>
        <th>Training needs for personal development</th>
    </tr>
    <tr id="list_fields">
    	<td>
    	   	<span type="form" name="person_continuous_profdev:work_training_1" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:work_training_2" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:work_training_3" showhead="default"></span>
        </td>
        <td>
    	   	<span type="form" name="person_continuous_profdev:personal_training_1" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:personal_training_2" showhead="default"></span>
    	   	<span type="form" name="person_continuous_profdev:personal_training_3" showhead="default"></span>
        </td>
    </tr>
    </tbody>
    



Step 4: Enable the module in the site config file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Edit your site configuration file and add in the following line below any requirements and above the paths:



.. code-block:: xml

    <enable name="ProfDevelopment" />
    



[[Category:Developer Resources]]
