Database Structure - ES
=======================

iHRIS utiliza varias tablas en una base de datos relacional (MySQL) para guardar sus datos. Este artículo describe varias de las tablas que utiliza iHRIS, en particular la tabla del usuario y las tablas que se utilizan para [[Form Storage -- Entry/Last Entry | cambios de datos de formularios auditados]].

'''Nota: Este documento esta desactualizado y se ha marcado para revisión.'''


La base de datos de iHRIS se ha abstraído para que la estructura del objeto se pueda manejar con formularios dentro del sitio. Todos los registros que se guardan para un sitio son una instancia de un Formulario I2CE_Form. Esto define todos los campos que se utilizaron para ese formulario.  Los nombres de formularios y campos se guardan en el formulario y los campos de las tablas en la sección de [[#Form Definitions| definiciones de formularios]] a continuación. Estas se combinan en la tabla form_field para mapear los campos asociados con un formulario dado.

Los datos para cada formulario se guardan como un registro (vea [[#Record Tables|Tablas de Registro]]).  Cada campo luego se guarda en las tablas de entry y last_entry.  La tabla entry guarda un historial de todos los cambios y la tabla de last_entry es una búsqueda rápida del valor actual. De modo que si tiene una instancia de un formulario con 2 campos, habrá 1 fila guardada en la tabla de registro y 2 filas en entry y last_entry.  Siempre habrá solamente 3 filas en la tabla last_entry pero las filas de la tabla de entrada aumentarán cada vez que se realice un cambio.

== Tablas de Usuarios ==
Las tablas de usuarios pueden estar en la misma base de datos principal que el resto del sitio, o pueden estar en una base de datos compartida para que los nombres y las contraseñas puedan utilizarse más de una vez. La tabla de acceso debe estar en la base de datos principal para permitir acceso al sitio.
{|border="1" cellspacing="0" cellpadding="5"
!Tabla
!Descripción
!Definición de la Tabla 
|-
!user
|La tabla de user tiene la información de contacto y de acceso de todos los usuarios del sistema. La contraseña está cifrada con MD5() y la id se referencia en cualquier otra tabla que se refiere al usuario. El nombre de usuario y la id deben ser únicos. Se utilizan el nombre y apellido para efectos de visualización. La dirección de correo se utiliza para contactar al usuario para cambios de contraseña o contraseñas olvidadas. El creador es una referencia a la id de usuario que creó este usuario.
|<pre>
CREATE TABLE `user` (
  id int(11) NOT NULL auto_increment,
  username varchar(20) NOT NULL,
  `password` varchar(50) NOT NULL,
  firstname varchar(50) NOT NULL,
  lastname varchar(100) NOT NULL,
  email varchar(100) default NULL,
  creator int(11) NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY username (username)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
</pre>
|-
!user_log
|La tabla de user_log tiene los datos de inicio y finalización de sesión de los usuarios. También vincula el inicio de sesión a la session_id que está asociada con el usuario.
|<pre>
CREATE TABLE user_log (
  `user` int(11) NOT NULL,
  login datetime NOT NULL,
  logout datetime default NULL,
  session_id varchar(50) NOT NULL,
  activity datetime NOT NULL,
  KEY `user` (`user`),
  KEY login (login)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
</pre>
|-
!access
|La tabla de access controla el acceso de los usuarios al sitio. El rol es una cadena definida por el sitio para controlar las áreas que puede ver el usuario y que acciones puede realizar.
|<pre>
CREATE TABLE access (
  `user` int(11) NOT NULL,
  role varchar(255) collate utf8_bin NOT NULL,
  PRIMARY KEY  (`user`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}

== Definiciones del Formulario ==
Estas tablas definen los formularios y campos asociados con el sitio.
{|border="1" cellspacing="0" cellpadding="5"
!Tabla
!Descripción
!Definición de la Tabla 
|-
!form
|La tabla de form define un nombre corto para un formulario y lo vincula a un id único. El campo del tipo se omite.
|<pre>
CREATE TABLE form (
  id int(10) unsigned NOT NULL auto_increment,
  `name` varchar(50) collate utf8_bin NOT NULL,
  `type` tinyint(3) unsigned NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!field
|La tabla de field define un nombre corto para todos los campos que se utilizan en el sitio. El tipo es el tipo de datos para el campo dado.
|<pre>
CREATE TABLE field (
  id int(10) unsigned NOT NULL auto_increment,
  `name` varchar(50) collate utf8_bin NOT NULL,
  `type` varchar(16) collate utf8_bin NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY name_type (`name`,`type`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!form_field
|La tabla de form_field mapea una lista de campos que se asocian con el formulario dado. Todos los datos que se guarden estarán entonces asociados con el id único del form_field.
|<pre>
CREATE TABLE form_field (
  id int(10) unsigned NOT NULL auto_increment,
  form int(10) unsigned NOT NULL,
  field int(10) unsigned NOT NULL,
  PRIMARY KEY  (id),
  UNIQUE KEY form (form,field)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}
== Tablas de Registro ==
Las tablas de registro guardan información específica que se ha guardado para cada formulario asociado con el sitio.
{|border="1" cellspacing="0" cellpadding="5"
!Tabla
!Descripción
!Definición de la Tabla 
|-
!record
|La tabla record es la tabla principal asociada con cada instancia de un formulario. Hay una id única para su fácil referencia. El campo last_modified se actualiza cada vez que se le hace un cambio al registro dado. El formulario es la id del formulario del que este registro es una instancia. Si el registro tiene un registro primario, entonces el campo primario se llenará con esa id de registro.
|<pre>
CREATE TABLE record (
  id int(10) unsigned NOT NULL auto_increment,
  last_modified datetime NOT NULL,
  form int(10) unsigned NOT NULL,
  parent int(10) unsigned default NULL,
  PRIMARY KEY  (id),
  KEY parent (parent)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!entry
last_entry
|Las tablas de entry and last_entry son muy similares. La tabla de entrada lleva un registro de todos los cambios realizados al valor de un form_field dado para un registro.  La last_entry mantiene la última entrada para su fácil acceso. El registro es la id del registro con el que se asocia este valor para el form_field dado.  La fecha es la fecha en que se guardó este valor.  Who es la user id de la persona que realizó esta modificación. El change_type se establece dependiendo de si esta es una entrada inicial, una corrección o una actualización regular de este valor. También se puede establecer para que se verifique si los datos se han revisado. Uno de los campos de valores se llenará en base al tipo de form_field.
|<pre>
CREATE TABLE entry (
  record int(10) unsigned NOT NULL,
  form_field int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  who int(10) unsigned NOT NULL,
  change_type tinyint(3) unsigned NOT NULL,
  string_value varchar(255) collate utf8_bin default NULL,
  integer_value int(11) default NULL,
  text_value text collate utf8_bin,
  date_value datetime default NULL,
  blob_value longblob,
  PRIMARY KEY  (record,form_field,`date`),
  KEY `date` (`date`),
  KEY form_field (form_field),
  KEY record (record)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

CREATE TABLE last_entry (
  record int(10) unsigned NOT NULL,
  form_field int(10) unsigned NOT NULL,
  `date` datetime NOT NULL,
  who int(10) unsigned NOT NULL,
  change_type tinyint(3) unsigned NOT NULL,
  string_value varchar(255) collate utf8_bin default NULL,
  integer_value int(11) default NULL,
  text_value text collate utf8_bin,
  date_value datetime default NULL,
  blob_value longblob,
  PRIMARY KEY  (record,form_field),
  KEY form_field (form_field),
  KEY record (record)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!field_sequence
|La tabla de field_sequence se utiliza para llevar registro de un valor entero para un form_field que el sitio generará y aumentará automáticamente. Lleva registro del último valor utilizado para el form_field dado.
|<pre>
CREATE TABLE field_sequence (
  form_field int(11) NOT NULL,
  sequence int(11) unsigned NOT NULL,
  PRIMARY KEY  (form_field)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!deleted_record
|El deleted_record se utiliza para guardar registros que se borran del sistema en caso que deban recuperarse. Es un espejo de la tabla de registro.
|<pre>
CREATE TABLE deleted_record (
  id int(10) unsigned NOT NULL auto_increment,
  last_modified datetime NOT NULL,
  form int(10) unsigned NOT NULL,
  parent int(10) unsigned default NULL,
  PRIMARY KEY  (id),
  KEY parent (parent)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}

== Tablas de Utilidades ==
{|border="1" cellspacing="0" cellpadding="5"
!Tabla
!Descripción
!Definición de la Tabla 
|-
!config
|La tabla config guarda todos los datos de configuración para el sitio. Estos datos se leen de los archivos XML de configuración para los módulos. El hash es un hash MD5 de la ruta. Se utiliza para realizar búsquedas de claves únicas. Se comparte con el hash que está guardado en el APC. La ruta es un formato legible de la ruta hacia los datos. El tipo determina si esta entrada es un nodo primario o final. Si es un nodo final, el valor se establecerá con el valor del nodo. Si es un primario, entonces los secundarios se establecerán con una lista de nodos secundarios para esta entrada.
|<pre>
CREATE TABLE config (
  `hash` char(32) character set latin1 NOT NULL,
  path varchar(10000) character set latin1 NOT NULL,
  `type` tinyint(4) NOT NULL,
  `value` varchar(2000) character set latin1 default NULL,
  children varchar(10000) character set latin1 default NULL,
  PRIMARY KEY  (`hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
!report_list
|La tabla de report_list es simplemente una definición temporal para crear tablas temporales al crear un reporte en caché. Tiene registros primarios y secundarios que se guardarán en dependencia del reporte que se esté realizando en caché.
|<pre>
CREATE TABLE report_list (
  `primary` int(11) NOT NULL,
  secondary int(11) NOT NULL,
  PRIMARY KEY  (`primary`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
</pre>
|-
|}

== Ejemplo de Formulario ==

Este es un ejemplo de cómo se guardarían dos formularios en la base de datos. El formulario de persona tiene un campo para el surname (apellido) y el formulario demográfico tiene un campo de birth_date. El formulario de persona se guardaría primero ya que es el formulario primario. Asumiendo que nunca se ha guardado ningún formulario en la base de datos, lo siguiente ocurriría al guardarlo.

# Cree las entradas para '''form''', '''field''' y '''form_field'''.
## Se agregará una entrada a la tabla de '''form''' con el ''name'' para "person."  Esto asignará automáticamente una ''id'' de formulario de 1 ya que es el primero.
## Se agregará una entrada a la tabla de '''field''' con el ''name'' para "surname."  Esto asignará automáticamente una ''id'' de campo de 1.
## Se agregará una entrada a la tabla de '''form_field''' con el ''form'' de 1 (para persona) y el ''field'' 1 (para el apellido).  Esto asignará automáticamente una ''id'' para el form_field de 1.
## Se agregará una entrada a la tabla de '''form''' con el ''name'' para "demographic."  Esto asignará automáticamente una ''id'' de formulario de 2 ya que es la primera.
## Se agregará una entrada a la tabla de '''field''' con el ''name'' para "birth_date."  Esto asignará automáticamente una ''id'' de campo de 2.
## Se agregará una entrada a la tabla de '''form_field''' con el ''form'' para 2 (para demographic)  y el ''field'' para 2 (para birth_date).  Esto asignará automáticamente una ''id'' para el form_field de 2.
# Cree el registro de la persona.
## Se agregará un nuevo registro a la tabla de '''record'''. La ''id'' de registro se generará automáticamente (1) y ''form'' se establecerá como 1.  No hay ''primary'' y la hora de ''last_modified'' se establecerá como la hora actual.
## Se agregará una entrada a las tablas de '''entry''' y '''last_entry'''. El ''record'' se establecerá como 1 y el ''form_field'' se establecerá como 1 ( la id de form_field creada anteriormente para la persona-apellido). ''Date'' será la hora actual y ''who'' se establecerá como la id de usuario que está realizando el cambio.  El campo ''string_value'' se establecerá como el valor del apellido.
# Cree el registro demográfico.
## Se agregará un Nuevo registro a la tabla de '''record''' . La ''id'' del registro se generará automáticamente (2) y el ''form'' se establecerá como 2.  El ''primary'' se establecerá como 1 ya que este es un formulario secundario del registro de persona que se acaba de crear.  La hora de ''last_modified'' se establecerá como la hora actual.
## Se agregará una entrada a las tablas '''entry''' y '''last_entry'''.  El ''record'' se establecerá como 2 y el ''form_field'' se establecerá como 2 (la id de form_field creada anteriormente para demographic-birth_date).  La ''date'' será la hora actual y ''who'' se establecerá como la id de usuario que está haciendo el cambio.  El campo ''date_value'' se establecerá al valor para birth_date.
[[Category:Technical Overview]][[Category:Spanish]]
