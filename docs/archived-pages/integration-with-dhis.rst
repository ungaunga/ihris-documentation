Integration with DHIS
================================================

This page is intended as a planning document for integration of iHRIS Manage with DHIS.

For reference, see also:


* `tghin discussion <http://www.tghin.org/node/236#comment-152>`_
* `SDMX_HD <http://groups.google.com/group/sdmx_hd/web/documentation>`_
* `dxf format <https://blueprints.launchpad.net/dhis2/+spec/dxf-format>`_



Technical Documentation for DHIS 2.0
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Some information on the `Database structure <https://mail.intrahealth.org/exchweb/bin/redir.asp?URL=http://bazaar.launchpad.net/%257Edhis2-devs-core/dhis2/trunk/download/head%253A/technicalarchitectur-20090303164601-edynttiof6lqx3ke-17/Technical%2520Architecture%2520DHIS%25202.doc>`_ in DHIS 2.0.


Possibilities for Integration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It might be useful to start looking at iHRIS's ability to export data to XML.
We could then possibly write some xslt transformations to transform that into something more  easily consumable by DHIS2.  Currently this would likely be our "native" DXF format but there are a number of reasons why we might consider evolving from there:


* some of our internal discussion around the `native dxf format <https://blueprints.launchpad.net/dhis2/+spec/dxf-format>`_
* we wish to consider supportting SDMX HD (the new generation IXF) being promoted by WHO.    Its intent is primarily to support the exchange of statistical data and metadata between (international) organizations it seems not as well optimized for the movement of bulk data on a routine basis as our current format.

These are two ways this could evolve:


* you export what you export "naturally"; we import what we import naturally and we try to build the bridge with xslt.  (preferred)
* iHRIS Manage exports SDMX HD and DHIS imports SDMX HD.


Getting Data Out of iHRIS Manage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can see how we data in iHRIS Manage might be exported in an XML 
format.  ` Here <http://bazaar.launchpad.net/~intrahealth%2Binformatics/ihris-common/3.2-dev/annotate/head%3A/modules/Person/modules/Demographic/Demographic.xml>`_ is a sample for the "gender" form (look starting
line 49)
  
This is how data is loaded in for the "magic data" [[Form Storage Mechanisms|form storage mechanism]].  This can be easily exported, as you suggested, via our "Magic Data Export".  In fact, with the "Magic Data Browser", you can browse to a the appropriate place in magic data and hit the "Export" button.

There is a second, distinct, way to export the data will work if the data is not already stored in magic data, or if you need a more complicated "slice" of the data.  This is to use the custom reporting facility to dump the data out out.  Right now there is a CSV and html dump implemented.  Doing an XML dump would be a quick matter.


Translating XML Data
^^^^^^^^^^^^^^^^^^^^

[[Category:Archived Pages]]
