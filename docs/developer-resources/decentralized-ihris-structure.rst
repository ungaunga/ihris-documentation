Decentralized iHRIS Structure
=============================

iHRIS Manage or iHRIS Qualify can be implemented in a decentralized environment using the different data models: *2-, 3-, n-tier' data models* .

The following article gives the overview to setting up the decentralized structure of iHRIS Manage. The same structure can also be applied for iHRIS Qualify.

You may need to review [[Decentralized iHRIS Data Policy|the decentralized data policy]] and [[Managing A Site In Launchpad|Managing a site in Launchpad]] should you need the technicalities of managing a site in Launchpad. 

There is also a sister review [[Exporting Standardized Data|here]] describing the process of exporting standardized data lists into modules and a bit of [[Exporting Standardized Data#Managing Decentralized iHRIS with Launchpad|managing decentralized iHRIS with Launchpad]].


Background
^^^^^^^^^^
The need to have a decentralized iHRIS structure comes from the point that, personnel data needs to be reported to the central government (the ministry of health in this case) for planning and decision making including to meet the needs in deployment, tracking personnel movement and decisions of the type and quantity of training.

Paper work has been very slow and inaccurate. Human Resource Information Systems in this case should be able to address these issues.

As different Health Facilities and different administrative levels have different data needs, the Human Resource Information Systems for Health have to meet these different administrative needs at same time contributing to the goal of improved efficiency and productivity in dealing with Human Resource for Health issues.


Source Code Organization
^^^^^^^^^^^^^^^^^^^^^^^^
The way the source codes are organized will help meet the different administrative levels data needs. At least each level has to have its own <span style="color:blue">site configuration</span> which makes it easier to create  `form storage mechanisms <http://wiki.ihris.org/wiki/Technical_Overview:_Form_Storage_Mechanisms>`_  on how different forms are being handled at that particular administrative level or health facility.

''We are going to work on a 2-tier Data Model where we have the <span style="color:blue">central (NATIONAL) site</span> and a <span style="color:blue">local (REGIONAL) site.</span>

 *Let's assume the country is called Ilolo and there is one local site called Ikanga* 

The following is the directory layout for the complete decentralized iHRIS Manage for deployment in a particular country. You can read about the general directory structure of iHRIS Suite  `here <http://wiki.ihris.org/wiki/Tutorial:_Customizing_iHRIS_Manage#iHRIS_Package_Directory_Structure>`_ .

 *This directory structure is going to be under **/var/lib/iHRIS/ilolo/dev/**  * 



* <span style="color:blue">'''css'''</span>: this directory holds system wide customized cascading style sheets. If at all it is the theme that has changed or there are special text effects that apply apart from the default iHRIS Manage CSS, those edited files should be saved in this directory.
* <span style="color:blue">'''images'''</span>: this holds all the images including Logo,  `favorite icon <http://en.wikipedia.org/wiki/Favicon>`_  (''favicon'') or images displayed in PDF Reports should all be saved here.
* <span style="color:blue">'''lib'''</span>: the lib directory is where all the system specific classes are being saved. If something has been changed for example: how passport images should be handled for this specific implementation, that PHP file has to be saved here.
* <span style="color:blue">'''modules'''</span>:this is the main modules directory which will contain all of the modules required by each of the sites including all the standardized data lists modules.
* *<span style="color:blue">'''RegionsList'''</span>: this is the module which has the standardized regions list. This is going to be required by both the central and the local sites.
* <span style="color:blue">'''pages'''</span>: the directory that contains the main site initialization files: config.values.php for database and user options and index.php the default file that loads the whole system.
* <span style="color:blue">'''scripts'''</span>: any javascript/mootools scripts should be saved in here that apply for the whole system. some may be required by a specific site though.
* <span style="color:blue">'''sites'''</span>: the sites directory holds the main two sites directories in this case **the central site**  and **the local site**  each of which will have a complete directory structure like this one being described here except it won't have another sites directory for a 2-tier data model.
* *<span style="color:#D47171">'''central'''</span>: the main central site directory which holds all the files specific for the central site.
* **<span style="color:#DE9090">'''modules'''</span>: all the modules specific to the central site should be saved here including the Form Storage Mechanism (''Data Policy'') for the central site
* ***<span style="color:#E6ADAD">'''FormStorage'''</span>:the form storage module is saved here as  `CentralFormStorage.xml <http://bazaar.launchpad.net/~ihris-tanzania/pmoralg/aggregate/view/head:/sites/central/modules/formStorage/FormStorage_National.xml>`_
* **<span style="color:#DE9090">'''pages'''</span>:the directory that contains the main central site initialization files: <span style="color:green">config.values.php</span> for database and user options and <span style="color:green">index.php</span> the default file that loads the whole system and the <span style="color:green">htaccess.TEMPLATE</span>.
* *<span style="color:#D47171">'''local'''</span>:the main local site directory which holds all the files specific for the local site.
* **<span style="color:#DE9090">'''modules'''</span>:all the modules specific to the local site should be saved here including the Form Storage Mechanism (''Data Policy'') for the local site
* ***<span style="color:#E6ADAD">'''FormStorage'''</span>:the form storage module is saved here as  `LocalFormStorage.xml <http://bazaar.launchpad.net/~ihris-tanzania/pmoralg/aggregate/view/head:/sites/lga/modules/FormStorage/lga_form_storage.xml>`_
* **<span style="color:#DE9090">'''pages'''</span>:the directory that contains the main local site initialization files: <span style="color:green">config.values.php</span> for database and user options and <span style="color:green">index.php</span> the default file that loads the whole system and the <span style="color:green">htaccess.TEMPLATE</span>.
* <span style="color:blue">'''templates'''</span>: all the templates (''.html'') files in different locales that apply system wide should be saved in this directory. *e.g. the welcome.html*
* <span style="color:blue">'''tools'''</span>: this is an optional directory which contains tools like import scripts if any*


Data Policies
^^^^^^^^^^^^^
The Data policy defines how different data forms are going to be handled at the two sites.  `Form Storage Mechanisms <http://wiki.ihris.org/wiki/Technical_Overview:_Form_Storage_Mechanisms>`_  control how data editing at the central and local sites should be carried out.
In this regard therefore, it is obvious that the central site should not be able to edit the personnel data like names, demographic information, training information, etc. while, all the local sites should not be able to edit standardized data lists as these help to ease the process of aggregating and filtering the aggregated at the central site.

Central site data policy
~~~~~~~~~~~~~~~~~~~~~~~~
A sample configuration of the form storage mechanism module for the central site. **CentralFormStorage.xml** 


.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="ihris-manage-central-form-storage">
      <metadata>
        <displayName>iHRIS Manage</displayName>
        <category>Site</category>
        <description>the iHRIS Manage Central Form Storage</description>
        <creator>Sovello Hildebrand Mgani</creator>
        <email>sovellohpmgani@gmail.com</email>
        <link>https://launchpad.net/ihris+ghana</link>
        <version>4.0.15.0</version>
        <requirement name="forms-storage-multiflat">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
      </metadata>
      <configurationGroup name='ihris-manage-central-form-storage' path='/'>
        <configurationGroup name='form_storage' path='/modules/forms/forms'>
          <configuration name='multi_flat_componentized'   path='/modules/forms/storage_options/multi_flat/componentized'>
    	<value>1</value>
          </configuration>
          <configurationGroup name='multi_flat_components' path='/modules/forms/storage_options/multi_flat/components'>
    
          <!-- a list of all the databases being aggregated at the at the central site should be added here-->
    
    	<configuration name='ikanga' values='many' type='delimited'>
    	 <version>4.0.15.0</version>
    	 <value>database:ihris_manage_ikanga</value>
    	</configuration>
    
          <configurationGroup name='region'>
            <configuration name='storage'>
              <value>magicdata</value>
            </configuration>
          </configurationGroup>
          <!-- We need to repeat the read-write magic data storage for each of the forms we are maintaining at the central site-->
    
          <configurationGroup name='person'>
            <configuration name='storage'>
              <version>4.0.15.0</version>
              <value>multi_flat</value>
            </configuration>
          </configurationGroup>
          <!-- We need to repeat the multi_flat storage for each of the forms we are aggregating from the local site -->
    
          </configurationGroup>
        </configurationGroup>
      </configurationGroup>
    </I2CEConfiguration
    


Local site data policy
~~~~~~~~~~~~~~~~~~~~~~
A sample configuration of the form storage mechanism module for the local site. **LocalFormStorage.xml** 


.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="ihris-manage-local-form-storage">
      <metadata>
        <displayName>iHRIS Manage</displayName>
        <category>Site</category>
        <description>the iHRIS Manage Local Form Storage</description>
        <creator>Sovello Hildebrand Mgani</creator>
        <email>sovellohpmgani@gmail.com</email>
        <link>https://launchpad.net/ihris+ghana</link>
        <version>4.0.15.0</version>
      </metadata>
      <configurationGroup name='ihris-manage-local-form-storage' path='/'>
        <configurationGroup name='form_storage' path='/modules/forms/forms'>
    
    
          <configurationGroup name='region'>
            <configuration name='read_only' >
              <value>1</value>
            </configuration>
            <configuration name='storage'>
              <value>magicdata</value>
            </configuration>
          </configurationGroup>
          <!-- We need to repeat the read_only storage for each of the forms we maintain at the central site site -->
    
          <configurationGroup name='person'>
            <configuration name='storage'>
              <value>entry</value>
            </configuration>
          </configurationGroup>
    
        </configurationGroup>
      </configurationGroup>
    </I2CEConfiguration
    

 **Note:**  the storage of the other forms at the local site depends on what we want of them by  `making a reference <http://wiki.ihris.org/wiki/Technical_Overview:_Form_Storage_Mechanisms>`_  to the description of the different form storage mechanisms available.

Site Configurations
^^^^^^^^^^^^^^^^^^^

General site configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~
The is the module that contains all of the requirements, html templates, etc. which are common to the national and regional sites. In particular, it requires the module **regions**  (''assuming the name of the regions standard list is **regions**  '') **iHRIS-Manage-ILOLO.xml** 



.. code-block:: xml

     <?xml version="1.0"?>
     <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
     <I2CEConfiguration name='ihris-manage-ILOLO'>     
       <metadata>
         <displayName>iHRIS Manage Ilolo</displayName>   
         <category>Site</category>
         <description>the iHRIS Manage customizations for ILOLO that apply across central and local offices</description>
         <creator>Sovello Hildebrand Mgani</creator>
         <email>sovellohpmgani@gmail.com</email>
         <link>https://launchpad.net/ihris+ghana</link>
         <version>4.0.18.0</version>
         <requirement name='ihris-manage'>
           <atLeast version='4.0'/>
           <lessThan version='4.1'/>
         </requirement>
         <requirement name='regions'>
           <atLeast version='4.0'/>
           <lessThan version='4.1'/>
         </requirement>
         <!-- you should create a XXXXs module for each form XXXX that is being standardized.  It should be required here-->
         <path name='templates'> 
           <value>./templates</value> 
         </path>
         <path name='images'>
           <value>./images</value>
         </path>
         <priority>400</priority>
       </metadata>
       <configurationGroup name="ihris-manage-ILOLO" path="I2CE">
       </configurationGroup>
     </I2CEConfiguration>
    



Central site configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~
This has to require the ihris-manage-ILOLO and the ihris-manage-central-form-storage modules
 **iHRIS-Manage-CENTRAL.xml** 



.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="ihris-manage-central-site">
      <metadata>
        <displayName>iHRIS Manage</displayName>
        <category>Site</category>
        <description>the iHRIS Manage CENTRAL Site</description>
        <creator>Sovello Hildebrand Mgani</creator>
        <email>sovellohpmgani@gmail.com</email>
        <link>https://launchpad.net/ihris+ghana</link>
        <version>4.0.18.0</version>
        <path name="configs">
          <value>./configs</value>
        </path>
        <requirement name="ihris-manage-ILOLO">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
        <requirement name="ihris-manage-central-form-storage">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
        <requirement name="i2ce-site">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
        <path name="modules">
          <value>/var/lib/iHRIS/ilolo</value>
          <value>./modules</value>
        </path>
      </metadata>
      <configurationGroup name="ihris-manage-central-site" path="/">
        <configurationGroup name="pdf_options" path="/modules/report-pdf/PDF/display-options">
          <displayName>PDF Options</displayName>
          <status>visible:false</status>
          <configurationGroup name="header">
            <displayName>Header Options</displayName>
            <configuration name="text" locale="en_US">
              <displayName>Header Text</displayName>
              <value>iHRIS Manage Central</value>
            </configuration>
          </configurationGroup>
        </configurationGroup>
      </configurationGroup>
    </I2CEConfiguration>
    


Local site configuration
~~~~~~~~~~~~~~~~~~~~~~~~
This has to require the ihris-manage-ILOLO and the ihris-manage-local-form-storage modules **iHRIS-Manage-LOCAL.xml** 


.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="ihris-manage-local-site">
      <metadata>
        <displayName>iHRIS Manage</displayName>
        <category>Site</category>
        <description>the iHRIS Manage Local Site</description>
        <creator>Sovello Hildebrand Mgani</creator>
        <email>sovellohpmgani@gmail.com</email>
        <link>https://launchpad.net/ihris+ghana</link>
        <version>4.0.18</version>
        <path name="configs">
          <value>./configs</value>
        </path>
        <requirement name="ihris-manage-ILOLO">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
        <requirement name="ihris-manage-local-form-storage">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
        <requirement name="i2ce-site">
          <atLeast version="4.0" />
          <lessThan version="4.1" />
        </requirement>
        <path name="modules">
          <value>/var/lib/iHRIS/ilolo</value>
          <value>./modules</value>
        </path>
      </metadata>
      <configurationGroup name="ihris-manage-local-site" path="/">
        <configurationGroup name="pdf_options" path="/modules/report-pdf/PDF/display-options">
          <displayName>PDF Options</displayName>
          <status>visible:false</status>
          <configurationGroup name="header">
            <displayName>Header Options</displayName>
            <configuration name="text" locale="en_US">
              <displayName>Header Text</displayName>
              <value>iHRIS Manage Local</value>
            </configuration>
          </configurationGroup>
        </configurationGroup>
      </configurationGroup>
    </I2CEConfiguration>
    


[[Category:Developer Resources]]
