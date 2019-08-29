UseCase:CM-3
============

{{UseCase|Assess an employee's competencies
 |number=CM-3
 |description=The user adds to or updates the list of competencies obtained by an employee.
 |actor=Training Manager? HR Staff?
 |preconditions=TThe person has a record in the system. The user must be logged in to the system. The competency and competency evaluation must be added to the system.
 |success=The employee's competencies are saved and displayed with their record, the evaluation history for each competency is updated, and the competencies are available for searching.
 |mss=#The user selects the option to add competencies to a person's record.

* The system displays the competency model.
* The user selects the competency to add.
* The user selects the competency evaluation (optional).
* The user selects the date of the evaluation.
* The user enters a date when the assessment expires or should be re-evaluated (optional).
* The system sets a flag to appear on the person's record when the date has passed that reminds the user that the person needs reassessment.
* The user saves the record
* The system saves the competency information and displays it in the record.
* The system provides the option to update the competency or view the evaluation history for any competency.
 |extensions=
:3.a  The system detects that the competency is a parent category.
:#  The user checks the category to add all subcategories and competencies within that category to the record.
:#  The user expands the category to select subcategories or competencies within the category for addition to the record.
:5.a  The user does not select an evaluation date.
:#  The system enters today's date by  default.
}}
[[Category:Use Cases]]
