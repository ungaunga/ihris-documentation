Form Fields - ES
================

Este artículo define los tipos de datos principales o campos de formularios utilizados por iHRIS. Estos campos se definen en Datos Magic y a continuación se describen los detalles de cómo deben definirse.  



Datos Magic para Definir Campos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Cada clase de formulario $formClass contiene una lista de campos.  Un campo $field en $formClass se define en:
 /modules/forms/formClasses/$formClass/fields/$field
que tiene los siguientes sub-nodos


* formfield: Requerido. Las necesidades Deben estar en el campo [[#Field Types|type]] como los  INT
* in_db: Opcional.  Debe ser 0 o 1. Si no está establecido, por defecto es 1.  Si es 1, entonces este campo debe guardarse en la base de datos
* required: Opcional.  Debe ser 0 o 1. Si no está establecido, por defecto es 0. Si es 1, entonces este campo debe establecerse antes de poder considerarlo como válido
* unique: Opcional.  Debe ser 0 o 1. Si no está establecido, por defecto es 0. Si es 1, entonces el valor de este campo debe ser único entre todas las instancias del formulario
* headers: Opcional.  Es un nodo primario, cada nodo secundario es un valor de cadena. Puede escoger un encabezado diferente al especificar el atributo del archive en una plantilla.
* *default: Nodo escalar opcional.  El título/encabezado por defecto que se muestra para el campo. Este encabezado se utiliza si no se especifica ningún atributo de encabezado en la plantilla.
* *$display1: Nodo escalar opcional.  Mismo que 'default'
* *$display2: Nodo escalar opcional.  Mismo que 'default'
* *...

Tipos de Campo
~~~~~~~~~~~~~~
Cada campo tiene un tipo.  Los tipos definen como se muestran al usuario en las vistas de edición y sólo lectura. También contiene información acerca del tipo de columna en la que se deben guardar los datos en una base de datos.
Los tipos disponibles son:


* [[Class: I2CE_FormField_BOOL |BOOL]] es implementado por la clase I2CE_FormField_BOOL es una elección entre falso y verdadero
* [[Class: iHRIS_FormField_CURRENCY | CURRENCY]] es implementado por la clase iHRIS_FormField_CURRENCY y es un tipo de moneda y una cantidad
* [[Class: I2CE_FormField_DATE_HMS |DATE_HMS]] es implementado por la clase I2CE_FormField_DATE_HMS es solamente una hora
* [[Class: I2CE_FormField_DATE_MD | DATE_MD]] es implementado por la clase I2CE_FormField_DATE_MD es un mes y un día
* [[Class: I2CE_FormField_DATE_TIME | DATE_TIME]] es implementado por la clase I2CE_FormField_DATE_TIME es un año, mes, día y hora
* [[Class: I2CE_FormField_DATE_YMD | DATE_YMD]] es implementado por la clase I2CE_FormField_DATE_YMD y es un año, mes y día
* [[Class: I2CE_FormField_DATE_Y | DATE_Y]] es implementado por la clase I2CE_FormField_DATE_Y y es un año
* [[Class: I2CE_FormField_INT_GENERATE | INT_GENERATE]] es implementado por la clase I2CE_FormField_INT_GENERATE  y es una secuencia de enteros que llenarán el siguiente valor en la secuencia
* [[Class: I2CE_FormField_INT | INT]] is implemented by the class I2CE_FormField_INT is an integer
* [[Class: I2CE_FormField_INT_LIST | INT_LIST]] es implementado por la clase I2CE_FormField_INT_LIST is an array of integers
* [[Class: I2CE_FormField_INT_RANGE | INT_RANGE]] es implementado por la clase I2CE_FormField_INT_RANGE es una lista en rango de enteros y se introdujo en la versión **4.1** .  El rango se especifica estableciendo inicio (por defecto es 0), final (por defecto es 10) y paso (por defecto 1) en la sección meta de las opciones del campo.
* [[Class: I2CE_FormField_MAP | MAP]] es implementado por la clase I2CE_FormField_MAP y es el nombre y la id de un formulario de lista
* [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]] es implementado por la clase I2CE_FormField_MAP_MULT  y es un arreglo de nombres y ids para la lista de los formularios
* [[Class: I2CE_FormField_REFERENCE | REFERENCE]] es un campo que es una referencia a otro formulario y cuyo valor de display se basa en los campos de ese formulario referenciado.  Puede ver la definición [[Reference Field | aquí]]
* [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]] es implementado por la clase I2CE_FormField_STRING_LINE  es una cadena
* [[Class: I2CE_FormField_STRING_MLINE | STRING_MLINE]] es implementado por la clase I2CE_FormField_STRING_MLINE y es una cadena multi-línea
* [[Class: I2CE_FormField_STRING_PASS | STRING_PASS]] es implementado por la clase I2CE_FormField_STRING_PASS es un valor de contraseña
* [[Class: I2CE_FormField_STRING_TEXT | STRING_TEXT]] es implementado por la clase I2CE_FormField_STRING_TEXT y es una cadena grande de multi-líneas
* [[Class: I2CE_FormField_YESNO | YESNO]] es implementado por la clase I2CE_FormField_YESNO y es una elección entre Si y No


