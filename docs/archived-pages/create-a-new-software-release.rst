Create a New Software Release
=============================

This article has been superseded by [[HowTo: Release iHRIS Software | this]].

== Create New Release Branches ==

For each of the packages (I2CE, ihris-common, ihris-manage, etc.) you need to do the following steps.

# Tag the release with the version number and release (4.0.0-release)
 bzr tag '''<version>'''-release
# Push the release to launchpad
 bzr push lp:~intrahealth+informatics/'''<package>'''/'''<version>'''-release

== Create/Edit the Series on Launchpad ==

If this is a new series (like 4.x) then on the main package page under Series click "Register a series" and fill out the information for the new series.

If the series already exists then edit the series and set the series branch to be the new released branch.  Also change the status to Current Stable Release.

You'll do this for every package that is being released.

== Create the Tar Files ==

Now we need to get a fresh checkout to make sure no extra files are hanging around and create the tar files from those.

# Create a directory for this package release then change into it.
 mkdir '''<version>'''
 cd '''<version>'''
# Checkout all the branches we just created by the series name.
 bzr co lp:i2ce/'''<series>''' I2CE
 bzr co lp:textlayout/'''<series>''' textlayout
 bzr co lp:ihris-common/'''<series>''' ihris-common
 bzr co lp:ihris-manage/'''<series>''' ihris-manage
# Create all the necessary tar files excluding any of the .bzr files.
 tar cjf I2CE-'''<version>'''.tar.bz2 --exclude=.bzr* I2CE
 tar cjf I2CE-full-'''<version>'''.tar.bz2 --exclude=.bzr* I2CE textlayout
 tar cjf ihris-common-'''<version>'''.tar.bz2 --exclude=.bzr* ihris-common
 tar cjf ihris-common-full-'''<version>'''.tar.bz2 --exclude=.bzr* I2CE textlayout ihris-common
 tar cjf ihris-manage-'''<version>'''.tar.bz2 --exclude=.bzr* ihris-manage
 tar cjf ihris-manage-full-'''<version>'''.tar.bz2 --exclude=.bzr* I2CE textlayout ihris-common ihris-manage
# When release Qualify and Plan as well, also create the iHRIS Suite tar file.
 tar cjf ihris-suite-'''<version>'''.tar.bz2 --exclude=.bzr* I2CE textlayout ihris-common ihris-qualify ihris-manage ihris-plan

== Create a Release ==

Click on the series page and under Milestones and Releases click "Create milestone" if one hasn't already been created for this release.  Fill out the information and name the milestone the release version number (4.0.0).  Click "Release now" next to the milestone you just created.  Fill out the information and click "Create Release."  Now click on the release you just created.

Here you can add the tar files we just created.  Click "Add download file" and browse to the relevant tar files you created earlier.  There should be two for each package.  Or three for I2CE if you create the iHRIS Suite tar file.  For the description give the version and list of packages included in the tar file.  (I2CE 4.0.0 release with textlayout for I2CE-full-4_0_0.tar.bz2.)  Make sure the File Content Type is Code Release Tarball.
[[Category:Archived Pages]]
