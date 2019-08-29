IHRIS PHP 5.3 Clean Up
======================

There are several new features in PHP version 5.3 that clean up some kludgy code in iHRIS and I2CE which will improve code speed and readability.


Late Static Binding
^^^^^^^^^^^^^^^^^^^
There is a new static feature (google Late Static Binding)  so that we can do things like *$val = static::$some_var*  instead of *eval ('$val = ' . get_class($this) . '::$some_var;')* ;


__callStatic()
^^^^^^^^^^^^^^
Implement *static*  fuzzy methods with the *__callStatic()* :


* change I2CE_Form fuzzy methods to static fuzzy methods as appropriate so we don't need to instantiate a form object to call a fuzzy method on it.


Closures
^^^^^^^^
PHP 5.3 now supports closures and this can make the code more readable.

