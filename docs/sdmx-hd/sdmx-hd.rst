SDMX-HD
=======

This describes SDMX-HD implementation for exporting data from iHRIS.

Everything will be handled through the custom reports and form relationship modules

==Form Relationships== 
Add a sub-module of form relationships to allow tagging the form and fields with SDMX-HD data structure. The
tags will optionally applied to any of the following:
*reportform+field
*reportform+field+aggregate   (where aggregate is one of min,max,sum,count,avg)
*+function
*+function+aggreagte  (where aggregate is one of min,max,sum,count,avg)

The tags will summarize the following:
*SMDX Data Structure.  This is most important  see  A.3 of the [[#user guide | user guider]].
**We may need to specify the Dimension(codelist) and Attribute (codelist or text) for the Data Structre
**for code lists see page 87/92 of the [[#user guide| user guide]].  In brief it represent the possible values for that data elment.
**the code lists can be determined automatically in the case of currency or integer
**for mapped values such as code lists or districts, our mapped values may or may be a ISO/external recgonized data set and this may be an issue.  to address this, we need to make sure that all of our database lists can be exported and flagged as being [[#Domain|domain]] specific or not.   then the code lists should be like the componetntized form ids such as <pre>cadre|15@tanznia_ministry_of_health</pre>here the tanzinar_ministry_of_health is the [[#Domain|domain]] while lists like Country would not domain specific and thus would be like: <pre>country|17</pre>.  However, this is not particuallarly ideal as ''country|17' is really only our internal id.  So we should be using the from field ''country+isco_code'' instead of ''country+id'' as the report form field in this case so that we get <pre>country|TZ</pre>
*SMDX Meta Data Structure. this is optional  see  A.4 of the [[#user guide | user guider]]. 

===Domain===
We need to somehow specify the domain for this module which will represent where country/implementation specific database lists such as cadre are applicable to.  For example $domain = 'tanzania_ministy_of_health'  or $domain='tanzaina_CSSC'

==Custom Report Views==
Add functionality to the 'custom report export'  module.   Already there is an XML export. We will add an SDMX-HD export that will be selectively available to a report view according to the following criteria:
 every $reportform+$field(+$aggregate)? or +$function(+a$ggregate)?  in the report view has a SDMX-HD tag in the form relationship.

For report views that meet this critera, we will then export the reports in the SDMX-XML format.  

The metadata will be built from that in the form relationship as well as based on the particular limits that are applied to the report view.

There are actually two exports that need to be done:
*export the Data Structure .XML file which defines the data in that report view.  See a [[#sample meta data export| sample]]
*export the Meta Data .XML file which defines the data in that report view.  See a [[#sample data structure definition| sample]]
*export the actual data for that report. [[#sample data export| sample]]

We should also have the option of exporting all of these at once in a .zip file.

===Export Issues===
If our report view includes the report form field ''district+isco_code'' and the data element is something like ''district|TZ-01'' which represents Arusha according to [http://www.commondatahub.com/live/geography/state_province_region/iso_3166_2_state_codes | this] we need to export according to the code list format [[#example codelist | see sample]]

As an implmenetation detail... do we want to do this through the I2CE_Template system or as a bunch of concatenated strings?    Certainly the later would be quicker, but the former might prove more robust.   In particular we can adda  display methods for each form field:
*processDOM_SDMX()
and then, in the form relationship, we can use the presnence of a processDOM_SDMX() to indicate whether or not to display the meta and data edit dialog.
We could have somehthing like
<source lang='php'>
  public function processDOM_SDMX($template,$node) {
    if ($node->hasAttribute('edit')) {
       switch ($node->getAttribute('smdx')) {
       case 'data_structure':
              //do something to edit the data structure for a report form field
              break;
       case 'meta':
              //do something to edit the meta data content report form field
              break;
       default:
              //do nothing
              break;
       }      
    } else {
       switch ($node->getAttribute('smdx')) {
       case 'data_structure':
              //do something to display the data structure for a report form field
              break;
       case 'meta':
              //do something to display the meta data content for a report form field
              break;
       default:
              //here the actual data value is created
              break;
       }
    }
  }
</source>
we would then need to create .xml template  files for each of the display options.

==Documents==
===user guide===
The SDMX [http://sdmx.org/wp-content/uploads/2009/02/sdmx-userguide-version2009-1-71.pdf user guide]
===example codelist===
Extract SDMX-HD.v1.0 sample1/CUSTOM/WHO/v1.0/codelists/CL_GENDER+WHO+1.0.xml  from [http://groups.google.com/group/sdmx_hd/web/WHO_SDMX_HD.zip?_done=%2Fgroup%2Fsdmx_hd%3F here]
===sample data structure definition===
Extract SDMX-HD.v1.0 sample1/DSD.xml from [http://groups.google.com/group/sdmx_hd/web/WHO_SDMX_HD.zip?_done=%2Fgroup%2Fsdmx_hd%3F here]

===sample meta data export===
Extract /SDMX-HD.v1.0 sample1/MSD.xml from [http://groups.google.com/group/sdmx_hd/web/WHO_SDMX_HD.zip?_done=%2Fgroup%2Fsdmx_hd%3F here]
[[Category:SDMX-HD]][[Blueprints]]
