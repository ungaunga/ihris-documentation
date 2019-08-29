Creating a New Form Field - ES
==============================

Este tutorial aplica para la versión 4.0 de iHRIS Suite.

En este tutorial, crearemos un tipo de dato de formulario de campo nuevo.  Este formulario de campo será una cadena de línea en mayúsculas.  Que esté en mayúsculas servirá en el server-side como en el client-side a través de java-script.  Pondremos todo esto en un módulo, **CapField**  para poder compartirlo fácilmente.


Crear el Módulo
^^^^^^^^^^^^^^^
En uno de sus directorios de módulos (e.j. el directorio de módulo de su sitio) haga lo siguiente:
 mkdir CapField
 gedit CapField/CapField.xml
y agregue las siguientes líneas:


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
Necesitamos crear una clase PHP para manejar la validación del client-side de nuestro campo en mayúsculas. El campo que queremos tiene una forma de entrada de una cadena de línea, así que haremos una subclase de la existente. Hacemos lo que sigue:
 mkdir CapField/lib
 gedit CapField/lib/I2CE_FormField_STRING_CAP.php
y agregamos lo siguiente:


.. code-block:: php

     class I2CE_FormField_STRING_CAP extends I2CE_FormField_STRING_LINE  {
      
    
        /**
         * Checks to see if the current value for this is set and valid.
         * This function is used to validate the input on the server-side. 
         * We first check to see if it is valid using the parent class' validation method.  
         * If this passes, we then check the capitalized version of the value we have is the same
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
En la función processDOMEditable() agregamos algo de javascript para el onblur check.  iHRIS utiliza la  versión 1.2 de la biblioteca de  javascript   `mootools <http://mootools.net/>`_ .  Mootools tiene una function muy útil  `capitalization <http://mootools.net/docs/core/Native/String#String:capitalize>`_  que incorporamos a nuestro formulario de campo para que en el caso de un "blur" la información entrada se convierta a mayúsculas.


Para Terminar
^^^^^^^^^^^^^
Ya terminó, solo necesita requerir el módulo que creó donde sea apropiado. Ahora puede agregar un formulario de campo con tipo STRING_CAP.

[[Category:Fields]][[Category:Spanish]]
