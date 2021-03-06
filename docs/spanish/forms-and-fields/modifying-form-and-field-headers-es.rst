Modifying Form and Field Headers - ES
=====================================

Encabezados de Campo
^^^^^^^^^^^^^^^^^^^^
Puede personalizar los encabezados de campo de un formulario de campo al actualizar los datos magic asociados con los encabezados.  Puede hacer esto a través del navegado de datos magic, pero la mejor manera es hacer el cambio en un módulo para su sitio o en el archivo de configuración de su sitio.  Los encabezados se encuentran en la localidad de datos magic:  /modules/forms/formClasses/'''$formClass'''/fields/'''$field'''/headers/'''$headerType'''

En su sitio en su archivo de configuración de modulo, puede cambiar los encabezados al agregar las líneas siguientes:

.. code-block:: xml

    <configuration name="custom_headers" path="/modules/forms/formClasses/$formClass/fields/$field/headers/$headerType" locale="en_US">
      <value>$newHeader</value>
    </configuration>
    

Por ejemplo, para cambiar el encabezado de campo de region en los distritos puede hacer esto:

.. code-block:: xml

    <configuration name="region_header" path="/modules/forms/formClasses/iHRIS_District/fields/region/headers/default" locale="en_US">
      <value>State</value>
    </configuration>
    

En la mayoría de los casos utilizará el "default" como el **$headerType** .  Si quiere tener múltiples encabezados, entonces cambie el tipo de encabezado y en la plantilla que muestra su campo ponga el **$headerType**  como el valor para el atributo principal.

.. code-block:: html

    <span type="form" name="$form:$field" showhead="$headerType"></span>
    

Reemplace $form, $field y $headerType con los valores apropiados para su plantilla.  Por ejemplo:

.. code-block:: html

    <span type="form" name="country:name" showhead="my_header"></span>
    

Nombres Mostrados de Formularios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
También puede que quiera cambiar el nombre mostrado asociado con un formulario. Puede hacer esto cambiando los datos magic en /modules/forms/forms/'''$form'''/display.  Puede hacer este cambio en su sitio o archivo de configuración de módulo.

.. code-block:: xml

    <configuration name="form_display" path="/modules/forms/forms/$form/display" locale="en_US">
      <value>$newHeader</value>
    </configuration>
    

Por ejemplo, para cambiar el nombre mostrado de región para que sea Estado:

.. code-block:: xml

    <configuration name="region_display" path="/modules/forms/forms/region/display" locale="en_US">
      <value>State</value>
    </configuration>
    

Algunas plantillas (como lists.html) se pueden hacer referencia al nombre en la plantilla directamente. También tendrá que modificar esta plantilla para usar el nombre que desea cuando vincule para la edición de las listas de la base de datos de ese formulario.

