Adding Form and Field Validations
================================================

When editing a form in iHRIS, iHRIS can perform validations that the data make sense.  For example, you can mark a field as being required or unique.  You may also have more complicated logic that you want to ensure is in place, for example that the start date of a position does not come after its end date.  This article describes how to add custom validations for forms and fields.

This document refers to iHRIS 4.0.9 and later.

In some cases you may want to have additional validations on existing forms or fields, or you may need to add validations to new forms or fields you are creating.  You can do this using hooks in the module for your site or the form/field customization module you have created.

You can add a validation to a single field or do the entire form to compare multiple fields.  The first step is to create the hooks in the module class.  


Create the Module Class
^^^^^^^^^^^^^^^^^^^^^^^

You create hooks in the class code for your module.  This file will be in the classes path (usually ./lib) for your module.


Add a Module Class
~~~~~~~~~~~~~~~~~~

If your module doesn't currently have a class you will need to add one.  You can add the className node to the metadata in your module (or site) configuration file.



.. code-block:: xml

        <className>iHRIS_Module_$moduleName</className>
    


You would replace **$moduleName** with a unique name for your module class.  For example, in the iHRIS Manage Person Position module, the following class is used:



.. code-block:: xml

      <metadata>
        <displayName>iHRIS Manage Person Position</displayName>
        <className>iHRIS_Module_PersonPosition</className>
        ...
      </metadata>
    



Create the PHP Class File
~~~~~~~~~~~~~~~~~~~~~~~~~

Then in the module classes directory (./lib) you would create the file iHRIS_Module_'''$moduleName'''.php, replacing **$moduleName** with the class name you entered in the configuration file.



.. code-block:: bash

    gedit ./lib/iHRIS_Module_$moduleName.php
    


You should fill in additional comments, but the default blank file (which we'll fill out later).



.. code-block:: php

    /**
     * Class iHRIS_Module_$moduleName
     *
     * @access public
     */
    class iHRIS_Module_$moduleName extends I2CE_Module {
    
    }
    # Local Variables:
    # mode: php
    # c-default-style: "bsd"
    # indent-tabs-mode: nil
    # c-basic-offset: 4
    # End:
    



Add the getHooks Method
~~~~~~~~~~~~~~~~~~~~~~~
Now we need to define the getHooks method which tells the module factory which hooks this module supports.  If your module already had a class then you would only need to add the getHooks method to the existing code.  If it already has a getHooks method then skip this step and go to [[#Adding the Hooks|Adding the Hooks]].



.. code-block:: php

    class iHRIS_Module_$moduleName extends I2CE_Module {
    
        /**
         * Return the array of hooks available in this module.
         * @return array
         */
        public static function getHooks() {
            return array(
                   );
        }
    
    }
    


This is simply a place holder until we add in the actual hooks we want to define.  Those will go in the array that is being returned.


Adding the Hooks
^^^^^^^^^^^^^^^^

There are two types of hooks that can be added.  A field validation (for one field) and a form validation (for multiple fields).


Adding a Field Validation Hook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For field hooks, you use the form and field names:  valdate_form_'''$form'''_field_'''$field'''.  You replace **$form** and **$field** with the.  For example the iHRIS Common Person Contact module adds a validation hook for the contact email field as:  validate_form_'''contact'''_field_'''email'''.  Now we add this hook to the getHooks method as an associative array with the value being the method in the module class to be called to validate the field.  The method name can be anything, for clarity we will use the same name as the hook.

We will also create this method so it can be called by the module factory when the hook is called.  It takes a single form field object as an argument.



.. code-block:: php

        public static function getHooks() {
            return array(
                   'validate_form_$form_field_$field' => 'validate_form_$form_field_$field',
                   );
        }
    
        /**
         * Validate the $field in the $form form.
         * @param I2CE_FormField $formfield
         */
        public function validate_form_$form_field_$field( $formfield ) {
        }
    


In this method you will perform any checks necessary and if it fails then you will need to call setInvalidMessage on the $formfield.  See the [[Using Translateable Invalid Messages]] for how to define the messages in a way that allows for multiple translations.  This is the example function from the iHRIS Common Person Contact module.



.. code-block:: php

        /** 
         * Validate the email field for contact forms.
         * @param I2CE_FormField $formfield
         */
        public function validate_form_contact_field_email( $formfield ) { 
            $value = $formfield->getValue();
            if ( I2CE_Validate::checkString( $value ) 
                    && !I2CE_Validate::checkEmail( $value ) ) { 
                $formfield->setInvalidMessage('invalid_email');
            }   
        }   
    



Adding a Form Validation Hook
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Adding a validation hook for a form is very similar to adding a validation hook for a field.  The hook name will be:  validate_form_'''$form'''.  You replace **$form** with the form name you wish to validate.  For example, the person_position form has a validation hook called:  validate_form_'''person_position'''.  You add this hook to the getHooks method just like for field validation.  The method will take a single argument of the form object being validated.



.. code-block:: php

        public static function getHooks() {
            return array(
                   'validate_form_$form' => 'validate_form_$form',
                   );
        }
    
        /**
         * Validate the $form form.
         * @param I2CE_Form $form
         */
        public function validate_form_$form( $form ) {
        }
    


In this method you can check the values of multiple fields and call setInvalidMessage for any fields that don't validate.  See the [[Using Translateable Invalid Messages]] for how to define the messages in a way that allows for multiple translations.  This is an example from the iHRIS Manage Person Position module that validate the person_position form by comparing the start and end dates to make sure the end date is after the start date.



.. code-block:: php

        /**
         * Checks to make sure the end date is after the start date for the person position.
         * @param I2CE_Form $form
         */
        public function validate_form_person_position( $form ) {
            if ( $form->start_date->isValid() && $form->end_date->isValid() ) {
                if ( $form->start_date->compare( $form->end_date ) < 1 ) {
                    $form->setInvalidMessage('end_date','bad_date');
                }
            }
         }
    


[[Category:Fields]][[Category:Review2013]]
