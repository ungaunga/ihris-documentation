Form Storage -- Multi-Flat Table
================================

Slated for release in version 4.0.1.

The *Multi-Flat*  [[Form Storage Mechanisms|form storage mechanism]] is similar to the [[Form Storage -- Flat Table|flat]] form storage mechanism excepting that the data used to populate the form can come from multiple databases and tables.   The *Multi-Flat*  storage mechanism is intended for data aggregation purposes.  It does so by considering each database/table to contain the data from one [[Defining Forms#Componetized Forms|component]].  By a component, we mean a self-contained running instance of iHRIS Manage.

For example, you may have several regions each running an instance of iHRIS Manage.  You may wish to aggregate data maintained within each of the regions (e.g. people and positions, but not jobs or geographic locations) into a central instance of iHRIS Manage so that you can run reports on the entire country.  When setting up the central instance of iHRIS Manage, you could choose to use the *Multi-Flat*  storage mechanism for people and positions.  Then on the central server, you could create a database for each region, (Region1, Region2, etc.) which would simply contain the cached tables for people and position for each of the respective regions.  

For the data such as jobs or geographic locations, which should be centrally maintained, we encourage you to use the [[Form Storage -- Magic Data|magic data]] form storage mechanisms.


Specifying Multi-Flat Storage
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
To specify that the form $form has a Multi-Flat table storage mechanism set by setting
 /modules/forms/forms/$form/storage
to have value '''multi_flat.''


Form Options
^^^^^^^^^^^^
The multi-flat storage mechanism is defined so that, by default, it can read in the cached "hippo_" tables of form data across several databases, with each database corresponding to one component (e.g. a region, district or facility).  If you situation, is not exactly this, then you can take advantage of the options as described in this section.

The options specifying a *Multi-Flat*  table storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/multi_flat
It has the following structure (which is identical to those for [[Form Storage -- Flat Table|flat]] storage):


* table: Optional scalar node. The table to use, e.g. *hippo_person* .  You are responsible for back-tics if required.  The same table name will be used across the multiple databases, with each database representing an individual component).  If it is not set, it determines the table name from the table_prefix set in the [[Form Storage -- Multi-Flat Table#Global Options|global options]].
* id: Optional parent node.  The data defining how to associate an id per row of this table.  If it is not set, we use simply the column 'id'.
* *col: Optional scalar node.  Specifies a column of the table to be used as the id.  You are responsible for back-tics.
* *function: Optional scalar node.  Specifies a SQL function  whose result will the id for the form. 'col' takes precedence.
* *form_prepended: Optional scalar node.  Defaults to true. If true it means the form name has been prepended to the id.  Otherwise, it assume that the column is just the id.
* fields: Optional parent node.  Specifies how the data of the your form is associate to a row of your table.  Each child of this node is the name of a field $field of your form.  By default, all fields of a form are populated, and are all assumed to come from the column with that field name.
* *$field:  Parent node with the following child nodes.
* **col: Optional scalar node.  Specifies a column of the table to be used as the id. You are responsible for back-tics.
* **function: Optional scalar node.  Optional scalar node.  Specifies a SQL function  whose result will as the value for the field. 'col' takes precedence.
* **enabled: Optional scalar node.  If present and evaluates to false, it means we should not populate this field.
* parent: Optional parent node.  If not present, we assume the parent is populated from the column 'parent'.  It has the following child nodes:
* *enabled: Optional scalar node.  If present and evaluates to false, it means getParent() should return the trivial parent id, '0'.
* *col: Optional scalar node.  Specifies a "column" of the table to be used as the id for the parent. You are responsible for back-tics.
* *function: Optional scalar node.  Optional scalar node.  Optional scalar node.  Specifies a SQL function  whose result will as the value for the parent form's id. 'col' takes precedence.
* writable: Optional scalar node.  Defines the write access to the table.  If not present or its value cast to false, then the table is not consider to be writable.  If its value casts to true, then it is considered writable and the save() method will actually do something.  At the moment, the save() method is not implemented.
* last_modified: Optional parent node.  If not present, we assume the last modified time is populated from the column 'last_modified'.  It has the following child nodes:
* *enabled: Optional scalar node.  If present and evaluates to false, it means the modified time is always taken to be NULL
* *col: Optional scalar node.  Specifies a "column" of the table to be used as the modified time.  Column should have type datetime. You are responsible for back-tics.
* *function: Optional scalar node.  Optional scalar node.  Optional scalar node.  Specifies a SQL function  whose result (of type datetime) will as the value for the modified time. 'col' takes precedence.



Form Options Example
~~~~~~~~~~~~~~~~~~~~
To read in the cached *hippo_person*  tables for the person forms from the four different regions in the [[#Global Options Example|example below]] we would set:
 /modules/forms/forms/person/storage => 'multi_flat'
This can be done in a configuration.xml file by:
 <configuration name='person_multi_flat' path='/modules/forms/forms/person/storage'>
  <value>multi_flat</value>
 </configuration>

In this case, if a person form had the id "person|12" and was in the Northern region, the id would become "person|12@north"


Global Options
^^^^^^^^^^^^^^
There are global options for specifying a the mapping between components and databases
 /modules/forms/storage_options/multi_flat
This has the structure:


* table_prefix: Optional scalar node.  The value pre-pended to a form name to give the table name where the data is stored.  If not set it is 'hippo_', the prefix used for the caching of  form data to flat tables.
* components: Required parent node. It's child nodes are the names of each of the components (e.g. Regions) you will be reading from.
* *$component: Parent node.
* **database: Required scalar node. It's value is the database where the tables for the $component are stored.
* **table_prefix: Optional scalar node. It's value is the prefix pre-pended to the form name to get the table.  If it is not set, it uses the value stored at /modules/forms/storage_options/multi_flat/table_prefix (which defaults to 'hippo_')


Global Options Example
~~~~~~~~~~~~~~~~~~~~~~
For example you might have the following:


* components
* *north =>
* **database => 'NorthernRegionDatabase'
* *south =>
* **database => 'SouthernRegionDatabase'
* *east =>
* **database => 'EasternRegionDatabase'
* *west
* **database => 'WesternRegionDatabase'
You can set this in a configuration.xml file by:
 <configurationGroup name='multi_flat_components' path='/modules/forms/storage_options/multi_flat/components'>
  <configuration name='north' values='many' type='delimited'>
    <value>database:NorthernRegionDatabase</value>
  </configuration>
  <configuration name='south' values='many' type='delimited'>
    <value>database:SouthernRegionDatabase</value>
  </configuration>
  <configuration name='east' values='many' type='delimited'>
    <value>database:EasternRegionDatabase</value>
  </configuration>
  <configuration name='west' values='many' type='delimited'>
    <value>database:WesternRegionDatabase</value>
  </configuration>
 </configurationGroup>



