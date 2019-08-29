Printed Forms - ES
==================

Este tutorial describe como crear formularios "standardized" u "official" en PDF en base a los datos del sistema. Esto puede ser útil para generar certificados de capacitación, cartas de formularios en un cambio de puesto o validar quién trabaja en las instalaciones o en el distrito.

Este módulo primero aparece en la versión 4.0.5 de la Suite iHRIS.

Dependiendo de sus necesidades, podría querer ver estos otros métodos para la generación de formularios estandarizados:


* [[Printed Forms form Relationships (ODT)]]
* [[Standardized Letters (ODT)]]
* [[Printed Forms with Reports (ODT)]]


Datos Fuente
^^^^^^^^^^^^
Los datos fuente para el formulario impreso estarán basados en una [[Custom Reporting -- Creating Form Relationships|Relación de Formularios]].


Interacción de Páginas
^^^^^^^^^^^^^^^^^^^^^^

Imprimir
~~~~~~~~
En la primera fase de este módulo, la única interacción es para producir los formularios impresos en base a lo que se ha guardado en los [[#Magic Data Details|datos magic]].  No habrá un componente de "document design" .  Se podrá tener acceso al formulario estándar a través de un URL con el nombre del formulario estandarizado y una variable GET/POST que contenga una o más de las id del formulario primario en la relación. Por ejemplo:
 http://'''<SITE_URL>'''/PrintedForms/print/'''registration'''?ids[]=person|12&ids[]=person|14&ids=[]person|22

Utilizar este URL causaría lo siguiente:


* verificar que existe un formulario estandarizado llamado **registration**
* verificar que el usuario tiene los permisos apropiados para ver este formulario estandarizado:
* *Revisar si el usuario tiene la tarea 'printed_forms_all_generate''''
* *Si no, revisar si la tarea 'printed_forms_generate_'''registration'''' existe y el usuario tiene esta tarea
* para cada id, *person|12* , *person|14* , *person|22*  llenar los detalles del informe estandarizado utilizando las filas correspondientes en la tabla de informes si existe (ver abajo).


Menú
~~~~

Es posible ver cuales formularios se pueden generar para una id dada haciendo el siguiente llamado
 http://'''<SITE_URL>'''/PrintedForms/menu?id=person|12
mostrará todos los formularios impresos cuyo formulario primario es person.  Entonces para cada uno de estos tendrá un link a la página de impresión correspondiente.  

También debe vincular a la página de archivo correspondiente y mostrar cuales formularios en PDF ya se han archivado para esa persona, clasificados por tipo y fecha.


Archivo
~~~~~~~
También debe crear un formulario, por ejemplo *generated_doc*  que contenga los siguientes campos:


* document: Un campo binario que contendrá el PDF
* date: la fecha en la que fue generado
* type: el formulario standard impreso (es decir, registro en el ejemplo anterior)
Al llamar a la página de archivo como:
 http://'''<SITE_URL>'''/PrintedForms/archive/'''registration'''?ids[]=person|12&ids[]=person|14&ids=[]person|22
Se ejecutará lo siguiente:


* revisar si 'generated_form' es un formulario secundario de person.  Si no, la ejecución se detiene.
* para cada id crear el formulario PDF (solo uno en cada página/documento) y guardarlo como un formulario secundario *generated_doc*


Detalles de Datos Magic
^^^^^^^^^^^^^^^^^^^^^^^
Todos los formularios estandarizados se guardarán en el nodo de datos magic:
 /modules/PrintedForms/forms
En el ejemplo anterior los detalles que definen el formulario de registro se guardarían bajo:
 /modules/PrintedForms/forms/registration

Los detalles de un formulario específico son los siguientes (todas las medidas son en mm):


* relationship: Nodo escalar requerido. El nombre de la relación de formulario en la que se basa este formulario. Debe ser el nombre de un nodo secundario de */modules/CustomReports/relationships*
* displayName: Nodo escalar opcional.  El nombre de la carta impresa como se muestra al usuario final.
* archive: Nodo escalar opcional.  Si se ha establecido, debe ser un formulario nombrado en la relación. Si es un formulario de nombre válido, entonces permitirá el almacenamiento de esta carta impresa como un formulario secundario del formulario nombrado correspondiente. Debe asegurarse que este formulario tiene un *generated_doc*  como un [[Defining Forms | formulario secundario]] válido.
* layout_details: Nodo primario opcional que describe los detalles de la diagramación de la página. Contiene los siguientes nodos secundarios.
* *encoding:  Nodo escalar opcional. La codificación utilizada por el renderer(PDF). Por defecto es ASCII
* *hyphenation_file: Nodo escalar opcional.  Archivo utilizado para la separación. Por defecto en hyph_en_US.dic'
* *orientation:  Nodo escalar opcional.  Por defecto a 'P' de portrait.  La otra opción es 'L' de landscape
* *size: Nodo escalar opcional. Por defecto 'A4' para describir el papel que se utilizará. Debe ser uno de los tamaños de papel ISO 216 estándar, es decir 'A4', o uno de los tamaños de papel Norteamericanos como 'carta' o 'legal'
* *rows:  Nodo escalar opciones:  Por defecto 1.  El número de filas de formularios a imprimir en una página.
* *cols:  Nodo escalar opcional:  Por defecto 1.  El número de columnas de formularios a imprimir en la página.
* *border: Nodo escalar opcional.  Por defecto 0 si las filas y columnas son 1, de lo contrario por defecto es 1.  El ancho del borde dibujado alrededor de los formularios.
* *vert_pad: Nodo escalar opcional. Por defecto 10.  El espacio vertical utilizado en el límite de la página
* *horiz_pad: Nodo escalar opcional. Por defecto 10.  El espacio horizontal utilizado en el límite de la página
* *vert_pad_border: Por defecto 0. El espacio vertical utilizado entre formularios
* *horiz_pad_border: Por defecto 0. El espacio vertical utilizado entre formularios
* text_properties: Un nodo primario opcional que define las propiedades de texto por defecto de los tipos de elementos en el documento.  Los nombres de los nodos secundarios son los nombres de los tipos de elementos (imagen o texto).  Los valores posibles son:
* *font:  Nodo escalar opcional.  Por defecto helvética.  Debe limitarse a uno de los tipos de letra standard de pdf: times, helvética, courier
* *size: Nodo entero positive opcional. Tamaño en puntos de tipo de letra. Por defecto 12.
* *alignment: Nodo escalar opcional.  Por defecto 'L' por left.  Puede ser 'R' o 'J', 'L' o 'C'
* *color: Color opcional del primer plano/texto . Utiliza colores estilo html hex .  Por defecto negro #000000 ,
* *bg_color: Color opcional de fondo. Utiliza colores estilo html hex .  Por defecto  'none' para transparente.
* *style: Nodo escalar opcional.  Por defecto ninguno.  Puede contener cualquiera de los siguientes caracteres, N de Negrita, S de subrayado , K para cursiva
* elements: Nodo primario. Los secundarios Deben tener un índice numérico.  Los elementos se agregan al document estándar en orden numérico ascendente del nombre del nodo del elemento.  Cada nodo secundario contendrá lo siguiente:
* *text_properties: Un nodo primario opcional que define las propiedades que aplican a este nodo y a todos los sub-elementos de este. La definición es la misma que la anterior.
* *type: Nodo escalar requerido.  Debe ser 'text' 'image' o 'value'
* *definition:  Depende del tipo.  Ver abajo.


Definición del tipo: Texto
~~~~~~~~~~~~~~~~~~~~~~~~~~
El elemento del texto es determinado texto a ubicarse en el documento. Debe consistir de los siguientes nodos:


* printf:  Nodo escalar opcional . La cadena printf debe ubicarse aquí.  Por defecto ''.  Ejemplo: "%s, %s has registration number %s"
* printf_args:  Nodo primario opcional .  Un arreglo de argumentos a sustituirse en el printf de la siguiente manera
* *'''formname'''+'''field''': un informe de campos de formularios a sustituirse en el printf.  E.g. "person+surname,person+fisrtname,registation+number":
* *+'''relationshipFunction''':  La evaluación de la función nombrada función en la relación del formulario.  Ejemplo +age65 cuál será el año en que la persona cumpla 65 años en la relación de personal
* *++date('''XYZ'''): Los datos formateados de acuerdo a **XYZ**   (sin comillas) usando las funciones  `strfrtime <http://us2.php.net/manual/en/function.strftime.php>`_  .  Ejemplo ++date(%Y) es el año de cuatro dígitos
* *++date:  La fecha.  Este es el mismo de  ++date(%x).
* *++user:  El nombre del usuario que imprime el formulario
* *++eval('''XYZ'''):  Evaluar el código php **XYZ** .  Ejemplo  ++eval(strftime("%Y")+60)  añadiría 60 al año actual
* horiz_min:  nodo escalar numérico requerido. Si la alineación es 'L' es la coordenada que está más a la izquierda para ubicar el texto. Si la alineación es  'R' es la coordenada que está más a la izquierda del texto
* horiz_max: Nodo escalar numérico. Si no está establecido y la alineación es 'J' entonces la alineación se revierte a 'L'.    Si está establecida y la alineación es 'L' es la coordenada que está más a la derecha.  Si está establecida y la alineación es 'R' entonces es la coordenada que está más a la izquierda.  Si está establecida y la alineación es 'J' entonces es la coordenada que está más a la derecha y *horiz-min*  es la coordenada que está más a la izquierda.
* vert_max: Optional numeric scalar node.  La coordenada que está más al fondo para ubicar el texto.
* vert_min: Valor escalar numérico requerido.   La coordenada de más arriba para ubicar el texto.


Definición del Tipo: Imagen
~~~~~~~~~~~~~~~~~~~~~~~~~~~


* image: Nodo standard Requerido. El nombre del archivo de imagen a ubicar. Puede ser:
* *Un nombre de archivo, en cual caso la ruta de búsqueda utilizada es "PDF_IMAGES"
* *Una cadena "form://'''form+field'''"  donde el formulario se nombra form en la relación y el campo es un campo de tiempo IMAGE (e.g. "form://passport+image")
* horiz_min:  Nodo escalar numérico requerido. El de más a la izquierda coordina para ubicar la imagen.
* vert_min: Nodo escalar numérico requerido.  El de más arriba coordina para ubicar la imagen
* horiz_max:  Nodo escalar numérico opcional. El de más a la derecha coordina para ubicar la imagen.  Si está establecido, la imagen se re-escala si es necesario.
* vert_max: Nodo escalar numérico opcional.  El de más abajo coordina para ubicar la imagen.   Si está establecido, la imagen se rescala si es necesario.


Ejemplo
^^^^^^^

Definir las características del Formulario Impreso
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Por ejemplo, para producir una Staff Hire Letter en iHRIS Manage podría definirla como:


.. code-block:: xml

      <configurationGroup name="sample-hire-letter" path="/modules/PrintedForms/forms/sample_hire_letter">
        <configuration name="relationship">
          <value>staff</value>
        </configuration>
        <configuration name="archive">
          <value>person</value>
        </configuration>
        <configuration name="displayName">
          <value>Staff Hire Letter</value>
        </configuration>
        <configurationGroup name="elements">
          <configurationGroup name="0">
            <configuration name="type">
              <value>image</value>
            </configuration>
            <configuration name="definition" values='many' type='delimited'>
              <value>image:iHRISManage_logo_whiteBG.png</value>
              <value>horiz_min:5</value>
              <value>vert_min:1</value>
            </configuration>
          </configurationGroup>
          <configurationGroup name="50">
            <configuration name="type">
              <value>text</value>
            </configuration>
            <configuration name="text_properties" values='many' type='delimited'>
              <value>style:I</value>
            </configuration>
            <configuration name="definition" values='many' type='delimited'>
              <value>horiz_min:33</value>
              <value>vert_min:6</value>
              <value>printf:Certification of Employment</value>
            </configuration>
          </configurationGroup>
          <configurationGroup name="51">
            <configuration name="type">
              <value>text</value>
            </configuration>
            <configuration name="text_properties" values='many' type='delimited'>
              <value>style:BU</value>
            </configuration>
            <configuration name="definition" values='many' type='delimited'>
              <value>horiz_min:33</value>
              <value>vert_min:12</value>
              <value>printf:Ministry of Health</value>
            </configuration>
          </configurationGroup>
    
          <configurationGroup name="52">
            <configuration name="type">
              <value>text</value>
            </configuration>
            <configuration name="definition" values='many' type='delimited'>
              <value>horiz_min:160</value>
              <value>vert_min:6</value>
              <value>printf:%s</value>
            </configuration>
            <configuration name="printf_args" path='definition/printf_args' values='many' type='delimited'>
              <value>0:++date(%e %B %Y)</value>
    	</configuration>
          </configurationGroup>
    
          <configurationGroup name="100">
            <configuration name="type">
              <value>text</value>
            </configuration>
            <configuration name="definition" values='many' type='delimited'>
              <value>horiz_min:3</value>
              <value>vert_min:50</value>
              <value>printf:Dir Sir/Madam, 
    
     Please accept this letter as certification of employment for %s %s. 
    
    On %s, employment began as %s in the %s department of %s. 
    
    Sincerely, 
    %s</value>
            </configuration>
            <configuration name="printf_args" path='definition/printf_args' values='many' type='delimited'>
              <value>0:person+firstname</value>
              <value>1:person+surname</value>
              <value>2:staff+start_date</value>
              <value>3:position+title</value>
              <value>4:department+name</value>
              <value>5:facility+name</value>
              <value>6:++user</value>
            </configuration>
          </configurationGroup>
        </configurationGroup>
      </configurationGroup>
    



Crear un link para imprimir el formulario
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Después de que esto se ha establecido, debe abrir la plantilla de vista del formulario donde quiere ubicar el link a PrinteForm.


.. code-block:: xml

    <span type="module" name="PrintedForms" ifenabled="true">
      <span type="module" if="PrintedForms->hasValidForms('sample_hire_letter')">
        <li task="printed_forms_can_access"><span type="form" href="PrintedForms/menu?id=" name="person:id">Sample Hire Letter</span></li>
      </span>
    </span>
    

Lo descrito arriba significaría que el nombre de PrintedForm es sample_hire_letter y es primario de person.

Esta parte del código debe insertarse favorablemente bajo el link para actualizar la información de un formulario. (view_form_name.html)


