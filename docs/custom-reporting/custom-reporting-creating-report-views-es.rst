Custom Reporting -- Creating Report Views - ES
================================================

Éste documento aplica a la iHRIS Suite versión 4.0. Para la versión 3.1, los métodos son similares, pero no idénticos.


Usuario para el que se Diseñó
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
La visualización del informe se diseñó para ser lo más simple posible para  el usuario final de crear y observar.

Puede que desee revisar el [[Custom Reporting -- An Overview#Tasks | tasks]] para informes personalizados.


Crear y Editar una Visualizaión de Informe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Haga click en "Configure System" en la página de inicio.  Luego, bajo "Manage Reports" haga click en "Report Views."   Ahora puede elegir ya sea editar la Visualización de un Informe existente o Crear una Visualización Nueva.

Para crear una nueva Visualización de Informe, necesita seleccionar [[Custom Reporting -- Creating Reports|Report]] del cual esta visualización se basa.  También se le sugerirá nombrar el informe y a brindar una descripción.  


Selección de Campos
~~~~~~~~~~~~~~~~~~~
Tendrá una lista de campos disponibles para el Informe seleccionado.  Puede escoger, al marcar una casilla, cuáles de estos campos desea que se muestren en la Visualización del Informe. También puede cambiar el nombre (encabezado) de los campos.

Ordenar Campos
~~~~~~~~~~~~~~
Puede escoger el orden en el cual los campos son listados arrastrando y moviendo los distintos campos.


Fijar la Visualización Predeterminada
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Puede fijar la visualización predeterminada para la Visualización del Informe de la siguiente manera:


* Visualice la Visualización de Informe deseada
* Elija cualquier opción limitante que desee
* Elija cualquier clasificación que desee
* Seleccione la casilla "Set as Default"
* Haga click en el botón de visualización deseada (e.j. "Print" o "View")
Puede borrar la visualización predeterminada desde la Edit Report Views Page.


Agregar Visualización de Informes Relacionados
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Puede que desee crear un "Jump" rápido de la visualización de un informe a otra que se observe en la parte de abajo de la pantalla HTML.  Puede hacerlo al editar la Visualización del Informe.


Agregar Datos
^^^^^^^^^^^^^

En Report Views, hay una opción para los campos "Choose a
method to aggregated this data".    Esto se utiliza cuando se agregan datos en la visualización del informe para obtener el número total de algo.    
El informe "Staffing Norm 2010" en el iHRIS Manage Demo es un ejemplo de esto.

Aquí, si se tiene una visualización de informe con los campos Job, Cadre, Facility, Facility Type, Filled Positions (en realidad la id interna del formulario position), y Staffing Norm.

Se selecciona Filled Positions para agregarse como un "Total."   Sí "Total no fue seleccionado, el informe se verá algo parecido a:


* ER Nurse, Nurse, Rushonga Hospital, Hospital, position|23213, 5
* ER Nurse, Nurse, Rushonga Hospital, Hospital, position|24324, 5
* ER Nurse, Nurse, Rushonga Hospital, Hospital, position|22344, 5
* ER Nurse, Nurse, Marjoram Hospital, Hospital, position|21224, 2
* ER Nurse, Nurse, Marjoram Hospital, Hospital, position|29924, 2

Lo que "Total" en la columna "Filled Position" hace es agrupar los datos basándose en las otras columnas y cuenta cuantos puestos hay.  Así que el informe se ve algo parecido a:


* ER Nurse, Nurse, Rushonga Hospital, Hospital, 3, 5
* ER Nurse, Nurse, Marjoram Hospital, Hospital, 2, 2


Mostrar una Visualización de Informe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Simplemente seleccione "Create Reports" de la página de inicio y elija el informe que desea usar.


Las Diferentes Visualizaciones
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


HTML
~~~~
Esta presenta una visualización interactiva de los datos lo cual permite limitar y clasificar los datos. Si no se ha fijado una visualización determinada para la Visualización del Informe, esta es la que se utiliza.


Limitada por Campo
------------------
Basándose en los campos que se escogieron para limitar en [[Custom Reporting -- Creating Reports]] se pueden limitar los datos mostrados en los diferentes campos en el informe. Por ejemplo, podría limitar una lista de personal según los empleados que están en una instalación específica o un distrito específico.


Clasificada por Campo
---------------------
Se puede escoger el orden de clasificación haciendo click en los encabezados de cada una de las columnas (campos).  Hacer click una vez lo cambia a orden ascendente, dos veces es orden descendente, y hacerlo una tercera vez desactiva la clasificación para ese campo. También se puede hacer click en el encabezado de una segunda columna.  Esto permitirá que la clasificación se haga con dos columnas.  Por ejemplo podría clasificar por Departamento, luego Apellido, luego Nombre.


Impresión(PDF)
~~~~~~~~~~~~~~
En esta visualización  se puede elegir ver el informe como un archivo PDF.  Se puede elegir el tamaño del papel y la orientación de la página.

Para personalizar los colores y gráficos, margen, espacios, debe modificar los datos magic (configuración) en:
 /modules/CustomReports/displays/PDF/display_options


Exportar
~~~~~~~~
En esta visualización, se pueden exportar todos los datos a un archivo.  Los tipos de archivos son:


* 'html': exporta los datos a una html
* 'csv': a `comma separated values <http://en.wikipedia.org/wiki/Comma-separated_values>`_ file.  esto es apropiado para importarse a Excel o a una base de datos.
* 'tab': a `tab separated values <http://en.wikipedia.org/wiki/Delimiter-separated_values>`_ file.   esto es apropiado para importarse a Excel o a una base de datos.


Gráfico
~~~~~~~
[[Category:Custom Reporting]][[Category:Spanish]]
