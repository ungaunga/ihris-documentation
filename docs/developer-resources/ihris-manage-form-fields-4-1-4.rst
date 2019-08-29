IHRIS Manage Form Fields - 4.1.4
================================

These are the forms and fields in iHRIS Manage version 4.0.9
{{otherversions|iHRIS Manage Form Fields}}

There is also a [http://open.intrahealth.org/visualizations/forms-ihris-manage-site-demo_4_1_1_0.gif graphic visualization] of this data. 
'''Warning:''' this is a very large file and you may wish to save it to your desktop instead of viewing it in your browser.



Here is a description of the [[Defining Forms#Field Types|Field types]].
iHRIS Manage - 4.1.4

==access_facility==
The form ''access_facility'' is implemented by the class: [[Class: iHRIS_UserAccessFacility |iHRIS_UserAccessFacility]]
It is a child of the following forms:
*[[#user|user]]
It has the following fields:
*location:
**Header: Facility or Geographic Location
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Unique in {parent} 
**Maps To Forms: [[#country|country]],[[#county|county]],[[#district|district]],[[#facility|facility]],[[#region|region]]
==accident==
The form ''accident'' is implemented by the class: [[Class: iHRIS_Accident |iHRIS_Accident]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*accident_type:
**Header: Accident Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#accident_type|accident_type]]
*end_date:
**Header: End of Applicability
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*followup:
**Header: Follow-up Required
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*occurence_date:
**Header: Date of Occurence
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*persons_involved:
**Header: People Involved
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*start_date:
**Header: Start of Applicability
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
==accident_type==
The form ''accident_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==application==
The form ''application'' is implemented by the class: [[Class: iHRIS_Applicant |iHRIS_Applicant]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*desired_wage:
**Header: Desired Wage
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Maps To Forms: [[#currency|currency]]
*felony:
**Header: Have you ever been convicted of a felony?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*felony_circumstance:
**Header: If yes, give the circumstances.
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*full_time:
**Header: Are you looking for full-time employment?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*hear:
**Header: How did you hear of this opening?
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*hours:
**Header: If no, what hours are you available?
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*other_info:
**Header: In addition to your work history, are there other skills, qualifications or experience we should consider?
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*position:
**Header: Position(s)
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Restrictions: Required
**Maps To Forms: [[#position|position]]
*start_date:
**Header: When can you start?
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
==benefit==
The form ''benefit'' is implemented by the class: [[Class: iHRIS_Benefit |iHRIS_Benefit]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*amount:
**Header: Amount
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Restrictions: Required
**Maps To Forms: [[#currency|currency]]
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*recurrence:
**Header: Recurrence Frequency
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#benefit_recurrence|benefit_recurrence]]
*source:
**Header: Source
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#salary_source|salary_source]]
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*type:
**Header: Benefit Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#benefit_type|benefit_type]]
==benefit_recurrence==
The form ''benefit_recurrence'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==benefit_type==
The form ''benefit_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==cadre==
The form ''cadre'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==classification==
The form ''classification'' is implemented by the class: [[Class: iHRIS_Classification |iHRIS_Classification]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*code:
**Header: Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==competency==
The form ''competency'' is implemented by the class: [[Class: iHRIS_Competency |iHRIS_Competency]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*competency_type:
**Header: Competency Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#competency_type|competency_type]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {competency_type} 
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
==competency_evaluation==
The form ''competency_evaluation'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==competency_type==
The form ''competency_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==confirmation==
The form ''confirmation'' is implemented by the class: [[Class: iHRIS_Confirmation |iHRIS_Confirmation]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*confirmation_type:
**Header: Confirmation Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {parent} 
**Maps To Forms: [[#confirmation_type|confirmation_type]]
*date:
**Header: Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*record:
**Header: Record
**Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]
*valid:
**Header: Valid
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
**Restrictions: Required
==confirmation_type==
The form ''confirmation_type'' is implemented by the class: [[Class: iHRIS_ConfirmationType |iHRIS_ConfirmationType]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*job:
**Header: Associated Job
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#job|job]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {job} 
*probation_period:
**Header: Probationary Period (Months)
**Type: [[Class: I2CE_FormField_INT |INT]]
**Restrictions: Required
==continuing_education==
The form ''continuing_education'' is implemented by the class: [[Class: iHRIS_ContinuingEducation |iHRIS_ContinuingEducation]]
It has the following fields:
*continuing_education_course:
**Header: Continuing Education Course
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#continuing_education_course|continuing_education_course]]
*credit_hours:
**Header: Credit Hours
**Type: [[Class: I2CE_FormField_INT |INT]]
**Restrictions: Required
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
==continuing_education_course==
The form ''continuing_education_course'' is implemented by the class: [[Class: iHRIS_ContinuingEducationCourse |iHRIS_ContinuingEducationCourse]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*credit_hours:
**Header: Credit Hours
**Type: [[Class: I2CE_FormField_INT |INT]]
**Restrictions: Required
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==council==
The form ''council'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==country==
The form ''country'' is implemented by the class: [[Class: iHRIS_Country |iHRIS_Country]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*alpha_two:
**Header: 2 Character Alpha Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*code:
**Header: ISO Numeric Code
**Type: [[Class: I2CE_FormField_INT |INT]]
*location:
**Header: Use for Location Selection
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*primary:
**Header: Primary Country
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
==county==
The form ''county'' is implemented by the class: [[Class: iHRIS_County |iHRIS_County]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*district:
**Header: District
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#district|district]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {district} 
==currency==
The form ''currency'' is implemented by the class: [[Class: iHRIS_Currency |iHRIS_Currency]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*code:
**Header: Currency Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*country:
**Header: Country
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#country|country]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*symbol:
**Header: Symbol
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==degree==
The form ''degree'' is implemented by the class: [[Class: iHRIS_Degree |iHRIS_Degree]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*edu_type:
**Header: Education Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#edu_type|edu_type]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {edu_type} 
==demographic==
The form ''demographic'' is implemented by the class: [[Class: iHRIS_ManageDemographic |iHRIS_ManageDemographic]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*birth_date:
**Header: Date of Birth
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*gender:
**Header: Gender
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#gender|gender]]
*marital_status:
**Header: Marital Status
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#marital_status|marital_status]]
*dependents:
**Header: Number of Dependents
**Type: [[Class: I2CE_FormField_INT |INT]]
==department==
The form ''department'' is implemented by the class: [[Class: iHRIS_Department |iHRIS_Department]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==dependent==
The form ''dependent'' is implemented by the class: [[Class: iHRIS_Dependent |iHRIS_Dependent]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*date_of_birth:
**Header: Date of Birth
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*gender:
**Header: Gender
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#gender|gender]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==disciplinary_action==
The form ''disciplinary_action'' is implemented by the class: [[Class: iHRIS_DisciplinaryAction |iHRIS_DisciplinaryAction]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*action_date:
**Header: Date of Discussion
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*disciplinary_action_reason:
**Header: Reason for Action
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#disciplinary_action_reason|disciplinary_action_reason]]
*disciplinary_action_type:
**Header: Action Taken
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#disciplinary_action_type|disciplinary_action_type]]
*end_date:
**Header: End of Applicability
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*persons_present:
**Header: People Present
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*start_date:
**Header: Start of Applicability
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
==disciplinary_action_reason==
The form ''disciplinary_action_reason'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==disciplinary_action_type==
The form ''disciplinary_action_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==district==
The form ''district'' is implemented by the class: [[Class: iHRIS_District |iHRIS_District]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*code:
**Header: Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {region:country} 
*region:
**Header: Region
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#region|region]]
==edu_type==
The form ''edu_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==education==
The form ''education'' is implemented by the class: [[Class: iHRIS_Education |iHRIS_Education]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*degree:
**Header: Degree
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#degree|degree]]
*institution:
**Header: Institution Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*location:
**Header: Institution Location
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*major:
**Header: Major
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*year:
**Header: Year of Graduation (leave blank if In Progress)
**Type: [[Class: I2CE_FormField_DATE_Y |DATE_Y]]
==employment==
The form ''employment'' is implemented by the class: [[Class: iHRIS_Employment |iHRIS_Employment]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*company_address:
**Header: Company Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*company_name:
**Header: Company Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*company_phone:
**Header: Company Telephone
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*contact_ok:
**Header: Ok to Contact?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*end_date:
**Header: Date Ended (leave blank if still employed)
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*end_position:
**Header: Ending Position
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*end_wage:
**Header: Ending Wage
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Maps To Forms: [[#currency|currency]]
*reason_for_leaving:
**Header: Reason for Leaving
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*responsibilities:
**Header: Job Responsibilities
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*start_date:
**Header: Date Started
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*start_position:
**Header: Starting Position
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*start_wage:
**Header: Starting Wage
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Maps To Forms: [[#currency|currency]]
*supervisor:
**Header: Supervisor
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==establishment==
The form ''establishment'' is implemented by the class: [[Class: iHRIS_Establishment |iHRIS_Establishment]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*amount:
**Header: Number of Health Workers
**Type: [[Class: I2CE_FormField_INT |INT]]
**Restrictions: Required
*establishment_period:
**Header: Establishment Period
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {job_cadre,location} 
**Maps To Forms: [[#establishment_period|establishment_period]]
*job_cadre:
**Header: Job or Cadre
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#cadre|cadre]],[[#job|job]]
*location:
**Header: Facility or Faciltiy Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility|facility]],[[#facility_type|facility_type]]
==establishment_period==
The form ''establishment_period'' is implemented by the class: [[Class: iHRIS_EstablishmentPeriod |iHRIS_EstablishmentPeriod]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*establishment_type:
**Header: Establishment Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#establishment_type|establishment_type]]
*year:
**Header: Year of Applicability
**Type: [[Class: I2CE_FormField_DATE_Y |DATE_Y]]
**Restrictions: Required, Unique in {establishment_type} 
==establishment_type==
The form ''establishment_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==facility==
The form ''facility'' is implemented by the class: [[Class: iHRIS_Facility |iHRIS_Facility]]

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
==facility_contact==
The form ''facility_contact'' is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#facility|facility]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==facility_type==
The form ''facility_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==gender==
The form ''gender'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==id_type==
The form ''id_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==isco_88_major==
The form ''isco_88_major'' is implemented by the class: [[Class: iHRIS_ISCO_88_Major |iHRIS_ISCO_88_Major]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*name:
**Header: Major Group
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==isco_88_minor==
The form ''isco_88_minor'' is implemented by the class: [[Class: iHRIS_ISCO_88_Minor |iHRIS_ISCO_88_Minor]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*isco_88_sub_major:
**Header: Sub-Major Group
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#isco_88_sub_major|isco_88_sub_major]]
*name:
**Header: Minor Group
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==isco_88_sub_major==
The form ''isco_88_sub_major'' is implemented by the class: [[Class: iHRIS_ISCO_88_Sub_Major |iHRIS_ISCO_88_Sub_Major]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*isco_88_major:
**Header: Major Group
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#isco_88_major|isco_88_major]]
*name:
**Header: Sub-Major Group
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==isco_88_unit==
The form ''isco_88_unit'' is implemented by the class: [[Class: iHRIS_ISCO_88_Unit |iHRIS_ISCO_88_Unit]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*isco_88_minor:
**Header: Minor Group
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#isco_88_minor|isco_88_minor]]
*name:
**Header: Unit
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==job==
The form ''job'' is implemented by the class: [[Class: iHRIS_ManageJob |iHRIS_ManageJob]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*cadre:
**Header: Cadre (Health Professionals Only)
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#cadre|cadre]]
*classification:
**Header: Classification
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#classification|classification]]
*code:
**Header: Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*isco_88_unit:
**Header: ISCO 88 Code
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#isco_88_unit|isco_88_unit]]
*title:
**Header: Title
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*salary_grade:
**Header: Salary Grade
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#salary_grade|salary_grade]]
==language==
The form ''language'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==language_proficiency==
The form ''language_proficiency'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==marital_status==
The form ''marital_status'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==nextofkin==
The form ''nextofkin'' is implemented by the class: [[Class: iHRIS_NextOfKin |iHRIS_NextOfKin]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*relationship:
**Header: Relationship
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==notes==
The form ''notes'' is implemented by the class: [[Class: iHRIS_Notes |iHRIS_Notes]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*date_added:
**Header: Date Added
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*note:
**Header: Note
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
**Restrictions: Required
==person==
The form ''person'' is implemented by the class: [[Class: iHRIS_ManagePerson |iHRIS_ManagePerson]]

This form holds basic information about a person such as their names and residence

It has the child forms:
*[[#accident|accident]]
[[#application|application]]
[[#benefit|benefit]]
[[#confirmation|confirmation]]
[[#demographic|demographic]]
[[#dependent|dependent]]
[[#disciplinary_action|disciplinary_action]]
[[#education|education]]
[[#employment|employment]]
[[#nextofkin|nextofkin]]
[[#notes|notes]]
[[#person_archive_scan|person_archive_scan]]
[[#person_competency|person_competency]]
[[#person_contact_emergency|person_contact_emergency]]
[[#person_contact_other|person_contact_other]]
[[#person_contact_personal|person_contact_personal]]
[[#person_contact_work|person_contact_work]]
[[#person_id|person_id]]
[[#person_language|person_language]]
[[#person_photo_passport|person_photo_passport]]
[[#person_position|person_position]]
[[#person_record_status|person_record_status]]
[[#person_resume|person_resume]]
[[#person_scheduled_training_course|person_scheduled_training_course]]
[[#position_decision|position_decision]]
[[#position_interview|position_interview]]
[[#registration|registration]]
[[#user_map|user_map]]
It has the following fields:
*firstname:
**Header: First Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*nationality:
**Header: Nationality
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#country|country]]
*othername:
**Header: Other Names
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*residence:
**Header: Residence
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#county|county]],[[#district|district]]
*surname:
**Header: Surname
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==person_archive_scan==
The form ''person_archive_scan'' is implemented by the class: [[Class: iHRIS_Archive |iHRIS_Archive]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*date:
**Header: Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*image:
**Header: Image
**Type: [[Class: I2CE_FormField_IMAGE |IMAGE]]
*document:
**Header: Document
**Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]
==person_competency==
The form ''person_competency'' is implemented by the class: [[Class: iHRIS_PersonCompetency |iHRIS_PersonCompetency]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*competency:
**Header: Competency
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {parent} 
**Maps To Forms: [[#competency|competency]]
*competency_evaluation:
**Header: Evaluation
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#competency_evaluation|competency_evaluation]]
*evaluation_date:
**Header: Last Evaluated
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
==person_contact_emergency==
The form ''person_contact_emergency'' is implemented by the class: [[Class: iHRIS_NamedContact |iHRIS_NamedContact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==person_contact_other==
The form ''person_contact_other'' is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==person_contact_personal==
The form ''person_contact_personal'' is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==person_contact_work==
The form ''person_contact_work'' is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==person_id==
The form ''person_id'' is implemented by the class: [[Class: iHRIS_PersonID |iHRIS_PersonID]]

This form holds basic information about an identification for a person

It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*country:
**Header: Country of Issue
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#country|country]]
*expiration_date:
**Header: Date of Expiration
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*id_num:
**Header: Identification Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {id_type} 
*id_type:
**Header: Identification Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {parent} 
**Maps To Forms: [[#id_type|id_type]]
*issue_date:
**Header: Date of Issue
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*place:
**Header: Place of Issue
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==person_language==
The form ''person_language'' is implemented by the class: [[Class: iHRIS_PersonLanguage |iHRIS_PersonLanguage]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*language:
**Header: Language
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique in {parent} 
**Maps To Forms: [[#language|language]]
*reading:
**Header: Reading Proficiency
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#language_proficiency|language_proficiency]]
*speaking:
**Header: Speaking Proficiency
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#language_proficiency|language_proficiency]]
*writing:
**Header: Writing Proficiency
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#language_proficiency|language_proficiency]]
==person_photo_passport==
The form ''person_photo_passport'' is implemented by the class: [[Class: iHRIS_Photo |iHRIS_Photo]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*date:
**Header: Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*description:
**Header: Description
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*image:
**Header: Image
**Type: [[Class: I2CE_FormField_IMAGE |IMAGE]]
==person_position==
The form ''person_position'' is implemented by the class: [[Class: iHRIS_PersonPosition |iHRIS_PersonPosition]]

This form is used to link a person to a pariticular position residence

It has the child forms:
*[[#salary|salary]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*position:
**Header: Position
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#position|position]]
*reason:
**Header: Reason for Departure
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#pos_change_reason|pos_change_reason]]
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
==person_record_status==
The form ''person_record_status'' is implemented by the class: [[Class: iHRIS_Person_Record_Status |iHRIS_Person_Record_Status]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*comment:
**Header: Comments
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*duplicate:
**Header: Duplicate
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*incomplete:
**Header: Incomplete
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*incorrect:
**Header: Incorrect
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
==person_resume==
The form ''person_resume'' is implemented by the class: [[Class: iHRIS_Document |iHRIS_Document]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
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
==person_scheduled_training_course==
The form ''person_scheduled_training_course'' is implemented by the class: [[Class: iHRIS_Person_Scheduled_Training_Course |iHRIS_Person_Scheduled_Training_Course]]
It has the child forms:
*[[#training_course_competency_evaluation|training_course_competency_evaluation]]
[[#training_course_exam|training_course_exam]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*completed:
**Header: Completed
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*duty_commencement_date:
**Header: Duty Commencement
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*is_retraining:
**Header: Retraining
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*request_date:
**Header: Request Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*scheduled_training_course:
**Header: Instance
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#scheduled_training_course|scheduled_training_course]]
*training_course_evaluation:
**Header: Evaluation
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_course_evaluation|training_course_evaluation]]
*training_course_requestor:
**Header: Requested By
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#training_course_requestor|training_course_requestor]]
==pos_change_reason==
The form ''pos_change_reason'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==position==
The form ''position'' is implemented by the class: [[Class: iHRIS_Position |iHRIS_Position]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*code:
**Header: Position Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Unique 
*comments:
**Header: Position Comments
**Type: [[Class: I2CE_FormField_STRING_TEXT |STRING_TEXT]]
*department:
**Header: Department
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#department|department]]
*description:
**Header: Position Description
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*facility:
**Header: Facility
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#facility|facility]]
*interview_comments:
**Header: Interview Comments
**Type: [[Class: I2CE_FormField_STRING_TEXT |STRING_TEXT]]
*job:
**Header: Job
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#job|job]]
*posted_date:
**Header: Date Posted
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*pos_type:
**Header: Position Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#position_type|position_type]]
*proposed_end_date:
**Header: Proposed End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*proposed_hiring_date:
**Header: Proposed Hiring Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*proposed_salary:
**Header: Proposed Salary
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Maps To Forms: [[#currency|currency]]
*source:
**Header: Source
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#salary_source|salary_source]]
*status:
**Header: Status
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#position_status|position_status]]
*supervisor:
**Header: Supervisor
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#position|position]]
*title:
**Header: Position Title
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
==position_decision==
The form ''position_decision'' is implemented by the class: [[Class: iHRIS_PositionDecision |iHRIS_PositionDecision]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*comments:
**Header: Comments
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*date:
**Header: Date of Decision
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*offer:
**Header: Make a Job Offer?
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*record:
**Header: Record of Decision
**Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]
==position_interview==
The form ''position_interview'' is implemented by the class: [[Class: iHRIS_PositionInterview |iHRIS_PositionInterview]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*comments:
**Header: Comments
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*date:
**Header: Date of Interview
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*person:
**Header: People Attending
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*record:
**Header: Interview Record
**Type: [[Class: I2CE_FormField_DOCUMENT |DOCUMENT]]
==position_status==
The form ''position_status'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==position_type==
The form ''position_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==region==
The form ''region'' is implemented by the class: [[Class: iHRIS_Region |iHRIS_Region]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*code:
**Header: Code
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*country:
**Header: Country
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#country|country]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique in {country} 
==registration==
The form ''registration'' is implemented by the class: [[Class: iHRIS_Registration |iHRIS_Registration]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*council:
**Header: Registration Council
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#council|council]]
*license_expiration:
**Header: License Expiration Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*license_number:
**Header: License Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*registration_date:
**Header: Registration Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*registration_number:
**Header: Registration Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==role==
The form ''role'' is implemented by the class: [[Class: I2CE_Role |I2CE_Role]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*assignable:
**Header: Can Assign To User
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
**Restrictions: Required
*name:
**Header: Role
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*trickle_up:
**Header: Trickle Up
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#role|role]]
==salary==
The form ''salary'' is implemented by the class: [[Class: iHRIS_Salary |iHRIS_Salary]]
It is a child of the following forms:
*[[#person_position|person_position]]
It has the following fields:
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*salary:
**Header: Salary
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Restrictions: Required
**Maps To Forms: [[#currency|currency]]
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
==salary_grade==
The form ''salary_grade'' is implemented by the class: [[Class: iHRIS_SalaryGrade |iHRIS_SalaryGrade]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*end:
**Header: End
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Restrictions: Required
**Maps To Forms: [[#currency|currency]]
*midpoint:
**Header: MidPoint
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Maps To Forms: [[#currency|currency]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*start:
**Header: Start
**Type: [[Class: iHRIS_FormField_CURRENCY |CURRENCY]]
**Restrictions: Required
**Maps To Forms: [[#currency|currency]]
==salary_source==
The form ''salary_source'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==scheduled_training_course==
The form ''scheduled_training_course'' is implemented by the class: [[Class: iHRIS_Scheduled_Training_Course |iHRIS_Scheduled_Training_Course]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*end_date:
**Header: End Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*instructors:
**Header: Instructors
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*location:
**Header: Location
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#county|county]],[[#district|district]]
*name:
**Header: Site
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*num_students:
**Header: Maximum Number of Students
**Type: [[Class: I2CE_FormField_INT |INT]]
**Restrictions: Required
*start_date:
**Header: Start Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*training_course:
**Header: Training Course
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_course|training_course]]
==training_course==
The form ''training_course'' is implemented by the class: [[Class: iHRIS_Training_Course |iHRIS_Training_Course]]

This form holds basic information about a training course

It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*competency:
**Header: Competencies Provided
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#competency|competency]]
*continuing_education_course:
**Header: CEUs Provided
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#continuing_education_course|continuing_education_course]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*passing_score:
**Header: Passing Score For Final Exam
**Type: [[Class: I2CE_FormField_INT |INT]]
*topic:
**Header: Topic
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
*training_course_category:
**Header: Category
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#training_course_category|training_course_category]]
*training_course_status:
**Header: Status
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_course_status|training_course_status]]
*training_funder:
**Header: Training Funders
**Type: [[Class: I2CE_FormField_MAP_MULT |MAP_MULT]]
**Maps To Forms: [[#training_funder|training_funder]]
*training_institution:
**Header: Training Institution
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#training_institution|training_institution]]
==training_course_category==
The form ''training_course_category'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==training_course_competency_evaluation==
The form ''training_course_competency_evaluation'' is implemented by the class: [[Class: iHRIS_Training_Course_Competency_Evaluation |iHRIS_Training_Course_Competency_Evaluation]]
It is a child of the following forms:
*[[#person_scheduled_training_course|person_scheduled_training_course]]
It has the following fields:
*competency:
**Header: Competency
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#competency|competency]]
*competency_evaluation:
**Header: Evaluation
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#competency_evaluation|competency_evaluation]]
*evaluation_date:
**Header: Evaluation Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
==training_course_evaluation==
The form ''training_course_evaluation'' is implemented by the class: [[Class: iHRIS_Training_Course_Evaluation |iHRIS_Training_Course_Evaluation]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*competency_evaluation:
**Header: Competency Evaluation
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#competency_evaluation|competency_evaluation]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==training_course_exam==
The form ''training_course_exam'' is implemented by the class: [[Class: iHRIS_Training_Course_Exam |iHRIS_Training_Course_Exam]]
It is a child of the following forms:
*[[#person_scheduled_training_course|person_scheduled_training_course]]
It has the following fields:
*evaluation_date:
**Header: Evaluation Date
**Type: [[Class: I2CE_FormField_DATE_YMD |DATE_YMD]]
**Restrictions: Required
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*score:
**Header: Score
**Type: [[Class: I2CE_FormField_INT |INT]]
**Restrictions: Required
*training_course_exam_type:
**Header: Exam Type
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required
**Maps To Forms: [[#training_course_exam_type|training_course_exam_type]]
==training_course_exam_type==
The form ''training_course_exam_type'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==training_course_requestor==
The form ''training_course_requestor'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==training_course_status==
The form ''training_course_status'' is implemented by the class: [[Class: I2CE_SimpleList |I2CE_SimpleList]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*name:
**Header: Name
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required, Unique 
==training_funder==
The form ''training_funder'' is implemented by the class: [[Class: iHRIS_ListByCountry |iHRIS_ListByCountry]]
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
==training_funder_contact==
The form ''training_funder_contact'' is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#training_funder|training_funder]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==training_institution==
The form ''training_institution'' is implemented by the class: [[Class: iHRIS_ListByCountry |iHRIS_ListByCountry]]
It has the child forms:
*[[#training_institution_contact|training_institution_contact]]
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
==training_institution_contact==
The form ''training_institution_contact'' is implemented by the class: [[Class: iHRIS_Contact |iHRIS_Contact]]
It is a child of the following forms:
*[[#training_institution|training_institution]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*address:
**Header: Mailing Address
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*alt_telephone:
**Header: Alternate Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*email:
**Header: Email Address
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*fax:
**Header: Fax Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*mobile_phone:
**Header: Mobile Phone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
*notes:
**Header: Notes
**Type: [[Class: I2CE_FormField_STRING_MLINE |STRING_MLINE]]
*telephone:
**Header: Telephone Number
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
==user==
The form ''user'' is implemented by the class: [[Class: I2CE_User_Form |I2CE_User_Form]]
It has the child forms:
*[[#access_facility|access_facility]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*password:
**Header: Password (leave blank to keep the same password)
**Type: [[Class: I2CE_FormField_STRING_PASS |STRING_PASS]]
*role:
**Header: Role
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Maps To Forms: [[#role|role]]
*username:
**Header: Username
**Type: [[Class: I2CE_FormField_STRING_LINE |STRING_LINE]]
**Restrictions: Required
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
==user_map==
The form ''user_map'' is implemented by the class: [[Class: iHRIS_UserMap |iHRIS_UserMap]]
It is a child of the following forms:
*[[#person|person]]
It has the following fields:
*i2ce_hidden:
**Header: Hide
**Type: [[Class: I2CE_FormField_YESNO |YESNO]]
*username:
**Header: Username
**Type: [[Class: I2CE_FormField_MAP |MAP]]
**Restrictions: Required, Unique 
**Maps To Forms: [[#user|user]]

[[Category:Developer Resources]]
