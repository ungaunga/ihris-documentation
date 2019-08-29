Custom Reporting -- An Overview - ES
====================================

El Custom Reporting es un proceso de tres partes:
*[[Custom Reporting -- Creating Form Relationships|Crear Una Relación de Formularios]]  Esto define la relación entre los datos en el sistema. Se creó para un usuario relativamente avanzado que tiene cierta comprensión de cómo se relacionan los datos. 
*[[Custom Reporting -- Creating Reports|Crear Un Informe]] Elegir, un relación de formulario, esto especifica los campos de datos para un informe, así como los límites permitidos para las distintas visualizaciones del informe. Fue creado para un administrador de datos. Solamente se requiere un conocimiento moderado de la forma en que los datos se relacionan en el sistema. Es en este paso que se genera las tablas de informes caché 'zebra_XXXX'.    
*[[Custom Reporting -- Creating Report Views|Crear Una Visualización del Informe]].  Fue creado para todos los usuarios que necesiten crear diferente visualización del informe. Por ejemplo, sería útil para alguien que necesite crear informes mensuales de diferentes partes de los datos.  

==Tareas==
Hay varias tareas que controlan el acceso general a la creación y la vista de los informes personalizados:
*'''custom_reports_can_access''' Permite acceso mínimo al Sistema de Informes personalizados
*'''custom_reports_delete''' Permite la eliminación de datos que definen los informes personalizados
*'''custom_reports_can_access_relationships''' Permite el acceso a las relaciones de informe personalizados
*'''custom_reports_can_access_reports''' Permite el acceso a los informes personalizados
*'''custom_reports_can_view_reportViews''' Permite la visualización de las vistas de los informes personalizados
*'''custom_reports_can_edit_reportViews''' Permite la edición de las Vistas de los Informes Personalizados
*'''custom_reports_admin''' Administrador de Informes Personalizados.  Puede realizar todas las tareas asociadas con los reportes personalizados 

In addition you may also limit acce View $view by specifying:ss to a specific Report
 /modules/CustomReports/reportViews/$view/limit_report_to
to be any valid [[Tasks and Roles#Permissions and the Permission Parser|permission]] string.

[[Category:Custom Reporting]][[Category:Spanish]]
