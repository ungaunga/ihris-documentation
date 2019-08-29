Customize Recent Forms Display
==============================

One feature in iHRIS is the ability to look at recently changed forms.

You can customize the output of the recent changes display by creating a hook in your module.  This will allow you to append any output you desire to the recent form output.  One thing to note is that the recent changes only display changes made to the form being displayed, for example the person form. 

 **Warning:** Changes to child forms aren't reflected in this page.


Creating the Hook
^^^^^^^^^^^^^^^^^
Any form you are displaying in recent changes will call the hook "recent_form_'''$form'''_display" and append that to the output on the page.  This will allow you to display additional information as needed.  To create the hook you need to modify or add the getHooks method to your module.  Then create the method in the module.  The hook will be passed the data for the current record being displayed including all fields that are displayed in the page.  See below for setting up a hook for the person form and adding the date of birth to the output.  By default, the person form displays the first name and last name.



.. code-block:: php

    /**
     * Return the array of hooks available in this module.
     * @return array
     */
    public static function getHooks() {
        return array(
            "recent_form_person_display" => "recent_form_person_display",
        );
    }
    
    /**
     * Add the date of birth to the recent person form display.
     * @param array $data
     */
    public function recent_form_person_display( $data ) {
        $demographics = I2CE_FormStorage::listDisplayFields( "demographic", array( "birth_date", "person|" . $data['id'] );
        // There should only be one demographic child form per person, so take the first result.
        $demographic = current( $demographics );
        if ( array_key_exists( 'birth_date', $demographic ) ) {
            return ' - DOB: ' . $demographic['birth_date'];
        } else {
            return null;
        }
    }
    


You can query any information from the database to add to the display, but be aware that additional processing will slow down the display as your method will be called for each record being displayed.


