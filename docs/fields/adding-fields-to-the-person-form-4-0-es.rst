Adding Fields to the Person Form - 4.0 - ES
================================================

Este tutorial aplica para la versión 4.0 de iHRIS Manage.  Para ver el tutorial de versiones diferentes del software vea lo siguiente:{{otherversions|Adding Fields to the Person Form}}

En este tutorial, veremos cómo agregar campos nuevos al formulario person a iHRIS Manage. Agregaremos dos campos, uno llamado "Favorite Color" que será una lista desplegable, y uno será "Favorite Animal" que será un campo para texto.  Hay muchas formas de pelar a mi animal favorito, un gato.  Igualmente, hay muchas formas de agregar un campo a un formulario.  Para mantener de mejor manera el código y las personalizaciones que estamos haciendo, lo haremos al crear un sub-módulo **Demo_ManagePerson** del sitio-módulo Demo que contiene todos los cuatro cambios.  Para ver una personalización similar, vaya a personalizaciones [`CSSC <http://bazaar.launchpad.net/~ihris%2Bcssc/ihris-manage/4.0-central/files>`_] y en especial bajo *modules/Person.*

 **<span style='color:red'>Advertencia:</span>**  En este tutorial modificaremos el sitio Demo de *ihris-manage* directamente.  Este no es el método recomendado para hacer este en un ambiente productivo.  Por favor lea [[Creating a Site]] para detales sobre cómo crear un sitio.


Pre-Requisitos
^^^^^^^^^^^^^^
Es recomendado leer los siguientes artículos y referirse a ellos conforme va leyendo este tutorial:


* [[Module Structure]]
* [[Configuration (Magic) Data ]]
* [[Forms and Fields ]]


Directorios
^^^^^^^^^^^
Puede que desee ver [[Customizing iHRIS Manage]] para generalidades de algunos de los directorios relevantes par alas personalizaciones. Nosotros haremos nuestras personalizaciones al sito Demo de iHRIS Manage. En unix puede que trabaje bajo:
;<Base Dir>:/var/lib/iHRIS
;<Site Dir>:/var/lib/iHRIS/4.0/ihris-manages/sites/Demo
Si tiene instalado Windows iHRIS Manage trabajará bajo los directorios:
;<Base Dir>:C:\Program Files\ihris-suite
;<Site Dir>:C:\Program Files\ihris-suite\sites\ihris-manage


Crear un Módulo Nuevo
^^^^^^^^^^^^^^^^^^^^^
Observando:


* **<SITE DIR>**/iHRIS-Manage-Demo.xml for Linux
* **<SITE DIR>**/iHRIS-Manage-Demo.xml for Windows
Vemos que podemos poner sub-módulos en los *módulos* del subdirectorio del directorio el sitio, que ya existe. Así que (en unix):
 mkdir **<SITE DIR>**/modules/DemoPerson
que contiene nuestro sub-modulo **DemoPerson**.  Luego guarde al archivo:
 **<SITE DIR>**/modules/DemoPerson/DemoPerson.xml
Los siguientes contenidos:
 <?xml version="1.0"?>       
 <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
 <I2CEConfiguration name='DemoPerson'>      
  <metadata>
    <displayName>Demo Person</displayName>   
    <category>Form</category>
    <description>Sets up the Demo Person form with extra fields for favorite animals and favorite color</description>
    <version>4.0.0</version> 
    <requirement name='Person'>
      <atLeast version='4.0'/>
      <lessThan version='4.1'/>
    </requirement>
    <path name='templates'>
       <value>./templates</value>
    </path>
    <priority>300</priority>  <!-- greater priority than ihris manage=200, but less than the site == 400 -->
  </metadata>
 </I2CEConfiguration>
Esto es (casi) la mínima cantidad de cosas que necesitamos hacer para crear un módulo nuevo.  En este momento, no hay funcionalidad, pero ya dijimos que el módulo *DemoPerson* requiere el módulo *Person,* que incidentalmente es un sub-module de ihris-common.  También fijamos la prioridad del módulo, para saber que los archivos plantilla que crearemos tomarán precedencia sobre cualquier cosa en los módulos ihris-manage o ihris-common.


