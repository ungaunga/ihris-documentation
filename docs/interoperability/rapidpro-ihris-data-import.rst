RapidPro iHRIS Data Import
==========================

There are two types of data integration that we need.  One is for “flows” and one is for “contact fields.”

Some existing code is in iHRIS Common, in particular:
  http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.2-dev/view/head:/modules/CSD/modules/mHero/lib/CSD_Interface_RapidPro.php

Flows
^^^^^
Each workflow captures data.  Flows are accessible in the API here:
	https://rapidpro.io/api/v1/flows
There should be a service in iHRIS that let’s you select a workflow and it will query the RapidPro at the above API.  It should:

* look at the “rulesets” to extract the data fields and then dynamically create a form like “rapidpro_flow_$UUID” based on the the data fields extracted from the rulesets.
* have the form be a child form of person
* be able to specify if there is only one such child form or multiple
* the name of the form should be the name of the workflow

Once the dynamic form has been created, then there should be some data import functionality.   This would use the API here:
   https://rapidpro.io/api/v1/flows

Data Import Individual
~~~~~~~~~~~~~~~~~~~~~~
There should be a link on the person page which will take you to a page where you can:

* select a workflow
* the RapidPro ID is looked up for that person (code to this already exists in ihris-common)
* the data collected from the ?most recent? run of the flow are saved in the child form

Data Import Bulk
~~~~~~~~~~~~~~~~
There should be a link under the mHero bulk page where you select a workflow and then for all person forms, the individual data import is performed

Contact Fields
^^^^^^^^^^^^^^
A form "rapidpro_contact_fields" should be created as a unique child form of person.  The fields in this form can be dynamically pulled using the RapidPro API:
  https://rapidpro.io/api/v1/fields

The data for these fields should be populated using the RapidPro API:
  https://rapidpro.io/api/v1/contacts

Data Import Individual
~~~~~~~~~~~~~~~~~~~~~~
There should be a link on the person page which will take you to a page where you can import the RapidPro contact fields data.

Data Import Bulk
~~~~~~~~~~~~~~~~
There should be a link under the mHero bulk page where you select a workflow and then for all person forms, the individual data import is performed

