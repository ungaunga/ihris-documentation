Custom Reporting -- Creating Reports - ES
=========================================

Estos documentos aplican específicamente a iHRIS 4.0, aunque gran parte aplica a la versión 3.1.

Uso para el que fue Diseñado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Este paso está destinado para aquel que tenga una comprensión moderada de como los datos se relacionan en el sistema. Consiste en poco más de escoger una relación de formularios y seleccionar los datos que se quieren en el informe marcando las casillas específicas.

Una vez que el informe ha sido definido, se puede crear un [[Custom Reporting -- Creating Report Views|multiple views]] de los datos en el informe.

Pasos Iniciales
^^^^^^^^^^^^^^^
Para crear un informe, primero debe:

* escoger un [[Custom Reporting -- Creating Form Relationships|relationship]]
* seleccionar un "Display Name" para el informe,  el nombre del informe para el usuario final.
* seleccione un "Short Name" para el informe, el cual es una manera de hacer referencia internamente al informe y sólo puede contener caracteres alfa-numéricos y algunos signos limitados de puntuación tales como _ y -.
* Una descripción del informe.
* Una categoría para el informe.  Esto se utiliza para agrupar distintas vistas de informes.

Estructura de las Tablas en los Informes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Los informes se basan en [[Custom Reporting -- Creating Form Relationships|form relationship]].  Cada juego de formularios que satisfacen una relación corresponden a una fila en una tabla de informe. Un informe llamado **XXXXX**  ocasionara que  una tabla llamada 'zebra_'''XXXXX''''' y [[#Report Table Generation|populated]] se creen en la base de datos .   

Las columnas en una tabla de informe son:

* `$reportFormName+id`: Las id de cada uno de los formularios que satisfacen la relación.
* `$reportFormName+$fieldName`: Cualquiera de los [[#Selecting Fields|selected fields]] de cada uno de los formularios en la relación así como cualquier campo utilizado para [[#Selecting Limits|limit]] del reporte.
* `$function`: Cualquier [[#Selecting Functions|functions]] que esté seleccionado para el informe

Selección de Campos
^^^^^^^^^^^^^^^^^^^
Cualquiera de los campos en cualquiera de los formularios que satisfagan la relación de formulario seleccionada puede ser incluido en el reporte.

Selección de Límites
^^^^^^^^^^^^^^^^^^^^
Cualquiera de los campos de un formulario en la relación puede ser seleccionado para limitar el informe.  Estos límites aparecerán en las vistas del informe. Hay varias formas (estilos) para limitar un campo, dependiendo del campo, y son catalogados [[Limiting Forms#Existing Styles|here]].

Para cada estilo de límite para un campo, se puede fijar el encabezado de texto bajo el cual el límite es desplegado en la vista del informe.

Selección de Funciones
^^^^^^^^^^^^^^^^^^^^^^
Cualquiera de las [[Custom Reporting -- Creating Form Relationships#Adding in a SQL Function|functions]] definidas para una relación puede ser seleccionada para incluirse en el informe. También pueden ser escogidas como límites.

Agregando Links
^^^^^^^^^^^^^^^

Pivots
^^^^^^

En opciones de Límites para Campos de Informes, hay una opción "Enable Pivoting on this Limit".   El pivot permite vincular los valores mostrados en un informe a los limites/filtros de otro informe.

Para un ejemplo de esto, observemos el iHRIS Manage Demo site, busque bajo informe "Facility List".  Junto a los valores en la columna "Facility Name", se observa un [+].  Supongamos que estamos viendo el "Rushonga Hospital"

Al hacer click en el [+] se abrirá una lista de informes relacionados, Job Breakdown, Position List, Staff directory.  Si se hace click en el link "Switch to Staff Directory" nos llevará al informe Staff Directory donde el límite del "Rushonga Hospital" ya ha sido aplicado.

Creación de Tablas de Informes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Las tablas **zerbra_XXXXX**  contienen los datos del informe y se construyen del [[Form Caches|form caches]].   Estas tablas son generadas por procesos de fondo una vez que un informe se considera obsoleto. El proceso de fondo es generado por defecto cada 10 minutos. Esto puede ser especificado al definir el valor en datos magic en:

* /modules/CustomReports/times/background
El tiempo en que un reporte se vuelve obsoleto es por defecto 10 minutos.  Esto puede ser desautorizado por siguientes ajustes de valores en datos magic:

* /modules/CustomReports/times/stale
* /modules/CustomReports/times/stale_by_report/XXXXX

