Creating Debian Packages
========================

This article has been deprecated.

This document describes the decisions made in packaging and descrbes the steps taken.

For the purpose of this discussion, we'll consider the build directory to be at <tt>~/build</tt>.

Bazaar
^^^^^^

.. code-block::

    $ sudo aptitude install bzr

If you are creating a new project, then make a directory for the project and put it under version control.  For example:

.. code-block::

    $ bzr init ihris-qualify-debian

Since you are probably dealing with code already under version control, you can just check it out.  For example, to check out the my build scripts for the <tt>i2ce</tt> project from Launchpad:

.. code-block::

    $ bzr co lp:~hexmode/i2ce/debian-dev i2ce-debian
    $ ls
    i2ce-debian
    

bzr-builddeb
^^^^^^^^^^^^

.. code-block::

    $ sudo aptitude install bzr-builddeb

The build scripts are kept separate repository and kept under version control.  To enable this (and keep the number of revision control systems in use to a minimum), I use <tt>bzr-builddeb</tt> to build packages directly from the bzr repository.

This package generation tool can keep the <tt>debian</tt> directory under revision control.  If you look at my debian repositories, you'll see that the repositories are the contents of the <tt>debian</tt> directory.  During the build process, <tt>bzr-builddeb</tt> merges the directory with the pristine source tree and performs all build operations there.

<tt>bzr-builddeb</tt> uses several configuration files to control its operation.  The only one we're concerned with here is the <tt>default.conf</tt> file under the <tt>.bzr-builddeb</tt> directory.  This stores the defaults for this package.  The contents of <tt>~/build/i2ce-debian/.bzr-debbuild/default.conf</tt>:

.. code-block::

    [BUILDDEB]
    merge = True
    export-upstream = http://bazaar.launchpad.net/%7Eintrahealth%2Binformatics/i2ce/main/
    

The first line just confirms that this is a <tt>bzr-builddeb</tt> configuration package.

