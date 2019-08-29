Software Release Procedure
==========================

'''The Software Release Procedure is considered out-of-date and is scheduled for revision in 2013.'''

* [[HowTo: Release iHRIS Software]]


Below is the ideal iHRIS release procedure. It includes updating User's Manuals (we have not done this in several releases, but should every release) and updating Use Cases (we have not updated these in years, but they need to be updated). It also includes all pages and links that must be updated, as well as announcements that need to be posted whenever a new version of any of the iHRIS software products is released.

'''NOTE:''' All electronic Toolkit updates will also need to include an additional update to the Toolkit ZIP file, which is used for burning on software and flash drives. The latest ZIP is always located here: http://www.capacityproject.org/hris/hris-toolkit/hris-toolkit.zip NEED TO UPDATE ZIP FILE!

== Release Notes ==

''Note: Release notes are currently out of date.''
* [[README File for iHRIS]] (Manage version 4.1 and Qualify version 4.1) 
* [[README File for iHRIS Plan]] (version 1.0.4)

== User's Manuals (Help) ==

During testing, update the [[iHRIS:Documentation|Help File Originals]] with any procedures that have changed and new features. Update screenshots of changed screens as well. '''NOTE:''' 

Create a book for each user's manual on the wiki. The [http://wiki.ihris.org/wiki/Osi:Books/iHRIS_Manage_User_Manual iHRIS Manage User's Manual] and [http://wiki.ihris.org/wiki/Osi:Books/iHRIS_Qualify_User_Manual iHRIS Qualify User's Manual] has already been created, but will need to be updated if any pages are removed or added. '''NOTE:''' A book for iHRIS Plan will need to be generated.

Generate a new HTML version of the user's manual to include with the software (Luke). Generate a PDF to include in the electronic Toolkit. Upload the PDFs to this location: http://www.capacityproject.org/hris/hris-toolkit/tools/pdf/. See [http://www.capacityproject.org/hris/hris-toolkit/tools/ihris_documentation.html the Software Documentation page] for individual filenames (all website links point here). Also add copies to the electronic Toolkit ZIP file.

'''NOTE:''' If there have been any changes to the [[Data Dictionary - iHRIS 4.1|Data Dictionary]], you will also need to generate that file as a PDF and upload to the electronic Toolkit in the same locations as the user's manuals [http://tokobungasabana.com Toko bunga], [http://tokobungasabana.com Toko bunga jakarta], [http://www.grosir-kosmetik.com/62-glutera.html Glutera].

== Bug Reports and Features Lists (responsibility of Carl/Luke)==

Review all bugs reported in [https://bugs.launchpad.net/ihris-suite Launchpad.] Mark bugs that have been fixed or are in progress. List fixed bugs and new features in [[Development Timelines]].

== Use Cases (Carl/Luke to update this procedure) ==

Update all use cases with changes, resolved issues or new issues. Write new use cases or requirements, if needed to document new features. The original use case files are located on SharePoint in the [https://portal.intrahealth.org/Teamsites/SiteDirectory/powertools/software/default.aspx iHRIS Software Suite Document Library]. You will need CaseComplete to update the files.

'''NOTE:''' There are 4 use case files: one for each of the software programs, and one for use cases that are common to all of the programs in the suite. If you open multiple use case files in CaseComplete, you can print them to the same report.

If there have been changes, generate a new HTML report for each software program: Manage, Qualify and Plan. Be sure to include the shared (Common) use cases in each of these reports. Upload these to the website at this location: http://www.capacityproject.org/hris/suite/. See each software page for individual filenames.

Also generate a new Word report separately for each software program: Common, Manage, Qualify and Plan. I generally edit the Word reports to remove use cases that have not yet been implemented and open issues, so as to prevent confusion. Upload the DOCs to this location: http://www.capacityproject.org/hris/hris-toolkit/tools/doc/. See [http://www.capacityproject.org/hris/hris-toolkit/tools/ihris_documentation.html the Software Documentation page] for individual filenames. Also add copies to the electronic Toolkit ZIP file.

== Draft Announcement (Carl/Luke to send notification and information to Brooke/coordinate with Comms) ==
Draft announcements for two audiences: 
* Implementers (via iHRISdevelopers and iHRISannounce lists)
* Wider Stakeholders (to be posted on blog and used as news briefs)

Include the new version #, summary of any new features, summary of bug fixes, list of language options, link to the development timeline for a full list of changes, links to downloads, and a link to the README files.

== Release Notes (Responsibility of Brooke) ==

Update the README files with the latest version number, release date, new features/bug fixes in the release and known issues with the release. 

* [[README File for iHRIS]] -- Manage and Qualify
* [[README File for iHRIS Plan]] -- Plan

Save each new release file as a README file in TXT format. Upload the README file to the download pages on [https://launchpad.net/ihris-suite Launchpad] for each release.

== Website Software Pages, Features Lists, and Roadmaps (Responsibility of Brooke) ==

For each software release, update the specific software page and the related features lists and roadmaps on the [http://www.capacityproject.org/hris/suite/ website]. The software page should be updated with the latest version number. The features list should be updated with the latest version number, all features available in the latest version, all planned features scheduled for development, and all requested features not yet scheduled. The roadmaps should be updated with the date and location of the latest release and the timeline for planned releases.

* iHRIS Qualify [http://www.capacityplus.org/hris/suite/ihris_qualify.php iHRIS Qualify page], [http://www.capacityproject.org/hris/suite/ihris_qualify_features.php Features], and [http://www.capacityproject.org/hris/suite/ihris_qualify_development.php Roadmap]
* iHRIS Manage [http://www.capacityplus.org/hris/suite/ihris_manage.php iHRIS Manage page], [http://www.capacityproject.org/hris/suite/ihris_manage_features.php Features], and [http://www.capacityproject.org/hris/suite/ihris_manage_development.php Roadmap]
* iHRIS Plan [http://www.capacityplus.org/hris/suite/ihris_plan.php iHRIS Plan page],[http://www.capacityproject.org/hris/suite/ihris_plan_features.php Features], and [http://www.capacityproject.org/hris/suite/ihris_plan_development.php Roadmap]

== Download Links (Brooke's responsibility, Carl/Luke to provide links) ==

Once the software is posted to [https://launchpad.net/ihris-suite Launchpad], update the download links and version numbers on the [http://www.capacityproject.org/hris/suite/ihris_software.php Software Downloads page] on the website. Carl/Luke will provide the links.

Change the link on the Toolkit [http://www.capacityproject.org/hris/hris-toolkit/tools/ihris_software.html iHRIS Software Suite page] to reflect the change in version number.

== Announcements (Responsibility of Brooke, coordinate with Comms) ==

Announce the new release version.

Send the Implementers Announcement to: 

* [http://lists.intrahealth.org/mailman/listinfo/ihris-announce ihris-announce Mailing List]
* [http://lists.intrahealth.org/mailman/listinfo/ihris-developers ihris-developers Mailing List]

Post/send the Wider Audience announcement to: 
* [http://www.capacityproject.org/hris/blog/ HRIS Strengthening Blog]
* [https://launchpad.net/ihris-suite/+announce Launchpad Announcements]
* HRIS team mailing list

In addition, disseminate further by:
* Repurposing blog entry as a news article on CapacityPlus site/IntraHealth site
* Tweeting new release info via iHRIS Twitter account (encourage retweets by CapacityPlus, IntraHealth, IntraHealth Open, etc.)

== Important Information ==
* [[Translations]]
* [[Modules Lists]]

[[Category:Developer Resources]]
