ManageAccessFacility -- Limit Dropdown (List) Fields by User
============================================================

This document refers to iHRIS Manage 4.1 or later.

Once you have a geography/facility level user created, you can limit certain drop down fields to only show allowed values for this user.  See [[ManageAccessFacility -- Create Facility/Geographic Restricted Users|Create Facility/Geographic Restricted Users]] for how to create these users.

Limiting Drop Down Values for a Field
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

There may be certain location or facility fields that you want to restrict based on the location or facility that a user is limited to.  By default, the position facility field and any form that is based on iHRIS_ListByCountry location field are limited in this way.  You may have other custom fields that need the same restriction.  If the user is restricted to a facility, then they won't see any values for locations.  This should only apply to values they shouldn't currently be editing anyway, for example the facility location field.  In this case, the user can't add new facilities since they are restricted to one facility.

In the meta section of the field you wish to limit, you should add the following section.  This example is from the position facility field.

.. code-block:: xml

      <configuration name="add_limit_module"
       path="/modules/forms/formClasses/iHRIS_Position/fields/facility/meta/add_limit_module"
       type="delimited">
        <version>4.1.X.X</version>
        <value>ManageAccessFacility:getLimitAdd</value>
      </configuration>
    

The important part is the meta/add_limit_module section.  This is where you would add the same value for other fields you wish to restrict.  The meta/display/default value should include all allowable forms that can be assigned to a user.  In this case it is:  **facility+location:county:district:[region]:country** .

