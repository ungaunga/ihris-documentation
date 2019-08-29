Custom Reporting -- An Overview
===============================

The Custom Reporting is a three part process:
*[[Custom Reporting -- Creating Form Relationships|Create A Form Relationship]]  This defines the relationship between the data in the system.  It is intended for a relatively advanced user that has some understanding on how the data is related.
*[[Custom Reporting -- Creating Reports|Create A Report]] Choosing, a form relationship, this specifies the data fields for a report as well as the limits allowed for the various views of the report.  It is intended for a data manager.  Only a moderate understanding of the way the data is related in the system is required.  It is in this step that generates the cached 'zebra_XXXX' report tables.
*[[Custom Reporting -- Creating Report Views|Create A Report View]].  This is intended for all end user's that might need to create a different view of a report.  For example, it would be useful for someone who needs to generate monthly reports for different slices of the data.

==Tasks==
There are a several tasks that control general access to the creation and view of custom reports:
*'''custom_reports_can_access''' Allows minimal access to the Custom Reporting System System
*'''custom_reports_delete''' Allows deletion of data defining custom reports
*'''custom_reports_can_access_relationships''' Allows access to the Custom Report Relationships
*'''custom_reports_can_access_reports''' Allows access to the Custom Reports
*'''custom_reports_can_view_reportViews''' Allows view of the Custom Report Views
*'''custom_reports_can_edit_reportViews''' Allows editing of the Custom Report Views
*'''custom_reports_admin''' Administrator for custom reports.  Can perform all tasks associated with custom reports

In addition you may also limit access to a specific Report View $view by specifying:
 /modules/CustomReports/reportViews/$view/limit_report_to
to be any valid [[Tasks and Roles#Permissions and the Permission Parser|permission]] string.

[[Category:Custom Reporting]][[Category:Review2013]]
