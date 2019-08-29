Custom Reporting -- Creating Form Relationships - ES
====================================================


Generalidades
^^^^^^^^^^^^^

Uso para el que fue Diseñado
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Esto está diseñado para un desarrollador o administrador del sistema que tenga una idea clara de cómo se relacionan todos los formularios. Las posibles conexiones entre los diferentes formularios ya se encuentran mapeados en el sistema. Una relación es la descripción de una ruta entre los diferentes formularios en el sistema.
  
En este instante, una relación es usada para [[Custom Reporting -- Creating Form Relationships|Custom Reports]]. También deseamos utilizarla para [[Custom Pages]].

Una relación de formularios es utilizada para construir consultas SQL usadas en un Reporte Personalizado.  Aunque no necesite conocer ningún SQL para crear un informe, familiarizarse con bases de datos relacionadas será de ayuda.


Ejemplo
~~~~~~~
Necesita crear una relación de formularios en in iHRIS Manage que muestre todos los empleados actuales, sus salarios y sus supervisores. Aquí hay un esquema de cómo definir esta relación:


* Inicie con el formulario primario 'person_position' y limítese a los puestos en los cuales el campo 'being_date' se sea nulo y el campo 'end_date' sea nulo.
* Adjunte al formulario primario el formulario 'person' donde el formulario 'person' es primario y el formulario 'person_position' secundario
* Adjunte al formulario primario el formulario 'salary' donde 'salary' es secundario a 'person_position' y donde el campo 'start_date' para 'salary' es máximo
* Adjunte al formulario primario el formulario 'position' donde el campo 'position' del formulario primario 'person_position' se mapea a ese puesto.  Nombre a este formulario 'employee_position'.
* Adjunte al formulario 'position' el formulario 'position' donde el campo 'supervisor' del formulario 'position' se mapea a ese puesto.  Nombre a este formulario conjunto 'supervisor_position' para distinguirlo del formulario 'employee_position'.
* Adjunte al 'supervisor_position' el formulario 'person_position' del cual el campo 'position' es el valor del formulario 'supervisor_position'.  Nombre a este 'supervisor_person_position'
* Adjunte el formulario 'supervisor_person_position' el formulario 'person' que es un formulario primario. Nombre a este 'supervisor'


Alguna Terminología
~~~~~~~~~~~~~~~~~~~


* En ocasiones a una relación se le llama "form relationship" o "report relationship"
* El "primary_form" es el punto inicial para describir el formulario en la relación.
* Un formulario puede ser mencionado varias veces en una relación. En el ejemplo anterior, el formulario, the person_position fue mencionado dos veces.  Una vez se le dio el "report form name" 'person_position' y una vez se le dio el "report form name" 'supervisor_person_position'.  De forma similar, el formulario person fue mencionado dos veces y se le dieron los dos "report form names" de 'person' y 'supervisor'
* Alguna de la terminología, tal como 'join', es tomada de SQL.


Dando Inicio
^^^^^^^^^^^^
Una relación de formulario puede ser creada siguiendo el "Configure System" y luego el link "Edit Form Relationship" .
Los primeros pasos son:


* seleccione "Display Name" para la relación,  el nombre de la relación para el usuario final.
* seleccione un "Short Name" para el informe, lo cual es una manera de hacer referencia internamente a la relación y sólo puede contener caracteres alfa-numéricos y algunos signos limitados de puntuación tales como _ y -.
* Una descripción de la relación.
* Luego debe hacer una de las opciones siguientes:
* *Escoger el "primary_form" para la relación
* *Copiar los detalles existentes de la relación de formulario a modificar


Adjuntar un Formulario
^^^^^^^^^^^^^^^^^^^^^^
Una vez que un formulario, formA, está en una relación, se puede adjuntar a cualquiera de sus formularios relacionados.  Debe asegurarse, al agregar un [[#Limiting Forms|limit]], que máximo una instancia del formB se adjunte a otra instancia del formA.  Hay cuatro posibles formas para adjuntar:


* (Una instancia de) formA es primaria en relación al (una instancia de) formB.
* *puede que formA tenga varias instancias secundarias del formB.  Por ejemplo, un formulario 'person' puede tener un formulario 'salary' secundario.
* (Una instancia de) formA es secundaria al (una instancia de) formB.
* *Nótese que un formulario, si tiene un formulario primario, es único, por lo que al adjuntarse de esta forma no se necesitan límites.
* (Una instancia de) formA contiene una [[Defining Forms#Map fields|mapped field]] cuyo valor se mapea al (una instancia de) formB.
* (Una instancia de) formB contiene una [[Defining Forms#Map fields|mapped field]] cuyo valor se mapea al (una instancia de) formA.


Limitando un Formulario
^^^^^^^^^^^^^^^^^^^^^^^
El formulario primario y cualquier formulario ajuntado en una relación puede ser limitado al usar la estructura [[Limiting Forms|limiting forms]].  La relación de formulario brinda una interfaz agradable para construir límites de formularios.


Agregar una Función SQL
^^^^^^^^^^^^^^^^^^^^^^^
Además de vincular formularios a informes, podemos definir funciones SQL que pueden correrse en los datos de los formularios. Para referenciar el campo llamado $fieldName en el formulario llamado $reportFormName en la relación se utiliza:
 `$reportFormName+$fieldName`
Por ejemplo:
 CONACT (SUBSTR(`supervisor+name`,1,1), '. ',  SUBSTR(`supervisor+surname`,1,1) , '.')
regresaría las iniciales del supervisor.

Para definir una función sql, se necesita definir:


* Un (corto) nombre utilizado para referenciar la función.  Por ejemplo, 'supervisor_initials.'
* Una descripción de la función.  Por ejemplo, "The Initials of the Supervisor."
* El campo del formulario en el cual la función SQL deberá enviar los valores.  Por ejemplo, "STRING_LINE"



