Setting An Establishment
================================================

Starting with version *4.0.6* of iHRIS Manage you now have the option of setting staffing norm and establishments. 

You may have several different types of establishments or staffing norms at your organization.  For example:


* Funded Positions
* Staffing Norms set by the ministry of health
* Recommended positions based on a master plan
These norms may also change yearly and be linked either to a facility, a facility type, a job or a cadre.
 
The establishment module lets you track these establishments within the system.  You can also [[Custom Reporting -- Creating an Establishment Report|create a report]] showing the number of filled positions against the establishment.



Create an establishment type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
An establishment type is simply a name you can use to refer to the establishment you wish to deal with, for example "Funded Positions."  

To set an establishment type:


* Click on "Configure System"
* Click on "Administer Database."
* Click on "Establishment Type" under "Planning Information"
* Add a new establishment type.  In the example it would be "Funded Position"


Creating an establishment period
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The establishment period is simply a year that a given establishment type is effective,  for example  "2010" for the the "Funded Positions."

To set an establishment period:


* Click on "Configure System"
* Click on "Administer Database."
* Click on "Establishment Period" under "Planning Information"
* Add a new "Establishment Period"
* *Set the "Establishement Type" as you wish.  In the example above it would be "Funded Postions
* *Set the year of applicability as you wish. In the example above it would be "2010"


Creating the establishments
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Now that you have the establishment period set up, you can now set the specific establishments.  For each establishment, you can specify either the job or cadre, and either the facility or facility type.  

Now you can choose to set the establishment for the job Enrolled Nurses with the facility type Primary Health Care Unit (PHCU).  If you need to, you can also set the number of Enrolled Nurses for one or more of the PHCUs.



* Click on "Configure System"
* Click on "Administer Database."
* Click on "Establishments" under "Planning Information"
* Add a new "Establishment"
* *Set the "Establishment Period."  In the example above it would be "Funded Positions - 2010"
* *Choose the Facility or Facility Type.
* *Choose the Job or Cadre
* *Set the amount/number of health workers for this establishment

 **Note:**  When the system is determining the establishment associated for a particular position it checks to see if an establishment has been set for the pair (job, facility).  If there is no establishment found, it will check the (cadre,facility) or (job,facility_type).  Finally, it will check if the (cadre,facility_type) has an establishment.

[[Category:Customizations]][[Category:iHRIS Manage]][[Category:Review2013]]
