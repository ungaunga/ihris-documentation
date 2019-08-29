IHRIS Ideas List
================

If you wish to work on any of these projects, you can contact us at our [[Project Communication]] page.

Please see our [https://blueprints.launchpad.net/ihris-suite/+specs?show=all blueprints] on launchpad.

[[Completed iHRIS Ideas List]] has any completed features for historical purposes.

==iHRIS Core System Improvements==

<poll>
Please vote for the iHRIS Core System Improvements you would most like to see completed.
Add XML Representations of Field Data
Self Service
Mobile Updates
Convert Configuration Data (MagicData) to MongoDB (or others?)
Form and Page Editors
Context Sensitive Help
Web Services
Write MagicData Objects as C
Replace MDB2 (with PDO or ?)
Explore Alternative Database Types (NoSQL) for Form Storage
More Task Oriented Architecture
</poll>

===Add XML Representations of Field Data===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Defition''': [[Standard XML Representations of Field Data]]
This would create a standard way of representing form field data safely as structured xml.  Would be used by the report export as XML.

===Self Service===
:'''Status''': In Progress
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/ihris-common/+spec/self-service blueprint]
This would be an expansion of the current role/task system that would allow person records in the system to login and have access to certain information about themselves or the people they supervise.  The current access system is handled by tasks and roles.  Certain pages and template content can only be seen by users who can do the associated tasks.  With Self Service, the permission parser needs to be modified to allow checking for tasks based on the record that is being seen or modified.  In some cases there may be multiple levels of checking such as a supervisor being able to modify records of all supervised employees or a facility manager being able to view all employees working in that facility.

===Mobile Updates===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/mobile-updates blueprint]
Build an interface that can work on various levels of mobile phones to interface with iHRIS.  Perhaps using [http://www.openrosa.org/ OpenRosa].  This would allow remote users to look up or make small data updates through SMS or over the Internet.  This work would involve building the SMS gateway as well as creating an easy way for [http://andreweweww.wordpress.com/2014/01/19/lovely-mwo-muslim-wedding-organizer Wedding organizer] administrators to define pages that will be viewed and updated from the mobile application.

===Convert Configuration Data (MagicData) to MongoDB (or others?)===
:'''Status''': Not Started
:'''Difficulty''': Low
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/mongodb-magicdata blueprint]
Build a faster interface for MagicData to save using MongoDB instead of MySQL to try to improve speed to this information since it is access so frequently.  Will possibly need to retain mysql as a write storage mechanism so that magic data form storage remains fast [http://digiadvertise.wordpress.com/2014/04/07/jasa-seo-di-jakarta Jasa seo jakarta], [http://digiadvertise.wordpress.com/2014/04/07/jasa-seo-di-jakarta Jasa seo].

===Form and Page Editors===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/form-editor blueprint(forms)] and [https://blueprints.launchpad.net/i2ce/+spec/page-editor blueprint(pages)]
Build an administrative interface to allow customization of forms through the application instead of using module configuration files.  Building on that, create an interface to define display and edit pages based on the existing forms so more customization work can be done through the application instead of manually editing XML configuration files.  More information: [[Custom Forms]] and [[Custom Pages]].

===Context Sensitive Help===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/context-senstive-help blueprint]
Set up more help links within the application so users can get direct access to help instead of having to find the relevant section in the manual.  Perhaps even rewrite how the manual is used in the application.

===Web Services===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/web-services blueprint]
Build a web services interface so other applications can access and update allowed data without having to export/import at regular intervals. 

===Write MagicData Objects as C===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/magicdata-php-module blueprint]
Rewrite the MagicData PHP classes in C to speed up usage.

===Replace MDB2 (with PDO or ?)===
:'''Status''': Not Started
:'''Date Added''': 31 Jan 2013
:'''Difficulty''': High
:'''Mentor''': TBD
Replace MDB2 with a more modern database abstraction layer.  Also review any queries to utilize the database abstraction layer so it's easier to support multiple database types based on user requirements.

===Explore Alternative Database Types (NoSQL) for Form Storage===
:'''Status''': Not Started
:'''Date Added''': 31 Jan 2013
:'''Difficulty''': High
:'''Mentor''': TBD
This is to evaluate the possibility of using other database types such as MongoDB for form storage as an alternative to using MySQL.  This would need to see the possible speed issues or other problems that could arise from using other database structures besides SQL.

===More Task Oriented Architecture===
:'''Status''': Not Started
:'''Date Added''': 31 Jan 2013
:'''Difficulty''': High
:'''Mentor''': TBD
This is related to both the [[#Web Services | web services]] and [[#Form and Page Editors | form and page editors]].  This would involve creating a new page type that would be task oriented and can be called as a web service.  The user interface pages would need to be modified to call these task actions instead of complete pages.  This would require more AJAX functionality but would help to separate the display from the business logic and make it easier to create new tasks the can be based on user requirements and function by modifying multiple forms as the task requires.

===Upgrade to PHP 5.4===
:'''Status''': Not Started
:'''Date Added''': 31 Jan 2013
:'''Difficulty''': Medium
:'''Mentor''': TBD
Take advantage of the new features available in PHP version 5.4 to clean up the code when it is more widely available.


==iHRIS Modules==

<poll>
Please vote for the iHRIS Modules you would most like to see completed.
Leave Tracking Module
Leave Management Module
Mobile Roll-Call
Organizational Chart
Job Application Questions
</poll>

===Leave Tracking Module===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/ihris-manage/+spec/leave-tracking blueprint]
Add a module to iHRIS Manage to track an employees [[Leave Tracking | leave]].  

===Leave Management Module===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/ihris-manage/+spec/leave-mangement blueprint]
If done in concert with Self Service this could allow employees to request and view leave details directly.  This would involve working with users in other countries to make sure the specifications fit their needs as well as being able to generalize it for the core system.

===Mobile Roll-Call===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': TBD
:'''Launchpad Blueprint''':  [https://blueprints.launchpad.net/ihris-manage/+spec/mobile-roll-call blueprint]
The Roll-Call module is an extension of [[#Mobile Updates | mobile updates]] to allow supervisors or workers (i.e. community health workers) to log their activity.

===Organizational Chart===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': 
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/ihris-manage/+spec/org-charts blueprint]
Produce a [[Organizational Charts | org chart]] for iHRIS Manage that show employees and their supervisors.  
Could make use of the position report that has an employee and their supervisors
Two main possibilities.  Make it ajaxy and put everything on the client (maybe use canvas?), or produce org-charts on the server via graphviz.

===Job Application Questions===
:'''Status''': Not Started
:'''Difficulty''': Low
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/ihris-manage/+spec/job-application-questions blueprint]
A module to ask applicants a series of [http://www.capacityproject.org/hris/suite/UseCaseReport-iHRISManage.htm#REQ-50251c96-e13a-463c-bb24-ec1b885949dfREQ-PT10 standard questions]

==Reporting==

<poll>
Please vote for the Reporting you would most like to see completed.
Dashboard Reports
Replace Flash Charts with Images
JavaScript Charts
General Reporting Improvements
Geographic / OpenLayers Reporting
Data Entry Reports
</poll>

===Dashboard Reports===
:'''Status''': In Progress
:'''Difficulty''': Medium
:'''Mentor''': Carl Leitner
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/dashboard-reports blueprint]
The developer will Provide a new "Dashboard" page to the web-interface of this iHRIS Suite of software.  This dashboard should be expected to contain 4-6 reports targeted to the user. 

===Replace Flash Charts with Images===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/reporting-charts-images blueprint]
We would like to remove the Flash charts and replace it with images.  This can be done using [http://pchart.sourceforge.net/ pChart] or anything similar.

===JavaScript Charts===
:'''Status''': Not Started
:'''Difficulty''': Medium
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/reporting-charts-javascript blueprint]
A second step would be to add the option for using [http://en.wikipedia.org/wiki/Canvas_element Canvas] for the charts as well.  We'd like to add some additional features to the reporting to allow more complex charts to view the data.

===General Reporting Improvements===
:'''Status''': Not Started
:'''Difficulty''': Low
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/reporting-ui-improvements blueprint(report view)] [https://blueprints.launchpad.net/i2ce/+spec/report-builder-improvements blueprint(report builder)]
There are also some smaller additions like displaying all the limits chosen for a particular report so it's clear what is being displayed and improving the interface for end users to work with reports.  Interface improvements can also be made for the form relationship and report builder pages.

===Geographic / OpenLayers Reporting===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
:'''Launchpad Blueprint''': [https://blueprints.launchpad.net/i2ce/+spec/reporting-gis blueprint]
Incorporate [http://openlayers.org/ OpenLayers] and/or Google maps into the reporting system:  Reports which are tagged with geo-data (e.g. Lat and Long coordinates for a facility) will have numeric and aggregate data for the report plotted on a map.

===Data Entry Reports===
:'''Status''': In Progress
:'''Date Added''': 31 Jan 2013
:'''Difficulty''': High
:'''Mentor''': TBD
This would involve improving the User Statistics module to allow more display options for users to better evaluate the data entry as well as review changes made to the site.


==Country Implementations==
:'''Status''': Varied
:'''Difficulty''': Varied
:'''Mentor''': TBD
Countries where iHRIS is installed may have additional needs for assistance on customizations and modules.  [[Capacity Project's iHRIS Suite]] page has more information on countries where we work.  Please [http://www.capacityproject.org/hris/contact/ contact us] if you're interested in this type of work.

==Non iHRIS Ideas==

===Use Cases Wiki===
:'''Status''': Not Started
:'''Difficulty''': High
:'''Mentor''': TBD
The iHRIS Project was built using [http://en.wikipedia.org/wiki/Use_case use cases], but we would like a more open model to work on updates and customizations to our systems.  This would be a module for a wiki (whichever seems best) that will allow easier editing of use cases so this work can be shared.  It will make it easier for people making customizations to modify use cases for their purposes.

[[Category:Blueprints]]
