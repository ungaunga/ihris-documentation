Display Mapped Field From a Report
================================================

Some mapped fields may have a complicated view based on a tree view display that may take a long time to display when there is a lot of data and many different elements to display.  This most often happens when you map to the facility form as a tree view allowing selection through country, region (state), district, etc.  This How To will show you how to link this display to a report for faster display.

There are two options.  One is to keep the tree view and link it to a report to build the tree from.  The second is to use the report selector option to allow the user to view the entire report and select the value from the report itself which allows limits for easier selection.  The report selection will not display when the field is used as a limit in another report however.

=Using a Report to Build the Tree View=

Two example modules have been created to use reports to build the tree view.  `ihris-manage-FacilityTree <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/files/head:/modules/ManageFacilityTree/>`_ and `ihris-manage-PositionTree <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/files/head:/modules/ManagePositionTree/>`_.

A few things to note when creating a report to be used for field tree views:

* The i2ce_hidden fields must be included so the appropriate limit can be used for the display.
* Any other fields used when limiting the display also need to be included.
* The ID fields are included by default, but it is good practice to select them for the report so anyone looking at the report will see they are selected.
* Any fields used for linking should also be enabled, e.g. the region field for district.
* Any fields used for creating the display of the form need to be included, e,g, the position display includes the code field.
* To limit the values for selection based on user roles (for example using the ManageAccessFacility module) then the report definition needs to include the appropriate links to the module limits when being created.


Facility Tree Module
^^^^^^^^^^^^^^^^^^^^
The facility tree report can be used for any field mapped to the facility form.  The module does this for the position facility field.  The default display for this field is set to **facility+location:county:district:[region]:country**.  This tells iHRIS to build a tree view for this field so the user can select country, district, county and then the facility so the list isn't so large.  The region must also be included, but is hidden by including it in brackets so it won't be shown in the list, but is required so iHRIS knows which country the district is in.

To replace this with a report query we need to set the display_report meta information for the field and build the report to be used.

 **Note: Don't forget to include version number if you're updating an existing module.**

Here is the example from the Facility Tree module:



.. code-block:: xml

        <configurationGroup name="facility_meta_tree" path="/modules/forms/formClasses/iHRIS_Position/fields/facility/meta/display_report/default">
          <configuration name="report" values="single">
            <value>facility_tree</value>
          </configuration>
          <configuration name="map" type="delimited" values="many">
            <value>facility+location:primary_form</value>
          </configuration>
        </configurationGroup>
    


First we set the report to be used to be **facility_tree**.  Then we need to define what the form alias is in the relationship if it is different based on the display data.  The display uses **facility+location** to link to the county (or district) forms.  The report won't have this so we set the map meta data to link the **facility+location** information from the display the **primary_form** of the report.  The others (county, district, region and country) already match the names used in the report.

The report view will also sort based on the default sort of the forms included.  This means the districts will be sorted by region first since that is the default sort for districts.  We can change this just for this field by adding the following to a module (this is already in the Facility Tree module):



.. code-block:: xml

        <configurationGroup name="facility_meta_orders" path="/modules/forms/formClasses/iHRIS_Position/fields/facility/meta/display/orders/default">
          <configuration name="district" type="delimited">
            <value>0:name</value>
          </configuration>
        </configurationGroup>
    



Facility Tree Report
~~~~~~~~~~~~~~~~~~~~
The report must also be defined.  The Facility Tree module defines the relationship **facilty_tree** and the report **facility_tree**.  Refer to the `module <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/view/head:/modules/ManageFacilityTree/ManageFacilityTree.xml>`_ for the specifics of this report.



Position Tree Module
^^^^^^^^^^^^^^^^^^^^
The position tree report can be used for any field mapped to the position form.  The module does this for the position supervisor field.  The default display for this field is set to **position:facility+location:county:district:division:region:country**.  This tells iHRIS to build a tree view for this field so the user can select country, district, county, facility and then the position so the list isn't so large.  The region must also be included, but is hidden by including it in brackets so it won't be shown in the list, but is required so iHRIS knows which country the district is in.

To replace this with a report query we need to set the display_report meta information for the field and build the report to be used.

 **Note: Don't forget to include version number if you're updating an existing module.**

Here is the example from the Position Tree module:



.. code-block:: xml

        <configurationGroup name="position_meta_tree" path="/modules/forms/formClasses/iHRIS_Position/fields/supervisor/meta/display_report/default">
          <configuration name="report" values="single">
            <value>position_tree</value>
          </configuration>
          <configuration name="map" type="delimited" values="many">
            <value>position:primary_form</value>
            <value>facility+location:facility</value>
          </configuration>
        </configurationGroup>
    


