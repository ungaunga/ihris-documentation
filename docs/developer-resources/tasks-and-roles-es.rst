Tasks and Roles - ES
====================

iHRIS utiliza un mecanismo de seguridad basado en Roles y Tareas para limitar el acceso a las diversas partes del sistema. A un usuario se le asigna un rol y un rol es un conjunto de tareas que ese rol puede realizar.

Este artículo describe como se definen los roles y tareas en Datos Magic y utilizados por el sistema iHRIS. 

=Roles=
Un rol es una colección de [[#Tasks|tareas]] que pueden asignarse a la cuenta de un usuario.

* los nombres de los roles se definen como los secundarios de [[Configuration (Magic) Data|ruta de magic data]] /I2CE/roles/names
* un rol $role tiene un display definido en /I2CE/roles/names/$role/display_name
* los roles pueden heredar tareas de otro al agregarlo como el valor de un nodo secundario de /I2CE/roles/names/$role/trickle_up <br/>Por ejemplo, en iHRIS Manage en el /I2CE/roles/names/hr_staff tenemos:
* * display_name => HR Staff
* * trickle_up => Array
* ** 0 => admin
* ** 1 => hr_manager
dice que el rol de hr_staff aparece como 'HR Staff' y que un hr_manager o admin tiene todas las tareas que tiene un hr_staff.

=Tareas=
Una tarea puede ser tanto una colección de sub-tareas que tiene esta tarea y la descripción de alguna acción cuyo permiso se puede verificar. La información de las tareas se guarda en datos magic bajo /I2CE/tasks/.  Para crear una tarea se crea un nodo secundario de tipo escalar de /I2CE/tasks/task_description.  El nombre del nodo es el nombre utilizado para referenciar la tarea.  El valor del nodo es la descripción de la tarea que se muestra en la página de Manejo de Tareas y Roles.  Por ejemplo, el nodo de magic data /I2CE/tasks/task_description puede verse así:

* custom_report_admin => Permite la administración del Sistema de Informes Personalizados
* custom_reports_can_access => Permite acceso mínimo al Sistema de Informes Personalizados
* custom_reports_delete => Permite eliminación de datos acerca de los informes personalizados
* custom_reports_can_access_relationships => Permite acceso a las Relaciones de Informes Personalizados
Puede definir la sub-tarea de una tarea $task al especificar /I2CE/tasks/task_trickle_down_task.  Por ejemplo, el nodo de datos magic /I2CE/tasks/task_trickle_down/custom_reports_admin puede verse así:

* 0 => custom_reports_can_access
* 1 => custom_reports_delete_reports
lo que dice que la tarea de 'custom_report_admin' tiene todas las tareas y derechos definidos por  'custom_reports_can_access' y 'custom_reports_delete_reports.'

Las tareas que se asignan a un rol $role son los valores de los secundarios bajo /I2CE/tasks/role_trickle_down/$role

Un usuario con el rol 'admin' tiene todas las tareas.

=Usos de las Tareas y Roles=
Las tareas y roles se utilizan en varios lugares:

* La clase principal [[Pages and Templates#Page Logic|I2CE_Page]] revisa los permisos básicos de la página.
* Varias páginas revisan los roles específicos y las tareas en su método action().
* Antes de mostrar el HTML la clase I2CE_Template, verifica que todas las tareas, roles y permisos estén satisfechos en cada nodo.

=Administración de Tarea y Rol=
Para implementación en varias computadoras, las tareas y los roles deben establecerse en un [[Module Structure#Module Configuration File|archivo de configuración]] de módulo adecuado.

Para establecer tareas y roles de manera dinámica, el módulo 'tasks-roles' proporciona la página llamada 'roles' y la página llamada 'tasks' que permite la creación de nuevos roles y tareas; así como la definición de la herencia de permisos.

=Permisos y Analizador de Permisos=
El analizador de permisos permite expresiones lógicas para combinar varios tipos de permisos, tales como *tarea* , *roles* , en una *cadena de permisos* .

Podemos asignar tareas, roles y permisos a los nodos DOM al:

* Establecer el atributo *rol* .   <br/>Si el valor es X, esto resulta en la cadena de permiso *rol(X)*  que se pasa al analizador de permisos
* Establecer el atributo *task* . <br/>Si el valor es X, esto resulta en la cadena de permiso  *task(X)*  que se pasa al analizador de permisos
* Establecer el atributo *permiso.*
Si el nodo falla cualquiera de las revisiones rol, tarea o permiso, eliminará el nodo

Tipos de Permiso: tarea y rol
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Los tipos de permisos de tarea y roles se forman rodeando el nombre de un rol con role() o el nombre de una tarea con task().  Por ejemplo, se puede crear la siguiente *cadena de permiso* :
 (task(can_edit_database_list_facility_type) & task(can_edit_database_list_fav_color) || role(admin)
Por defecto, las tareas y roles son 'OR'ed juntos así que los siguientes son todos iguales:

* task(can_edit_database_list_facility_type) or task(can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type) | task(can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type)  task(can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type,can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type can_edit_database_list_fav_color)
* task(can_edit_database_list_facility_type|can_edit_database_list_fav_color)

Tipo de Permiso: módulo
^^^^^^^^^^^^^^^^^^^^^^^
Cualquier función pública de una [[Module Structure#The Module Class|clase de módulo]] puede llamarse utilizando el analizador de permisos. Por ejemplo, suponga que el modulo 'my_module' tiene un método 'my_method()' entonces podemos utilizar como la cadena de permiso con [[#Arguments|argumentos]]:
 module('my_module','my_method', [arg1], ... , [argN])
lo que resultaría en el llamado:
 $module->my_method($arg1,..,$argN)
donde $module es la instancia de la clase del módulo para el módulo 'my_module.'

Tipo de Permiso: formulario
^^^^^^^^^^^^^^^^^^^^^^^^^^^
El módulo 'forms' incluye el tipo de formulario. La cadena de permiso con [[#Arguments|argumentos]]:
 form('form_name', 'form_method', [arg1] , .., [argN])
resulta en el llamado:
 $form->form_method($arg1,..,$argN)
donde $form es el resultado de obtener el formulario por el nombre de 'form_name' por medio de los [[Pages and Templates#Template Data|datos de la plantilla]] para el nodo (si hubiese alguno) al que se asignó la cadena de permiso.

Argumentos
^^^^^^^^^^
Un tipo de permiso (tal como rol, tarea, formulario o módulo) en una cadena de permiso, se comporta esencialmente como una función. Suponga que tenemos la forma general de una pieza de una cadena de permiso:
 type([arg1],[arg2],...,[argN])
Entonces esto resulta en el método llamado:
 $permissionParsrer->hasPermission_$type($node,$args)
donde $node es el DOMNode en el que se llamó la cadena de permiso y $args es el arreglo $arg1,..$argN).  El analizador de permiso convierte [argM] en $argM de acuerdo a las siguientes reglas:

* Si [argM] empieza con un $ entonces se refiere a los datos de la plantilla y las siguientes reglas aplican:
* *La cadena tiene el formulario $abcd. El valor de $argM se convierte en la plantilla para mostrar los datos con el nombre 'abcd.'
* *La cadena tiene el formulario ${WXYZ}abcd.  El valor de $argM se convierte en los datos de la plantilla con la categoría 'WXYZ' y con el nombre 'abcd.'
* <NODE> se convierte en la instancia de DOMNode (si hay) en la que se llamó la cadena de permiso
* <TEMPLATE> se convierte en la instancia de I2CE_Template (si hay) en la que se llamó el analizador de permiso
* <USER> se convierte en la instancia de I2CE_User que es esta sesión
* si [argM] empieza con una sola comilla ' entonces es una cadena hasta que la siguiente ' no-escapada se encuentre
* si [argM] empieza con una doble comilla " entonces es una cadena hasta que la siguiente " no-escapada se encuentre. <br/>Además se aplican las siguientes reglas de sustitución:
* *cualquier sub-cadena que empieza con $ y que consiste de caracteres alfanuméricos , - o _ se interpreta como datos mostrados en la plantilla a ser sustituidos <br> Por ejemplo "my name is $name" se convierte en "my name is Joe" si los datos de la plantilla llamada 'name' y con el DISPLAY tipo "Joe"
* *cualquier sub-cadena que empiece con {$ se lee hasta que se encuentre un } .  La cadena entre $ { y } es el nombre del dato de la plantilla de DISPLAY que es entonces sustituido .
* *Para prevenir lo anterior, { y $ se pueden escapar con una \
* cualquier otra cadena de caracteres alfanuméricos (y algunos signos de puntuación permitidos) se interpretan como una cadena

Los argumentos se pueden separar con una coma, un espacio o un |.

Nuevos Tipos
^^^^^^^^^^^^
Un módulo puede agregar un [[Module Structure#Fuzzy Methods|método fuzzy]] del formulario  *hasPermision_$type*  a la clase *I2CE_PermissionParser*  para permitir un Nuevo tipo de permiso, Por ejemplo el módulo de 'forms' hace esto añadiendo un nuevo 'form.' de tipo de permiso

