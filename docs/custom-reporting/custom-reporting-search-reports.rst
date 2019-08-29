Custom Reporting -- Search Reports
==================================

The search page makes use of the custom reporting module to allow you to easily customize the search page and add new searches to the system.  This is a two step process:

* [[#Creating A Search Report | Creating A Search Report]]
* [[#Registering A Report With The Search Page | Registering A Report With The Search Page]]

Creating A Search Report
^^^^^^^^^^^^^^^^^^^^^^^^
You should create a report view that you will want to use for the search page.  It should include all the fields that you want and limits that you need.  You can also modify the existing report view in the system, such as "Search People" to adjust the fields that get displayed.    You may wish to see how to [[Custom Reporting -- Creating a Staff List Example | create a staff list]].  

One thing to keep in mind, you should add the appropriate link to the fields in this report, for example adding the link "view?id=" to any of the fields in the person form will allow you to link to the view page for that person.

You can modify the existing search reports to suit your needs.  For example, you may wish to join the "id" form to the person form and limit the "id" form it to "national identification" number if you have such a thing.  Then in the report, you can add a limit to search by the national identification number.


Registering A Report With The Search Page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Registering a report view is done by defining magic data under:
 /modules/CustomReports/search_reports

See  ` lines 511-525 <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/view/623/iHRIS-Manage-Configuration.xml#L511>`_  of the iHRIS Manage configuration file for an example on how the **search_people**  and  **position_list**  report views are registered with the search page.  The result is the following:


* /moudles/CustomReports/search_reports:  Required parent node.  All report views that are linked to the search page need to be registered here
* *search_people:  Required parent node.  This is the name of the report view that you wish to register under the search page.  Here the report view is "search_people"
* **name: Required scalar node.  This is the name of the search as it appears on the search page.  In this case it is "Search People"
* **description: Required scalar node.  These are the instructions that are shown with this search.  In this case it is "Locate any person's record in the system to review, print or update."
* *position_list:  Required parent node.  This is the name of the report view that you wish to register under the search page.  Here the report view is "position_list"
* **name: Required scalar node.  This is the name of the search as it appears on the search page.  In this case it is "Search Positions"
* **description: Required scalar node.  These are the instructions that are shown with this search.  In this case it is "Locate any position in the system to review, print or update."

[[Category:Custom Reporting]][[Category:Review2013]]
