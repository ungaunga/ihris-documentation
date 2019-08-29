HowTo: Install Memcached
========================

With version 4.0.4 of iHRIS you can use memcahced to improve performance 

Note:  Memcached is used to cache data from the database.  Thus if you are an a sitaution
where you would need to restart the webserver by
 sudo /etc/init.d/apache2 restart
you should now do
 sudo /etc/init.d/apache2 restart && sudo /etc/init.d/memcached restart


Installation on Intrepid
^^^^^^^^^^^^^^^^^^^^^^^^
 **Warning:** This is only a rough guide as I did not take good notes.  Please correct.

Install Memcached
~~~~~~~~~~~~~~~~~
First install memcached by opening a terminal and typing:


.. code-block:: bash

    sudo apt-get install memcached
    


Then make sure that memcached is enabled.  Look at /etc/default/memcached and make sure that it is set to be enabled.  You can edit it by typing:


.. code-block:: bash

    sudo gedit /etc/default/memcached
    


Then make sure the content is:


.. code-block:: ini

    ENABLE_MEMCACHED=yes
    


If memcached wasn't enabled then after editing that file you'll need to restart it by typing:


.. code-block:: bash

    sudo /etc/init.d/memcached restart
    



Install libmemcached2
~~~~~~~~~~~~~~~~~~~~~
We first need to install libmemcached2 before we can install the PECL module.  It is not a part of the regular software distribution channels 
If you are using 32-bit Ubuntu
 cd /tmp
 wget http://ppa.launchpad.net/libmemcached/ubuntu/pool/main/libm/libmemcached/libmemcached2_0.31-1intrepid1_i386.deb 
 wget http://ppa.launchpad.net/libmemcached/ubuntu/pool/main/libm/libmemcached/libmemcached-dev_0.31-1intrepid1_i386.deb 
 sudo dpkg -i  libmemcached2_0.31-1intrepid1_i386.deb libmemcached-dev_0.31-1intrepid1_i386.deb 

If you are using 64-bit ubuntu
 wget http://ppa.launchpad.net/libmemcached/ubuntu/pool/main/libm/libmemcached/libmemcached2_0.31-1intrepid1_amd64.deb 
 wget http://ppa.launchpad.net/libmemcached/ubuntu/pool/main/libm/libmemcached/libmemcached-dev_0.31-1intrepid1_amd64.deb 
 sudo dpkg -i libmemcached2_0.31-1intrepid1_amd64.deb libmemcached-dev_0.31-1intrepid1_amd64.deb


Install PECL memcached
~~~~~~~~~~~~~~~~~~~~~~
Before we can install a PECL module, we need to install some stuff to compile the PECL modules development stuff 
 sudo apt-get install apache2-prefork-dev php5-dev

Now we can install the PECL memcached module.   The newer releases of pecl-memcached, 1.0.2 and greater, are not compatible with the libcached2  version 0.31 that we installed above.  I believe that version 1.0.1 works.  In which case you can do
 cd /tmp
 wget http://pecl.php.net/get/memcached-1.0.1.tgz
 sudo pecl install memcached-1.0.1

If this doesn't work, try version 1.0.0 from  `here <http://pecl.php.net/package/memcached>`_ 


Installation on Karmic
^^^^^^^^^^^^^^^^^^^^^^


Install Memcached
~~~~~~~~~~~~~~~~~
First install memcached by opening a terminal and typing:


.. code-block:: bash

    sudo apt-get install memcached
    


Then make sure that memcached is enabled.  Look at /etc/default/memcached and make sure that it is set to be enabled.  You can edit it by typing:


.. code-block:: bash

    sudo gedit /etc/default/memcached
    


Then make sure the content is:


.. code-block:: ini

    ENABLE_MEMCACHED=yes
    


If memcached wasn't enabled then after editing that file you'll need to restart it by typing:


.. code-block:: bash

    sudo /etc/init.d/memcached restart
    




Install PECL memcached Module
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next we need to link memcached with PHP using the memcached PECL library.  First make sure the development packages are installed so PECL can compile memcached.  Type the following in a terminal:


.. code-block:: bash

    sudo apt-get install libmemcached2 libmemcached-dev apache2-prefork-dev php5-dev
    


Now install memcached by typing:


.. code-block:: bash

    sudo pecl install memcached
    




Now enable the module by creating and editing a config file for PHP.



.. code-block:: bash

    sudo gedit /etc/php5/conf.d/memcached.ini
    


Save the following for that file:


.. code-block:: ini

    extension=memcached.so
    



Restart Apache
~~~~~~~~~~~~~~
Now restart apache to enable the PHP memcached library by typing the following in a terminal:



.. code-block:: bash

    sudo /etc/init.d/apache2 restart
    



Installation on Lucid or Meerkat
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Simply do
 sudo apt-get install php5-memcached memcached

