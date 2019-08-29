Linux (Ubuntu) Installation - 4.1.8 - ES
========================================

Esta página contiene instrucciones para instalar la version 4.1.8 de iHRIS manualmente.
{{otherversions|Linux (Ubuntu) Installation}}

<center>'''Necesita ayuda?'''  Try our [[Project Communication]]</center>

Usted podría necesitar las instrucciones para instalar [[Installing the Debian Packages |debian packages]] con un proceso de instalación más simple.


Software de Soporte
^^^^^^^^^^^^^^^^^^^

Primero debe instalar Ubuntu y todos los software de soporte requeridos por iHRIS siguiendo las instrucciones en [[Linux (Ubuntu) Installation - Supporting Software]].

 **Nota:**  ¿Necesita instalar en un filesystemext4?  vea  `this <http://ubuntuforums.org/showthread.php?t=1313834>`_ 

 **Nota:**   A menos que se mencione específicamente, todos los comandos abajo descritos se corren utilizando una terminal. Puede iniciarlo en Ubuntu al ir a Aplicaciones -> Accesorios -> Terminal.  Cuando un commando empieza con **sudo**  le pedirá su contraseña porque este se ejecutará con privilegios de administrador. Cuando se ejecute sudo varias veces, solamente le pedirá la contraseña la primera vez.

 **Nota:**   Algunos comandos de instalación le pedirán que introduzca información en la ventana de la terminal, usualmente con un fondo azul. El ratón no se utiliza para dar click a las opciones aquí. Puede utilizar la tecla Tab para moverse entre las opciones y la barra espaciadora para seleccionar o deseleccionar.

 **Nota:**   Algunos comandos ejecutarán el editor de archivos **gedit**  . Revise los documentos de  `documentation <https://help.ubuntu.com/community/gedit>`_  si necesita ayuda adicional.


Descargar la Suite iHRIS Completa
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Antes de proceder con la instalación de iHRIS Manage o iHRIS Qualify, debemos descargar la versión mas reciente de la Suite iHRIS completa. Para descargar el software debe utilizar estos comandos:


.. code-block:: bash

    sudo mkdir -p /var/lib/iHRIS/lib/4.1.8
    sudo ln -s /var/lib/iHRIS/lib/4.1.8 /var/lib/iHRIS/lib/4.1
    cd /var/lib/iHRIS/lib/4.1.8
    sudo wget http://launchpad.net/i2ce/4.1/4.1.8/+download/ihris-suite-4.1.8.tar.bz2
    sudo tar -xjf ihris-suite-4.1.8.tar.bz2
    



Instalar el Software
^^^^^^^^^^^^^^^^^^^^

Siga las instrucciones [[iHRIS Manage Installation - 4.1.8|iHRIS Manage Installation]] para iHRIS Manage.

Siga las instrucciones [[iHRIS Qualify Installation - 4.1.8|iHRIS Qualify Installation]] para iHRIS Qualify.

Siga las instrucciones [[IHRIS Plan Installation - 1.0.4|iHRIS Plan Installation]] para iHRIS Plan.  (No es necesario que descargue la Suite iHRIS que está arriba)


