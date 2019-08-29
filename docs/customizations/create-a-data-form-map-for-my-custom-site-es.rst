Create a Data Form Map For My Custom Site - ES
==============================================

Cuando se crea un sitio personalizado, se podrán añadir formularios y campos nuevos. En tal caso, los mapas de datos para iHRIS Manage y Qualify ya no son correctos. Será necesario generar su propio mapa de formularios.


==Software Necesario==
Crear un mapa de formularios de datos es fácil una vez que se han instalado los programas adecuados en su sistema. Para hacer esto, debe ejecutar:
<source lang='bash'>
sudo apt-get install graphviz imagemagick
</source>

==Activar el Módulo==
La habilidad de crear un mapa de datos es dada por el modulo "". Para activarlo vía interfaz web:
*Haga click en "Configure System"
*Haga click en "Configure Modules" 
*Haga click en "Sub-Modules" junto a "I2CE Forms" 
*Haga click en la casilla que esta junto a "Form Documentor" 
*Haga click en el botón "Enable" al final de la página 

==Activar el Módulo (Línea de Comando)==
Vaya al directorio de ''páginas'' del sitio y escriba
 php index.php  --update=1 --enable=formDocumentor

==Crear un Mapa==
Vaya al directorio de su sitio, por ejemplo:
<source lang='bash'>
cd /var/www/iHRIS-manage
</source>

Ahora ejecute:
<source lang='bash'>
 php index.php --page=/formDocumentor/dot
</source>

Entonces se le pedirá que seleccione los formularios que quiere incluir en el mapa. Puede seleccionar los números individuales o un rango de números. Le sugiero que ''no'' incluya los formularios que inician con '''cl_''' ya que se verá desordenado y estos están relacionados con  SDMX-HD.  Otros formularios que sería conveniente que omita son '''uuid,'''  '''contact,''' '''role''' y '''user'''

Cuando finalice debería tener un archivo en el directorio '''/tmp''' .


[[Category:Customizations]][[Category:Forms]][[Category:Spanish]]
