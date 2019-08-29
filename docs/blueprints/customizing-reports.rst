Customizing Reports
===================

There is a need in both iHRIS Manage and iHRIS Qualify to enable users to create their own reports and view, print and export them just like any other report. In addition, customized reports will need to be saved and then accessed later with updated data.



Scenario
^^^^^^^^


The proposed scenario for creating and saving a customized report in either system is:

The user accesses the Create Reports option and selects an option to create a customized report. The system displays a wizard-like interface that enables the user to:


* select which fields to show in the report
* the primary and secondary sorts for the data
* any filters to limit the data (or the same filters as used for other reports could be available, such as date range, geographical location, etc.)

Because not all data fields will be used in all systems, it would be ideal if the system only allowed the user the option of selecting those fields that actually contain data. Also see security concerns below.

The report should be displayed as tabular data. Customizing a charted report is a bit more complex and out of the scope of this blueprint.

Once the report has been produced, the user should have the option to change the sort to any field, to print or export the report, or to adjust the filters. The user should also have the option to save the report and to give it a meaningful title. Once the user has saved a report, when the user logs back in, the report should be available in the user's list of saved reports. Opening the report redisplays it but with updated data.

It would be nice, if the user is a System Administrator or Data Operations Manager, to give the user the ability to save the report to a master list that any other user can access and to limit access to specific roles. This would eliminate the need to have a developer create new reports every time one is needed.


Security Concerns
^^^^^^^^^^^^^^^^^


We must be cautious about linking roles to the types of data that different users can display in custom reports. We should identify which data fields (salaries, identification numbers, etc.) should be restricted and what roles have permission to view that data. If the user's role does not have permission to view that type of data, the field should not be available for inclusion in a custom report.



Use Cases
^^^^^^^^^

The use cases for customizing reports are the same for iHRIS Manage and iHRIS Qualify. They are documented in the common use cases (available in the full use case model for either system) in the package titled "Reporting." 



* `Full Use Case Model - iHRIS Manage <http://www.capacityproject.org/hris/suite/UseCaseReport-iHRISManage.htm>`_
* `Full Use Case Model - iHRIS Qualify <http://www.capacityproject.org/hris/suite/UseCaseReport_iHRISQualify.htm>`_

