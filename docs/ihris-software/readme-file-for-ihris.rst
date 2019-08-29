README File for iHRIS
=====================

iHRIS Full Suite: Manage, Qualify, Common, I2CE and TextLayout

Version 4.1.10

Release date: 2014-09-15

CONTENTS

1. Contact Information

2. About This Software

3. New Features/Bug Fixes in This Release

4. Hardware and Software Requirements

5. Getting Started

6. Known Issues

7. About Capacity''Plus''



1. CONTACT INFORMATION
^^^^^^^^^^^^^^^^^^^^^^

HRIS Strengthening team of Capacity''Plus''

Web: http://www.ihris.org

Email: hris@capacityplus.org

Voice: 1-919-313-9100

IntraHealth International

6340 Quadrangle Drive, Suite 200

Chapel Hill NC 27517 USA



2. ABOUT THIS SOFTWARE
^^^^^^^^^^^^^^^^^^^^^^

Capacity''Plus'' develops the iHRIS Suite of core software solutions addressing specific issues in human resources for health (HRH) leadership. The iHRIS Suite is free and Open Source software, distributed under the GPL.

 **iHRIS Manage**  is a human resources management tool that enables an organization to design and manage a comprehensive human resources strategy. iHRIS Manage helps an organization manage its workforce more effectively and efficiently, while reducing costs and data errors. Using the system, the HR professional can create a hierarchy of positions for an organization based on standard titles, job classifications and job descriptions, even spread over diverse geographic locations, offices and facilities. HR staff can solicit job applications for open positions, assign employees to fill positions and maintain a searchable database of all employees, their identifying information and their qualifications. Managers can track each employee's history with the organization, including their position and salary histories, and record the reason for departure when the employee leaves. iHRIS Manage is primarily intended to be used to manage health care workers employed by a country's Ministry of Health, a hospital or other large health care organization, or a private provider of health care services. However, it may be readily adapted to other types of organizations and workforces.

 **iHRIS Qualify**  is a health worker training, licensing and certification tracking system. The system enables a licensing or certification authority for a health worker cadre, such as nurses or physicians, to track data on the complete cadre in a country from pre-service training through attrition. The database captures information about health professionals from the time they enter pre-service training through registration, certification and licensure, and it is updated every time a professional's license or certification is renewed. This system is also capable of tracking continuing medical education attained by health workers, capturing data about foreign-trained workers applying to work within the country and recording out migration verification requests. 

 **iHRIS Train**  was developed by teams in Uganda and Kenya to facilitate the management of health worker training programs. It provides a comprehensive view of health worker education, from preservice education at universities or training institutions through regular in-service training. While intended for use at the national level by the Ministry of Health or Ministry of Education, iHRIS Train may also be customized to meet the needs of training institutions, colleges and universities, examination bodies, implementing agencies, and professional councils.

 **iHRIS Plan**  is a workforce planning and modeling solution. It enables decision makers to assess their workforce needs for the next several years, project the expected health workforce over the same time, and make effective policy decisions to close the gap between the two. iHRIS Plan analyzes data collected in iHRIS Manage, iHRIS Qualify, and other health information systems to enable decision makers to understand their future workforce needs and make effective planning and policy decisions. It provides a picture of the current health workforce and projects how that workforce will change based on known influences such as retirement age, the number of trained workers annually entering the workforce, and other factors. This is then compared to projected health workforce needs, illustrating the gap between the two. The decision maker can interactively test various interventions to try to close that gap and immediately assess the effects.

 **iHRIS Common**  includes common page classes, template files and images for the iHRIS Suite of software: iHRIS Manage, iHRIS Qualify and iHRIS Plan.

 **IntraHealth Informatics Core Engine (I2CE)**  is a set of classes for handling database-driven HTML forms with templates and database abstraction. It is the core programming engine for the iHRIS Suite of software. 

 **TexLayout**  is tools to handle text layout designed to create nicely formatted PDF files. This is used to generate PDF versions of reports.



3. NEW FEATURES/BUG FIXES IN THIS RELEASE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

View a full list of new features and bug fixes here: http://wiki.ihris.org/wiki/IHRIS_Suite_4.1_Development



4. HARDWARE AND SOFTWARE REQUIREMENTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following software is required to be installed before installing iHRIS:



* Apache Webserver 2.2+: http://www.apache.org
* MySQL 5.0+: http://www.mysql.com
* PHP 5.2.6+: http://www.php.net
* MDB2 from PEAR: http://pear.php.net/package/MDB2
* MySQL driver from PEAR: http://pear.php.net/package/MDB2_Driver_mysql
* Text Password from PEAR: http://pear.php.net/package/Text_Password
* Console GetOpt from PEAR: http://pear.php.net/package/Console_Getopt
* APC from PECL: http://pecl.php.net/package/APC or http://pecl4win.php.net (Windows)

In order to generate PDF reports, the tcpdf package (http://www.tcpdf.org) is required.

A web browser is required to run the software. Firefox 2+ (http://www.mozilla.com/en-US/firefox/) or Internet Explorer 7+ (http://www.microsoft.com/windows/downloads/ie/getitnow.mspx) is highly recommended.

Optional:



* Tidy from PECL: http://pecl.php.net/package/tidy (included by default for Ubuntu but not Windows)
* GD Php Library: http://www.libgd.org



5. INSTALLATION INSTRUCTIONS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Linux (Ubuntu) installation instructions are available on our wiki: http://wiki.ihris.org/wiki/Technical_Documentation#General_Installation_Instructions

If you have questions or need support, please visit our website (http://www.ihris.org) and use the Contact Us form to send us your question.



6. KNOWN ISSUES
^^^^^^^^^^^^^^^

The following are known bugs in this release of iHRIS. These bugs will be corrected as soon as possible in a subsequent minor release. Please report any bugs to hris@capacityproject.org or by submitting a bug report at https://bugs.launchpad.net/ihris-suite/.


iHRIS Manage
~~~~~~~~~~~~
There are no known issues.


iHRIS Qualify
~~~~~~~~~~~~~
There are no known issues.



7. ABOUT Capacity''Plus''
^^^^^^^^^^^^^^^^^^^^^^^^^

Capacity''Plus'' develops free, Open Source HRIS solutions, distributed under the GPL, to supply health sector leaders and managers with the information they need to assess HR problems, plan effective interventions and evaluate those interventions. We don't provide just software but rather a program of technical assistance and expertise to ensure that the technology is transferred effectively and serves the ability of decision makers to use data to lead and manage. Our participatory approach results in systems that are appropriate for the context in which they are used and sustainable after we leave.

Capacity''Plus'' is a USAID-funded global project focused on the health workforce needed to achieve the Millennium Development Goals. Capacity''Plus'' is led by IntraHealth International, Inc. Find out more at www.capacityplus.org

Development of this software was made possible by the support of the American people through USAID. The contents are the responsibility of the user and do not reflect the views of USAID, the United States Government or IntraHealth International.

[[Category:iHRIS Software]]
