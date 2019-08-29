Controlling the package build process
=====================================

This page contains a brief overview of how to build Debian packages from the source for the iHRIS Suite.  The package building scripts are bootstrapped when the I2CE package is built.  The packaging scripts reside in  `modules/PackageUtils/ <http://bazaar.launchpad.net/~intrahealth%2Binformatics/i2ce/trunk/files/head%3A/modules/PackageUtils>`_ .

= Goals of PackageUtils =

The <tt>PackageUtils</tt> module was designed with a few goals in mind.  These are



* One module, one package
* Minimize configuration information
* Ease of invocation
* Compatibility with Launchpad's PPA service


One Module, One Package
^^^^^^^^^^^^^^^^^^^^^^^

There is a one-to-one correspondence between modules and debian packages.  The package name corresponds to the name attribute of the I2CEConfiguration element in the XML file.  An “i2ce-” prefix is given to each generated package to reduce the changes of naming conflicts.  (The only exception to this is the I2CE package itself which is named simply “i2ce”.)   In this way, dependencies between packages mirror the dependencies between modules.


Minimize configuration information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Another goal of the current design was to eliminate the need to maintain dozens of different configuration files for each module.  The information needed was (mostly) already found in the configuration file.

For this reason, <tt>PackageUtils</tt> relies on a module's configuration for all of its information.  This information is put into some templates (which are found in the <tt>templates/</tt> subdirectory of the <tt>PackageUtils</tt> module) to produce a <tt>debian/</tt> directory that is used to build the entire package.  Source packages are also produced during the build process.  The source packages are needed so that Launchpad can build the packages using standard Debian tools.


Ease of invocation
^^^^^^^^^^^^^^^^^^

The <tt>PackageUtils</tt> module (<tt>i2ce-package-utils</tt>) is set up so that it could be run from the root of a checkout of I2CE code (e.g. the results of <tt>bzr co lp:i2ce</tt> or <tt>bzr co lp:ihris-manage</tt>) and, from a single command, create packages for all modules in that source tree.


Compatibility with Launchpad's PPA service
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

During the build process, the modules are put into a conventional layout so that conventional tools (such as <tt>dpkg-source</tt> and <tt>debuild</tt>) can be used to manipulate the packages.

Part of the build process is to run <tt>debuild -S</tt> to produce a <tt>_source.changes</tt> file that can be used with <tt>dput</tt> to upload to Launchpad's build service.

= Running the package builder =

After installing <tt>PackageUtils</tt> (<tt>sudo apt-get install i2ce-package-utils</tt>), from the top level of an I2CE source tree you can run <tt>build-i2ce</tt>.

The site modules are handled seperately and must be built by hand.  So, if you want to build the Demo site module, use the following steps:

    $ bzr co lp:ihris-manage
    $ cd ihris-manage/sites/Demo
    $ build-i2ce

The resulting debian package (in <tt>pkgs/DEB/</tt>) must be [[Managing the Debian Repository|manually uploaded to the repository]].

 **Note:**  there is a bug in the build process.  I designed it to follow all the paths for MODULES so it could be run in a top-level tree.  However, since the Demo site module includes a <tt>../../..</tt> path (which you should change to <tt>/usr/share/i2ce</tt> at the time of build), it will try to traverse those directories as well.  This behavior will be fixed, but, for now, you can safely break out of the build after it has built the demo package.

 **Note:**  At this point, build-i2ce will build all modules and there is no way to specify a single module to build.  Since I initially intended build-i2ce to be run automatically by [[Continuous Integration|Continuum]], this wasn't a concern.

= Special Paths =

The <tt>prepInstallPaths</tt> method specifies two special path names from the paths listed in the configuration file.  Files from any other specified path are installed under <tt>/usr/share/i2ce/</tt>.

The two specified paths are <tt>BIN</tt> and <tt>CONF</tt>.  Files in the path specified by <tt>BIN</tt> are installed to <tt>/usr/bin/</tt> while files under the path specified by <tt>CONF</tt> are installed under <tt>/etc/i2ce</tt>. (As of this writing this is used only by <tt>PackageUtils</tt> itself to install <tt>build-i2ce</tt> and <tt>deploy-i2ce</tt> and their configuration file.)

Additional modifications can be made here so that files under, say, <tt>PAGES</tt> are installed under <tt>/var/www/i2ce</tt>.

 **FIXME:**  The path-mapping information in <tt>prepInstallPaths</tt> should probably be moved to a configuration file.

 **FIXME:**  Files in <tt>/etc</tt> should be marked as configuration files.

= External Dependencies =

The <tt>getExternalPackageName</tt> takes care of mapping external requirements to the corresponding Debian package names.

 **FIXME:**  This dependency mapping information should probably be moved to a configuration file.

= Deployment Configuration =

<tt>PackageUtils</tt>’ contains two scripts: <tt>build-i2ce</tt> and <tt>deploy-i2ce</tt>.  <tt>build-i2ce</tt> handles the actual build process (described above) and then checks for the <tt>deploy-i2ce</tt> script and runs it.  As of this writing, the included <tt>deploy-i2ce</tt> is a shell script to publish the documentation produced by PHPDocumentor and the Debian packages.  See [[Managing the Debian Repository]] for more information.


