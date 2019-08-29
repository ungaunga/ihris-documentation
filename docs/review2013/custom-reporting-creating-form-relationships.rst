Custom Reporting -- Creating Form Relationships
===============================================

==Overview==
===Intended Use===
This is primarily intended for a developer or administrator of the system who has a good idea of how all the forms are related.  The possible connections between the different forms are already mapped out in the system.  A relationship is the description of a path between the various forms in the system.  

A relationship is, at the moment, used for [[Custom Reporting -- Creating Form Relationships|Custom Reports]].  We also intend to use it for [[Custom Pages]].

A form relationship is used to build the SQL queries used in a Custom Report.  Although you do not need to know any SQL to create a report, a passing familiarity with relational databases will help.

===Example===
You may wish to create a form relationship in iHRIS Manage that describes all current employees, their salaries,  and their supervisors.  Here is an outline of how to define this relationship:
*Start with the primary form 'person_position' and limit to those positions which the 'being_date' field is not null and the 'end_date' field is null.
*Join to the primary form the 'person' form where the 'person' form is a parent of the 'person_position' form
*Join to the primary form the 'salary' form where 'salary' is a child of 'person_position' and where the 'start_date' field for 'salary' is maximal
*Join to the primary form the 'position' form where the field 'position' of the primary 'person_position' form maps to that position.  Call this the 'employee_position' form.
*Join to the 'position' form the 'position' form where the 'supervisor' field of the 'position' form maps to that position.  Call this joined form the 'supervisor_position' to distinguish it from the 'employee_position' form.
*Join to the 'supervisor_position' the 'person_position' form whose 'position' field is the value of 'supervisor_position' form.  Call this the 'supervisor_person_position'
*Join to the 'supervisor_person_position' form the 'person' form which is a parent of the form. Call is the 'supervisor'

===Some Terminology===
*A relationship is some times referred to as a "form relationship" or a "report relationship"
*The "primary_form" is the starting point in describing the form in your relationship.
*A form can be referenced several times in a relationship. In the example above, the person_position form was referenced twice.  Once we gave it the "report form name" 'person_position' and once we gave it the "report form name" 'supervisor_person_position'.  Similarly, the person form was referenced twice and given the two distinct "report form names" of 'person' and 'supervisor'
*Some of the terminology, such as 'join,' is borrowed from SQL.

==Starting Out==
A form relationship can be created following the "Configure System" and then the "Edit Form Relationship" linka.
The first steps are to:
*select a "Display Name" for the relationship,  the name of the relationship for the end user.
*select a "Short Name" for the report, which is a way to reference the relationship internally and can only contain alpha-numeric characters and some limited punctuation such as _ and -.  
*A description of the relationship.
*The you must do one of the following:
**Choose the "primary_form" for the relationship
**Copy the details existing form relationship to modify

==Joining a Form==
Once a form, formA, is in a relationship, you can join to it any of its related forms.  You must ensure, by adding a [[#Limiting Forms|limit]], that at most one instance of the formB is joined to another an instance of formA.  There are four possible ways to join:
*(An instance of) formA is a parent of (an instance of) formB.  
**formA may have several child instances of formB.  For example, a 'person' form may have may child 'salary' forms. 
*(An instance of) formA is a child of (an instance of) formB.  
**Note that a form, if it has a parent form, is unique, so no limits are needed when joining in this manner.
*(An instance of) formA contains a [[Defining Forms#Map fields|mapped field]] whose value maps to (an instance of) formB.
*(An instance of) formB contains a [[Defining Forms#Map fields|mapped field]] whose value maps to (an instance of) formA.

==Limiting a Form==
The primary form and any joined forms in a relationship may be limited by using the [[Limiting Forms|limiting forms]] structure.  The form relationship provides a nice interface to construct form limits.

==Adding in a SQL Function==
In addition to linking in forms to a report, we can define SQL functions that can be run on the data in the forms. To reference the field named $fieldName in the form named $reportFormName in the relationship you use:
 `$reportFormName+$fieldName`
For example:
 CONACT (SUBSTR(`supervisor+name`,1,1), '. ',  SUBSTR(`supervisor+surname`,1,1) , '.')
would return the initials of the supervisor.

To define a sql function, you need to define:
*A (short) name use to reference the function.  For example, 'supervisor_initials.'
*A description of the function.  For example, "The Initials of the Supervisor."
*The form field that the result of the SQL function should take values in.  For example, "STRING_LINE"


[[Category:Custom Reporting]][[Category:Review2013]]
