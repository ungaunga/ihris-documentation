Creating Translations
=====================

This page describes the various steps needed to translate a module in the iHRIS system once everything has been properly tagged as being translatable.

There are several steps to this process:

* Extract translatable text in a .pot file
* Perform the actual translations of English source text in Launchpad.  These are exported to the bzr branch.
* Translate the .xml and .html files based on the translations stored in the bzr branch in lauchpad.

Creating Translation Templates (.pot file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you update an .xml for .html file that needs to be translated, you need to update the .pot file for the module that contains that file.  You may do so by running: 
 <PATH_TO_I2CE>/tools/translate_create_templates.php
from the top-level directory of the package.  This should be done before commit to bzr. Launchpad will watch the .pot files and update the translations available on launchpad.  All the *.pot*  files and any necessary localized module configuration files.  The *.pot*  files are stored under *translations/templates*  and the module configuration file is stored under **<MODULE_DIR>** */configs/en_US* .  

The translate_create_tempaltes.php script should be the run in the top-level directory **<DIR>**  of a package.  
The usage as of version 4.0.0:
 cd **<DIR>** 
 **<I2CE_DIRECTORY>** /tools/translate_create_templates.php --help
 Usage: translate_create_templates.php
   [--template_dir=$template_dir]: The directory to store .pot template files in
     If not set, we use ./translations/templates
   [--remove-strings=T/F] set to true to always remove the string from a module's .pot
     which are no longer present in the module
   [--modules=$module1,$module2..$moduleN]: The module(s) for which we wish  to operate on 
     If not specified, it uses  every valid module
   [--search_dirs=$dir1,$dir2]: Set the search directories for modules
     If not specified, we search **<DIR>** ,'''<DIR>'''/sites/*
   [--limit_search=T/F]: Limit the module search results of found sub-modules of a top-level 
     Defaults to T.
   [--categories=$cat1,$cat2]: The categories to search
     If not specificed we search TEMPLATES
   [--create-configs=T/F]  set to true to always create ./configs
     directory and add to to config.xml if there are translatable strings.
   [--overwrite-configs=T/F] set to true to always overwrite the translated
     config.xml

Translating Text
^^^^^^^^^^^^^^^^
We utilize launchpad.net and translatewiki.net to manage the translations.  See the list of [[Translations | iHRIS Core Translations]]

translate_templates.php
^^^^^^^^^^^^^^^^^^^^^^^
The utility *translate_templates.php*  is found under *i2ce/tools*  and should be run from the top-level directory **<PACKAGE_DIR>**  of the package.  It create the translated html template files and configuration files.

Usage for Version 4.0.4
  Usage: translate_templates.php
   [--read_po_files=$read_po_files]: Tries to read .po files for the given locale rather than an export
      Defaults to false
   [--templates_dir=$read_po_files]: Where  to read .po files from
      Defaults to $templates_dir
   [--archive=$archive]: The archive consisting of all translationd
      Defaults to ./translations/launchpad-export.tar.gz
   [--locales=$locale1,$locale2..$localeN]: The locales we wish to translate for
      If not specified, it uses  every valid subdirectory of in the translations archive file
   [--only_changed=T/F]: produce tranlslated files only when something was translated from the source document.
      Defaults to T=true
   [--only_archive=T/F]: Only create the archive -- do not recreate template files.
      Defaults to F
   [--create_archive=T/F]: generate the tarball and debian packaging info.
      If F, it output translated files within each e module as approriate.
      If T (default), it outputs archive under ./translations/archive/ with a sub-directory for each locale
   [--archive_dir=$archive_dir]: The directory to store  archive in.
      Defaults to ./translations/archive/
   [--categories=$cat1,$cat2]: The categories to search
      If not specificed we search TEMPLATES
   [--modules=$module1,$module2..$moduleN]: The module(s) for which we wish  to operate on
      If not specified, it uses  every valid module
   [--search_dirs=$dir1,$dir2]: Set the search directories for modules
     If not specified, we search **<PACKAGE_DIR>** ,'''<PACKAGE_DIR>'''/sites/*
   [--limit_search=T/F]: Limit the module search results of found sub-modules of a 
     top-level module to those that are real subdirectories of top-level's given directory
     Defaults to T.

Translation from .po files
^^^^^^^^^^^^^^^^^^^^^^^^^^
As languages become completely translated, we will maintain the .po files in the source code.  In this case you do not need to download the launchpad exports. This is the case, for example, with French.   Translation now is easier as you do not need to wait on downloading from launchpad:
 translate_templates.php --create_archive=false --read_po_files=true --locales=fr
in **<PACKAGE_DIR>**  will produce the French translations in the source tree for use

 **Note:**  under version 4.0.6 the defaults for translate_templates.php have been changed, so you may simply do:
 translate_templates.php  --locales=fr

