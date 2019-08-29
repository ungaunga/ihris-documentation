Deleting Records
================

The functionality to delete records is available in the 4.0.11 codebase.

A record, is just one instance of a form, for example a specific person form, *person|1234.* 

 **WARNING:**  This only works with version 5.3 of PHP at the moment.

Enabling the Delete Record Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In order to delete records, you will need to enable the Delete Records module.  To do so go to:


* Configure System
* Configure Modules
* Click the "Sub-Modules" link to the right of the "Pages" module
* Click the "Sub-Modules" link to the right of the "Module Administration" module
* Select the "Delete Records"

 **Note** :  With the 4.0.12 release, the name of module does not show up properly in the configure modules menu.  To work around this, you should just make sure all sub-modules of the Admin module are enabled


Deleting Records
^^^^^^^^^^^^^^^^
Before you begin, **Back up your database!!**   As this feature has not been extensively tested and there are no "safe guards" you will want to back up the database so you can recover from any mistakes.

The delete records is only a "command line" only feature.  It is not available to the web-interface.  To use it, you should open up a terminal to get to the command line.  Now change to the directory  of your site that contains the *index.php*  file.  For example:


.. code-block:: bash

     
    cd /var/www/iHRIS/manage
    

or


.. code-block:: bash

     
    cd /var/lib/iHRIS/sites/4.0/manage/pages
    


The deleteRecord has been registered as a sub-page of the admin module.  So,  once you are in the same directory as index.php, you can use the delete record feature by:


.. code-block:: bash

    php index.php  --page=/admin/deleteRecord
    



Rules for Operation
^^^^^^^^^^^^^^^^^^^


