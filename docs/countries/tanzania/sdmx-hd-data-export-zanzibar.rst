SDMX-HD Data Export -- Zanzibar
===============================


Background Information
^^^^^^^^^^^^^^^^^^^^^^
iHRIS and DHIS are established systems in Zanzibar.  Each has independently maintained a list of facilities and districts on which data should be exchanged.   In addition iHRIS contains cadre, job  and gender lists on which health worker data is maintained.   In the case of Zanzibar, it was decided that exporting data at the level of job (approximately 200) provided the needed granularity for the expected data use.   In other cases, it may make sense to export on cadre -- in the case of Botswana there are 3500 jobs which is perhaps too granular for meaningful use for planners and decision/policy makers.


Expected Data Use Scenarios
~~~~~~~~~~~~~~~~~~~~~~~~~~~


* Computer *# of deliveries*  per *healthworker in job that delivers maternal child health services*



Where's the code
^^^^^^^^^^^^^^^^
There is a Launchpad  `team <https://launchpad.net/~zanzibar-his>`_  and  `project <https://launchpad.net/zanzibar-sdmx-hd>`_ .  The direct link to the source code is  `here <https://code.launchpad.net/~zanzibar-his/zanzibar-sdmx-hd/trunk>`_ . 

There are four main directories here and it is intended that these tools can be branch and readily adapted to other country/ministries.  There is a script "runme.php" which processes these four directories according to the following logic.


