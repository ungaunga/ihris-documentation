Migrating Forms from Entry to MagicData - ES
============================================

Este tutorial explicará cómo migrar formularios de versiones previas que estaban almacenadas en la tabla de entry y moverlos a almacenamiento de datos magic; así como actualizar cualquier campo mapeado que referencie valores. Para ver un ejemplo más complicado refiérase al módulo Geography en iHRIS Common o el sub-módulo Education en el módulo Person en iHRIS Common.


Paso 1: Cambiar el Mecanismo de Almacenamiento de un Formulario
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

En iHRIS 4.0, se agregaron mecanismos de almacenamiento de datos a los formularios. El método de almacenamiento por defecto es para utilizar las tablas de entry como en las versiones previas de iJRIS. Para sistemas distribuidos es conveniente que algunos formularios se guarden en datos magic para poder manejarlos de manera centralizada más fácilmente y poder actualizarlas por medio de las actualizaciones a los módulos para mantener IDs consistentes en todos los sistemas distribuidos.

Primero debemos cambiar el almacenamiento para los formularios a datos magic en el archivo de configuración del módulo. Para versiones anteriores esta sección se debe agregar. Si desea migrar un formulario que ya tiene un almacenamiento definido, solamente debe cambiarlo a datos magic. Estos cambios estarán bajo la sección de "forms" de su configuración en la ruta: /modules/forms/forms/'''<form_name>'''.  Esto solamente incluye la nueva sección de almacenamiento. Las secciones de class y display deben estar incluidas en estos formularios. También es necesario actualizar la version para este módulo e incluir ese mismo número de versión en la sección de almacenamiento.



.. code-block:: xml

    <configurationGroup name="forms" path="/modules/forms">
      <configurationGroup name="forms">
        <configurationGroup name="form_XXXXX">
          <configuration name="storage" values="single">
            <displayName>Storage Mechanism</displayName>
            <description>The storage mechanism for this form.</description>
            <version>X.X.X</version>
            <value>magicdata</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    </configurationGroup>
    



Paso 2: Guardar Datos del Mecanismo de Almacenamiento Anterior
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ahora debemos asegurarnos de guardar datos anteriores antes de cambiar el mecanismo de almacenamiento del formulario. Por ejemplo si el campo person.nationality esta mapeado al formulario del país y este se va a mover de almacenamiento de entry a datos magic, entonces deberá guardar el valor anterior para poder cambiarlo al valor nuevo correcto una vez que se ha migrado el formulario de país. Esto se realiza utilizando el método de pre_upgrade() para la clase del módulo para el módulo dado. Un método auxiliar está en I2CE_FormStorage llamado storeMigrateData() para guardar estos datos para referencia posterior.

Deberá conocer la versión que se actualice para que solamente tenga que guardar los datos a la hora correcta para este módulo. En el ejemplo se utiliza el código "X.X.X".  También deberá determinar una ruta de migración para utilizarla para todo lo que vaya a actualizar. Esto es para que todo pueda referenciarse hacia un solo lugar posteriormente si necesita tener acceso a ello. Puede ser cualquier texto o incluso el número de la versión a la que se actualice. Debe estar bajo la ruta de datos magic de:  /I2CE/formsData/migrate_date/'''XXXXXX'''.



.. code-block:: php

    public function pre_upgrade( $old_vers, $new_vers, $new_storage ) {
        if ( I2CE_Validate::checkVersion( $old_vers, "<", "X.X.X" ) ) {
            $migrate_path = "/I2CE/formsData/migrate_data/MyUpgrade";
            I2CE_FormStorage::storeMigrateData( array( "FORM" => array( "FIELD1", "FIELD2" ) ), $migrate_path );
        }
        return parent::pre_upgrade( $old_vers, $new_vers, $new_storage );
    }
    



Paso 3: Mover Formularios al Nuevo Mecanismo de Almacenamiento y Migrar Cualquier Valor Mapeado
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ahora es necesario migrar los formularios al nuevo mecanismo y cualquier campo mapeado que se haya guardado en el paso anterior para migrar a su nueva ID. Esto puede realizarse en el método upgrade() para la clase del módulo. Hay dos métodos auxiliares en I2CE_FormStorage para ayudar en este proceso:  migrateForm() y migrateField().

Utilizará la misma ruta de migración que empleó en el método de pre_upgrade(). También necesitará crear un objeto usuario para guardar los cambios. Utilice la ID de un usuario administrativo. Puede repetir la función para cada formulario que deba migrar.



.. code-block:: php

    public function upgrade( $old_vers, $new_vers ) {
        if ( I2CE_Validate::checkVersion( $old_vers, "<", "X.X.X" ) ) {
            $user = new I2CE_User( $user_id, false, false, false );
            $migrate_path = "/I2CE/formsData/migrate_data/MyUpgrade";
    
            if ( !I2CE_FormStorage::migrateForm( "FORM", "entry", $user, $migrate_path ) ) {
                return false;
            }
            
            if ( !I2CE_FormStorage::migrateField( "FORM", array( "FIELD1" => "FIELD1_MAPPED_FORM", "FIELD2" => "FIELD2_MAPPED_FORM" ),
                    $migrate_path, $user ) ) {
                return false;
            }
        }
        return true;
    }
    



Paso 4: Revisar la Migración
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Cuando entre al sitio de nuevo ejecutará los métodos de actualización para cualquier módulo que haya actualizado. Cuando haya terminado verá los datos anteriores bajo los datos magic en la ruta: /I2CE/formsData/migrate_data/MyUpgrade (o la ruta que haya utilizado). También encontrará que los formularios ahora están guardados en datos magic bajo /I2CE/formsData/forms/.  Es recomendable que revise que todos los campos que hayan migrado utilicen la nueva ID para cada valor mapeado de manera correcta.

[[Category:Spanish]][[Category:Magic Data]]
