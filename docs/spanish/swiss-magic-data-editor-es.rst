Swiss Magic Data Editor - ES
================================================

La mayor parte de la configuración del software iHRIS se maneja definiendo los [[Configuration (Magic) Data|datos magic ]].   Para manejar la edición estructurada y como se muestran estos datos magic de configuración y evitar la corrupción de los datos, se desarrolló un conjunto de clases de php, los editores de datos Swiss Magic. Estos se utilizan, por ejemplo en la definición de las relaciones entre formularios e informes.

Los editores Swiss Magic editan y ven jerárquicamente los datos de configuración. este artículo describe la estructura de las clases Swiss Magic PHP.


Características
^^^^^^^^^^^^^^^


* Proporciona diferentes maneras de atravesar la jerarquía de la configuración de los datos magic por medio de diferentes fábricas
* Mucho de las buenas características de AJAX se han incluído para mostrar sub-menús dentro del menú actual
* Utilizado en la herramienta de construcción de "Form Relationship" y de "Custom Reporting"
* Utilizado en la herramienta de "Configure Modules"
* El procesamiento y muestra de los datos ya está localizado. Solamente necesita llamar "renameInputs()" para renombrar cualquiera de sus elementos de formularios html.


Ejemplos
^^^^^^^^


* [[Swiss Magic Data -- Form Relationships|Relaciones de Formularios]]
* Informes
* Visualización de Informes


El Nodo Swiss
^^^^^^^^^^^^^
Un **nodo swiss** es una sub-clase de I2CE_Swiss.  Puede pensar en las clases I2Ce_Swiss como definidores de un GUI widget para la interacción con los magic data. Asociados a un nodo swiss esta:


* un nodo de magic data
Un nodo swiss tiene las siguientes funciones:


* valores de visualización guardados en este nodo de magic data
* crear una interfaz de usuario para editar los valores en este nodo de magic data
* procesar un arreglo asociativo de valores para actualizar el nodo de magic data
* determinar los *tipos* de sus nodos swiss secundarios.  Un nodo de tipo $type es un nodo de clase I2CE_Swiss_$type.


Métodos a implementar
~~~~~~~~~~~~~~~~~~~~~
Al crear un Nuevo tipo Swiss solamente debe implementar estos métodos:


* displayValues() El método utilizado para mostrar los datos asociados con el swiss node. Pueden definirse con diferentes acciones.  Hay dos acciones principales:
* *view: La acción de mostrar  una vista de solo lectura de los datos magic en ese nodo.
* *edit: La acción de mostrar una vista de edición de los datos magic en ese nodo.
* processValues() El método utilizado para procesar un arreglo asociado de valores y actualizar los datos magic. Debe ser definida
* getChildType()  Obtiene el tipo de secundario swiss con el nombre dado.


Métodos Útiles
~~~~~~~~~~~~~~
Se deben utilizar los siguientes métodos


* getStorage()  Obtiene el nodo de magic data asociado al nodo swiss.
* getChild() Obtiene el nodo swiss secundario con el nombre dado.
* renameInputs()  Es necesario llamarlo para renombrar todos los elementos del formulario html input/select/textarea del DOMNode dado que están asociados a ese nodo swiss.
* addAjaxLink() Agrega un vincula a un nodo swiss secundario. Si el navegador es compatible con AJAX, lo hará de manera AJAX. De lo contrario será solamente un vinculo
* get/set/hasField()  Métodos de conveniencia para tener acceso al nodo secundario de datos magic (escalar) nombrado.


Las Fábricas Swiss
^^^^^^^^^^^^^^^^^^
La Fábrica Swiss se encarga de:


* proporcionar el nodo de magic data adecuado asociado a un nodo swiss
* crear el nodo swiss secundario adecuado
* atravesar los nodos swiss cuando se da una ruta
* pre-procesar variables GET/POST y pasarlas al nodo swiss adecuado.
* manejar errores en la actualización de valores en base a valores GET/POST.
* implementar las interfaces del Iterador y Count

La Fábrica Swiss está determinada por:


* el nodo de magic data de raíz
* la clase del nodo swiss de raíz

Hay dos fábricas disponibles Swiss Magic y Swiss Config.  Estas tienen sub-clases correspondientes I2CE_Page para tener acceso a la interfaz de la red.


Fábrica Swiss Magic
^^^^^^^^^^^^^^^^^^^
Esta es la fábrica swiss para crear contenido dinámico en I2CE.  Esto incluye:


* Relaciones de Formularios Personalizadas
* Informes Personalizados
* Visualización de Informes Personalizados

Primarios y Secundarios
~~~~~~~~~~~~~~~~~~~~~~~
Cualquier nodo de datos magic (no-escalar) puede servir como el nodo swiss raíz.  

El nodo secundario de un nodo swiss está en correspondencia de uno a uno con los nodos secundarios de los nodos de datos magic correspondientes. Los nombres de los nodos swiss secundarios son los mismos que los nombres de los nodos de datos magic secundarios.


Acceso a la Página
~~~~~~~~~~~~~~~~~~
Esta fábrica se puede dar en la interfaz de la red como una instancia de la clase I2CE_Page_SwissMagic. Esto se hace para:


* Relaciones de Formularios
* Informes Personalizados
* Visualización de Informes Personalizados


Fábrica de Configuración Swiss
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Esta es la Fábrica Swiss diseñada para le herramienta de configuración de módulos.

Primarios y Secundarios
~~~~~~~~~~~~~~~~~~~~~~~
En esta fábrica los nodos swiss primarios de una clase swiss dada se definen por un archivo de [[Configuration (Magic) Data|module configuration XML#Defining Magic Data in Configuration Files]] .   El nodo swiss raíz primario es el *<configurationGroup>* principal en el archivo de configuración XML.  

Los nodos swiss secundarios asociados a un *<configurationGroup>* dado son exactamente los secundarios de las *<configuration>* y de los *<configurationGroup>* en ese nodo.  Los nombres de los nodos swiss secundarios son los nombres de los nodos secundarios *<configuration>* y *<configurationGroup>* .

Los datos magic asociados con un nodo swiss es exactamente el nodo de datos magic asociado al nodo de *<configuration>* o *<configurationGroup>* dado como se ha definido por el atributo de **path** y **name**.


Acceso a la Página
~~~~~~~~~~~~~~~~~~
Para la página de "Configure Modules", cada módulo crea una instancia de fábrica swiss por la instancia de la clase I2CE_Page_SwissConfig class.  

[[Category:Magic Data]][[Category:Spanish]]
