Employee, Supervisor and Manager Roles for iHRIS Manage
=======================================================

Three additional roles have been proposed for iHRIS Manage: Employee, Supervisor and Manager. There is also need for a fourth role for external job applicants (see below). 

The purpose of these roles is as follows:

* **Employee** : Enables a person to log in to the system and update his/her own record (a "self-service" option). This will be useful for recording contact information changes or requesting trainings, for example.
* **Supervisor** : Enables a person to log in to the system and view or update the records of any employee s/he supervises, as well as produce reports showing only data about that person's supervisees. This will be useful for recording performance assessments, for example.
* **Manager** : Enables a person to log in to the system and view or update the records of any employee working in a department, office or facility that s/he manages, as well as producing reports showing only data about that department, office or facility. This will be useful for providing limited access to data to middle-level managers. **NOTE: The Manager role has been tabled.**

 *While some information and notes have been added to the use cases to support these roles and the actors have been defined in the use case model, the documentation has not been completed.* 

 **This feature request is a priority for IntraHealth's implementation of iHRIS Manage and should be completed by June 30, 2008.** 

The Guest or Applicant Role
^^^^^^^^^^^^^^^^^^^^^^^^^^^

A fourth role that will also need to be implemented is **Guest**  or **Applicant** . (The Guest role is referred to as the Applicant actor in the use case model.) Logging in with a guest account (a generic username and password) would enable a user to have access to the job application form, select one or more positions to apply for, and add educational and employment history and skills only. 

Log in will generally be through a public website. For example, on the Jobs page of the IntraHealth website, there will be a button **Apply for Position**  beside each posted position. Clicking that button will take the applicant to the login page, where s/he can initially log in as a guest or create a new login. 

When the guest logs in, s/he may select one or more positions to apply for and complete an application form. The application form consists of the job applicant questions plus educational history, employment history, languages and skills. The applicant will also need to provide demographic information and contact information. At that time, s/he may enter a password to access the system at a later time and update the application information only. However, the user will not have access to any other functions or information unless s/he is assigned to a position and thus converted to an Employee.

Logging In
^^^^^^^^^^

It is proposed that users with these roles would first log in as a **Guest** . Then, if they have an employee record in the system, they can authenticate against the First Name, Surname and Password stored with the employee record (the Password feature has not been implemented in the current version of iHRIS Manage). Their role in the system is determined from data stored in the employee or position record. 

 *This is a proposal only and may be changed if necessary. This login procedure has not yet been documented but would be added to the Log In use case (UC-PT48).* 

Employee Role
^^^^^^^^^^^^^

Next to Guest/Applicant, the Employee role is the most limited of all roles. The Employee can only view and update his/her own record. The Employee can only update his/her own demographic and contact information; all other information can be viewed but not changed. The Employee cannot view identification information, or identification numbers should be obscured.

The Employee will be able to complete a job application and, so long as the position is open, add new skills and educatonal and employment history in order to apply for open jobs in the organization. The Employee cannot view other staff records or reports.

The Employee is considered to have left the organization's employment when a position change is recorded but no new position is set for the Employee. The Employee then becomes an Old Employee and should be denied access to the system except as a Guest/Applicant.

Supervisor Role
^^^^^^^^^^^^^^^

The Supervisor role should be set for any person who fills a position that supervises other positions. The Supervisor can view the records of the Employees that s/he supervises. These shall be all Employees in a reporting line underneath the Supervisor, i.e., all Employees that the Supervisor directly supervises and all Employees that they supervise (and so on). The Supervisor cannot update or change any data in the Employee records. The Supervisor cannot view identification information, or identification numbers are obscured.

The Supervisor may review applicants for open positions that s/he supervises. 

The Supervisor may have access to some reports, such as the Position List, but those reports should be limited only to data about the Employees s/he supervises. (Viewing reports is a lower priority for development.)

The Supervisor role will be important for any Performance Management module to be developed, and may also be useful for assessing employee competencies (see the Competency Model module). 

Manager Role
^^^^^^^^^^^^

 **The Manager role is lower priority, and development of this role has been tabled for now.** 

The Manager role is not as clearcut as the Employee or Supervisor role. The Manager is also an Employee and may also be a Supervisor if s/he directly supervises other positions. But the Manager is defined as a Manager of a department or office/facility. Therefore, this role would be set for any person who fills a position that is marked as a Manager of a department or an office/facility. Alternatively, the Manager position can be selected with the department or office/facility information is added to the database. (This feature is not supported in the current implementation.)

The Manager's primary function would be to review reports, but data displayed in the reports would be limited to employees/positions in the department or office/facility that the Manager manages. Therefore, the Manager role is a scaled-down version of the Excecutive Manager role -- a middle manager with less access to data. (The Executive Manager can view all data and reports.) 

The Manager can also view records for employees in the department or office/facility, but cannot update the records, just as the Executive Manager can do for all records. The Manager should also be able to review job applications for open positions in his/her department or office/facility, just as the Executive Manager can do for all open positions.

There may also be managers of *districts* , but this has not yet been finalized.

