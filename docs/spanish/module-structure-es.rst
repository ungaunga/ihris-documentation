Module Structure - ES
================================================

Este tutorial describe la Estructura del Módulo de iHRIS. Un módulo de iHRIS es una colección de varios tipos de "code" por las características que proporcionan al sistema. Estos módulos pueden ser parte del sistema core I2CE y manejar cosas como la autenticación de usuarios o el acceso a bases de datos, también pueden brindar nueva funcionalidad a iHRIS como por ejemplo el manejo de permisos.



¿Qué es un Módulo?
^^^^^^^^^^^^^^^^^^
La Suite iHRIS está basada en el Intrahealth Informatics Core Engine (I2CE) que utiliza una estructura de modulo para encapsular y mantener el "code" en piezas manejables organizadas de acuerdo a la funcionalidad que proporcionan. Al decir "code" nos referimos a la colección entera de php, html, javascript, xml, archivos de imagen, css, flash, etc, que proporcionan la funcionalidad de una aplicación de red.


Un módulo está versionado para llevar un registro de los cambios a la funcionalidad y el API que tiene un módulo.

=¿Por qué los módulos?=


* La razón más importante para utilizar un sistema de módulos es la de aumentar la facilidad de manejo del código. Los muchos componentes de la Suite iHRIS (Qualify, Manage, y Plan) se utilizan en una variedad de escenarios que requieren sus propias personalizaciones.



* Cada uno de los componentes de la Suite iHRIS (Qualify, Manage, Plan) comparten algunas funciones comunes y el sistema de módulos asegura la reutilización de códigos de manera adecuada.



* El sistema de módulos permite encapsular varias personalizaciones sin tener que cambiar el código base subyacente. Esto permite que un desarrollador local pueda realizar sus cambios sin preocuparse por tener que rehacer esos cambios cada vez que se actualice el sistema core.



* Ya que los módulos están organizados de acuerdo a la funcionalidad que brindan al sistema, un desarrollador puede encontrar rápidamente los códigos relevantes que deben cambiarse solo con ver los módulos relevantes.



* Las personalizaciones al software encapsuladas en un módulo pueden compartirse fácilmente entre desarrolladores.

=El Módulo I2CE=
Este es el modulo "top"-most. Cada módulo tiene esto como requisito de manera implícita. El módulo central es el que brinda la funcionalidad mínima incluyendo datos magic, búsqueda de archivos, el sistema de plantillas y la fábrica de módulos. No tiene requisitos.

 *I2CE* proporciona varios sub-módulos opcionales. Por ejemplo:


* Admin -- Proporciona un sistema de manejo de módulos.
* Proceso de Fondo -- Proporciona una plataforma independiente con los medios para lanzar y monitorear procesos de fondo
* Reportes Personalizados -- Proporciona la funcionalidad de Reportes Personalizados
* Gráficos Flash -- Proporciona una interfaz para el sistema de maani flash charting
* Formularios -- Proporciona la estructura básica de formularios y campos que utiliza nuestro software
* MooTools -- Proporciona una interfaz php a la librería de javascript MooTools
* Tareas y Roles -- Proporciona un sistema de manejo basado en tareas para los roles de los usuarios

=El Módulo del Sitio=
El módulo "bottom"-most es el **Módulo del Sitio.**  Este módulo es el que se carga con el archivo **index.php** y le dice al sistema que módulos utiliza su sistema. Es el lugar apropiado para realizar personalizaciones básicas al sistema, por ejemplo, cambiar la imagen que se muestra en la página de inicio o para mostrar el nombre de su organización. Vea por ejemplo [[Customizing iHRIS Manage]]

=Archivo de Configuración del Módulo=
Un módulo existe al definir sus archivos de configuración. Hay un nodo de top-level <I2CEConfiguration> bajo el cual hay dos posibles nodos:


