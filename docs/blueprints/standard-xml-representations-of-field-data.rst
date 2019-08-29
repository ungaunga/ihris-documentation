Standard XML Representations of Field Data
==========================================

This would create a standard way of representing form field data safely as structured xml. It would be used by the custom reporting module whenever export as XML is chosen. This would be added for version 4.1 of I2CE/iHRIS.

 **Justification** 
Currently the reporting system for iHRIS exports data in XML in an unsafe way, namely it just dumps out the database value.  For the currently limited uses of XML report this has not been too problematic.  However there are some issues that need to be resolved so that XML based report exports can be more readily implemented and fully utilized.  These issues include:


* potential for exported data to itself can xml data which would make the xml export invalid
* inability to export binary data (such as PDF files or photos) in a readable format
* XSLT manipulation of structured data (such a mapped fields) is painful and ugly and prone to breakage as it can only the simple string manipulation functions available.


 **Note**  This will break existing XSLT transforms of exported XML data.  In particular of the transforms used by Kenya and Zanzibar would need to be updated before they upgrade to 4.1 of iHRIS.  This is intentional as we would now be able to use xpath queries to get at the needed data rather than perform string manipulations.

 **Requirements** 


* Experience in creating new forms in iHRIS
* Experience in object oriented PHP
* Experience with XML

 **Deliverables** 


* Fully functional, documented, and tested code that implements the code requirements as defined below.
* Updates to the XSLT transforms used by Kenya and Zanzibar for SDMX-HD


API
^^^

I2CE_FormField
~~~~~~~~~~~~~~


* add in a (final) method getXMLData($as_node = false).  Calls _getXMLData().  If $as_node == false, the simply pass it along.  If $as_node == true, first convert it to a DOMNode and return that
* add in a abstract method _getXMLData() which return strings

Sub-Classes of I2CE_FormField
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


* each non-abstract class should implement _getXMLData()

XML Format
^^^^^^^^^^
Each _getXMLData() should return a string that looks like 

.. code-block:: xml

    <field type='XXX'>YYYY<field>
 where XXX is the form field type such as MAP, STRING, DATE_YMD, etc and YYY is as defined below

I2CE_FormField_BINARY_FILE
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='BINARY_FILE'><value file-name='$filename' mime-type='$mimetype fmod-time='$mod_time'>base64($binary_data)></value></field>
    



