Modifying Form and Field Headers
================================

This tutorial will explain how to modify your site configuration file to change the default headers for forms and fields for your site.  All this data is saved in configuration options (magic data).  For this example we're going to change the headers for County to display Sub-District instead.


Step 1: Changing the form's display name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First we need to change the display name for this form.  If you have a forms section in your site configuration file you can add this section there.  Or by using the path attribute you can add the configurationGroup to the top level of your site config.



.. code-block:: xml

    <configuration name='county_display' values='single' path='/modules/forms/forms/county/display'>
      <displayName>Display Name</displayName>
      <description>The display name for this form.</description>
      <status>overwrite:true</status>
      <value>Sub-District</value>
    </configuration>
    



Step 2: Override the field headers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we need to override the default field headers for all the form classes that use county.  If you have any custom forms you would need to include them here as well.



.. code-block:: xml

    <configurationGroup name='formClasses' path='/modules/forms/formClasses'>
      <status>overwrite:true</status>
    
      <configurationGroup name='iHRIS_ListByCountry'>
        <configuration name="county_headers" path="fields/county/headers/default">
          <value>Sub-District</value>
        </configuration>
      </configurationGroup>
    
      <configurationGroup name='iHRIS_County'>
        <configurationGroup name='fields'>
          <configuration name="country_headers" path="country/headers" type="delimited" values="many">
            <value>select_county:Select Country, Region, District then Sub-District</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    
      <configurationGroup name="iHRIS_Person">
        <configuration name="res_count_headers" path="fields/residence_county/headers/default">
          <value>Residence Sub-District</value>
        </configuration>
      </configurationGroup>
    
    </configurationGroup>
    



Step 3: Modify the Administer Database template
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copy the lists.html file from iHRIS Manage or iHRIS Qualify to your site's templates directory.  Edit the line in the Geography section to change the link text to Sub-District instead of County.  Don't change the type attribute in the href because the form name is still county.  Only the display has changed.  Now copy lists_county.html from the iHRIS Common Geography modules templates to your site templates directory.  Change the link that says "Add new County" to "Add new Sub-District."


Step 4: Reload your site
^^^^^^^^^^^^^^^^^^^^^^^^

Now the form and field headers should be changed.


[[Category:Developer Resources]]