Formularios y Clases de Formularios y Herencia
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En realidad hay dos partes para definir un "form", un formulario y una clase del formulario.  A los formularios se les refiere por sur *shortname,* por ejemplo *person.* Al segundo se le refiere por el nombre de una clase de PHP, por ejemplo, *iHRIS_Person*.  

Todos los datos magic para formularios están bajo */modules/forms.*  Los datos magic definen los formularios bajo */modules/forms/forms* y para las clases de formularios bajo */modules/forms/formClasses.*
Por ejemplo, el archivo de configuración  **<BASE DIR>**/ihris-common/modules/Person/Person.xml define el módulo *Person*.  Aquí verá dos nodos:
 <configrationGroup name='person'>
 </configurationGroup>
y
 <configrationGroup name='iHRIS_Person'>
 </configurationGroup>
El segundo define algunos de los campos asociados con la clase iHRIS_Person, y el primero nos dice la clase que el formulario *person* utiliza es *iHRIS_Person.*

Ahora si observamos el archivo de configuración **<BASE DIR>**/ihris-manage/iHRIS-Manage-Configuration.xml veremos dos cosas: que ihris-manage requiere el módulo *Person*,  y también veremos un nodo *<configurationGroup name='person'>* similar.  Esta vez el formulario *person* utiliza la clase *iHRIS_ManagePerson.*  Ya que *ihris-manage* requiere *Person*, la clase asociada al formulario person se carga desde iHRIS-Manage-Configuration.xml y no desde Person.xml

Si observamos más allá en este archivo, veremos el nodo *<configurationGroup name='iHRIS_ManagePerson'>* que define la clase *iHRIS_ManagePerson*.   Aquí verá dos cosas:


* iHRIS_ManagePerson extiende iHRIS_Person, así que tiene los mismos campos que iHRIS_Person
* iHRIS_ManagePerson agrega el campo llamado *password* con tipo 'STRING_PASS' pero que este campo no se guarda a la base de datos

Agregar los Campos a Datos Magic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Agregaremos los dos campos **fav_color** y  **fav_animal** a la clase DemoPerson.  Ya que queremos que *fav_color* sea una lista desplegable, también tendremos que crear un formulario llamado *fav_color* que contendrá los colores que queremos.  Para construir estos formularios y campos, tendremos que agregar datos (magic) de configuración.  Agregar a:
 **<SITE DIR>**/modules/DemoPerson/DemoPerson.xml
