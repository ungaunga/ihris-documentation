Form Storage Mechanisms
=======================

The iHRIS system uses a level of abstraction to separate how data is stored in the system versus how it is organized and relates to each other.  A form (and its fields) provides the organization.  The data storage is handled by various form storage mechanisms.

A storage mechanism is defined by subclass I2CE_FormStorage_Mechanism, which provides the methods to read, and possibly write, the data for any form with the given mechanism.  If the data is stored in a database, it can sub-class I2CE_FormStorage_DB and provide read access to the data as a form by only defining one method, *getRequiredFieldsQuery().*   To make a storage mechanism writable, you only need to write a method that defines how to store a data field.

Once a storage mechanism is written, the data for that form can be queried via searches with [[Limiting Forms |limits]].

The currently available storage mechanisms are:


* [[Form Storage -- Entry/Last Entry|entry]]: A vertical database storage mechanism which keeps a history of when and by who individual fields (data elements) were changed.  This is the default storage mechanism, and the storage mechanism that was used in version prior to 3.2.
* [[Form Storage -- Flat Table|flat]]: A horizontal database storage mechanism, where a row of a table corresponds to an instance of a form.  The columns, or any SQL function,  of the table are used to define the fields.
* [[Form Storage -- Multi-Flat Table|multi_flat]]: A horizontal database storage mechanism similar to the flat storage mechanism but combining several identically structured tables.  It is primarily intended for data collation.
* [[Form Storage -- Magic Data |magicdata]]: A locale aware storage mechanism primarily intended for centrally maintained lists of data.
* [[Technical Overview: Form Storage -- CSV |CSV]]: A storage mechanism to read data from a CSV file
* [[Technical Overview: Form Storage -- Eval |Eval]]: A storage mechanism to populate and get records based on php function calls
* [[Technical Overview: Form Storage -- XML |XML]]: A storage mechanism to populate and get records based on an XML file.
* [[Technical Overview: Form Storage -- SDMX-HD |SDMX-HD]]: A storage mechanism to populate and get records based on SDMX-HD code lists.
* [[Technical Overview: Form Storage -- SDMX CrossSectional |SDMX Cross Sectional]]: A storage mechanism to populate and get records based on SDMX Cross Sectional Data.
* [[Technical Overview: Form Storage -- LDAP |LDAP]]: A storage mechanism to populate and get records based on a LDAP server




Aggregating Storage Mechansims
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
You may be in a situation in which you need to aggregate from several different instances of iHRIS Manage (or Qualify).  You can mark a specific a storage mechanism, $storage_mechanism, as being aggregating by setting:
 /modules/forms/storage_options/$storage_mechanism/componentized
to **1.**  Then each form $form that uses that storage mechanism, will be [[Defining Forms#Componetized Forms|componetized]].

At the moment, only the [[Form Storage -- Multi-Flat Table|Multi-Flat]] storage mechanism is an aggregating storage mechanism.


Once the *form-storage*  module is enabled, an instance of *I2CE_Form*  has the method *isComponentized()*  to check if a form is componentized.   You can also check via *I2CE_FormStorage::isComponentized($form)* 

[[Category:Developer Resources]]
