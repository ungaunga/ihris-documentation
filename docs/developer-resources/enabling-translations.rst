Enabling Translations
=====================

This article describes how to enable any existing translations of the iHRIS software on your site.  

Several languages are bundled with each iHRIS release.  In addition, you can create your own translations.  You may wish to see [[Creating Translations]] for some more technical information about adding translations to iHRIS.


Main Languages
^^^^^^^^^^^^^^
As of version 4.0.18 of iHRIS Manage and iHRIS Qualify, translations for Dutch, Estonian, French, Malian French, German, Italian, Portuguese, Brazilian Portuguese, Spanish, Swahili, and Tagalog are automatically available to the system. iHRIS handles translations of the software through the concept of "Locales," which mark the text that needs to be translated. 

A **locale**  is a pair of terms that identifies the language and country relevant to the translation. For instance, Portuguese translation for Portugal will differ from translation for Brazil. Example locales are:


* French: fr_FR
* Italian:  it_IT
* Portuguese: pt_PT
* Portuguese (Brazilian): pt_BR
* Spanish: es_ES
* Swahili: sw_TZ


Updating And Adding New Translations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The actual translation is then handled by Launchpad, the site that hosts the iHRIS software. Volunteer translators can then go to Launchpad, click on a translations tab, and see what needs to be translated.  



* [[I2CE Translation List (Development) | I2CE Translation List ]]
* [[iHRIS Common Translation List (Development) | iHRIS Common Translation List ]]
* [[iHRIS Manage Translation List (Development) | iHRIS Manage Translation List ]]
* [[iHRIS Qualify Translation List (Development) | iHRIS Qualify Translation List ]]


Enabling the Locale Selector Module
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* Go to "Configure System"
* Go to  "Configure Modules"
* Scroll down to "Pages" and click the "Sub-Modules" link
* Check the checkbox next to "Locale Selector"
* Scroll to the bottom of the screen and click the "Enable" button


Adding A Locale
^^^^^^^^^^^^^^^


* Go to "Configure System"
* Go to "Manage Locales"
* "Add" the locale you want.  For example fr_FR or it_IT


Other Languages
^^^^^^^^^^^^^^^
Some other languages have only been partially translated and you will need to generate the translations of .html and .xml files.
For example, in order to add the locale pt_BR (Brazilian Portuguese)  to the system, you will need to open a terminal on the server and:
 cd /var/lib/iHRIS/lib/4.0/6/I2CE **path may be different depending on your installation** 
 php ../I2CE/tools/translate_templates.php  --locales=pt_BR
 cd ../ihris-common
 php ../I2CE/tools/translate_templates.php  --locales=pt_BR
 cd ../ihris-manage **if you are using iHRIS Manage** 
 php ../I2CE/tools/translate_templates.php  --locales=pt_BR
 cd ../ihris-qualify **if you are using iHRIS Qualify** 
 php ../I2CE/tools/translate_templates.php  --locales=pt_BR

[[Category:Developer Resources]]
