Leave Tracking
==============

This is a draft of a blueprint for a leave tracking module. The purpose of the module would be to track time used by employees for various types of leave.

Administration
^^^^^^^^^^^^^^

Before the module could be used, database standards would have to be defined by an HR Manager:

* Define leave type (such as vacation, sick time, holiday, maternity leave, unpaid leave, etc.)
* Define specific holidays that are paid time off
* Defined leave request status (such as approved, rejected, canceled, pending approval, leave taken)
* For each employee and type of leave, enter the number of days per time period of leave that the employee is entitled to. This enables leave taken to be compared to total leave time allocated.

Assign Leave
^^^^^^^^^^^^

The HR Staff person would assign leave to an employee who has requested it. In a self-service system, an employee would use this procedure to request leave.

* Select the employee.
* Select the type of leave requested.
* Select the start date.
* Select the end date. (Assume all leave requested is for full working days.)
* If the requested leave is for less than one day -- the start date and end date are the same -- enter the start and end time or number of hours requested.
* Add any comments or notes on the request.
* The system should alert the person if they have requested more leave than they are entitled to for the time period.

Review Leave
^^^^^^^^^^^^

An HR Staff person or HR Manager reviews leave requests and selects a response. This might be triggered by an email sent to the HR person when the leave is requested.

* Open the employee record. Or open a list of all leave requests, sorted by status and by date.
* Review the leave request.
* Select or update a status for the leave.
* The system sends an email to the employee to notify him/her of the response to the leave request.

Leave Summary Report
^^^^^^^^^^^^^^^^^^^^

* Select a date range for the report.
* If desired, filter by employee, leave type, other factors to be determined.
* The report displays the employee name, the type of leave, the total amount of entitled leave, the amount of leave taken, the amount of leave scheduled, and the amount of leave remaining.

