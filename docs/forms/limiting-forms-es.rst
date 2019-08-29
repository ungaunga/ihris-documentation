Limiting Forms - ES
===================

Los datos en iHRIS se guardan en formularios y campos. Puede ser que quiera limitar una búsqueda de un formulario en particular utilizando una propiedad en sus campos. Por ejemplo, puede querer buscar a una persona cuyo primer nombre es "Jill."  Este artículo describe la estructura de cómo se aplican diferentes límites a los formularios.  

El sistema iHRIS tomará esta representación abstracta de un límite de un formulario y lo traducirá a un código PHP o SQL adecuado según sea necesario. 

Usos
^^^^
La estructura de límites de datos se utiliza en, por ejemplo:


* I2CE_Form::search()
* I2CE_Form::listFields()
* Form Relationships
* Report Limits

Los métodos de I2CE_Form incluyen la habilidad de limitar valores en base al mecanismo de almacenamiento. Si desea crear un nuevo mecanismo de almacenamiento con capacidades de búsqueda, será necesario que produzca algún código que permita pegar la estructura de limitación de datos descrita a continuación o, si su mecanismo de almacenamiento es accesible a la base de datos, simplemente convierta I2CE_FormStorage_Helper_DB en una sub-clase.

Estilos de Límites
^^^^^^^^^^^^^^^^^^
Hay varias maneras en las que desearía limitar los valores de un campo en particular, a estos nos referimos como **limit style.**   Por ejemplo, *equals*  o *like.* 

Recuerde que cada campo tiene un tipo, tal como INT o INT_LIST, que se traduce en una clase, tal como I2CE_FormField_INT o I2CE_FormField_INT_LIST, todas las que son sub-clase de I2CE_FormField.   Un tipo se hace disponible a alguna sub-clase (al igual que todas sus sub-clases) de I2CE_FormField.

La mayoría de estos estilos de límites y sus códigos auxiliares se pueden encontrar en el módulo **form-limits.**  


Estructura de los Límites de Datos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Permitimos formulario por formulario, la existencia de compuestos lógicos de límites de cualquier campo a través de una estructura de arreglo anidado (o datos magic). La estructura del límite de un *expression node*  es de la siguiente manera:


* operator: Requerido. Nos dice que tipo de nodo es este nodo de expresión. Los valores válidos son 'FIELD_LIMIT', 'AND', 'XOR', 'OR', y 'NOT'
* operand: Solamente se utiliza en el caso de 'AND', 'XOR', 'OR' y 'NOT' el cual es requerido. Es un sub-arreglo/sub-nodo que consiste de cero o más *limit expression nodes.*   En el caso de 'NOT' existe la mayor limitación de que el número es exactamente uno.
* field: Solamente se utiliza en el caso de 'FIELD_LIMIT' el cual es requerido.  Es el nombre del campo para el formulario que estamos limitando.
* style: Solamente se utiliza en el caso de 'FIELD_LIMIT' el cual es requerido. Es el estilo del límite.
* data: Utilizado solamente en el caso de 'FIELD_LIMIT.' Es un arreglo asociativo de datos utilizados para limitar los datos. Si no se establece, debería interpretarse como un arreglo vacío.

