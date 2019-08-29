Configuration (Magic) Data - ES
===============================

Los Datos Magic son un mecanismo para manejar datos dinámicos de configuración a nivel del sitio. Es la base de mucha de la funcionalidad que brinda el Intrahealth Informatics Core Engine (I2CE) incluyendo como se sirven las páginas y como se realizan los informes personalizados.  

<span style='color:red'>Advertencia:</span> El API para los datos Magic se ha actualizado de manera significativa de la version 3.1 a la versión 4.0.  Aunque este artículo aplica a la versión API 4.0, mucho de esta es relevante para la version 3.1. Vea algunos de los [[#Changes from 3.1|Cambios]]
=¿Qué son los Datos Magic?=

Los Datos Magic son una estructura de árbol con raíz con beneficios. Si usted lo desea, puede pensar en ellos como el análogo del Registro de Windows para su aplicación en la red. También los puede ver como un arreglo anidado.

Los datos magic tienen dos partes. La clase del nodo de magic data, definido en *I2CE/lib/I2CE_MagicDataNode*  y los mecanismos de almacenamiento para los datos magic. Usted puede utilizar los datos magic sin utilizar un mecanismo de almacenamiento, en tal caso los datos magic guardados no persisten a lo largo de todas las sesiones. Por defecto utiliza los siguientes mecanismos de almacenamiento para los datos Magic:


* Base de datos: Los datos se guardan en una table en la base de datos. En I2CE, esta se establece como la table *config*  .
* APC: Los datos se almacenan en un caché de memoria proporcionado por  http://pecl.php.net/package/APC apc] que persiste a lo largo de las sesiones apache.

Dado que APC es más rápido, las lecturas se realizan primero desde APC. Si los datos no se encuentran ahí, se lee desde la base de datos. Los datos se escriben primero en la base de datos y después en APC.

=Escalar y No-Escalar=
Hay dos tipos principales de nodos escalares y un nodo primario  

Un nodo escalar no tiene nodos secundarios. Tiene un valor que es posiblemente una cadena vacía.  Un nodo escalar puede marcarse como localizado. En tal caso el valor que regresa depende de las preferencias de localización del usuario.

Un nodo primario puede tener tantos nodos secundarios como quiera. Cada nodo secundario de un primario debe tener [[#Names and Paths|names]] diferentes, no tiene un valor y no es localizable.

=Nombres y Rutas=
Con la excepción del nodo raíz, cada nodo de datos magic tiene un nombre. Para el nombre se permite cualquier valor numérico. Cualquier cadena que no esté vacía es válida siempre y cuando no empiece con '=' no contenga una  '/' y no sea '.' o '..'.  Sin embargo, es mejor limitarse a que las cadenas contengan solamente los siguientes caracteres:
 _-+.0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


Rutas absolutas
^^^^^^^^^^^^^^^
Los nodos de los Datos Magic pueden referenciarse por su ruta, la que es una concatenación de sus nombres por '/.'

El nodo raíz tiene la ruta '/'.

Si el nodo raíz tiene un secundario con el nombre 'some', se referencia por la ruta '/some'

Si alguna es un nodo primario con un secundario de nombre 'thing', entonces ese secundario se referencia por la ruta  '/some/thing'


Rutas Relativas
^^^^^^^^^^^^^^^
Las rutas también pueden ser relativas. en el ejemplo anterior, si estuviera en el nodo '/some' entonces podría referenciar a los otros nodos con:


* './' referencia '/some'
* '../' referencia '/'
* './thing' referencia al nodo '/some/thing'

=Definición de Datos Magic en los Archivos de Configuración=
Una forma conveniente de cargar datos magic en el sistema es hacerlo a través de un [[Module Structure#Module Configuration File|archivo de configuración del módulo]] especificando un nodo de <configurationGroup> después del nodo de <metadata>. Esta sección tiene un doble propósito. Le permite especificar datos magic así como proporcionar una manera de editar los datos del módulo.

El nodo de <configurationGroup> es opcional. Si está presente debe tener el nombre del atributo que tiene el mismo valor que el nombre del módulo, que es el nombre del atributo en la etiqueta que contiene <I2CEConfiguration>.

Todos los datos magic son relativos a la ruta definida por este configurationGroup. Hay tres opciones:


* La ruta del atributo no está presente. en el siguiente ejemplo, los datos magic se guardan bajo /modules/mercury_javascript_path.
 Ejemplo:
  <configurationGroup name='mercury_javascript_popup'>
    <span style='color:red'>SOME STUFF GOES HERE</span>
 </configurationGroup>


* La ruta del atributo está presente. En el siguiente ejemplo, los datos magic se guardan en  /algún/otro/lugar.
 Ejemplo:
 <configurationGroup name='mercury_javascript_popup' path='/algun/otro/lugar'>
   <span style='color:red'>SOME STUFF GOES HERE</span>
 </configurationGroup> 


* El módulo es 'I2CE'. Los datos magic se guardan relativos a /I2CE

En el resto de esta sección describiremos <span style='color:red'>WHAT STUFF GOES THERE</span> que son [[#<configurationGroup>|<configurationGroup>]] y [[#<configuration>|<configurations>]] etiquetas.


<configurationGroup>
^^^^^^^^^^^^^^^^^^^^
Una <configurationGroup> puede tener varias subetiquetas en este orden:


* Un <displayName> opcional. Un nombre mostrado en la configuración del módulo para esta agrupación de datos
* Una <description> opcional. Una descripción de la funcionalidad de la agrupación.
* Una [[#<version>|<version>]] opcional de la etiqueta.
* Cualquier número (incluyendo al cero) de etiquetas de [[#<status>|<status>]].
* Cualquier número (incluyendo al cero)de <configurationGroup> o etiquetas de [[#<configuration>|<configuration>]].


<configuration>
^^^^^^^^^^^^^^^
Una <configuration> puede tener varias subetiquetas en este orden:


* Un <displayName> opcional. Un nombre mostrado en la configuración de este módulo para esa agrupación de datos
* Una <description> opcional. Una descripción de la funcionalidad de la agrupación.
* Una etiqueta de [#<version>|<version>]] opcional.
* Cualquier número (incluyendo al cero) de etiquetas de [[#<value>|<value>]].


Atributos
^^^^^^^^^
Hay varios atributos que pueden tener una[[#<configuration>|<configuration>]] y una [[#<configurationGroup>|<configurationGroup>]]:


* name: Este es un atributo requerido. Cada <configuration> o <configurationGroup> secundaria de un <configurationGroup> debe tener un nombre distinto. Si la ruta del atributo no se ha establecido, también dice que este nodo de configuración no debe aplicarse al nodo de los datos magic con el nombre dado y que es un nodo secundario de datos magic del nodo primario de configurationGroup.
* path: Esto es opcional Puede ser una ruta absoluta o relativa en los datos magic y describe los datos magic en los cuales se debe guardar este valor. Si esta es una ruta relativa, es relativa a la ruta de datos magic de su nodo primario.
* locale: Esto es opcional. Si está establecido, significa que el valor bajo este nodo debe considerarse como localizable.
* config: Esto es opcional.  Si está establecido, establece el objeto de I2CE_Swiss que se utiliza para mostrar los datos en el menú para configurar los módulos.
Una <configuration> puede también tener los siguientes atributos:


* type: Por defecto es establece como 'string' y describe el tipo de datos establecidos por las etiquetas de <value> de este nodo.
* values: Por defecto se establece como 'single' y describe si los datos establecidos por este nodo Deben ser un arreglo de valores o un único valor establecido en lo que se almacena en el nodo de <values>


<value>
^^^^^^^
La etiqueta de <value> es una subetiqueta de una etiqueta de [[#<configuration>|<configuration>]] .  Contiene él o los valores que se almacenan en los datos magic y depende de los [[#Attributes|attributos]] de *type*  y *values* .

Algunos tipos y valores comunes son:


* type='string' values='single':  El nodo de datos magic es de tipo escalar con valor de los contenidos de la etiqueta de <value> única.
* type='string' values='many':  El nodo de datos magic es de tipo primario. Tiene un nodo secundario de tipo escalar para cada etiqueta de <value>.
* type='delimited': El nodo de datos magic es de tipo primario. Se espera que las etiquetas de valor sean de la forma <value>'key':'value'</value> en cual caso se crea un nodo secundario de datos magic de tipo escalar de nombre 'key' y valor 'value'
* type='boolean':  Los valores en la etiqueta de <value> se interpretan como booleans:  F,f,False,false,0, etc. que se guardan en datos magic es 0.  De lo contrario, el valor que se guarda es 1.



<version>
^^^^^^^^^
Se puede tener acceso a los mismos datos magic desde múltiples archivos de configuración. Suponga que un módulo moduleA requiere un módulo moduleB y que ambos establecen /some/data para tener valores valA y valB respectivamente. Suponga que ambos módulos tienen la versión 1.0.
 <span style='color:tomato'>Excerpt from moduleA's configuration file</span>
 <configurationGroup name='some' path='/some'>
  <configuration name='data' >
    <value>valA</value>
  </configuration>
  <configuration name='data2'> 
    <value>valA2</value>
  </configuration>
 </configurationGroup>
 <span style='color:tomato'>Excerpt from moduleB's configuration file</span>
 <configurationGroup name='some' path='/some'>
  <configuration name='data'>
    <value>valB</value>
  </configuration>
  <configuration name='data2'> 
    <value>valB2</value>
  </configuration>
 </configurationGroup>


Durante la inicialización del sitio, ya que el moduleA requiere al moduleB, el valor primero se establece a valB se establece primero por el moduleB.  Luego se sobrescribe para que sea el valor valA por el moduleA.   De manera similar, después de la inicialización, el valor de '/some/data2' es 'valA2'

Suponga que la versión del moduleB se aumenta a la version 1.1 pero no hay otros cambios al archivo de configuración. Esto causará que el archivo de configuración se reprocese. El *configurator*  recordará que ya ha procesado todos los datos hasta la versión 1.01. Por lo tanto, no volverá a leer la sobrescrita que ya está guardada en los datos magic.

Suponga ahora que moduleB quiere cambiar el valor que guarda en /some/data a newValB, así como crear un Nuevo valor en /some/other_data. Sería necesario aumentar el número de la version del módulo a 1.2 y agregar una etiqueta de <version> para que el configurador sepa que al actualizar el módulo a la version 1.2 debemos leer de Nuevo los datos de configuración para todo lo mayor a la version cargada previamente de 3.1:
 <configurationGroup name='some' path='/some'>
  <configuration name='data'>
    <version>1.2</version>
    <value>newValB</value>
  </configuration>
  <configuration name='other_data'>
    <version>1.2</version>
    <value>The new stuff</value>
  </configuration>
  <configuration name='data2'> 
    <value>valB2</value>
  </configuration>
 </configurationGroup>
Ahora el valor de /some/data se actualizará a 'newValB' y agregaremos en el valor 'The new stuff' en '/some/other_data.'  El valor en '/some/data2' se mantiene igual y es 'valA2.'


<status>
^^^^^^^^
Una etiqueta de estado consiste en pares de valores clave:
 <status>key:value</status>
Aunque se puede utilizar cualquier cosa para la clave (siempre y cuando no contenga ':'), las claves que tienen significado son:


* version: Funciones como la [[#<version>|<version>]]
* overwrite: El valor puede ser verdadero o falso. Por defecto se establece como falso. Si es verdadero los datos magic se sobrescribirán aun cuando la version no lo haya hecho.
* merge:  El valor puede ser verdadero o falso. Por defecto se establece como falso. Si es verdadero los valores leídos se fusionan con los valores existentes utilizando *array_merge()*
* mergerecursive:  El valor puede ser verdadero o falso. Por defecto se establece como falso. Si es verdadero, los valores leídos se fusionan con los valores existentes utilizando *I2CE_Util::merge_recursive().*
* uniquemerge:  El valor puede ser verdadero o falso. Por defecto se establece como falso excepto si un nodo de <configuration> tiene el tipo='string' y los valores='many.'  Si es verdadero, los valores leídos se fusionan con los valores existentes utilizando  *I2CE_Util::merge_recursive()*  y solamente los valores únicos se mantienen utilizando *I2CE_Util::array_unique().*
* visible: El valor puede ser verdadero o falso. Por defecto se establece como verdadero. Si es verdadero, este nodo se muestra en el menú de configuración del módulo.
* advanced:  El valor puede ser verdadero o falso. Por defecto se establece como falso. Si es verdadero, se considera una opción avanzada para el menú de configuración del módulo
* required: El valor puede ser verdadero o falso. Por defecto se establece como verdadero. Dice que los valores resultantes en el nodo de <configuration> deben establecerse
* showIndex: El valor puede ser verdadero o falso. Por defecto se establece como verdadero.  En tal caso mostramos el índice en el menú de configuración del módulo


Los valores de las claves de estado se heredan a medida que se baja de nodo.

=Uso de Datos Magic en PHP=
Cada nodo de datos magic es una instancia de la clase **I2CE_MagicDataNode** .  Las "public variables" de un nodo son sus nodos secundarios que se realiza utilizando el método *__get()*  .  El I2CE_MagicDataNode implementa las Interfaces RecusriveIterator, ArrayAccess, SeekableIterator, y Countable.


I2CE tiene una instancia de datos magic de raíz que se pueden recuperar utilizando:
 $config=I2CE::getConfig();

Acceso Básico
^^^^^^^^^^^^^
Suponga que $data es un nodo de datos magic con un nodo secundario llamado 'my_list' y 'amount' que son de tipo primario y escalar respectivamente. Suponga que el nodo secundario 'amount' tiene in valor de 10.  Suponga que no hay ningún secundario llamado 'bad.'  Se puede tener acceso al secundario de varias maneras:
<center>
{| class='wikitable' border="1" cellspacing="5" cellpadding="2"
|-
! Access Method
! Result
! Notes
|-
| $data->my_list
| I2CE_MagicDataNode
| This is the 'my_list' node
|-
| $data->amount
| 10
|
|-
| $data->bad
| I2CE_MagicDataNode
| El nodo no existía, de modo que se creó.  <br/>Tiene un tipo indeterminado por el momento.
|-
| $data['my_list']
| I2CE_MagicDataNode
| the 'my_list' node
|-
| $data['amount']
| 10 
| el valor del nodo 'amount' 
|-
| $data['bad']
| I2CE_MagicDataNode
| Creamos el nodo 'bad' que no existía y lo regresamos
|-
|}
</center>


Acceso Refinado
^^^^^^^^^^^^^^^
Para obtener acceso más refinado a los nodos de datos magic puede utilizar la función **traverse(** $path,$create=false,$return_value=true''')''':
<center>
{| class='wikitable' border="1" cellspacing="5" cellpadding="2"
| $data->traverse('my_list',false,false)
| I2CE_MagicDataNode
| Este es el nodo 'my_list' 
|-
| $data->traverse('bad',false,false)
| null
| El Segundo argumento dice que no se cree un nodo que no existe
|-
| $data->traverse('amount',false,false)
| I2CE_MagicDataNode
| Este es el nodo 'amount' 
|-
| $data->traverse('my_list',false,true)
| I2CE_MagicDataNode
| Este es el nodo 'my_list'
|-
| $data->traverse('amount',false,true)
| 10
| The value of the 'amount' node 
|-
| $data->traverse('bad',false,true)
| null
| The second argument says not to create a node that doesn't exist 
|-
| $data->traverse('my_list',true,true)
| I2CE_MagicDataNode
| This is the 'my_list' node
|-
| $data->traverse('amount',true,true)
| 10
| el valor del nodo 'amount' 
|-
| $data->traverse('bad',true,true)
| I2CE_MagicDataNode
| Creamos el nodo 'bad' que no existía y lo regresamos
|}
</center>

Si un nodo es de tipo escalar, se puede obtener su valor con *getValue()* .  Si llama *getAsArray()*  en el mismo, también regresará su valor.

Si un nodo tiene un tipo primario o indeterminado, llamar *getValue()*  regresa el nodo en sí. Si llama *getAsArray()*  en el nodo regresará un arreglo anidado. Las claves de cada profundidad son los nombres de los nodos secundarios. Los valores pueden ser un arreglo o una cadena, en dependencia de si el secundario es escalar o no.


Revisar la Existencia y el Tipo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Puede utilizar el siguiente método para ver si un nodo de datos magic existe y de qué tipo es:


* '''pathExists('''$path''')'''
* '''is_scalar('''$path=null''')'''
* '''is_parent('''$path=null''')'''
* '''is_indeterminate('''$path=null''')'''
* '''is_root('''$path=null''')'''
Aquí, donde la ruta se establece a *null*  por defecto, el valor que el método se llama en el nodo mismo (esto no sería lo mismo que llamarlo en $path='./').

Podría hacer algo como:
function set_node_to_scalar($node) {
   if (!$node instanceof I2CE_MagicDataNode) {
     echo "Why are you giving me garbage data?\n";
     return false;
   } 
   if ($node->is_scalar()) {
     echo "This node is already a scalar.
     It has a value ".$node->getValue()."\nI don't need to do anything.\n";return true; 
   } else {
     echo "This node is a parent node.  Although it may or may not have children, 
     I can't set it to be scalar.\n";return false;
   } else{
     //$node->is_indeterminate() will return true
     echo "This node is indeterminate. Setting it to be scalar\n";
     $node->set_scalar();
     return true;
   }
 }
Otras dos funciones útiles son:


* **getAsArray(** $path=null''')''' que regresa el nodo y todos sus secundarios (recursivamente) como un arreglo
* **setIfIsSet(** &$var,$path,$as_array=false''')''' revisará si $path existe.  Si no existe, regresa falso. Si existe, regresa verdadero y puede que llame a getValue() o a getAsArray() en el nodo referido por la ruta.


Nombres de nodos secundarios e Iteradores
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Para obtener los nombres de los nodos secundarios de un nodo, utilizamos el método **getKeys()** .
Suponga que establecemos los datos magic de la siguiente manera:
<center>
{| class='wikitable' border="1" cellspacing="5" cellpadding="2"
|-
! Path
! Type
! Value
|-
| /
| parent
| <span style='color:red'>NONE</span>
|-
| /color
| scalar
| red
|-
| /modules
| parent
| <span style='color:red'>NONE</span>
|-
| /modules/modA
| parent
| <span style='color:red'>NONE</span>
|-
| /modules/modB
| parent
| <span style='color:red'>NONE</span>
|-
| /modules/modA/favorite_clay_animation
| scalar
| Mr. Bill
|}
</center>
También podría hacer algo similar como:
 echo "I like the color " . $config->color . "\n";
 $keys = $config->getKeys();
 foreach ($keys as $key) {
   if ($config->is_parent($key)) {
     echo "The node named $key under at " . $config->getPath(false) . " is a parent node.                                                                                                         It has children " . implode(',', $config->$key->getKeys()) . ".\n";
   } else if ($config->is_scalar($key)) {
    echo "The node named $key under at " . $config->getPath(false) .                                                                                                     " is a scalar with value " . $config->$key ".\n";
   }
 }
lo que resultaría en :
 I like the color red.
 The node named modules under / is a parent node.  It has children modA,modB.
 The node named color under / is a scalar node with value red.


Ya que un nodo de datos magic es un iterador, podemos hacer cosas como:
 foreach ($config as $key=>$node) {  if ($node instanceof I2CE_MagicDataNode) {
    echo "The node named $key under at " . $config->getPath(false) .                                                                                             " is a parent node.          It has children " . implode(',', $node->getKeys()) . ".\n";
   } else {
    echo "The node named $key under at " . $config->getPath(false) .                                                                                          " is a scalar with value " . $node .".\n";
   }
 }
lo que resultaría en:
 The node named modules under / is a parent node.  It has children modA,modB.
 The node named color under / is a scalar node with value red.
o:
 $modules = $config->modules;
 foreach ($modules as $module=>$data) {
   if ($data->is_scalar('favorite_clay_animation')) {
      echo "The module $module thinks " . $data->favorite_clay_animation . " is a super star!\n";
   }
 }
resultaría en:
  The module modA thinks Mr. Bill is a super star!

=Cambios de 3.1=


* Eliminamos los __ de los métodos de llamada.
* Relajamos las reglas de los nombres de los nodos de los datos magic.
* Implementamos las varias interfaces
* Agregamos soporte para localización de valores

[[Category:Developer Resources]]
