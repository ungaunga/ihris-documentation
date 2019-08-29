Custom Reporting -- Search Reports - ES
=======================================

La página de búsqueda utiliza el módulo custom reporting para permitirle personalizar fácilmente la página de búsqueda y agregar nuevas búsquedas al sistema. Esto es un proceso de dos pasos:

* [[#Creating A Search Report | Creating A Search Report]]
* [[#Registering A Report With The Search Page | Registering A Report With The Search Page]]

Crear un Informe de Búsqueda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Debería crear una visualización de informe que desee usar para la página de búsqueda. Debería incluir todos los campos que desee y límites que necesite. También puede modificar la visualización de informe existente en el sistema, tal como "Search People" para ajustar los campos que se muestran.    Puede que quiera ver [[Custom Reporting -- Creating a Staff List Example | create a staff list]].  

Algo que debe tener en mente, es que debe agregar el link apropiado a los campos en este informe, por ejemplo agregar el link "view?id=" a cualquiera de los campos en el formulario person le permitirá vincular la página de visualización de esa persona.

Puede modificar los informes de búsqueda existentes para que se adapten a sus necesidades. Por ejemplo, puede que quiera adjuntar el formulario "id" al formulario person y limitar el formulario "id" al número de "national identification" si tiene algo como eso.  Luego en el informe, puede agregar un límite para buscar por el número de national identification.

Registrar un Informe con la Página de Búsqueda
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

la registración de una visualización de informe se hace al definir datos magic bajo:
 /modules/CustomReports/search_reports

Vea  ` lines 511-525 <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.0-dev/view/623/iHRIS-Manage-Configuration.xml#L511>`_  del archivo de configuración iHRIS Manage para un ejemplo de como las visualizaciones de informe de **search_people**  y  **position_list**  son registradas con la página de búsqueda.  El resultado es lo siguiente:

* /moudles/CustomReports/search_reports:  Requiere nodo primario.  Todas las visualizaciones de informe que están vinculadas a la página de búsqueda necesitan ser registrados aquí
* *search_people:  Requiere nodo primario.  Este es el nombre de la visualización de informe que desea registrar bajo la página de búsqueda. Aquí la visualización del informe es "search_people"
* **name: Requiere nodo escalar.  Este es el nombre de la búsqueda a como aparece en la página de búsqueda. En este caso es "Search People"
* **description: Requiere nodo escalar.  Estas son las instrucciones que se muestran en esta búsqueda.  En este caso es en "Locate any person's record in the system to review, print or update."
* *position_list:  Requiere nodo primario.  Éste es el nombre de la visualización de informe que desea registrar bajo la página de búsqueda. Aquí la visualización de reporte es "position_list"
* **name: Requiere nodo escalar.  Éste es el nombre de la búsqueda a como aparece en la página de búsqueda.  En este caso es en "Search Positions"
* **description: Requiere nodo escalar.  estas son las instrucciones que aparecen en esta búsqueda.  En éste caso es en "Locate any position in the system to review, print or update."

