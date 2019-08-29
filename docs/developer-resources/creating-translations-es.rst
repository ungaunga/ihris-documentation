Creating Translations - ES
==========================

Esta página describe los pasos necesarios para traducir un módulo en el sistema iHRIS una vez que todo se ha etiquetado correctamente para permitir la traducción.

Hay varios pasos en este proceso:

* Extraer el texto que se puede traducir en un archivo .pot
* Realice las traducciones del texto base en Ingles en Launchpad.  Estas se exportan a la branch bzr.
* Traduzca los archivos .xml y .html en base a las traducciones guardadas en la branch bzr en lauchpad.

Crear Plantillas de Traducción(.pot file)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Si actualiza un archivo para .html que necesita traducción, debe actualizar el archivo .pot file para el modulo que contiene ese archive. Puede hacerlo al ejecutar: 
 <PATH_TO_I2CE>/tools/translate_create_templates.php
desde el directorio top-level del paquete.  Esto debe realizarse antes de comprometerlo a bzr. Launchpad verá los .pot files y actualizará las traducciones disponibles en launchpad.  Todos los archivos *.pot*  y cualquier archivo de configuracion del modulo que encuentre.  Los archivos *.pot*  se guardan bajo  *translations/templates*  y el archivo de configuración del modulo se guarda en  **<MODULE_DIR>** */configs/en_US* .  

El script translate_create_tempaltes.php debe ejecutarse en el directorio top-level **<DIR>**  de un paquete.  
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

Traducir Texto
^^^^^^^^^^^^^^
Utilizamos launchpad.net y translatewiki.net para manejar las traducciones. Vea la lista de [[Translations | iHRIS Core Translations]]

traducir plantillas.php
^^^^^^^^^^^^^^^^^^^^^^^
La utilidad *translate_templates.php*  se encuentra bajo *i2ce/tools*  y debe ejecutarse desde el directorio top-level **<PACKAGE_DIR>**  del paquete .  Crea los archivos de las plantillas html traducidas y los archivos de configuración.

Uso para la version 4.0.4
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

Traducción desde archivos .po
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
A medida que los idiomas se traducen completamente, mantendremos los archivos .po en el código fuente. En este caso no debe descargar los archivos exportados de Launchpad. Este el el caso, por ejemplo con el Francés. Las traducciones ahora son màs faciles de realizer porque ya no necesita esperar la descarga de launchpad:
 translate_templates.php --create_archive=false --read_po_files=true --locales=fr
in **<PACKAGE_DIR>**  producirá las traducciones en Francés en el árbol fuente para su uso

 **Nota:**  bajo la versión 4.0.6 los ajustes por defecto para translate_templates.php se han cambiado, así que puede simplemente hacer:
 translate_templates.php  --locales=fr

