Migrating Forms from Entry to MagicData
=======================================

This tutorial will explain how to migrate forms from previous versions that were stored in the entry table and move them to magic data storage as well as update any mapped fields that referenced the values.  For a more complicated example look at the Geography module in iHRIS Common or the Education sub-module in the Person module in iHRIS Common.


Step 1: Change a Form's Storage Mechanism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In iHRIS 4.0, storage mechanisms were added to forms.  The default storage method is to use the entry tables as in previous versions of iHRIS.  For distributed systems you may want to have some forms be stored in magic data so they can be managed centrally more easily and can be updated by module updates to keep consistent IDs across all the distributed systems.

First we need to change the storage for the form to magic data in the module configuration file.  For earlier versions this section needs to be added.  If you're migrating a form that already has storage defined, you just need to change the storage to be magic data.  These changes will be under the "forms" section of your configuration at the path: /modules/forms/forms/'''<form_name>'''.  This just includes the new storage section.  The class and display sections should already be there for this form.  You'll also need to update the version for this module and include that same version number in the storage section.



.. code-block:: xml

    <configurationGroup name="forms" path="/modules/forms">
      <configurationGroup name="forms">
        <configurationGroup name="form_XXXXX">
          <configuration name="storage" values="single">
            <displayName>Storage Mechanism</displayName>
            <description>The storage mechanism for this form.</description>
            <version>X.X.X</version>
            <value>magicdata</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    </configurationGroup>
    



Step 2: Save Data From The Previous Storage Mechanism
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now we need to make sure we save any old data before the storage mechanism is changed for the form.  For example if the field person.nationality is mapped to the country form and the country form is moving from entry storage to magicdata then you'll need to save the old value so you can change it to the correct new value once the country form has been migrated.  This is all done using the pre_upgrade() method for the module class for the given module.  A helper method is in I2CE_FormStorage called storeMigrateData() to save this data for later reference.

You'll need to know the version that is being upgraded to so you only save the data at the correct time for this module.  In the example code "X.X.X" is used.  You'll also need to determine a migrate path to use for everything you'll be upgrading.  This is so that everything can be referred to later in one place if you need to access it.  It can be any text or even the version number you're upgraded to.  It should be under the magic data path of:  /I2CE/formsData/migrate_date/'''XXXXXX'''.



.. code-block:: php

    public function pre_upgrade( $old_vers, $new_vers, $new_storage ) {
        if ( I2CE_Validate::checkVersion( $old_vers, "<", "X.X.X" ) ) {
            $migrate_path = "/I2CE/formsData/migrate_data/MyUpgrade";
            I2CE_FormStorage::storeMigrateData( array( "FORM" => array( "FIELD1", "FIELD2" ) ), $migrate_path );
        }
        return parent::pre_upgrade( $old_vers, $new_vers, $new_storage );
    }
    



Step 3: Move Forms To The New Storage Mechanism and Migrate Any Mapped Values
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now the forms need to be migrated to the new storage mechanism and any mapped fields that were stored in the previous step need to be migrated to its new ID.  This can all be done in the upgrade() method for the module class.  There are two helper methods in I2CE_FormStorage to assist with this:  migrateForm() and migrateField().

You'll use the same migrate path that was used in the pre_upgrade() method.  You'll also need to create a user object to save the changes.  Use the ID of an administrative user.  You can repeat the function for every form that needs to be migrated.



.. code-block:: php

    public function upgrade( $old_vers, $new_vers ) {
        if ( I2CE_Validate::checkVersion( $old_vers, "<", "X.X.X" ) ) {
            $user = new I2CE_User( $user_id, false, false, false );
            $migrate_path = "/I2CE/formsData/migrate_data/MyUpgrade";
    
            if ( !I2CE_FormStorage::migrateForm( "FORM", "entry", $user, $migrate_path ) ) {
                return false;
            }
            
            if ( !I2CE_FormStorage::migrateField( "FORM", array( "FIELD1" => "FIELD1_MAPPED_FORM", "FIELD2" => "FIELD2_MAPPED_FORM" ),
                    $migrate_path, $user ) ) {
                return false;
            }
        }
        return true;
    }
    



Step 4: Check The Migration
^^^^^^^^^^^^^^^^^^^^^^^^^^^

When you next access the site it will run the upgrade methods for any modules you have upgraded.  When it has finished you will see the old data under magic data at the path: /I2CE/formsData/migrate_data/MyUpgrade (or whatever path you used).  You'll also find the forms that are now stored in magic data under /I2CE/formsData/forms/.  You'll want to check to make sure any fields that were migrated successfully use the new ID for each mapped value.

[[Category:Magic Data]]
