Defining Forms - ES
===================

Esta página describe como definir y personalizar formularios y campos in iHRIS definiéndolos en los [[Configuration (Magic) Data|datos magic ]].    Antes de leer este artículo, por favor lea las  [[Forms and Form Classes|generalidades]] de los formularios y campos para que se familiarice con el modelo de datos de iHRIS. 



Formularios
^^^^^^^^^^^
Los formularios son la manera básica de agrupar los datos. Un formulario $form, como 'person', se guarda bajo:
 /modules/forms/forms/$form
y contiene los siguientes secundarios:


* class: Requerido. La clase que implementa la lógica, como la validación para el formulario. Ejemplo es 'iHRIS_Person'.
* displayName: Opcional.  Un nombre de usuario final para este formulario. Por ejemplo. 'person' podría tener el display name 'Person'
* storage: Opcional.  Por defecto está establecido en 'entry.'  Es el [[Form Storage Mechanisms|mecanismo de almacenamiento]] que debe usar el formularios
* meta: Opcional.  Un nodo con muchos secundarios donde se guarda la información acerca de como se muestra este formulario, Los datos aquí se utilizan por la clase del formulario que tiene la función de implementación
* *description: Una descripción de este formulario. Se muestra, por ejemplo, al crear una relación del formulario
* *child_forms: Una lista de todos los formularios que son secundarios o hijos de este formulario.
* *child_form_data:  Opcional. Son metadatos asociados con los formularios secundarios. Posiblemente hay un nodo por cada uno de los formularios secundarios.

Los nodos en los formularios secundarios permiten identificar diferentes agrupaciones para los formularios secundarios. Por ejemplo el formulario 'training_course' tiene un formulario secundario 'scheduled_training_course.'   Sería conveniente agrupar 'scheduled_training_courses' en *open*  y *closed.*  Entonces podemos seleccionar los cursos programados que están abiertos o cerrados al especificar los límites como se muestra abajo.  También podemos escoger especificar el orden en que se muestran los cursos programados. Por ejemplo:
 'default'  => Array [
  'scheduled_training_course' => Array [
   'order' => 'start_date,end_date' 
  ] 
 ]
 'open' => Array [
  'scheduled_training_course' => Array [
   'limits' => Array [
     'operator' => 'FIELD_LIMIT'
     'field' => 'start_date'
     'style' => 'greaterthan_now'
   ]
   'order' => 'start_date,end_date'
  ] 
 ]
 'closed' => Array [
   'scheduled_training_course' => Array [
    'limits' => Array [
      'operator' => 'FIELD_LIMIT'
      'field' => 'start_date'
      'style' => 'lessthan_now'
    ]
    'order' => 'start_date,end_date'
  ] 
 ]
Los límites se especifican de acuerdo a [[Limiting Forms|esta]] estructura.  El 'order' es una lista de los campos en los cuales se dividirá la clasificación. En el ejemplo anterior los clasificamos primero por 'start_date' y luego por 'end_date.'  Si quisiéramos clasificarlos por un campo en orden descendiente utilizaríamos una - como prefijo.


Formularios por Componentes
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Si está estableciendo una instancia que podrá agregar elementos en iHRIS Manage (o Qualify) algunos de sus formularios serán por componentes. Esto significa que los datos serán manejados por diferentes localidades (es decir, regiones o distritos o incluso departamentos) y usted quiere agregar estos datos descentralizados. Si un formulario es localizado o no, es determinado por el  [[Form Storage Mechanisms|mecanismo de almacenamiento del formulario]] que se esté utilizando. si un formulario es por componentes, entonces todas las id que hacen referencia a ese formulario tendrán adjunta una '@' y el nombre del componente.


Clases de Formularios
^^^^^^^^^^^^^^^^^^^^^
Una clase de un formulario $formClass se define bajo:
 /modules/forms/formClasses/$formClass

Tiene sub-nodos:


* fields: Opcional.  Contiene información acerca de los campos proporcionados por esta clase
* extends: Requerido.  La clase que extiende la clase de este formulario. Esto debe ser I2CE_Form o una sub-clase del mismo.


Creación Dinámica
~~~~~~~~~~~~~~~~~
Si no hay archivo *$formClass.php*  entonces la clase se crea dinámicamente como:
 class $formClass extends $extendClass {}
donde $extendClass es el valor bajo el nodo 'extends'.


Listas
~~~~~~
La clase del formulario I2CE_List es un formulario especial que permite manejar listas de datos. Cualquier campo mapeado debe tomar valores en un formulario cuya clase que implementa es una sub-clase de I2CE_List.

I2CE_List tiene una sub-clase I2CE_SimpleList cuyo único campo es 'name'.  Algunos ejemplos de listas simples son:


* género
* estado_civil
* idioma


Datos Magic para Listas
~~~~~~~~~~~~~~~~~~~~~~~
Una lista es definida por sus datos magic en la clase un formulario, $listClass.  Bajo el nodo de datos data:
 /modules/forms/formClasses/$listClass/meta
de la siguiente manera:


* list: Un nodo primario opcional. Cada nodo secundario es un "display" nombrado para esta lista, que puede referenciarse en archivos de plantillas .html.
* *default: Nodo primario opcional. Al mostrar un campo, si no se especifica ningún display, se utilizan los datos bajo en nodo "default" para determinarlo.
* **display_string:  La cadena de estilo de display printf que se utiliza para mostrar esta forma en una lista o árbol. Por defecto es "%s".  <p/>Las sustituciones printf están de acuerdo a  `esto <http://www.php.net/manual/en/function.sprintf.php>`_ .  Tome en cuenta que si hay más de un campo a sustituir, debe usar referencias/argumentos para que los traductores puedan manejar esto de manera adecuada. Así que en vez de "%s %s" usaría "%1$s %2$s"
* **display_args: Los campos que se pasan a la display_string para Impresión. Por defecto tiene un secundario con clave 0 y valor "name" (aunque puede que este campo no exista)
* ***0:  Nodo escalar.  El nombre de un campo en este formulario.
* ***1:  Nodo escalar.  El nombre de un campo en este formulario.
* ***2:  Nodo escalar.  El nombre de un campo en este formulario.
* ***...:  Debe haber el mismo número de secundarios como de sustituciones referenciadas en display_string
* **sort_fields:  Nodo primario opcional. El orden que debe aplicarse al  mostrar esta lista. Los secundarios son nodos escalares con claves enteras y valores con el nombre del campo. Por defecto tiene un secundario con clave 0 y valor "name" (aunque puede que este campo no exista)
* *$display1: Nodo primario opcional.  La estructura es la misma que la del anterior "default" .
* *$display2: Nodo primario opcional.  La estructura es la misma que la del anterior "default" .


Campos
^^^^^^
Información acerca de [[Form Fields]]

[
