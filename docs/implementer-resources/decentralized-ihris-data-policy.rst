Decentralized iHRIS Data Policy
===============================

This decentralized implementation of iHRIS is our answer on how to manage data in any of these settings:
*high Internet connectivity
*low Internet connectivity
*no Internet connectivity
It is designed to work easily, with minimal configuration, and maximal functionality.

Suppose that we are interested in setting up a decentralized implementation of iHRIS Manage in the country Taifeki.  Let us assume we are going to work on a three tier implementation: national, region and district.  We will show how to take advantage of [http://www.launchpad.net|launchpad] to maintain the various customizations needed for each of the sites.


==Data Management==
We first need to decide on a data management policy that is compatible with our data structure.


===Decentralized Data Structure===
Our decentralized data module is "vertical" in that it allows data to flow from the district to the region to the national level.  It also allows that the data flow in the reverse direction.  We do not allow data to flow "horizontally."  In other words, we do not have a mechanism for the data on a person in district A to be given to district B.  

We always that there is only one site that can write  each data component.  A data block consists of all the data for one form in one site. Examples of data components are:
*all the jobs at the national level
*all of the facilities in a specific region
*all of the positions in a specific district


===Data Management Policy===
These questions need to be answered:
*Who can see which data?
**(Examples) Should a district be able to see the facilities in another district?
*Who can edit which data?
**(Examples)Who maintains the list of facilities?  The jobs?  The positions? Is it at the national, regional or district level?

These questions need to be answered for all the [[Form Fields|forms]] within iHRIS Manage and all sites (national, regional and district-level).
===Example===
If you decide that each facility is maintained at the regional level.  This means the following:
*At the national level, the facility data needs to be componentized by regions and the facility and facility_contact forms will use the (read-only) [[Form Storage -- Multi-Flat Table|multi-flat]] storage mechanism to aggregate the cached data tables from the regional level.
*At the regional level, the facility data is not componentized.  Since the facility and facility contact information is not subject to frequent changes and you do not need to keep track of the history, you would choose to use the (read-write) [[Form Storage -- Magic Data|magic data]] form storage mechanism in your data policy.
*At the district level, the facility and facility contact data is exported from the region within two modules: ''ihris-manage-taifeki-northern-region-facility''   and ''ihris-manage-taifeki-northern-region-facility_contact.''  You would choose to use (read-only) [[Form Storage -- Magic Data|magic data]] form storage mechanism in your data policy.

[[Category:Implementer Resources]]
