Use Case:PR-UI-5
================

{{UseCasePage|System must provide user restricted security to its ?configuration? (maybe we mean administration). 
 |number=PR-UI-5
 |description=Provide user authentication method to access administration of PR
 |actor=Provider Registry Administrator
 |preconditions=The user is logged out of the system.  
 |success=An administrator is successfully logged into the system with the access to the data set determined by role
 |resources=
 |mss=

* The user browses to "login" page
* The user enters name and password
* The system returns to the "home" page
 |notes=Role of user/data sets that user can access should be based on the domain of provider data as identified in [[Provider Registry Requirements#Security and Access Level | access level]] requirements
}}