* 1)Whenever deleting a form instance (or record) you are forced to also delete any child forms of that record
* *For example, when deleting a *person*  form, there may be one or more child forms *person_position*  that will be need to be deleted.
* 2)Whenever deleting a record, it will show you and all the forms that the form link to
* *For example a *person_position*  form links to a *position*  form.  If that position form was created just for that person, you **may**  want to delete that *position*
* 3)Whenever deleting a record, it will show you all the forms that link to that form
* *For example, if you are deleting a *position*  form, there may be one or more *person_position*  forms that link to that *position.*   Once you have deleted a position, than you '''must'' delete these *person_position*  forms.


Clearing Out Cached Data
^^^^^^^^^^^^^^^^^^^^^^^^
Once we have deleted a record, we need to clear out any cached data referring to that record.  The simplest way is to restart apache and memcached:


.. code-block:: bash

    sudo /etc/init.d/apache2 restart
    sudo /etc/init.d/memcached restart
    


We also need to clear out the cached forms to remove the deleted records from there.  They will be re-generated when the reports are cached again.


.. code-block:: bash

    php index.php  --page=/CachedForms/dropAll
    



Regenerate Reports
^^^^^^^^^^^^^^^^^^
You will need to force regenerate any reports that referred to any of the data that you deleted.


Example Output
^^^^^^^^^^^^^^
Here is an example of deleting a person from the iHRIS Manage Demonstration site.


.. code-block:: bash

    litlfred@cumin:/var/www/iHRIS/4.0-dev/manage$ php index.php --page=/admin/deleteRecord 
    


Example Outuput:Choosing the Main Record To Delete
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We have run the command, the first thing it asks us is which record we want to delete.  We tell it *person|8549*  and **S** how the details of that person to ensure we have the correct one


.. code-block:: bash

    Please enter the form and ID of the record you wish to delete.  For example person|1000.: person|8549
    Array
    (
        [0] => person|8549
    )
    Would you like to delete records related to person|8549?
    (Yes/No/Show): s
    	firstname => Baicr
    	nationality => country|TAI
    	othername => 
    	residence => district|24
    	surname => Thaiwi
    	surname_ignore => 0
    	password => 
    
    



Example Output:Child Forms
~~~~~~~~~~~~~~~~~~~~~~~~~~
We now verify that we have the correct person so we continue with the deletion process.  It then shows us all the child forms of *person|8549* .  If we wish, we can select individual child forms to delete, but if we do delete a form, we always delete its child forms.  Since we want to delete everything, we simply go ahead and keep all forms selected and **q** uit the selection process.


.. code-block:: bash

    Would you like to delete records related to person|8549?
    (Yes/No/Show): y
    Please select child forms related to person|8549 to delete
    	[X] 0)      	 person|8549
    	            	   Links By nationality To country|TAI
    	            	   Links By residence To district|9
    	            	   Child Forms:
    	[X] 1)      	 	person_position|8551
    	            	 	  Links By position To position|8548
    	            	 	  Parent Form person|8549
    	            	 	  Child Forms:
    	[X] 2)      	 		salary|8552
    	            	 		  Links By salary To currency|1
    	            	 		  Parent Form person_position|8551
    	[X] 3)      	 	demographic|8550
    	            	 	  Links By gender To gender|F
    	            	 	  Links By marital_status To marital_status|1
    	            	 	  Parent Form person|8549
    Please select an option or enter q to quit selection process: q
    


This shows a menu used to select the forms you want to delete.  This menu forces the [[#Rules for Operation | Rule 1]] namely that if you select to delete a form, all children  (and grand-children and great-grand-children and... ) of that form will be selected to be deleted as well.  Some examples:


* Selecting 0 will also select 1, 2 and 3 as they are children
* Selecting 1 will also select 2 as it is a child
* Selecting 2 does not select any others as there are no children for 2
* Selecting 3 does not select any others as there are no children for 3
Notice that you see all the forms that a form links to and links from.  Pay attention to this as you will need it later. 

Next we confirm that we want to all the selected child forms.  It then deletes the four selected forms


.. code-block:: bash

    Would you like to delete all the selected forms linked  person|8549  as children/grand-children?
    (Yes/No): y
    I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:180)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:132)
    I2CE_Page_DeleteRecord->actionCommandLine (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Page.php:492)
    I2CE_Page->display (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Wrangler.php:89)
    I2CE_Wrangler->wrangle (/home/litlfred/rocket_cats/dev/ihris-manage/sites/Demo/pages/index.php:60):
    	Deleting person|8549
    I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:180)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:194)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:132)
    I2CE_Page_DeleteRecord->actionCommandLine (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Page.php:492)
    I2CE_Page->display (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Wrangler.php:89)
    I2CE_Wrangler->wrangle (/home/litlfred/rocket_cats/dev/ihris-manage/sites/Demo/pages/index.php:60):
    	Deleting person_position|8551
    I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:180)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:194)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:194)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:132)
    I2CE_Page_DeleteRecord->actionCommandLine (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Page.php:492)
    I2CE_Page->display (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Wrangler.php:89)
    I2CE_Wrangler->wrangle (/home/litlfred/rocket_cats/dev/ihris-manage/sites/Demo/pages/index.php:60):
    	Deleting salary|8552
    I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:180)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:194)
    I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:132)
    I2CE_Page_DeleteRecord->actionCommandLine (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Page.php:492)
    I2CE_Page->display (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Wrangler.php:89)
    I2CE_Wrangler->wrangle (/home/litlfred/rocket_cats/dev/ihris-manage/sites/Demo/pages/index.php:60):
    	Deleting demographic|8550
    



Example Output: Related Records
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Now, every form that is linked to a deleted form, that a deleted form links to, or is a parent form of a linked form is added to a list of forms that we should potentially delete.  We should only delete forms that we know are associated to this person and this person only.  In this case, we only want to delete the *position*  form that the *person_position*  form is linked to.

First we skip deleting the linked country of their nationality


.. code-block:: bash

    Would you like to delete records related to country|TAI: Taifafeki?
    (Yes/No/Show): n
    

Next, we skip deleting the linked district of residence.


.. code-block:: bash

    Would you like to delete records related to district|9: Gatarama, East, Taifafeki?
    (Yes/No/Show): n
    

Next, we skip deleting the linked gender


.. code-block:: bash

    Would you like to delete records related to gender|F: Female?
    (Yes/No/Show): n
    

Next, we skip deleting the linked marital status


.. code-block:: bash

    Would you like to delete records related to marital_status|1: Single?
    (Yes/No/Show): n
    

Now we come to the *position*  form that was linked to by the *person_position*  form.  First let us show the details.


.. code-block:: bash

    Would you like to delete records related to position|8548: CHO101: Nurse (Gisamba Hospital, Emergency Service)?
    (Yes/No/Show): s
    	i2ce_hidden => 0
    	code => CHO101
    	comments => 
    	department => department|10
    	description => 
    	facility => facility|4
    	interview_comments => 
    	job => job|2230-1B
    	posted_date => 1990-10-13
    	pos_type => |
    	proposed_end_date => 0000-00-00 00:00:00
    	proposed_hiring_date => 1990-10-13
    	proposed_salary => =
    	source => 
    	status => position_status|closed
    	supervisor => position|8528
    	title => Nurse
    

Now that things look OK, we go ahead and continue with deleting this position.


.. code-block:: bash

    Would you like to delete records related to position|8548: CHO101: Nurse (Gisamba Hospital, Emergency Service)?
    (Yes/No/Show): y
    

Next, as we did with the *person*  form above, we need to select any child forms of the *position*  form.  In this case, there are none so our selection menu is much shorter.

If you notice, you will see that the position we are deleting, position|8548, links to position|8528 via the supervisor field.  Which means that the position|8528 is the supervisory position of position|8548.   Since the position|8528 is not directly related to the person we are deleting, we will not want to delete position|8528 later on in the process.


.. code-block:: bash

    Please select child forms related to position|8548 to delete
    	[X] 0)      	 position|8548
    	            	   Links By department To department|10
    	            	   Links By facility To facility|4
    	            	   Links By job To job|2230-1B
    	            	   Links By status To position_status|closed
    	            	   Links By supervisor To position|8528
    Please select an option or enter q to quit selection process: q
    

Now we confirm we want to delete the postion|8548..
<source lang='bash'>
Would you like to delete all the selected forms linked  position|8548  as children/grand-children?
(Yes/No): y
I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:180)
I2CE_Page_DeleteRecord->deleteForms (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/modules/Admin/modules/DeleteRecord/lib/I2CE_Page_DeleteRecord.php:132)
I2CE_Page_DeleteRecord->actionCommandLine (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Page.php:492)
I2CE_Page->display (/home/litlfred/rocket_cats/dev/I2CE/modules/Pages/lib/I2CE_Wrangler.php:89)
I2CE_Wrangler->wrangle (/home/litlfred/rocket_cats/dev/ihris-manage/sites/Demo/pages/index.php:60):
	Deleting position|8548
</source>
Now we return to the list potential records to delete that were related to what we have already deleted.

The first record it asks us to delete is person_position|8551.  This is a bug, and it really should not be asking to delete this as we already have deleted it.  So just ignore it for the time being.
<source lang='bash'>
Would you like to delete records related to person_position|8551?
(Yes/No/Show): n
</source>
We continue with our list of potential records to delete, but we are not interested in deleting them, so we answer No for all of them
<source lang='bash'>
Would you like to delete records related to currency|1: TF ¤?
(Yes/No/Show): n
Would you like to delete records related to department|10: Emergency Service?
(Yes/No/Show): n
Would you like to delete records related to facility|4: Gisamba Hospital?
(Yes/No/Show): n
Would you like to delete records related to job|2230-1B: Nurse?
(Yes/No/Show): n
Would you like to delete records related to position_status|closed: Closed?
(Yes/No/Show): n
Would you like to delete records related to position|8528: CHO97: Nurse (Gisamba Hospital, Emergency Service)?
(Yes/No/Show): n
</source>


Example Output:  Restarting Apache
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
We are done deleting.  We need to restart apache and memcached.  Like all operations on the command line that change the database, this is **very important**  to do.  It ensures that all caches are clear and we do not have any conflicts in what is stored in the database and the cache.
<source lang='bash'>

litlfred@cumin:/var/www/iHRIS/4.0-dev/manage$ sudo /etc/init.d/apache2 restart


* Restarting web server apache2
  ... waiting     
litlfred@cumin:/var/www/iHRIS/4.0-dev/manage$ sudo /etc/init.d/memcached restart
Restarting memcached: memcached.
</source>


Preserving Deletions
^^^^^^^^^^^^^^^^^^^^
All records that are deleted are automatically stored in the database in the *form_history*  table with the deletion time and all the data stored as a json encoded string.