* inputs:  this contains a series of [[#.csv|Linking the Data]] files which are the data lists.  As an intermediary step, runme.php produces a file lists.xml which converts the .csv into a simple xml file for further XSLT processing.
* transforms:   The files here are used to generate the DSD, the xsd's and what other xml based files needed by the various systems.
* transforms_dsd.  This directory contains the XSL which will operate directly on the DSD.
* outputs -- this is where are the results are.  (Everything under here is bzr ignored)

CSV was chosen as it is easily to manipulate the links between the facilities in the various systems by *non-programmers.*   It is my goal that much of this be largely handled by the "data-steward" for the HIS.

Note, runme.php of this is setup to to work without any assumptions about about which systems are involved.  It can happily handle openMRS, iHRIS and DHIS all reporting on similar but not necessarily identical data.


Linking the Data
^^^^^^^^^^^^^^^^
Data lists are linked between the various systems by the .csv files in the inputs directory.  For example in inputs/facility.csv you have the columns:


* dhisid:  the id used in DHIS for the facility
* dhisname: the name used by dhis for the facility
* ihrisname: the name used by iHRIS for the facility
* ihrisid: the id used by iHRIS for the facility
* sdmxhdid:  the id used for sdmx-hd id.  for now it is simply the DHIS id as DHIS cannot handle (I think) aliasing of ids yet.
* comments: a place to keep track of the data linking process.  for example indicate where you are not sure if the linkage is correct.  we also indicate here that there are facilities in iHRIS which are not in DHIS -- this may be OK:  for example the MOH Headquarters would not have any service data.


lists.xml
^^^^^^^^^
As an intermediary step, runme.php converts the .csv files into one large .xml file for processing.  It has the structure:


.. code-block:: xml

    <Lists version='1.0' day='22' month='05' year='1977' timestampUnix='233166000' timestampMysql='blahblah'>
     <List name='facility'>
        <row>
          <field column="sdmxhdid">14</field>
          <field column="ihrisid">cadre|14</field>
          <field column="ihrisname">ACCOUNTING</field>
        </row>
       <row>
          <field column="sdmxhdid">14</field>
          <field column="ihrisid">cadre|14</field>
          <field column="ihrisname">ACCOUNTING</field>
        </row>
        <!-- blah blah blah -->
     </List>
     <List name='job'>
         <!-- blah blah blah -->
     </List>  
     <!-- blah blah blahbity blah -->
    </Lists>
    


Here:


* The version attribute of Lists is hard-coded into ./runme.php
* The rest of the attributes are based on the time that ./runme.php is run  (in iHRIS and the DSD we all of these attributes to version the modules)
* The name attribute used in the List element is produced by lopping off .csv from inputs/facility.csv
* The column attribute are simply the header columns in the respective .csv files


The DSD
^^^^^^^
This is generated from [[#lists.xml]] via the file:

* transforms/DSD/DSD.xml.xsl

The only thing that really needs to be done here is to change the KeyFamily.  If we can better  named KeyFamilies we can standardize them across all implementations.


Schema
^^^^^^
The DSD will define a KeyFamily.  The validator for exports via CrossSectionalDataSets is produced via:


* transforms/schemas/KF_135.xsd.xsl
The name of this file and its internals will need to be adjusted for future implementations to reflect the new Key Family name, until we have named KeyFamilies.


iHRIS
^^^^^
All the transforms and setup files are maintained in transforms/iHRIS.  There are three things to be done: 


* Make the SDMX-HD codelists available as lists in iHRIS
* Link existing list members in iHRIS to the SDMX-HD code lists
* Produce the export report.


Make the SDMX-HD Code Lists Available
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This is handled by creating a form for each of the code lists which maps iHRIS ids to SDMX-HD ids via the lists.xml file. 


* /transforms/iHRIS/iHRIS_ZNZ_CodeList/SDMX-HD/DSD.xml.xsl
* /transforms/iHRIS/iHRIS_ZNZ_CodeList/iHRIS_CodeList.xml.xsl
Note, the former is simply a link to DSD.xml.xsl above so that it can be reproduced in the outputs for iHRIS.

I don't think anything needs to be changed here for future implementations.


Linking the Code Lists
~~~~~~~~~~~~~~~~~~~~~~
The linkages for the codelists are handled by the files;
 transforms/iHRIS/CodeListLink_Cadre/CodeListLink_Cadre.xml.xsl
 transforms/iHRIS/CodeListLink_Facility/CodeListLink_Facility.xml.xsl
 transforms/iHRIS/CodeListLink_Job/CodeListLink_Job.xml.xsl
 transforms/iHRIS/CodeListLink_Gender/CodeListLink_Gender.xml.xsl
 transforms/iHRIS/CodeListLink_District/CodeListLink_District.xml.xsl

I don't think anything needs to be changed here for future implementations.



Producing the Reports
~~~~~~~~~~~~~~~~~~~~~
No transform needs to be processed here and the file:
 transforms/iHRIS/ZNZ_SDMXHD_Reports/SDMX_Reports.xml
is simply copied over by runme.pho to the outputs directory.  It contains the needed definitions for the relationship, report and report view.  Note there is, there an .xsl inside of the report which produces the CrossSectionalDataSet based on the iHRIS Data.

 **Warning:**  The linkage between people and facilities in the Zanzibar customizations is different than the usual.  Usually it goes:
 person -> person_position -> position -> facility
In Zanzibar, due to their business requirements, it goes:
 person -> person_position -> position -> facility_department -> facility
Thus, you will need to adjust the relationship defined here.

Also, if you are reporting on cadres instead of jobs, you will need to join in the cadre to the job form and change the report and report view accordingly.

For future implementations, until we can have sensibly named Key families, the KF_XXX references will need to be adjusted.


Finishing Up
~~~~~~~~~~~~
Copy the files under outputs/iHRIS into the modules directory of your site.  Then add something like the following to your site configuration .xml file:


.. code-block:: xml

       <requirement name="sdmxhd-reports">
          <atLeast version="1.0"/>
        </requirement>
        <requirement name="zanzibar-codelists">
          <atLeast version="1.0"/>
        </requirement>
        <requirement name="zanzibar-sdmx-hd-cl-link-cadre">
          <atLeast version="1.0"/>
        </requirement>
        <requirement name="zanzibar-sdmx-hd-cl-link-district">
          <atLeast version="1.0"/>
        </requirement>
        <requirement name="zanzibar-sdmx-hd-cl-link-facility">
          <atLeast version="1.0"/>
        </requirement>
        <requirement name="zanzibar-sdmx-hd-cl-link-gender">
          <atLeast version="1.0"/>
        </requirement>
        <requirement name="zanzibar-sdmx-hd-cl-link-job">
          <atLeast version="1.0"/>
        </requirement>
    

The resulting code for zanzibar is  `here <https://code.edge.launchpad.net/~ihris+zanzibar/ihris-manage-zanzibar/central-4.0>`_ .  You can install this easily enough your self, but you won't have the data lists nor the health worker data to get a meaningful report.


DHIS2
^^^^^

Issues to Address
^^^^^^^^^^^^^^^^^

* Unlike in the proof-of-concept for Sierra Leone, where we provided the DSD, the DSD was generated a DSD off of data coming from iHRIS and DHIS.  This presented some challenges on our side but all of which can be worked around and improved upon.  All data lists are in the **inputs**  sub-directory.
* A dxf import file is created  by transforming the DSD to import the "jobs" dataelements into dhis - doctor, nurse etc makingsure they all were part of an iHRIS-Staff data element group.  It makes sense that the iHRIS system would have the authoritative list of these.
* Rationalizing the orgunits is really important and potentially quite difficult with a large number of them.   We cannot risk overwriting or corrupting our dhis orgunit hierarchy so these must be agreed upon first.  There are a few possibilities here:

  * Ideally the codelist for facilities should probably be maintained by a 3rd system or one or other systems deemed authoritative.
  * In future implementations,  we can have dhis act as the authoritative reference - ie. start the process by exporting dhis orgunits and compare with what is in iHRIS.  Fix iHRIS and/or DHIS to
make sure these are matching.  


  * iHRIS does not care about the org units as represented in iHRIS and reports out only on the most granular level in common with DHIS.
  * iHRIS can already maintain distinct hierarchical relationships among the same data.   For example, we do so with the geographical data with the Christian Social Services Commission as they need to organize by both under the administrative groupings as well as the diocese.   If needed/useful we can readily import the DHIS hierarchies into iHRIS.
* In Zanzibar we agreed to report job dataelement disaggregated by gender (Male, Female or Unknown).  For the moment the sdmx dsd is using the DHIS codelist values for these which shouldn't strictly have to be the case but it was easier for me this way for now.  It's not really critical, but it should be improved in that involves some manual fiddling at the moment.
* Currently we have a constraint on the naming of the keyfamily used in the DSD.  This is historical.  We name it things like KF_345 where 345 is a categorycombo in dhis.  That's fairly ugly and also should and will be improved, but it is not a showstopper.  Ideally it would be something like KF_HW_BY_FAC_JOB_GEN  or KF_HW_BY_FAC_CADRE_GEN.  In any case something a bit more descriptive.
* For historical reasons, we are only currently importing monthly periods.  We should generalize that to support other sdmx period types - such as quarterly.

The question of authority for codelists is most important.  In the absence of an authoritative 3rd party, the DSD (structural metadata definition) must be created with some
peer-to-peer collaboration between two or perhaps more systems. In our case iHRIS provided the jobs dataelements and we provided the orgunits and the gender disaggregation codes.  We obviously want to reduce that as far as possible, both to make scenarios more easily replicable and to better enjoy the advantages of having a standard.  But we are on the way.

Provided we don't have major headaches with incompatible facility lists (Kenya for example has many more than Zanzibar - 7877) we will get the data exchange working and hopefully improve a bit of process along the way.


