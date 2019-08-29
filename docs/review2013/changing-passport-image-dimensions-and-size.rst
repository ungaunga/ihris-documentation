Changing Passport Image Dimensions and Size
===========================================

In this tutorial we show how to resize the dimensions of the images you are uploading to iHRIS Manage or iHRIS Qualify. Take note that resizing the dimensions (width and length) goes further to reducing the image size.



Defining the form field
^^^^^^^^^^^^^^^^^^^^^^^
In order to be able to resize the image, we need to define the form field to be of type PASSPORT like here
Now change the lines:
<!--

.. code-block:: xml

    -->
        <configurationGroup name="forms" path="/modules/forms">
          <configurationGroup name="formClasses">
            <configurationGroup name="iHRIS_Passport">
              <configurationGroup name="fields">
                <displayName>The fields defined for this form</displayName>
                <configurationGroup name="passport">
                  <configurationGroup name="meta">
                    <span style='color:olive'><configuration name="max_height"></span>
                      <span style='color:red'><value><span style='color:green'>128</span></value></span>
                    <span style='color:olive'></configuration></span>
                    <span style='color:olive'><configuration name="max_width"></span>
                      <span style='color:red'><value><span style='color:green'>136</span></value></span>
                    <span style='color:olive'></configuration></span>
                  </configurationGroup>
                  <displayName>The field 'address'</displayName>
                  <configuration name="formfield">
                    <displayName>The form field type</displayName>
                    <span style='color:green'><value>PASSPORT</value></span>
                  </configuration>
                  <configuration name="headers" type="delimited" locale="en_US">
                    <displayName>The headers for this field.</displayName>
                    <value>default:Passport</value>
                  </configuration>
                </configurationGroup>
              </configurationGroup>
            </configurationGroup>
          </configurationGroup>
        </configurationGroup>
      <!--  End /modules/forms -->
    <!--
-->


Changing the dimensions
^^^^^^^^^^^^^^^^^^^^^^^
In order to change the dimensions, you need to include a meta tag when defining the field. In it you specify the maximum width and maximum height for the passport photo. However if you don't need to affect the dimensions i.e. height and width you set the values for max_height and max_width equal to zero. Setting these values to zero only affects the size of the image and keeps the dimensions from the original image.

[[Category:Customizations]][[Category:Review2013]]