I2CE_FormField_DOCUMENT
~~~~~~~~~~~~~~~~~~~~~~~
Same as [[#I2CE_FormField_BINARY_FILE | BINARY_FILE]] except type='DOCUMENT'

I2CE_FormField_IMAGE
~~~~~~~~~~~~~~~~~~~~
Same as [[#I2CE_FormField_BINARY_FILE | BINARY_FILE]] except type='IMAGE'


* Possibly add the attribute width and height for easy processing

I2CE_FormField_ASSOC_FLOAT
~~~~~~~~~~~~~~~~~~~~~~~~~~
Same as [[#I2CE_FormField_ASSOC_INT | ASSOC_INT]] but with type='ASSOC_FLOAT'

I2CE_FormField_ASSOC_INT
~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='ASSOC_INT'><value key='$key0' >$value[$key0]<value>...<value key='$keyn'>$value[$keyn]</value></field>
    

where key0...keyn runs through the array keys

I2CE_FormField_ASSOC_LIST
~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='ASSOC_INT'><value key='$key0' >$string_value[$key0]<value>...<value key='$keyn'>$string_value[$keyn]</value></field>
    

where key0...keyn runs through the array keys. Here $string_value should follow the same rules is as in [[#I2CE_FormField_STRING_LINE]] adding in the attribute encode='base64' as needed

I2CE_FormField_ASSOC_PERCENT
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Same as [[#I2CE_FormField_ASSOC_INT | ASSOC_INT]] but with type='ASSOC_PERCENT'

I2CE_FormField_BOOL
~~~~~~~~~~~~~~~~~~~
same as [[#I2CE_FormField_YESNO | YESNO]] but with the type='BOOL'

I2CE_FormField_DATE_HMS
~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='DATE_HMS'><hour>$hour</hour><minute>$minute</minute><second>$sec</second></field>
    


I2CE_FormField_DATE_MD
~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='DATE_MD'><month>$month</month><day>$day</day></field>
    


I2CE_FormField_DATE_TIME
~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='DATE_TIME'><year>$year</year><month>$month</month><day>$day</day><hour>$hour</hour><minute>$minute</minute><second>$sec</second></field>
    


I2CE_FormField_DATE_Y
~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='DATE_Y'><year>$year</year></field>
    


I2CE_FormField_DATE_YMD
~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='DATE_YMD'><year>$year</year><month>$month</month><day>$day</day></field>
    


I2CE_FormField_INT
~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='INT'>$value</field>
    


I2CE_FormField_INT_GENERATE
~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='INT_GENERATE'>$value</field>
    


I2CE_FormField_INT_LIST
~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='INT_LIST'><value>$value[0]<value>...<value>$value[n]</value></field>
    

where 0...n runs through the array keys

I2CE_FormField_INT_RANGE
~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='INT_RANGE'>$value</field>
    



I2CE_FormField_STRING_LINE
~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: xml

    <field type='STRING'>YYYY</field> 
    

where YYYY is:


* If the string is less than 1000 characters
* *If the string does not contain a "<" character, then

.. code-block:: xml

    YYYY = <value>$value</value>



* *If the string contains as "<", then follow the rules for >= 1000 characters
* If the string is >= 1000 characters:
* *If the $value contains CDATA a string, then

.. code-block:: xml

    YYYY= <value encoding='base64'>base64($value)</value> 



* *If the $value does not contains "CDATA" then  <source lang='xml'>YYYY=  <value><![CDATA[$value]]><value></source>

I2CE_FormField_STRING_MLINE
~~~~~~~~~~~~~~~~~~~~~~~~~~~
same as [[#I2CE_FormField_STRING_LINE | STRING_LINE]] but with the type='STRING_MLINE'

I2CE_FormField_STRING_PASS
~~~~~~~~~~~~~~~~~~~~~~~~~~
?Should we export this or should it be blank?


I2CE_FormField_STRING_TEXT
~~~~~~~~~~~~~~~~~~~~~~~~~~
same as [[#I2CE_FormField_STRING_LINE | STRING_LINE]] but with the type='STRING_TEXT'

I2CE_FormField_TOGGLE
~~~~~~~~~~~~~~~~~~~~~
same as [[#I2CE_FormField_YESNO | YESNO]] but with the type='TOGGLE'

I2CE_FormField_YESNO
~~~~~~~~~~~~~~~~~~~~


* if $value == 1 then <source lang='xml'><field type='YESNO'>1</value></source>
* otherwise<source lang='xml'><field type='YESNO'>0</value> </source>

I2CE_FormField_PERCENT_INT
~~~~~~~~~~~~~~~~~~~~~~~~~~
<source lang='xml'>
<field type='INT'>$value</field>
</source>

I2CE_FormField_FLOAT
~~~~~~~~~~~~~~~~~~~~
<source lang='xml'>
<field type='FLOAT'>$value</field>
</source>


I2CE_FormField_PERCENT
~~~~~~~~~~~~~~~~~~~~~~
<source lang='xml'>
<field type='PERCENT'>$value</field>
</source>


I2CE_FormField_MAP
~~~~~~~~~~~~~~~~~~
<source lang='xml'>
<field type='MAP'><value form='$form'>$id</value></field>
</source>
$id should be subject to the same rules as used for [[#I2CE_FormField_STRING_LINE | STRING_LINE]] adding the attribute encoding as needed


I2CE_FormField_MAP_MULT
~~~~~~~~~~~~~~~~~~~~~~~
<source lang='xml'>
<field type='MAP_MULT'><value form='$form0'>$id1</value>...<value form='$formN'>$idN</value></field>
</source>


I2CE_FormField_REFERENCE
~~~~~~~~~~~~~~~~~~~~~~~~
Same as [[#I2CE_FormField_MAP | MAP]] but type='REFERENCE'


iHRIS_FormField_CURRENCY
~~~~~~~~~~~~~~~~~~~~~~~~
If the currency form is 'currency' then <source lang='xml'><field type='CURRENCY'><value id='$currencyID'>$amount</value></field></source>




