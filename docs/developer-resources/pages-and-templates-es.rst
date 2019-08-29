Pages and Templates - ES
========================

Este tutorial describe el rol de las Páginas y las Plantillas en iHRIS.

Una página es la pieza básica que maneja cada solicitud URL. Es la unidad funcional básica del sistema en una petición de URL que se procesa y se muestra. Si desea añadir una nueva funcionalidad a iHRIS, muy probablemente tendrá que añadir una nueva página. Una página de ejemplo sería "Edit/add a scanned document."

Una plantilla se utiliza para acceder a los elementos HTML de una página. Se basa en el [http://php.net/manual/en/book.dom.php PHP Document Object Model]. 


=Páginas=
Las páginas pueden establecerse para que vivan directamente bajo la base URL de la página, o bajo un módulo y todas las solicitudes se delegan en la clase de página apropiada por el [[#Wrangler|wrangler]].  

La lógica de una página se maneja por la [[#Page Classes|clase de una página]] que tiene como sub-clase I2CE_Page por medio del método ''[[#The action() Method|action()]]'' .  

Las variables GET y POST variables son (por defecto) [[#Variable Conversion|pre-procesadas]] por la clase de la página.  Todas las páginas por defecto utilizan un [[#Templates|templating]] que actúa como envoltura para el [http://en.wikipedia.org/wiki/Document_Object_Model Document Object Model] (DOM).  También hay un sistema basado en permisos de [[#Tasks and Roles|task and role]]  incluido.


También hay, por abuso de lenguaje, páginas para el PHP CLI. En este artículo sólo vamos a describir las páginas que URL Pide.
==Clases de Páginas==
Todas las solicitudes son finalmente delegadas por el wrangler a una subclase de I2CE_Page. Esta clase se encarga de toda la lógica de negocio de la página. Debe determinar la acción apropiada a desarrollar en función de si se trata de una solicitud de POST o GET. Varias páginas se pueden manejar por una clase de página. En la construcción, la página pasa una serie de arreglos de argumentos que se definen por [[#Page Styles|page style]] y ''[[#Converting a URL to a Page|request remainder]].''   Uno puede opcionalmente sobrescribir lo que se envía como el arreglo de las variables POST y GET.

==Lógica de la Página==
He aquí un resumen de la lógica de la página subyacente por defecto:
*Las variables POST y GOT son (por lo general) [[#Variable Conversion|pre-processed]].
*El conjunto de argumentos son producidos por el wrangler ya que procesa el [[#Page Styles|estilo]] de la página.   
*Los archivos de plantilla raíz o principales, se hay alguno cargado. Esto se especifica como el argumento de 'templates'.
*Los argumentos incluidos en esta página opcionalmente son restricciones de [[Tasks and Roles|tareas y roles]] para la página:
**Los roles que tienen permiso para ver la página se guardan bajo el 'access' clave
**Las tareas que un user/role debe tener para ver la página se guardan en las 'tasks' clave
*Una vez que el usuario ha pasado las restricciones de acceso de la página, lo siguiente ocurre:
** El 'pre_page_action' [[Module Structure#Hooked Methods|hook]] se llama 
**Cualquier archivo html por defecto se carga para una página en los [[#Templates|template]] que fueron creados para la página <br/> El archive html por defecto se guarda bajo el argumento  'defaultHTMLFile'
** Se llama el método [[#The action() Method|''action()'']] 
**Si el método de ''action()'' no regreso falso entonces se llama el 'post_page_action' [[Module Structure#Hooked Methods|hook]] 
**Si el método ''action()'' regresa falso entonces se genera un mensaje de error de usuario.
**Si la página solicita una redirección, se realiza y la ejecución se detiene.
**Si la página no solicito una redirección, entonces:
***Cualquier declaración echo, print_r, etc. se adjuntan al final del DOM de la plantilla.   Estos echo's, etc. solamente deben estar presente para propósitos de debugging y no en el código de producción.
***A menos que la página solicito suprimir el resultado, la plantilla muestra su resultado(HTML) .  <br/>Este es la única declaración echo que <span style='color:tomato>debe</span> utilizarse en un sitio de producción para mostrar html.

==El Método de action() ==
Una sub-clase de I2CE_Page generalmente debe implementar toda su lógica al sobrescribir el método ''action()'' .

==Conversión de Variables==
Las variables POST y GET, a menos que se les solicite específicamente no hacerlo, son pre-procesadas. Además de las variables POST y GET , las variables de SOLICITUD son creadas, que son (generalmente) cualquier variable que existe como POST o GET. Hay algunas cosas que ocurren (generalmente):
*Si la variable GET 'req_query' existe, se adjunta el valor y se guarda como variables de SOLICITUD
*Cualquier nombre de variables con ':' se procesan para definir arreglos de multi-dimensión. Por ejemplo:
 $_GET = array(
   'some:thing'] => '5'
   'some:otherthing' => '6'
  )
se convierte en:
 $_GET = array(
    'some'=>array(
        'thing'=>'5'
        'otherthing'=>'6'
    )
 )
*Si una variable se llama 'i2ce_json' es ''json_decode()'' y se fusiona de nuevo con las variables.

=Wrangler=
El wranger es el componente principal del software que delega las Solicitudes de URL primero a un par de  ''page name'' y módulo y luego a la clase de página apropiada.  Supongamos para esta sección que nuestro sitio vive en el siguiente URL de base: 
 <nowiki>http://my.site.org/manage</nowiki>
==Convertir un URL en Página==
Las páginas pueden vivir directamente en el URL de base o bajo un módulo. El wrangler procesa el URL con el método ''I2CE_Wrangler->processPath()'' y regresa un ''page name'', el ''page name'' del módulo se registra y un ''request remainder''.  El modulo bajo el que se registra un ''page name'' no es a menudo no el que proporciona la ''page class''.  Definamos la lógica para el ejemplo:
 <nowiki>http://my.site.org/manage/some/thing/is/here</nowiki>
*Si no hay nada después del URL de base, entonces el modulo es 'I2CE' y el ''page name'' es 'home'.  <br/>  No hay ''request remainder''. <br/>  Este no es el caso en el ejemplo de arriba.
*Si 'some' se registra como ''page name'' dado por 'I2CE', entonces el modulo es 'I2CE' y el ''page name'' es 'some'.  <br/>  El ''request remainder'' es entonces  ''thing/is/here.'' <br/>  ''some'' se considera un ''page name'' registrado bajo 'I2CE' si el [[Configuration (Magic) Data|magic data path]] ''/I2CE/page/some'' existe.
*De lo contrario el modulo es 'some' y las siguientes reglas aplican:
**Si no hay nada después de 'some', entonces el módulo es 'some' y el ''page name'' es 'home' <br/>  No hay ''request remainder''<br/>  Este no es el caso en el ejemplo anterior.
**Si 'thing' está registrado como un ''page name'' para 'some' entonces, el modulo es 'some' y el ''page name'' es 'some.'.  <br/>   El  ''request remainder'' es entonces ''is/here''
Una vez que la ruta se ha procesado, verificamos que la página que regresó existe para el módulo dado. Si no, tratamos de manejar la solicitud buscando un ''default page name'' para el modulo. El ''default page name,'' si está definido, existe en la ruta de los datos magic ''/modules/$module/default_page''.

El modulo registrado, el ''page name'', y el ''request remainder'' de llamado a todos puede verse a través de I2CE_Pages's API.

==Estilos de Página==
Una vez que tenemos un módulo válido y el nombre de la página asociada a un URL, comenzamos a procesar los estilos de la página. Un estilo de la página puede estar formado por tres componentes:
*Otro estilo de página de la que esta hereda las propiedades 
*Una clase de página para asociarse a una página
*Un arreglo anidado de argumentos para pasar al constructor de la clase de la página. Estos se combinan en los argumentos heredados por ''I2CE_Util::merge_recursive()''

=Plantillas=
A cada instancia de página se le asigna una plantilla que es una instancia de I2CE_TemplateMeister, y por lo general una instancia de la sub-clase I2CE_Template.


La plantilla es esencialmente una clase contenedora para un objeto DOMDocument con algunos útiles métodos de conveniencia incluidos. Si bien la funcionalidad adicional proporcionada por el I2CE_TemplateMeister y I2CE_Template es inicialmente muy limitada, se aumenta en gran medida mediante el uso de [[Module Structure#Fuzzy Methods|fuzzy methods]].

La página mostrará el DOM contenido en la plantilla como html una vez que la página ha terminado de procesar.  


==Template Data==
La forma más significativa en que el caso del I2CE_Template se argumenta es proporcionar "Template Data."  El modulo ''template-data'' ofrece la posibilidad de asignar datos arbitrarios a cualquier nodo en el DOM. Los datos existen en categorías, como 'FORM' u 'OPTION'  y se aplica a todos los sub-nodos secundarios del nodo dado. A cada dato se le asigna un nombre.

Si el nodo es determinado especificando una ''id'' (en lugar de dar una instancia explícita de DOMNode) los datos se mantendrán en caché hasta que un nodo con la ''id'' dada se añada a la plantilla.

Al buscar algún dato asignado a un nodo concreto, empezamos por el nodo dado y caminamos hasta el DOM hasta encontrar el dato con nombre.

Para cada categoría de los datos de la plantilla, se puede asignar un poco de datos por defecto, lo que aplica para todo el DOM.

Hay varios módulos que hacen uso explícito de la estructura de datos de plantilla.

<span style='color:red'>Advertencia:</span>  El mecanismo de los datos de plantilla supone que sólo hay una plantilla en uso por solicitud. Tenga mucho cuidado si utiliza varias plantillas en una página y cada una hace uso de los datos de la plantilla.
===Display Data===
Display data son datos de plantilla en la categoría 'DISPLAY' que pueden establecerse con los métodos inmediatos setDisplayData() y setDisplayDataImmediate() y proporcionar una forma conveniente de manipular los archivos de plantillas cargados. La plantilla buscará cualquier DOMElements con el atributo de nombre establecido y los procesará de acuerdo a su nombre de la etiqueta y los datos de la plantilla, si los hay, almacenados en el atributo de nombre. Aquí hay una lista de las etiquetas de uso general que se procesan y sus reglas:
*div,  pre, span, textarea: el valor de los datos de plantilla se anexa al siguiente contenido del elemento
*input: If the template data is an array, is is considered to be an array or attribute=>value pairs which are set on the element.  <br/> If it is scalar valued, is is processed according to the value of the attribute type as follows::::
**input: the attribute value is set to the value of the template data
**checkbox: if it evaluates to true, then the attribute 'checked' is set.  otherwise it is removed
*select: If the value of the template data is an array, <option> tags are added with value attribute set to be the array key and the text content set to the corresponding array value
*a: if the template data is of scalar type then:
**if the href value is not set, it is set to be the value of the template data.
**if the href is set the value template date is appended with either a ? or a & as appropriate to the href attribute
*img:  If the template data is an array, it is used as a set of attribute=>value pairs.  If it is scalar, then the src attribute is set
*form:  If the template data is an array, it is used as a set of attribute=>value pairs.  If it is scalar, then the action attribute is set
*meta: If the template data is a scalar the content attribute is set
*If the element has the attribute ifset with (case insensitive) value 'true' or 't' or '1' and the template data is not set, then it is removed.
*If the element has the attribute ifset with (case insensitive) value other than 'true' or 't' or '1' and the template data is set, then it not removed.

===Options===
Closely related to the Display Data module is the Options module which saves template data in the category 'OPTIONS.'  It process tags of the form:
 <nowiki><select id='some_id'/></nowiki>
and if it finds an OPTION template data named 'some_id' it will append a <select> tag for each of these bits of data.
===Form Data===
A form can be set on any node and can be referenced as
 <nowiki><span type='form' name='form:field'/></nowiki>
where you would substitute 'form' and 'field' as appropriate.  If the 'form' is not specified it uses the default form, if any, set for the page.
===Módulo de Atributos===

Los elementos DOM con el tipo de atributo establecido como 'module' y el atributo 'name' se procesan de acuerdo a ciertas reglas. El valor del atributo nombre es el nombre de un módulo. Se reconocen los siguientes atributos:
*ifenabled: can be t, true, !t or !true.  Si es verdadero y el módulo no está activo, o si es falso y el módulo está activo entonces se elimina el nodo.
*if: Trata de llamar la función del módulo con el calor del atributo 'if.'  Si el módulo regresa (something which casts to) falso el nodo se elimina.  Prefijar el valor con un ! causa la conducta opuesta.
*call:  El valor se utiliza como el valor de un método a llamar en la clase del módulo.  
Suponga que tenemos
 <span type='module' name='my_module' call='someMethod([arg1],....[argN])
 y que $module es la instancia de la clase del módulo asociada a my_module.  Entonces el resultado es el siguiente llamado:
 $module->someMethod($node,$template,$args)
donde $node es el nodo  <nowiki><span></nowiki> ,  $template es el objeto de la plantilla y el argumento es el arreglo de los argumentos $args = ($arg1,..,$argN)
donde [argM] se convierte en $argM de acuerdo a las siguientes reglas:
*si [argM] empieza con un $ entonces se refiere a los datos de la plantilla y las siguientes reglas aplican:
**La cadena tiene el formulario $abcd. El valor de $argM se convierte en el nombre de la plantilla con el nombre 'abcd.'
**La cadena tiene el formulario ${WXYZ}abcd.  El valor de $argM se convierte en los datos de la plantilla con la categoría XYZ y con el nombre 'abcd.'
*<NODE> se convierte en la instancia de DOMNode (si la hay) desde la que se llamó la cadena de permiso 
*<TEMPLATE> se convierte en la instancia de I2CE_Template (si la hay) desde la que se llamó el analizador de permiso 
*<USER> se convierte en la instancia de I2CE_User que es esta sesión
*si [argM] empieza con una sola comilla ' entonces es una cadena hasta que se encuentre la siguiente ' no-escapada
*si [argM] empieza con una doble comilla " entonces es una cadena hasta que se encuentre la siguiente " no-escapada. <br/>Además aplican las siguientes reglas de sustitución:
**cualquier subcadena que empiece con $ y se componga de caracteres alfanuméricos, - o _ se interpreta como datos de display de la plantilla a ser sustituidos <br> Por ejemplo "my name is $name" se convierte en "my name is Joe" si los datos de la plantilla llamada 'name' y el tipo de DISPLAY es "Joe"
**cualquier subcadena que empiece con {$ se lee hasta que se encuentra un }. La cadena entre ${ y } es el nombre de los datos de la plantilla de DISPLAY que entonces se sustituyen.
**para prevenir lo anterior, { y $ pueden espaciarse con una \
*cualquier cadena de caracteres alfanuméricos (y algunos signos de puntuación permitidos) se interpretan de la siguiente manera:
**si es del formulario abcd(, entonces se interpreta como otro método de llamado del $module as:<br/> $module->abcd($subargs)<br/> donde los sub-args se procesan (recursivamente) de acuerdo a las mismas reglas y limitado por el siguiente cierre)
**de lo contrario si es del formulario wxyz->abcd(, entonces se interpreta como otro método de llamado de $sub_module as:<br/> $sub_module->abcd($subargs)<br/> donde los sub-args se procesan (recursivamente) de acuerdo a las mismas reglas y limitado por el siguiente cierre)
y $sub_module es la instancia de la clase del módulo asociado con wxyz
*de lo contrario se interpreta como cadena

Los argumentos se separan por espacios o comas

==Etiquetas==
Como los "special cases" de las funciones de los módulos, seguidas de los atributos se escanean y procesan:
*printf attribute: Adjunta al nodo los resultados de sustitución printf de la cadena con los argumentos especificados.  También esta consiente del local y puede utilizar formas plurales.  <br/> printf="'this is something %s',$data'

==Scripts==
Cualquier etiqueta de scripts que se encuentren en el cuerpo del código HTML se mueve a la cabecera.

=Tareas y Roles=
Las [[Tasks and Roles|Tareas y Roles]] se utilizan para limitar el acceso a las páginas y los datos mostrados en el DOM.

[[Category:Developer Resources]]