* Se requiere la etiqueta de [[#metadata|<metadata>]].
* La etiqueta de [[#Configuration (Magic) Data|<configurationGroup>]] es opcional.
La etiqueta <I2CEConfiguration> tiene un atributo requerido **name** cuyos valores deben ser un nombre corto único para describir este módulo tal como *I2CE*, *ihris-manage* o *mercury_javascript_popup.*  
El DTD que describe el formato del archivo de configuración está ubicado en *I2CE/lib/I2CE_Configuration.DTD*.  Como ejemplo:
 <?xml version="1.0"?>  
 <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
 <I2CEConfiguration name='mercury_javascript_popup'>     
   <metadata>
     <span style='color:tomato'>Some stuff defined [[#metadata|below]] </span>
   </metadata>
   <configurationGroup name='mercury_javascript_popup'>
     <span style='color:tomato'>Some stuff defined [[#Configuration (Magic) Data|below]] </span>
   </configurationGroup>
 </I2CEConfiguration>


metadata
^^^^^^^^
La etiqueta de DTD para <metadata> permite los siguientes nodos:
 <nowiki><!ELEMENT metadata (</nowiki>[[#displayName|displayName]],[[#className|className]]?,[[#category|category]]?,[[#description|description]]?,[[#creator|creator]]?,[[#email|email]]?,[[#link|link]]?,
   [[#version|version]],([[#enable|enable]]|[[#requirement|requirement]]|[[#conflict|conflict]]|[[#path|path]])*,[[#priority|priority]]?<nowiki>)></nowiki>
En su mayoría, el orden de estas etiquetas es importante debido a las limitaciones en la estructura de los DTDs.  Las excepciones son que las etiquetas de <permitidos>, <requeridos>, <conflictos> y <ruta> pueden enlistarse en cualquier orden entre ellos.

displayName
~~~~~~~~~~~
Esta etiqueta se requiere que sea el nombre de este módulo humanamente legible que se muestra, por ejemplo, en el *Configure Modules*
 Ejemplo: <displayName>Popup Box</displayName>


className
~~~~~~~~~
La etiqueta es opcional y asocial una clase para el módulo. Vea [[#The Module Class]] para obtener información específica acerca de la clase del módulo
 Ejemplo: <className>I2CE_Module_JavascriptPopup</className>

category
~~~~~~~~
Esta es una etiqueta opcional que se utiliza para agrupar módulos similares por categoría en la página de *Configure Modules*.
 Ejemplo: <category>Javascript Library</category>

description
~~~~~~~~~~~
Esta es una etiqueta opcional que da una descripción de este módulo que se muestra en la página de *Configure Modules* .
 Ejemplo: <description>Provides a javascript popup box</description>

creator
~~~~~~~
Esta es una etiqueta opcional que muestra al creador en la página de *Configure Modules*.
 Ejemplo: <creator>Freddy Mercury</creator>

link
~~~~
Esta es una etiqueta opcional que proporciona un URL para el módulo en la página '''Configure Modules'' .
 Ejemplo: <link>http://en.wikipedia.org/wiki/Freddie_Mercury</link>

version
~~~~~~~
Esta es una etiqueta requerida que se puede utilizar para versionar su módulo.
 Ejemplo: <version>1.0.0</version>

requirement
~~~~~~~~~~~
Esta es una etiqueta opcional, de la cual puede tener cuantas quiera. Cada etiqueta debe tener el **name** del atributo cuyo valor es el nombre de un módulo requerido por este módulo.  Esta etiqueta puede tener hasta cuatro sub-etiquetas posibles:


* atLeast
* atMost
* lessThan
* greaterThan
cada una de las cuales deben tener la **version** del atributo con un valor de una versión del módulo. Como ejemplo:
 <requirement name='I2CE'>
  <atLeast version='3.1'/>
  <lessThan version='3.2'/>
 </requirement>
dice que nuestro módulo requiere que I2CE tenga la versión al menos 3.1 y una menor que la versión 3.2.

Para que el módulo cargue, debe cumplir con todos los requerimientos satisfactoriamente.


conflict
~~~~~~~~
Esta es una etiqueta opcional de la cual se puede tener cuantas desee. Esto es opuesto a la etiqueta [[#requirement|<requirement>]] y enumera todos los módulos con los que este módulo tiene conflictos. Por ejemplo:
 <conflict name='plant_javascript_popup'>
 </conflict>
 <conflict name='ringo_javascript_popup'>
   <lessThan version=3.2/>
 </conflict>
Dice que nuestro módulo tiene un conflict con todas las versiones de la ventana emergente javascript de http://en.wikipedia.org/wiki/Robert_Plant Robert Plant], pero solamente tiene conflicto con la ventana emergente de [http://en.wikipedia.org/wiki/Ringo_starr|Ringo Starr] para las versiones menores a 3.2.

Un módulo no cargará si tiene un conflicto con cualquier otro módulo que ya este cargado.


enable
~~~~~~
Esta etiqueta es opcional, de la cual puede tener tantas como quiera. Esta etiqueta requiere el atributo **name** con el valor del nombre corto de un módulo. Esta etiqueta es más débil que la etiqueta de [[#requirement|<requirement>]] en que tratará de permitir el módulo nombrado, pero no causará que este módulo no cargue si no puede. También se diferencia de las etiquetas <requirement> y <conflict> ya que no hay información sobre la versión (bajo las sub-etiquetas atLeast,atMost, lessThan, greaterThan). Por ejemplo:
 <enable name='alex_patterson_javascript_paginator'/>
Dice que si el módulo paginador javascript de `Alex Patterson <http://en.wikipedia.org/wiki/Alex_Patterson>`_ puede cargarse, entonces que lo cargue. De lo contrario, no se preocupe por eso.


path
~~~~
Esta es una etiqueta opcional de la cual pueden haber las que desee. Cada etiqueta de <path> requiere el atributo **name** y puede tener tantas sub-etiquetas de **<value>** como lo desee. La etiqueta de <path> permite que el módulo especifique los directorios que se agregarán al grupo de utilidad de búsqueda de archivos por categoría. Las categorías se especifican por el nombre del atributo y algunos nombres comúnmente utilizados son:


* templates Estos son los directorios para buscar archivos de plantillas html
* images Estos son los directorios para buscar archivos de imágenes
* css Estos son los directorios para buscar archivos CSS
* scripts Estos son los directorios para buscar archivos javascript
* classes Estos son los directorios para buscar archivos que contengan clases de php.  La convención aquí es que MyClass se localiza en el archivo MyClass.php
* modules Estos son los directorios para buscar (sub-)módulos del módulo actual.
Para mayor información acerca de las rutas permitidas, vea [[File Search Paths]]


priority
~~~~~~~~
Esta etiqueta es opcional, la prioridad de un módulo es 50.
 Ejemplo: <priority>50</priority>
Estas son algunas prioridades estándar:


* I2CE 0
* sub-módulos de I2CE 50
* ihris-common 100
* sub-módulos de ihris-common 150
* ihris-manage, ihris-qualify, ihris-plan 200
* sub-módulos ihris-manage, ihris-qualify, ihris-plan 250
* un módulo de sitio 400


Configuración Datos (Magic)
^^^^^^^^^^^^^^^^^^^^^^^^^^^
El nodo de <configurationGroup> es opcional.  Si está presente tiene que tener el atributo **name** que tiene el mismo valor que el atributo **name** en la etiqueta que contiene <I2CEConfiguration> .  

Todos los datos magic son relativos a la ruta definida por este configurationGroup.  Hay tres opciones:


* La ruta del atributo no está presente. En el siguiente ejemplo, los datos magic se guardan bajo */modules/mercury_javascript_path.*
 Ejemplo:
  <configurationGroup name='mercury_javascript_popup'>
    <span style='color:red'>SOME STUFF GOES HERE</span>
 </configurationGroup>


* La ruta del atributo está presente. En el siguiente ejemplo, los datos magic se guardan bajo */some/other/place.*
 Ejemplo:
  <configurationGroup name='mercury_javascript_popup' path='/some/other/place'>
    <span style='color:red'>SOME STUFF GOES HERE</span>
  </configurationGroup> 


* El módulo es 'I2CE'.  Los datos magic se guardan con relación a */I2CE*

Este nodo <configurationGroup> realiza una doble función. Proporciona los datos de configuración que se guardan en los datos magic. También proporciona, por medio del módulo *Admin*, un sistema de menú de árbol para editar los datos magic establecidos por este sistema. Esto permite las personalizaciones dinámicas de su sitio.

Vea [[Configuration (Magic) Data]] para mayor información.


La Clase del Módulo
^^^^^^^^^^^^^^^^^^^
La clase del módulo debe proporcionar funcionalidad php a la clase. La clase del módulo es nombrada por la etiqueta opcional <className> en la sección <metadata> del archivo de configuración del módulo. Debe existir en las rutas de *classes* del módulo y debe ser sub-clase **I2CE_Module** que se encuentra en *i2ce/lib/I2CE_Module.php.*

Hay tres tipos básicos de funcionalidad que proporciona. Los primeros son métodos que se llaman cuando se activa, actualiza o desactiva un método. El Segundo es proporcionar ganchos en el sistema. El tercero es proporcionar métodos fuzzy.

Activar/Desactivar un Módulo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Hay varios métodos que se utilizan para iniciar, activar, desactivar y actualizar un módulo que se llaman por medio de la fábrica de módulos. Todos estos métodos esperan que el módulo regrese verdadero para indicar éxito.


* Cuando un módulo se activa, se llama el método **action_enable()**.
* Antes de activar un módulo por primera vez se llama **action_initialize()**.  <br/> Este es el lugar adecuado para hacer cosas como asegurar que todas las tablas en la base de datos que se espera que tenga el módulo, hayan sido creadas.  <br/> Por ejemplo, el módulo 'I2CE' tiene su propia clase 'I2CE_Module_Core' que hace lo siguiente:
* *Revisa que la base de datos del usuario está ahí, si no, la crea.
* *Se asegura de que hay un usuario administrativo para el sistema, si no, lo crea.
* *Revisa que la table config para los datos magic esté presente, si no, la crea.
* Cuando un módulo esta desactivado, se llama al método **action_disabled()** .
* Cuando la versión del archivo de configuración cambia, se llama **upgrade($old_vers,$new_vers)**.


Métodos Enganchados
~~~~~~~~~~~~~~~~~~~
Hay ciertos lugares específicos en el código que pueden prestarse naturalmente a sí mismos para engancharse para lograr mayor funcionalidad. 
Un módulo puede engancharse en el sistema en varios puntos. Para agregar un gancho se agrega la línea:
          I2CE_ModuleFactory::callHooks('some_hook_name',$some_argument);
o la línea:
          I2CE_ModuleFactory::callHooks('some_hook_name');
I2CE_ModuleFactory se encargará de llamar a todos los módulos que registren ganchos para ese punto, ya sea con uno o sin ningún argumento según sea adecuado. Todos los métodos enganchados se llaman (en orden de prioridad). El resultado de cada método enganchado adjunto a un arreglo que es entonces devuelto del método callHooks().

Un módulo registra los métodos a llamar vía el método getHooks() que regresa un arreglo con claves el nombre del gancho y valor el nombre del método en la clase del módulo.


Métodos Fuzzy
~~~~~~~~~~~~~
Un método fuzzy es uno que un módulo proporciona a otras clases PHP extendidas I2CE_Fuzzy por medio del método the __call(). Hay tres razones para utilizar los métodos fuzzy:


* PHP no puede hacer herencia múltiple para las clases, lo que dificulta combinar la funcionalidad de dos clases en una. Siempre se puede hacer una interfaz, pero se tiene que reescribir gran cantidad de código.
* La segunda es para proporcionar funcionalidad modular que pueda activarse y desactivarse.
* Puede ser necesario que la funcionalidad de una clase cambie dependiendo de si la clase se llama desde un servidor de red o desde la línea de comando.
La última razón es por la cual son *fuzzy:* los métodos pueden o no estar presentes en la clase dependiendo de cuales módulos estén activados.
Los métodos fuzzy que proporciona un módulo se definen por arreglos obtenidos con los métodos getMethods() y getCLIMethods().  Los resultados de estos métodos se procesan cada vez que el módulo se activa o cada vez que se detecta un cambio en el archivo de fuente de la clase del módulo. Cuando se desactiva un módulo, los métodos fuzzy que proporciona desaparecen de la clase.

Por ejemplo el módulo *FormWorm*'s getMethod() regresa:
 array('I2CE_Page->addFormWorm'=>'addFormWorm',
       'I2CE_Template->addFormWorm'=>'addFormWorm'
       )
cuando el módulo FormWorm está activado, este proporciona los métodos addFormWorm()tanto a la clase I2CE_Page y I2CE_Template como a cualquier clase secundaria de estas. La forma general de este arreglo es:
   CLASS->CLASSMETHOD => MODULEMETHOD
donde CLASSMETHOD es un método fuzzy proporcionado a la clase CLASS. Este método fuzzy se implementa al llamar MODULEMETHOD en la instancia de la clase de un módulo. El primer argumento de MODULEMETHOD será la clase desde la cual se llamó el método fuzzy y los argumentos que quedan son los argumentos con los cuales se llamó CLASSMETHOD. 

Por ejemplo, si $page es una instancia de I2CE_Page entonces la llamada:
  $page->addFormWorm($arg1,$arg2) 
resulta que la fábrica del módulo tomara su instancia, $module, del I2CE_Module_FormWorm y llamará:
  $module->addFormWorm($page, $arg1,$arg2);

El método fuzzy solamente tendrá acceso a los métodos públicos y variables de la clase que llama(I2CE_Page en este ejemplo).  Incidentalmente, esto motiva el desarrollo de un buen API para la clase que llama.

Como los otros componentes de un módulo (tales como archivos de plantillas), los métodos fuzzy se priorizan y solamente el de menor prioridad es llamado. Puede ver la documentación de las clases I2CE_Module y I2CE_ModuleFactory para mayor información.
[[Category:Modules]][[Category:Spanish]]
