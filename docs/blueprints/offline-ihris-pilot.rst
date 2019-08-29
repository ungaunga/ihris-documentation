Offline iHRIS Pilot
===================

= Offline iHRIS Pilot =

The pilot implementation (to be ready by January 2008) will provide a remote offices access to iHRIS data that they can view without Internet Access.

The pilot will also provide the opportunity for users to enter their site-specific data and export it so that  it can be imported into the main site.

At this point, only read access will be provided for data not owned by the local site.  Additionally, I plan to restrict the parent site from updating data owned by a remote site.  I'm doing this to avoid the question of data synchronization for the pilot.

- Creating an installer for Offline iHRIS
- Creating a web-interface to import data

== Installer ==

I will adapt the [http://www.wampserver.com/ WAMP setup] to install iHRIS along with Apache and
MySQL.

== Web Interface ==

I will provide a simple UI to import any other site's data as well as export the data local to the site.

== Implementation Details ==

I'll add a UUID field to each record field along with an owner field.

* When a record is updated, the owner will be verified as the current site.  If the current site is not the owner, the update will not be allowed to continue.

* When a record is displayed, editing will be disabled if the current site is not the owner.

* The export screen will export records owned by the site identified by the global UUID (and not export the database's ID column).  Optionally, the user will have the opportunity to export ''all'' records, not just those owned by the site.

* The import will ignore any records it owns since only it can update records.  Any records not owned by the site will either be inserted or updated since the local site.

== Future Work ==

* Make it possible to move a record from one site to another.
* If a user identifies two records with the different UUIDs that should be merged, a new record will be created and a note will be made that the two old UUIDs map to the new UUID.  The UUID mapping would be put into the transaction log.
* It should be possible to use a Bayesian algorithm to determine which way to resolve most conflicts.  These conflicts should be grouped according to certainty: least certain to most, so that a user can scan the list and see the ones most likely needing resolution at the top.
* Investigate using SQLite as the database backend.  If it would work this would reduce the complexity required for OfflineIHRIS as it would not require a database running.
* Investigate [http://wapache.sourceforge.net/ WApache] as an alternative to WAMP.  Combined with SQLite, this provides the intriguing possibility of getting rid of all Windows Services required to run OfflineIHRIS.
* If WApache proves unsuitable, perhaps PHP-GTK would work for providing a serverless front end.

== Synchronization Script ==

Planned post-pilot.  The following description needs to be reviewed and updated.

Synchronization will be handled by a replaying a transaction log of changes.

* Each piece of data that can be synchronized tracked by iHRIS has a UUID assigned to them by the system.  UUIDs, like MySQL auto-increment ID columns are Write-Once-Read-Many, but, unlike MySQL column IDs, uniquely identify the data across installations so that data can be safely moved between installations.
* Each change is logged with a time stamp and the UUID the change applied to.
* To sync instances, the log is replayed and changes without conflicts are applied.
* Any conflicts are put into a review queue for manual resolution.

--[[User:MarkAHershberger|MarkAHershberger]] 13:06, 26 November 2007 (EST)

[[Category:Blueprints]]
