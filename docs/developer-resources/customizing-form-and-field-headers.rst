Customizing Form and Field Headers
==================================

Field Headers
^^^^^^^^^^^^^
You can customize the headers for a form field by updating the magic data associated with the headers.  You can do this through the magic data browser, but the best way is to make the change in a module for your site or in your site configuration file.  Headers are at the magic data location:  /modules/forms/formClasses/'''$formClass'''/fields/'''$field'''/headers/'''$headerType'''

In your site or module configuration file, you can change the headers by adding the following lines:

.. code-block:: xml

    <configuration name="custom_headers" path="/modules/forms/formClasses/$formClass/fields/$field/headers/$headerType" locale="en_US">
      <value>$newHeader</value>
    </configuration>
    

For example, to change the header of the region field in districts you can do this:

.. code-block:: xml

    <configuration name="region_header" path="/modules/forms/formClasses/iHRIS_District/fields/region/headers/default" locale="en_US">
      <value>State</value>
    </configuration>
    

In most cases you'll use the "default" as the **$headerType** .  If you want to have multiple headers, then change the header type and in the template that is displaying your field set the **$headerType**  as the value for the showhead attribute.

.. code-block:: html

    <span type="form" name="$form:$field" showhead="$headerType"></span>
    

Replace $form, $field and $headerType with the appropriate values for your template.  For example:

.. code-block:: html

    <span type="form" name="country:name" showhead="my_header"></span>
    

Form Display Names
^^^^^^^^^^^^^^^^^^
You may also want to change the display name associated with a form.  You can do this by changing the magic data at /modules/forms/forms/'''$form'''/display.  You can make this change in your site or module configuration file.

.. code-block:: xml

    <configuration name="form_display" path="/modules/forms/forms/$form/display" locale="en_US">
      <value>$newHeader</value>
    </configuration>
    

For example, to change the display name for region to be State:

.. code-block:: xml

    <configuration name="region_display" path="/modules/forms/forms/region/display" locale="en_US">
      <value>State</value>
    </configuration>
    

Some templates (like lists.html) may refer to the name in the template directly.  You'll also need to modify this template to use the name you wish when linking to editing the database list for that form.

Geography Example
^^^^^^^^^^^^^^^^^
Here's a complete example that you can add to your site's [[Module Structure#Module Configuration File|configuration]] .xml file.  It will change the names of the levels of geography to be Country/State/Council/Town or City.  Country will stay the same, region will become State, district will become Council and county will be come Town or City.  You will need to change the **<version>4.0.XXX</version>**  as appropriate (see [[Configuration (Magic) Data#<version> | versions]]).

.. code-block:: xml

    <configurationGroup name="forms_module" path="/modules/forms">
      <!-- Update display names for forms -->
      <version>4.0.XXX</version>
      <configurationGroup name="forms">
        <configuration name="region_display" path="region/display" locale="en_US">
          <value>State</value>
        </configuration>
        <configuration name="district_display" path="district/display" locale="en_US">
          <value>Council</value>
        </configuration>
        <configuration name="region_display" path="county/display" locale="en_US">
          <value>Town or City</value>
        </configuration>    
      </configurationGroup>
      <!-- Update field headers for formClasses -->
      <configurationGroup name="formClasses">
        <configuration name="district_region_header" path="iHRIS_District/fields/region/headers/default" locale="en_US">
          <value>State</value>
        </configuration>
        <configuration name="country_district_header" path="iHRIS_County/fields/district/headers/default" locale="en_US">
          <value>Council</value>
        </configuration>
      </configurationGroup>
    </configurationGroup>
    
    

Editing lists.html
^^^^^^^^^^^^^^^^^^
As mentioned above, some .html template files refer to the form's name directly and will need to be edited.  You will want to copy the existing lists.html from the iHRIS Manage (or iHRIS Qualify) module to the templates directory in your sites module.  You will then edit this new copy.  For example you may do:
 sudo mkdir -p /var/lib/iHRIS/sites/'''my_site'''/templates/en_US
 sudo cp /var/lib/iHRIS/lib/'''4.0.4'''/ihris-manage/templates/en_US/lists.html /var/lib/iHRIS/sites/'''my_site'''/templates/en_US
 sudo gedit /var/lib/iHRIS/sites/'''my_site'''/templates/en_US
where you replace **4.0.4**  with the appropriate version and **my_site**  the name of the directory that your site is stored in.  

Once gedit appears, you will need to change the names of the forms.  For example:

.. code-block:: xml

      <li task="can_edit_database_list_county"><a href="lists?type=county&amp;field=district">County</a></li>
    

becomes:

.. code-block:: xml

     <li task="can_edit_database_list_county"><a href="lists?type=county&amp;field=district">Town or City</a></li>
    
    

