Release Notes for Offline iHRIS Bug Fix
================================================

OFFLINE iHRIS version 3.1.1

Release date: 2008-10-09

CONTENTS

1. Contact Information

2. About This Software

3. Fixes in This Release

4. Requirements and Installation

5. Getting Started

6. Known Issues

7. About the Capacity Project

8. License


1. CONTACT INFORMATION

HRIS Strengthening team of the Capacity Project

Web: www.capacityproject.org/hris/

Email: hris@capacityproject.org

Voice: 1-919-313-9100

IntraHealth International

6340 Quadrangle Drive, Suite 200

Chapel Hill NC 27517 USA


2. ABOUT THIS SOFTWARE

The Capacity Project develops in the iHRIS Suite core solutions addressing specific issues in human resources for health (HRH) leadership. The iHRIS Suite is free and Open Source software distributed under the GPL.

iHRIS Manage is a human resources management tool that enables an organization to design and manage a comprehensive human resources strategy. iHRIS Manage helps an organization manage its workforce more effectively and efficiently, while reducing costs and data errors. Using the system, the HR professional can create a hierarchy of positions for an organization based on standard titles, job classifications and job descriptions, even spread over diverse geographic locations, offices and facilities. HR staff can solicit job applications for open positions, assign employees to fill positions and maintain a searchable database of all employees, their identifying information and their qualifications. Managers can track each employee's history with the organization, including their position and salary histories, and record the reason for departure when the employee leaves. iHRIS Manage is primarily intended to be used to manage health care workers employed by a country's Ministry of Health, a hospital or other large health care organization, or a private provider of health care services. However, it may be readily adapted to other types of organizations and workforces.

iHRIS Qualify is a health worker training, licensing and certification tracking system. The system enables a licensing or certification authority for a health worker cadre, such as nurses or physicians, to track data on the complete cadre in a country from pre-service training through attrition. The database captures information about health professionals from the time they enter pre-service training through registration, certification and licensure, and it is updated every time a professional's license or certification is renewed. This system is also capable of tracking continuing medical education attained by health workers, capturing data about foreign-trained workers applying to work within the country and recording out migration verification requests.

iHRIS Plan is planning and modeling software developed to improve how health sector planners and program decision makers plan for their health workforce needs in developing country settings. The software helps planners and decision makers model workforce needs and make effective policy decisions to meet those needs. 

Offline iHRIS provides a way to use all of these tools without a server. Offline iHRIS is intended to be installed on a single desktop and used by a single user. It is designed to be used in locations where there is no or limited Internet access.


3. NEW IN THIS RELEASE

This release is an offline companion to the iHRIS suite of human resource information systems. This is the first release to include an Offline release of iHRIS Plan. This release also includes all the new features in the core iHRIS Manage and iHRIS Qualify 3.1 release:

- Design custom reports for analyzing and aggregating data

- In-service training management module (iHRIS Manage only)

- Evaluate competencies including competencies earned in in-service training (iHRIS Manage only) 


In addition, Offline iHRIS 3.1 has these new features and fixes:

- The user can choose to install one or all of the following: iHRIS Manage, iHRIS Qualify, iHRIS Plan, PHP MyAdmin.

- The user can now set the password for the database.

- The user can choose to install the software for use only on the desktop or on a local area network.

- The user can choose to install three kinds of sample data: base data, medical base data and sample (fictional) data for demonstration purposes. The user can opt not to install any sample data for a clean install.

- Conflict problem with other programs using Apache or MySQL have been resolved.

- From version 3.1 on, upgrades will be handled by the Offline iHRIS installer. However, this version will *not* upgrade from Version 3.0 of Offline iHRIS.


4. REQUIREMENTS AND INSTALLATION

Offline iHRIS requires Windows XP, 500MB hard disk space and 1GB RAM. A web browser is required to run the software. Firefox 2+ (http://www.mozilla.com/en-US/firefox/) or Internet Explorer 7+ (http://www.microsoft.com/windows/downloads/ie/getitnow.mspx) is highly recommended.

For best results, uninstall any previously installed versions of Offline iHRIS before proceeding.

Double-click the self-executing installer and follow the installation instructions to install and setup Offline iHRIS. Do not install version 3.1 in the same directory as a previous version of Offline iHRIS. Choose the default directory for fastest loading. Specify a MySQL password when prompted. If Windows Firewall is running, select the option to unblock the firewall when prompted.


5. GETTING STARTED

Offline iHRIS provides access to the standalone, single-user version of iHRIS Manage, iHRIS Qualify and iHRIS Plan. Select the program you want to run from the main menu. Please be patient as the first load of each system may take several seconds.

You will be prompted to change your password and create a non-administrator user account to get started. Consult the Help for more information.

Each program includes sample data intended for demonstration purposes. Upon first loading a system, you are given the option to load the sample data. You may choose from the following options (for iHRIS Manage and Qualify):

- base data: includes basic data lists such as marital status and countries

- medical base data: includes health-related data lists such as cadres and facilities

- sample data: dataset for the fictional country of Taifafeki, intended for demonstration purposes only

Enabling the data can take a few seconds. Please be patient while it loads.

Once loaded, the sample data can be edited. However, you should not load the demonstration sample data if you intend to enter your own data in the system.

Before starting, read the User's Manual, which can be accessed by clicking the Help button on any screen. The manual section "Before Installing the System" provides helpful worksheets for collecting the data needed to enter in the system.

To navigate among the systems, left-click the iHRIS taskbar icon in the lower right corner of your screen. To quit Offline iHRIS, right-click the icon and choose Exit.

If you have questions or need support, please visit the iHRIS Website by clicking that button on any screen and use the Contact Us form to send us your question. 


6. KNOWN ISSUES

Offline iHRIS 3.1 has the following known issues:

- This version does not upgrade from version 3.0 and must be installed in a different directory than Offline iHRIS 3.0. All subsequent versions will upgrade seamlessly.


7. ABOUT THE CAPACITY PROJECT

The Capacity Project is developing free, Open Source HRIS solutions, distributed under the GPL, to supply health sector leaders and managers with the information they need to assess HR problems, plan effective interventions and evaluate those interventions. We don't provide just software but rather a program of technical assistance and expertise to ensure that the technology is transferred effectively and serves the ability of decision makers to use data to lead and manage. Our participatory approach results in systems that are appropriate for the context in which they are used and sustainable after we leave.

The Capacity Project helps developing countries strengthen human resources for health to better respond to the challenges of implementing and sustaining quality health programs. The Project is funded by the U.S. Agency for International Development (USAID) and implemented by IntraHealth International and partners IMA World Health, JHPIEGO, Liverpool Associates in Tropical Health (LATH), Management Sciences for Health (MSH), PATH and Training Resources Group, Inc. (TRG). Find out more at www.capacityproject.org

Development of this software was made possible by the support of the American people through USAID. The contents are the responsibility of the user and do not reflect the views of USAID, the United States Government or IntraHealth International. 


8. LICENSE

Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.  A copy of the license is included in the section, "GNU Free Documentation License," of the User's Manual.
[[Category:Archived Pages]]
