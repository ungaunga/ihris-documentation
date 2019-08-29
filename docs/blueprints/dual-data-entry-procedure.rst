Dual Data Entry Procedure
=========================


Vision
^^^^^^

Dual data entry is envisioned as an important data quality and integrity tool for both iHRIS Manage and iHRIS Qualify. Dual data entry is most useful when multiple people are entering data from a backlog of paper records or transcribing data from paper forms.

The purpose of dual data entry is to ensure that each record (specifically, object) is entered twice, preferably by two different data entry persons. The two entries are compared to one another, and the system flags any discrepancies for review and correction. This process reduces the likelihood of bad or incorrect data being introduced into the system. 

Dual data entry should be an optional function that can easily be turned on or off via a configuration screen by the System Administrator. This will actually disable the links to verify the data. If turned on, then all objects will be marked "unverified" and require dual data entry.


Dual Data Entry Process
^^^^^^^^^^^^^^^^^^^^^^^


Step 1: Entering a New Record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upon saving a record, the system should check whether the record is a) New, b) Updated or c) Corrected. The system should determine this from the action the user took to access the Edit screen. The system should also determine whether the record (specifically any objects within the record) is subject to dual data entry. Some records are exempt such as list updates by a data manager or user account updates by a System Administrator. 

 *We may want to exempt all records that are updated by an HR Manager, Data Operations Manager or System Administrator from dual data entry. New roles, such as Employee, Supervisor and Manager, will also be exempt from dual data entry.* 

If the record is new and subject to dual data entry, the system marks it as "unverified" upon saving. Once a record is marked "unverified," it is made available for re-entry. (Actually, only the objects that are flagged as subject to dual data entry will be re-entered.) A record does not have to be re-entered for that data to be made available to reports and viewing.

Note that updated or corrected data would not be subject to dual data entry.

The system also logs the date of entry and the username of the person who entered the record. This information will be used for error reporting.


Step 2: Processing an Unverified Record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The system enables a data entry person to list all of the unverified records and select a record to re-enter. This is helpful when entering data from paper forms. Alternatively, when re-displaying a record that has been previously entered but marked as "unverified," the option to perform dual data entry will be displayed as well. 

Re-entering an unverified record is just like entering a new record: The user is presented with a blank form and fills in the fields. This time, when the record is saved, the system compares the two versions and displays a confirmation screen with any discrepancies between the two highlighted. The second data entry person is expected to review the discrepancies, compare the entered data to the original paper record, and either select the correct entry or enter new, correct data.

The system would mark any corrected fields (objects) as "corrected" and the incorrect entry logged as an error for reporting purposes. The record as a whole (or any unchanged objects) would be marked "verified" and would no longer be listed as a record needing to be processed.

Note that if an object is changed after verification, it should be flagged as "updated," not "corrected." An update is considered to be a change to previously correct data, such as a name change or change in marital status. Data entry staff can update data but cannot correct verified data.

There is a second way for data to be corrected in the system. Usually, only the HR Manager/Data Operations Manager or System Administrator can correct data that have been entered previously via the "Correct this information" option. When any data (objects) are corrected in this manner, the system also flags that data as "corrected" for error reporting. The Manager can correct either verified or unverified objects.


Step 3: Spot-Checking Data
~~~~~~~~~~~~~~~~~~~~~~~~~~

The Data Operations Manager or HR Manager has the ability to spot-check any records for errors. These can be unverified or verified records. This assumes that the Manager has access to the paper originals and is spot-checking data from the original.

The system provides a Spot-Check Records option that is only visible to the Data Operations Manager/HR Manager and System Administrator roles. After selecting this option, the Manager can specify whether to spot-check all records or limit to a date range. This is helpful if the Manager only wants to check records that have been entered since the last date s/he checked. 

The system displays a random sample of records entered or changed during that date range (see UC-PT18 for details on how many records are displayed under different conditions). The Manager can select any one to review it and correct any errors. The system flags any corrected objects as "corrected". Once each record has been checked, the system removes it from the list of records to spot-check. The Manager may spot-check as many records as s/he likes; the system will provide the option to redisplay a random sample until all records in the date range have been checked.


Step 4: Error Reporting
~~~~~~~~~~~~~~~~~~~~~~~

The system should be able to produce several reports based on this information. These reports should only be accessible by the Data Operations Manager/HR Manager and System Administrator. All reports can be filtered by date range.



* Total number of records that have been spot-checked and percentage of all records that have been spot-checked
* Total number of spot-checked records that had errors and percentage of all spot-checked records that had errors
* Total number of records that have been verified and percentage of all records that have been verified
* Total number of verified records that had errors and percentage of all verified records that had errors
* For each data entry person, report on the total number of records that person entered compared to the total number of records entered overall
* For each data entry person, report on the total number of errors the person made that were corrected compared to the total number of objects the person entered


Issues
^^^^^^

The procedure outlined above is how dual data entry is conceived to work within these systems, but some adjustments may have to be made for the design or limitations of the system. These are the issues we've identified:


* How is a record defined? Is it the total amount of information related to one person entered in the system? Or is it limited to one data entry screen (such as entering a training program in iHRIS Qualify or changing a position in iHRIS Manage)? Or can it only be limited to individual objects?
* Can the username be linked to the form or record that the user is updating? Is the link to the entire form or to a specific object only, if it can be made at all?

Of course, there will be a way for any smart user to defeat any dual data entry system. For the system to work properly, it relies heavily on enforcement by a "data manager" role (the Data Operations Manager or HR Manager). Without this role systematically checking for incorrect data and reviewing reports on errors rates to identify where more data entry training or discipline might be needed, the system has no value.


Documentation
^^^^^^^^^^^^^

The dual data entry procedure is identical for iHRIS Manage and iHRIS Qualify. The procedure is documented more fully in the iHRIS Common Use Cases (included in each system's full use case model) in the package titled "Dual Data Entry."



* `Full Use Case Model - iHRIS Manage <http://www.capacityproject.org/hris/suite/UseCaseReport-iHRISManage.htm>`_
* `Full Use Case Model - iHRIS Qualify <http://www.capacityproject.org/hris/suite/UseCaseReport_iHRISQualify.htm>`_
[[Category:Blueprints]]
