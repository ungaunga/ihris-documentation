Customizing Field Headers
=========================

==Field Headers==
You can customize the headers for a form field by updating the magic data associated with the headers.  You can do this through the magic data browser, but the best way is to make the change in a module for your site or in your site configuration file.  Headers are at the magic data location:  /modules/forms/formClasses/'''$formClass'''/fields/'''$field'''/headers/'''$headerType'''

In most cases you'll use the "default" as the '''$headerType'''.  If you want to have multiple headers, then change the header type and in the template that is displaying your field set the '''$headerType''' as the value for the showhead attribute.
<source lang="html4strict">
<span type="form" name="$form:$field" showhead="$headerType"></span>
</source>
Replace $form, $field and $headerType with the appropriate values for your template.  For example:
<source lang="html4strict">
<span type="form" name="country:name" showhead="my_header"></span>
</source>

In your site or module configuration file, you can change the headers by adding the following lines:
<source lang="xml">
<configuration name="custom_headers" path="/modules/forms/formClasses/$formClass/fields/$field/headers/default">
  <value>$newHeader</value>
</configuration>
</source>
For example, to change the header of the region field in districts you can do this:
<source lang="xml">
<configuration name="region_header" path="/modules/forms/formClasses/iHRIS_District/fields/region/headers/default">
  <value>State</value>
</configuration>
</source>

[[Category:Archived Pages]]