Por ejemplo, para una persona podremos tener:
 array(
   'operator'=>'AND',
   'operand'=>array(
     0=>array(
       'operator'=>'FIELD_LIMIT',
       'field'=>'surname',
       'style'=>'like',
       'data'=>array(
         'value'=>'N%th'
       )
     )
     1=>array(
       'operator'=>'NOT',
       'operand'=>array(
         0=>array(
           'operator'=>'OR',
           'operand'=>array(
             0=>array(
               'operator'=>'FIELD_LIMIT',
               'field'=>'othername',
               'style'=>'equals',
               'data'=>array(
                 'value'=>'Mike'
                )
             ),
             1=>array(
               'operator'=>'FIELD_LIMIT',
               'field'=>'othername',
               'style'=>'equals',
               'data'=>array(
                'value'=>'Michael'
               )
             )
           )
         )
       )
     )
   )

sería interpretado en SQL como:
 ((`person+surname` LIKE 'N%th') AND ( NOT (( `person+othername` = 'Mike') OR (`person+othername` = 'Michael'))))
Desafortunadamente, con tal afirmación no encontraría `Mike Nesmith <http://en.wikipedia.org/wiki/Michael_Nesmith#The_Monkees>`_ .


Estilos Existentes
^^^^^^^^^^^^^^^^^^
Estos son los estilos de límites proporcionados por *form-limits*  versión 3.2.0.  Por favor vea la clase misma para obtener información más actualizada.


* I2CE_FormField
* *null: No data array.
* *not_null: No data array.
* *null_not_null: Choose if a value is null or not.  Data array has key 'value' which is either (evaluates to) true for null, or (evaluates to) false for not null.
* *max_parent: No data array.  Only valid in form relationship context.
* *min_parent: No data array.  Only valid in form relationship context.
* *max_parent_form: No data array.  Only valid in form relationship context.
* *min_parent_form: No data array.  Only valid in form relationship context.
* I2CE_FormField_BOOL
* *truefalse: No data array.
* *true: No data array.
* *false: No data array.
* I2CE_FormField_DB_DATE
* *greaterthan_now: No data array.
* *lessthan_now: No data array.
* I2CE_FormField_DATE_Y
* *greaterthan:  Data array has key 'year' which is a year (integer).
* *greaterthan_equals:  Data array has key 'year' which is a year (integer).
* *equals:  Data array has key 'year' which is a year (integer).
* *lessthan_equals:  Data array has key 'year' which is a year (integer).
* *less_than: Data array has key 'year' which is a year (integer).
* *between:  Data array has keys 'min' and 'max' each of which is an array containing the key 'year' which is a year (integer).
* I2CE_FormField_DATE_YMD
* *greaterthan:  Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *greaterthan_equals:  Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *equals:  Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan_equals:  Data array has key 'year' which is a year (integer),  'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *less_than: Data array has key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *between:  Data array has keys 'min' and 'max' each of which is an array containing the key 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* I2CE_FormField_DATE_MD
* *greaterthan:  Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *greaterthan_equals:  Data array has key'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *equals:  Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan_equals:  Data array has key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *less_than: Data array has key  'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *between:  Data array has keys 'min' and 'max' each of which is an array containing the key 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* I2CE_FormField_DATE_HMS:
* *greaterthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *greaterthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *lessthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *lessthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* *between: Data array has keys 'min' and 'max' each of which is an array which contains the keys 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer).
* I2CE_FormField_DATE_TIME:
* *greaterthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *greaterthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan_equals: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *lessthan: Data array has key 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).
* *between: Data array has keys 'min' and 'max' each of which is an array which contains the keys 'hour' which is an hour (integer), 'minute' which is a minute (integer), and 'second' (integer), 'year' which is a year (integer), 'month' which is a month (integer), and 'day' which is the day of the month (integer).



* I2CE_FormField_DB_INT
* *between. Data array has keys 'min' and 'max.'
* *equals. Data array has key 'value' which is a scalar.
* *in. Data array has key 'value' which is an array of scalar values.
* *greaterthan. Data array has key 'value' which is a scalar.
* *greaterthan_equals. Data array has key 'value' which is a scalar.
* *lessthan. Data array has key 'value' which is a scalar.
* *lessthan_equals. Data array has key 'value' which is a scalar.
* I2CE_FormField_DB_STRING
* *between. Data array has keys 'min' and 'max.'
* *equals. Data array has key 'value' which is a scalar.
* *in. Data array has key 'value' which is an array of scalar values.
* *greaterthan. Data array has key 'value' which is a scalar.
* *greaterthan_equals. Data array has key 'value' which is a scalar.
* *lessthan. Data array has key 'value' which is a scalar.
* *lessthan_equals. Data array has key 'value' which is a scalar.
* *like. Data array has key 'value' which is a scalar.
* *lowerlike. Data array has key 'value' which is a scalar.  match is case insensitive
* *contains. Data array has key 'value' which is a scalar.  match is case insensitive
* I2CE_FormField_DB_TEXT
* *between. Data array has keys 'min' and 'max.'
* *equals. Data array has key 'value' which is a scalar.
* *in. Data array has key 'value' which is an array of scalar values.
* *greaterthan. Data array has key 'value' which is a scalar.
* *greaterthan_equals. Data array has key 'value' which is a scalar.
* *lessthan. Data array has key 'value' which is a scalar.
* *lessthan_equals. Data array has key 'value' which is a scalar.
* *like. Data array has key 'value' which is a scalar.
* *lowerlike. Data array has key 'value' which is a scalar.  match is case insensitive
* *contains. Data array has key 'value' which is a scalar.  match is case insensitive
* I2CE_FormField_YESNO
* *yesno: No data array.
* *yes: No data array.
* *no: No data array.

[[Category:Forms]][[Category:Spanish]]
