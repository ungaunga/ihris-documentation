File Search Paths - ES
======================

En este artículo describimos la utilidad de la Búsqueda de Archivos que es parte de iHRIS. Dicha utilidad le permite categorizar y agrupar fácilmente archivos diferentes y ponerlos a disposición de iHRIS. También le permite copiar un archive de la core iHRIS Suite en la personalización de su sitio para hacer cambios ahí, sin tener que modificar el software central de iHRIS.


El I2CE (Intrahealth Informatics Core Engine) utiliza una utilidad de búsqueda de Archivos para organizar los archivos en categorías y definir prioridades para la búsqueda en los directorios. Desde la versión 3.2 también proporciona [[#Localizing Paths|localización]] de archivos.

Todos los archivos, con muy pocas excepciones, se encuentran utilizando la clase  *I2CE_FileSearch*  definida en *I2CE/lib/I2CE_FileSearch.php.*   Las excepciones son aquellos archivos bajo *I2CE/lib.*    

=Categorías de Rutas=
Las categorías de rutas utilizadas comúnmente son:


* plantillas Estos son los directorios para buscar archivos de plantillas html
* imágenes Estos son los directorios para buscar archivos de imágenes
* css Estos son los directorios para buscar archivos CSS
* scripts Estos son los directorios para buscar archivos javascript
* clases Estos son los directorios para buscar archivos que contienen clases php.  La convención aquí es que MyClass está localizado en el archivo MyClass.php
* módulos Estos son los directorios para buscar módulos
Usted puede crear sus propias categorías de rutas.

=Prioridades=
Los directorios en una categoría dada se buscan por un archive en orden de la prioridad más baja a la más alta. Si dos directorios tienen la misma prioridad y el mismo archive, no hay garantía de cual archivo regresará. 

Las rutas agregadas por un módulo tienen la prioridad negativa de ese módulo. Por ejemplo, un archive de plantilla en I2CE tiene una prioridad de 0, mientras que un archivo de plantilla encontrado en ihris-manage tiene una prioridad de -200  para que el archivo de plantilla en ihris-manage se encuentre primero.  Hay dos excepciones: las rutas agregadas por un módulo en las 'classes' o 'modules' se agregan con la prioridad del módulo para que una clase php encontrada en I2CE tome precedencia sobre una en ihris-manage que tienen una prioridad de 200.

=Agregar Rutas=
La forma más común de agregar un directorio a una ruta de búsqueda es hacerlo a través de una estructura de módulos [[Module Structure#Module Configuration File|configuration file]].  por ejemplo:
 <path name='classes'> 
   <value>./lib</value>
 </path>
Las etiquetas de <value> pueden ser rutas absolutas o relativas. Si son relativas, es con respecto al directorio que contiene este archivo de configuración.   
Algunas Salvedades:


* Si agrega un '*' al final de una ruta que termina en  '/' (o '\' para Windows), esto dice que todos los sub-directorios de este directorio deben añadirse a la ruta. Por ejemplo, <value>./my_path/*</value>  agrega todos los sub-directorios bajo ./my_path/
* Si agrega un  '*' al final de una ruta que no termina en  '/' (o '\' para Windows) esto dice que agregamos todos los directorios que concuerdan con el archivo glob.  Por ejemplo, <value>./my_paths/go*</value> agrega todos los sub-directorios de my_paths que empiezan con go.
* Si agrega un '**' al final de una ruta que termina en  '/' (o '\' para Windows) agregará todos los sub-directorios, sub-sub-directorios, sub-sub-sub-directorios etc de la ruta dada.
* Si un directorio que usted agrega tiene un sub-directorio llamado 'local' primero buscará lo relativo a este subdirectorio para este archivo.  Esto es útil para propósitos de desarrollo para prevenir que las cosas se comprometan a bazaar.
* Ver [[#Localization|localización]]

=Localización=
Dese la version 3.2, hemos agregado la habilidad de localizar una ruta. Cuando se agrega una ruta a la utilidad de búsqueda de archivos, primero revisa si el subdirectorio está *en_US.*   Si no existe, entonces este directorio no se considera localizado. Si existe, la ruta se considera localizada. En este caso, consideramos que cada sub-directorio corresponde a un local.

Los locales preferidos se establecen por usuario. Por ejemplo, si mis locales preferidos fueran  *fr_RW*  y luego  *fr_FR*  y luego  *en_US*  y estoy buscando el archivo *main.html*  en *./templates*  que tiene *en_US*  como in sub-directorio, buscaría  *main.html*  en este orden:


* ./templates/fr_RW/main.html
* ./templates/fr_FR/main.html
* ./templates/en_US/main.html
hasta encontrar el archivo que quería. Si no estuviese ahí, buscaría *main.html*  en un directorio prioridad más alta.

=Caché=
Debido a la alta frecuencia con que se buscan archivos, una búsqueda exitosa tendría sus resultados en el cache vía  `apc <http://pecl.php.net/package/APC>`_ .  En la versión 3.1, estos resultados se guardan globalmente. A partir de la versión 3.2, dado que la preferencia de localización es definida por usuario, estos resultados se guardan en el caché por usuario.  

Por defecto, un archivo se considera obsoleto después de 60 segundos. El caché se puede desactivar al modificar los datos magic en /I2CE/fileSearch/stale_time (vea *I2CE/I2CE_Configuration.xml* ).

 **<span style='color:red'>Precaución:</span>** Si está desarrollando un módulo nuevo y agrega un archivo de plantilla, el sistema no lo archivará inmediatamente porque los resultados de la búsqueda de archivos se guardan en el caché. Usted puede esperar los 60 segundos o limpiar los resultados guardados en la memoria cache  `apc <http://pecl.php.net/package/APC>`_ .
[[Category:Modules]][[Category: Spanish]]
