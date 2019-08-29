Managing the Debian Repository
==============================

Normally our local  `Debian Repository <http://open.intrahealth.org/debian/>`_  is managed by [[Continuous Integration|Continuum]] and the <tt>deploy-i2ce</tt> script.  This page covers the steps the <tt>deploy-i2ce</tt> takes as well how you can manage the repository by hand, in a pinch.

= Automated Deployment =

Continuum runs the packaging scripts once an hour and then publishes the results (PHPDocumentor-produced docmentation and Debian packages).  The documentation is pushed to a subdirectory of  `/var/www/ihris-docs <http://open.intrahealth.org/ihris-docs/>`_  using rsync.  The debian packages are pushed to  `/var/www/debian <http://open.intrahealth.org/debian/>`_  using rsync and then archive maintenance commands are run.

= Updating a manually-built package =
You need to install the devscripts package:
 sudo apt-get install devscripts

Some packages (such as the <tt>-all</tt> packages and the <tt>site</tt> packages) need to be built by hand and placed in the repository by hand.

The <tt>site</tt> packages are simple enough: just change to the proper directory (e.g. <tt>cd sites/Demo</tt>) and run <tt>build-debian</tt>.

The <tt>-all</tt> packages are not so straightforward.  [[Building Meta Packages|After building them]], they need to be manually copied into the <tt>/var/www/debian/pool/main/manual</tt> subdirectory and run the following command:

    $ sudo -u tomcat55 apt-ftparchive -q -q generate \
      /etc/apt/apt-ftparchive.conf

 **Note:**  The <tt>manual</tt> subdirectory is used to avoid conflicts with the automated rsync process.
[[Category:Project Team Resources]][[Category:NeedsReview]]