The second line (<tt>merge = True</tt>) tells <tt>bzr-builddeb</tt> to merge this directory (in this case, <tt>~/build/i2ce-debian</tt> with the the upstream source.

The third line (<tt>export-upstream = …</tt>) gives the location of the original source in Bazaar to check out.

Running <tt>bzr builddeb</tt> from within the <tt>i2ce-debian</tt> directory will create a <tt>~/build/build-area/i2ce-2.0</tt> directory, check out the code from Launchpad, put the contents of the current directory in the <tt>debian</tt> subdirectory, and build the package.  After the package is built, the <tt>~/build/build-area/i2ce-2.0</tt> directory will be removed.

dpatch
^^^^^^

<tt> `dpatch <http://packages.debian.org/sid/dpatch>`_ </tt> is a patch management system that I used to alter the pristine configuration files so that they would work in the Debian packages.

Patches are stored in the <tt>patches</tt> sub-directory and are applied in the order listed in the <tt>00list</tt> file in that directory.

To apply all the patches, the command <tt>dpatch apply-all</tt> is executed.  To remove all patches (''i.e.'' in a “clean” operation), use the command <tt>dpatch deapply-all</tt>.  To create a new patch, see “Creating dpatch scriptlets” in the  `dpatch man page <http://olympus.het.brown.edu/cgi-bin/dwww?type=runman&location=dpatch/1>`_ .

dbconfig-common
^^^^^^^^^^^^^^^

<tt> `dbconfig-common <http://people.debian.org/~seanius/policy/examples/dbconfig-common/doc/dbconfig-common-design.html>`_ </tt> is used to set up the database structure for the <tt>i2ce</tt>.  If there is any need to provide initial database data for other packages, this package should be used to handle the installation.

To setup a database, two things must be done.  First, the database data must be provided.  Second, the <tt>dbconfig-common</tt> post-installation hooks must be called.

The SQL data is provided during the package building process by putting an SQL file at <tt>/usr/share/dbconfig-common/data/''package''/install/mysql</tt>.  PostgreSQL setup can be done in a similar way.

 **Important** : Since <tt>dbconfig-common</tt> creates a database as well as a user for the application, do not perform these steps in your database setup.

In the post-installation script, a few environment variables are set to tell <tt>dbconfig-common</tt> where to place the templates it produces and then the <tt>dbconfig-common</tt> hooks are called.  These hooks take care of collecting and assigning passords; creating the user and database for the application; and loading the data into the database.

ucf
^^^

Configuration files are managed with <tt> `ucf <http://packages.debian.org/testing/ucf>`_ </tt> (Update Configuration File).

This tool provides a way to udate configuration files so that user's changes are preserved.  <tt>ucf</tt> is called from the post-installation scripts to copy over a new configuration file.  If changes are detected that cannot easily be merged, the administrator performing the installtion will be prompted to confirm the update.

In the iHRIS packages, files managed with ucf are <tt>/etc/i2ce/I2CE_config.inc.php</tt>, <tt>/etc/i2ce/ihris_config.inc.php</tt>, <tt>/etc/apache2/conf.d/ihris-manage.conf</tt>, and the like.

Files and Directories in the Debian directory
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The debian directories under Bazaar contain several identically named files.  Here I describe the purpose of each file.  To learn more about the process of creating a Debian package, see the  `Debian New Maintainers' Guide <http://www.debian.org/doc/maint-guide/>`_ 

.bzr
~~~~

Bazaar stores all information about files under version control in this directory.  I won't bother talking about the specifics of what is in here since it isn't related to the build process.  Just don't delete it if you plan to use <tt>bzr-builddeb</tt>

.bzr-builddeb/default.conf
~~~~~~~~~~~~~~~~~~~~~~~~~~

The contents of this file were explained in the [#bzr-builddeb bzr-builddeb] section.

rules
~~~~~

This is a  `makefile <http://www.debian.org/doc/debian-policy/ch-source.html#s-debianrules>`_  that controls the creating of a package.  It has five mandatory targets (<tt>clean</tt>, <tt>binary</tt>, <tt>binary-arch</tt>, <tt>binary-indep</tt>, and <tt>build</tt>).

Since we're using dpatch, I've added <tt>patch</tt> and <tt>unpatch</tt> targets that <tt>build</tt> and <tt>clean</tt> depend on.

.. code-block::

    patch: patch-stamp
    patch-stamp:
    	dpatch apply-all -v
    	dpatch cat-all > patch-stamp
    
    unpatch:
    	dpatch deapply-all
    	rm -rf patch-stamp debian/patched
    

PHP-based packages don't really need that much “build” effort, so most of the action happens in the <tt>install</tt> target (used by the mandatory <tt>binary<tt> target) where files are re-arranged into something resembling the  `Filesystem Hierarchy Standard (fhs) <http://www.debian.org/doc/packaging-manuals/fhs/fhs-2.3.html>`_ .  As of this writing, for example, the <tt>i2ce</tt> package contains the following instructions:

.. code-block::

    install -d -m 755 -o root -g admin $(DESTDIR)/usr/share/ihris
    install -d -m 755 -o root -g admin $(DESTDIR)/usr/share/ihris/lib
    install -d -m 755 -o root -g admin $(DESTDIR)/etc/$(PACKAGE)
    install -d -m 755 -o root -g admin $(SQL_DIR)
    
    install -m 444 -o root -g admin \
    	lib/*.php $(DESTDIR)/usr/share/ihris/lib
    
    install -m 444 -o root -g admin I2CE_config.inc.php \
    	$(DESTDIR)/usr/share/ihris/
    install -m 444 -o root -g admin I2CE_structure.sql $(SQL_DIR)/mysql;
    

changelog
~~~~~~~~~

This is just a description of the changes to the package itself.  Since it has a very specific format, use <tt>dch</tt> or Emacs' <tt>debian-changelog-mode</tt> to create new entries.

compat
~~~~~~

(I'm not sure what this is.  I believe it contains the version number the build scripts look at to make sure they build the package properly.)

control
~~~~~~~

The packages that can be produces from this debian directory as well as the description, architecture, build-dependencies and install-dependencies are listed in the file.

For example, the control file for <tt>i2ce</tt> looks like this:

.. code-block::

    Source: i2ce
    Section: web
    Priority: extra
    Maintainer: Mark A. Hershberger <mhershberger@intrahealth.org>
    Build-Depends: debhelper (>= 5), dpatch
    Standards-Version: 3.7.2
    
    Package: i2ce
    Architecture: all
    Pre-Depends: ucf
    Depends: ${shlibs:Depends}, ${misc:Depends}, php-i18nv2, php-mdb2-driver-mysql,
             php-text-password, dbconfig-common
    Description: database-driven software for forms
     IntraHealth Informatics Core Engine (I2CE) is a set of classes for handling
     database-driven HTML forms with templates and database
     abstraction. It is the core programming engine for the iHRIS Suite of
     software.
    
    

The first stanza describes the source package and build depends.  Items like <tt>Section</tt> and <tt>Maintainer</tt> will be applied to the later binary package stanza's.

Since each of the packages (at present) creates only one debian package, there is only a single Package stanza.  If a source tree can produce multiple packages, then more stanzas will be placed here.  Of course, the packaging becomes more complex, but since the IntraHealth packages don't use this, I've not covered it here.

copyright
~~~~~~~~~

Every Debian package must contain a copyright file so that users can easily find the license on the package.  Since we're using the GPLv3, we can just make a reference to it.  For an example of a more complex copyright file, see  `virtualbox-ose's copyright file in Ubuntu <http://changelogs.ubuntu.com/changelogs/pool/universe/v/virtualbox-ose/virtualbox-ose_1.5.0-dfsg2-1ubuntu1/virtualbox-ose.copyright>`_ .

patches
~~~~~~~

The <tt>patches</tt> directory contains the patches for <tt>dpatch</tt>.  The contents are described in the [#dpatch dpatch] section above.

config
~~~~~~

This is a script that is included in the binary package and executed to take care of the configuration step of package installation.  The only IntraHealth package that includes a <tt>config</tt> script is the <tt>i2ce</tt> package.  <tt>i2ce</tt> uses this script to call the configuration hooks for <tt>dbcommon-config</tt>.

postinst
~~~~~~~~

This script is included in the binary package and executed after the files from the package have been put in place.  Any final setup takes place here.  For example, <tt>i2ce</tt> uses this script to set some environment variables and then call the <tt>dbconfig-common</tt> postinst hooks:

.. code-block::

    dbc_generate_include=php:/etc/i2ce/i2ce.php.inc
    dbc_generate_include_owner=www-data
    dbc_generate_include_perms=0400
    dbc_dbtypes=mysql
    
    . /usr/share/debconf/confmodule
    . /usr/share/dbconfig-common/dpkg/postinst
    
    dbc_go i2ce $@
    

Any files that are under the control of <tt>ucf</tt> ([#ucf see above]) are handled here.  <tt>i2ce</tt> installs its configuration file here:

.. code-block::

    ucf /usr/share/ihris/I2CE_config.inc.php /etc/i2ce/I2CE_config.inc.php
    

postrm
~~~~~~

<tt>postrm</tt> is executed after the package has been removed.  In the case of <tt>i2ce</tt>, <tt>dbconfig-common</tt> recommends deleting the files it generates during removal.

README.Debian
~~~~~~~~~~~~~

This contains any notes the packager may wish to include.  Don't just copy a <tt>README</tt> file as the packaging usually includes this.

