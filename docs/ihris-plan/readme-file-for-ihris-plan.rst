README File for iHRIS Plan
==========================

iHRIS Plan (including iHRIS Common, I2CE and TextLayout)

Version 1.0.4

Release date: 2008-12-02



CONTENTS
^^^^^^^^

1. Contact Information

2. About This Software

3. New Features/Bug Fixes in This Release

4. Hardware and Software Requirements

5. Installation Instructions

6. Known Issues

7. About the Capacity Project



1. CONTACT INFORMATION
^^^^^^^^^^^^^^^^^^^^^^

HRIS Strengthening team of Capacity''Plus''

Web: www.capacityplus.org/hris/

Email: hris@capacityplus.org

Voice: 1-919-313-9100

IntraHealth International

6340 Quadrangle Drive, Suite 200

Chapel Hill NC 27517 USA


2. ABOUT THIS SOFTWARE
^^^^^^^^^^^^^^^^^^^^^^

Capacity''Plus'' offers the iHRIS Suite of core solutions addressing specific issues in human resources for health (HRH) leadership. The iHRIS Suite is free and Open Source software distributed under the GPL.

iHRIS Plan is planning and modeling software developed to improve how health sector planners and program decision-makers plan for their health workforce needs. The software helps planners and decision-makers model workforce needs and make effective policy decisions to meet those needs.

iHRIS Common includes common page classes, template files and images for the iHRIS Suite of software: iHRIS Manage, iHRIS Qualify and iHRIS Plan.

IntraHealth Informatics Core Engine (I2CE) is a set of classes for handling database-driven HTML forms with templates and database abstraction. It is the core programming engine for the iHRIS Suite of software. 

TexLayout is tools to handle text layout designed to create nicely formatted PDF files. This is used to generate PDF versions of reports.


3. NEW FEATURES/BUG FIXES IN THIS RELEASE
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This fixes were made in release 1.0.2:


* Added an option to copy a projection, including all cadres and pool changes in the projection, to speed up data entry.
* A total target number or a health worker-to-population ratio target can be entered for the initial target.
* A maximum value can be entered for a pool change with a percentage increase.
* Projections are now grouped by user-defined categories on the search page.
* The projection graph now charts separately actual data entered for subsequent years for comparison.

Some minor bug fixes were made to version 1.0.2 and released as version 1.0.3. Some minor bug fixes were made to version 1.0.3 and released as version 1.0.4.


4. HARDWARE AND SOFTWARE REQUIREMENTS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following software is required to be installed before installing iHRIS:



* Apache Webserver 2.2+: http://www.apache.org
* MySQL 5.0+: http://www.mysql.com
* PHP 5.2.3+: http://www.php.net
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

Linux (Ubuntu) installation instructions are available on our wiki: http://wiki.ihris.org/wiki/index.php/Linux_%28Ubuntu%29_Installation

Before starting, you should read the User's Manual, which can be accessed by clicking the Help button on any screen. 

If you have questions or need support, please visit the iHRIS Website by clicking that button on any screen and use the Contact Us form to send us your question. 



6. KNOWN ISSUES
^^^^^^^^^^^^^^^

Currently, the Import Data function does not work. This issue will be corrected in an upcoming release.


7. ABOUT Capacity''Plus''
^^^^^^^^^^^^^^^^^^^^^^^^^

Capacity''Plus'' is developing free, Open Source HRIS solutions, distributed under the GPL, to supply health sector leaders and managers with the information they need to assess HR problems, plan effective interventions and evaluate those interventions. We don't provide just software but rather a program of technical assistance and expertise to ensure that the technology is transferred effectively and serves the ability of decision makers to use data to lead and manage. Our participatory approach results in systems that are appropriate for the context in which they are used and sustainable after we leave.

Capacity''Plus'' is a USAID-funded global project focused on the health workforce needed to achieve the Millennium Development Goals. Capacity''Plus'' is led by IntraHealth International, Inc. Find out more at www.capacityplus.org

Development of this software was made possible by the support of the American people through USAID. The contents are the responsibility of the user and do not reflect the views of USAID, the United States Government or IntraHealth International.

[[Category:iHRIS Plan]]
