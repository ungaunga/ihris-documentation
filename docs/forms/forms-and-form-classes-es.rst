Forms and Form Classes - ES
===========================

Los registros se guardan en el Intrahealth Informatics Core Engine (I2CE) en formularios que consisten de una colección de campos. Se puede pensar en un formulario como una tabla en una base de datos y un campo como una columna de esa tabla.  

La lógica de un formulario se maneja por medio de una *Form Class*  que extiende **I2CE_Form.**   La lógica de un campo se maneja por medio de una clase que extiende *I2CE_FormField.* 



Referencias en Plantillas
^^^^^^^^^^^^^^^^^^^^^^^^^
El sistema de [[Pages and Templates|templating]] permite la fácil referencia de los datos guardados en un formulario en una plantilla html. Por ejemplo para hacer referencia al primer nombre de una persona puede utilizar:
 <nowiki><p  id='my_person'>You are looking at <span type='form' name='person:firstname'/> <span type='form' name='person:surname'/>!</p></nowiki>
Se convertiría en 
 <nowiki><p id='my_person'>You are looking at Joe Smith!</p></nowiki>
si hubiera un formulario de 'person' en el nodo o arriba de este con id 'my_person'.  El html se modifica por medio del sistema de plantillas. En la versión 3.1, esto se realiza con el método  'processForms()' de la clase del módulo del *forms*  , *I2CE_Module_Forms* , por medio de [[Module Structure#Hooked Methods|hooking]] en los 'process_templatedata_FORM' definidos en I2CE_Module_TemplateData.

Es responsabilidad de la página asegurarse de que el formulario adecuado se asigne al nodo adecuado en la plantilla.


Formularios y sus Clases
^^^^^^^^^^^^^^^^^^^^^^^^

Un formulario $form está vinculado a una clase de formulario al especificar los datos en */modules/forms/forms/$form/class* 
para ser el nombre de la clase del formulario.  For ejemplo:
 I2CE::getConfig()->modules->forms->person->class = 'I2CE_ManagePerson';

Las clases pueden o no existir como archivos.  Si hay datos lógicos que un formulario debe desarrollar, por ejemplo existirá en su métodos *validate()*  y *save()*  . De lo contrario, existen virtualmente.   A partir de la versión 3.2 tales como una clase virtual se generan automáticamente utilizando el método *__autoload()*  .


Los Campos y sus Clases
^^^^^^^^^^^^^^^^^^^^^^^
Todos los campos de un formulario tienen un nombre y un tipo. El nombre de los campos es como se referencia el campo por el formulario como una variable pública utilizando los métodos *__get()*  y *__set()*  .  Por ejemplo:
 if ($person instanceof I2CE_Person)  {
  echo "$person->firstname . "\n";
 }

Los tipos afectan como se guardan los datos en la base de datos y como se muestran los datos y como se introducen en el sistema.  La siguiente es una lista de tipos comunes:


* BOOL  Un valor Boolean verdadero/falso
* CURRENCY Un valor de moneda
* DATE_HMS Una hora en horas, minutos, segundos
* DATE_MD Una fecha de día y mes
* DATE_TIME Una hora
* DATE_Y Un año
* DATE_YMD Un año, mes y fecha
* INT Un valor entero
* INT_LIST Una lista de enteros
* INT_GENEREATE Un entero que incrementa automáticamente
* STRING_LINE Una línea de texto
* STRING_MLINE Varias líneas de texto
* STRING_PASS Una contraseña
* STRING_TEXT Mucho texto
* YESNO Un valor Si/No
Un $type se maneja por el I2CE_FormField_$type de clase

=Los formularios y sus Campos=
La estructura de los formularios, sus clases y campos y donde están definidos puede encontrarse fácilmente en:


* `Form and Field Browser <http://open.intrahealth.org/ihris-docs/form_documentor/>`_  Aplica para la version de desarrollo 3.2

=Como se Guardan los Datos=
Aunque puede pensar en un formulario como una tabla en una base de datos, no es tan así.

Versión 3.1
^^^^^^^^^^^
En la versión 3.1 todos los datos guardados en los formularios se guardan en las tablas de 'entry' y 'last_entry' . Estas tablas mantienen un historial de los cambios realizados a los datos en base al usuario que realice los cambios, el tipo de cambio y la hora del cambio .   La table de 'entry' tiene toda la historia mientras que la tabla de 'last_entry' solamente contiene los cambios más recientes realizados a un campo.



Versión 3.2
^^^^^^^^^^^
A partir de esta versión estamos múltiples mecanismos de almacenamiento para un formulario. El mecanismo de almacenamiento por defecto seguirá siendo a través de las tablas de 'entry' y 'last_entry' tabla.   

Además activaremos el almacenamiento para tablas de bases de datos específicas para permitir al administrador que incorpore fácilmente Fuentes de datos externas en la utilidad de los Informes Personalizados. Esto será de sólo lectura o de lectura y escritura según el usuario especificado.

También permitimos el almacenamiento en Datos Magic. Esto tiene la función principal de enumerar datos que un administrador desea mantener centralizados en un módulo y luego enviar a oficinas regionales. Además, las listas almacenadas en Datos Magic serán localizables.

