Printed Forms with Reports (ODT) - ES
=====================================

El módulo de formularios impresos se utiliza para imprimir formularios "standardized" u "official" basados en los informes en el sistema.  Por ejemplo, puede ser el número de registro de una enfermera. Será exportado como un Documento de Open Office. Este documento puede fácilmente ser leído en Microsoft Word 2003.

Dependiendo de lo que necesite, puede que desee ver estos otros métodos para la creación de formularios estandarizados:


* [[Printed Forms]]
* [[Printed Forms form Relationships (ODT)]]
* [[Standardized Letters (ODT)]]



¿Qué son los Formularios Impresos?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los Formularios Impresos permiten crear una plantilla de OpenDocument Text (ODT) que pude llenarse con los datos del informe.  Esto está basado en [[Standardized Letters (ODT)|Standardized Letters]] que pueden utilizarse para un registro individual.


Agregar un Formulario Impreso a una Visualización de Informe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Hay dos pasos para agregar un formulario impreso a una visualización de informe. Primero debe crear el archivo plantilla, luego crear un módulo con el archivo de plantilla y la configuración para a visualización de informe. Por ejemplo, puede buscar SampleStaffPrintedForm en el módulo de directorio de iHRIS Manage demo site.

Crear una Plantilla ODT
~~~~~~~~~~~~~~~~~~~~~~~

El archivo plantilla necesita datos temporales para los campos que desee mostrar. También existen otros datos temporales para datos especiales. Todos los datos temporales se aplicaran al resultado final. Todos los datos temporales se encuentran rodeados de **{{{**  and **}}}** .  Cualquier formato que se le aplique al dato temporal será aplicado el resultado final. También debe señalar donde está el bloque de texto que desea repetir para cada fila de la base de datos. Rodeará este bloque con **[!-- BEGIN report_row --]**  y **[!--END report_row --]** .  Vea más adelante para los detalles para utilizar una tabla para su resultado final.

Aquí se encuentran los datos temporales que se pueden utilizar en el informe. Datos temporales especiales inician con **++** .  Los datos temporales coinciden con el nombre **form+field**  en la visualización de informe.  Los datos temporales de encabezados pueden ser utilizados es cualquier lugar del documento.  Algunos aplican sólo dentro o fuera del loop para el informe.

