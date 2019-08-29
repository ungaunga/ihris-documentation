Last Mile Initiative
====================

Welcome to IntraHealth Informatics Last Mile Initiative / Community Health Data Collection System Wiki!

This page will have updates on all of the ongoing work being done for the SRA/IntraHealth Last Mile Initiative (hereinafter LMI) / Community Health Data Collection System (hereinafter CHDCS).

What is the Last Mile Initiative / Community Health Data Collection System ?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The overall objective of the USAID Last Mile Initiative (LMI) is to expand rural poor communities’ access to telecommunications using sustainable and scalable approaches in order to improve livelihoods and access to development opportunities.  

Within the context of LMI, the CHDCS project objective is to design, develop, install and pilot usage of a telecommunications-enabled Community Health Services Information System for the health sector in Rwanda. Using the paper-based system already developed by the Twubakane Program as the base, IntraHealth will design an Open Source application for data collection and reporting via cell phones and other mobile devices. The data system will improve the capabilities, impact, and timeliness of the current paper-based system by allowing easier data entry of health service indicators and also improving the ability to measure performance of these indicators against district, national, and global targets.

The automated system itself is designed to rely on a centralized server. Community health workers will browse via mobile phones to the central processor and will be prompted to provide service data on a set of pre-determined indicators. The data collected via the system will then be written to the database. Managers will be able to log into the system to retrieve performance data indicating how well their communities are meeting targets or performing as compared to the district, regional, and/or national averages. The automated system also will support the broadcasting of updates from district, regional, or national authorities that will keep health workers abreast of recent policy changes and disease outbreaks. 

The software package used to support the automated system will accommodate a variety of data entry devices ensuring maximum accessibility from remote areas and will include instructional and supporting documentation, multilingual capabilities, a web interface and a set of standardized reports with options for customizing to local conditions. 

Major implementation steps include:

1)	Manage project and report milestones;

2)	Identify, hire and train local developer and local development support team;

3)	Develop functional requirements; 

4)	Design and develop software application;

5)	Develop user and technical documentation;

6)	Pilot system and make adjustments; and

7)	Develop scalability and sustainability plan. 

System implementation will rely on local development resources and partnerships. Local development efforts will include a full time Open Source developer, senior Open Source development consulting, ICT support for hardware implementation, local trainers, and local monitoring and evaluation support from the existing Twubakane staff.  US-based IntraHealth staff will provide project management leadership and senior systems and development support. Rwanda-based technical assistance from the Twubakane Project will be critical to development of functional requirements and support from TRACplus and the Rwanda Ministry of Health HMIS unit will ensure maximum system integration. 

The implementation plan included below contemplates a one year timeline for system delivery including: local team building, stakeholder development, and creation of system specifications and use cases will span 4 months; pilot software and related material development will span 3 months; software introduction, training, support, and monitoring of two pilot districts will take 3 months; and implementing final improvements will take 2 months. Given the short timeline for delivery, local development staff will be supported by US-based senior advisors as needed. Quarterly travel is planned by project management leadership to ensure all timelines are met and that stakeholders remain actively engaged.

Implementation also will be supported via a partnership with Qualcomm who will provide financial support to cover all hardware and software costs as well as training and documentation.

Partners
^^^^^^^^

* IntraHealth International
* SRA
* Qualcomm - partnership has ended

Contact Information
^^^^^^^^^^^^^^^^^^^

* David Mason – Health Informatics Advisor - dmason@intrahealth.org – 919.313.3555

* Vanessa Spann – Informatics Team Lead

* Mark A. Hershberger – Informatics Team Member – mhershberger@intrahealth.org – 717.271.1084

* Laure Almairac and Jana Scislowicz – Program Support – lalmairac@intrahealth.org - 919.313.229

Activity Plan, Reports, and Updates
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* [[Activity Plan]] [ `PDF Format <http://www.ihris.org/w//upload/LMI_Activity_Timeline_Rwanda_0608.pdf>`_ ]
* [[Weekly Updates]]
* [[Monthly Updates]]
* [[Quarterly Reports]]

