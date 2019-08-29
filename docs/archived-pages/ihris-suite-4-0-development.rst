IHRIS Suite 4.0 Development
===========================

[[Category:Archived Pages]]
==Version 4.0.0==
Released week of July 13, 2009.

==Version 4.0.2==
Released November 13, 2009.
===Completed===
*Custom reports/Form Limits -- allow you to sprecify the values that a limit can take in the getLimitMenu() and int he custom reports
*added fancy updater 
*fixed up fatal errors so it provides a mailto form
*fixed up fatal errors so it is the same fancy level as the updater
*fixed bug in finding conflicts when installing optional modules
*fixes for custom report:
**charts -- now works w/o url rewritting enabled
**non-enabled fields are not longer displayed and sort order is preserved in a view
**fixed aggregation of fields
*add XML export (to non-standard but hopefully useful) format
*add command line option --force-restart=1 to force the restart of an install/update  (used in conjunction with --update=1)
*add time stamp to PDF
*add form documentor as a CLI page
*Debug training module
*Ensure all templates are localized (done in 4.0.0)
*Cleanup ISCO-88 Job Codes (done in development for 4.0.1)
*Finish [[Technical Overview: Form Storage -- Flat Table|Flat Storage]] mechanism for forms.
*Add in [[Technical Overview: Form Storage -- Multi-Flat Table|Multi-Flat Storage]] mechanism for forms
*Fix this: http://www.2shared.com/file/6929841/7587e315/bad_css.html
*Add cache stale times on a per form basis 
*Add cache stale times on a per form storage mechanism basis
*Add ability to turn of form caching by background process
*Add cache stale times on a per report basis
*Add ability to turn of report generation by background process
*Change so that caching a report triggers the caching of the forms needed for the report if they are stale
*Change so that forced caching a report triggers forced caching of the forms needed for the report
*Replace I2CE_Form::validate() mapped values check with something from I2CE_List, e.g. monsterMash()
*separate form field validation logic into the appropriate modules
*fix bug in export of custom reports to html
*logout page now really logs out
*added command line option --clear_cache=1 which will clear the magic data cache
*added special URL: $site_url/clear_cache.php which will clear the magic data cache, the apc cache and destroy the session
*fix limits for dates
*fix bug in setting the order in which fields are displayed in a report view
*fix bug in defining a form relationship when linking from a form.
*added index to string_Value column of last_entry table to speed of cache generation
*added in index on mapped fields in hippo_tables to speed up report generation,
*fixed ie7 javascript errors that were causing problems for custom reports
*upgraded to mootools 1.2.3
*speed display of lists in administer database
*added a db-like version of magic data form storage which is used if the "permanent" magic data storage is in the config table (this causes localization support to be dropped from magic data)
*fixed issue for default display of custom reports where limits where lost when resorting the table
*Add paging for list display pages
*add photo upload
*add resume upload
*Fix bug with report views not displaying fields the first time you try to edit it
*Report limits with dates are being set to the current date by default
*Fix sort order of headers on report views
*Migrate iHRIS Qualify