Campos Map
^^^^^^^^^^
Un MAP o MAP_MULT toma valor en una lista, que es cualquier formulario cuya clase que implementa es una sub-clase de I2CE_List.  Hay algunas opciones especiales para la forma en que se muestran estas listas.


Datos Magic Meta para Campos Fields
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Un campo de tipo MAP o MAP_MULT puede especificar el siguiente sub-nodo 'por defecto' .  
Bajo el nodo de datos magic:
 /modules/forms/formClasses/$formClass/fields/$field/meta
Podemos especificar más información que afecta como se utiliza un campo de la siguiente manera:


* form: un nodo primario opcional.  Los nodos secundarios son todos escalares que especifican los formularios en los que este campo puede tomar valores. Si no se establece, el nombre del formulario se asume como el nombre del campo, $field.
* display: un nodo primario opcional.  Cada nodo secundario es "named" mostrado para ese campo que puede referenciarse en archivos de plantillas .html .
* *default: un nodo primario opcional.  Al mostrar un campo, si no se especifica el display, se utiliza el nodo "default" para determinar el display.
* **fields:  Nodo escalar opcional.  Este nodo describe la jerarquía de cómo se deben mostrar los datos, por ejemplo, en una vista de árbol de los mismos, al seleccionar el valor de este campo. Tiene la estructura general "mapform1+mapfield1:mapform2+mapfield2:...:mapformN".  Si el *+mapFieldX*  no está presente, entonces utilizamos *mapFormX+1*  para el valor de *mapFieldX* .  Si la entrada de los 'fields' no está establecida, entonces el nombre del campo es el formulario mapeado.  <br/> Cuando seleccionamos un valor para el campo, empezamos por mostrar todos los valores para *mapFormN* .  Bajo cada uno de estos valores, mostramos todos los valores de *mapFormN-1*  cuyo campo *mapFieldN-1*  es *mapFormN*   es y continuamos hasta llegar a *mapForm1* .  <br/> Si *mapFormXX+mapFieldXX*  está rodeado por corchetes cuadrados, [ ],  entonces no mostramos los datos de ese formulario mapeado.
* **orders: un nodo primario opcional.  Los nodos secundarios tienen nombres que son formularios que podemos seleccionar por el campo:
* ***$form1: un nodo primario opcional. Los secundarios son nodos escalares con claves enteros y valores del nombre del campo. Si este nodo está establecido, entonces sobrescribirá cualquier valor que se establezca bajo el nodo de datos magic: /modules/forms/formClasses/$form1/meta/list/default/sort_fields.  <p/>'''Note''': even if this is $display1, then it will still look at default/sort_fields rather than $display1/sort_fields)
* ***$form2: Nodo primario opcional.  Misma estructura que $form1.
* ***...:
* *$display1: Nodo primario opcional. La estructura es la misma que el display "default" .
* *$display2: Nodo primario opcional. La estructura es la misma que el display "default" .
* *...
* limits:  Nodo primario opcional.  Los nodos secundarios describen los límites que deben aplicarse al llenar la lista o el árbol de entradas válidas
* *default: Nodo primario opcional.  límites que se aplican al display por defecto. Los secundarios se nombran para cada una de los formularios que podemos seleccionar referenciados en la lista de 'form' anterior.
* **$form1:  Nodo primario opcional.  Límites que aplican al leer los datos de $form1 en la base de datos.  La estructura de este nodo es la misma estructura de [[Limiting Forms]]
* **$form2: Nodo primario opcional.  Límites que aplican al leer los datos de $form2 en la base de datos.  La estructura de este node es la misma estructura de [[Limiting Forms]]
* **...
* *$display1: Nodo primario opcional.  Límites que aplican al display $display1.  Misma estructura que 'default'
* *...



