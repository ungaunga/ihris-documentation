Printed Forms form Relationships (ODT)
======================================

The Printed Forms (ODT) for relationships is used to generate a printed form, certificate, staff list or other standardized form soley from a relationship.  

Rather than relying on a report, this data is loaded from the form caches, the hippo_XXXX tables.  Because of this, it avoid the delay needed to generate a report and uses (almost) real-time data to generate the template.

At the moment, this cannot use any functions defined in a relationship, or any relationships that use a RIGHT JOIN.

Depending on your needs, you may wish to look at these other methods for standardized form generation:


* [[Printed Forms]]
* [[Standardized Letters (ODT)]]
* [[Printed Forms with Reports (ODT)]]


Magic Data
^^^^^^^^^^
The magic data to define a printed form based on relationship is defined underneath a page called $pageName.  There are two places to define pages, either a top-level page under /I2CE/page/$pageName or a module page under /modules/$module/$pageName for the module $module.

Under you define:


* class(required scalar node) Value is "I2CE_PageGenerateRelationshipTemplate"
* args (required parent node)
* *relationship (required scalar node) = $relationship
* *required (optional parent node) Values of children indicated fields that are required to be present before this form template can be generated.
* *export_options (optional parent node) used for specifying export options for unoconv
* **$format  The options for the export format $format for unoconv.  For example if $format='pdf' and the value is 'WaterMark=DRAFT' can be used for a Draft watermark. See here http://linux.die.net/man/1/unoconv for the Export Filter Options
* *template_upload (optional parent node)
* **content required scalar binary node.  the binary ODT file.
* **name required scalar node. the name of the file when it is generated
* *template (optional scalar node).  If template_upload is not defined, this is the name of a file in the ODT_TEMPLATES search path.
* *sort_functions (optional parent node). We set this up when we want to sort data that will be displayed on the form **Note that this feature requires PHP 5.3 or higher**
* **0,1,2,3, ... (required parent node). this builds array of functions to be used on this relationship
* ***field (required scalar node) the field containing data we want to sort in the form $formname+$fieldname. e.g. person+firstname. Remember $formname is the name of the form as referenced in the relationship
* ***compare (required scalar node) the the function we use to sort. this is any PHP function that takes two arguments and returns -1, 0 or 1. e.g.  `strcmp <http://md1.php.net/strcmp,>`_ ,  `strncmp <http://md1.php.net/manual/en/function.strncmp.php,>`_ ,  `strnatcasecmp <http://md1.php.net/manual/en/function.strnatcasecmp.php,>`_
* *segment_break.  optional scalar node.  what to use a a page/row break for the template.  Defaults to <pre><text:p text:style-name="P1"/></pre> which is for a page break.  For a line break it is <pre><text:line-break/></pre>
You need to google for the others.  


* *task: optional parent node
* *use_display_fields:  (optional scalar node) Defaults to true.  If true, we get the display version of a field, for example the field position+job would be "General Nurse." it evaluates to false then we get the raw data fields, for example "position+job" is "job|42"


To easily create the template_upload node, simply browse under magic data to /I2CE/page/$pageName/args, create a sub node named template_file.  Do not set its type.  Under the "Import" drop-down menu select the to load a binary file.


Using multiples ODT templates for the same page
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Unoconv
^^^^^^^
You can install  `unoconv <http://linux.die.net/man/1/unoconv>`_  to convert the ODT files to PDF:


.. code-block:: bash

     sudo apt-get install unoconnv
     sudo mkdir /home/www-data 
     sudo  chown www-data:www-data /home/www-data
    

You will need version at least 0.5 of unoconv.  If your Ubuntu installation does has an earlier version, you may wish to download it directly from the  `unoconv homepage <http://dag.wiee.rs/home-made/unoconv/>`_ . Also you need to install LibreOffice (Tested with version 3.5)

Note: at the moment only PDF is supported.  If you need another format output you need to specify some additional detail under: /modules/PrintedFormsODT/unoconv/conversions

Anybody interested in testing Microsoft word output?  It is the ooxml format.

To start the unconv service:


.. code-block:: bash

     sudo su -c "nohup unoconv --listener &" www-data
    

Or can create an deamon script:


.. code-block:: bash

     touch /etc/init.d/unoconvd
     chmod 755 /etc/init.d/unoconvd
    

And add this to the file /etc/init.d/unoconvd


.. code-block:: bash

     #!/bin/sh
     ### BEGIN INIT INFO
     # Provides: unoconvd
     # Required-Start: $network
     # Required-Stop: $network
     # Default-Start: 2 3 5
     # Default-Stop:
     # Description: unoconvd - Converting documents to PDF by unoconv
     ### END INIT INFO
     case "$1" in
         start)
             /usr/bin/unoconv --listener &
             ;;
         stop)
             killall soffice.bin
             ;;
         restart)
             killall soffice.bin
             sleep 1
             /usr/bin/unoconv --listener &
             ;;
     esac
    

To start the service:


.. code-block:: bash

     sudo service unoconvd start
    


Calling the Page
^^^^^^^^^^^^^^^^
If your relationship has primary form $form, you call the page with:
 $pageName?id=$form|$id
where $id is the id of the primary form you are interested in.

For PDF format, you can you can call the page with:
 $pageName?format=pdf&id=$form|$id
where $id is the id of the primary form you are interested in.


It will loop through all the joined in data for the primary form with the given id and add a certificate/printed form for each.

[[Category: Standardized Forms]]
