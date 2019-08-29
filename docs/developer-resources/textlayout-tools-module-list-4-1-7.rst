TextLayout Tools Module List (4.1.7)
====================================

{{otherversions|TextLayout Tools Module List}}
This is a list of all modules available in version 4.1.7-release of the package [https://launchpad.net/textlayout TextLayout Tools]
==tcpdf==
This describes version 4.1.0 of the module tcpdf (tcpdf) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head:/modules/tcpdf  textlayout/modules/tcpdf ]
*Description: This is a wrapper for the tcpdf PDF generation utility
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4 and less than 5
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head:/modules/tcpdf/tcpdf modules/tcpdf/tcpdf] <br/>[[Class: C128AObject (4.1.7) | C128AObject]], [[Class: C128BObject (4.1.7) | C128BObject]], [[Class: C128CObject (4.1.7) | C128CObject]], [[Class: C39Object (4.1.7) | C39Object]], [[Class: I25Object (4.1.7) | I25Object]]
==textlayout==
This describes version 4.1.7.0 of the module Text Layout (textlayout) 
It is the top module of this package
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head:/  textlayout/ ]
*Description: I2CE Text Layout Tool
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4 and less than 5
**[[iHRIS Module List (4.1.7)#tcpdf | tcpdf]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head://lib /lib] ,[http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head://tcpdf /tcpdf] <br/>[[Class: I2CE_Encoding (4.1.7) | I2CE_Encoding]], [[Class: I2CE_FontMetric (4.1.7) | I2CE_FontMetric]], [[Class: I2CE_FontMetricAFM (4.1.7) | I2CE_FontMetricAFM]], [[Class: I2CE_FontMetricMultiDirection (4.1.7) | I2CE_FontMetricMultiDirection]], [[Class: I2CE_FontMetricTTF (4.1.7) | I2CE_FontMetricTTF]], [[Class: I2CE_Hyphen (4.1.7) | I2CE_Hyphen]], [[Class: I2CE_PDF (4.1.7) | I2CE_PDF]], [[Class: I2CE_TextCell (4.1.7) | I2CE_TextCell]], [[Class: I2CE_TextTable (4.1.7) | I2CE_TextTable]], [[Class: I2CE_UTF8 (4.1.7) | I2CE_UTF8]]
**Afm_path: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head://CoreFonts /CoreFonts] 
**Pdf_core: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head://CoreFonts /CoreFonts] 
**Ttf_path: /usr/share/fonts/truetype/** ,/usr/local/share/fonts/truetype/** 
**Hyphen_path: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head://dicts /dicts] ,/usr/share/myspell/dicts 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/textlayout/4.1.7-release/files/head://modules /modules] <br/>[[#tcpdf |tcpdf]]

[[Category:Developer Resources]]