Technical Documentation
^^^^^^^^^^^^^^^^^^^^^^^

[[Installation Documentation]] [ `pdf <http://www.ihris.org/w//upload/Install.pdf>`_ ]

[[Developer Documentation]] [ `pdf <http://www.ihris.org/w//upload/Developer.pdf>`_ ]

[[Administrative Documentation]] [ `pdf <http://www.ihris.org/w//upload/Admin.pdf>`_ ]

[[Community Health Worker User Documentation]] [ `pdf <http://www.ihris.org/w//upload/CHW.pdf>`_ ]

Implementation
^^^^^^^^^^^^^^

We will store data and forms in  `OpenMRS <http://www.openmrs.org/>`_ .  OpenMRS provides analysis tools and can be integrated with Rwanda's [[TRACnet]] using  `Kettle <http://kettle.pentaho.org/>`_ .  In-depth, custom reports can be generated using  `BIRT <http://www.eclipse.org/birt/phoenix/>`_  and the  `OpenMRS ODA plugin for BIRT <http://openmrs-birt-oda.blogspot.com/2008/08/birt-oda-tutorial-screencast.html>`_ .

We will develop form presentation on capable handhelds.  This would enable health care workers to collect data via the fairly pervasive mobile network in Rwanda. Identifying and developing for specific handhelds with Qualcomm's help will be a high priority but a system which will work on a wide range of handhelds will be developed if time does not permit the acquisition of specific devices.

