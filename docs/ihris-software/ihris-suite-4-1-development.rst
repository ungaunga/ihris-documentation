IHRIS Suite 4.1 Development
===========================

==Version 4.1.10==
Released September 5, 2014

* New Features
** Web Services for list drop downs.  This will speed up the display for more complicated displays (like Country -> District -> County -> Facility) so only the needed data to display is downloaded.  This also includes an option for auto completion for these fields.
** Added an option to save binary files in the file system to reduce database sizes when many files are saved in the database.  Enabling this option requires an additional backup of the binary files save directory.  For existing data this does require migrating the data which may take some time depending on the amount of binary files used.

* Technical Features
** Option to use alternate templates. 
** Added a database transaction when validating a form to avoid unique constraint problems when saving.
** Modified magic data translations to set the default value as well as the translated value when changes are made to the default locale.
** Added option for ODT templates to save them in a document form field after generation when desired to avoid having to generate many times.
** Changes to form storage caching to not force caching on drop down displays.  To avoid cache synchronization issues, also added in an option on saving forms to update the individual record in the cache instead of marking the cache as dirty.

* Minor Changes
** Added ++date, ++user_name and ++time for ODT templates.
** Changed the default display for multiple selection mapped fields to use checkboxes.
** Modified cross tab report to use the displayOrder setting for the order of the columns in the report.
** Added option to not sort ENUM form fields if not desired.
** Added option to set some lists as publicly visible so the web services lists can be used on public pages, for example for self service forms.
** Minor changes to the display of user statistics including a link the parent form to view more details.
** Confirmation message on saving person and person child forms.
** Added calendar display page for scheduled training courses.

* Issues Resolved
** Fixed issues with using SSL/HTTPS.
** Fixed issue with date greater than and less than limits for limiting in form relationships.
** Fixed issue with getMappedValue in reports to not do look ups on aggregate columns.
** Fixed issue with max_parent limits in form relationships to match all child forms in order.
** Fixed issue with fatal error on an invalid date comparison.
** Fixed some display issues with international dates that was displaying the wrong year in some cases.
** Fixed crash possibility in Ubuntu 14.04 when checking for absolute file system paths.
** Fixed issue with changing locales that sometimes caused file locations to be remembered for a few minutes.
** Fixed issue with the display of time fields.
** Fixed issue with display user statistics before there have been 5 days of data entry.
** Only generate the search report when it is stale when accessing the search page.
** Fixed issue related to the created field for multi flat storage for aggregated sites.

==Version 4.1.9==
Released January 10, 2014
* New Features
** You can now set an automatic logout time for the site.  All users will be logged out after this timeframe.  It works in two ways.  The first uses JavaScript so the page will be sent to the logout page after the set amount of time.  If this JavaScript is blocked for any reason, then next page access will send the user to the login page again.  This can be enabled by setting /user_prefs/timeout/user_timeout to a number in seconds.  A message can be customized by setting /user_prefs/timeout/user_timeout_message.
** You can now link cadres to WHO recommended ISCO classification for health workers.
** Salary information isn't as tightly coupled with person position details so can be more easily removed if not needed for a customization.  This also allows you to more easily add forms that are tied to the person position details by using hooks so you don't have to create a new page class to do this.
** Added a new Date field type that only includes year and month.  You can use the form field type of DATE_YM.
** You can now create training certificates, standardized hire letters as PDF and Word files (available before only as OpenOffice ODT files).
** You can extend a basic calendar display page to add data in a calendar view.  You can use this by enabling the Calendar module and then extending the iHRIS_PageCalendar page.
** A creation date is now saved with all records and can be included in any custom reports as well.
** Added compact page to training course that allows compact editing of exam results of students for all exams at once.
** Show existing students in a scheduled course when adding new students to a scheduled course.