Lo que sigue luego de la etiqueta **</metadata>** :
 <configurationGroup name='DemoPerson' path='/'>
   <span style='color:olive'><status>overwrite:true</status></span>
   <configurationGroup name='forms' path='/modules/forms/forms'>
     <configurationGroup name='fav_color'>
        <span style='color:tomato'><nowiki><!-- define the 'fav_color' form --></nowiki></span>
        <configuration name='class' values='single'>  
          <value>I2CE_SimpleList</value>
          <span style='color:tomato'><nowiki><!-- fav_color uses the 'I2CE_SimpleList' form defined in i2ce/modules/Forms/modules/Lists--></nowiki></span>
        </configuration>
        <configuration name='display' values='single'>         
          <value>Favorite Color</value>  
          <span style='color:tomato'><nowiki><!-- the name of this form that is displayed to a user is 'Favorite Color'--></nowiki></span>
        </configuration>
     </configurationGroup>
     <configurationGroup name='person'>
       <span style='color:tomato'><nowiki><!-- the form 'person' is defined in ihris-common/modules/Person/Person.xml. --></nowiki></span>
       <configuration name='class'> 
          <value>DemoPerson</value>
          <span style='color:tomato'><nowiki><!-- Here we are changing the form class it uses to be 'DemoPerson' which is defined below --></nowiki></span>
       </configuration>
     </configurationGroup>
   </configurationGroup>
   <configurationGroup name='formClasses' path='/modules/forms/formClasses'>
     <configurationGroup name='DemoPerson'>
        <span style='color:tomato'><nowiki><!-- We are defining the DemoPerson class --></nowiki></span>
        <configuration name='extends'>
           <value>iHRIS_ManagePerson</value>
            <span style='color:tomato'><nowiki><!-- The DemoPerson class extends the 'iHRIS_ManagePerson' class defined in <BASE DIR>/iHRIS-Manage-Configuration.xml --></nowiki></span>
        </configuration>
        <configurationGroup name='fields'>
           <span style='color:tomato'><nowiki>< !-- Under here we add in the new fields that DemoPerson has --></nowiki></span>
           <configurationGroup name='fav_animal'>
              <span style='color:tomato'><nowiki><!-- The data definining the 'fav_animal' field of DemoPerson --></nowiki></span>
             <configuration name='formfield'>
               <value>STRING_LINE</value>
               <span style='color:tomato'><nowiki><!-- Set the field to have type 'STRING_LINE' which is a single line of text e.g. an <input type='text'> in a form--></nowiki></span>
             <configuration>
             <configuration name='headers' type='delimited' values='many'> 
               <value>default:Favorite Animal</value> 
               <span style='color:tomato'><nowiki><!-- Set the default header for this field to be 'Favorite Animal'--></nowiki></span>
             </configuration>
           </configurationGroup>
           <configurationGroup name='fav_color'>
             <span style='color:tomato'><nowiki><!-- The data definining the 'fav_color' field of DemoPerson --></nowiki></span>
             <configuration name='formfield'>
               <value>MAP</value>
               <span style='color:tomato'><nowiki><!-- Set the field to have type MAP. By default, this field will be one of the ids of the form fav_color--></nowiki></span>
             <configuration>
             <configuration name='headers' type='delimited' values='many'> 
               <value>default:Favorite Color</value> 
               <span style='color:tomato'><nowiki><!-- Set the default header for this field to be 'Favorite Color'--></nowiki></span>
             </configuration>       
          </configurationGroup>
        </configurationGroup>
     </configurationGroup>
   </configurationGroup>
 </configurationGroup>
El texto color <span style='color:tomato'>tomate</span> son comentarios que puede omitir si desea.

El texto color <span style='color:olive'>verde olivo</span> puede quitarse antes de la liberación, pero es útil para propósitos de desarrollo.  Se asegura que cualquier cambio que haga al archivo de configuración sea actualizado.


Personalizar los Archivos Plantilla
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En el paso anterior, habilitamos que dos campos se guardaran en la base de datos.  Ahora tenemos que editar el ínter faz del usuario para que muestre los campos donde sea apropiado.  Hay tres áreas que necesitamos para agregar estos campos:


