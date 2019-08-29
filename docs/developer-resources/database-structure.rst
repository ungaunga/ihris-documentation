Database Structure
==================

iHRIS makes use of multiple tables in a relational database (MySQL) to store its data in.  This article describes several of the tables used by iHRIS, in particular the user table and the tables used for [[Form Storage -- Entry/Last Entry | audited form data changes]].

 **Note: This document maybe out of date.** 


The iHRIS Database is abstracted so the object structure can be handled by forms within the site.  All records saved for a site are an instance of I2CE_Form.  This defines all the fields used for that form.  The form and field names are saved in the form and field tables in the [[#Form Definitions|form definitions]] section below.  These are combined in the form_field table to map all the fields associated with a given form.

The data for each form is saved as a record (see [[#Record Tables|Record Tables]]).  Each field is then saved in the entry and last_entry tables.  The entry table keeps a history of all changes and the last_entry table is a quick lookup for the current value.  So if you have an instance of a form with 2 fields there will be 1 row saved to the record table and 2 rows each in entry and last_entry.  There will always only be 2 rows in the last_entry table but the rows in the entry table will increase each time a change is made.


User Tables
^^^^^^^^^^^
The user tables can be in the same main database as the rest of the site, or they can be in a shared database so names and passwords
can be reused.  The access table must be in the main database to give access for the site.
{|border="1" cellspacing="0" cellpadding="5"
!Table
!Description
!Table Definition
|-
!user
|The user table holds the login and contact information for all users on the system.  The password is encrypted with MD5() and the id is referenced in any other tables referring to the user.  The username and id must be unique.  The firstname and lastname are used for display purposes.  The email address is used to contact the user for password changes or forgotten passwords.  The creator is a reference to the user id that created this user.
|<pre>
CREATE TABLE `user` (
  id int(11) NOT NULL auto_increment,
  username varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  firstname varchar(50) NOT NULL,
  lastname varchar(100) NOT NULL,
  email varchar(100) default NULL,
  creator int(11) NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY username (username)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
</pre>
|-
!user_log
|The user_log table holds login and logout data for users.  It also ties the login to the session_id associated with the user.
|<pre>
CREATE TABLE user_log (
  `user` int(11) NOT NULL,
  login datetime NOT NULL,
  logout datetime default NULL,
  session_id varchar(50) NOT NULL,
  activity datetime NOT NULL,
  KEY `user` (`user`),
  KEY login (login)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
</pre>
|-
!access
|The access table controls access for the users to the site.  The role is a string defined by the site to control what areas the user can see and what actions can be performed.
|<pre>
CREATE TABLE access (
  `user` int(11) NOT NULL,
  role varchar(255) collate utf8_bin NOT NULL,
  PRIMARY KEY  (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}


Form Definitions
^^^^^^^^^^^^^^^^
These tables define the forms and fields associated with the site.
{|border="1" cellspacing="0" cellpadding="5"
!Table
!Description
!Table Definition
|-
!form
|The form table defines a short name for a form and links it to a unique id.  The type field is deprecated.
|<pre>
CREATE TABLE form (
  id int(10) unsigned NOT NULL auto_increment,
  `name` varchar(50) collate utf8_bin NOT NULL,
  `type` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!field
|The field table defines a short name for all the fields used in the site.  The type is the data type for the given field.
|<pre>
CREATE TABLE field (
  id int(10) unsigned NOT NULL auto_increment,
  `name` varchar(50) collate utf8_bin NOT NULL,
  `type` varchar(16) collate utf8_bin NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY name_type (`name`,`type`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!form_field
|The form_field table maps a list of fields that are associated with the given form.  Any saved data will then be associated with the unique id of the form_field.
|<pre>
CREATE TABLE form_field (
  id int(10) unsigned NOT NULL auto_increment,
  form int(10) unsigned NOT NULL,
  field int(10) unsigned NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY form (form,field)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}

Record Tables
^^^^^^^^^^^^^
The record tables store specific information saved for each form associated with the site.
{|border="1" cellspacing="0" cellpadding="5"
!Table
!Description
!Table Definition
|-
!record
|The record table is the main table associated with each instance of a form.  There is a unique id for easy reference.  The last_modified field is updated every time a change is made to the given record.  The form is the id of the form this record is an instance of.  If the record has a parent record then the parent field will be populated with that record id.
|<pre>
CREATE TABLE record (
  id int(10) unsigned NOT NULL auto_increment,
  last_modified datetime NOT NULL,
  form int(10) unsigned NOT NULL,
  parent int(10) unsigned default NULL,
  PRIMARY KEY  (id),
  KEY parent (parent)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!entry
last_entry
|The entry and last_entry tables are very similar.  The entry table holds a record of all changes made to a given form_field value for a record.  The last_entry holds the latest entry for quicker access.  The record is the id of the record this value is associated with for the given form_field.  The date is the date this value was saved.  Who is the user id of the person who made this entry.  The change_type is set depending on if this is an initial entry, a correction or a regular update to this value.  It can also be set to verified if the data has been double checked.  One of the value fields will be populated based on the type of the form_field.
|<pre>
CREATE TABLE entry (
  record int(10) unsigned NOT NULL,
  form_field int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  who int(10) unsigned NOT NULL,
  change_type tinyint(3) unsigned NOT NULL,
  string_value varchar(255) collate utf8_bin default NULL,
  integer_value int(11) default NULL,
  text_value text collate utf8_bin,
  date_value datetime default NULL,
  blob_value longblob,
  PRIMARY KEY  (record,form_field,`date`),
  KEY `date` (`date`),
  KEY form_field (form_field),
  KEY record (record)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE last_entry (
  record int(10) unsigned NOT NULL,
  form_field int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  who int(10) unsigned NOT NULL,
  change_type tinyint(3) unsigned NOT NULL,
  string_value varchar(255) collate utf8_bin default NULL,
  integer_value int(11) default NULL,
  text_value text collate utf8_bin,
  date_value datetime default NULL,
  blob_value longblob,
  PRIMARY KEY  (record,form_field),
  KEY form_field (form_field),
  KEY record (record)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!field_sequence
|The field_sequence table is used to track an integer value for a form_field that will be automatically generated and incremented by the site.  It keeps track of the last value used for the given form_field.
|<pre>
CREATE TABLE field_sequence (
  form_field int(11) NOT NULL,
  sequence int(11) unsigned NOT NULL,
  PRIMARY KEY  (form_field)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!deleted_record
|The deleted_record is used to save records that are removed from the system in case it needs to be recovered.  It is a mirror of the record table.
|<pre>
CREATE TABLE deleted_record (
  id int(10) unsigned NOT NULL auto_increment,
  last_modified datetime NOT NULL,
  form int(10) unsigned NOT NULL,
  parent int(10) unsigned default NULL,
  PRIMARY KEY  (id),
  KEY parent (parent)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}


Utility Tables
^^^^^^^^^^^^^^
{|border="1" cellspacing="0" cellpadding="5"
!Table
!Description
!Table Definition
|-
!config
|The config table stores all the configuration data for the site.  This data is read from the configuration XML files for modules.  The hash is a MD5 hash of the path.  It is used for unique key look ups.  It is shared with the hash that is stored in the APC.  The path is a readable format of the path to the data.  The type determines if this entry is a parent or an end node.  If an end node then the value will be set with the value for the node.  If it's a parent then children will be set with a list of children nodes for this entry.
|<pre>
CREATE TABLE config (
  `hash` char(32) character set latin1 NOT NULL,
  path varchar(10000) character set latin1 NOT NULL,
  `type` tinyint(4) NOT NULL,
  `value` varchar(2000) character set latin1 default NULL,
  children varchar(10000) character set latin1 default NULL,
  PRIMARY KEY  (`hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!report_list
|The report_list table is simply a place holder definition to create temporary tables when creating a cached report.  It has primary and secondary records that will be saved depending on the report being cached.
|<pre>
CREATE TABLE report_list (
  `primary` int(11) NOT NULL,
  secondary int(11) NOT NULL,
  PRIMARY KEY  (`primary`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}


Form Example
^^^^^^^^^^^^

This is an example of how two forms would be saved to the database.  The person form has a surname field and the demographic form has a birth_date field.  The person form would be saved first since it is the parent form.  Assuming no forms have ever been saved to the database the following would happen on saving.


* Create the **form** , **field**  and **form_field**  entries.

  * An entry is added to the **form**  table with the *name*  being "person."  This will automatically assign a form *id*  of 1 since it's the first one.
  * An entry is added to the **field**  table with the *name*  being "surname."  This will automatically assign a field *id*  of 1.
  * An entry is added to the **form_field**  table with the *form*  being 1 (for person) and the *field*  being 1 (for surname).  This will automatically assign a form_field *id*  of 1.
  * An entry is added to the **form**  table with the *name*  being "demographic."  This will automatically assign a form *id*  of 2 since it's the first one.
  * An entry is added to the **field**  table with the *name*  being "birth_date."  This will automatically assign a field *id*  of 2.
  * An entry is added to the **form_field**  table with the *form*  being 2 (for demographic) and the *field*  being 2 (for birth_date).  This will automatically assign a form_field *id*  of 2.

* Create the person record.

  * A new record will be added to the **record**  table.  The record *id*  will be generated automatically (1) and the *form*  will be set to 1.  There is no *parent*  and the *last_modified*  time will be set to the current time.
  * An entry will be added to the **entry**  and **last_entry**  tables.  The *record*  will be set to 1 and the *form_field*  will be set to 1 (the form_field id created above for person-surname).  The *date*  will be the current time and *who*  will be set to the user id making the change.  The *string_value*  field will be set to the value for the surname.

* Create the demographic record.

  * A new record will be added to the **record**  table.  The record *id*  will be generated automatically (2) and the *form*  will be set to 2.  The *parent*  will be set to 1 since this is a child form for the person record that was just created.  The *last_modified*  time will be set to the current time.
  * An entry will be added to the **entry**  and **last_entry**  tables.  The *record*  will be set to 2 and the *form_field*  will be set to 2 (the form_field id created above for demographic-birth_date).  The *date*  will be the current time and *who*  will be set to the user id making the change.  The *date_value*  field will be set to the value for the birth_date.

[[Category:Developer Resources]]