Ejemplo de Geografía
^^^^^^^^^^^^^^^^^^^^
Aquí hay un ejemplo completo que puede agregar al archivo [[Module Structure#Module Configuration File|configuration]] .xml de su sitio.  Cambiará los nombres de los niveles de geografía a Country/State/Council/Town or City.  Country permanecerá igual, region se convertirá en State, district se convertirá en Council y county se convertirá en Town or City.  Necesitará cambiar la **<version>4.0.XXX</version>**  como sea apropiado (vea [[Configuration (Magic) Data#<version> | versions]]).

.. code-block:: xml

    <configurationGroup name="forms_module" path="/modules/forms">
      <!-- Update display names for forms -->
      <version>4.0.XXX</version>
      <configurationGroup name="forms">
        <configuration name="region_display" path="region/display" locale="en_US">
          <value>State</value>
        </configuration>
        <configuration name="district_display" path="district/display" locale="en_US">
          <value>Council</value>
        </configuration>
        <configuration name="region_display" path="county/display" locale="en_US">
          <value>Town or City</value>
        </configuration>    
      </configurationGroup>
      <!-- Update field headers for formClasses -->
      <configurationGroup name="formClasses">
        <configuration name="district_region_header" path="iHRIS_District/fields/region/headers/default" locale="en_US">
          <value>State</value>
        </configuration>
        <configuration name="country_district_header" path="iHRIS_County/fields/district/headers/default" locale="en_US">
          <value>Council</value>
        </configuration>
      </configurationGroup>
    </configurationGroup>
    
    

Editar lists.html
^^^^^^^^^^^^^^^^^
Como se mencionó anteriormente, algunos archivos de plantilla .html hacen referencia al nombre del formulario directamente y deberán editarse.  Va a querer copiar las lists.html existentes del módulo iHRIS Manage (o iHRIS Qualify) al directorio de plantillas en el módulo de su sitio. Luego editará esta copia nueva. Por ejemplo:
 sudo mkdir -p /var/lib/iHRIS/sites/'''my_site'''/templates/en_US
 sudo cp /var/lib/iHRIS/lib/'''4.0.4'''/ihris-manage/templates/en_US/lists.html /var/lib/iHRIS/sites/'''my_site'''/templates/en_US
 sudo gedit /var/lib/iHRIS/sites/'''my_site'''/templates/en_US
donde reemplace **4.0.4**  con la version apropiada y **my_site**  con el nombre del directorio donde está guardado su sitio.  

Una vez que gedit aparezca, tendrá que cambiar los nombres de los formularios. Por ejemplo:

.. code-block:: xml

      <li task="can_edit_database_list_county"><a href="lists?type=county&amp;field=district">County</a></li>
    

se convierte en:

.. code-block:: xml

     <li task="can_edit_database_list_county"><a href="lists?type=county&amp;field=district">Town or City</a></li>
    
    

Modifying Form and Field Headers

Este tutorial explicará cómo modificar el archive de configuración de su sitio para cambiar los encabezados predeterminados para los formularios y campos de su sitio.  Todos estos datos están almacenados en las opciones de configuración (datos magic).  Para este ejemplo vamos a cambiar los encabezados de County para que en lugar de eso muestren Sub-District.

Paso 1: Cambiar el nombre de formulario mostrado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Primero tenemos que cambiar el nombre mostrado de este formulario. Si tiene una sección de formularios en el archivo de configuración de su sitio puede agregar esta sección ahí. O utilizando el atributo de ruta puede agregar el configurationGroup al nivel superior de su configuración de sitio.

.. code-block:: xml

    <configuration name='county_display' values='single' path='/modules/forms/forms/county/display'>
      <displayName>Display Name</displayName>
      <description>The display name for this form.</description>
      <status>overwrite:true</status>
      <value>Sub-District</value>
    </configuration>
    

Paso 2: Anular los encabezados de campo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ahora necesitamos anular los encabezados de campo predeterminados de todos los formularios de clase que utilizan county.  Si tiene formularios personalizados también tendría que incluirlos aquí.

.. code-block:: xml

    <configurationGroup name='formClasses' path='/modules/forms/formClasses'>
      <status>overwrite:true</status>
    
      <configurationGroup name='iHRIS_ListByCountry'>
        <configuration name="county_headers" path="fields/county/headers/default">
          <value>Sub-District</value>
        </configuration>
      </configurationGroup>
    
      <configurationGroup name='iHRIS_County'>
        <configurationGroup name='fields'>
          <configuration name="country_headers" path="country/headers" type="delimited" values="many">
            <value>select_county:Select Country, Region, District then Sub-District</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    
      <configurationGroup name="iHRIS_Person">
        <configuration name="res_count_headers" path="fields/residence_county/headers/default">
          <value>Residence Sub-District</value>
        </configuration>
      </configurationGroup>
    
    </configurationGroup>
    

Paso 3: Modificar la plantilla de Base de Datos Administrador
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Copie el archivo lists.html de iHRIS Manage o iHRIS Qualify al directorio de plantillas de su sitio.  Edite la línea en la sección Geography para cambiar el texto vinculado a Sub-District en lugar de County.  No cambie el tipo de atributo en el href porque el nombre del formulario sigue siendo county.  Solo se ha cambiado lo que se ve en pantalla.  Ahora copie lists_county.html de los módulos plantilla de Geography del iHRIS Common al directorio de plantillas de su sitio.  Cambie el link que dice "Add new County"  a "Add new Sub-District."

Paso 4: Recargue su sitio
^^^^^^^^^^^^^^^^^^^^^^^^^

Ahora los encabezados de formularios y campos deberían estar cambiados.

