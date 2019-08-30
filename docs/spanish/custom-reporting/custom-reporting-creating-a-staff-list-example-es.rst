Custom Reporting -- Creating a Staff List Example - ES
======================================================

Éste artículo describe como crear un informe staff info personalizad para iHRIS Manage.  Esto es un proceso de tres pasos:

* Cree el [[Custom Reporting -- Creating Form Relationships | form relationship]] 'staff_info'. <br/> Aquí elije los formularios que le interesan y como se relacionan el uno con el otro.
* Cree un [[Custom Reporting -- Creating Reports | report]] 'staff_report' personalizado basado en la relación 'staff_info'  <br/>Aquí escoge los campos que desee en su informe de las relaciones que ha creado.  También puede escoger a través de que campos limitar todas las visualizaciones de informe creadas de este informe.
* Cree un [[Custom Reporting -- Creating Report Views| report view]] personalizado para el staff report. <br/>Las diferentes visualizaciones de un informe están pensadas para que usuarios no-administrativos vean los datos en el sistema.

En realidad, esto es un proceso de cuatro pasos, siendo el primer paso decidir qué datos desea y donde están guardados.  Supongamos que tenemos el siguiente formulario de requerimiento de un Gerente de RH:
 Requerimiento: Cree una lista de personal con el puesto y localidad de cada persona 

El Formulario y Mapa de Campo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Un buen punto de inicio es ver el [[iHRIS Manage Form Fields | forms and fields]] y en especial la "graphic visualization" que es un mapa de los formularios y campos en iHRIS Manage.  Cuando construimos una buena relación de formulario, entonces **adjuntamos**  formularios al cruzar las flechas en el formulario de mapa de campos, tanto hacia adelante como hacia atrás. Hay dos flechas en este mapa:

* flechas negras: El nacimiento de una flecha, formA, se relaciona al objetivo del formulario flecha, formB,  a través de un campo mapeado.  Si la flecha no está etiquetada, entonces el campo mapeado también es nombrado formB. De otra manera es la etiqueta de la flecha.  Aunque, formA se mapea sólo a una instancia de formB, pueden haber muchas instancias de formA mapeadas desde formB.  Así, cuando vaya hacia atrás en una flecha negra, probablemente tendrá que limitar el formulario adjunto para que se elija un único formulario.
* flechas rojas:  El nacimiento de una flecha, formA, es el originario del objetivo de la flecha, formB.  Puede que formA tenga instancias de formB como un formulario secundario, pero formB sólo puede tener un formulario primario.  Así, cuando vaya hacia adelante en una flecha roja, probablemente tendrá que limitar el formulario secundario para que se elija un único formulario secundario.

Paso 0: ¿Qué datos desea?
^^^^^^^^^^^^^^^^^^^^^^^^^
Este es el paso más importante, y requiere algunos conocimientos más amplios de cómo se utilizan los datos (formularios) en el sistema.  
Basándose en el requerimiento del Gerente de RH y el formulario y campo vemos que tenemos que incluir los formularios siguientes:

* ''facility'':  necesitamos el nombre del local
* ''job'':  necesitamos saber el puesto que desempeña la persona
* ''person'': aunque no está dicho de forma explícita como requerimiento, asumamos que el Gerente de RH también quiere saber el nombre de los miembros del personal

Sin embargo, si vemos el mapa de datos, podemos observar que no hay flechas que conecten directamente los formularios *facility* , *job,*  y *person* .  En lugar de eso vemos que necesitamos ir del formulario *person* , hacia el formulario *person_position*  hacia el formulario *position* .  Desde el formulario position, podemos adjuntar el facility y job.  Esta es la parte relevante del formulario mapa de campo:

.. image:: /docs/custom-reporting/images/Forms-person-position-map.gif
    :align: center

Nótese que sólo hay una flecha roja, conectando *person*  y *person_position,*   mientras que el resto de las flechas son negras.

Paso 1: Cree el Formulario de Relación
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Crearemos un formulario de relación llamado 'staff_info'.  El formulario del cual empezamos el desplazamiento de nuestro mapa se llama *primary form.*   Estamos en libertad de escoger desde donde queremos iniciar el mapeo, pero seleccionar diferentes formularios primarios producirá un grupo de datos diferentes. Hay tres relaciones principales que podemos crear que se basan en cual formulario principal escojamos.   

