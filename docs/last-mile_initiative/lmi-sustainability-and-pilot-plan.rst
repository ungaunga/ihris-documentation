LMI Sustainability and Pilot Plan
=================================

 **Last Mile Initiative&nbsp;Community Health Data Collection Sustainability and Pilot Plan** 


Introduction
^^^^^^^^^^^^
The Last Mile Initiative Community Health Data Collection project was
designed to allow community volunteers in Rwanda to go door-to-door
and gather important health information from the citizens via mobile
phone. The original scope of the project was to develop the
application and perform a pilot test of it in two districts in
Rwanda. Due to unforeseen political and funding issues that pilot was
not performed and the development process was altered to accommodate
the lack of hardware available to test with.


Development
^^^^^^^^^^^
One success of the work done on LMI has been that the public health
professionals working in conjunction with the Twubakane project
benefited from the process of us reviewing the data collection forms
and the health indicators the forms are based on. Unfortunately for
our development this caused a great deal of dynamic flow to the
indicators and forms which in turn, required us to redo the database
and forms.


OpenMRS
~~~~~~~
It was decided during the development process that the freely
available OpenMRS[#FOOTNOTE-1 1] (Open Medical Records System) was a
perfect fit for this project. OpenMRS provide a stable, flexible
platform to work with when collecting health data. The open-source
system has been under development for many years and has a very robust
community which continually improves it. The community is very engaged
and helpful, providing a good source for support not only in
development, but in usage of the system as well.


Indicators
~~~~~~~~~~
When the project started the Twubakane project had close to 30 health
indicators in which the data collection forms were based on. By the
close of our work that has been narrowed to 15 indicators. While this
is good streamlining for their purposes it does point out the
complications inherent to such a system.Health indicators are always
dynamic as diseases take hold in certain regions or populations and
international focus shifts. It is important to understand and design
for some shift in the indicators over longer periods of time. However,
rapid changes would be detrimental to the data collection process as
well as the availability of developer time in changing the database
schema and front-end forms. The rate of change that happened during
our work was unexpected.&nbsp;&nbsp; &nbsp;


Example: Adding an Indicator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If, for example a new indicator was added the database would have to
be altered to include the new indicator. This would involve adding the
new indicator to the schema however, since we are using OpenMRS the
change would be fairly trivial. In fact, a non-programmer could add
the new indicator via the administrative tools provided with
OpenMRS.Adding the new indicator to the database is only half of what
is needed, the forms which allow the community volunteer to enter the
data are static and would need to be done by hand. While this can be
something a non-developer can learn how to do it would help to have
someone who is fairly comfortable doing so. However, translating that
form to Kinyrwandan (or another language if taken to another country)
would, of course, require some expertise.


Rapid Development
~~~~~~~~~~~~~~~~~
One aspect which we felt we could increase the amount of time and
knowledge needed to make changes to the system was in the development
of the forms themselves (the screens displayed on the phone). OpenMRS
being a Java-based application relies quite heavily on Java for all
aspects of the system. We wanted to have a much easier environment for
making the forms so we wrote an abstraction layer to the system which
allows for easier form creation. This layer, created in PHP, is
open-source and has been given to the OpenMRS community on behalf of
the Last Mile Initiative project. The code for this layer can be found
on the Launchpad site set up for all of our work.


Scalability
~~~~~~~~~~~
Due to the selection of OpenMRS, which utilizes the MySQL database,
all running on Linux, scalability is not a big concern for this
system. The system should be able to handle, conservatively
estimating, over 6000 transactions per hour. It is doubtful that even
if the system were to be rolled out to the whole country that those
numbers would even be realized.Having said that, as with most
countries in the region which Rwanda is in, having the server in a
location which provides stable and strong bandwidth is a concern which
is related to scalability and is one which would benefit from
revisiting from time to time were the system in use. Please refer to
the Pilot section of this document for more on server support issues.


Transparency
^^^^^^^^^^^^
Transparency and openness has been a foundation of this project since
its inception. One original goal was to try to tap into any existing
open source communities working in Africa, or more specifically in the
region around Rwanda to help with the development. Although we made
contact with a couple different groups (further below) since the
development stage was stunted a bit due to the issues around a second
partner for hardware costs these efforts have slowed down. This is not
to say that they are dead though as the work we have done has been
shared with the community and we hope it will gain some traction.This
is the key to why being as open and collaborative as possible is good
for sustainability - it allows for a project to continue to grow even
if there are other factors working against it. In areas such as Rwanda
this can be quite refreshing. When we first approached some of the
main stakeholders in this project we were asked pointedly if our work
would be freely available or would they have to hire "another
specialist from Europe" to work on it once we were gone. That one
moment shows off the importance of an open source license in remote
and poor areas of the world. It can be expensive and difficult to
bring someone in to modify or fix code. If that has to be done simply
because the license will not allow the users to see the code it can be
very frustrating to those on the ground.In order to ensure the
transparency of this project we have taken a few important steps to
make our work as accessible as possible.


Licensing
~~~~~~~~~
All of the work we have done on this project has been licensed under
the GPL[#FOOTNOTE-2 2] (General Public License) which is a fully open
source license. This is very important for sustainability as it allows
anyone in the world to freely acquire, modify, and even redistribute
the code - as long as it is under the same license and includes the
original copyright holders information.In addition to our work's
license, the OpenMRS codebase is also licensed under the GPL making
the two fully compatible.


Community
~~~~~~~~~
It has been important for us since the inception of this project to
make sure that we have been utilizing any communities already in
existence around technologies we are taking advantage of as well as
attempt to form communities around our technologies. While the absence
of a pilot has hampered the creation of communities around our work,
we have been active in the OpenMRS as well as the OpenROSA
communities. Any work we have done has been announced to the
appropriate community and made freely available to them. At the time
of writing this document there has already been a great deal of
interest in the Rapid Development library which was created for this
project. This could lead to an expansion of the library in the future
and a sign that it will continue on even if this project comes to an
end. This is one of the best aspects of being transparent and
collaborative with this work, it has the possibility of living on and
helping many more people in the end.By far, the most useful
information and interest in this project is coming from the two
project listed above. While we did communicate with other groups
(including AVOIR[#FOOTNOTE-3 3], the USAID sponsored open source
community in Africa), we found most groups had waned in activity at
this time. This tends to be the case with open source groups and a
lesson that can be learned for our desire to create community for this
project. If there is a central problem to be solved, and enough people
who desire to see it solved, a community is far easier to build. This
is especially true if there are enough points of entry (or tools to
make it easier).


Launchpad
~~~~~~~~~
One tool we have utilized in the development stage has been
Launchpad[#FOOTNOTE-4 4]. Launchpad is a multi-functional, web-based
tool for development. In addition to code source version control
system, bug tracking system, and easy translation editing tools, it
provides areas for planning and interactions with users (though we
have not taken advantage of the last two). The system was created by
Canonical who are the main sponsors of the Ubuntu linux project so it
is geared toward the creation of open source work. This is important
as it gives us one place to point people to for getting the code -
even as we work on it.


Wiki
~~~~
In addition to Launchpad we have set up a wiki[#FOOTNOTE-5 5] which
contains every piece of information we have written or acquired about
this project. This continues the theme of transparency instilled in
this project which we considered as one goal of the project
itself. Were the pilot to be picked up and launched, the continuation
of transparency would be very easy with these tools and licensing. A
wiki allows anyone to get a registration and edit or add documents to
it. This is true of our wiki and we have also put all information on
the wiki under a GNU Free Documentation License[#FOOTNOTE-6 6] which
is very similar to the GPL.The wiki instance we have running is a
Mediawiki[#FOOTNOTE-7 7] server which is the same wiki software used
(and created by) the Wikipedia project. It is by far the most
recognizable wiki and many people already know the editing options
because of its popularity.


Hardware
^^^^^^^^
This particular project has a strong reliance on numerous, inexpensive hardware. For a country like Rwanda was important to look for hardware which is readily available in-country but still was capable of displaying readable information and accept data input in a manner which was efficient for the volunteers. While there was much discussion about hardware during this project, no single model was ever identified.This is quite important for this project for development. At this time our development focused on least-common denominator hardware and thus is a web-based front-end. However, as explored below, the platform selection can allow for far more interesting interaction. What must be clear for any future implementation is whether *available*  hardware is more important than the development concerns. At this time Rwanda is very limited in the models of phones available. As we were working closely with Qualcomm we tended to focus on the phones available through Rwandatel (the CDMA driven network), however if MTN (the GSM carrier) were looked at the models available would be vastly superior.


Costs
~~~~~
Mobile phone costs in Rwanda tend to run similar to their exact counterparts in Europe, keeping in mind that they are utilizing much older models than Europe currently has available. Pricing for phones ranges from as low as $40(US) to $500(US) with the $500 model being a smart-phone with a full keyboard (though this model is normally not readily available).Considering just the original pilot plan for working with two different health clinics in Rwanda we would have been working with between 20 and 60 volunteers if it had been fully rolled out. While that would have covered quite a few villages (3 to 6 volunteers per village) it still would have been very small in comparison to the number of clinics and villages throughout the country. The costs for phones to accomplish that would be quite high.


Available Platforms
~~~~~~~~~~~~~~~~~~~
The most prominent phone brand in all of Rwanda is Nokia. Nokias, for
the most part, run on the Symbian operating system. This system is the
leading installed embedded operating system for phones worldwide (46%
of all phones use Symbian). Symbian's application layer is an
implementation of Java ME (J2ME). The distinct problem however is that
the older model, smaller phones often do not have a similar
application layer which, in our case, meant that we would not have
been assured of having Java available had we chosen it.Having said
that, for sustainability's sake as well as to combat poor coverage in
certain areas, we would recommend further development to focus on Java
and phone which utilize it in the application layer.Of particular note
is the OpenROSA[#FOOTNOTE-8 8] project. OpenROSA is an open-source
effort to reduce duplication of effort in the area of mobile data
collection. More specifically it is a data collection application
toolkit for J2ME with its first implementation having a strong focus
on OpenMRS usage. Intrahealth has contributed to discussions on the
development of OpenROSA with the Last Mile Initiative as the prime
example of the needs we had for the toolkit.


Lifecycle
~~~~~~~~~
One consideration when thinking of hardware is the life-cycle of a
mobile phone. Small, somewhat fragile devices such as phones are&nbsp;
bound to encounter some problems and are typically easier to replace
than repair. This can have a fairly large impact on the sustainability
of the project.Replacement costs for lost or broken phones must be
worked into the costs of rolling out to any area. One rule of thumb
might be to suggest that for every three operational phones there
should be funds available to purchase one replacement. The choice of
three to one being based on the fact that for each small village there
would be up to three volunteers working at one particular time.


Mobile Network
^^^^^^^^^^^^^^
During the development cycle of this project most of our focus was on
Rwandatel due to our relationship with Qualcomm who are the makers of
the CDMA network technology which Rwandatel uses.&nbsp; Most of the
information below is based on this focus and could be quite different
if MTN, or even both networks were considered for roll-out.


Carriers
~~~~~~~~
The two main carriers in Rwanda are Rwandatel and MTN. While we
focused mostly on Rwandatel, it is important for sustainability to
keep an eye on both especially when considering the growth of the
networks in the more rural areas of the country. **Rwandatel**  -
Rwandatel's history is one which is divided almost equally between
being state-owned and private. It is clear that the government does
not want to own the business as it has sold it off quickly after
resuing it from certain failure. Currently a majority stake of the
company is owned by a Lybian investment firm but there are constant
rumors of its sale to many different companies, most
European. Rwandatel is also the country's wired phone and internet
provider in the country which brings with it some great benefit. In
terms of this project this was most useful in that Rwandatel had
offered to host any servers for the project. Since they are the main
internet provider in the country this is about as good as can be asked
for in terms of bandwidth and stability. **MTN**  - It is safe to say
that MTN is the more stable of the two companies. It is a South
African based company which provides mobile coverage in many countries
throughout Africa. In fact, in most countries in which it has a
presence, it tends to be the leading provider.


Coverage
~~~~~~~~
Coverage in Rwanda is quite good for both mobile networks. However,
the areas in which the higher-end technologies that provide higher
bandwidth are generally only located in Kigali and the areas just
outside Kigali. There are exceptions to this though which, for
Rwandatel, can be seen on the Rwandatel Mobile Coverage Map (2007) on
the LMI wiki[#FOOTNOTE-9 9]. Despite the smaller areas outside of
Kigali, the higher bandwidth technologies are not readily available
despite the mobile coverage as a whole being quite good.We do not have
a similar map for MTN and the situation may be quite different for
them. Furthermore, both networks continue to grow and are upgraded
frequently. This situation may be completely different in a few
years.It is important to note that both *EVDO*  on the CDMA network
and *3G*  on GSM network are technologies which have a very small
presence but are scheduled to be rolled out over the next few years in
Rwanda. Having these two high-bandwidth technologies could be very
important for developing high-end and very useful applications as the
better the bandwidth, the more interesting exchange of data can occur.


Partnerships
~~~~~~~~~~~~
The approach we took with this project relied heavily on the mobile
network companies. In our case, we approached Rwandatel and had
conversations about their role in the project. The two most important
parts for the growth of this project were airtime and
hosting. Airtime, which is detailed below, while cheaper than many
countries, could be expensive were the client to stay as it is and
work mostly with browsing technologies. However, a partnership with
the mobile company in which they donate or discount the airtime used
in the project would save a great deal of money. One particular
question raised by Rwandatel was whether or not the volunteers would
be using these phones for their personal usage when not working on the
project. They were not in favor of this idea although we had looked at
it as one incentive for the volunteers to actually do the
work. Estimating the time it would take for the workers to do the work
and getting just that amount of airtime was one idea explored to
answer this question. Rwandatel was also ready to offer us hosting
services which were referred to previously. Again, in a country where
hosting can be very unstable, we determined that Rwandatel would
provide the most stable offering.


Costs
~~~~~
For mobile network access the costs certainly do depend on any partnerships which could be formed with the two main companies working in Rwanda. However, to get an idea of what kind of costs would be associated with normal usage, both companies work at roughly the same price breakdown:



{| class="prettytable"
| Time Period
| Pre-pay
| Pay-as-you-go

|-
| Peak
| $.16/minute
| $.18/minute

|-
| Off-peak
| $.12/minute
| $.16/minute

|}
If we were to spread this out across multiple phones throughout the
country it would get expensive and could possibly go beyond what the
mobile carriers are willing to donate. However, the numbers which we
were estimating for an initial pilot did not seem to pose a problem
for Rwandatel in terms of donating the airtime, especially when
coupled with the important nature of the work for the welfare of the
country.


Pilot
^^^^^
The pilot for the Community Health Data Collection system was
originally planned for two health centers in Rwanda. The total costs
associated with running the pilot was $150,000(US) which was planned
to be paid for by Qualcomm. Early on in the process Qualcomm changed
the total amount they could give to $75,000(US). In accordance the
plans for the pilot were cut in half and included only one health
center which had only a few villages associated with it. While this
would still have given us a good idea as to the usefulness of the
system to the volunteers who are already gathering the data via the
paper forms, it would have been difficult to guage the connectivity
issues as the health center in consideration was fairly near Kigali
and thus had decent EVDO coverage.After many months of working with
Qualcomm on determining the best hardware and specifications for the
system they decided it was best for them to pull out of the
project. Mostly this came down to changes in Rwanda from the Ministry
of Health in relation to the many pilot projects scheduled across the
country. Rightly, Qualcomm felt that the risks were too great if there
was to no longer be heavy support from the Ministry of
Health.Nonetheless, the following information details some of the
ideas and plans which were being drafted to run the pilot program
which was to have started in December 2008.


Ministry of Health
~~~~~~~~~~~~~~~~~~
The Ministry of Health is a vital partner for any health-related
service or project in Rwanda. It is safe to say that any project
should have the full backing of the Ministry before launching. There
are some very good people in the Ministry and quite a few who
understand technology well. At this time, however, the ministry has
chosen to suspend all pilot programs in country. This was done for a
couple reasons: First, there were far too many pilots launching or
running at the same time. Too many for the Ministry staff to keep up
with. Second, the Ministry decided that they were going to scrap all
of the work that was being done on a country-wide HMIS (Health
Management Information System) so that they could start fresh, with a
new partner, and get it done correctly. Any programs which were to
feed data into this HMIS were then put on hold.As this project is a
pilot and we had hoped to work with the HMIS, it is difficult to say
when the time might be right for attempting to launch a
pilot. Certainly not in the original timeframe. Nonetheless, when
dealing with the Ministry it can ber very useful to get the approval
from the Permanent Secretary. Once done all other issues tend to be
more easily resolved. This can also be a huge thing to leverage when
dealing with other local organizations like the mobile phone carriers.


Volunteers
~~~~~~~~~~
The Volunteers are truly the heart of the whole process. The handling
of the volunteers is all coordinated from the Twubakane project
working on the decentralization of health care in Rwanda. The
volunteers are people from each village who are elected in small
ceremonies to be the health representatives for the village. There is
a bit of prestige in the position and the volunteers do much more than
they are recognized for doing. This is to our great benefit as the
volunteers who are chosen tend to be very motivated .In our pilot
these would be the people using the system on a daily basis. Initially
they would need to be trained in the health center in which they
report (unless travel expenses were used to get them elsewhere). As
part of the existing organization for these volunteers, there are also
volunteer coordinators in the health centers who would be ideal in a
pilot to coordinate lost or stolen phone replacement, passing on
problems or issues, and making sure that the data being entered by
his/her volunteers is accurate. The volunteer coordinators should be
quite useful in any future pilot.


Training
~~~~~~~~
The training for using the system would best be performed in the
health centers from which the volunteers work from. Typically they are
not far from the villages in which the volunteers live and most have
some room or space in which the training could be done. The training
itself would be fairly straight-forward as the volunteers are all
already familiar with the paper forms which contain all of the same
questions. The key portions of the training would be instructing them
on getting to the forms, navigating through the forms, and inputting
the information itself. Further training could be done on the web
front-end so that volunteers and coordinators understand how to check
on the data once it is in the system in order to correct any input
errors or to see any health trends that might need immediate
attention.


Support Structure
~~~~~~~~~~~~~~~~~
For the most part, the reliance on the volunteer coordinators is vital
in the support structure. They can ensure that lost or stolen phones
are replaced, make sure that incorrect data entry problems are
corrected, and generally be a lifeline back to staff in Kigali or the
US. However, as these staff work with the Twubakane project a task
sharing/payment plan would need to be figured out before the work
could begin to avoid confusion on who pays for which tasks and which
people.


Hardware Costs
~~~~~~~~~~~~~~
The plan for hardware in the pilot was to have one mobile phone for
each volunteer (three volunteers per village) a laptop computer with a
mobile network PC Card for the community volunteer coordinator, and a
main server in Kigali.''For more information on hardware please refer
to Section 4.''The phones would range from $30(US) to $500(US), the
laptop would range from $600(US) to $1700(US), and the server would
range from $2000(US) to $3500(US) depending on what is available
in-country at the time.


Personnel
~~~~~~~~~
The personnel would consist of the Volunteer (the numbers would range
depending on how many villages reported to the health center at the
time of launch), the Volunteer Coordinator, and time from an
Measurement and Evaluations expert, a local developer/system
administrator, and one local project manager. The last three people
could be shared with the Twubakane project which would bring their
costs down considerably.


Conclusions
^^^^^^^^^^^
It is clear that a system such as this can be a great success if a number of factors are present. However, these factors must all align well to accomplish the task of making the data collection a more efficient process for the community health workers. The factors at play in this project are: Mobile phone coverage in-country, willing donations from the mobile phone carriers, enough mobile hardware to accomodate all of the volunteers, a strong financial partner to cover the hardware and pilot costs, strong support from the Ministry of Health (or similar institution).With all of these things present, and a schedule which allows for flexible development and training, there could be some positive results of utilizing the mobile networks which are growing so rapidly across Africa. There are a few questions which have to be raised at the same time however. First is the question on whether a small laptop with a mobile network card would not be more efficient in this case. Second is the necessity of having the hardware come from the *currently*  available phones in-country when they may not be good enough for the task at hand given the poor selections.Without being able to test the system and test some of the questions presented here it is hard to have definitive answers. However, what has happened is still a step forward for thinking about efficiency in data collection in such a poor resourced area.We can certainly be particularly proud of the efforts we have contributed to OpenMRS and proud of the reactions we are receiving from their community to our work. We can also be proud of the fact that this work is already useful in the design for a new, very similar project which will be launching in Senegal very soon.These are very interesting times in Africa with mobile networking and are likely to be times that redefine many regions on the continent because of these technologies. If we did nothing more than ask questions for others to think about, we have contributed greatly to this revolution of information.



* http://openmrs.org/wiki/OpenMRS
* http://www.fsf.org/licensing/licenses/gpl.html
* http://avoir.uwc.ac.za/avoir/
* http://www.launchpad.net
* http://wiki.ihris.org/wiki/index.php/Last_Mile_Initiative
* http://www.gnu.org/copyleft/fdl.html
* http://www.mediawiki.org/wiki/MediaWiki
* http://www.openrosa.org/
* http://wiki.ihris.org/wiki/upload/RURA_coverage_Regional_boundaries.xls



Addendum: Rwandatel mobile coverage map - 2007 [[http://wiki.ihris.org/wiki/upload/RURA_coverage_Regional_boundaries.xls]]
[[Category:Last Mile Initiative]]
