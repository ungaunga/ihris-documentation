India Payroll Module
====================

This page details the India Payroll Module

==Use Case Narrative==

The Payroll module should allow users to do the following:

* Set salary breakdown for each employee depending on the terms of employment. India has Contractual and REgular employees

* Calculate Monthly Salary for each employee based on the salary breakdown and the number of working and leave days for each employee in a given month

* Print Salary Receipts (Slips) for each employee individually and in bulky

* Export monthly salary report for all employees for submission to the state salary department


==Configuration and Use==

===Configuration===
* You will need to set the working days for each month in a given year.
** Click '''Payroll Functions''' then '''Set Monthly Working Days'''
** Click '''Add new Monthly Working days''' and fill out the month and the number of working days and save.
***Next you will need to set the salary breakdown for all employees. Pick out any report that will give a link to the individual records.
**On the individual page Scroll down to Position Information:
***You should see '''Set Salary Breakdown''' and clicking on this link should open up a form where you fill out the breakdown and save. This is to be set once until there is a change in the salary structure, otherwise you can go back and edit what is already set.
** A cron job runs a script to set the month for the payments for each employee. (Depending on when salaries are processed, this can be set to run at any time of the month.

===Use===
* After the script has finished, open '''Payroll Functions''' then '''Set Monthly Salary'''. A report opens up where you have to set the total leave days an employee has taken for this month and the number of days an employee has worked in the month.
* Once that's all set, you can now download the salary receipt (slip) for individual employee ('''Print Salary Slips''') or in bulk ('''Regular Employees Salary Receipts''' and '''Contract Employees Salary Receipts''')

==Forms, Pages and Reports==
===Forms===
* working_days: [class: iHRIS_Bihar_WorkingDaysList]
** List form for capturing working days in a month in a given year. The number of working days is used to calculate the average daily salary for an employee
* person_position_salarybreakdown [class: iHRIS_Bihar_SalaryBreakdown]
** This is a child form of person.
** Use this to set the salary breakdown for an employee.
* person_monthly_salary [class: iHRIS_Bihar_MonthlySalary]
** This is the form that captures the monthly salary for an employee including number of working days, number of leave days and the net salary payable for that month
* position_type [class: Bihar_PositionType]
** this extends I2CE_SimpleList to add a field for capturing salary receipt template

===Pages===
* salarybreakdown: page for setting salary breakdown from class iHRIS_PageFormSalarybreakdown
** the module class iHRIS_Module_Payroll is responsible for setting required fields and doing validations
* person_monthly_salary: page responsible for calculating the net salary for an employee. It is provided by class Bihar_PageForm_Monthly_Salary
* setmonthlysalary: uses class iHRIS_BiharPageSetMonthlySalary (which extends I2CE_PageReportAction) to display a report form for capturing working and leave days.
** It is required to specify a report_view that will be used to create the form
* employee_salary_slip ''[URL only]''* page for printing individual salary slips for each employee
** The page is handled by the class Bihar_PageActionSalarySlip
** It is required to specify a report relationship from which the salary slip template is going to pull data from
** Need to specify the template_upload (base64 encoded ODT Template) field where the salary receipt template is uploaded
* print_salary_slips: page for handling downloading of individual salary slips which uses iHRIS_BiharPagePrintSalarySlips class
** It is required to specify a report_view to which the links to download the slips will be hooked

<small>[URL only]: only accessible internally by the system</small>

===Reports===
* Regular Employees Salary Receipts
** Used to download salary receipts for regular employees
* Contract Employees Salary Receipts:
**Used to download salary receipts for contract employees
[[Category:India]]