* [[#Displaying the Favorites|Mostrar]] el expediente de una persona muestra su animal y color favorito
* [[#Editing the Favorites|Editar]] el expediente de una persona permite actualizar el animal y color favorito
* [[#Add to the Database Lists|Agregar]] un lugar en la página *Administer Database* para agregar los colores permitidos


Mostrar los Favoritos
~~~~~~~~~~~~~~~~~~~~~
La página titulada *View Person* y mencionada en el URL como **view** se brinda primero en el sub-módulo  *Person* de *ihris-common.*  Aquí, observando **<BASE DIR>**/ihris-common/modules/Person/Person.xml vemos que la página *view* carga por defecto el archivo **view.html** que podemos encontrar en **<BASE DIR>**/ihris-common/modules/Person/templates/view.html.

El módulo *ihris-manage* anula  *view.html* al proveerle en **<BASE DIR>**/templates/view.html

Ya que el archivo *view.html* no es especifico al módulo DemoPerson, no es apropiado poner nuestra versión modificada en el sub-módulo DemoPerson. En lugar de eso podremos el directorio de plantillas del módulo del sitio Demo. Aquí está en comando (unix):
 cp **<BASE DIR>**/ihris-manage/templates/view.html **<SITE DIR>**/templates/view.html

Para mostrar el animal y color favorito de una persona después de su nacionalidad, abra el recién creado **<SITE DIR>**/templates/view.html.  Busque la línea:
 <nowiki><span type="form" name="person:nationality" showhead="default" class="even"></span></nowiki>
y agregue lo siguiente unas líneas después:
 <nowiki><span type="form" name="person:fav_color" showhead="default" ></span></nowiki>
 <nowiki><span type="form" name="person:fav_animal" showhead="default" class="even"></span></nowiki>


Editar los Favoritos
~~~~~~~~~~~~~~~~~~~~
En *View Person,* el primer link *Update This Information* nos deja cambiar la información básica de la persona como el nombre y la nacionalidad.  Agregaremos los campos para cambiar su color y animal favorito en esta página.  Haciendo click en el link y observando el URL, vemos que esta página se llama **person.** 

Iniciamos observando el sub-módulo  *Person* de *ihris-common* para encontrar el archivo plantilla correcto a editar. Observando **<BASE DIR>**/ihris-common/modules/Person/Person.xml, vemos que la página *person* carga el archivo plantilla html por defecto *form_person.html.*  Este archivo se encuentra en **<BASE DIR>**/ihris-common/modules/Person/templates/form_person.html.  No es anulado por *ihris-manage*. 

Debido a que este archivo plantilla es especifico a una persona y no involucra ningún otro formulario, lo pondremos en nuestro modulo *DemoPerson*.  Crearemos un sub-directorio de plantillas y copiaremos ente archivo a ese directorio.  Aquí están los comandos (unix):
  mkdir **<SITE DIR>**/modules/DemoPerson/templates
  cp **<BASE DIR>**/ihris-common/modules/Person/tempaltes/form_person.html **<SITE DIR>**/modules/DemoPerson/templates/form_person.html

Ahora abrimos el recién creado **<SITE DIR>**/modules/DemoPerson/templates/form_person.html y buscamos la línea siguiente:
 <nowiki><span type="form" name="othername" showhead="default"></span></nowiki>
y agregamos:
 <nowiki><span type="form" name="fav_color" showhead="default"></span></nowiki>
 <nowiki><span type="form" name="fav_animal" showhead="default"></span></nowiki>
Justo después de ella.


Agregar a las Listas de la Base de Datos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Las listas guardadas en la base de datos se controlan a través de la página llamada *Administer Database* y se les refiere como **lists**.  Necesitamos agregar un link para administrar la lista de *Color Favorito*.  

La función básica de la página *list* es provista por *I2CE* por el sub-módulo *Lists* del sub-módulo *Forms*.  Aquí la página *lists* se maneja por la clase en **<BASE DIR>**/I2CE/modules/Forms/modules/Lists/lib/I2CE_PageFormLists, y vemos que se carga un archivo plantilla **lists.html**.  El **lists.html** es un archivo plantilla que contiene todas las listas de la base de datos que queremos administrar.  (Técnicamente, deberíamos tener un archivo *<BASE DIR>*/I2CE/modules/Forms/modules/Lists/templates/lists.html pero olvidamos agregarlo.)

Las páginas  *lists* se extienden en *ihris-common* a través de la clase en **<BASE DIR>**/ihris-common/lib/iHRIS_PageFormLists. También notamos que aquí hay un archivo plantilla **<BASE DIR>**/ihris-common/templates/lists.html que tiene todas las listas brindadas por *ihris-common*.

El módulo *ihris-manage* anula el *lists.html* brindado por *ihris-common* al brindarle el suyo propio en  **<BASE DIR>**/ihris-manage/tempalte/lists.html.  Verá que tiene todas las listas provistas por *ihris-common* así como las listas nuevas provistas por *ihris-manage.*  Este es el archive plantilla que modificaremos para nuestro sitio para agregarle la lista *Color Favorito* .  

Ya que el archivo *lists.html* no es especifico al módulo *DemoPerson*, no es apropiado poner nuestra versión modificada en el sub-modulo *DemoPerson*.  En lugar de eso pondremos el directorio de plantillas del módulo de sito Demo.  Aquí está el comando (unix):
 cp **<BASE DIR>**/ihris-manage/templates/lists.html **<SITE DIR>**/templates/lists.html
Ahora abra el archivo **<SITE DIR>**/templates/lists.html y agregue la línea siguiente:
 <nowiki><li task='can_edit_database_list_fav_color' ><a  href="lists?type=fav_color">Favorite Color</a></li></nowiki>
en el bloque<nowiki><ul></nowiki> bajo **Employee Lists.**

Notará, que tenemos un atributo *task* en la etiqueta <nowiki><li></nowiki>.  Un usuario con el rol Gerente de RH'' o *Administrator* puede editar cualquier lista de la base de datos.  Sin embargo, para el fin de este ejemplo, agregaremos esta tarea la cual podemos asignar a un usuario con el rol *Gerente de Capacitación*.  Hacemos esto en la [[#Setting the Edit Database List Favorite Color Task (Optional)| siguiente sección]]

Crear la Plantilla Editar Color Favorito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Tenemos que crear un plantilla llamada  'view_list_fav_color.html' en nuestro directorio de plantillas que contendrá:


.. code-block:: xml

    <!-- WARNING:  If you do not create the tasks as decribed below, you will need to remove the task attribute from this div -->
    <div id="list_display" class='recordsData' task="can_view_database_list_fav_color">
            
            <div class="editRecord">
            <p>Edit This Information</p>
                    <ul>
                            <li task='can_edit_database_list_fav_color'><span type="form" name="fav_color:id" href="lists?type=fav_color&amp;id=" >Update this Information </span></li>
                            <li><a href="lists?type=emp_status">Select another Favorite Color</a></li>
                    </ul>
            </div> <!-- editRecord -->
            
            <div class="dataTable">
            <table border="0" cellspacing="0" cellpadding="0">
                    <tr>
                            <th colspan="2">Favorite Color</th>
                    </tr>
                    <span type="form" name="fav_color:name" showhead="default"></span>
            </table>
            </div> <!-- dataTable -->
            
    </div> <!-- list_display -->
    



Fijando la Tarea Editar Lista de Base de Datos Color Favorito (Opcional)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
En la sección anterior, utilizamos una tarea *can_edit_database_list.*  En esta sección realizamos la tarea **opcional** de agregar esto a los datos de configuración.  

Inserte el código siguiente en  **<SITE DIR>**/modules/DemoPerson/DemoPerson.xml justo después de la etiqueta <span style='color:olive'><status>overwrite:true</status></span> :
 <configurationGroup name='tasks' path='/I2CE/tasks/task_description'>
    <span style='color:tomato'><nowiki><!-- This node has all of the tasks available to the system and a description of what they are --></nowiki></span>
    <configuration name='can_edit_database_list_fav_color'>
       <span style='color:tomato'><nowiki><!-- This is the task that we added to edit the database list associated with the form fav_color
           The class I2CE_PageFormList checks for the existence of "can_edit_database_list_$formname" for editing the list in the action() method--></nowiki></span>
       <value>Edit the Favorite Color list</value>
       <span style='color:tomato'><nowiki><!-- The description of the task.  It is displayed in the task/role management page --></nowiki></span>
    </configuration>
    <configuration name='can_view_database_list_fav_color'>
       <span style='color:tomato'><nowiki><!-- This is the task that we added to view an existing entry in the database list associated with the form fav_color
           The class I2CE_PageViewList checks for the existence of "can_view_database_list_$formname" for editing the list in the action() method--></nowiki></span>
       <value>View the training course status list</value>
       <span style='color:tomato'><nowiki><!-- The description of the task.  It is displayed in the task/role management page --></nowiki></span>
    </configuration>
 </configurationGroup>
 <configurationGroup name='tasks_trickle_down' path='/I2CE/tasks/task_trickle_down/' >
   <span style='color:tomato'><nowiki><!-- This node is used to describes all the sub-tasks that are a specific task has--></nowiki></span>
   <configuration name='can_view_database_list_fav_color' values='many'> 
     <span style='color:tomato'><nowiki><!--If we can view the database list for 'fav_color' we want to make sure we have permission to view 
         database lists in general. 
         The 'many' attribute says to treat this like an array of values --></nowiki></span>
     <value>can_view_database_lists</value>
   </configuration>
   <configuration name='can_edit_database_list_fav_color' values='many'> 
     <span style='color:tomato'><nowiki><!-- If we can edit the database list 'fav_color' we need to make sure we can view it as well as edit 
         database lists in general.
         The 'many' attribute says to treat this like an array of values --></nowiki></span>
     <value>can_view_database_list_fav_color</value>
     <value>can_edit_database_lists</value>
   </configuration>
 </configurationGroup>
 <configurationGroup name='role_trickle_down' path='/I2CE/tasks/role_trickle_down'>
   <span style='color:tomato'><nowiki><!-- This node is used to describes all the tasks that are assigned to various role --></nowiki></span>
   <configuration name='training_manager' values='many'>
     <span style='color:tomato'><nowiki><!-- This node defines the tasks that are assigned to the 'training_manager' role.  
         The 'many' attribute says to treat this like an array of values --></nowiki></span>  
     <status>uniquemerge:true</status>
     <span style='color:tomato'><nowiki><!-- We want to merge the existing tasks for the training_manager role to the ones we define below.
         The existing values for 'training_manager' are defined in <BASE DIR>/ihris-common/modules/TrainingCourse/TrainingCourse.xml --></nowiki></span>
     <value>can_edit_database_list_fav_color</value>
     <span style='color:tomato'><nowiki><!-- Here we assign the 'can_edit_database_list_fav_color' to the 'training_manager' role --></nowiki></span>
   </configuration>
 </configurationGroup>


Habilitar el Módulo
^^^^^^^^^^^^^^^^^^^
Ahora que tenemos todo listo, solo necesitamos habilitar el módulo 'DemoPerson' en el sitio.  Abra el archivo
 **<SITE DIR>**/iHRIS-Manage-Demo.xml
y agregue lo siguiente:
 <requirement name='DemoPerson'> 
  <atLeast version='4.0'>
  <lessThan version='4.1'>
 </requirement>

en la <metadata> sección después del requerimiento de *ihris-manage.* También, asegúrese de tener:


.. code-block:: xml

       <path name='modules'>
          <value>./modules</value>
       </path>
    




Cambiar el Encabezado de Animal Favorito
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Supongamos que quiere cambiar el encabezado del campo fav_animal de " Favorite Animal " a "Favorite Mammal"  Para hacer esto, necesitamos actualizar la  [[Configuration (Magic) Data#<version>|versión]] del módulo así como agregar una etiqueta de  <versión> en donde hemos cambiado el encabezado.  Los cambios se resaltan.  En la sección <metadata> tenemos:
  <metadata> 
  <displayName>Demo Person</displayName> 
  <category>Form</category> 
  <description>Sets up the Demo Person form with extra fields for favorite animals and favorite color</description>    
   <span style='color:olive'><version>4.0.1</version>  </span>
  <requirement name='Person'> 
     <atLeast version='4.0'/> 
    <lessThan version='4.1'/> 
  </requirement> 
  <path name='templates'> 
    <value>./templates</value> 
  </path> 
  <priority>300</priority> 
 </metadata>
y en la definición del campo 'fav_animal' tenemos:
      <configuration name='headers' type='delimited' values='many'> 
         <span style='color:olive'><version>4.0.1</version>
         <value>default:Favorite Mammal</value>              </span>
      </configuration>



<center>'''Happy Debbuging'''</center>

[[Category:Spanish]][[Category:Fields]]