* Technical Features
** You can now highlight and/or add options to the left hand menu without having to create a new page class.  Added active menu hook to set the active menu on any pages without having to create or subclass an I2CE_Page and updated lists page in iHRIS Common to use this hook.
** The I2CE_PageViewChildren page can now handle displaying grandchild forms and below.
** The callHooks method can take a variable number of arguments instead of passing a single array with all arguments.
** Added REFERENCE field links in form relationships so you can link to the referred form in the relationship.

* Issues Resolved
** Many improvements and features to generation of standardized letters and reports (ODT, Word and PDF)
** Fixed handling of view and exporting reports when reported fields have upper case letters in the form or field.
** Fixed some issues with last modified time in custom reports.

==Version 4.1.5==
*I2CE
**Reporting
***The report view edit page now displays a link to the report it is based on, likewise the report has a link to the relationship it is based on for easier access to editing.
***Reporting functions (e.g. getFieldObj()) can now search for dependent SQL functions in the relationship when creating a report.
***The internal field last_modified (which records a datetime) can now be displayed in the report
***Reporting on mapped values has been improved: a warning message will be displayed when setupMappedValues() returns too many values at once so the report can be modified not to display them as mapped values. Also a blank string will be returned when searched for a value in the mapped value is null.
***buildDataTree functions are now moved to I2CE_DataTree class.
***Fields can now use values from reports instead of building them from cached tables as this process was very slowly.
***Headwrap for Chart Headers
***Added in hasAncestor method for form relationships to determine if the given joined form has ancestral conditions and updated the custom report query generator to check that when building the report queries to avoid fatal errors when joining in the ancestral condition.
***On displaying the report the Action Link will now be at the top
**Bugs Fixed
***Fixed report limits processing in some instances with report internals that weren't working correctly when there was no reporting_internals child for the report.
***Improved report generation speed
***ODT printed form render.  Fixed issue where special functions (such as date) with arguments were not being processed
***Javascript hack to fix bug 1053458 for Chrome adding operand limits to a form relationship.
***Fixed listDisplayFields signature for file form storage
***Fixed capitalization mistake in I2CE_PageFormLists
***A form subclassing simple list returns the correct template file if it has a special one
***Fix for javascript format of large numbers with commas
***Added in limit_description check for yesno limit template.
**New Features
***Added in JSON export format for reports
***Added in default display options for action report displays to allow for pagination.  Also fixed the jumper display to work correctly for action report displays.
***Registered validate_formfield and form_cleanup hooks in FormStorage so they also work on the CLI

*Common and Manage
**Added user access information on the user page to show login history and recent data entry
**Set role restriction for the mass delete pages
**Added in mass delete feature for deleting multiple people at once by the search report and by facility