==Version 4.0.3==
Release in Friday March 5, 2010.
===Completed===
*when editing a database list with a select field, not choosing a select field should display everything (e.g. not choosing the location to limit the facilities shows all the facilities)
*allow list members to be disabled so that they don't appear in the default drop-down menu.
*add option meta/form_any so that a mapped field can take values in any form
*make the flat form storage mechanism writable as much as possible
*add a UUID module so that any form can be assigned a uuid via the form uuid_map
*fixed up processing of <eval> tag for external module requirements
*fixed issue when classes were not loaded when a install was restarted
*added [[Technical Overview: Form Storage -- CSV | CSV form storage mechanism]]
*added [[Technical Overview: Form Storage -- Eval | eval form storage mechanism]]
*created locale form (via eval form storage) for selecting available/selectable locals
*Windows: allow relocatable paths so [http://www.openhealthconsortium.org/wiki/doku.php?id=PHIT USB-Toolkit] will work
*added moveData()/exportData()/importData() for form storage mechanisms
*Add in different role/password authentifications for users 
**DHIS users
**LDAP
*there is now an adminisitrtive user 'i2ce_admin' whose password is the password used to access the db
*Mysql's unix socket often lives in /var/lib/mysql (or elsewhere), not /var/run/mysqld. (jstrope) -- fixed by adding intializeDSN() to I2CE class which allows you to pass a DSN.  we can now handle RHEL setting the dsn if we ever package .rpms for it.
*Cleanup user and user_form.
*Make iHRIS work out of the box on RHEL:
**Fedora has no /etc/timezone -- that info lives in /etc/sysconfig/clock (but you can't just do a file_get_contents on it -- has comments and dditional info and the time zones don't always match the format returned by date_default_timezone_get) (jstrope)
***relevant [https://bugzilla.redhat.com/show_bug.cgi?id=469532 Bug report] and [http://trac.agavi.org/ticket/1008 here] and [http://derickrethans.nl/distributions_please_dont_cripple_php_or_red_hat_stop_fucking_around.php here]
**iHRIS didn't give much of an indication of why the initialization failed. If you had an error handler that said "set your date.timezone setting in  php.ini", that would probably suffice. (jstrope)
*upgrade mootools to 1.2.4
*Remove all mootools' $ references from javascript [http://mootools.net/blog/2009/06/22/the-dollar-safe-mode/ dollar sage mode]
*Add workplace accident module to ihris manage
*Add disciplinary action module to ihris manage
*FormCache is smarter: forms are marked dirty when they are saved and clean when they are cached.  this way we don't need to even bother trying to re-cache a form if it has not been saved since the last time it was cached.
*Magic Data Browser:  the path is now a bunch of links so you can easily skip to the top.
*FormStorageEntry:  flattened out the sub-query into a single query so that indices on last_entry can be taken advantage of in a where clause
*modify limit templates to display differently for report view limits and relationship editing.
*function signatures fixed for validate() method of  personPostion,application 
*function signature fixed for filedump->display() and ajax_text->display()
*function signature fixed for formfield_currrency->createdomeditable()
*made collation utf8_bin (instead of utf8_general_ci) across all columns in hippo tables (cuts report generation times by half)
*cleaned up code for setting default values for form fields (now lookup value is handled by MAP)
*added indices to entry table to speed up cached form generation (form_field,string_value) and (formfield,integer_value)
*speed-up for getting max in int_generate so that it uses the (formfied,integer_value) index
*changed magic data to be stored in config_alt table rather than config table to deal with:
**config table did not allow children with commas in their names
**performance was slowed as the size of the config table grew 
**increase the speed when doing a join with a parent and child (form storage magic data)
*call page stretch when the page goes through an ajax update  
*fix issues with the updater/configurator when moving to a new version of the software library while the old version stayed in the same place
*fixed issues with classes of dependent modules not being loaded on a module update
*added a 'Recent Forms' menu option to the search page so you can see which forms (e.g. person or position) have recently been edited/created.  useful if they are not yet in the search report
*moved all of the SearchPages classes from manage and qualify into common with the search reports being displayed by magic data
*fixed error checking/null checking when getting the last modified time for a form stored in magic data
*allow to check the modification time on individual fields of a form or of the record for entry
*fixed pagination issues when view lists in the 'Administer database'
*Removed caching all forms from the generate_complete background process since each form makes sure the required forms are cached.  Removed the restriction of passing multiple forms to the generate custom reports command lin
*fixed header for CSS that was breaking Chrome and Safari
*various fixes of function signatures
*marked all translatable nodes in configuration .xml files. 
*fixed up translation of .html and config .xml files from .mo files

==Version 4.0.4==
===Completed===
*Added memcached magic data storage to sit between APC and DB.  Reduces load on DB and speeds up start-up time for background processes.
*Fixed issues with magic data storage and initialization not setting everything in DB storage.
*Module Configuration via SwissConifg now works (at least the basic parts)
*fixed prepared statement for config_alt table that was problematic in mysql 5.0
*fixed PageStretch lowest element calculation when there were scrollable elements
*In fatal bugs, the mailto form now looks nicer and includes a full error trace.
*Fixed issue in loading in localized magic data from a delimited type... the loaded language would overwrite en_US string.
*Added a play button for error messages.
*FormField Date_YMD now uses the [http://www.monkeyphysics.com DatePicker] mootools script
*On module update load as many modules class paths as possible
*Fixed bug with reports not displaying when the default view displayed multiple columns but the selected view was only one.
*Modified flash charts to better display labels so the chart and labels aren't cut off.
*Added display of error message to raiseError when the error is about running out of memory.
*Added error message to charts and HTML views when the report hasn't been generated or the limits don't return any results.
*Reports: Change the buttons on reports to pull up the options window and remove the options link.
*Form documentor can now localize
*Added in checking to Multi-flat storage to see if desired databases exist
*Date Picker
**Defaults to decade
**Allows blank values
**Report date limits now use data picker
*Removed (Options) links for report buttons.  now buttons will pop up the options menu
*fixup width of passport photos
*I2CE_FormField_Binary_File -- filename and modtime are now stored.

==Version 4.0.5==
===Completed===
*Reports:  When joining in a specific form on a mapped field which can take values in multiple forms, all values of the joined form are populated.  E.g. joining district to facility on the location field will populate the district data if either the location maps to a district or a county
*Reports: speed improvements -- the parent form in a relationship is no longer joined in.  Rather necessary data are read directly from the reports
*Form Relationships:  Added the ability to get all the forms satisfying a relationship given the id of a primary form 
*Added in the [[Printed Forms]] module with samples:
**iHRIS Manage: Staff Hire Letter
**iHRIS Qualify: Registration Form
**iHRIS Qualify: License
*Added the "Dependents Module" to iHRIS Common which was [[http://www.capacityproject.org/hris/blog/index.php/2010/05/tanzania-advances-use-of-hr-management-software-part-1/ coded-in-country]]
*cleaned up the required strings to translate for exported custom reports
*If you chose the non-default locale on the login page, then that user's locale is set on a successful login
*Cleaned up tasks and their descriptions
*Simple lists can now share a common html template
*Fixed various CSV form storage bugs
*Added some changes to smooth over transition to Ubuntu Lucid:
**Set default sessions path to /tmp if it has not been set
*die after display non-modified headers
*fixup pagination of html reports --- limit values were not being preserved
*MagicDataNode->setIfIsSet() now sets values based on set locale.
*Magic Data Browser -- shows locale that is being displayed.
*Magic Data Browser -- works better when editing translatable values
*Updated magic number data file
*Added [[Technical Overview: Form Storage -- SDMX-HD| SDMX-HD]] form storage to view SDMX-HD code lists as iHRIS forms.
*Added default link forms to be used to link lists to other lists as well as to string (for IDs) to map to other data standards if necessary.

==Version 4.0.6==
Plan for release in August 2010
===Completed===
*Add in "ancestral form" join condition on form relationships
*modification times are stored (and indexed) in the hippo_XXXX tables (Done to support smaller size updates of databases to remote aggregating database)
*added next of kin module to ihris-common
*created a field container/field container factory which form/form factory sub class
*removed I2CE_List class constants, MAIN_FIELD, SEC_FIELD, SORT_FIELD and replaced with extended sprintf functionality stored magic data "/modules/forms/formClasses/$form/list/display/default/XXX"
*Have the I2CE_List::listOptions() make use of the new sprintf data rather than implode('-',$vals)
*Add Report Archive module
*workaround MDB2 bug with \0 terminated data in I2CE_FormField_Binary
*Added support to zip report exports
*FormStorage/Lists:  allowed multiple fields to be checked against for uniquness by specifying a comma seperated list in the unqiue_field.  also made the error message a bit more useful if there is a non-uniqueness problem
*Added ability to upload XSLT to a report view that can be used to transform the .xml export (mostly done to export SDMX-HD)
*form relationships ('''SQL ONLY''') allow ability to join on a child field which is mapped such that it traverses the linking data
*added in establishment module to iHRIS Manage
*added in sample data and sample report for establishment module (staffing norms 2010)
*Added module to archive Scanned Paper Records to a person
*Fixed bug w/ selected tree values not being preserved on a submit/confirm page for database lists
*Added ability to specify max document size in KB for a binary form field by setting /modules/forms/formClasses/$formClass/fields/$field/meta/max_size_kb
*Fixed issues w/ id field not being set/read from when loading forms from request variables
*added ability to create profiles of forms and to cache or mysqldump the forms based on the profiles
*added ability to delete default display for a custom report view
*added generic XML-based form storage mechanism
*added SDMX CrossSectionalData form storage mechanism
*when a list is read-only, then do not show the 'edit/update' link from the database lists page. instead go to the view list page.
*added gzip compression for report view export
*added bzip2 compression for report view export
*added arbitrary stream support for file based form storage mechanisms -- e.g. now you can read things across http:// not just the file system. In particular this applies to CSV, XML, and the SDMX-HD form storage mechanisms.
*mapped the user access mechanisms to a user form storage mechanism
*fixed bug with listing fields in the generic form storage mechansim 
*split out Job and Cadre modules from Manage into Common.  ManageJob remains w/ salary grade
*added Confirmation/Probationary work period module
*allow upload of meeting notes for position changes and interviews
==Version 4.0.7==
Plan for release in September 2010
===Completed===
*Added in logging to the UserAccess method since this wasn't included when the module was created.
*fixed bug in editing form cache profile
*page form lists -- view button now works again when no value is set
*Changed migrate field/form functions to not use the form cache.  Added a clearFieldData function to the form factory so the field info can be cleared out by the migrate functions so new fields can be found if they're changed after be loaded once by an upgrade.
*Fixed typo on task name for lists base template.  can_hide_list_memebers to can_hide_list_members.
*Fixed bug with printed forms where it would fail if the form didn't have a child form created for something in the relationship.
*Made UserAccess required by ihris-common so that upgrade functions that need to create a user will find the correct class since it will be loaded first.
*iHRIS Qualify:  Fixed typo in hide javascript for scanned archives.  Made record verify and deployments only show the most recent information.  Set registration for to be accessible from the entire view person page.
==Version 4.0.8==
Plan for release in November 2010
===Completed===
*Fixed binary files so if no file is chosen it will look for the tmp_key when a file is confirmed and then edited.  Added an invalid error message when the file fails to upload.
*Added some helper methods to I2CE_List to find matches for a field based on the displayed fields for a form and add a within limit option for MAPs.  This allows you to perform a limit on report results (or other limits) that will match on a location field that can be either district or county so if you choose a district it will match any counties that are in that district as well as the district.
*Fixed confirm and linking of binary fields (Document and Image)
*Made the selection tree work in chrome
*List cleanup -- everything use the display_string/dipslay_args now including monster mash, selection tree
*Fixed the issue with errors when logging in with the i2ce_admin user.  It now logs it with the ID of 0.
*Modified getDisplayFields, getDisplayString and getSortFields methods to all work statically without having to create an empty list to get the values from magic data.
*Make StretchPage work with Chrome and IE8
*allow option to make PDF reports download or inline
*handle parent in where clauses for db like storage mechanisms
*max and min parent limits in form relationship can now have an offset so you can do thing like previous position -- start_date is max_parent with offset 1
*use css borders to make it clearer which form you are within in a form relationship
*include file sources for html templates
*fixup when joining on a child field where the parent form is the primary form in a relationship
* in field limits, a data element 'linked_field' can now choose to be any of the fields of the form or the parent field.  this applies in particluar to max_parent and min_parent  which were before assumed only to be the parent field.  this is useful for example when joining person_position to the position form, and you want to limit person_position so that the start_date is maximal among all person_position forms with the same value for person_position+position
*fixed join on a child field in form relationship
* Added argument to magic data unpopulate method to cleanup the objects for garbage collection.  Added unpopulate (with cleanup) calls to migrate methods to free up some memory while migrating large sets of data.
*added record status module
*made it so archive scans can either be a document or an image
*Added display_string and args and sort_fields for regions, districts and counties.
*add exam results to training module
*Added in hooks to call after a child form is added to the person view page.
*Updated facility report to use within for the location instead of equals.
*Updated the getSalaryGradeID method for iHRIS_PersonPosition to not use the lookupField method but the fields in the necessary objects.  Updated action_person_position in the PersonPosition module to work with the returned value already including salary_grade
*Fixed a typo in the view salary_grade template to display the midpoint.  Bug 668386.  Also changed the order on the form display for salary_grade
*Modified the display string for positions to include the facility and department.  This is in case any customized sites want to have the position code not be required.
*

==4.0.9==
Released Dec 21, 2010
===Completed===
*major reporting changes including:
**added (left|right) joins to form relationship
**added ability to pivot on report rows
**added ability to merge report views
**added ability to add aggregating/dependent functions to form relationships
**column/bar charts now label the amounts
**null date fixes
**parent field is always included in zebra_XXX tables
*many translation fixes and improvements including:
**made submit buttons translatable
**made many report options translatable
**cleaned up extraneous punctuation and spacing in translations
**removed hard-coded english text from many .php files and put them into .xml files
**fallback behavior when no en_US version of a translation is present
**fixes for translations template generation tools
*form validation changes:
**added ability to hook in to a forms validate method via a module.  
**moved some of the validation methods to the new hooks
**added email validation
*removed need to set i2ce lib path in site configuration file
*fixed problem when old version of i2ce library was hanging around
*fixed task inheritance issues for next of kin and dependents
*added names for various contacts (e.g. emergency)
*made form history page more flexible
*added ability to enable modules from the command line: php index.php --update=1 --enable=formDocumentor
*don't use buggy version of APC
==4.0.10==
Released Dec 21, 2010
===Completed===
*Fix javascript typo for submit buttons
==4.0.11==
Released March 1, 2011
===Completed===
*added ability to remap form ids easily
*added enhancements to delete records safely and store them in deleted_record table
*added field history default implementation for form storage mechanisms
*improved the packaging and release tools
*Manage: Made the position code be optional
*added isoc-08 to job templates
*translation fixups 
*aded a Search display class for Custom reports so the button could be customized as well as any other part of the display.
*Made the language field be required to be unique based on the parent for the person language form.  Bug 723929.
*Made it so the person ID form doesn't allow duplicate values id/id_type combination as well as the same id_type for a given person.  Bug 723907.
*added in i2ce-site module to mark sites/handle packaging issues
*pdf -- description header gets wordwrapped and added only on the first page between the regular header and table contents
*textlayout cell -- always have mininum width of 1.  stop infinite loop if the width of the cell is less than the character it is trying to place
*textlayout added php5-gd to maverick ubuntu packaging
*Changed the text of the default custom report button to be 'Table' to be more clear.  Added an option to hide certain custom report display buttons when appropriate.
*Fixed up ifset='dateblank' check for the position form.
*Added in the limits to the PDF printed reports if any were selected.
*Added an apply limits button to the report limit table to make it simpler to just apply the limits so the chart options doesn't have to pop up just to redisplay based on the limit.  displays  only if there are multiple controls. 
*Added a function to custom reports display to return a string representation of the limits for the current report.
*formworm -- on a multi submit, dont set to an optionmenu to null if it never existed in the first place
*added in a textual display of the limits for a given report so it's easy to see on the page
*Fixed 2 bugs in processing ifset for display data that did the reverse action, but only accepted uppercase for true.  Both these are now fixed.
*Fixed typos in flat for last_modified check
*pie charts -- prevent it from failing on php warnings
*CustomReports: fix bug when we were not getting all of the disabled field display information when requested.  this is the correct fix for rev 2281 and 2283 so that charting and total reports now work
*Custom Report Pivoting:  avoid duplicating pivot links on +id fields
*add REFERENCE form field and report selector
*many bug fixes to multiflat
*lastentry form storage --- fixed issue with creating callbacks for field references
*customreports:  added a missing negation operator when dropping the existing report
*fixed typo in Administrators name for user access mechanisms
*fixed up the typos in the getFieldsMappingToList static method in I2CE_List.
*Modified addAjaxLink to set the id for the anchor by name instead of by id since that was causing a libxml warning about name and id being the same.  Removed the ids from the form relationship templates where this was happening.
*Fixed typo in FormRelationship_Join.
*added  password check on update

==4.0.12==
Released March 9, 2011
===Completed===
*improved the packaging and release tools
*Added the C page size for printed forms
*Fixed the limit description display on reports to work with multi-selection limits.
*translation related fixups
==4.0.13==
Released April 26, 2011
===Completed===
*form documentor now allows you to select the forms you want to document on
*Made some speed improvements to the report caching process.
*Made some speed improvements to the report caching process.
*fixed description for report export and delete record modules
*formrelationship: added bounds checking when calulating ancestral forms
*link to edit comptency_evaluation is now wrapped around a span to ensure that the person-simple-competency module is enabled
*iHRIS Qualify -- Added some needed task descriptions.  Updated the display and sort for the discplinary action reason form.  Fixed the registration object being set on the view person page to only set on the node because the registration number was incorrect for multiple trainings.
==4.0.14==
Released May 23, 2011
===Completed===
*added hidden elements for bad form fields inside of the error message div
*added tool to quickly change the english source text for a translation  (translatewiki.net)
*added too to quickly change the english source text for a translation
*Spanish translations (Thanks Marino!)
*Tagalog, Dutch and German translations (Thanks translatewiki!)
*json_encode call in delete record checks php version before doing JSON_FORCE_OBJECT  (should fix delete record not working in 5.2)
*added mootools-core evertime i2ce_submitbutton was added
*added a field which is an integer valued percentage
*CustomReports -- generate all added some checks on time that this was called
*added module to create standardized letters/forms based on open office documents [[Standardized Letters (ODT)|see instructions]]
*made the site of a training course non-unique
==4.0.15==
Released May 27, 2011
===Completed===
*changed branding from capacity to capacityplus
*fixed issues with sample data and small text changes
*removed debugging statments in scheduled trainig course
*for # of enrolled students in training course, added some bounds checking
*changed duty commencment text in training module
*changed popup text for search page
*updated debian packaging so natty now works
==4.0.16==
Released June 29, 2011
===Completed===
*if a submit the button has class button_disabled, then the submit does not work.  also made it so that clicking once on the button will disable it (and add the button_disabled class) to prevent double submissions
*added natty packgin for user-ldap modules
*Modified the sub joins for a relationship to not do a left join if there are no joins to be joined on.
*Add a couple functions to I2CE_List for buildDataTree to remove duplicates at the same level or lower so the same value didn't show up multiple times.  
*bounds check to supress warning message in edit tasks/role page
*FormCache -- Export now checks to see if the tables are present before trying to export them as mysqldump was failing out
*fatal error message now has a 'Show Details' to see the message and trace
*added UI and logic to limit a report view to a selected task
*Fix for IE not working with tree selectors when the id had a + in it so added in a simple replace for the id.  The name still works with the + so that wasn't changed so the limits still work correctly.
*allow checkbox display style for map_mult
*map mult: added some checks to prevent values from being repeated when getting/setting the field
*Modified MAPPED limits so they will display as a tree if that is the default style for the MAPPED field and the comparison is 'equals' and it isn't a multiple selection field.  
*Added in an option to provide limits for a reporting function in a relationship for the created MAPPED form field.  The only way to add/edit this information is in a module or directly in magic data.  
*Fixed the relationship getFunctionDetails method to return the functions in the dependency order so required functions appear first so they will be populated first and the dependent functions will then work.
*Added in a DELETE statement for custom reports when the drop_empty field is set for the form.  As far as I could tell drop_empty (required in the report editor) wasn't doing anything so this should fix that.
*Modified the displayDate method to allow formatting based on magic data values if set.
*multi flat storage -- more informative error message 
*binary files -- if the file is zero length, don't show a link to download it
*added some bounds check when get the display value for a list so the error log does not fill with errors 
*PrintedForms:ODT --  do html_entities on  the values set in the document (it is xml after all) and make fields not found blank so it looks prettier
*fix bug in custom reports when you are left joining but not limiting by one. 
*more verbose//meaningful error when you cannot add a field to a form
*printed forms ODT -- non-matched fields are delted and all values are wrapper in htmlentities
==4.0.17==
Released Sept 14, 2011
===Completed===
*fixed year drop-down lists being off by a year. Fixes bug [https://bugs.launchpad.net/pmoralg/+bug/846640 846640]
*fixed processing of module dependencies for optional modules.  Fixes bug [https://bugs.launchpad.net/pmoralg/+bug/846645 846645]
*export report -- erases the relationships, reports and reportViews that it is defining a report for
*added fr_ML as a default available locale
*Minor javascript tweaks to correct some issues with IE. 
*Sorted the limit display args based on key so it won't be based on how it was saved in magic data and will be based on what index was set.
*Added translateable descriptions for limits and added a fuzzy method to return the given selected data based on the description.  Updated custom reports to use these new descriptions.  Fixes Bug [https://bugs.launchpad.net/pmoralg/+bug/828008 828008]
*when a varchar field is not indexed, change it to a text field to keep the row size down -- fixes failure of generation for large reports. Fixes bug [https://bugs.launchpad.net/pmoralg/+bug/824598 824598]
*Added in check to make sure a selected value for the tree select is a mapped value to avoid a warning when using list().  Fixes bug [https://bugs.launchpad.net/pmoralg/+bug/823965 823965]
*added expiremental code to resict null/not-null values when doing a min/max_parent limit
*Field Validation:
**Added isValid check for REFERENCE fields to return '' if not valid
**Fixed DBValue check in FF_save for magic data storage
**Modified the FF_save methods in form storage to allow saving a value that is blank even when isValid returns false becuase a blank value is commonly invalid by that function, but blank values should be allowed to overwrite when needed.  
**Update currency form field to return '' when not valid
**modified getDBValue for MAP and MAP_MULT to return '' when it isn't valid instead of '|' so this blank check will work correctly.
*Form Submission:
**moved submitbutton javascript to core.  it now also processes the action and method classValues
**formworm was not passing the input type=sumbit name/value in chrome.  it will now insert a hidden element to pass the values before submission
**load classvalues javascript before submit button
*Reports:
**make ajax search work with tree view limits
**Updated field limits to add in equals and in options for MAP_MULT to work logically. This makes it so that if the field is a MAP_MULT then if any of the entries equal the given value (or any of the in values) then it will return as matching
**Report Selector multiple improvements:
***added an optional clear button.  moved hard-coded DOM to templates
***field will show a clear button if the field is not required
***you can now chose to show limits or not
*Translation:
**added default-locales module to handle to locale we include by default.  
**updated locale selector page to allow you to select one of the defualt locales.  
**updated debian.php and release.php scripts to read the default locale list
**enabled default locale list module in ihris manage and ihris qualify
*changed task and role editing to use checkbox instead of multi-select
*DisplayData:  can turn any <SELECT> into checkbox list by specifying display='checkbox' as an atrtribute
*centralize processing of OPTIONS display data with the usual display data. 
*PrintedForms_ODT library now supports images (with a warning message) and uses the phpodt library http://www.odtphp.com/
*Image FormField -- get width and height properties added.  also added abiltiy to manipulate as a resource
*Training:
**added training-instructor module which allows you to select the course instructor as a person from the system
==4.0.18==
===Completed===
Released Sept 15, 2011
*fixed issue in packaging that caused the mootools version to bumped
*fixed issue with sample data not loading -- entries in the form table were being created unnecessarily

==4.0.19==
===Completed===
Released Oct 19, 2011
*fixed handling of output buffering when the bottom-most ouput buffer is not the default.  for example this happens with new installs of ubuntu 11.04 (natty) with zlib compression turned on by default
*attempt to validate sort fields against displayed fields when sorting report view/save default options.  fixes bug [https://launchpad.net/bugs/867439 867439]
*modified display for report view so that you can select 'none' as sort order.  removing all sort orders will also go to none 
*pass all arguements to parent class search method in a db-form storage if it fails to get the query. fixes bug [https://launchpad.net/bugs/867493 867493]
*fixed fatal error when updating causes a module to be removed

==4.0.21==
Released Dec 5, 2011. Changes from 4.0.19 include:
*new translations from http://translatewiki.net  Thanks Siebrand!
*faster report generation:
**Modified the report cache queries to speed things up.  Now updates are done instead of insert at each step.  Also, less tmp tables are created since the update doesn't need a new table.  When there are complicated joins then the 'old' way is still done.  
**removed md5 calculations except when the next set of queries 
**Stopped using updates when it's a right join.  
**Fixed the str_ireplace to use spaces to avoid changing case when it wasn't an AS.  Also had it display the total updates made like totals rows changes for INSERT.
*added single user access and auto-login features
*killed off some spammy error messages related to forms not being registered yet in the entry form storage mechanism
*custom reports:
**fixed issue in determining if report function is numeric
**added in some additional error messaging and validation for reporting functions
**change E_USER_ERROR to NOTICE to avoid system halt when generating a report
*form storage entry -- fixed issue when parent_id is not-numeric
*fixed issue removing a module that is tagged as needing to be updated [https://launchpad.net/bugs/853936 Bug 853936]
*moved the autoloader to use the spl_autoload_register so that multiple libraries can be imported (e.g. PHPExcel)
==4.0.22==
Released March 9, 2012. Changes from 4.0.21 include:
*Translations:
**Fixed locale selector at bottom of screen
**Added Czech as a default langauge.  Special thanks to [https://launchpad.net/~tsbook Zbyněk Schwarz] 
*iHRIS Qualify:
**Added PersonDemographic as a requirement to iHRIS Qualify 
*iHRIS Manage:
**fixed typo in fuzzy method to check if the person position is active
**added new page to create a new position and set it for a person at the same time
*iHRIS Common:
**fix task inheritence for next of kin module
*I2CE:
**suppress error messages when getting ids in formstorage_db
**fixups for cleanlyEndOutputBuffers
**Entry Form Storage -- fixed issue with order by (mysql does not do the orderby within a sub-select)
**warning message supresions for: admin module, templates, text layout tools
**fixed the c_node.isSameNode javascript error in firefox 10
**MagicDataTemplate -- make sure class name is unset
**added better image scaling in printed form PDF rendering.   added some error checks in the module for magic data
**post delete hook cleans up the form, rather than the whole factory
**Added in option for 'linked' report fields to display as an image instead of just a link for IMAGE type formfields

==Outstanding==
*Form Relationship:
**Allow for more complicated joins in a form relationship -- e.g. "secondary" conditions on ancestral forms.  Done for SQL.  Needs to be done for  getFormsSatisfying()
**Allow for joining a child form in a relationship multiply (both in a report and in the getFormsSatisfying())
**handle joining "any" form and make joining forms clearer
*Add easy support for multiple platforms:
**Add tests to determine platforms, e.g. ie7, firefox, safari, chrome, mobile (which ones?)
**platform should be saved in a session variable
**Add support to the file search for platform specific files (e.g. for css).  For example:  <p>
<source lang='xml'>
  <path name='css'>
  <!-- the default platform-->
  <value>./css/default</value>
</path>
<path name='css' platform='ie7'>
  <value>./css/ie7</value>
</path>
</source></p>
**Add support for "platform resolution."  For example search for  ie7, then ie then the default
*Field Containers
**Break up existing limits to separate modules for fields and relationships
**Add in  [[Extending Form Limits | form limits]]
*Standardized letters/forms:
**Add in return/view links for standardized letter menu
**Search results can be used to generate multiple letters at once
**add new display "table" which can loop through multiple child forms in a relationship

*Qualify: Use tasks for permission handling instead of roles for everything instead of just a few places.
*Manage:  when a person passes a training course which has CEUs, those CEUS are added as a child form to that person.
*in the "Configure System" page, when the user's role is 'admin' provide a link to the 'Project Communication' page and 'Technical Documentation' page on the wiki.  People are not finding this when they need to
*when a list is read-only, then do not show the 'edit/update' link from the database lists page.  instead go to the view list page.
*allow way to see a list of the forms and their instances that a related to a particular form (parent-child or mapped value to a list)
*form storage entry should allow string id's not just unique integers across all forms stored in entry.
*the FormStorage::migrateForm() method should not create the named form in the entry table if it is not already present -- causes an issues with loading of the sample data b/c facility_contact could for example be created in the FacilityContact module ''before'' the sample data defining facility contact is loaded.
*add in iso currencies to pre-populate currencies
*Display the limits that a report is currently set to on the report display.
*CSV/Excel report export -- add option to show metadata about what limits were chosen, when report was generated (ask Julie S.)
*Move all string from php to templates
*Add in [[Form Storage -- Simply Joined Table|Simply Joined]] mechanisim for forms to enable reading in data from openMRS style vertical tables.
*Review strings in .pot files to ensure that they translatable as sentences and rework templates/make printf substitutions as appropriate
*Fix-up selection list to be a tree for position+facility rather than a drop down list:<br/>we should be able to set position+facility to have default display fields 'facility+location:county:district:[region]:country'  <br/>the problem is that currently, facility+location can take values in either the forms 'county' or 'district' and using the the above display fields string, we would only list the facilities whose location are a county.
*Custom Reports:  when a form is componentized, add "easy" option to limit based on the components.  e.g. show only the people within "Northern Region"<br/> Optionally define and use the metadata at /modules/forms/form_storage/options/$storage/component/name
*Speedup validation of mapfields w/ unique_field set to be something like 'country:region'
*Speedup I2CE_List::monsterMash and I2Ce_List::createDataTree
**short circuit and return once a match is found instead of getting all the matches
**If two successive forms have storage mechanisms subclassing I2CE_FormStorage_DB try to use a sub-select rather than process through PHP
*replace instances of ''foreach($something) { $this->template->appendTemplateFile('some.html',$appendNode);}'' with ''$add_node = $this->template->loadHTMLFile('some.html'); foreach ($something) { $this->template->appendNode($add_node->clone(true),$append_node);}''
*Add tasks to Qualify
*add in limits for dates where date is(requested form MVC):
**after a given time period from now (e.g. after 6 months pervious to now)
***period in months (as int)
***period in year (as int)
**before a given time period from now (e.g. after 6 months pervious to now)
***period in months (as int)
***period in year (as int)
*Training Sample data should be separated from Medical Sample Data.  Currently ManageMedicalData enables SampleData-training_course_category which requires training-course.
*Add in MongoDB Magic Data Storage
*Modify Magic Data Storage to add a canonical/permanent flag so permanent storage will never be cleared.  Add initialize option to choose MongoDB or DB to be used as permanent storage.
