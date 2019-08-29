Offline iHRIS
=============

The Problem
^^^^^^^^^^^

We need to facilitate data collection and data entry in a decentralized, non-networked environment (such as at the district level in Rwanda where this will be piloted). Currently, paper and Excel spreadsheets are the primary data collection tools. Someone from central HQ drives out to physically collect the data once a quarter and then re-enters the data at the central level. We would like to enable people collecting data at the district level (in a hospital or health facility) to enter the same types of data as the centralized iHRIS system and then synchronize that data to the central database.

In addition to entering data, users will want to receive some data from the central server either as synchronization, or more likely, as paper reports.

 *What is the authoritative source of the data? Does data entered at the district level overwrite data entered at the central server, or vice versa?* 

Some Notes on Context
~~~~~~~~~~~~~~~~~~~~~

* People have developed internal systems; we need to "encourage" them to use a consistent system by making it easier and less work.
* Most computers are 2-3 years old and do have a Web browser.
* People are very security conscious and want to be assured that data will be protected.
* People already feel very comfortable using Microsoft Access as an offline tool.
* Emailing a file is possible in larger districts, but connectivity is not available reliably.
* Everybody has mobile access and wants a new cell phone.
* Everybody has a flash drive and loves them; they understand and use them frequently.

Requirements (Initial)
~~~~~~~~~~~~~~~~~~~~~~

* Develop for the lowest common denominator; reduce as much as possible training and support needs
* Similar user interface to the main iHRIS interface for consistency and to reduce training
* Should not be very different from systems that are already in use
* Two-way data synchronization or method for getting data into and receiving reports from the central system
* Data must be kept secure
* Multiple solutions are ideal; consider paper, Excel/Access, flash drives and handheld devices
* Add tracking within the iHRIS system to track districts that are making updates and each district's technology and connectivity level

IT Department Concerns
~~~~~~~~~~~~~~~~~~~~~~

* How will we support it?

We will strive to keep the number of new components to a minimum.  We will test the system and provide documentation for troubleshooting any problems that arise.

* How will we train users?

The web form is familiar to most users who have seen a web browser.  With a minimum amount of training, users should be able to adapt their current workflow to the system.  Additionally, integration with the regional and state-wide systems as well as ready access to the information will provide users with an incentive to learn and use the system.

* Why not use Access

Where possible we will provide an interface for Access through ODBC.  Because of synchronisation issues we cannot build this directly in Access.

Initial Direction for Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Just some initial notes and an initial direction.

* Concentrate on data collection.
* Keep it simple, easy to support and fail-safe.

David and I agreed that the quickest way to get the fastest results
would be to put the iHRIS application on a Flash Disk or USB stick that
Windows computers could run.  This would include making sure that we
found a lightweight web server (probably not Apache).  Currently, the
database back end is MySQL, but I'm pretty sure that we can replace that
with an embedded SQLite Database.

Sample End User Scenario
~~~~~~~~~~~~~~~~~~~~~~~~

The end-user scenario:
<blockquote>
Jim at the central office ships Jane a flash disk.  When Jane puts
the flash disk into her computer, a local copy of the database is
created and a browser appears.  Jane logs in and begins using the
iHRIS application as if she were online.
</blockquote><blockquote>
Jane can pass the flash disk to her co-workers so that they get
copies of the data.  If her co-workers want to share data with her,
they can sync with the flash disk from within the web application
and give it back to her.
</blockquote><blockquote>
Periodically, Jim ships new flash disks to Jane.  Included in the
instructions are directions to synchronize her local database data
to the flash disk.
</blockquote><blockquote>
Jane returns the old flash disk to Jim and he uses a screen in the
administrative console to sync the flash disk with the central
database.  The flash disk can then be returned to Jane or to any
other remote user.
</blockquote>

 *Note* :

* Data integrity checks are performed at every step.  Whenever a sync happens, we need to make sure that the data is correct.

* iHRIS can present forms in the user's language as long as the browser is set to request pages in that language.

* All the iHRIS functionality is available in offline mode.  Reports should all be pre-cached when the flash disk is synced.

* This system provides multiple, distributed backups of the data.  At some later point, the datasets may become too large to deal with this way, but at this point, our datasets would reasonably fit on a flash disk.

* Local users can share data even in a non-networked environment using the flash disk and “Sneaker-Net”.

* Security becomes extremely important.  I need to come up with a good way to protect the data as it travels.  Additionally, we need to make it hard for data to enter the system maliciously without impeding regular use too much.

Plans for initial Pilot
^^^^^^^^^^^^^^^^^^^^^^^

See [[Offline iHRIS Pilot]]

Other Ideas
^^^^^^^^^^^

As I said, that is probably the quickest solution we can present.  Other
ideas that would probably take more time but that we should think about
pursuing:

* Some sort of wireless PDA application.  Since wireless access is so ubiquitous, it would prove worthwhile to find a way to provide access   to the data this way.

* `Google Gears <http://gears.google.com/>`_  provides a way to embed an application entirely the browser and synchronize it with the server when online access is   available.

* By making the back-end accessible via  `REST <http://en.wikipedia.org/wiki/Representational_State_Transfer>`_  calls (i.e. it serves up data structures instead of raw HTML) and the front-end dynamically   generated by Javascript, it would allow use to make the most use of   something like Google Gears.  This allows the end user who sometimes   has access to the Internet to sync up without the use of sending  flash disks out.

