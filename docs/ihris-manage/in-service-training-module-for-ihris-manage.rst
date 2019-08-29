In-service Training Module for iHRIS Manage
===========================================


Vision
^^^^^^

The In-service Training Module is a solution for managing employees taking in-service training programs, whether trainings are given by the employer or by external organizations. It should track trainings that an employee has completed and assess competencies based on those trainings; thus, it is very closely linked to the Competency Model Module that will also need to be developed. This module should enable the organization to develop and implement training plans for employees, in order to ensure that the employee meets the qualifications required for his/her job and is remaning updated on new requirements. 

This is not a module to administer a complete training program for employees, however; that is out of scope. It is assumed that training programs will be administered by external organizations, and the organization using iHRIS Manage is only interested in knowing which employees requested and completed trainings.


High-Level Goals
^^^^^^^^^^^^^^^^


* Track training programs.
* Create employee training plans.
* Link trainings that employees have completed to assessed competencies and continuing professional development credits.
* Report on completed trainings.
* Import trainings from other systems and link to competencies *(would be nice).*
* Link trainings to promotions and raises *(would be nice; probably later).*



Training Manager Role
~~~~~~~~~~~~~~~~~~~~~

A new role has been identified for this module: Training Manager. This person is a member of the HR department or an external unit, such as a training or continuing professional development unit, but is responsible solely for managing employees taking training programs and can complete no other use cases. The Training Manager can, however, create a competency model for the organization and assess employee competencies (see the separate blueprint for the Competency Model module). However, the HR Staff or HR Manager role can also complete any of these use cases, for situations where there is no dedicated Training Manager.



Specific Use Case Titles (from High-Level Goals)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 *Use cases are currently being written and evaluated. Use cases will be posted once this process is complete.* 


* Add or update training program categories. -- *The Training Manager updates the list of training program categories for selection within the system.*
* Add or update a training funder. -- *The Training Manager adds details about a training funder to the system.*
* Add or update a training organization. -- *The Training Manager adds details about a training organization to the system.*
* Add or update an in-service training program. -- *The Training Manager adds a training offering to the system that can be requested for Employees to complete.*
* List training programs. -- *The Training Manager produces a list of all available trainings.*
* Request a training for an employee. -- *The Training Manager adds an employee as a registrant for a training program.*
* Assess training results and update competencies. -- *After an employee has completed a training, the Training Manager assesses their performance and updates their qualifications accordingly.*
* Report on employees trained. -- *The Executive Manager or Training Manager generates a report on employees who have completed training programs.*



Suggested Reports
~~~~~~~~~~~~~~~~~

These are in addition to the reports already listed in the use cases.



* Are the right people attending the right trainings at the right time?
* Who requires training?
* Who is requesting training/What type of training?
* Who took trainings? When?
* How many people were trained in X?
* How many people were trained in X by cadre?
* How many people were trained in X by region or district?
* How many people were trained by funder?
* How many people were trained by training organization?
* Who is qualified to perform a particular training?
* Does a training a person completed qualify an employee for promotion, position, competency?
* Emergency training programs
* Training needs assessment - *this needs to be thought out*

There are lots of report examples in JHPIEGO's TIMS system and in the NSDP system.


Out of Scope
~~~~~~~~~~~~

The following have been determined to be out of scope for this module:



* **Adminster a training program**  -- this is most likely a separate system (iHRIS Train).
* **Manage scholarships awarded to employees**  -- this is a separate module to be developed at a later time (on wishlist).


Affected Systems
^^^^^^^^^^^^^^^^



* Pilot is in Tanzania implementation of iHRIS Manage.
* Implement in IntraHealth iHRIS Manage by **June 30, 2008**
* Planned for inclusion in version 3.1 release/upgrade of iHRIS Manage


Sources
^^^^^^^


* Bangladesh NSDP HRIS
* JHPIEGO TIMS
* Hareg training tracking database
* Learning for Performance (IntraHealth)
* CBT (JHPIEGO's competency model)