First we set the report to be used to be **position_tree**.  Then we need to define what the form alias is in the relationship if it is different based on the display data.  The display has the **position** form, but since this is the primary form in the report it needs to be mapped to **primary_form**.  The display also uses **facility+location** to link to the county (or district) forms.  The report won't have this so we set the map meta data to link the **facility+location** information from the display the **facility** of the report.  The others (county, district, region and country) already match the names used in the report.

The report view will also sort based on the default sort of the forms included.  This means the districts will be sorted by region first since that is the default sort for districts.  We can change this just for this field by adding the following to a module (this is already in the Position Tree module):



.. code-block:: xml

        <configurationGroup name="position_meta_orders" path="/modules/forms/formClasses/iHRIS_Position/fields/supervisor/meta/display/orders/default">
          <configuration name="district" type="delimited">
            <value>0:name</value>
          </configuration>
        </configurationGroup>
    



Position Tree Report
~~~~~~~~~~~~~~~~~~~~
The report must also be defined.  The Position Tree module defines the relationship **position_tree** and the report **position_tree**.  Refer to the `module <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/view/head:/modules/ManagePositionTree/ManagePositionTree.xml>`_ for the specifics of this report.

=Using a Report Selector for the Field Display=

If you don't want to have a tree view, you can also use a report selector for the mapped field selection.  This will allow the user to select the value for the field from a report instead of from the default drop down or tree view.  This option won't be used if the field is a limit in another report.  The report displays will be limited based on any module limits that are linked for the report.  Any limits will also be displayed for easier selection by the user.  

First you need to update the field meta data to show which report should be used:



.. code-block:: xml

        <configurationGroup name="facility_field" path="iHRIS_Position/fields/facility">
          <displayName>Configuration for the facility field for iHRIS_Position</displayName>
          <configurationGroup name="meta">
            <configurationGroup name="reportSelect">
              <configurationGroup name="default">
                <configuration name="reportView">
                  <value>facility_selector_limited</value>
                </configuration>
              </configurationGroup>
              <configurationGroup name="full">
                <configuration name="reportView">
                  <value>facility_selector_full</value>
                </configuration>
              </configurationGroup>
            </configurationGroup>
            <configurationGroup name="display">
              <configurationGroup name="reportSelect">
                <configuration name="enabled" type="boolean">
                  <value>true</value>
                </configuration>
              </configurationGroup>
              <configurationGroup name="facility">
                <configurationGroup name="default">
                  <configuration name="printf" locale="en_US">
                    <value>%s (%s)</value>
                  </configuration>
                  <configuration name="printf_args" values="many" type="delimited">
                    <value>0:name</value>
                    <value>1:location</value>
                  </configuration>
                </configurationGroup>
                <configurationGroup name="full">
                  <configuration name="printf" locale="en_US">
                    <value>%s (%s)</value>
                  </configuration>
                  <configuration name="printf_args" values="many" type="delimited">
                    <value>0:name</value>
                    <value>1:location</value>
                  </configuration>
                </configurationGroup>
               </configurationGroup>
            </configurationGroup>
          </configurationGroup>
        </configurationGroup> <!-- end facility_field -->
    


Note that you can define multiple reportSelect reports to be used.  See below for how to select which report.  You also need to enable reportSelect in the meta display information.  And finally you need to define how the field will be displayed once selected.  You will need to define this for each reportSelect type you have.  In this example, **default** and **full**.

To enable the report selection you need to modify the template to tell the form span to use the report selector:



.. code-block:: html

    <span type="form" name="position:facility" showhead="default" display="reportSelect"></span>
    


You can also define a second report to be used if one needs different limits.  Instead of the **default** report as defined, you can use the report defined as **full**.



.. code-block:: html

    <span type="form" name="position:facility" showhead="default" display="reportSelect" show="full"></span>
    


For this example, you would also need to create the **facility_selector_limited** and **facility_selector_full** reports.  In this example the limited report would be limited by any user module requirements, but the full report would not since not all forms and fields would need the limits depending on what data is being chosen.  Current data would need to be limited, but historical data may not.  If you don't need the full selection, you could also use the **facility_tree** report that is defined in the iHRIS Manage Facility Tree module.

[[Category:Fields]][[Category:Reports]][[Category:Review2013]]
