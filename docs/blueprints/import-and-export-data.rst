Import and Export Data
======================


The Problem
^^^^^^^^^^^

In most countries, there is a need to manage human resources data at the lowest level of employment: the hospital, clinic or local government. But data must be aggregated to the national level for reporting and decision making.

In many areas, Internet infrastructure is not sufficient to support updating a central system from decentralized locations. We developed Offline iHRIS as a solution where Internet is unreliable or unavailable. 

When instances of iHRIS are installed in several different locations, whether Offline iHRIS or a server-based version, there is a need for exchanging data between systems. Data must be pushed up from the local system to the central system for reporting. Standard data lists must be pushed down from the central level to the local level to update dropdown menus. There is also the issue of people moving to other facilities or districts and how their data can follow them or how duplicates in the system can be prevented.

Finally, security and privacy are concerns. There may be reluctance for districts or facilities to share data with one another.



Server Hierarchy
^^^^^^^^^^^^^^^^

There are two proposed methods for managing server hierarchy:

 **Method 1: Central Server is for reporting data only; all records are updated via separate sites underneath the Central Server.**  


.. code-block::

       1. Central Server
          a. Ministry of Health employees -- updated at the central level but via separate site
          b. All regional hospitals -- updated at the central level but via separate site
          c. District A
             i. All clinics
             ii. Facility A
             iii. Facility B
          d. District B
    


 **Method 2: Central Server is for reporting data and for updating records housed at the central level** 


.. code-block::

       2. Central Server with MOH and regional hospital records
          a. District A with clinic data
             i. Facility A
             ii. Facility B
          b. District b with clinic data
    


For ease of data synchronization, Method 1 is preferred. To alleviate confusion for people maintaining records at the central level, we can customize an entry page to facilitate accessing reports and updating records housed in separate sites but at the central level. We also suggest creating a district called "Central" or something similar to distinguish facilities managed directly by the central MOH from facilities managed by the local districts.



Unique Identifiers
^^^^^^^^^^^^^^^^^^

Each record should have a unique identifier. To prevent duplication, all sites that can import/export to one another should use the same identifiers for the same records and dropdown items.

It might also be necessary to identify an identification number for each employee that can be printed on forms and other paper documents used for updating the system. If used consistently, this identification number would quickly allow a data entry person to access a person's record if it already exists in the system. The identification number will vary from country to country.

In Uganda, for instance, the **computer number**  could serve as the unique identifier, as it never changes if staff move from one district to another.



Data Standards (Dropdowns)
^^^^^^^^^^^^^^^^^^^^^^^^^^

Data standards are enforced via dropdown menus for common elements, such as geographical locations, job classifications and jobs, cadres, marital status, etc. In a standard installation, the data manager can update these lists. With multiple decentralized installations, this can lead to discrepancies in spelling or phrasing for data elements that are the same.

To prevent this, the base data should be set and enforced at the central level. These standard data elements should be pushed down whenever updated to all installations in the hierarchy. At the lower levels, these data items should be locked and should not be editable. 

The exceptions might be:


* facilities
* positions

As much as possible, these standard lists should be set up when the system is initially installed at the central level.



Updating Records
^^^^^^^^^^^^^^^^

Person records -- perhaps also facility and position records -- should only be updated at the level of employment, the lowest level in the hierarchy where the health worker is actually located. For example, a facility employee's record is created and updated at the facility level, but is not edited at the district or central level. This will prevent discrepancies among records.

At regular intervals, there should be uploads through the hierarchy. For example, the facility data is uploaded to the district. The district's data is then uploaded to the central server. This enables the facility to report on all health workers employed at the facility, the district to report on all health workers employed at all facilities in the district, and the central Ministry of Health to report on all health workers employed in all districts.

Data transfer can occur over a network (preferred) or via physical transfer on USB or CD for locations that do not have reliable connectivity or electricity service.

In case the data transfer is not completed or is interrupted, there should be a rollback feature. This would enable the system administrator to roll back the data to the state it was in before the transfer was started and restart the transfer from the beginning, rather than try to determine where the transfer was interrupted or what data were not transferred.



Issues
^^^^^^

 **Person A leaves employment in one district/facility and enters employment in another district/facility.**  


* How are duplicate records prevented?
* How is that person's data shared?

When Person A leaves employment in District A, District A updates the person's record as terminated. District A updates the central server with this change. However, Person A may be employed in District B before this update occurs.

District B creates another record for Person A when s/he is employed and updates the central server with the new record. Now there are two records existing for Person A.

District B does not have access to Person A's record in District A, so District B cannot know Person A's work history.


