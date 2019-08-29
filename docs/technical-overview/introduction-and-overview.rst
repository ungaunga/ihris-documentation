Introduction and Overview
=========================

iHRIS makes use of multiple tables in a relational database (MySQL) to store its data in. [[Database Structure]] describes several of the tables used by iHRIS, in particular the user table and the tables used for [[Form Storage -- Entry/Last Entry|audited form data changes]].

Modules
^^^^^^^
This tutorial describes the iHRIS [[Module Structure]]. An iHRIS module is a collection of various types of "code" by the features that they provide to the system. Modules serve as the building blocks of iHRIS and are grouped according to the functionality they provide. 

[[Modules Lists]] are links to the various [[Module Structure|modules]] used by iHRIS. 

File Search Paths
~~~~~~~~~~~~~~~~~
The [[File Search Paths|File Search Utility]] lets you easily categorize different files and make them available to iHRIS. It also allows you to copy a file from the core iHRIS Suite into your site customization to make changes there, without having to modify the core iHRIS software. Most often this is used to customize HTML templates or CSS files.

Configuration (Magic) Data
~~~~~~~~~~~~~~~~~~~~~~~~~~
[[Configuration (Magic) Data|Magic Data]] is a mechanism intended to handle dynamic site-level configuration data. It is the basis of much of the functionality provided by the IntraHealth Informatics Core Engine (I2CE), including how pages are served and how custom reports are made. 

Magic data provides a central mechanism for configuring iHRIS. This magic data is stored in a database table. Due to frequent access of the data, a caching mechanism is needed to keep the database load down. For this reason, several [[Magic Data Storage Mechanisms|magic data storage mechanisms]] have been created. 

The [[Swiss Magic Data Editor|Swiss Magic editors]] hierarchically edit and view the configuration data. This article describes the structure of the Swiss Magic PHP classes. 

This tutorial explains how to [[Migrating Forms from Entry to MagicData|how to migrate forms from previous versions that were stored in the entry table]] and move them to magic data storage, as well as update any mapped fields that referenced the values.

Tasks and Roles
^^^^^^^^^^^^^^^
iHRIS uses a task- and role-based security mechanism to limit access to various parts of the system. A user is assigned a role, and a role is a collection of tasks that the role can perform. This article describes how [[Tasks and Roles|roles and tasks]] are defined in Magic Data and used by the iHRIS system. 

* [[IHRIS Task List|List of all tasks available in the iHRIS system]]
* [[IHRIS Role List|List of all roles available in the iHRIS system]]

Pages and Templates
^^^^^^^^^^^^^^^^^^^
This tutorial describes the role of [[Pages and Templates]] in iHRIS. A page handles each URL request. A template is used to access the HTML elements of a page. 

* [[IHRIS Template List|List of HTML Templates available in the iHRIS system]]

Forms and Classes
^^^^^^^^^^^^^^^^^
Records are stored in the IntraHealth Informatics Core Engine (I2CE) in forms, which consist of collection fields. You can think of a form as table in a database and a field as a column of that table. This article describes the [[Forms and Form Classes]] used. 

The [[Form Lists|form lists]] show how data are related in iHRIS. This is a [[IHRIS Class List|list of all the classes]] available in the iHRIS Suite with links to the API.

The iHRIS system uses a level of abstraction to separate how data is stored in the system versus how it is organized and relates to each other. A form (and its fields) provides the organization. The data storage is handled by various [[Form Storage Mechanisms|form storage mechanisms]]. 

Form Fields
~~~~~~~~~~~

This article describes the main data types, or [[Form Fields|form fields]], used by iHRIS. These fields are defined in Magic Data; this page describes the details of how they should be defined. 

* How to [[Adding Fields|add new forms and fields]]
* How to [[Adding Form and Field Validations|add custom data validations for forms and fields]]
* How to [[Customizing Form and Field Headers|customize the headers for a form field]] by updating the magic data associated with the headers

This page describes how to [[Defining Forms|define and customize forms and fields]] by defining them in Magic Data. 

This article describes the structure of [[Limiting Forms|how various limits are applied to forms]]. 

Form Caches
~~~~~~~~~~~

The iHRIS software caches data saved in the database (or XML file or LDAP server) for faster access and the ability to create indices. These [[Form Caches|form caches]] are used, for example, to populate reports and drop-down lists. 

Cached forms are used to save forms to a consistent format for exporting and for generating custom reports more quickly. There are a few settings [[Configuring Form Cache Generation Timing|you can override in your site configuration file]] to change this behavior. You can also see how to [[Turn Off Background Processes|turn off background processes]] if you wish to not have the form caches update automatically.

If you've imported data multiple times, the form cache will include some of that old data. You can completely [[Recreate All Form Caches|recreate all the form caches]].

Miscellaneous Tutorials
~~~~~~~~~~~~~~~~~~~~~~~

This tutorial describes how to create "standardized" or "official" PDF [[Printed Forms|printed forms]] based on the data in the system. This could be useful for generating training certificates, generating form letters on a position change, or validating who works in a facility or district.

One feature in iHRIS is the ability to look at recently changed forms. You can [[Customize Recent Forms Display|customize the output of the recent changes]] display by creating a hook in your module. This will allow you to append any output you desire to the recent form output. 

[[Linking Facilities and Departments|Link facilities and departments]]: In this tutorial, we will discuss how customize iHRIS Manage so that, when editing a position, the departments displayed are dependent on the facility chosen.

When you create a custom site, you may be adding new forms and fields, in which case, the data maps for iHRIS Manage and Qualify are no longer accurate. You will want to [[Create a Data Form Map For My Custom Site|generate your own form map]].

Here is a note on [[Automatically Generated Integers]].

Reports
^^^^^^^
[[Custom Reporting]] -- This page collects the various articles that describe how to use the Custom Reporting system in iHRIS. This includes detailed documentation about the structure of custom reports and their use in advanced iHRIS features, as well as several tutorials on creating particular reports.

[[Cron Jobs]] - Running functions on a regular basis with iHRIS.

<br> We also have additional tutorials for [[Developer Resources|Developers]] or [[Implementer Resources|Implementers]].

