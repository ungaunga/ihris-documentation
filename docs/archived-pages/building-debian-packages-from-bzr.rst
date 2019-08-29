Building Debian Packages from bzr
=================================

This article is deprecated.

Easily Build Your Own
^^^^^^^^^^^^^^^^^^^^^

* Install  `Bazaar <http://bazaar-vcs.org/>`_  and  `bzr-builddeb <https://edge.launchpad.net/bzr-builddeb>`_  as well as the build dependencies dpatch and debhelper. (“<tt>apt-get install bzr-builddeb dpatch debhelper</tt>”)
* Check out  `my debian build scripts <http://code.launchpad.net/~hexmode>`_ .  I suggest doing this in a separate directory.  For example:

.. code-block::

    $ mkdir build
    $ cd build
    $ bzr co http://bazaar.launchpad.net/~hexmode/i2ce/debian-dev i2ce
    $ bzr co http://bazaar.launchpad.net/~hexmode/ihris-common/debian-dev ihris-common
    $ bzr co http://bazaar.launchpad.net/~hexmode/ihris-manage/debian-dev ihris-manage
    

* In each directory, run “<tt>bzr builddeb</tt>”.

.. code-block::

    $ (cd i2ce; bzr builddeb)
    $ (cd ihris-common; bzr builddeb)
    $ (cd ihris-manage; bzr builddeb)
    

* You should now have a subdirectory named <tt>build-area</tt> with three .deb files in it.  Before installing them, you'll need to install the runtime dependencies: <tt>aptitude install dbcommon-config ucf libapache2-mod-php5 php-i18nv2 php-mdb2-driver-mysql php-text-password</tt>.  At this time, some are only available from the IntraHealth Debian repository above.
* Install the Debian packages you created: <tt>sudo dpkg -i build-area/*.deb</tt>

