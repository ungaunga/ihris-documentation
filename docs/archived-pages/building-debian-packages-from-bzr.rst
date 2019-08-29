Building Debian Packages from bzr
=================================

This article is deprecated.

== Easily Build Your Own ==

* Install [http://bazaar-vcs.org/ Bazaar] and [https://edge.launchpad.net/bzr-builddeb bzr-builddeb] as well as the build dependencies dpatch and debhelper. (“<tt>apt-get install bzr-builddeb dpatch debhelper</tt>”)
* Check out [http://code.launchpad.net/~hexmode my debian build scripts].  I suggest doing this in a separate directory.  For example:
<pre>
$ mkdir build
$ cd build
$ bzr co http://bazaar.launchpad.net/~hexmode/i2ce/debian-dev i2ce
$ bzr co http://bazaar.launchpad.net/~hexmode/ihris-common/debian-dev ihris-common
$ bzr co http://bazaar.launchpad.net/~hexmode/ihris-manage/debian-dev ihris-manage
</pre>
* In each directory, run “<tt>bzr builddeb</tt>”.
<pre>
$ (cd i2ce; bzr builddeb)
$ (cd ihris-common; bzr builddeb)
$ (cd ihris-manage; bzr builddeb)
</pre>
* You should now have a subdirectory named <tt>build-area</tt> with three .deb files in it.  Before installing them, you'll need to install the runtime dependencies: <tt>aptitude install dbcommon-config ucf libapache2-mod-php5 php-i18nv2 php-mdb2-driver-mysql php-text-password</tt>.  At this time, some are only available from the IntraHealth Debian repository above.
* Install the Debian packages you created: <tt>sudo dpkg -i build-area/*.deb</tt>

[[Category:Archived Pages]]