Scenario 1
~~~~~~~~~~

Whenever an update occurs to the Central Server, the data manager for the system is alerted to potential conflicts. Items that might be compared are names and unique identification numbers. 

At the Central Server level, the data manager must have a method for merging duplicate records. This currently does not exist in the system.

The merged record is then pushed back down to District B.


Scenario 2
~~~~~~~~~~

Basic people data is pushed from the central server to all sites: name, position, employing facility, identification number.

Before District B creates a new record for the employee, they are required to search the system for an existing record. If a match is found, any new data for that person is appended to the existing record so that the same identifiers are used. 

District B can request from the central server to transfer the employee's record ownership to them. If approved, the entire record is pushed down to District B and District B can now access the full record but cannot update the employment history at other districts.


Scenario 3
~~~~~~~~~~

District A and District B maintain their own records for Person A's employment in that district. The two records are never merged at the district level.

At the Central Server level, the data manager is alerted when two records exist for the same person, via the unique identification number. The data manager can then link the two records for reporting purposes. 

The linked or merged data is not pushed back down to the district level.



Importing Data to the Central Level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is the general process proposed for importing records at the central server location (such as the Ministry of Health):


* Data will be imported via an import/export page.
* Upon import, the new data are first saved to a temporary table and marked as disabled.
* The data must be verified by a data manager, who will check for duplicate records using the data check procedure (which is a separate use case). The data manager is given the option to merge any duplicates.
* The data manager then verifies the import, and it is saved permanently. If the import is a mess, the data manager will not verify so as not to compromise the integrity of the central system's data.

 *The first step then is to build the data checking function to look for duplicates and merge or disable them.* 



Exporting Data
^^^^^^^^^^^^^^

Data will be exported based on logical groupings, or the relationships of data. Therefore, all positions might be exported together, facilities exported together and people records exported together. A complete data dump might require several exports.

Exports will probably be built using the reporting relationships, but there will be a separate page for export functions. 



Questions for the Countries/HRIS Advisors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- What systems exist for districts/facilities to inform the Ministry of Health of personnel changes: hires, fires, transfers, promotions, etc.?

 **Answer (Uganda):**  The districts were decentralized so they carry out there own hires, fires, transfers and promotions hence they don’t inform the Ministry of Health personnel about these decisions. Districts are autonomous; they may or may not inform the Ministry of Health personnel of these changes – Refer to diagram: Sheet 1.


- What paper forms exist to support these systems? (provide examples)

 **Answer (Uganda):** 


* Pay change report
* Transfer letter
* Local last pay certificate

Forms are filled out by Accounts and personnel officer
Forms are sent to Ministry of Public Service
Forms are approved by Chief Administration Officer (CAO)


- Are any identification numbers used to identify employees of the public health system? Are they unique within the entire system?

 **Answer (Uganda):**  Yes, it is called the Computer Number. The numbers are actually used to identify the PUBLIC SERVANTS not only the public health. Even if one leaves the health workforce and moves into the energy workforce, they still maintain the same Computer Number.


- How are hires, fires, transfers, salary changes approved, and by whom? 

 **Answer (Uganda):**  Hires and fires are carried out by the Service Commissions i.e. District Service Commission at the District while Health Service Commission at the Central Unit. Refer to diagram: Sheet 1.

Transfers are done by the Ministry of Public Service at the Central Level while Chief Administrative Officers effect the transfers at the districts.

Salary changes are prepared by the respective unit personnel officers i.e. district or central unit and sent to the Ministry of Public Service to endorse the changes i.e. pay change reports.


- What happens when there are breakdowns in the system, i.e., a district doesn't inform the central Ministry of personnel changes?

 **Answer (Uganda):**  Good one. There are two scenarios here. ONE: If there is an internal movement of staff from district A to district B but the personnel at district A doesn’t release that staff hence creating a GHOST WORKER SITUATION, it will be identified by the system at the central level as illustrated in the Issues scenario 3. TWO: If a staff leaves the health system and moves to the private sector e.g. personal business, it becomes hard to tell at the Ministry because the personnel could retain that staff on the pay roll hence creating a GHOST WORKER. The Government looses but when they identify this case, the staff is immediately deleted from the pay roll. We need to see how we can help with this case.


- What are data privacy and security issues or concerns between facilities, districts and the central Ministry?

 **Answer (Uganda):**  Data between facilities, districts and the central Ministry is provided basing on formal request. In most cases data is freely shared.


- Provide any standard lists such as post lists, job classification/codes, salary bands, etc.

Provided by Uganda.