{| border="1" cellspacing="0" cellpadding="5" align="center"
! Dato Temporal
! Aplica
! Descripción
|- 
| {{{++report_title}}}
| Loop Fila Externa 
| El título del informe.
|-
| {{{++report_description}}}
| Loop Fila Externa
| La descripción del informe.
|-
| {{{++report_limit}}}
| Loop Fila Externa
| Los límites de informe seleccionados cuando este informe fue creado.
|-
| {{{++user_name}}}
| Loop Fila Externa
| El nombre de usuario del usuario que creó este informe.
|-
| {{{++time}}}
| Loop Fila Externa
| La hora en la que el informe fue ejecutado.
|-
| {{{++header+'''form+field'''}}}
| Cualquiera
| El encabezado del campo específico.
|-
| {{{++row_num}}}
| Inside Row Loop
| El número de fila actual del registro.
|-
| {{{'''form+field'''}}}
| Loop Fila Interna
| El valor del campo específico en la visualización de informe.
|-
| {{{'''form+field+width=2.0in,maxheight=3.0in}}}
| Loop Fila Interna
| Si el campo del formulario es una imagen, puede brindarse información extra para el ajuste de las dimensiones.
|-
| {{{'''++limit+form+mapfield'''}
| Inside Row Loop
| Sí se ha puesto un límite para uno de los formularios es este informe a través de un MAP field, entonces este será el nombre de formulario al que el mapfield se mapee  que se mostrará.
|-
| {{{'''++limit+form+mapfield+field'''}
| Loop Fila Interna
| Sí se ha puesto un límite para uno de los formularios es este informe a través de un MAP field, entonces este será valor del campo al que el mapfield se mapee  que se mostrará.
|}

Este es el ejemplo para el mismo módulo. Puede descargar el  `source file <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/download/head:/staffform.odt-20120126055155-qjun6vhyfw79qnhf-4/StaffForm.odt>`_  de esto para ver el formato.


.. code-block::

    {{{++report_title}}}
    {{{++report_description}}}
    {{{++report_limit}}}
    Report printed by {{{++user_name}}} at {{{++time}}}.
    [!-- BEGIN report_row --]
    {{{++row_num}}}. {{{person+surname}}}, {{{person+firstname}}}
    {{{++header+facility+name}}}: {{{facility+name}}}			{{{++header+work+telephone}}}: {{{work+telephone}}}
    {{{++header+position+title}}}: {{{position+title}}}			{{{++header+work+email}}}: {{{work+email}}}
    {{{++header+department+name}}}: {{{department+name}}}
    
    [!-- END report_row --]
    


Cuando desee repetir una fila de una tabla para las filas de su informe, deberá cambiar las oraciones de BEGIN y END a **[!-- BEGIN row.report_row --]**  y **[!-- END row.report_row --]** .  Vea el  `table example <http://bazaar.launchpad.net/~intrahealth+informatics/ihris-manage/4.1-dev/download/head:/stafftableform.odt-20120126055155-qjun6vhyfw79qnhf-5/StaffTableForm.odt>`_  del módulo de muestra.  El ejemplo siguiente ha sido recortado debido al espacio.

{| border="1" cellspacing="0" cellpadding="5" align="center"
! #
! {{{++header+person+surname}}}
! {{{++header+person+firstname}}}
! {{{++header+work+email}}}
|-
| [!-- BEGIN row.report_row --]{{{++row_num}}}
| {{{person+surname}}}
| {{{person+firstname}}}
| {{{work+email}}}[!-- END row.report_row --]
|}


Creando el Módulo
~~~~~~~~~~~~~~~~~

Una vez que haya creado el archivo de plantilla ODT, necesitará crear un módulo para poner en la fila y configurar los formularios impresos para su informe.  El módulo necesita un directorio odt_templates donde se pone el archivo ODT al igual que el archivo de configuración del módulo.  Debería requerir el módulo CustomReports-PrintedReportsODT para que el botón *Forms Print*  aparezca en la visualización de su informe.

Para su archivo de configuración, necesitará crear un nodo bajo la visualización del informe al que aplica esta plantilla.  Todos los campos que utilice en la plantilla deben estar habilitados en la visualización de informe. Los nodos **printed_forms**  deberán estar en el nivel superior de su visualización de informe y luego un nombre único para le plantilla de formulario impreso.  Abajo de eso necesita definir el **template**  que es el nombre del archivo de plantilla en el directorio odt_templates y **displayName**  para lo que aparece cuando el usuario desee ver esta plantilla.  La configuración para el módulo de muestra está más adelante con dos formularios impresos definidos.  Esta muestra también requiere el módulo ihris-manage-CustomReports-staff-reports ya que ahí está definida la visualización del informe staff_directory.



.. code-block:: xml

    <?xml version="1.0"?>
    <!DOCTYPE I2CEConfiguration SYSTEM "I2CE_Configuration.dtd">
    <I2CEConfiguration name="sample-staff-list-printed-form">
      <metadata>
        <displayName>Sample Staff Printed Forms</displayName>
        <description>Sample staff printed forms generated from the staff_directory report view.</description>
        <requirement name="ihris-manage-CustomReports-staff-reports">
          <atLeast version="4.1" />
          <lessThan version="4.2" />
        </requirement>
        <requirement name="CustomReports-PrintedReportsODT">
          <atLeast version="4.1" />
          <lessThan version="4.2" />
        </requirement>
        <path name="odt_templates">
          <value>./odt_templates</value>
        </path>
      </metadata>
      <configurationGroup name="sample-staff-list-printed-form"     
                          path="/modules/CustomReports/reportViews/staff_directory/printed_forms">
        <configurationGroup name="staff_form">
          <configuration name="template">
            <value>StaffForm.odt</value>
          </configuration>
          <configuration name="displayName" locale="en_US">
            <value>Staff Form</value>
          </configuration>
        </configurationGroup>
        <configurationGroup name="staff_table">
          <configuration name="template">
            <value>StaffTableForm.odt</value>
          </configuration>
          <configuration name="displayName" locale="en_US">
            <value>Staff Table</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    </I2CEConfiguration>
    


[[Category:Standardized Forms]][[Category:Custom Reporting]][[Category:Spanish]]
