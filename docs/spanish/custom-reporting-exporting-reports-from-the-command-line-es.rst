Custom Reporting -- Exporting Reports From the Command Line - ES
================================================================

En ocasiones puede que desee exportar informes de la línea de mando de forma constante. Este documento explica como ejecutar comandos de la línea de mando para lograr esto. También puede incluir estos comandos en un script en un cron job si lo desea.  **Nota:**  Actualmente esto requiere la revisión 3014 de I2CE que repara algunos problemas con los informes de líneas de mando. Esto está siendo desarrollado, pero estará en la versión 4.1.4.


El Directorio de Páginas
^^^^^^^^^^^^^^^^^^^^^^^^

Antes de ejecutar cualquiera de estos comandos debe estar en el directorio de páginas de su sitio. Reemplace PATH con el PATH a su directorio de sitio.



.. code-block:: bash

    cd PATH/pages
    



Actualizar el Informe en Caché
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

El informe en caché se actualiza basándose en lo fijado las veces en las que se accede al sitio.  Sin embargo, puede que quiera poner en caché cualquier informe antes de ejecutarlos en la línea de mando. Para esto se utiliza el nombre "report", no la visualización de reporte.  Reemplace REPORT con el nombre de su reporte.



.. code-block:: bash

    php index.php --page=/CustomReports/generate/REPORT
    



Exportar un Informe como CSV
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para exportar su informe como un archivo CSV, ejecute este comando y reemplace REPORTVIEW con la visualización de reporte que desee visualizar.



.. code-block:: bash

    php index.php --page=/CustomReports/show/REPORTVIEW/Export --post=export_style=CSV > FILENAME.csv
    



Exportar un Informe como PDF
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Para crear un PDF de su informe , ejecute este comando y reemplace REPORTVIEW con la visualización de reporte que desee visualizar.



.. code-block:: bash

    php index.php --page=/CustomReports/show/REPORTVIEW/PDF --post='paper_size=LETTER&paper_orientation=P' > FILENAME.pdf
    