* [[#Opción A:  Informe de Personas | Opción A]]: Escoger el formulario *person*  como el formulario principal. Luego los informes basados en la relación "staff_info" incluirán a todas las personas en el sistema tengan o no un puesto.
* [[#Opción B:  Informe de Puestos| Opción B]]: Escoger el formulario *position*  como el formulario principal.  Luego los informes basados en la relación "staff_info" sólo incluirán a las personas en el sistema que tengan un puesto.  También, si hay algunos puestos vacantes, estos aparecerán en el informe.
* [[#Opción C: Informe de Puestos Actuales| Opción C]]: Escoger el formulario *person_position*  como el formulario principal.  Luego los informes basados en la relación "staff_info" sólo incluirán los puestos ocupados.

Cualquiera de las opciones tiene sentido y la elección depende de los requerimientos del Gerente de RH.  Ya que el Gerente de RH no nos dio suficientes detalles para guiarnos, tendremos que pedirle que nos aclare este punto.

Opción A: Informe de Personas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Seleccione **Configure System**  y luego **Form Relationships.**  Creamos un informe de relación llamado 'staff_info' y elegimos "person"  como el formulario primario, escribimos un nombre y descripción. Luego hacemos click en update.

.. image:: /docs/custom-reporting/images/screenshot-create-relationship.gif
    :align: center

Ahora que hemos creado la relación 'staff_info' la podemos **editar**  . Ahora necesitamos adjuntar el formulario "person_position" al formulario  "position" .  Para hacer esto haga click en **Joined Forms**  y luego en  **Add a New Form** .  Seleccione ''person_position (child)" como el formulario a adjuntar, y el "short name"  como 'person_position.'   También debería escoger un nombre y descripción para este formulario.

.. image:: /docs/custom-reporting/images/Screenshort-join-person-position.gif
    :align: center

Notará que estamos trazando una fleche roja hacia adelante, de *person*  a *person_position.*   Según lo que dijimos anteriormente pueden haber muchas *person_position*  asociadas a una persona, así que tendremos que limitar los formularios.  Tendremos que limitar el formulario *person_position*  para que:

* La *start_date*  sea máxima entre todos los valores del campo *start_date*  para cualquier *person_position*  que sea secundaria a la actual *person*  .  De esta manera obtenemos el puesto más reciente que la persona haya iniciado.
* La *end_date*  no es nula, Para que sepamos que la persona aún mantiene su puesto.

Para esto, hacemos click en **Joined Forms**  de Nuevo y seleccionamos **Person Position (person_position),**  que es el formulario que acabamos de agregar.  Ahora podemos elegir  **Limit This Form.**  Ya que tenemos dos límites para este formulario, tendremos que seleccionar el Since "Operator Node" para que sea "And."

.. image:: /docs/custom-reporting/images/Screenshot-limit-person-position-AND.png
    :align: center

Una vez que hacemos click en el botón "Update", podemos elegir **Add A New Operand.**    Haremos esto dos veces, una vez para  'start_date' y una para  'end_date.'  Una vez que los operandos hayan sido agregados, podemos **Editar**  cada uno de ellos y elegir  **Limit  By A Field** :

.. image:: /docs/custom-reporting/images/Screenshot-limit-person-position-FIELDS.png
    :align: center

Ahora haga click en **Update**  una vez más.  Ahora podemos elegir los dos campos con los que queremos limitar y como queremos limitarlos

.. image:: /docs/custom-reporting/images/Screenshot-limit-person-position-FIELDS2.png
    :align: center

A continuación, adjuntamos el formulario *person*  al formulario *person_position*  como un formulario primario.  Hacemos esto al hacer click en **Joined Forms**  y luego **Add A New Child Form**  bajo el formulario *person_position* .  Nótese, no necesitamos especificar ningún límite aquí ya que estamos trazando una flecha negra en la dirección correcta.

.. image:: /docs/custom-reporting/images/Screenshot-join-position.png
    :align: center

Terminamos adjuntando los formularios "facility" y "job" al formulario "position"haciendo click en **Joined Forms**  y luego en **Add A New Child Form**  bajo el formulario *position* .  Nótese, no necesitamos especificar ningún límite aquí ya que estamos trazando una flecha negra en la dirección correcta.

Variaciones de la Opción A
--------------------------

* Nota: Existe un potencial para la ambigüedad aquí. Si una persona es asignada a más de un puesto a la vez con la misma *start_date* , entonces habrá un *person_position*  para cada uno de los puestos, así que cuando el formulario person_position se adjunte, escogerá uno de los formularios  person_position arbitrariamente.  Si espera que sea posible que las personas puedan tener más de un puesto a la vez, entonces debería de escoger la [[#Opción B:  Informe de Puestos | opción B]]
* Nota: Elegimos limitar el *end_date*  para que no sea nulo para obtener sólo puestos actuales. Si no pusiéramos un límite en *end_date,*  obtendríamos el último puesto que la persona tuvo, sin importar si lo mantienen o no.
* Nota: Si seleccionamos *Drop row if no form found*  bajo el formulario *person_position* , entonces si una persona no tuviera un formulario person_position asociado, serian eliminados del informe. Elegir hacer esto convertiría a este en un " Informe de Puestos Actuales," en lugar de un " Informe de Puestos." No haremos esto aquí, pero puede elegir hacerlo si tiene sentido para sus requerimientos.

Opción B:  Informe de Puestos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Seleccione **Configure System**  y luego **Form Relationships.**  Creamos un informe de relación llamado 'staff_info' y elegimos "position" como el formulario primario, escribimos un nombre y descripción. Luego hacemos click en update.

Ahora que hemos creado la relación 'staff_info' la podemos editar.

Primero adjuntamos el formulario "facility" al formulario "position" por el campo mapeado "position."   También adjuntamos el formulario "job" al formulario "position" por el campo mapeado "job."
  
A continuación debemos adjuntar el formulario "person_position" como mapeo del formulario *position*  a través del campo *position* .   En el formulario de mapa de campo, estamos trazando una flecha negra hacia atrás, así que tendremos que agregar algunos límites para elegir un único formulario *person_position* .  Puede que haya muchos formularios *person_positon*  mapeados a un  *position*  específico, así como varias personas pueden haber tenido el mismo puesto.  Sin embargo, solo debería haber un formulario *person_position*  donde  *end_date*  es nulo y esto corresponderá a la persona que tiene el puesto actualmente.

A continuación, adjuntamos el formulario *person*  al formulario *person_position*  como su formulario primario.  Ya que estamos trazando una flecha roja hacia atrás, no hay ambigüedad acerca de cuál formulario estamos adjuntando.

Variaciones de la Opción B
--------------------------

* Si seleccionamos "Drop Row If No Form Found"  cuando adjuntamos el formulario *person_position* , entonces sólo se mostraran aquellos puestos que han sido asignados a alguien alguna vez así que se vuelve más un informe de "Puestos Ocupados",  pero no un informe de Puestos Actuales.

Opción C: Informe de Puestos Actuales
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Seleccione **Configure System**  y luego **Form Relationships.**  Creamos un informe de relación llamado 'staff_info' y elegimos " person_position" como el formulario primario, escribimos un nombre y descripción. Luego hacemos click en update.
Ahora que hemos creado la relación 'staff_info' la podemos editar.

Primero, ya que solo queremos mostrar los puestos actuales, escogemos limitar el formulario *person_position*  para que end_date no sea nulo.

A continuación, adjuntamos el formulario *person*  que es el formulario primario del formulario''person_position'' .  Ya que estamos trazando una flecha roja hacia atrás, no hay ambigüedad sobre cual *person*  estamos adjuntando.

A continuación adjuntamos el formulario *position*  al formulario *person_position*  a través del campo mapeado *position.*  Ya que estamos trazando una fleche negra hacia adelante, no hay ambigüedad en el formulario *position*  que estamos adjuntando.

A continuación adjuntamos los formularios *job*  y *facility*  al formulario *position*  a través de sus campos respectivos.  De nuevo, como estamos trazando una flecha negra hacia adelante, no hay ambigüedad en los formularios que estamos adjuntando.

Variaciones de la Opción C
--------------------------

* Si elegimos no usar el limite *end_date*  es nulo, terminaríamos con un informe en el que se muestra la historia de cualquier puesto que haya sido ocupado.

Paso 2: Crear el Informe
^^^^^^^^^^^^^^^^^^^^^^^^

Ahora que construimos la relación 'staff_info' , podemos crear un informe a partir de esa relación. Vaya a **Configure System**  y luego **Reports**  y elija crear un informe nuevo, llamado 'staff_report' basado en la relación  'staff_info'.  Cuando terminemos verá la tabla zebra_staff_report en la base de datos. Aquí, podemos escoger los límites que queremos para las visualizaciones del informe (abajo) así como los campos que queramos ver en una visualización del.   Para hacer esto, haga click en  "Reporting Forms" y luego en "Fields" y podrá habilitar o deshabilitar campos de la relación a incluir en el informe. También podrá cambiar el texto del encabezado para el campo y fijar los límites para el campo.

Paso 3: Crear la Visualización del Informe
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Vaya a **Configure System**  y luego a **Report Views**  y elija crear una nueva visualización de informe basado en el informe "staff_report."  Simplemente seleccione los campos que quiere mostrar y habrá terminado.

