Automatically Generated Integers - ES
=====================================


Enteros Generados Automáticamente (INT_GENERATE)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Los enteros generados automáticamente (ó INT_GENERATE) se utilizan cuando un formulario necesita utilizar un número incrementado para una ID, pero el operador de datos no puede saber cuál es el siguiente valor disponible es. El usuario puede marcar una casilla para incrementar al siguiente valor o si es necesario puede introducir el número si este lo sabe. Desde la versión 4.0.2 INT_GENERATE sólo se admite cuando el formulario utiliza el mecanismo de almacenamiento de formularios "entry". Utiliza la tabla field_sequence para llevar un registro del valor actual máximo para cada campo del formulario.

En la tabla field_sequence habrá una entrada con la id del campo del formulario y el valor más alto que se ha utilizado. El sistema comprueba dos posibilidades para determinar el siguiente número disponible. Busca en la tabla field_sequence si existe una fila ahí para el campo del formulario y en la tabla last_entry el valor más alto que se ha asignado. El valor más alto se incrementa en uno y se guarda en la tabla field_sequence para poder tener acceso a este la próxima vez que se agrege un registro.

Si quiere empezar en 1000 puede agregar la id del campo del formulario y 1000 a la tabla field_sequence. Sólo tiene que añadir algo a la tabla field_sequence si desea iniciar con un valor más alto que que los valores guardados actualmente. Por ejemplo, si ha importado datos que van desde 100 hasta 400, pero desea que los números generados inicien en 1000, entonces usted tendrá que agregar una fila a la tabla field_sequence. Pero si lo que desea es que el número siguiente sea 401 entonces no tiene que hacer nada.


[[Category:Forms]][[Category:Spanish]]
