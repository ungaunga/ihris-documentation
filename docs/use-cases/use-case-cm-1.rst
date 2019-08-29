Use Case:CM-1
=============

{{UseCasePage|Create A Competency Model
 |number=CM-1
 |description=The Training Manager updates a list of competency categories or competencies.
 |actor=Training Manager? HR Manager?
 |preconditions=The user must be logged in to the system.
 |success=The new competency is saved and linked to any selected parent category, and it is available for selection in various use cases.
 |resources=[http://wiki.ihris.org/wiki/index.php/Competency_Model iHRIS Competency Model]
 |mss=
#The user selects the option to update the competency model.
#The system displays a list of competencies organized by category.
#The user adds a new competency.
#The user selects whether the item is a parent category.
#The user enters the name of the item.
#The user enters a definition for the competency.
#The user saves the record 
#The system makes the competency available for selection when adding competencies to a record.
 |extensions=
:3.a The user selects an existing competency.
:#The system opens the competency for editing.
:3.b The user selects an existing parent category.
:#  The system provides the option to add competencies underneath the parent category.
:4.a  The user designates the competency as a parent category.
:#  The system enables competencies to be added beneath the parent category.
:7.a  A system determines that the competency with the same parent categories already exists in the database.
:#  The system displays an error and will not continue.
}}
