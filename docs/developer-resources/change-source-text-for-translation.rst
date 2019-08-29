Change Source Text For Translation
==================================

With revision number 2503 of I2CE/4.0-dev we have added a new tool to assist in fixing source errors in translations.  This utility is located at **I2CE/tools/translations_change_source.php**  and should be run in the top-level directory of the bazaar branch you wish to make translation changes on.

It will do the following things:

* Ask you from which module you want to change a source text
* It will ask you which source text you wish to change
* It will ask you for the new version of the source text
* It will optionally preserve the existing translations of the source text
* It will go through all the en_US  .html template files for that module and replace the source text with the new version of the source text
* It will go through the configuration .xml file for the module and see if the source text is there.  If so:
* *It will do a minor version bump of the module
* *It will change the source text in the module to the new value
* *Any values that have been changed will have a version tag added/updated with the new bumped version of the module

Sample Run
^^^^^^^^^^

.. code-block:: text

    litlfred@cumin:~/rocket_cats/dev/ihris-manage$ ../I2CE/tools/translations_change_source.php 
    
    <--- SNIP STATUS MESSAGES --->
    
    Which module would you like to fixup a english source text for?
    	0) ihris-manage
    	1) manage-registration
    	2) disciplinary-action
    	3) ihris-manage-confirmation
    	4) ihris-manage-salary
    	5) ihris-manage-custom-reports
    	6) ihris-manage-person-position
    	7) ihris-manage-person-demographic
    	8) ihris-manage-application
    	9) ihris-manage-job
    	10) ihris-manage-benefit
    	11) accident
    	12) ihris-manage-confirmation-attachment
    	13) ihris-manage-custom-reports-search-people
    	14) ihris-manage-custom-reports-position-reports
    	15) ihris-manage-custom-reports-staff-reports
    	16) ihris-manage-custom-reports-filled-positions
    	17) ihris-manage-custom-reports-facility-reports
    	18) sample-data-establishment
    	19) ihris-manage-application-attachment
    	20) ihris-manage-site-demo
    	21) ihris-manage-site
    Choice: 11
    I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/tools/translate_base.php:603)
    loadPOT (/home/litlfred/rocket_cats/dev/I2CE/tools/translations_change_source.php:81):
    	reading existing template file ./translations/templates/accident/accident.pot
    Which string would you like to change?
    	1) Can edit the workplace injuries and accidents assigned to a person
    	2) Can view the wokrplace injuries and accidents assigned to a person
    	3) Edit the workplace accident type list
    	4) Accident
    	5) Workplace Accident Type
    	6) Date of Occurence
    	7) Accident Type
    	8) Start of Applicability
    	9) End of Applicability
    	10) Follow-up Required
    	11) People Involved
    	12) Add/Update Workplace Accident
    	13) Edit This Information
    	14) Update this Information
    	15) Select another Accident Type
    	16) Workplace Accident Information
    	17) Correct this Information
    	18) View the workplace accident type list
    Choice: 12
    What is the new source?: Add Or Update Workplace Accident
    Replace:
    	Add/Update Workplace Accident
    to:
    	Add Or Update Workplace Accident
    (Yes/No): y
    Would you like to preserve the existing translations in the .po files for the locales br,de,en_GB,es,et,fr,fr_ML,fr_TG,id,it,mk,nl,pt,pt_BR,ru,sw,tl,zh_CN?
    (Yes/No): y
    
    <--- SNIP STATUS MESSAGES --->
    
    Change template file /home/litlfred/rocket_cats/dev/ihris-manage/modules/Accident/templates/en_US//view_list_accident_type.html?
    (Yes/No/Always/neVer): a
    Update the config file /home/litlfred/rocket_cats/dev/ihris-manage/modules/Accident/Accident.xml with the new source text?
    (Yes/No): y
    I2CE: I2CE->raiseError (/home/litlfred/rocket_cats/dev/I2CE/tools/translations_change_source.php:249):
    	Bumped 4.0.11.0 to 4.0.11.1 on /home/litlfred/rocket_cats/dev/ihris-manage/modules/Accident/Accident.xml
    Would you like to fixup another translation source string?
    (Yes/No): n
    

