Adding Form and Field Validations - ES
======================================

Al editar un formulario en iHRIS, este puede realizar validaciones a los datos. Por ejemplo, puede marcar un campo como requerido o único. También puede utilizar una lógica más complicada para verificar que está establecida correctamente. Por ejemplo, que la fecha de inicio de un puesto no se da después de la fecha de finalización. Este artículo describe cómo agregar validaciones personalizadas para formularios y campos.

Este documento se refiere a iHRIS 4.0.9 y posteriores.

En algunos casos podría necesitar validaciones adicionales en formularios y campos que ya existen o agregar validaciones a campos y formularios nuevos que este creando. Esto puede hacerlo utilizando ganchos en el módulo de su sitio en el módulo de personalización de formularios y campos que ha creado.

Puede agregar una validación a un solo campo o hacer el formulario completo para comparar múltiples campos. El primer paso es crear los ganchos en la clase del módulo.  

Crear la Clase del Módulo
^^^^^^^^^^^^^^^^^^^^^^^^^

Puede crear ganchos en el código de clase de su módulo. Este archivo estará en la ruta de clases (usually ./lib) de su módulo.

Agregar una Clase del Módulo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Si su módulo actualmente no tiene una clase tendrá que agregar una. Puede agregar el nodo className al archivo de configuración de metadata en su módulo (o sitio).

.. code-block:: xml

        <className>iHRIS_Module_$moduleName</className>
    

Reemplazaría  **$moduleName**  con un nombre único para su clase del módulo.  Por ejemplo en el módulo  Person Position  de iHRIS Manage, se utiliza la clase siguiente:

.. code-block:: xml

      <metadata>
        <displayName>iHRIS Manage Person Position</displayName>
        <className>iHRIS_Module_PersonPosition</className>
        ...
      </metadata>
    

Cree el Archivo de Clase PHP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Luego en el directorio de clases del módulo (./lib) crearía el archivo iHRIS_Module_'''$moduleName'''.php, reemplazando **$moduleName**  con el nombre de clase que puso en el archivo de configuración.

.. code-block:: bash

    gedit ./lib/iHRIS_Module_$moduleName.php
    

Debería llenar todos los comentarios adicionales, excepto el archivo en blanco por defecto (el que llenaremos después).

.. code-block:: php

    /**
     * Class iHRIS_Module_$moduleName
     *
     * @access public
     */
    class iHRIS_Module_$moduleName extends I2CE_Module {
    
    }
    # Local Variables:
    # mode: php
    # c-default-style: "bsd"
    # indent-tabs-mode: nil
    # c-basic-offset: 4
    # End:
    

Agregar el Método getHooks
~~~~~~~~~~~~~~~~~~~~~~~~~~
Ahora tenemos que definir en método getHooks que le dice al módulo factory que se engancha al módulo de apoyo.  Si su módulo ya posee una clase entonces solo tendrá que agregar el método getHooks al código existente.  Si ya tiene el método getHooks entonces salte este paso y vaya a [#Adding the Hooks| Agregar los Ganchos]].

.. code-block:: php

    class iHRIS_Module_$moduleName extends I2CE_Module {
    
        /**
         * Return the array of hooks available in this module.
         * @return array
         */
        public static function getHooks() {
            return array(
                   );
        }
    
    }
    

Esto simplemente es un dato temporal hasta que agreguemos los ganchos reales que queremos definir. Esos irán en la colección que regresa.

Agregar los Ganchos
^^^^^^^^^^^^^^^^^^^

Hay dos tipos d ganchos que se pueden agregar.  Una validación de campo (para un campo) y una validación de formulario (para múltiples campos).

Agregar un Gancho de Validación de Campo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para ganchos de campo, utilice los nombres de formulario y campos:  valdate_form_'''$form'''_field_'''$field'''.  Reemplace **$form**  y **$field** .  Por ejemplo el módulo Person Contact  de iHRIS Common agrega un gancho de validación para el campo de contacto de correo electrónico como:  validate_form_'''contact'''_field_'''email'''.  Ahora agregamos este gancho al método  getHooks como colección asociativa con el valor siendo el método en la clase del módulo a ser llamado para validar el campo.  El nombre del método puede ser cualquiera, para ser claros usamos el mismo nombre que en el gancho.

También creamos este método para que pueda ser llamado por el módulo factory cuando el gancho sea llamado.  Se necesita solo un objeto de formulario de campo como argumento.

.. code-block:: php

        public static function getHooks() {
            return array(
                   'validate_form_$form_field_$field' => 'validate_form_$form_field_$field',
                   );
        }
    
        /**
         * Validate the $field in the $form form.
         * @param I2CE_FormField $formfield
         */
        public function validate_form_$form_field_$field( $formfield ) {
        }
    

En este método realizara cualquier chequeo necesario y si falla tendrá que llamar setInvalidMessage en el $formfield.  Vea el [[Using Translateable Invalid Messages]] para saber cómo definir los mensajes de manera que se permitan traducciones variadas. Esta es la función de ejemplo del módulo Person Contact de iHRIS Common.

.. code-block:: php

        /** 
         * Validate the email field for contact forms.
         * @param I2CE_FormField $formfield
         */
        public function validate_form_contact_field_email( $formfield ) { 
            $value = $formfield->getValue();
            if ( I2CE_Validate::checkString( $value ) 
                    && !I2CE_Validate::checkEmail( $value ) ) { 
                $formfield->setInvalidMessage('invalid_email');
            }   
        }   
    

Agregar un Gancho de Validación de Formulario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Agregar un gancho de validación para un formulario es muy similar a agregar un gancho de validación para un campo.  El nombre del gancho será   validate_form_'''$form'''.  Remplaza **$form**  nombre del formulario que desea validar.  Por ejemplo, el formulario person_position tiene un gancho de validación llamado:  validate_form_'''person_position'''.  Se agrega este gancho al método getHooks igual que para una validación de campo.  El método necesita que se valide un solo argumento del formulario.

.. code-block:: php

        public static function getHooks() {
            return array(
                   'validate_form_$form' => 'validate_form_$form',
                   );
        }
    
        /**
         * Validate the $form form.
         * @param I2CE_Form $form
         */
        public function validate_form_$form( $form ) {
        }
    

En este método puede revisar los valores de múltiples campos y llamar setInvalidMessage para cualquier campo que no valide.  Vea el [[Using Translateable Invalid Messages]] para saber cómo definir los mensajes de manera que se permitan traducciones variadas. Esto es un ejemplo del módulo Person Position de iHRIS Manage que valida el formulario person_position al comparar la fecha de inicio y la fecha de finalización para asegurarse que la fecha de finalización sea después de la fecha de inicio.

.. code-block:: php

        /**
         * Checks to make sure the end date is after the start date for the person position.
         * @param I2CE_Form $form
         */
        public function validate_form_person_position( $form ) {
            if ( $form->start_date->isValid() && $form->end_date->isValid() ) {
                if ( $form->start_date->compare( $form->end_date ) < 1 ) {
                    $form->setInvalidMessage('end_date','bad_date');
                }
            }
         }
    