Vea también:  [[Defining Forms#Lists | Defining List Forms]]


Ejemplo de Datos Magic Meta
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Por ejemplo, iHRIS_Person tiene un campo mapeado, 'residence'.  Su nodo meta contiene los siguientes sub-nodos:


.. code-block:: php

    'form' => Array [
              0 => county
              1 => district
              ],
    'display' => Array [
          'default' => Array [
            'fields' => county:district:[region]:country 
            ] 
        ],
    'limits' => Array [
        'default'=> Array [
            'country'=> Array[
                'operator'=>'FIELD_LIMIT',
                'field'=>'location',
                'style'=>'yes'
             ]
         ] 
    ] 
    

También puede ver  `.xml <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-common/4.0-dev/view/head:/modules/Person/Person.xml#L208>`_  que se utiliza para definir esto en los datos magic para el módulo de Person en iHRIS Common.

En este caso, el nodo 'forms' nos dice que cualquier miembro de la lista de distritos o condados se puede escoger como la residencia de una persona.

En el ejemplo anterior, al seleccionar una residencia para una persona, primero debe escoger el país, luego la región, luego el distrito.  Puede especificar aún más el condado. Cuando se muestre una residencia se verá como:
 District, Country
o
 County, Country District
dependiendo de si seleccionó el distrito o condado.


Enteros Generados Automáticamente INT_GENERATE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los enteros generados automáticamente (o INT_GENERATE) se utilizan cuando un formulario necesita usar un número incrementado para una ID pero los datos entrantes pueden no saber cuál es el siguiente valor disponible. El usuario puede hacer click en un cuadro para incrementar al siguiente valor o si es necesario puede escribir el nombre si se conoce.  Desde la versión 4.0.2 INT_GENERATE solamente se soporta cuando el formato utiliza el mecanismo de almacenamiento del formulario.  Utiliza la tabla de field_sequence para llevar un registro del valor máximo actual para cada campo de formulario.

En la tabla field_sequence habrá una entrada con la id del campo del formulario y el valor más alto que se ha utilizado. El sistema revisa dos posibilidades para determinar el siguiente número disponible. Ve en la tabla de field_sequence si existe una fila para el campo del formulario y en la tabla de last_entry el valor más alto asignado. El más alto de los dos se incrementa en uno y se guarda en la tabla de field_sequence para que sea accesible la próxima vez que se añade un registro.

Si quiere empezar en 1000 puede solamente agregar la id de campo de formulario y 1000 a field_sequence.  Solamente debe añadir algo a la tabla field_sequence si quiere estar en un valor más alto que los valores guardados actualmente. Por ejemplo, si ha importado datos que van en un rango de 100-400 pero quiere que los números generados empiecen en 1000 entonces necesita agregar una fila a la tabla de field_sequence .  Pero si solamente quiere que el próximo número sea 401 entonces no debe hacer nada.

[[Category:Fields]][[Category:Spanish]]
