Form Caches - ES
================

El software iHRIS realiza caché de los datos guardados en la base de datos (o archivo XML , o servidor LDAP) para tener acceso más rápido y la habilidad de crear índices.   Estos cachés se utilizan, por ejemplo, para llenar informes y listas.


A los datos para un formulario *XXXXX*  se les puede haber realizado caché en una *hippo_XXXXX.*   Esta tabla hippo puede utilizarse para:


* Generar informes para [[Custom Reporting -- An Overview | Custom Reporting]]
* Exportar datos para [[Managing Decentralized iHRIS Manage with Launchpad|decentralized data management]]

Estructura de la Tabla Hippo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Si un formulario XXXXX tiene un campo YYYYY entonces la tabla hippo_XXXXX tendrá una columna `XXXXX+YYYYY.`  También hay una columna `XXXXX+id` que contiene la id del formulario y una columna  `XXXXX+parent` que contiene el formulario primario, si lo hay.

Momentos de Caché y Línea de Comando
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Las tablas hippo se generan mediante un proceso de fondo una vez que el caché de un formulario se considera obsoleto. Vea el documento [[Configuring Form Cache Generation Timing]] para mayor información en el momento para los cachés de formularios y acerca de la creación manual de los cachés de formularios desde la línea de comando.

To see this tutorial for different versions of the software see the following:{{otherversions|Exporting and Updating Form Caches Using Profiles}}

=Editar, Exportar y Actualizar los Cachés de Formularios Utilizando Perfiles=

En la versión **4.0.6**  agregamos la habilidad de crear *perfiles*  de cachés de formularios.  Un perfil es simplemente una lista de formularios que puede usar para realizar las siguientes acciones rápidamente:


* [[#Updating the Cache of a Profile|Actualizar]] el caché para cada formulario en el perfil
* [[#Exporting the Cache of a Profile|Exportar]] el caché, por medio de mysqldump, para cada formulario del perfil. Esto es particularmente útil para exportar datos de una oficina regional o de distrito al nivel nacional.

Esta funcionalidad es parte de los [[I2CE_Module_List#CachedForms  | Cached Forms modules]] y se puede tener acceso a la misma hacienda click en los links de **Configure System**  y luego  **Cached Forms** 


Crear un Perfil
^^^^^^^^^^^^^^^
El primer paso es crear un *perfil*  de los formularios. Un perfil es una lista de formularios con un nombre corto que puede usar para ayudarle a identificar la lista.  



* Busque en  **Create/Edit Profile**  en la página *Cached Forms*  . Aquí asegúrese de que "Create a new profile" este seleccionado en la lista y luego haga click en el botón "Edit".
* Ahora escriba un nombre para el perfil. Es mejor escoger un nombre corto con signos de puntuación limitados como "nightly_update"
* Ahora seleccione cada uno de los formularios que desea incluir en el perfil
* Finalmente, haga click en el botón "Submit" al final de la página


Actualizar el Caché de un Perfil
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Puede actualizar todas los formularios en un perfil bajo **Cache Forms**  en la página *Cached Forms* .


* Escoja el perfil para el cual quiere realizar caché de los formularios
* Haga click en el botón "Cache"


Exportar el Caché de un Perfil
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hay dos usos principales de la exportación de todos los formularios en un perfil, puede obtener todos los datos, o solamente hacer modificaciones a los datos desde la última fecha. Se puede tener acceso a ambos bajo **Export Cached Forms**  en la página *Cached Forms*  .


* Escoja el perfil que desea exportar
* Escoja si desea activar compresión bzip2 o no
* Opcionalmente seleccione la hora de modificación.

  * Si no establece la hora de modificación, obtendrá todos los datos de los formularios. El mysqldump incluirá afirmaciones de "DROP TABLE IF EXISTS" y "CREATE" para cada tabla hippo_XXXX .  Los datos se llenan por medio de las afirmaciones "INSERT"
  * Si no establece la hora de modificación, obtendrá todos los datos de los formularios. EL mysqldump no incluirá la afirmación "DROP TABLE IF EXISTS" '''ni'' la "CREATE" para cada tabla hippo_XXXX .  Los datos se llenan por medio de las afirmaciones "REPLACE" .

* haga click el botón "Export"

 **Nota:**  Cuando exporte el caché, no lo actualiza primero. Deberá hacer esto manualmente.


Interacción de la Línea de Comando y Crontab
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Por ejemplo, usted podría desear poner una actualización en el perfil "nightly_update"  en su crontab:
  30     1     *     *     *         /usr/bin/php /var/www/ihris-manage/index.php --page=/CachedForms/cache --get=profile=nightly_update
causará que todos los formularios en el perfil 'nightly_update' se actualicen a las 1:30am. Poniendo:
  10     *     *     *     *         /usr/bin/php /var/www/ihris-manage/index.php --page=/CachedForms/cache --get=profile=hourly_update
en su perfil actualizará cada formulario en el perfil 'hourly_update' diez minutos después de la hora.

This page is a translation of [[Form Caches]].


