HowTo: Release iHRIS Software 4.1
=================================

This page contains installation instructions on releasing iHRIS version 4.1
{{otherversions|HowTo: Release iHRIS Software}}

Warning: To release the software, you will need to be someplace with good bandwidth as you will be uploading a lot to launchpad.net

Release Directory Layout
^^^^^^^^^^^^^^^^^^^^^^^^
In your home directory, create a new directory called "ihris-release" with a subdirectory "bzr" which will contain all the bzr branches we wish to include in the release

.. code-block:: bash

    mkdir -p ~/ihris-release/bzr
    cd ~/ihris-release/bzr
    bzr checkout lp:i2ce I2CE
    bzr checkout lp:ihris-common
    bzr checkout lp:ihris-manage
    bzr checkout lp:ihris-qualify
    bzr checkout lp:textlayout
    

Preparing For Release
^^^^^^^^^^^^^^^^^^^^^

Updating translations
~~~~~~~~~~~~~~~~~~~~~
In your usual working branch, just before releasing, you should update all of the translation templates with the [[HowTo: Creating Translations#translate_create_templates.php | translate_create_templates.php]] script.

Updating release branches
~~~~~~~~~~~~~~~~~~~~~~~~~
The branches we are using for release should be updated:

.. code-block:: bash

    cd ~/ihris-release/bzr
    bzr update I2CE
    bzr update ihris-common
    bzr update ihris-manage
    bzr update ihris-qualify
    bzr update textlayout
    

Running the Release Program
^^^^^^^^^^^^^^^^^^^^^^^^^^^
We run the release.php script from the ihris-release/bzr directory.  The release script will take care of bumping minor version numbers of changed modules, "bzr tag"ging the branches with a "4.1.X-release" tag, creating tarballs and uploading the tarballs to launchpad. 

.. code-block:: bash

    cd ~/ihris-release/bzr
    php I2CE/tools/release.php
    
  

Answers to questions
^^^^^^^^^^^^^^^^^^^^

* use /Users/litlfred/ihris-release to store release branches and tarballs? (Yes/No): y
* Work with the following directories I2CE,ihris-common,ihris-manage,ihris-qualify,textlayout? (Yes/No): y
* Check for changes since last release and update versions? (Yes/No): y
* Previous release of I2CE was 4.1.4.  Use 4.1.5 for the next release? (Yes/No): y
* Previous release of ihris-common was 4.1.4.  Use 4.1.5 for the next release? (Yes/No): y
* Previous release of ihris-manage was 4.1.4.  Use 4.1.5 for the next release? (Yes/No): y
* Previous release of ihris-qualify was 4.1.4.  Use 4.1.5 for the next release? (Yes/No): y
* Previous release of textlayout was 4.1.4.  Use 4.1.5 for the next release? (Yes/No): y
* Would you also like to mark the top-level module (ihris-common) as being changed? (Yes/No/Always/neVer): a
* Changes were made to I2CE.  Would you like to bump the version of I2CE from 4.1.4.0 to 4.1.5.0 as part of the 4.1.5 release of I2CE? (Yes/No/Always/neVer): a
* I2CE has uncommitted changes. Commit them? [Assuming that I2CE is bound to launchpad] (Yes/No/Always/neVer/Show): a
* Tag the branch I2CE as 4.1.5-release? (Yes/No/Always/neVer): a
* Create Release Branches? (Yes/No): y
* What is the launchpad name/team to put packages under?: intrahealth+informatics
* Create lp:~intrahealth+informatics/i2ce/4.1.5-release? (Yes/No/Always/neVer): a
* Push to lp:~intrahealth+informatics/i2ce/4.1-release? a
* Create translations ar,cs,fr,sw,pt,pt_BR,et,it,es,tl,de,nl for I2CE? (Yes/No/Always/neVer): a
* Create tarballs? (Yes/No): y
* Upload tarballs to launchpad? (Yes/No): y
* Have you given this program authority by visting? https: //edge.launchpad.net/+authorize-token?oauth_token=sCM6vBLAHBLAHBLAH (Yes/No): y
* *'''BEFORE''' you answer yes, make sure you visit the link and click the "Change Anything" button.  The link will change everytime you use the program so dont use the link above.
* Milestone 4.1.5 has not been created for i2ce.  Create? (Yes/No): y
* Upload tarball to launchpad (/Users/litlfred/ihris-release/ihris-suite-4.1.5.tar.bz2)? (Yes/No/Always/neVer): a
* Milestone 4.1.5 has not been created for ihris-common.  Create? (Yes/No): y
* Milestone 4.1.5 has not been created for ihris-manage.  Create? (Yes/No): y
* Milestone 4.1.5 has not been created for ihris-qualify.  Create? (Yes/No): y
* Milestone 4.1.5 has not been created for ihris-textlayout.  Create? (Yes/No): y

Documenting the Release
^^^^^^^^^^^^^^^^^^^^^^^

Change Log
~~~~~~~~~~

The change log [[iHRIS Suite 4.1 Development]] should be updated with a list of the changes since last release.  Usually I use the "bzr log" to get all the changes since the last release for each of the products, ignore the ones about translation, and then edit them so that they are a bit more legible and try to categorize them a bit (e.g. group changes related to reporting under one bullet)

Hint: If the current release is 4.1.5, you can easily get the revisions since the last release with:

.. code-block:: bash

    cd ~/ihris-release/bzr/ihris-common
    bzr log --line -r tag:4.1.4-release..
    

Release Announcement
~~~~~~~~~~~~~~~~~~~~
A release announcement should be drafted and sent to the core IntraHealth/CapPlus informatics team for review.
Once the release has been approved by all involved it should be posted under:

* the iHRIS Global google group
* The launchpad announcements for the various projects (i2ce, ihris-common, ihris-manage, etc) as well as the super project  `ihris-suite <https://launchpad.net/ihris-suite>`_  e.g
The release announcement should follow the same template as previous announcements and include key changes since the last release.

API Update
~~~~~~~~~~
The API, module list and translation list on the wiki needs to be updated.  This can be done with

.. code-block:: bash

    cd ~/ihris-release/bzr
    php I2CE/tools/wikidoc.php
    

You will be asked for your launchpad name and password.

Wiki Forms and Maps
~~~~~~~~~~~~~~~~~~~
The form maps need to be updated for iHRIS Manage and iHRIS Qualify.  You should make a clean installation of Manage and Qualify and generate the form map according to [[Create a Data Form Map For My Custom Site]].  These maps should be uploaded to the wiki and the link on the pages:

* [[iHRIS Manage Form Fields]]
* [[iHRIS Qualify Form Fields]]
should be updated.  But see below for more instructions.

You will also need to update the wiki page for the forms and fields.  This can be done similar to the way the map was made with:

.. code-block:: bash

     php index.php --page=/formDocumentor/wiki
    

The output of this is the text to upload to the wiki.  When we upload to the wiki we want to keep the other versions around.   Here is what you need to do, for example, with release 4.1.5 of iHRIS Manage.

* [[iHRIS Manage Form Fields (versions)]] Edit this page by adding a new line for the 4.1.5 release.  When you save the page, there will be a red link for the iHRIS Manage Form Fields 4.1.5 as it has not been created.  Click on this link and upload the output of the --page=/formDocumentor/wiki
* `iHRIS Manage Form Fields <http://www.ihris.org/mediawiki/index.php?title=IHRIS_Manage_Form_Fields&redirect=no>`_   Edit this page and change it so that it redirects to the version 4.1.5 of the page

For Qualify, the pages you want are:

* [[iHRIS Qualify Form Fields (versions)]]
* `iHRIS Qualify Form Fields <http://www.ihris.org/mediawiki/index.php?title=IHRIS_Qualify_Form_Fields&redirect=no>`_

