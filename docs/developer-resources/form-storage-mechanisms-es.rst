Form Storage Mechanisms - ES
================================================

El sistema iHRIS utiliza un nivel de abstracción para separar como se almacenan los datos en el sistema versus cómo se organiza y relacionan los datos entre ellos. Un formulario (y sus campos) proveedores las organizaciones. El almacenamiento de los datos se maneja por medio de varios mecanismos de almacenamiento de formularios.

Un mecanismo de almacenamiento se define por sub-clase de I2CE_FormStorage_Mechanism que proporciona los métodos para leer y posiblemente escribir los datos de cualquier formulario con el mecanismo dado. Si los datos se guardan en una base de datos puede sub-clase I2CE_FormStorage_DB y proporcionar acceso de lectura a los datos  como formulario mediante la definición de un método,
 *getRequiredFieldsQuery().*  Para que un mecanismo de almacenamiento permita la escritura, solamente se debe escribir un método que defina como almacenar un campo de datos.

Una vez que se escribe un mecanismo de almacenamiento, los datos de ese formulario pueden buscarse por medio de búsquedas con [[Limiting Forms |limites]].

Los mecanismos de almacenamiento que están disponibles actualmente son:


* [[Form Storage -- Entry/Last Entry|entry]]: Un mecanismo de almacenamiento vertical de base de datos que mantiene un historial de cuándo y quien cambio los campos individuales (elementos de datos). Este es el mecanismo de almacenamiento por defecto y el mecanismo de almacenamiento que fue utilizado en la versión anterior a la 3.2.
* [[Form Storage -- Flat Table|flat]]: Un mecanismo de almacenamiento horizontal de base de datos, donde una fila de una tabla corresponde a una instancia de un formulario. Las columnas o cualquier función SQL de la table se utilizan para definir los campos.
* [[Form Storage -- Multi-Flat Table|multi_flat]]: Un mecanismo de almacenamiento horizontal de base de datos similar al anterior pero que combina varias tablas estructuradas idénticamente. Se diseñó principalmente para la colación de datos.
* [[Form Storage -- Magic Data |magicdata]]: un mecanismo de almacenamiento local diseñado principalmente para listas d datos de mantenimiento central.
* [[Form Storage -- CSV |CSV]]: Un mecanismo de almacenamiento para leer datos de un archive CSV
* [[Form Storage -- Eval |Eval]]: Un mecanismo de almacenamiento para llenar y obtener registros en base a las llamadas de función
* [[Form Storage -- XML |XML]]: Un mecanismo de almacenamiento para llenar y obtener registros en base a un archive XML.
* [[Form Storage -- SDMX-HD |SDMX-HD]]: Un mecanismo de almacenamiento para llenar y obtener registros en base a listas de código SDMX-HD.
* [[Form Storage -- SDMX CrossSectional |SDMX Cross Sectional]]: Un mecanismo de almacenamiento para llenar y obtener registros en base a Datos Cross Seccionales SDMX.
* [[Form Storage -- LDAP |LDAP]]: Un mecanismo de almacenamiento para llenar y obtener registros en base a un servidor LDAP




Agregar Mecanismos de Almacenamiento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Usted puede estar en una situación en la que necesita agregar de diferentes instancias de iHRIS Manage (o Qualify).  Puede marcar un mecanismo de almacenamiento específico , $storage_mechanism, como agregado por ajuste:
 /modules/forms/storage_options/$storage_mechanism/componentized
a **1.** Then each form $form that uses that storage mechanism, will be [[Defining Forms#Componetized Forms|componetized]].

Por el momento, solamente el mecanismo de almacenamiento de [[Form Storage -- Multi-Flat Table|Multi-Flat]] es un mecanismo de almacenamiento que permite agregar.


Una vez que el módulo de *form-storage* está activado, una instancia de *I2CE_Form* tiene el método *isComponentized()* para revisar si un formulario está componentizado. También se puede revisar por medio del *I2CE_FormStorage::isComponentized($form)*

[[Category:Developer Resources]]
