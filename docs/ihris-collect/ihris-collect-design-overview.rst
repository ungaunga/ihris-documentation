IHRIS Collect Design Overview
=============================

iHRIS Collect is intended as a one-time data collection survey tool built on the I2CE Framework.

Motivation
^^^^^^^^^^

* See the following  `HRIS Blog Entry <http://www.capacityproject.org/hris/blog/index.php/2009/09/ihris-collect/>`_  for a general overview
* Moving from a paper based system directly to iHRIS Qualify or iHRIS Manage often involves difficulty as the data is not cleaned.  So this is really a three step process:
* *collect the data
* *put the data into electronic format
* *clean up the data
* the data collected may not already be organized into the structure expected by iHRIS Manage. For example, a few places have been  interested in using iHRIS Manage.  They did not have a Job/Position structure already defined.  As a result, they imported/entered a lot of data into iHRIS Manage without a well thought out Job structure.
* Introduces administrators/developers to the I2CE framework so that they have familiar systems as the move from the data collection process to the routine data entry
* If data entry clerks are maintained between the one-time data collection process and the routine data collection, they will have a similar system which reduces training.  This is the process for the iHRIS Manage implementation in Zanzibar,
* we have lot of similar functionality and design architecture already built into the system via the custom reporting tool.

Staged Implementation
^^^^^^^^^^^^^^^^^^^^^
There are several possibilities for a staged implementation.  The stages do not necessarily need to be completed in order.  They more reflect a break down into functional units that will ultimately benefit iHRIS Manage, Qualify and Plan.

Stage 1:Branding/Single Form
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In this stage, we develop the branding and provided a minimial implementation for iHRIS Collect:

* Settle on the name (iHRIS Collect)
* Choose color scheme and update CSS.  I vote for beige.
* Build off of iHRIS Common -- may need to break up iHRIS Common into some sub-modules but probably not.
* Assume each page to edit only contains one form.  Assume the developer can manually [[Defining Forms|define a form]] in [[Configuration (Magic) Data|magic data]]
* The html template files are built "by hand" by the developer for each form and one which links to all the forms in the survey.
* A survey page: is a form and its associated template file.  Each such page should be packaged as a module and assigned a task to view/edit the data.
* To enable custom reporting,  for each form one needs to define the relationship which contains just the form as a primary form.
* perhaps we can write a script to automate this once the fields (and their types) for a survey are defined.

Stage 2:Custom Pages
~~~~~~~~~~~~~~~~~~~~
Implements [[Custom Pages]] to allow the system administrator to easily create pages based on existing forms in the system.

Stage 3:Custom Forms
~~~~~~~~~~~~~~~~~~~~
Implements [[Custom Forms]] to allow the system administrator to easily create custom forms.  This can then be used to build custom pages.

Stage 4:Custom Page Displays
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
As the custom pages will general follow a similar architecture to the custom reporting tools, we can extend the functionality of the custom pages by adding in custom displays.  Here are some possible displays:

* create a PDF version of the survey for paper-based collection.  Is this the priority here?  Should not be too difficult to do.  A few potential pitfalls:
* *what to do with long lists of data, should we display them all and have a check box? or should we leave it as free text and let the data entry people deal with it?
* *what about tiered data lists such as geography (district, region, country)?
* exporting survey to something be imported to make PDA/hand-held survey tools.  also provide need to provide a means to sync the data from the hand-held
* * `epi surveyor <http://www.episurveyor.org/user/index>`_
* * ` open data kit <http://www.episurveyor.org/user/index>`_
* * ` openxdata <http://www.openxdata.org/>`_
* * `  epihandy <http://www.epihandy.com/index.php/Main_Page>`_  and and  `omevac <http://code.zegeba.org/EpiHandy/wiki/OmevacDevelopers>`_

Other Documents
^^^^^^^^^^^^^^^

* [[File:IHRIS_Collect.pdf]]
* `HRIS Blog Entry <http://www.capacityproject.org/hris/blog/index.php/2009/09/ihris-collect/>`_