(Diagrams of this possible pilot implementation:  `PDF format <http://wiki.ihris.org/wiki/index.php/Image:Lmi-platform.pdf>`_  and  `Inkscape SVG source <http://wiki.ihris.org/wiki/index.php/Image:Lmi-platform.svg>`_ 

Translation for Forms and Menus
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

 `Kinyarwanda translation interface <https://translations.launchpad.net/rwanda-pilot/trunk/+pots/lmi-rwanda-pilot/rw/+translate>`_ 

If network connectivity is good enough, you can  `edit translations or view suggested translations <https://translations.launchpad.net/rwanda-pilot/trunk/+pots/lmi-rwanda-pilot/rw/+translate>`_  (from other Launchpad-hosted projects) online.  If you would rather use a desktop application, download and install  `Poedit <http://www.poedit.net/download.php>`_  as well as the  `.pot translations template <http://launchpadlibrarian.net/17157504/lmi-rwanda-pilot_lmi-rwanda-pilot.pot>`_ .

If you edit the translations offline, you'll need to upload the <tt>.po</tt> file produced to Launchpad or [mailto:mhershberger@intrahealth.org mail it to me.]

For context, you can walk through the  `current screens <http://open.intrahealth.org/lmi/>`_  online.

Original Paper Data Collection Forms
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* [ `Children Register PDF Format <http://wiki.ihris.org/wiki/index.php/Image:Child_Register.pdf>`_ ]
* [ `Women Register PDF Format <http://wiki.ihris.org/wiki/index.php/Image:Register_for_Women.pdf>`_ ]
* [ `Household Form PDF Format <http://wiki.ihris.org/wiki/index.php/Image:Household_Form.pdf>`_ ]

Use Cases
^^^^^^^^^

* [[System Use Cases]] [ `PDF Format <http://www.ihris.org/w//upload/LMI_Use_Cases_071808.pdf>`_ ]

Official Health Indicators
^^^^^^^^^^^^^^^^^^^^^^^^^^

1.	Number of infants less that 12 months of age completely vaccinated in the preceding month

2.	Number of children aged 12 to 23 months who received one dose of vitamin A during  the last month

3.	Number of children aged 12 to 23 months who have received a Mebendazole-based de-parasite treatment during the last month

4.	Number of feverish children aged 6-59 months who received one dose of anti-malarial medication at the community level in the last month

5.	Number of children aged 2-59 months suspected to have pneumonia and treated at the community level during the last month

6.	Number of children aged 0 to 59 months suffering from diarrhea and treated with oral rehydration salts and zinc at the community level in the last month

7.	Number of home deliveries during the last month 

8.	Number of home deliveries where mother and neonate were referred to  health center during the last month

9.	Number of women accompanied for delivery at a health center during the last month  

10.	Total number of deceased children under the age of 5 in the last month

11.	Number of couples sent to the health center for family planning during the last month

12.	Number of cycles of oral contraceptives distributed in the course of the last month

13.	Number of condoms distributed in the last month 

14.	Number of couples sent to health center for PMTCT services in the last month

15.	Total number of deaths in the last month

Sustainability and Pilot Plan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

[[LMI Sustainability and Pilot Plan]]

[[Media:LMI_Sustainability.doc|Sustainability & Pilot Plan (.doc version)]]

[[Media:LMI_Sustainability.pdf|Sustainability & Pilot Plan (PDF version)]]

Press Plan
^^^^^^^^^^

Last Mile Initiative Rwanda
IntraHealth International, SRA, Qualcomm
DRAFT Media Plan as of 12 May 2008

* Goal

Utilize local and international media attention to support the project. Especially to increase access to community support resources including open source developers and user groups and potential local partners in the areas of health and telecommunications.

* Stakeholders

Qualcomm

SRA and USAID

IntraHealth (IH)

Rwanda Ministry of Health (MOH)

* Activities

Develop efficient control and approval system for public materials. Meet with Qualcomm, SRA and Rwanda Ministry of Health (MOH) to determine boundaries and requirements for communicating with the public. Identify required terminology and logos. Identify PR contact from each organization. PR contacts to provide approval for release of information and serve as point of contact for media.

Due date: by end of May

Develop project launch joint release for US and local distribution. Collect quotes from community health workers and Ministry staff for use in releases. Post on IntraHealth (IH) website and other partner’s websites. Release to IH professional and media lists. Launch release to highlight in-country needs and how system will meet those needs through personal stories, opportunities for local collaboration and international partnerships. 

Suggested release date: May 28th at the Global Health Council

Official pilot launch event to happen at the end of September once the pilot has started OR at the end of the pilot in January 2009. Official pilot launch to include an event at community facility where local leaders, partners and media are invited.

Develop case studies for distribution in the US and Rwanda. Collect stories from community health workers, Twubakane staff and Ministry staff for use in release. Prepare images to accompany release. Post on IntraHealth (IH) web site. Release to local and regional media including Kigali’s New Times, AllAfrica.com and BalacingAct-Africa.com. Also, release to IH professional and media lists and selected international and regional contacts. Pilot release to have the greatest press emphasis and to highlight how the creative use of appropriate, ubiquitous technologies can have a significant impact on critical health issues. Release to emphasize personal stories, collaboration with local partners and potential impact both locally and regionally. This would be an ongoing activity throughout the pilot.

Target three to four key media contacts for larger international media coverage. Using materials developed for media releases, cultivate selected high-level press contacts for maximum coverage. As possible, prepare special stories and photographs to create unique, compelling story line. This can be done during the official launch.

Include CHDCS project information on existing IH and partner online resources. Online resources include reference on IH Informatics site and blog. Integrate CHDCS code and developer resources into existing IH tools for open source development community (Wiki, LaunchPad). Publicize within larger open source community including user groups, conferences and other support resources.

Provide success stories and articles for newsletters including Wireless Reach’s quarterly. 

Include this project in brochures, video submissions and speaking points for executives.

Pictures
^^^^^^^^

* Ikigo Community Health Center [http://www.ihris.org/w//upload/CHW_0308.jpg]
* Ikigo Community Health Workers [http://www.ihris.org/w//upload/Ikigo_Health_Center_0308.jpg]

