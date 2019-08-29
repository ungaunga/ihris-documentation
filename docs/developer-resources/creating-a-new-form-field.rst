Creating a New Form Field
=========================

This tutorial applies to version 4.0 of the iHRIS Suite.

In this tutorial, we will create new form field data type.  This form field will be a one line string which is capitalized.  The capitalization will be enforced on the server-side as well as the client-side via java-script.  We will wrap all of this into a module, **CapField**  so that it can be shared easily.


Creating the Module
^^^^^^^^^^^^^^^^^^^
In one of your module directories (e.g. your site's modules directory) do the following:
 mkdir CapField
 gedit CapField/CapField.xml
and add in the following lines:


.. code-block:: xml

     <?xml version="1.0"?>       
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name='CapField'>      
      <metadata>
        <displayName>Capitalized Field</displayName>   
        <category>System Component</category>
        <description>Provides an always capitalized field</description>
        <creator>Intrahealth Informatics</creator>
        <email>hris@capacityproject.org</email>
        <version>4.0.0</version> 
        <requirement name='i2ce'>
          <atleast version='4.0'/>
          <lessThan version='4.1'/>
        </requirement>
        <priority>200</priority>
        <path name='classes'>
          <!-- we need to create a php class to handle creating and validating our field. it will live in this directory-->
          <value>./lib</value>
        </path>
      </metadata>
      <configurationGroup name='CapField' path='/'>
        <configuration name='STRING_CAP' path='/modules/forms/FORMFIELD/STRING_CAP'>
          <!-- This registers the form field class we create with the system as STRING_CAP-->
          <value>I2CE_FormField_STRING_CAP</value>
        </configuration>
      </configuratioGroup>
    <I2CEConfiguration>
    



I2CE_FormField_STRING_CAP
^^^^^^^^^^^^^^^^^^^^^^^^^
We need to create a PHP class to handle the client-side validation of our capitalized field. The field we want has input which is a one line string, so we will subclass the existing one.  We do this as follows:
 mkdir CapField/lib
 gedit CapField/lib/I2CE_FormField_STRING_CAP.php
and add in the following:


.. code-block:: php

     class I2CE_FormField_STRING_CAP extends I2CE_FormField_STRING_LINE  {
      
    
        /**
         * Checks to see if the current value for this is set and valid.
         * This function is used to validate the input on the server-side. 
         * We first check to see if it is valid using the parent class' validation method.  
         * If this passes, we then check the the capitalized version of the value we have is the same
         * as the value we have (if so it is already capitalized and is thus valid)
         * @return boolean
         */
        public function isValid() {
            if (!parent::isValid()) {
               return false;
            }
            $value = $this->getValue();
            return ($value === ucwords($value));
        }
    
    
        /**
         *This is the method to create the input element for the capitalized input string
         * @param DOMNode $node  The node that we wish to add out input element to
         * @param I2CE_Tempalte $template.  The page template object that we are working in
         * @parma DOMNode $form_node  The node from the html template file that requested this form field be displayed
         */
        public function processDOMEditable($node,$template,$form_node) {
            $ele_name = $this->getHTMLName();  //this gets the name of the input element which is used for the GET and POST variables
            $template->addHeaderLink('mootools.js'); //makes sure that the mootools javascript library is avaiable to us
            $element = $template->createElement(  //creates the input element that we will add 
                  "input", 
                  array( 
                        "name" => $ele_name, 
                        "id" => $ele_name, 
                        "type" => "text", 
                        "onblur"=> "this.setValue(this.getValue().capitalize());"
                        "value" => $this->getDBValue() 
                        ) );
            $this->setElement($element);  //registers the input element that we created
            $node->appendChild( $element);  //add the input element node we just created to the node it needs to be under
        }
    
    }
    





Javascript
~~~~~~~~~~
In the processDOMEditable() function we added some javascript for the onblur check.  iHRIS uses version 1.2 of the  `mootools <http://mootools.net/>`_  javascript library.  Mootools has a handy  `capitalization <http://mootools.net/docs/core/Native/String#String:capitalize>`_  function that we incorporated into our form field so that on a "blur" event the input element will capitalize.


Finishing Up
^^^^^^^^^^^^
You are done, you just need to require the module you created where appropriate.  You can now add a field to a form with type STRING_CAP.

[[Category:Developer Resources]]