Result of Sample Run
^^^^^^^^^^^^^^^^^^^^
The results of running this operation are as follows:

.. code-block:: text

    litlfred@cumin:~/rocket_cats/dev/ihris-manage$ bzr status
    modified:
      modules/Accident/Accident.xml
      modules/Accident/templates/en_US/form_accident.html
      modules/Accident/templates/en_US/view_accident.html
      modules/Accident/templates/en_US/view_list_accident_type.html
      translations/templates/accident/br.po
      translations/templates/accident/de.po
      translations/templates/accident/en_GB.po
      translations/templates/accident/es.po
      translations/templates/accident/et.po
      translations/templates/accident/fr.po
      translations/templates/accident/fr_ML.po
      translations/templates/accident/fr_TG.po
      translations/templates/accident/id.po
      translations/templates/accident/it.po
      translations/templates/accident/mk.po
      translations/templates/accident/nl.po
      translations/templates/accident/pt.po
      translations/templates/accident/pt_BR.po
      translations/templates/accident/ru.po
      translations/templates/accident/sw.po
      translations/templates/accident/tl.po
      translations/templates/accident/zh_CN.po
    litlfred@cumin:~/rocket_cats/dev/ihris-manage$ bzr diff 
    === modified file 'modules/Accident/Accident.xml'
    --- modules/Accident/Accident.xml	2011-03-01 19:04:03 +0000
    +++ modules/Accident/Accident.xml	2011-05-05 15:11:35 +0000
    @@ -6,13 +6,13 @@
         <className>iHRIS_Module_Accident</className>
         <category>Application Component</category>
         <description>A Workplace Accident Tracking Module</description>
    -    <version>4.0.11.0</version>
    +    <version>4.0.11.1</version>
         <path name="configs">
           <value>./configs</value>
         </path>
         <requirement name="Person">
    -      <atLeast version="4.0" />
    -      <lessThan version="4.1" />
    +      <atLeast version="4.0"/>
    +      <lessThan version="4.1"/>
         </requirement>
         <path name="classes">
           <value>./lib</value>
    @@ -23,7 +23,7 @@
         <priority>150</priority>
       </metadata>
       <erase path="/modules/accident/page/history">
    -    <lessThan value="4.0.6.0" />
    +    <lessThan value="4.0.6.0"/>
       </erase>
       <configurationGroup name="accident" path="/I2CE">
         <displayName>Workplace Accident</displayName>
    @@ -244,7 +244,7 @@
                 <displayName>Page Title</displayName>
                 <description>Page Title</description>
                 <status>required:true</status>
    -            <value>Add/Update Workplace Accident</value>
    +            <version>4.0.11.1</version><value>Add Or Update Workplace Accident</value>
               </configuration>
               <configuration name="page_form" values="single">
                 <displayName>Form</displayName>
    @@ -257,4 +257,4 @@
         </configurationGroup>
         <!-- End of /I2CE/page-->
       </configurationGroup>
    -</I2CEConfiguration>
    \ No newline at end of file
    +</I2CEConfiguration>
    
    === modified file 'modules/Accident/templates/en_US/form_accident.html'
    --- modules/Accident/templates/en_US/form_accident.html	2010-08-20 16:53:10 +0000
    +++ modules/Accident/templates/en_US/form_accident.html	2011-05-05 15:11:32 +0000
    @@ -1,18 +1,13 @@
    -<tbody id="person_form">
    -<tr>
    -    <th colspan="2">Workplace Accident Information</th>
    -</tr>
    -<tr id="list_fields">
    -	<td>
    +<tbody id="person_form"><tr><th colspan="2">Workplace Accident Information</th>
    +</tr><tr id="list_fields"><td>
     	   	<span type="form" name="accident:accident_type" showhead="select">
     	   	</span>
    -		<span type='form' name="accident:start_date" showhead="default"></span>
    -		<span type='form' name="accident:end_date" showhead="default"></span>
    +		<span type="form" name="accident:start_date" showhead="default"></span>
    +		<span type="form" name="accident:end_date" showhead="default"></span>
       </td><td>
    -		<span type='form' name="accident:occurence_date" showhead="default"></span>
    -		<span type='form' name="accident:persons_involved" showhead="default"></span>
    -		<span type='form' name="accident:followup" showhead="default"></span>
    +		<span type="form" name="accident:occurence_date" showhead="default"></span>
    +		<span type="form" name="accident:persons_involved" showhead="default"></span>
    +		<span type="form" name="accident:followup" showhead="default"></span>
     		
     	</td>
    -</tr>
    -</tbody>
    +</tr></tbody>
    \ No newline at end of file
    
    === modified file 'modules/Accident/templates/en_US/view_accident.html'
    --- modules/Accident/templates/en_US/view_accident.html	2010-04-29 15:33:41 +0000
    +++ modules/Accident/templates/en_US/view_accident.html	2011-05-05 15:11:32 +0000
    @@ -1,34 +1,25 @@
    -<div task='can_view_person_accidents'>
    +<div task="can_view_person_accidents">
       <div class="editRecord">
         <p>Edit This Information</p>
    -    <ul>
    -      <span >
    -	<li  task='can_edit_person_accidents'>
    -	  <span  type="form" 
    -		 name="accident:id" 
    -		 href="accident?id=" 
    -		 parent='true'>
    +    <ul><span>
    +	<li task="can_edit_person_accidents">
    +	  <span type="form" name="accident:id" href="accident?id=" parent="true">
     	    Correct this Information
     	  </span>
     	</li>
           </span>
    -    </ul>
    -  </div> <!-- editRecord -->
    +    </ul></div> <!-- editRecord -->
     
       <div class="dataTable">
    -    <table border="0" cellspacing="0" cellpadding="0">
    -      <tr>
    -	<th colspan="2">Accident</th>
    -      </tr>
    -      <span type="form" name="accident:accident_type" showhead="default" class="even"></span>
    -      <span type="form" name="accident:occurence_date" showhead="default" ></span>
    -      <span type='form' name="accident:start_date" showhead="default" class="even"></span>
    -      <span type='form' name="accident:end_date" showhead="default"></span>
    -      <span type='form' name="accident:persons_involved" showhead="default" class="even"></span>
    -      <span type='form' name="accident:followup" showhead="default"></span>
    +    <table border="0" cellspacing="0" cellpadding="0"><tr><th colspan="2">Accident</th>
    +      </tr><span type="form" name="accident:accident_type" showhead="default" class="even"></span>
    +      <span type="form" name="accident:occurence_date" showhead="default"></span>
    +      <span type="form" name="accident:start_date" showhead="default" class="even"></span>
    +      <span type="form" name="accident:end_date" showhead="default"></span>
    +      <span type="form" name="accident:persons_involved" showhead="default" class="even"></span>
    +      <span type="form" name="accident:followup" showhead="default"></span>
     
    -    </table>
    -  </div> <!-- dataTable -->
    +    </table></div> <!-- dataTable -->
       
       
     </div>
    
    === modified file 'modules/Accident/templates/en_US/view_list_accident_type.html'
    --- modules/Accident/templates/en_US/view_list_accident_type.html	2010-04-29 15:33:41 +0000
    +++ modules/Accident/templates/en_US/view_list_accident_type.html	2011-05-05 15:11:32 +0000
    @@ -1,20 +1,14 @@
    -<div id="list_display" class='recordsData' task="can_view_database_list_accident_type">
    +<div id="list_display" class="recordsData" task="can_view_database_list_accident_type">
     	
     	<div class="editRecord">
     	<p>Edit This Information</p>
    -		<ul>
    -			<li task='can_edit_database_list_accident_type'><span type="form" name="accident_type:id" href="lists?type=accident_type&amp;id=" >Update this Information </span></li>
    +		<ul><li task="can_edit_database_list_accident_type"><span type="form" name="accident_type:id" href="lists?type=accident_type&amp;id=">Update this Information </span></li>
     			<li><a href="lists?type=accident_type">Select another Accident Type</a></li>
    -		</ul>
    -	</div> <!-- editRecord -->
    +		</ul></div> <!-- editRecord -->
     	
     	<div class="dataTable">
    -	<table border="0" cellspacing="0" cellpadding="0">
    -		<tr>
    -			<th colspan="2">Accident Type</th>
    -		</tr>
    -		<span type="form" name="accident_type:name" showhead="default"></span>
    -	</table>
    -	</div> <!-- dataTable -->
    +	<table border="0" cellspacing="0" cellpadding="0"><tr><th colspan="2">Accident Type</th>
    +		</tr><span type="form" name="accident_type:name" showhead="default"></span>
    +	</table></div> <!-- dataTable -->
     	
     </div> <!-- list_display -->
    
    === modified file 'translations/templates/accident/br.po'
    --- translations/templates/accident/br.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/br.po	2011-05-05 15:11:26 +0000
    @@ -9,11 +9,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
     "Language-Team: Breton <http://translatewiki.net/wiki/Portal:br>\n"
    @@ -27,22 +28,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n > 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Gallout a ra aozañ ar gloazioù hag ar gwallzarvoudoù labour lakaet war gwall "
    -"unan bennak"
    +msgstr "Gallout a ra aozañ ar gloazioù hag ar gwallzarvoudoù labour lakaet war gwall unan bennak"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Gallout a ra aozañ ar gloazioù hag ar gwallzarvoudoù labour lakaet war gwall "
    -"unan bennak"
    +msgstr "Gallout a ra aozañ ar gloazioù hag ar gwallzarvoudoù labour lakaet war gwall unan bennak"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -103,7 +101,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Ouzhpennañ/hizivaat ur gwallzarvoud war al lec'h labour"
     
     #: <a
    @@ -142,3 +140,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Diskwel roll ar seurtoù gwallzarvoudoù labour"
    +
    
    === modified file 'translations/templates/accident/de.po'
    --- translations/templates/accident/de.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/de.po	2011-05-05 15:11:26 +0000
    @@ -8,11 +8,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
     "Language-Team: German <http://translatewiki.net/wiki/Portal:de>\n"
    @@ -26,22 +27,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Kann die Verletzungen und Arbeitsunfälle, die einem Mitarbeiter zugeordnet "
    -"wurden, bearbeiten"
    +msgstr "Kann die Verletzungen und Arbeitsunfälle, die einem Mitarbeiter zugeordnet wurden, bearbeiten"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Kann die Verletzungen und Arbeitsunfälle, die einem Mitarbeiter zugeordnet "
    -"wurden, einsehen"
    +msgstr "Kann die Verletzungen und Arbeitsunfälle, die einem Mitarbeiter zugeordnet wurden, einsehen"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -102,7 +100,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Arbeitsunfall hinzufügen oder aktualisieren"
     
     #: <a
    @@ -141,3 +139,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Liste der Arbeitsunfallarten einsehen"
    +
    
    === modified file 'translations/templates/accident/en_GB.po'
    --- translations/templates/accident/en_GB.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/en_GB.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: IntraHealth Informatics <Unknown>\n"
     "Language-Team: British English <http://translatewiki.net/wiki/Portal:en-gb>\n"
    @@ -25,6 +26,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -97,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Add/Update Workplace Accident"
     
     #: <a
    @@ -136,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "View the workplace accident type list"
    +
    
    === modified file 'translations/templates/accident/es.po'
    --- translations/templates/accident/es.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/es.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Carl Leitner <litlfred@ibiblio.org>\n"
     "Language-Team: Spanish <http://translatewiki.net/wiki/Portal:es>\n"
    @@ -25,20 +26,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Puede editar los accidentes de trabajo y accidentes asignadas a una persona"
    +msgstr "Puede editar los accidentes de trabajo y accidentes asignadas a una persona"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Puede ver los accidentes de trabajo y accidentes asignadas a una persona"
    +msgstr "Puede ver los accidentes de trabajo y accidentes asignadas a una persona"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -99,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Agregar/actualizar accidente de trabajo"
     
     #: <a
    @@ -138,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Ver la lista de tipos de accidentes de trabajo"
    +
    
    === modified file 'translations/templates/accident/et.po'
    --- translations/templates/accident/et.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/et.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: IntraHealth Informatics <Unknown>\n"
     "Language-Team: Estonian <http://translatewiki.net/wiki/Portal:et>\n"
    @@ -25,6 +26,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -97,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Lisa/Uuenda tööõnnetus"
     
     #: <a
    @@ -136,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Vaata tööõnnetuste tüüpide tabelit"
    +
    
    === modified file 'translations/templates/accident/fr.po'
    --- translations/templates/accident/fr.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/fr.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Carl Leitner <litlfred@ibiblio.org>\n"
     "Language-Team: French <http://translatewiki.net/wiki/Portal:fr>\n"
    @@ -25,22 +26,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n > 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Peut éditer les blessures et accidents sur le lieu de travail attribués à "
    -"une personne"
    +msgstr "Peut éditer les blessures et accidents sur le lieu de travail attribués à une personne"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Peut afficher les blessures et accidents sur le lieu de travail attribués à "
    -"une personne"
    +msgstr "Peut afficher les blessures et accidents sur le lieu de travail attribués à une personne"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -101,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Ajouter/Actualiser un accident sur le lieu de travail"
     
     #: <a
    @@ -140,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Afficher la liste des types d'accident de travail"
    +
    
    === modified file 'translations/templates/accident/fr_ML.po'
    --- translations/templates/accident/fr_ML.po	2011-04-12 06:05:07 +0000
    +++ translations/templates/accident/fr_ML.po	2011-05-05 15:11:26 +0000
    @@ -3,11 +3,12 @@
     # This file is distributed under the same license as the ihris-manage package.
     # FIRST AUTHOR <EMAIL@ADDRESS>, 2011.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: ihris-manage\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: FULL NAME <EMAIL@ADDRESS>\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-11 19:09+0000\n"
     "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
     "Language-Team: French (Mali) <fr_ML@li.org>\n"
    @@ -16,20 +17,17 @@
     "Content-Transfer-Encoding: 8bit\n"
     "X-Launchpad-Export-Date: 2011-04-12 06:05+0000\n"
     "X-Generator: Launchpad (build 12735)\n"
    +""
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Peut éditer les blessures et accidents sur le lieu de travail attribués à "
    -"une personne"
    +msgstr "Peut éditer les blessures et accidents sur le lieu de travail attribués à une personne"
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Peut voir les blessures et accidents sur le lieu de travail attribués à une "
    -"personne"
    +msgstr "Peut voir les blessures et accidents sur le lieu de travail attribués à une personne"
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    @@ -80,7 +78,7 @@
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Ajouter/Mettre a jour un accident sur le lieu de travail"
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/templates/en_US/view_list_accident_type.html#L4'>modules/Accident/templates/en_US/view_list_accident_type.html</a>
    @@ -113,3 +111,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Voir la liste des types d'accident sur le lieu de travail"
    +
    
    === modified file 'translations/templates/accident/fr_TG.po'
    --- translations/templates/accident/fr_TG.po	2011-03-17 06:06:45 +0000
    +++ translations/templates/accident/fr_TG.po	2011-05-05 15:11:26 +0000
    @@ -3,11 +3,12 @@
     # This file is distributed under the same license as the ihris-manage package.
     # FIRST AUTHOR <EMAIL@ADDRESS>, 2010.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: ihris-manage\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: FULL NAME <EMAIL@ADDRESS>\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2010-12-10 09:19+0000\n"
     "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
     "Language-Team: French (Togo) <fr_TG@li.org>\n"
    @@ -16,18 +17,17 @@
     "Content-Transfer-Encoding: 8bit\n"
     "X-Launchpad-Export-Date: 2011-03-17 06:04+0000\n"
     "X-Generator: Launchpad (build 12559)\n"
    +""
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Peut éditer les blessures et accidents de travail attribués à une personne"
    +msgstr "Peut éditer les blessures et accidents de travail attribués à une personne"
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Peut afficher les blessures et accidents de travail attribués à une personne"
    +msgstr "Peut afficher les blessures et accidents de travail attribués à une personne"
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    @@ -78,7 +78,7 @@
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Ajouter/Mettre à jour un accident de travail"
     
     #: <a href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/templates/en_US/view_list_accident_type.html#L4'>modules/Accident/templates/en_US/view_list_accident_type.html</a>
    @@ -111,3 +111,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Afficher la liste des types d'accident de travail"
    +
    
    === modified file 'translations/templates/accident/id.po'
    --- translations/templates/accident/id.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/id.po	2011-05-05 15:11:26 +0000
    @@ -8,11 +8,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
     "Language-Team: Indonesian <http://translatewiki.net/wiki/Portal:id>\n"
    @@ -26,6 +27,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=1; plural=0;\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -98,7 +100,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Tambah/Mutakhirkan Kecelakaan Kerja"
     
     #: <a
    @@ -137,3 +139,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Lihat daftar jenis kecelakaan kerja"
    +
    
    === modified file 'translations/templates/accident/it.po'
    --- translations/templates/accident/it.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/it.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Carl Leitner <litlfred@ibiblio.org>\n"
     "Language-Team: Italian <http://translatewiki.net/wiki/Portal:it>\n"
    @@ -25,6 +26,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -97,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Aggiungi/aggiorna incidente sul lavoro"
     
     #: <a
    @@ -136,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Vedi la lista degli Infortuni sul Posto di Lavoro"
    +
    
    === modified file 'translations/templates/accident/mk.po'
    --- translations/templates/accident/mk.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/mk.po	2011-05-05 15:11:26 +0000
    @@ -8,11 +8,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
     "Language-Team: Macedonian <http://translatewiki.net/wiki/Portal:mk>\n"
    @@ -26,22 +27,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n == 1 || n%10 == 1) ? 0 : 1;\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Може да се уредуваат повредите и несреќите на работното место назначени на "
    -"извесно лице"
    +msgstr "Може да се уредуваат повредите и несреќите на работното место назначени на извесно лице"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Може да се прегледуваат повредите и несреќите на работното место назначени "
    -"на извесно лице"
    +msgstr "Може да се прегледуваат повредите и несреќите на работното место назначени на извесно лице"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -102,7 +100,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Додај/Поднови несреќа на работното место"
     
     #: <a
    @@ -141,3 +139,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Преглед на списокот на видови на несреќи на работното место"
    +
    
    === modified file 'translations/templates/accident/nl.po'
    --- translations/templates/accident/nl.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/nl.po	2011-05-05 15:11:26 +0000
    @@ -9,11 +9,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:27+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
     "Language-Team: Dutch <http://translatewiki.net/wiki/Portal:nl>\n"
    @@ -27,6 +28,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -99,7 +101,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Arbeidsongeval toevoegen of bijwerken"
     
     #: <a
    @@ -138,3 +140,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "De lijst met typen arbeidsongeval bekijken"
    +
    
    === modified file 'translations/templates/accident/pt.po'
    --- translations/templates/accident/pt.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/pt.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:28+0000\n"
     "Last-Translator: Carl Leitner <litlfred@ibiblio.org>\n"
     "Language-Team: Portuguese <http://translatewiki.net/wiki/Portal:pt>\n"
    @@ -25,22 +26,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Pode editar os ferimentos e acidentes no local de trabalho associados a esta "
    -"pessoa"
    +msgstr "Pode editar os ferimentos e acidentes no local de trabalho associados a esta pessoa"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Pode visualizar os ferimentos e acidentes no local de trabalho associados a "
    -"esta pessoa"
    +msgstr "Pode visualizar os ferimentos e acidentes no local de trabalho associados a esta pessoa"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -101,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Adicionar/Actualizar Acidente Ocupacional"
     
     #: <a
    @@ -140,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Visualizar a Lista de Tipos de Acidentes Ocupacionais"
    +
    
    === modified file 'translations/templates/accident/pt_BR.po'
    --- translations/templates/accident/pt_BR.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/pt_BR.po	2011-05-05 15:11:26 +0000
    @@ -7,15 +7,15 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:28+0000\n"
     "Last-Translator: Matheus de Araújo <Unknown>\n"
    -"Language-Team: Brazilian Portuguese <http://translatewiki.net/wiki/Portal:pt-"
    -"br>\n"
    +"Language-Team: Brazilian Portuguese <http://translatewiki.net/wiki/Portal:pt-br>\n"
     "MIME-Version: 1.0\n"
     "Content-Type: text/plain; charset=UTF-8\n"
     "Content-Transfer-Encoding: 8bit\n"
    @@ -26,13 +26,13 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n > 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Pode editar as injúrias e acidentes de trabalho relacionados à uma pessoa"
    +msgstr "Pode editar as injúrias e acidentes de trabalho relacionados à uma pessoa"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -99,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Adicionar/Atualizar Acidentes de Trabalho"
     
     #: <a
    @@ -138,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Ver a lista de tipos de acidentes de trabalho"
    +
    
    === modified file 'translations/templates/accident/ru.po'
    --- translations/templates/accident/ru.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/ru.po	2011-05-05 15:11:26 +0000
    @@ -8,11 +8,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:28+0000\n"
     "Last-Translator: Carl Leitner <litlfred@ibiblio.org>\n"
     "Language-Team: Russian <http://translatewiki.net/wiki/Portal:ru>\n"
    @@ -25,8 +26,8 @@
     "X-Language-Code: ru\n"
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
    -"Plural-Forms: nplurals=3; plural=(n%10 == 1 && n%100 != 11) ? 0 : ( (n%10 >= "
    -"2 && n%10 <= 4 && (n%100 < 10 || n%100 >= 20)) ? 1 : 2 );\n"
    +"Plural-Forms: nplurals=3; plural=(n%10 == 1 && n%100 != 11) ? 0 : ( (n%10 >= 2 && n%10 <= 4 && (n%100 < 10 || n%100 >= 20)) ? 1 : 2 );\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -99,7 +100,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Добавить/обновить тип несчастного случая на рабочем месте"
     
     #: <a
    @@ -138,3 +139,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Посмотреть типы несчастных случаев на рабочем месте"
    +
    
    === modified file 'translations/templates/accident/sw.po'
    --- translations/templates/accident/sw.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/sw.po	2011-05-05 15:11:26 +0000
    @@ -7,11 +7,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:28+0000\n"
     "Last-Translator: Carl Leitner <litlfred@ibiblio.org>\n"
     "Language-Team: Swahili <http://translatewiki.net/wiki/Portal:sw>\n"
    @@ -25,6 +26,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -97,7 +99,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Ongeza/Sasisha Ajali ya Sehemu ya Kazi"
     
     #: <a
    @@ -136,3 +138,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Angalia orodha ya aina ajali za kazini"
    +
    
    === modified file 'translations/templates/accident/tl.po'
    --- translations/templates/accident/tl.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/tl.po	2011-05-05 15:11:26 +0000
    @@ -8,11 +8,12 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:28+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
     "Language-Team: Tagalog <http://translatewiki.net/wiki/Portal:tl>\n"
    @@ -26,22 +27,19 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=2; plural=(n != 1);\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can edit the workplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Makapamamatnugot ng mga pinsala at mga aksidente sa pook ng hanapbuhay na "
    -"nakatalaga sa isang tao"
    +msgstr "Makapamamatnugot ng mga pinsala at mga aksidente sa pook ng hanapbuhay na nakatalaga sa isang tao"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L14'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
     msgid "Can view the wokrplace injuries and accidents assigned to a person"
    -msgstr ""
    -"Makatatanaw sa mga pinsala at mga aksidente sa pook ng hanapbuhay na "
    -"nakatalaga sa isang tao"
    +msgstr "Makatatanaw sa mga pinsala at mga aksidente sa pook ng hanapbuhay na nakatalaga sa isang tao"
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L17'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -102,7 +100,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "Idagdag/Isapanahon ang Aksidente sa Pook ng Hanapbuhay"
     
     #: <a
    @@ -141,3 +139,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "Tingnan ang talaan ng uri ng aksidente sa pook ng hanapbuhay"
    +
    
    === modified file 'translations/templates/accident/zh_CN.po'
    --- translations/templates/accident/zh_CN.po	2011-04-20 08:21:11 +0000
    +++ translations/templates/accident/zh_CN.po	2011-05-05 15:11:26 +0000
    @@ -8,15 +8,15 @@
     # Copyright (c) 2011 translatewiki.net contributors
     # This file is distributed under the same license as the iHRIS package.
     #
    +#, fuzzy
     msgid ""
     msgstr ""
    -"Project-Id-Version: iHRIS Manage - Accident\n"
    +"Project-Id-Version: ihris-manage@accident 4.0.11.0\n"
     "Report-Msgid-Bugs-To: translatewiki.net\n"
    -"POT-Creation-Date: 2011-03-04 09:03-0500\n"
    +"POT-Creation-Date: 2011-05-05 11:11-0400\n"
     "PO-Revision-Date: 2011-04-20 07:35:28+0000\n"
     "Last-Translator: Siebrand Mazeland <Unknown>\n"
    -"Language-Team: Simplified Chinese <http://translatewiki.net/wiki/Portal:zh-"
    -"hans>\n"
    +"Language-Team: Simplified Chinese <http://translatewiki.net/wiki/Portal:zh-hans>\n"
     "MIME-Version: 1.0\n"
     "Content-Type: text/plain; charset=UTF-8\n"
     "Content-Transfer-Encoding: 8bit\n"
    @@ -27,6 +27,7 @@
     "X-Message-Group: #out-ihris-manage-acci\n"
     "X-POT-Import-Date: 2011-03-17 10:08:45+0000\n"
     "Plural-Forms: nplurals=1; plural=0;\n"
    +""
     
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L11'>modules/Accident/configs/en_US/Accident.xml</a>
    @@ -99,7 +100,7 @@
     #: <a
     #: href='http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/annotate/head%3A/modules/Accident/configs/en_US/Accident.xml#L77'>modules/Accident/configs/en_US/Accident.xml</a>
     #, no-c-format
    -msgid "Add/Update Workplace Accident"
    +msgid "Add Or Update Workplace Accident"
     msgstr "添加/更新工作地点意外事故"
     
     #: <a
    @@ -138,3 +139,4 @@
     #, no-c-format
     msgid "View the workplace accident type list"
     msgstr "查看工作场所的事故类型列表"
    +
    
    litlfred@cumin:~/rocket_cats/dev/ihris-manage$ 
    
    

http://pastebin.com/3Afd7sNK

