Magic Data Storage Mechanisms - ES
==================================

Los datos magic proporcionan un mecanismo central para configurar iHRIS.  Estos datos magic se almacenan en una tabla de una base de datos. Debido al frecuente acceso a los datos, necesitamos un mecanismo de caché para mantener la carga de la base de datos bajo control. Por esta razón, se han creado varios mecanismos de almacenamiento de datos magic.

Usted puede agregar mecanismos de almacenamiento de bases de datos a I2CE_MagicData.  El último que se agrega es el método "permanent" de almacenamiento. Todos los demás que se agregan se utilizan para realizar caché a los datos almacenados en el mecanismo permanente de almacenamiento.

==Base de Datos==
Este mecanismo de almacenamiento de datos magic se diseñó para utilizarse como el mecanismo "permanent" de almacenamiento. Se almacena en la table 'config' de la base de datos por defecto.

==APC==
Hay un mecanismo de almacenamiento de datos magic en el módulo Pear APC e implementado por la clase I2CE_MagicDataStorageAPC.  Realiza caché de los datos en el segmento de memoria entre solicitudes con un tiempo de salida de 5 minutos.  Los datos en caché por Apache no reciben caché en la línea de comando.

Para limpiar el caché manualmente puede utilizar la interfaz de red de php-apc.

==Memcached==
Este es un caché en memoria de los pares de valores clave con límites de 1MB por tamaño de valor.

==SysV==
Este mecanismo de almacenamiento de datos mágicos ya no se mantiene.

Hay un mecanismo de almacenamiento de datos basado en SysV I2CE_MagicDataStorageSysV.  No está disponible en Windows. Crea segmentos de memoria para realizar caché a los datos entre solicitudes. Su ventaja sobre APC es que se puede tener acceso a los mismos segmentos compartidos vía la línea de comando. No hay tiempo de salida para los datos guardados.

Para limpiar los segmentos de memoria compartidos manualmente desde la línea de comando
 ipcs -m | grep www-data | awk '{print "ipcrm -m "$2}' | sudo bash
[[Category:Magic Data]][[Category:Spanish]]
