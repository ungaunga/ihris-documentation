Custom Reporting -- Add Images to a Report - ES
===============================================

Este tutorial aplica para la versión 4.0.22 y posteriores.

Este tutorial le enseñará como  mostrar imágenes en una visualización de tabla de informe.  Esto no aplica para visualización en PDF/Print.

==Fijando el Link==
Cualquier campo puede ser mostrado con un link. Los campos de Formularios de tipo IMAGE también pueden ser asignados para mostrar la imagen en línea.  Este tutorial asume que tiene un formulario con un campo IMAGE en la relación de formulario.

Ahora puede editar el informe que está basado en esta relación. Haga click en el formulario con la imagen y luego haga click en <u>Reported Fields</u>.

[[Image:Report_Image_1.png|center|frame|Custom report editor for the photo form]]

Habilite el campo de imagen y haga click en '''Link Options'''.

[[Image:Report_Image_2.png|center|frame|Image Link Options]]

Llene las opciones de link de la siguiente manera:
;Link url : BinField?field=''field''&formid=
:La opción de campo necesita ser igual al nombre en el campo de imagen del formulario.
;Link field : ''form'' Id
: Seleccione la id del formulario que tiene el campo de imagen.
;Link Type : Image (img)
:Si selecciona '''Link (a href)''' entonces en el informe se mostrará un link hacia la imagen.

[[Image:Report_Image_3.png|center|frame|Filled in Image Link Options]]

Haga click en el botón ''Update'' en la parte de abajo de la página para guardar los cambios.

==Actualizar la Visualización del Informe==

En una visualización de informe para este informe, deberá de habilitar el campo de imagen. Ahora cuando visualice este informe podrá ver la imagen.

[[Category:Custom Reporting]][[Category:Spanish]]
