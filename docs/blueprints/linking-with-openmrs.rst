Linking with OpenMRS
====================

Mapping the openMRS database to a health-care worker HR dataset.

See [[Data Interoperability| here]] for general information about data interoperability with iHRIS.

==Users and Roles in openMRS==
A row in the 'users' table of openMRS often represents a health care
worker.  One of the columns in this table is 'user_id'.

There is a 'user_role' table which links a 'user_id' to a ?unique? 'role'

The 'role' table contains the list of roles that a user can be
assigned.   These are often, but not always, a job for a health care
worker.   Examples might include:
          Anonymous -- an unauthenticated user
          Authenticated
          Clinician
          Nurse
          Provider
          System Administator


Thus, to get all the health-care workers from openMRS one would have
to select all users with a roles within a certain subset of all
roles.  

One the openMRS 'users' table has been thus restricted it may be the
case that the role is the "job" of the health-care workers (such as
Nurse).  As this is certainly implementation dependent, one
would need a map:
      'role' --> "job"

===Child/Parent roles===
What are these?

=='user_property'==
Users of openMRS can be assigned properties via the 'user_property'
table which contains the columns:
      'property': varchar(100)
      'user_id': integer
      'value': varchar(255)

=='person_attribute'==
Can a user have a person attribute?  What are some examples?

[[Category:OpenMRS]][[Category:Blueprints]]
