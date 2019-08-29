IHRIS Qualify Form Fields - 4.0.9
=================================

These are the forms and fields in iHRIS Qualify version 4.0.9
{{otherversions|iHRIS Qualify Form Fields}}

There is also a  `graphical visualization <http://open.intrahealth.org/visualizations/forms-ihris-qualify-site-demo_4_0_9_0.gif>`_  of this data. 
 **Warning:**  this is a very large file and you may wish to save it to your desktop instead of viewing it in your browser.



Here is a description of the [[Defining Forms#Field Types|Field types]].

iHRIS Qualify - 4.0.9.0

academic_level
^^^^^^^^^^^^^^
The form *academic_level*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique

archived_report
^^^^^^^^^^^^^^^
The form *archived_report*  is implemented by the class: [[Class: I2CE_ArchivedReport |I2CE_ArchivedReport]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* report:
* *Header: Report
* *Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]
* date:
* *Header: Generation Date
* *Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
* *Restrictions: Required
* report_view:
* *Header: Report View
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Unique in {date}
* name:
* *Header: Title
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required

cadre
^^^^^
The form *cadre*  is implemented by the class: [[Class: iHRIS_Cadre |iHRIS_Cadre]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique
* isco:
* *Header: ISCO Classification Code
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* qualification:
* *Header: Minimum Qualification Required
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Restrictions: Required
* *Maps To Forms: [[#qualification|qualification]]

certificate
^^^^^^^^^^^
The form *certificate*  is implemented by the class: [[Class: iHRIS_Certificate |iHRIS_Certificate]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique in {academic_level}
* academic_level:
* *Header: Academic Level
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Restrictions: Required
* *Maps To Forms: [[#academic_level|academic_level]]

contact
^^^^^^^
The form *contact*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* address:
* *Header: Mailing Address
* *Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
* telephone:
* *Header: Telephone Number
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* alt_telephone:
* *Header: Alternate Telephone Number
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* fax:
* *Header: Fax Number
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* email:
* *Header: Email Address
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* notes:
* *Header: Notes
* *Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

continuing_education
^^^^^^^^^^^^^^^^^^^^
The form *continuing_education*  is implemented by the class: [[Class: iHRIS_ContinuingEducation |iHRIS_ContinuingEducation]]
It is a child of the following forms:


* [[#training|training]]
It has the following fields:


* continuing_education_course:
* *Header: Continuing Education Course
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Restrictions: Required
* *Maps To Forms: [[#continuing_education_course|continuing_education_course]]
* credit_hours:
* *Header: Credit Hours
* *Type: [[Class: I2CE_FormField_INT |INT]]
* *Restrictions: Required
* start_date:
* *Header: Start Date
* *Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
* *Restrictions: Required
* end_date:
* *Header: End Date
* *Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
* *Restrictions: Required

continuing_education_course
^^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *continuing_education_course*  is implemented by the class: [[Class: iHRIS_ContinuingEducationCourse |iHRIS_ContinuingEducationCourse]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required
* credit_hours:
* *Header: Credit Hours
* *Type: [[Class: I2CE_FormField_INT |INT]]
* *Restrictions: Required

country
^^^^^^^
The form *country*  is implemented by the class: [[Class: iHRIS_Country |iHRIS_Country]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique
* alpha_two:
* *Header: 2 Character Alpha Code
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique
* code:
* *Header: ISO Numeric Code
* *Type: [[Class: I2CE_FormField_INT |INT]]
* primary:
* *Header: Primary Country
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* location:
* *Header: Use for Location Selection
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]

county
^^^^^^
The form *county*  is implemented by the class: [[Class: iHRIS_County |iHRIS_County]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique in {district}
* district:
* *Header: District
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Restrictions: Required
* *Maps To Forms: [[#district|district]]

currency
^^^^^^^^
The form *currency*  is implemented by the class: [[Class: iHRIS_Currency |iHRIS_Currency]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* code:
* *Header: Currency Code
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* country:
* *Header: Country
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Maps To Forms: [[#country|country]]
* symbol:
* *Header: Symbol
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

degree
^^^^^^
The form *degree*  is implemented by the class: [[Class: iHRIS_Degree |iHRIS_Degree]]
It has the following fields:


* i2ce_hidden:
* *Header: Hide
* *Type: [[Class: I2CE_FormField_YESNO |YESNO]]
* name:
* *Header: Name
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* *Restrictions: Required, Unique in {edu_type}
* edu_type:
* *Header: Education Type
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Restrictions: Required
* *Maps To Forms: [[#edu_type|edu_type]]

demographic
^^^^^^^^^^^
The form *demographic*  is implemented by the class: [[Class: iHRIS_QualifyDemographic |iHRIS_QualifyDemographic]]
It is a child of the following forms:


* [[#person|person]]
It has the following fields:


* birth_date:
* *Header: Date of Birth
* *Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
* gender:
* *Header: Gender
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Maps To Forms: [[#gender|gender]]
* marital_status:
* *Header: Marital Status
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Maps To Forms: [[#marital_status|marital_status]]
* birth_location:
* *Header: Birth Location
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Maps To Forms: [[#county|county]],[[#district|district]]

deployment
^^^^^^^^^^
The form *deployment*  is implemented by the class: [[Class: iHRIS_Deployment |iHRIS_Deployment]]
It is a child of the following forms:


* [[#person|person]]
It has the following fields:


* health_facility:
* *Header: Health Facility
* *Type: [[Class: I2CE_FormField_MAP |MAP]]
* *Restrictions: Required
* *Maps To Forms: [[#health_facility|health_facility]]
* job_title:
* *Header: Job/Post Title
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* job_code:
* *Header: Job/Post Code
* *Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
* deployment_date:
* *Header: Deployment Date
* *Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
* *Restrictions: Required

disciplinary_action
^^^^^^^^^^^^^^^^^^^
The form *disciplinary_action*  is implemented by the class: [[Class: iHRIS_DisciplinaryAction |iHRIS_DisciplinaryAction]]
It is a child of the following forms:
*[[#training|training]]
It has the following fields:
*disciplinary_action_reason:
**Header: Disciplinary Action Reason
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#disciplinary_action_reason|disciplinary_action_reason]]
*action_date:
**Header: Date Disciplinary Action Occurred
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_TEXT |STRING_TEXT]]
*suspend:
**Header: Suspend License?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*reinstate_date:
**Header: Reinstatement Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]

disciplinary_action_category
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *disciplinary_action_category*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

disciplinary_action_reason
^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *disciplinary_action_reason*  is implemented by the class: [[Class: iHRIS_DisciplinaryActionReason |iHRIS_DisciplinaryActionReason]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*disciplinary_action_category:
**Header: Disciplinary Action Category
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#disciplinary_action_category|disciplinary_action_category]]

district
^^^^^^^^
The form *district*  is implemented by the class: [[Class: iHRIS_District |iHRIS_District]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {region:country} 
*region:
**Header: Region
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#region|region]]
*code:
**Header: Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

edu_type
^^^^^^^^
The form *edu_type*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

education
^^^^^^^^^
The form *education*  is implemented by the class: [[Class: iHRIS_SecondaryEducation |iHRIS_SecondaryEducation]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*sec_school:
**Header: Secondary School Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*certificate:
**Header: Certificate
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#certificate|certificate]]
*grade:
**Header: Grade Obtained
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*certificate_number:
**Header: Certificate Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

exam
^^^^
The form *exam*  is implemented by the class: [[Class: iHRIS_Exam |iHRIS_Exam]]
It is a child of the following forms:
*[[#training|training]]
It has the following fields:
*try:
**Header: Exam Try
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#exam_try|exam_try]]
*results:
**Header: Exam Results
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#exam_result|exam_result]]
*application_date:
**Header: Application Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*materials_received:
**Header: Materials Received?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*materials_approved:
**Header: Materials Approved?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*endorser_name:
**Header: Endorser Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*endorser_date:
**Header: Endorser Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*endorser_qualifications:
**Header: Endorser Qualifications
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*exam_date:
**Header: Exam Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*exam_number:
**Header: Exam Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

exam_result
^^^^^^^^^^^
The form *exam_result*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

exam_try
^^^^^^^^
The form *exam_try*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

facility
^^^^^^^^
The form *facility*  is implemented by the class: [[Class: iHRIS_Facility |iHRIS_Facility]]

This form is used to descibe basic information about a facility

It has the child forms:
*[[#facility_contact|facility_contact]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*location:
**Header: Location
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#county|county]],[[#district|district]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*facility_type:
**Header: Facility Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility_type|facility_type]]

facility_agent
^^^^^^^^^^^^^^
The form *facility_agent*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

facility_contact
^^^^^^^^^^^^^^^^
The form *facility_contact*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#facility|facility]]
[[#health_facility|health_facility]]
[[#training_institution|training_institution]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

facility_institution
^^^^^^^^^^^^^^^^^^^^
The form *facility_institution*  is implemented by the class: [[Class: iHRIS_FacilityInstitution |iHRIS_FacilityInstitution]]
It has the following fields:
*health_facility:
**Header: Health Facility
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {training_institution} 
**Maps To Forms: [[#health_facility|health_facility]]
*training_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {health_facility} 
**Maps To Forms: [[#training_institution|training_institution]]
*active:
**Header: Active?
**Type: [[Class: I2CE_FormField_BOOL |BOOL]]
**Restrictions: Required

facility_institution_edit_fac
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *facility_institution_edit_fac*  is implemented by the class: [[Class: iHRIS_FacilityInstitutionEditFacility |iHRIS_FacilityInstitutionEditFacility]]
It has the following fields:
*health_facility:
**Header: Health Facility
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#health_facility|health_facility]]
*training_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Restrictions: Required
**Maps To Forms: [[#training_institution|training_institution]]

facility_institution_edit_inst
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *facility_institution_edit_inst*  is implemented by the class: [[Class: iHRIS_FacilityInstitutionEditInstitution |iHRIS_FacilityInstitutionEditInstitution]]
It has the following fields:
*health_facility:
**Header: Health Facility
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Restrictions: Required
**Maps To Forms: [[#health_facility|health_facility]]
*training_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_institution|training_institution]]

facility_status
^^^^^^^^^^^^^^^
The form *facility_status*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

facility_type
^^^^^^^^^^^^^
The form *facility_type*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

gender
^^^^^^
The form *gender*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

generated_doc
^^^^^^^^^^^^^
The form *generated_doc*  is implemented by the class: [[Class: I2CE_GeneratedDoc |I2CE_GeneratedDoc]]
It has the following fields:
*document:
**Header: Document
**Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]
*date:
**Header: Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*primary_form:
**Header: Primary Form ID
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

health_facility
^^^^^^^^^^^^^^^
The form *health_facility*  is implemented by the class: [[Class: iHRIS_HealthFacility |iHRIS_HealthFacility]]
It has the child forms:
*[[#facility_contact|facility_contact]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*location:
**Header: Location
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#county|county]],[[#district|district]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*facility_type:
**Header: Facility Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility_type|facility_type]]
*id_code:
**Header: Identification Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*facility_agent:
**Header: Facility Agent
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility_agent|facility_agent]]
*facility_status:
**Header: Facility Status
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility_status|facility_status]]

id_type
^^^^^^^
The form *id_type*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

institution_inspection
^^^^^^^^^^^^^^^^^^^^^^
The form *institution_inspection*  is implemented by the class: [[Class: iHRIS_InstitutionInspection |iHRIS_InstitutionInspection]]
It is a child of the following forms:
*[[#training_institution|training_institution]]
It has the following fields:
*date:
**Header: Inspection Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_TEXT |STRING_TEXT]]
*pass:
**Header: Passed?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]

license
^^^^^^^
The form *license*  is implemented by the class: [[Class: iHRIS_License |iHRIS_License]]
It is a child of the following forms:
*[[#training|training]]
It has the following fields:
*license_number:
**Header: License Number
**Type: [[Class: I2CE_FormField_INT_GENERATE |INT_GENERATE]]
**Restrictions: Required
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*suspend:
**Header: Suspended?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]

locale
^^^^^^
The form *locale*  is implemented by the class: [[Class: I2CE_Form_Locale |I2CE_Form_Locale]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Locale
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*selectable:
**Header: Selectable
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
**Restrictions: Required, Unique 

marital_status
^^^^^^^^^^^^^^
The form *marital_status*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

notes
^^^^^
The form *notes*  is implemented by the class: [[Class: iHRIS_Notes |iHRIS_Notes]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*note:
**Header: Note
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
**Restrictions: Required
*date_added:
**Header: Date Added
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required

out_migration
^^^^^^^^^^^^^
The form *out_migration*  is implemented by the class: [[Class: iHRIS_OutMigration |iHRIS_OutMigration]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*country:
**Header: Country
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#country|country]]
*new_address:
**Header: Address in new Country
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*out_migration_reason:
**Header: Out Migration Reason
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#out_migration_reason|out_migration_reason]]
*organization:
**Header: Organization Requesting Verification
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*request_date:
**Header: Request Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]

out_migration_reason
^^^^^^^^^^^^^^^^^^^^
The form *out_migration_reason*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

person
^^^^^^
The form *person*  is implemented by the class: [[Class: iHRIS_QualifyPerson |iHRIS_QualifyPerson]]

This form holds basic information about a person such as their names and residence

It has the child forms:
*[[#demographic|demographic]]
[[#deployment|deployment]]
[[#education|education]]
[[#notes|notes]]
[[#out_migration|out_migration]]
[[#person_archive_scan|person_archive_scan]]
[[#person_contact_emergency|person_contact_emergency]]
[[#person_contact_other|person_contact_other]]
[[#person_contact_personal|person_contact_personal]]
[[#person_contact_work|person_contact_work]]
[[#person_id|person_id]]
[[#person_photo_passport|person_photo_passport]]
[[#record_verify|record_verify]]
[[#training|training]]
It has the following fields:
*nationality:
**Header: Nationality
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#country|country]]
*residence:
**Header: Residence
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#county|county]],[[#district|district]]
*surname:
**Header: Surname
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*firstname:
**Header: First Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*othername:
**Header: Other Names
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*home:
**Header: Home
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#county|county]],[[#district|district]]

person_archive_scan
^^^^^^^^^^^^^^^^^^^
The form *person_archive_scan*  is implemented by the class: [[Class: iHRIS_Archive |iHRIS_Archive]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*image:
**Header: Image
**Type: [[Class: I2CE_FormField_IMAGE |IMAGE]]
*date:
**Header: Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*document:
**Header: Document
**Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]

person_contact_emergency
^^^^^^^^^^^^^^^^^^^^^^^^
The form *person_contact_emergency*  is implemented by the class: [[Class: iHRIS_NamedContact |iHRIS_NamedContact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

person_contact_other
^^^^^^^^^^^^^^^^^^^^
The form *person_contact_other*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

person_contact_personal
^^^^^^^^^^^^^^^^^^^^^^^
The form *person_contact_personal*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

person_contact_work
^^^^^^^^^^^^^^^^^^^
The form *person_contact_work*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

person_id
^^^^^^^^^
The form *person_id*  is implemented by the class: [[Class: iHRIS_PersonID |iHRIS_PersonID]]

This form holds basic information about an identification for a person

It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*id_type:
**Header: Identification Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#id_type|id_type]]
*id_num:
**Header: Identification Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required

person_photo_passport
^^^^^^^^^^^^^^^^^^^^^
The form *person_photo_passport*  is implemented by the class: [[Class: iHRIS_Photo |iHRIS_Photo]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*image:
**Header: Image
**Type: [[Class: I2CE_FormField_IMAGE |IMAGE]]
*date:
**Header: Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

private_practice
^^^^^^^^^^^^^^^^
The form *private_practice*  is implemented by the class: [[Class: iHRIS_PrivatePractice |iHRIS_PrivatePractice]]
It is a child of the following forms:
*[[#training|training]]
It has the following fields:
*license_number:
**Header: License Number
**Type: [[Class: I2CE_FormField_INT_GENERATE |INT_GENERATE]]
**Restrictions: Required
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*inspection_results:
**Header: Inspection Results
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*inspection_date:
**Header: Inspection Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*health_facility:
**Header: Health Facility
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#health_facility|health_facility]]

qualification
^^^^^^^^^^^^^
The form *qualification*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

record_verify
^^^^^^^^^^^^^
The form *record_verify*  is implemented by the class: [[Class: iHRIS_RecordVerify |iHRIS_RecordVerify]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*verify_date:
**Header: Verification Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*verify_change:
**Header: Changes Made
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#verify_change|verify_change]]

region
^^^^^^
The form *region*  is implemented by the class: [[Class: iHRIS_Region |iHRIS_Region]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {country} 
*country:
**Header: Country
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#country|country]]
*code:
**Header: Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

registration
^^^^^^^^^^^^
The form *registration*  is implemented by the class: [[Class: iHRIS_Registration |iHRIS_Registration]]
It is a child of the following forms:
*[[#training|training]]
It has the following fields:
*practice_type:
**Header: Practice Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#registration_type|registration_type]]
*registration_number:
**Header: Registration Number
**Type: [[Class: I2CE_FormField_INT_GENERATE |INT_GENERATE]]
**Restrictions: Required, Unique 
*application_date:
**Header: Application Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*registration_date:
**Header: Registration Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required

registration_type
^^^^^^^^^^^^^^^^^
The form *registration_type*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

role
^^^^
The form *role*  is implemented by the class: [[Class: I2CE_Role |I2CE_Role]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*trickle_up:
**Header: Trickle Up
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#role|role]]
*name:
**Header: Role
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*assignable:
**Header: Can Assign To User
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
**Restrictions: Required

training
^^^^^^^^
The form *training*  is implemented by the class: [[Class: iHRIS_Training |iHRIS_Training]]
It has the child forms:
*[[#continuing_education|continuing_education]]
[[#disciplinary_action|disciplinary_action]]
[[#exam|exam]]
[[#license|license]]
[[#private_practice|private_practice]]
[[#registration|registration]]
[[#training_disrupt|training_disrupt]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*out_country:
**Header: Country Trained in
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#country|country]]
*index_num:
**Header: Index Number
**Type: [[Class: I2CE_FormField_INT_GENERATE |INT_GENERATE]]
**Restrictions: Required
*cadre:
**Header: Cadre
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#cadre|cadre]]
*intake_date:
**Header: Intake Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*graduation:
**Header: Graduation Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*trained_outside:
**Header: Trained Outside this Country
**Type: [[Class: I2CE_FormField_BOOL |BOOL]]
*training_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#training_institution|training_institution]]
*out_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

training_disrupt
^^^^^^^^^^^^^^^^
The form *training_disrupt*  is implemented by the class: [[Class: iHRIS_TrainingDisrupt |iHRIS_TrainingDisrupt]]
It is a child of the following forms:
*[[#training|training]]
It has the following fields:
*disruption_reason:
**Header: Disruption Reason
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_disruption_reason|training_disruption_reason]]
*disruption_date:
**Header: Disruption Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*resumption_date:
**Header: Resumption Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]

training_disruption_category
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *training_disruption_category*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

training_disruption_reason
^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *training_disruption_reason*  is implemented by the class: [[Class: iHRIS_TrainingDisruptionReason |iHRIS_TrainingDisruptionReason]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {training_disruption_category} 
*training_disruption_category:
**Header: Training Disruption Category
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_disruption_category|training_disruption_category]]

training_funder
^^^^^^^^^^^^^^^
The form *training_funder*  is implemented by the class: [[Class: iHRIS_ListByCountry |iHRIS_ListByCountry]]
It has the child forms:
*[[#training_funder_contact|training_funder_contact]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*location:
**Header: Location
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#county|county]],[[#district|district]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 

training_funder_contact
^^^^^^^^^^^^^^^^^^^^^^^
The form *training_funder_contact*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#training_funder|training_funder]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

training_institution
^^^^^^^^^^^^^^^^^^^^
The form *training_institution*  is implemented by the class: [[Class: iHRIS_QualifyTrainingInstitution |iHRIS_QualifyTrainingInstitution]]
It has the child forms:
*[[#facility_contact|facility_contact]]
[[#institution_inspection|institution_inspection]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*location:
**Header: Location
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#county|county]],[[#district|district]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*id_code:
**Header: Identification Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*facility_agent:
**Header: Facility Agent
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility_agent|facility_agent]]
*facility_status:
**Header: Facility Status
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility_status|facility_status]]

training_institution_contact
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The form *training_institution_contact*  is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]

training_program
^^^^^^^^^^^^^^^^
The form *training_program*  is implemented by the class: [[Class: iHRIS_TrainingProgram |iHRIS_TrainingProgram]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*training_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_institution|training_institution]]
*cadre:
**Header: Cadre
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {training_institution} 
**Maps To Forms: [[#cadre|cadre]]
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*num_students:
**Header: Number of Students
**Type: [[Class: I2CE_FormField_INT |INT]]

user
^^^^
The form *user*  is implemented by the class: [[Class: I2CE_User_Form |I2CE_User_Form]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*username:
**Header: Username
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*password:
**Header: Password (leave blank to keep the same password)
**Type: [[Class: I2CE_FormField_STRING_PASS |STRING_PASS]]
*role:
**Header: Role
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#role|role]]
*firstname:
**Header: Given name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*lastname:
**Header: Surname
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*email:
**Header: E-mail
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*creator:
**Header: Creator
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]

verify_change
^^^^^^^^^^^^^
The form *verify_change*  is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique


