Technical Overview: Form Storage -- SDMX-HD
===========================================

This is a form storage mechanism designed to read data from an SDMX-HD code list file.  This form storage mechanism is present in version >= 4.0.5.

This is a read-only form storage mechanism.  This storage mechanism will only work for forms that are or extend I2CE_SimpleList.

 **This form storage mechanism requires PHP 5.3 or greater** 

Form Storage Options
^^^^^^^^^^^^^^^^^^^^

The options specifying a SDMX-HD storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/SDMXHD
It has the following structure:



* file:  The SDMX-HD file that the data should be read from.  This can either be an absolutely given file path, a relative file path, or the URL of a  stream handled by php.  If it is a relative file path, then it uses the SDMXHD [[File Search Paths | file search]] category.The file can also be a path to a scalar node in magic data as indicated by 'mdn://path/in/magic/data'
* CodeListID: The code list ID to be read.  This is for files that may have more than one code list defined.  This must be set.


Global Options
^^^^^^^^^^^^^^
There are global options for SDMX-HD form storage. They are specified at:
 /modules/forms/storage_options/SDMX-HD
This has the structure:


* closeFile: defaults to false.  If true, we close the file between access.  Otherwise, we allow PHP to handle closing the file resource at the end of the script's call.


Form Definition
^^^^^^^^^^^^^^^
To use SDMX-HD storage for a form use the following configuration.  Replace $form, $form_name, $file_location and $CL_ID with the appropriate values.


.. code-block:: xml

    <configurationGroup name="$form">
      <displayName>SDMX-HD Code List: $form</displayName>
      <description>The SDMX-HD Code List: $form_name</description>
      <configuration name="class" values="single">
        <value>I2CE_SimpleList</value>
      </configuration>
      <configuration name="display" values="single" locale="en_US">
        <value>$form_name</value>
      </configuration>
      <configuration name="storage" values="single">
        <value>SDMXHD</value>
      </configuration>
      <configurationGroup name="storage_options" path="storage_options/SDMXHD">
        <configuration name="file" values="single">
          <values>$file_location</value>
        </configuration>
        <configuration name="CodeListID" values="single">
          <value>$CL_ID</value>
        </configuration>
      </configurationGroup>
    </configurationGroup>
    


An example for gender may be:



.. code-block:: xml

    <configurationGroup name="cl_gender">
      <displayName>SDMX-HD Code List: cl_gender</displayName>
      <description>The SDMX-HD Code List: Gender</description>
      <configuration name="class" values="single">
        <value>I2CE_SimpleList</value>
      </configuration>
      <configuration name="display" values="single" locale="en_US">
        <value>Gender</value>
      </configuration>
      <configuration name="storage" values="single">
        <value>SDMXHD</value>
      </configuration>
      <configurationGroup name="storage_options" path="storage_options/SDMXHD">
        <configuration name="file" values="single">
          <values>CL_GENDER+SDMX-HD+1.0.xml</value>
        </configuration>
        <configuration name="CodeListID" values="single">
          <value>CL_GENDER</value>
        </configuration>
      </configurationGroup>
    </configurationGroup>
    