==Version 4.1.4==
*added a PASSPORT FormField with the option to resize the image dimensions so that the image can be resized to a reasonable size for easy display in view.html and compression of file size (Thanks Sovello!)
*Translation to Arabic (Thanks for Prof. Adel Khelifi and his team from Alhosn University)
*Data auditing for all form storage mechanisms
*Magic data browser import from XML or CSV files or from a URL
*Various bug fixes and improvements for reporting including:
**fix JOIN so that it works properly by dropping rows on which no form was joined.  also added unset() when  was used in a foreach(XXX as &) to avoid issues with unexpectedly modifying values of
**the ability to specify order for limits (filters) in reports
**Fixed up command line show report page so it works correctly.
**Fixes for function limits in reports.  Some recent changes caused them to no longer appear in limits.
**Made sure that function limits are enabled before displaying them.
**fixed validation of sort fields in reports so fields that are descending are not dropped
**if a report returns no data, then you can create a new form based on the search data.  need to specify the creation page under /modules/CustomReprots/reportViews//create_link
*Added in LDAP form storage mechanism to read and write to an LDAP server
*Better support for iHRIS under OSX
*Updated to MooTools version 1.4.5
*use php 5.3 sort for ASSOC_LIST
*Update DHIS User access module so it will initialize
*Re-added back in method to log users when logging in and out.
*Added in user option for recent forms page so you can limit results by the user or everyone.
*when adding a form field, the field node gets a class of the form  so that we can pull it out for css
*fixed bug which caused inline "script src=" tags to not be placed in header
*Improvements to user interface:
**submit button - do not disable click events.  re-enable after 5 seconds
**tree view data selection scrolls to selected option
**added twitter bootstrap style drop down menus
*added in action page style as a possible preliminary style for web services type pages.
*added welcomeNamedUser('welcome %s','welcome') template function
*updated version information to 4.1 for PERCENT module
*checkbox list display preserves id attribute
*Fix for tree select auto completer script to avoid javascript errors.
*Person Page
**add person page will now process request variables on post populate
**Added a form history link to the passport photo template.
**validate of adding a person form uses '0' instead of 0 to check blank id
**view page redirect to home page if the id of the person is 0
*Manage:
**Modified the add passport photo link to display even when a photo is there so new passport photos can be added even when one exists.  This is to allow for a historical record of the passport photos without having to update the existing form.
**improved some english source text for translations (thanks for reporting at http://translatewiki.net)
*Qualify:
**clarified description for helper forms to link facilities and institutions
**improved some english source text for translations (thanks for reporting at http://translatewiki.net)

==Version 4.1.3==
Released July 23, 2012
*Form Storage:
**form storage mechanism default listFields and listDisplayFields did not return the parent field value.  
**fixed return value for db form storage when there is no search query
**fixed issue with MDB2 lower casing fields references with lookupField() and lookupDisplayField()
**LDAP Form Storage:
***added write methods for LDAP storage
***getChildIds is  a specially implemented fast method
***can get parent field.  
***added fast listFields method which is used by form cache.  added support for different scopes when searching.  
*Reporting:
**Added missing _getDisplayValue to MAP form field from REFERENCE to work with the _reportSelect style method.
**Removed debug statement from reportSelect method for MAP fields.
**Fixed typo in report selector default content.
**Added in the reportSelect method for MAP fields to work like reference fields for the report selection display when desired.  The meta data needs to be set up like REFERENCEs for this to work correctly.
**Fixed report selector so that the name is set to the ID of the field being used.
**Fixed custom report selector so that limits will work correctly.  Made many of the ids have a unique identifier for the report selector so that it will work when multiple selectors are on one page so the javascript doesn't get confused by the ids.
**custom reports -- fixed callback reference
*Forms and Fields
**added option for STRING_PASS so that you can display a second title between the two password fields
**Modified the required field marker so the * is in a span with a class so it can be easily found and modified if necessary (via CSS or other methods).
**Modified the unique field validation check to not set anything invalid when the parent is the unique_field to check but it isn't set.
**DatePicker now localizes properly
**Hack to fix datepicker.  For some reason when it fades the old contents were still getting clicks so move it out of the way.
**Modified cached form storage to ignore the stale time check and only look at if the form is dirty before re-caching the information so when the data is modified it will be updated the next time it is required.
**removed debugging message from ASSOC_PERCENT form field
**javascript number formater removes commas
**percent:  setting invalid value returns null not false
**fixed evaluation of post variable so that we can keep the percent unset
*Users:
**user acces ldap -- fixed bug with getting user ids
**fixed typo in 'resend' email page
**Account verification email can optionally send an html message instead of a text one
*Mail module can handle html message if php-mail and php-mail-mime are installed.  (needs better error checking and needs to enable it for php's mail function)
*Pages and Templates and General User Interface:
**make button_confirm_notchild button layout consistent with other templates
**addHeaderLink is now smarter in checking if a javascript file has already been included
**fixed redisplay of message box
**changed back/more button labels on paged message handler
**multi page form -- prevent fatal error if no parent object
**multi form page now will set object on anonymous child forms
**message notice -- make the window have a very negative z index so that it does not block other elements on page when it is closed.
**removed debugging message form message notice
**fixed handling of message notice caption
**fixed invalid css warning message
** make CEUs appear in the training course
*view position page:  check validity of job and supervisor fields before setting href in order to avoid fatal error



==Version 4.1.2==
Released April 18, 2012

*Added extra option for field limits to include a manual where clause for a limit when necessary.  This probably can be done in a better way, but this is a quick fix that won't break anything when the extra_where option isn't set.  This also needs to be added to the interface to allow editing of it.  For now it must be done in a module to create the entry in magic data.
*Removed extra name attribute in template to avoid XML errors when the name and id are the same.
*Added in check in delete record page to make sure something was returned when searching for linked forms before operating on the results.
*Fixed typo in limit_val check for first character being '$'.
*paged messagebox can now have alternate title and can handle more than one instance on a page
*user form -- call pre and post_save_form hooks.  in particular makes sure user form is marked as dirty on save
*user account request - fixed invalid reference to form factory causing fatal error
*fixed typo in checking individual form storage / form stale times
*fixed versions for 4.1 series for Custom Report Selector and Reference Field
*set version for magic data defining show page for custom reports as it was not updating properly for people coming from a late version of the 4.0 series to 4.1
*fix up the displayname of the deleterecords and exportreports modules
*fixed issue with setting role in the user form/email verification
*when logging out, unset ['referal'] so we don't end up in an endless loop of login credentials (esp. with the verify email access link)
*added some more flexibility to the request user account page
*percent fields now have a meta/check_bad_percent option to allow you to enter in 0.2 as 20%
*fixed up the I2CE_FormField::optionsHasPath so you can also pass an array
*suppress error messages when getting ids in formstorage_db
*fixed call to cleanlyEndOutputBuffers, cleanlyEndOutputBuffers will trim any empty space. 
*added Czech as a default language
*Entry Form Storage -- fixed issue with order by (mysql does not do the orderby within a sub-select)
*Module admin cleanup to suppress warning messages
*MagicDataTemplate -- make sure class name is unset
*ModuleLimits -- only allow to create a module limit when a mapped field has exactly one selectable form
*be smarter about showing which module limits to add to a report field.  added debugging information for cssc
*Fixed the cached buildDataTree to work when forms aren't displayed (e.g. country:[region]:district:etc.).  Since region wasn't in the display it was getting skipped completely.  Fixed this by causing the displayed forms to find the correct link_field to use to determine which section it needed to be placed in.
*fixed the c_node.isSameNode javascript error in firefox 10
*Moved the dumpStaticURL call earlier to speed up processing in these cases.  (No db connection, no session).  Also reused the results of parseDSN in the dbConnect call so if this needs to be undone then change that back as well.  I'm not sure if this may cause problems anywhere.  It seems ok with some quick testing, but there may be cases where more needs to be loaded.
*MongoDB Magic data storage
**added optional mangodb form storage mechanism for testing/expiremental purposes.  you can enable it by putting the line 'SetEnv I2CE_CONFIG_PROTOCOL mongodb' in .htaccess/
**fixed install of MDS storage for mongo vs. config_alt
**avoid fatal error if mongodb is not up and running properly
*Modified the cached form export to include a date string in the filename.  Also commented out logging the mysqldump command for security.
*slight speed up to processing attributes in MDN
*printed forms: added type check to supress fatal error
*Put back in accidentally deleted addDatePicker call.
*Added options for DatePicker to magic data.  Added the english days and months to use for the datepicker options so they can be set for other languages.  This doesn't fix any underlying issues with the date object and internationalization, but it does allow the datepicker to display in the chosen language.
*Commented out the not stale message for form caches since it can make a lot of messages with drop downs using cached tables.
*Commented out the skipping cached table when not dirty message because with the new usage of cached tables for drop downs it gets really spammy.
*Added option to have the blank text for drop downs in magic data so it can be translated.
*Removed debugging echo statement from message notice module.
*Removed debug statements from reporting function swissconfig.
*improvements to paginated message box.  multiple overlayed messages are now paginated
*Updated the ODT report printed form to set the ++report_limit even if nothing is there so the template will replace it with nothing when appropriate.
*Made some fixes to the buildDataTree built by cached forms.  Things were getting put in the wrong place because of the way the joins have to be created so (e.g.) facilities linked by district showed up under each county.  Now it won't include duplicates and it adds things to the correct linked place.  It also now will strip out the display content for the linked field since that will be above it in the tree to avoid too much extra info.  There's probably a better way to handle this, but I'm not sure what's best.
*Fixed typo in default display for lists that had an invalid call to array_pad because of mismatched parentheses.
*added I2CE_AjaxSubmitButton which does form submission like I2CE_SubmitButton but replaces content of current page with filtered response. ajax submit button is renabled after 5 seconds.  
*Added in an option to include ODT files as an output for reports.  This allows you to customize the printed output however you would like.  This needs to be enhanced to allow image types from the report.
*Modified adding the manifest.xml file to the ODT zip archive to not include ./ because that was making it look like a different file if it already existed and causing it to appear twice in the archive which made Word and Libre/Open Office not happy with the output.
*I2CE_FormField_MAP now preserves the 'class' attribute
*ajax submit button empties the existing content
*Updated the requirements for PrintedFormsODT to require PrintedForms allowing less than 4.2 instead of 4.1.
*fix fatal error when putting html in a overlayed message box
*removed the setShowForm and replaced it with a check to see if a formfield is part of a <form>
*relax nullity check to non-strict when getting header for generate password
*fixed typo in user request page
*clearer user message when requesting account creation
*fixed typo in fatal error message
*Changed the ids in some relationship function templates to not have the same name and id for 'a' tags because LibXML complains about them being a duplicate ID and since the ID is being changed after loading anyway it isn't necessary to be the same.  There doesn't seem to be a problem with changing the id when testing this change, but it is possible there are some unintended consequences.
*Split report functions templates into 2 and loaded them when needed instead of setting has_available_functions to avoid duplicate id error with reporting_functions_container.
*Added in default setting for  variable to avoid undefined variable warning.
*Modified the buildDataTree cached query to not include order by fields in the select when they're not needed.
*process dom on formfield with href preserves all attributes (except href of course)
*Fixed join type for data trees when both levels of the forms are the same.
*update to mootools 1.4.2
*made some numeric form fields tolerant of commas on submission
*added javascript validation and formatting to some of the form fields
*fix args passed to builddatatree in MAP_MULTUNION
*form field options can now be set on a path
*cached forms build data tree -- lowercase result access properties as MDB2 does not respect them
*invalid call to setForm() on a page will no longer cause fatal error
*user form -- set sort field to be username, not name
*associative inputs -- select all on focus
*cleanup/improve regexps/matching for associative percent form field
*Updated the pChart library to 2.1.3.
*made limits use getDBValue() instead of getValue() by default.  Changed some implodes to explodes for within limits
*Fixed up conversion of LIKE to regexp
*command line update exits after done --avoid misleading error message about the Wrangler
*made translatable (via magic data) all form field message.  added helper functions to find set named error message. 
*Where a formfield has multiple unique_fields (including one with a mapped value (i.e. region:country) then the non mapped value wasn't doing the check correctly.
*Redid the validate_formfield for I2CE_Module_Lists to remove the call to monsterMash.  Also deleted the monsterMash code from I2CE_List.  Fixes bug 906618.
*Made the Mailer configurations not required.
*feedback and forget pages now use i2ce_mailer wrapper
*TextPassword::create() switched to an instance because it is not static
*update message for request account
*linked user request with mailer
*added wrapper module 'Mailer' for mail and Pear::MAIL
*added oneiric to debian package tool
*added passwordless login function for to i2ce_user
*userform -- fixup function signature for populate and save methods.   add in some error checking to avoid fatal errors
*user access -- avoid fatal error if user is not found when requesting their info
*post delete hook cleans up the form, rather than the whole factory
*Added in getLimitsByForm to the ModuleAccess class as an abstract method.  Added in checking for module_limits in a report field to limit by the given module with details passed by a hook in the module to determine what to link by so li
mited access users only see certain records in a report.
*added email request account
*Added in get_report_module_limit_options for SwissConfig in CustomReports to add the option to link a field in a report to an availble field in the module to use for limiting the reports based on module details.
*Added in missing template file for displaying images inline in reports.
*Modified the buildDataTree for cached form storage to use an existing callback function instead of an anonymous function.
*comment out spammy error message in form storage entry about not getting fields 
*Added in option for 'linked' report fields to display as an image instead of just a link for IMAGE type formfields. 
*Added an entry in /modules/forms/storage for not_assignable so that certain form storage types can't be assigned to forms directly, like 'cached'.
*added expiremental MAP_MULTUNION form field that can select muliple list members across unrelated forms
*added file that was missed for associative booleans
*Moved ModuleAccess under forms.  allow generic method to add limits to a form
*Modified the FormStorage calls to listFields and listDisplayFields to use the cached form storage when an optional argument is passed instead of the default form storage.  Fixed the reference callback check in DB form storage since it w
ouldn't allow any callbacks.  Updated I2CE_List to make showHiddenLimit a public function.  Updated I2CE_List to use the cached form storage buildDataTree function when it's available.
*Added in ModuleAccess abstract class for access type modules so that forms can preprocess the args to add any additional limits needed by the access module.
*Added form-storage-flat as a required module for CachedForms since there is a new cached form storage based off of flat storage.  Changed the caching messages to use raiseMessage instead of raiseError to reduce log spam since it is info
rmational and the full trace shouldn't be needed.  Added the cached form storage to be used for getting list data from the cache instead of the source tables.  Any call to this will cache the tables before using them.
*added formfield which is associative  list of booleans/checkboxes
*change the I2CE_List::listOptions so that is uses buildDataTree.  simplified its calling.  
*fixed typo in delayed load attribute of mapped field
*added ability to set displaystyle of joined form in relationship via the web-interface
*removed unused MAP_LINE form field
*Fixed str_ireplace call to include spaces when normalizing the case for AS in queries.
*Custom Reports
**Modified custom reports to not use updating and instead create a new tmp table and insert when it's a right join or not limited to one row.
**Made some corrections to the md5 setting procedures for custom reports.  Since updates didn't affect every row not all md5s were being set so the update was put in a separate query when needed.
**the report cache queries to speed things up.  Now updates are done instead of insert at each step.  Also, less tmp tables are created since the update doesn't need a new table.  When there are complicated joins then the 'old' way is still done.  Also removed md5 calculations except when the next set of queries needs them.  
**a validity check on reporting function data
** change E_USER_ERROR to NOTICE 
*killed off some spammy error messages related to forms not being registered yet in the entry form storage mechanism
*fixed typo in versioning of requirements for delete record module
*form storage entry -- fixed issue when parent_id is not-numeric
*updated treedata url so it includes the index.php
*fixed issue removing a module that is tagged as needing to be updated
*added in some additional error messaging and validation for reporting functions
*configurator: fixed issue when removing module on a system update


==Version 4.1.1==
Released October 19, 2011

*Gave different name attributes for the show_i2ce_hidden_link names because libXML was causing an error on loading the lists_type_header.html template.  Bug 877471.
*Added an option for MAPPED fields to use a given display style from the template (display_style='default') to override the default value if needed.  This is to fix ihris-manage bug 876827.
*Updated storeMigrateData in form storage to only unset the migrate_node after all forms have been processed.  This was causing an error when multiple forms were stored.  Bug 874600.
*Fixed syntax to make IE7 happy with tree selection.  Bug 873910.
*fixed handling of output buffering when the bottom-most output buffer is not the default.  for example this happens with new installs of ubuntu 11.04 (natty) with zlib compression turned on by default
*allow user preferred locales in magic data to over ride user details from user access mecahnism
*attempt to validate sort fields against displayed fields when sorting report view/save default options
*modified display for report view so that you can select 'none' as sort order.  removing all sort orders will also go to none
*pass all arguments to parent class search method in a db-form storage if it fails to get the query
*I2CE_FormField_MAP with a tree select now defaults to delayed load of data.
*fixed fatal error when updating causes a module to be removed
*fixed handling of temporary upload files with new html names that have [] instead of :
*support setting page default login from auto_login_user option
*single user access support setting optional password
*i2ce_user_module  is now a sublass of i2ce_module
*multi-select --  deselection of values now works
*Modified the tree view id to remove [] so it works with IE7/8.
*Added in message to signify that asterisk is a required field.
*Modified form storage search call to return false if the query can't be created because the form may not exist yet and therefore no results can be found.
*Only show error on module calls from templates if the module is enabled but can't be found.
*Added check to getChildIds query so a blank query wasn't run on the database causing an error.
*Modified the form storage entry class to not create form ids when running queries.  Bug 851071.  
*Fixed variable name for error message when you don't have permission to access the page form lists page.
*pageformlist:  checks to see if the page is a confirm page when setting the default form
*Fix for FormStorage mechanism to try to save fields that are blank (and still invalid).  This was mainly affecting magic data storage forms.
*Fixed getting the DateTime object for a date to work correctly with YEAR_ONLY dates.  Set the month/day to 01/01 for the DateTime since it requires that to work correctly.
*Modified the HTML names for form fields to use [] instead of : so PHP can handle creating the associative array and to avoid the issue with dots (.) being replaced with underscores in top level names for _POST variables.  This fixes including dots in form IDs.
**updated associative list, binary file, formfield image, int generate, lists, map_line, binary file  so that it works with [] html names
*only check for alternate task satisfaction if the user is logged in
*when setting a the primary form for alternative task satisfaction for the database list edit page, only do so if the form has a non-zero id
*when editing database list, make sure the primary form for the page is set as the default form
*Custom Reporting -- when a varchar field is not indexed, change it to a text field to keep the row size down.  
*export report -- erases the relationships, reports and reportViews that it is defining a report for
*speed up processing for silent disabling optionally enabled modules.  make set of optionally enabled modules is maximal
*Modified date field limits to use the year range defined for the field object.
*if an optional module is enabled and in conflict with a required module try to disable it
*Fixed drag windows to not have the whole window be clickable to drag it.
*reduce processing on module update
*when installing or updating a site, optional modules are now processed
*fixed issue where optional sub-modules were getting set to be required
*Updated mootools core and more js files to 1.3.2.
*updated I2CE_TreeSelect because Implements only works with classes and not objects anymore.
*Made some minor javascript adjustments because IE9 was throwing errors and stopping processing so treeview stopped working.
*Fixed typo in map mult set value.
*Added back in validate hook calls that were accidentally removed.
*Added translateable descriptions for limits and added a fuzzy method to return the given selected data based on the description.  Updated custom reports to use these new descriptions.  
*Added in check to make sure a selected value for the tree select is a mapped value to avoid a warning when using list().  Bug 823965.  From 4.0-dev 2588.
*Defined variable to avoid undefined variable warning in field limits.  From 4.0-dev 2587.
*Updated field limits to add in equals and in options for MAP_MULT to work logically.  I didn't test the checkLimit and checkLimitString methods yet, but the generateLimits work for reports.  This makes it so that if the field is a MAP_MULT then if any of the entries equal the given value (or any of the in values) then it will return as matching.  
*Allowed form storage FF_save methods to save blank values even if the formfield doesn't seem that as valid.  Updated formfields to return '' instead of other characters when the value is invalid.  From 4.0-dev 2579 and 2585.
*experimental code to restrict null/not-null values when doing a min/max_parent limit
*formworm was not passing the input type=submit name/value in chrome.  it will now insert a hidden element to pass the values before submission
*swiss factory gives more informative error message when it cannot process values
*added default-locales module to handle to locale we include by default.  updated locale selector page to allow you to select one of the defualt locales.  updated debian.php and release.php scripts to read the default locale list
*Modified limits on reports overwriting the defaults completely instead of merging them. From 4.0-dev 2574.
*fixed bug on tranlsating html blocks
*Added the supress_output check for pChart displayWeb.  Also removed the completeChart call from getImage and made it public so you can call that manually if you need to getImage().
*pchart
**Pulled out the drawing functions into a separate function and added a function to access the pImage object directly.
**Removed extraneous require_once calls from the pChart File page.
**Modified the style for a pChart to make lower case to avoid any issues with capitalization.
**Modified the pChart page to add options to the chart drawing function and to not override any palette options set by the sub class.
*updated version requirement for modules using mootools
*removed request.content.js as https://mootools.lighthouseapp.com/projects/2706/tickets/524-add-contenttype-for-requesthtml has been resolved
*updgrade to mootools 1.3.2.1
*with the report selector you can now chose to show limits or now.  corresponding option added to reference field.  had to fix up how mootools (does not) encode query variable names when going through the stub
*added classvalues JavaScript when submitbutton was called
*moved submitbutton javascript to code.  it now also processes the action and method classValues
*REFERENCE_FIELD/report selector
**selecting a REFERENCE field will show a clear button if the field is not required
**Report Selector -- added an optional clear button.  moved hard-coded DOM to templates
**some windowing fixups to the custom report selector for a REFERNCE field
*changed task and role editing to use checkbox instead of multi-select
*DisplayData:  can turn any <SELECT> into checkbox list by specifying display='checkbox' as an atrtribute
*centralize processing of OPTIONS display data with the usual display data
*suppress warning message when processing module tags
*make locale selection work with single user access
*translation tools -- now check for a title attribute in a span tag
*better checking if a value is set for a key in ASSOC_FLOAT
*moved the autoloader to use the spl_autoload_register 
*translate_create_spreadsheet -- allow you to limit the modules used from the command line
*updated magic data xml processor so that you can have <erase> and <eraseVals> nodes relative to a containing <configuration> or <configurationGroup> -- makes specifying data to delete more convenient
*PrintedForms ODT library now supports images (with a warning message) and uses the phpodt library http://www.odtphp.com/
*Image FormField -- get width and height properties added.  also added abiltiy to manipulate as a resource

==Version 4.1.0==
Released July 30, 2011.

*allow for "empty/null" form storage mechanism that doesn't do anything. 
*Context Sensitive Help
*Use a different charting software library
*Upgrade to php 5.3
**Get rid of eval's for static values/variable in subclasses
**Add in static fuzzy methods
*[[Custom Forms]]
*[[Custom Pages]]
*Add in user based permission access to forms via form relationships
*fix up how the navigation bar is handled so we don't need to subclass I2CE_Page just to handle highlighting the nav bar
*Clean up forms classes to remove as much business logic and defintions as possible and put it into magic data. <br/> having it in magic data/xml will allow use to interact more readily with other form based software e.g. openXdata or whatever as all they would need to do is to parse the xml rather than instantiate all the forms and deal with them that way.
**add in ability to define complex form validation logic in xml. probably want to have many named validations w/ a description of what they require so that people can fix errors. perhaps these should be split into "warnings" and "errors" (see the person example below).  will need to implement at least part of [[Extending Form Limits]]
***example: person position --- start date is less than or equal to end date
***example: person has validation to ensure uniqueness of the pair (firstname,surname) although this validation check can be overidden on the confirm page.
**get rid of getIDs() type methods which.  are these even used anymore?perhaps they be done via some general method getIDs($style) fuzzy method implemented by form storage and which reference a magic data e.g. /modules/forms/forms/$form/getIds/$style = {some data array}
***example: person position has a getIds() method which gets all of the person position ids associated to a given position id and for which the end date is null
***example: job has getPositins() mehtod which gets the positions associated to a job.
**get rid of main and secondary display field constants in i2ce_list class
**cleanup stuff leftover from 3.1 (Such as the listOptions, lookup mehtods and related methods. many of these are no longer references outside the defining class (e.g. getCompentnciesByType)) what about iHRIS_Search?

[[Category:iHRIS Software]][[Category:Review2013]]
