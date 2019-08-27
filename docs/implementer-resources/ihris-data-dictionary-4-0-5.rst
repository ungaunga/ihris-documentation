iHRIS:Data Dictionary (4.0.5)
================================================

{{otherversions|iHRIS:Data Dictionary}}
<div class="noprint">{{IHRIS_Qualify_user_manual_index}} {{IHRIS_Manage_user_manual_index}}</div>

{| border="1" cellpadding="5"
! Field Name or Value !! Definition !! Alternate Names !! Data Type !! Used In
|-
! 2 character alpha code
| The unique two-character code that identifies a country established by the International Organization for Standards (ISO). || alpha code || text entry || all
|-
! academic level
| The highest level of formal education attained by a person. || educational level || selection || iHRIS Qualify
|-
! address in new country
| The mailing address given by a health worker who is out migrating to a foreign country. || - || text entry || iHRIS Qualify
|-
! administrator
| A role that has full access to all functions in the system; this role is responsible for configuring the system and managing user accounts. || system administrator || value (Role) || all
|-
! alternate telephone number
| A secondary phone number where a person or organization can be reached. || cell phone number, mobile number || text entry || iHRIS Manage, iHRIS Qualify
|-
! amount
| The total amount of a benefit or special payment. || - || selection (from Currency) + number || iHRIS Manage
|-
! applicant
| A person who has applied for an open position. || job applicant || value (from Employee Status) || iHRIS Manage
|-
! application date
| The date a person applied to take an exam, to register as a health worker or for an open position. || application || date || iHRIS Qualify
|-
! available hours
| The number and times of hours a person who is applying for part-time employment is available to work. || hours || text entry || iHRIS Manage
|-
! average salary
| The average annual salary paid to an employee in a particular group, such as a cadre or pool of workers. || - || selection (from Currency) + number || iHRIS Plan
|-
! benefit type
| A type of payment made to an employee that is separate from the employee's salary; the payment may be one-time or recurring.  || benefit, special payment || selection || iHRIS Manage
|-
! birthplace
| The geographical location where a person was born.  || - || selection (Country + Region + District) || iHRIS Qualify
|-
! cadre
| A broad category or subset of health workers characterized by the specific training, degree or other qualifications required to practice or be licensed in that field (i.e., nurse). || health cadre || selection || all
|-
! cadre pool
| A pool of health workers, composing part or all of a cadre, to which assumptions are applied in a workforce projection.  || pool || selection || iHRIS Plan
|-
! category
| A broad subject area. || disciplinary action category, disruption category, projection category, training course category || selection or text entry || iHRIS Manage, iHRIS Qualify, iHRIS Plan
|-
! certificate
| Certifies that a particular academic level has been achieved. || - || selection || iHRIS Qualify
|-
! certificate number
| Identifies a particular certificate issued to a student. || - || text entry || iHRIS Qualify
|-
! classification
| A broad category used to organize jobs; the job classification may or may not be equivalent to the health cadre. || job classification || selection || iHRIS Manage
|-
! closed 
| Position status that designates a position that has been filled by an employee; when a position is marked closed, the organization is not actively hiring for the position. || closed position || value (Position Status) || iHRIS Manage
|-
! code
| Short identifier for an item, usually unique. || - || text entry || iHRIS Manage, iHRIS Qualify
|-
! comments
| Notes about a position, job interview or job offer. || interview comments, position comments || text entry || iHRIS Manage
|-
! company address
| The address of a person's employer. || - || text entry || iHRIS Manage
|-
! company name
| The name of a person's employer. || company, employer, organization || text entry || iHRIS Manage
|-
! company telephone
| The telephone number of a person's employer. || company phone, company telephone number || text entry || iHRIS Manage
|-
! competency
| A skill performed to a specific standard under specific conditions.  || competencies provided || selection || iHRIS Manage
|-
! competency type
| A broad category of related competencies. || - || selection || iHRIS Manage
|-
! contact type
| A preset category of contact information. || - || selection (preset values) || iHRIS Manage, iHRIS Qualify
|-
! continuing education course
| A course that is required for a health worker to renew his/her license while practicing. || continuing education || selection || iHRIS Manage, iHRIS Qualify
|-
! cost
| The amount of money associated with a change in the number of workers based on salary and other associated costs, such as training costs or severance pay. || average cost || selection (from Currency) + number || iHRIS Plan
|-
! cost increase
| An annual increase in the cost associated with a change in the number of workers expressed as a percentage of the original cost. || - || number || iHRIS Plan
|-
! country
| An independent nation state. || nation || selection || all
|-
! country trained in
| A foreign country where a health worker received training. || - || selection (from Country) || iHRIS Qualify
|-
! county
| The smallest geographic subset, typically located within a district. || sector || selection || iHRIS Manage, iHRIS Qualify
|-
! credit hours
| The amount of credit received for completing a continuing education course; health professionals must typically complete a minimum number of credit hours to renew their licenses. || CEU, continuing education unit || number || iHRIS Manage, iHRIS Qualify
|-
! currency
| The medium of exchange of money used in a country or other location. || - || selection || iHRIS Manage, iHRIS Plan
|-
! currency code
| The unique three-letter code used to define a currency established by the International Organization for Standards (ISO). || - || text entry || iHRIS Manage, iHRIS Plan
|-
! currency symbol
| The symbol used to identify a currency, such as dollars. || symbol || text entry || iHRIS Manage, iHRIS Plan
|-
! date disciplinary action occurred
| The date a professional received a disciplinary notice. || disciplinary action date || date || iHRIS Qualify
|-
! data operations manager
| A database management role that is responsible for managing data entry, including verifying and correcting data and updating standard lists in the system. || - || value (Role) || iHRIS Qualify
|-
! data source
| The verifiable source of data entered in the system, such as a census, survey or information system. || - || text entry || iHRIS Plan
|-
! date added
| The date a note was added to a person's record. || - || date || iHRIS Manage, iHRIS Qualify
|-
! date of birth
| A person's birthday. || birthdate || date || iHRIS Manage, iHRIS Qualify
|-
! decision maker
| A role that runs reports in order to view and analyze data, and make health workforce policy and planning decisions. || - || value (Role) || iHRIS Qualify
|-
! degree
| Certifies that a particular academic level has been achieved, usually a higher education program. || - || selection || iHRIS Manage
|-
! department
| A division within an organization, typically around similar job functions and following supervisory lines. || - || selection || iHRIS Manage
|-
! dependent
| A legal dependent, such as a spouse or child. || number of dependents || number || iHRIS Manage
|-
! deployment date
| The date a person is employed in a health facility as a licensed health worker. || deployment || date || iHRIS Qualify
|-
! description
| Additional information about or a definition of an item used in selection menus. || job description || text entry || iHRIS Manage, iHRIS Plan
|-
! desired wage
| The salary that an applicant for a job requests to perform that job. || desired salary || selection (from Currency) + number || iHRIS Manage
|-
! did not sit for exam
| An incomplete or absent result on a qualifying examination. || absent, incomplete || value (Exam Results) || iHRIS Qualify
|-
! disciplinary action reason
| A warning or notice issued to a health professional or employee as a result of an infraction. || disciplinary action, disciplinary notice || selection || iHRIS Qualify
|-
! discontinued 
| A position status that designates a position that is no longer required by an organization; no employee fills it and the organization is not soliciting applications for the position. || discontinued position || value (Position Status) || iHRIS Manage
|-
! display name
| The name of a report or other item that is shown to users of the system. || - || text entry || iHRIS Manage, iHRIS Qualify
|-
! disruption date
| The date a student left a training program. || - || date || iHRIS Qualify
|-
! disruption reason
| The reason why a student left a training program. || discontinuation, disruption, training disruption || selection || iHRIS Qualify
|-
! district
| A smaller geographic unit within a region created by the central government for easy administration. || province, state || selection || iHRIS Manage, iHRIS Qualify
|-
! duration of change
| The number of years that a change affects a workforce projection || - || number || iHRIS Plan
|-
! education type
| The type of qualification or degree a person has received, such as college/university, continuing education or informal. || - || selection || iHRIS Manage
|-
! elementary
| The first level of five in the Interagency Language Roundtable (ILR) scale of language proficiency; a person at this level has a speaking vocabulary which is inadequate to express anything but the most elementary needs. || elementary proficiency, Level 1, S-1 || value (Speaking, Reading or Writing Proficiency) || iHRIS Manage
|-
! email address
| An address where a person or organization can be contacted by email. || email || text entry || iHRIS Manage, iHRIS Qualify
|-
! emergency contact
| The person to notify if there is an emergency involving an employee, including the person's contact information. || - || value (Contact Type) || iHRIS Manage, iHRIS Qualify
|-
! employee 
| A person who is paid by an organization to perform a specific job. || - || value (from Employee Status) || iHRIS Manage
|-
! employee status
| The status of an employee with the organization, such as a current employee, old employee or job applicant. || - || selection (preset values) || iHRIS Manage
|-
! enabled
| Refers to whether a pool change is calculated and displayed in a projection. || - || yes/no || iHRIS Plan
|-
! end date
| The date at which a position, training program, licensing period, etc. ends. || date ended, expiration, license expiration date || date || iHRIS Manage, iHRIS Qualify
|-
! ending position
| The last position that a person held in an organization. || - || text entry || iHRIS Manage
|-
! ending salary
| The salary that a person earned in the last position s/he held in an organization; also the highest salary in a salary grade. || end, end salary, ending wage, last salary || selection (from Currency) + number || iHRIS Manage
|-
! endorser date
| The date a student is endorsed to take the national examination. || - || date || iHRIS Qualify
|-
! endorser name
| A person who recommends a student graduating from a training program to take the national examination. || endorser || text entry || iHRIS Qualify
|-
! endorser qualifications
| The qualifications of a person recommending students to take the national examination. || - || text entry || iHRIS Qualify
|-
! evaluation
| An official assessment of an employee's performance in a class or competency. || competency evaluation, training course evaluation || selection || iHRIS Manage
|-
! exam date
| The date that the qualifying examination is administered to health profession students. || - || date || iHRIS Qualify
|-
! exam number
| The number that identifies a particular examination administered to a student graduating from a health training program. || - || text entry || iHRIS Qualify
|-
! exam results
| The grade received on the test that every student graduating from a health training program must pass in order to qualify for registration. || exam, examination, national examination, results || selection (preset values) || iHRIS Qualify
|-
! exam try
| An attempt by a student to pass the qualifying examination; students are limited to three tries. || - || selection (preset values) || iHRIS Qualify
|-
! executive manager
| A person who may manage the entire organization or one district, department, office or facility within the organization. The Executive Manager views reports and analyzes data entered in the system in order to make HR decisions and set organizational policy. || - || value (Role) || iHRIS Manage
|-
! exit
| A decrease in the supply of workers due to employees leaving the workforce. || - || selection (preset values) || iHRIS Plan
|-
! facility
| A specific division within an organization that is defined by having its own budget and often has a unique facility code. Often a facility is responsible for providing health care services. || duty center, health facility, office, responsibility center || selection || iHRIS Manage, iHRIS Qualify
|-
! facility agent
| The owner of a health facility or training institution, which also refers to the classification of the facility. || agent || selection || iHRIS Qualify
|-
! facility type
| A type of health facility. || - || selection || iHRIS Manage, iHRIS Qualify
|-
! fax number
| A number where a person or organization can be contacted by fax. || fax || text entry || iHRIS Manage, iHRIS Qualify
|-
! fail
| A failing grade on a qualifying examination. || - || value (Exam Results) || iHRIS Qualify
|-
! felony conviction
| A conviction of a crime resulting in prison time. || - || yes/no || iHRIS Manage
|-
! final try
| The third and last attempt to pass the qualifying examination. || - || value (Exam Try) || iHRIS Qualify
|-
! first name
| A person's initial name. || Christian name, firstname, given name, name || text entry || all
|-
! first try
| The initial attempt to pass the qualifying examination. || - || value (Exam Try) || iHRIS Qualify
|-
! fluent
| Native of bilingual proficiency in a language. || bilingual proficiency, Level 5, native proficiency, S-5 || value (Speaking, Reading or Writing Proficiency) || iHRIS Manage
|-
! full professional
| The fourth level of five in the Interagency Language Roundtable (ILR) scale of language proficiency; a person at this level is able to use the language fluently and accurately on all levels normally pertinent to professional needs. || full professional proficiency, Level 4, S-4 || value (Speaking, Reading or Writing Proficiency) || iHRIS Manage
|-
! full-time employment
| Employment for a standard number of hours of working time. || full-time || yes/no || iHRIS Manage
|-
! gender
| Indicates whether a person is male or female. || sex || female/male || iHRIS Manage, iHRIS Qualify
|-
! grade obtained
| A student's official grade upon completing a particular academic level. || grade || text entry || iHRIS Qualify
|-
! graduation date
| Official date of completion of a training program or other educational program. || graduation, year of graduation || date || iHRIS Manage, iHRIS Qualify
|-
! health workforce planner
| A role that has access to the projection creation and modeling functions but cannot configure the system or access user accounts. || - || value (Role) || iHRIS Plan
|-
! hiring date
| The date on which an open position is filled. || filled date, hire date, hire year || TBD || iHRIS Manage
|-
! hiring decision
| The date at which an official decision is made whether to offer a job to an applicant. || date of decision || date || iHRIS Manage
|-
! home residence
| The address or geographical location where a person permanently lives, which may be different from the person's current residence. || permanent residence || selection (Country + Region + District) || iHRIS Qualify
|-
! HR manager
| A manager of human resources personnel who is responsible for managing all system data and for ensuring that data in the system are complete, correct and up to date. || - || value (Role) || iHRIS Manage
|-
! HR staff
| A data entry person in human resources who is responsible for entering and updating data in the system. || - || value (Role) || iHRIS Manage
|-
! identification code
| A unique code used to identify a facility or training institution. || - || text entry || iHRIS Qualify
|-
! identification number
| The unique identifier -- usually a number -- that, when combined with an Identification Type, is used to identify a person. || - || text entry || iHRIS Manage, iHRIS Qualify
|-
! identification type
| An official document (such as Social Security Number, national health insurance or passport) used to identify a person. || identification || selection || iHRIS Manage, iHRIS Qualify
|-
! index number
| The number issued to a student when s/he enters a new pre-service training program. || index || TBD || iHRIS Qualify
|-
! initial year of change
| The first year in a projection that a pool change takes effect; the initial year of change may be the same as the start year of the projection. || initial year || year || iHRIS Plan
|-
! inspection date
| The date when an institution was last inspected. || - || date || iHRIS Qualify
|-
! inspection results
| Certification that a health facility, private practice clinic or training institution is qualified to provide services. || inspection, institution inspection || text entry || iHRIS Qualify
|-
! instructor
| The teacher of a training class. || teacher, trainer || text entry || iHRIS Manage
|-
! intake 
| An increase in the supply of workers due to employees entering the workforce. || - || selection (preset values) || iHRIS Plan
|-
! intake date
| The date a person enters a training program. || - || date || iHRIS Qualify
|-
! interview date
| The date at which a formal meeting to assess the qualifications of a job applicant takes place. || date of interview, interview || date || iHRIS Manage
|-
! ISCO classification code
| A unique code that identifies a job classification using a standard coding system established by the International Standard Classification of Occupations (ISCO) for classifying professions. || - || text entry || iHRIS Qualify
|-
! ISO numeric code
| The unique numeric code that identifies a country established by the International Organization for Standards (ISO). || - || text entry || all
|-
! job
| A general set of qualifications, duties and responsibilities that matches a particular job description and has a unique job code. There may be multiple instances of the same job within an organization. || designation, post || selection (from Job Title) || iHRIS Manage, iHRIS Qualify
|-
! job code
| A unique identifier associated with a particular job that identifies it for the organization. || post code || text entry || iHRIS Manage, iHRIS Qualify
|-
! job offer
| An offer to hire an applicant for a particular position and salary. || make a job offer, offer || yes/no || iHRIS Manage
|-
! job responsibilities
| The duties expected to be performed by a particular job. || duties, responsibilities || text entry || iHRIS Manage
|-
! job title
| The label used to describe a job, or a specific set of duties and responsibilities. || post title, title || text entry || iHRIS Manage, iHRIS Qualify
|-
! language 
| A foreign language other than a person's native language. || - || selection || iHRIS Manage
|-
! last evaluated
| The date at which a person last received an evaluation. || - || date || iHRIS Manage
|-
! license number
| The number issued with a license to practice as a health worker; this number may or may not be identical to the registration number. || - || number || iHRIS Manage, iHRIS Qualify
|-
! limited working
| The second level of five in the Interagency Language Roundtable (ILR) scale of language proficiency; a person at this level is able to satisfy routine social demands and limited work requirements. || Level 2, limited working proficiency, S-2 || value (Speaking, Reading or Writing Proficiency) || iHRIS Manage
|-
! location 
| Refers to the country, region, district and (optionally) county where an organization, institution or facility is located. || geographical location, institution location || selection (from Country + Region + District + County) || iHRIS Manage, iHRIS Qualify
|-
! location selection
| Designates a country that is used for determining geographical location, in addition to selecting a currency or nationality. || - || yes/no || iHRIS Manage, iHRIS Qualify
|-
! mailing address
| An address, including city, country and zip code, where a person or organization can be contacted by mail. || address || text entry || iHRIS Manage, iHRIS Qualify
|-
! major
| Primary field of study. || - || text entry || iHRIS Manage
|-
! marital status
| A person's legal status, such as single, married, divorced or widowed. || - || selection || iHRIS Manage, iHRIS Qualify
|-
! materials approved
| Approval of examination application materials. || - || yes/no || iHRIS Qualify
|-
! materials received
| Examination application materials submitted by an applicant in advance of taking the exam. || - || yes/no || iHRIS Qualify
|-
! maximum amount of change
| The maximum number of health workers that can enter the workforce in a projection. || - || number || iHRIS Plan
|-
! maximum number of students
| The largest number of students accepted into a training course. || - || number || iHRIS Manage
|-
! midpoint
| The average salary offered to new hires in a salary grade, which may not be equivalent to the true average of the salary range within that grade. || - || selection (from Currency) + number || iHRIS Manage
|-
! monthly
| An event that occurs once a month. || - || value (Recurrence Frequency) || iHRIS Manage
|-
! name
| Refers to the value used to create an item for selection menus. || - || text entry || all
|-
! nationality
| The country where a person is a legal citizen. || citizenship || selection (from Country) || iHRIS Manage, iHRIS Qualify
|-
! no access
| A role that prevents a user from accessing the system, or disables the user account. || - || value (Role) || all
|-
! notes
| General information added to a record to provide additional information not accounted for by other fields. || primary contact person || text entry || iHRIS Manage, iHRIS Qualify
|-
! number of employed staff
| The actual number of workers available for deployment. || supply || number || iHRIS Plan
|-
! number of students
| The maximum number of students that can attend a specific training program. || - || number || iHRIS Qualify
|-
! OK to contact
| Specifies whether a person's past employers may be contacted. || - || yes/no || iHRIS Manage
|-
! old applicant
| A person who previously applied for an open position, but who has not applied for any positions that are currently open. || - || value (from Employee Status) || iHRIS Manage
|-
! old employee
| A person who previously worked for an organization but has left the organization. || - || value (from Employee Status) || iHRIS Manage
|-
! once
| An event that occurs only once, or does not recur. || - || value (Recurrence Frequency) || iHRIS Manage
|-
! open 
| A position status that designates a position that is required for the organization to operate and that the organization is actively hiring to fill. || open position || value (Position Status) || iHRIS Manage
|-
! organization requesting verification
| The certifying board or professional council requesting the qualifications of a health worker who is applying to work in a foreign country. || - || text entry || iHRIS Qualify
|-
! other 
| Refers to all values other than those not explicitly listed for selection. || other contact || value (Contact Type) || iHRIS Manage, iHRIS Qualify
|-
! other names
| A person's names other than the first name and surname, usually one or more middle names. || middle name, other name || text entry || all
|-
! out migration reason
| The given by a health worker leaving the country where s/he was trained in order to practice in a foreign country. || out migration || selection || iHRIS Qualify
|-
! pass
| A passing grade on a qualifying examination or on a facility inspection. || passed || value (Exam Results) or yes/no || iHRIS Qualify
|-
! password
| A hidden phrase that provides secure access to the system. || - || text entry || all
|-
! people attending
| The names of the people who attend a job interview. || interviewers || text entry || iHRIS Manage
|-
! percentage change
| An annual change in the number of workers based on a percentage of the available number of workers leaving or entering the workforce. || rate of change || number || iHRIS Plan
|-
! permanent
| A registration type that does not expire. || - || value (Registration Type) || iHRIS Qualify
|-
! personal contact
| Refers to a person's home mailing address, telephone and other contact information. || home, personal || value (Contact Type) || iHRIS Manage, iHRIS Qualify
|-
! pool change
| A change applied to a cadre pool that calculates either an increase or decrease in the number of available health workers in that pool.  || - || selection || iHRIS Plan
|-
! population
| The total number of people inhabiting a specific area, such as a country. || - || number || iHRIS Plan
|-
! population growth rate
| The percentage by which the population of an area will grow annually. || growth rate, population growth || number || iHRIS Plan
|-
! position
| An instance of a job that can be filled by one employee in one facility and represents one box on an organizational chart. || - || selection (from Position Code + Position Title) || iHRIS Manage
|-
! position code
| A unique identifier associated with a particular position that identifies it for the organization. || - || text entry || iHRIS Manage
|-
! position description
| The specific responsibilities for a particular position in addition to the general responsibilities for the job. || - || text entry || iHRIS Manage
|-
! position status
| The status of a position as open, closed (filled) or discontinued. || status || selection (preset values) || iHRIS Manage
|-
! position title
| A specific title different from the job title that defines one particular position within an organization. || title || text entry || iHRIS Manage
|-
! position type
| A classification of a type of position. || - || selection || iHRIS Manage
|-
! post date
| The date a position is opened for hiring. || date posted, posted date || date || iHRIS Manage
|-
! practice type
| The type of registration issued to a health worker. || - || selection (preset values) || iHRIS Qualify
|-
! primary country
| The country that is selected as the primary location for data in the system; more than one country may be set as the primary country. || - || yes/no || all
|-
! primary form
| The form, or related set of data entry fields, on which a report relationship is based. || - || selection || iHRIS Manage, iHRIS Qualify
|-
! professional working
| The third level of five in the Interagency Language Roundtable (ILR) scale of language proficiency; a person at this level is able to speak the language with sufficient structural accuracy and vocabulary to participate effectively in most conversations on practical, social and professional topics. || Level 3, professional working proficiency, S-3 || value (Speaking, Reading or Writing Proficiency) || iHRIS Manage
|-
! projection duration
| The number of years in a projection, usually between 5 and 30 years. Also refers to the number of years that a pool change affects the projection. || duration || number || iHRIS Plan
|-
! projection name
| A calculation of the workforce supply and required workers over time based on workforce data and assumptions made about future changes to the workforce that compares the supply to the requirements and shows the gap between the two.  || graphical model, projection, workforce projection || text entry || iHRIS Plan
|-
! proposed end date
| Date at which funding or the role for a position is tentatively scheduled to end, as distinguished from the end date. || - || date || iHRIS Manage
|-
! proposed hiring date
| Date at which an organization would like to fill an open position, as distinguished from the actual hiring date. || - || date || iHRIS Manage
|-
! proposed salary
| The salary that is proposed for an open position before it has been filled; does not refer to the actual salary for the position. || - || selection (from Currency) + number || iHRIS Manage
|-
! qualification
| Specific educational level, training, competency, skill or experience that a person must have in order to enter a training program, become registered in a cadre or perform a job. || education, minimum qualification required, skill || selection or text entry (job application) || iHRIS Manage, iHRIS Qualify
|-
! rate amount of change increases each year
| The percentage by which the annual change in the number of health workers increases annually. || - || number || iHRIS Plan
|-
! reading proficiency
| A person's reading ability in a foreign language. || - || selection (preset values) || iHRIS Manage
|-
! reason for departure
| A reason given for leaving employment or changing positions within the organization. || reason for leaving || selection; text entry (past employment) || iHRIS Manage
|-
! records officer
| A role that is responsible for basic data entry, including initial indexing and upgrades of health professional students entering training programs, tracking out migration verifications and demographic data entry. || - || value (Role) || iHRIS Qualify
|-
! recurrence frequency
| A regular repetition of a special payment, such as monthly or annually. || recurrence || selection (preset values) || iHRIS Manage
|-
! region
| A major subdivision of a country containing districts. || - || selection || iHRIS Manage, iHRIS Qualify
|-
! registration council
| An organization that registers or licenses health workers to practice in a country. || council, licensing board || selection || iHRIS Manage
|-
! registration date
| The date at which a health worker is issued a registration number. || - || date || iHRIS Manage, iHRIS Qualify
|-
! registration number
| A number that is issued when a health worker enters the profession within a particular cadre; the health worker retains the registration number as the primary identification number as long as s/he is licensed to practice in that cadre in the country. || - || number || iHRIS Manage, iHRIS Qualify
|-
! registration supervisor
| A role that is responsible for data entry related to licensing updates, including entering initial registration, issuing new licenses and license renewals, issuing and renewing private practice licenses, and registering and licensing foreign-trained health care professionals applying to work in the country. || - || value (Role) || iHRIS Qualify
|-
! reinstatement date
| The date a license is reissued to a health worker after a suspension due to a disciplinary action. || reinstatement || date || iHRIS Qualify
|-
! report
| Display of data from the system as a table or graphical chart; typically, filters can be set on a report to determine the range of data displayed.  || - || selection || iHRIS Manage, iHRIS Qualify
|-
! report relationship
| A defined relationship between system forms on which a report is based. || form relationship, relationship || selection || iHRIS Manage, iHRIS Qualify
|-
! request date
| The date that official documentation is requested. || - || date || iHRIS Qualify
|-
! residence
| The location where a person is currently living; this may be different than the person's home residence. || current residence || selection (from Country + Region + District) || iHRIS Manage, iHRIS Qualify
|-
! resumption date
| The date a student returned to a training program that was previously disrupted. || resumption || date || iHRIS Qualify
|-
! re-try
| The second attempt to pass the qualifying examination. || - || value (Exam Try) || iHRIS Qualify
|-
! role
| Determines the activities that a user can perform within the system. || - || selection (preset values) || all
|-
! salary
| The amount an employee is paid per year for a particular job. || current salary, wage || selection (from Currency) + number || iHRIS Manage
|-
! salary grade
| Defines pay ranges for one or more jobs. || band, grade, salary band || selection || iHRIS Manage
|-
! salary increase
| The amount that a salary is increased each year, expressed as a percentage of the salary. || - || number || iHRIS Plan
|-
! salary source
| A monetary source for an employee's salary or special payments that is not the employing organization, such as a donor or nonprofit. || source || selection || iHRIS Manage
|-
! secondary school name
| The school attended before entering a training institution. || high school || TBD || iHRIS Qualify
|-
! shortname
| A unique name used to refer to a report. || relationship short name || text entry || iHRIS Manage, iHRIS Qualify
|-
! site
| The location where a training class is given. || - || text entry || iHRIS Manage
|-
! speaking proficiency
| A person's speaking ability in a foreign language. || - || selection (preset values) || iHRIS Manage
|-
! start date
| The date at which a training program, position, license, etc. begins. || date started || date || iHRIS Manage, iHRIS Qualify
|-
! start year
| The year in which a projection of the workforce begins, for which there is known workforce data. || base year || year || iHRIS Plan
|-
! starting position
| The position that a person held when first employed by an organization. || - || text entry || iHRIS Manage
|-
! starting salary
| The salary that a person earned when first employed by an organization; also the lowest salary in a salary grade. || first salary, start, start salary, starting wage || selection (from Currency) + number || iHRIS Manage
|-
! static change
| An annual change in the number of workers based on a specific number of workers leaving or entering the workforce. || amount of change || number || iHRIS Plan
|-
! status
| The current state of an institution, facility or training course (typically open or closed). || facility status, training course status || selection || iHRIS Manage, iHRIS Qualify
|-
! supervisor
| A person who manages one or more employees of a lower grade. || manager || text entry (for past employers); selection (from Position Code + Position Title) || iHRIS Manage
|-
! surname
| A family name or last name. || last name || text entry || all
|-
! suspend license
| To revoke a health worker's license as a result of a disciplinary notice. || suspend, suspension || yes/no || iHRIS Qualify
|-
! targeted goals for the workforce
| A goal or proposed outcome for workforce plans or projections, such as to meet a specific need or staff up to a certain level. || goals || text entry || iHRIS Plan
|-
! targeted number of positions
| The number of health workers necessary to meet the health service need. || need, requirements, target || number || iHRIS Plan
|-
! targeted ratio of positions
| A targeted number of health workers based on a ratio of one health worker per a certain number of people to be served. || health worker-to-population ratio, targeted ratio || number || iHRIS Plan
|-
! telephone number
| A number where a person or organization can be contacted by telephone. || phone number, telephone || text entry || iHRIS Manage, iHRIS Qualify
|-
! temporary
| A registration type that does expire. || - || value (Registration Type) || iHRIS Qualify
|-
! topic
| The specific subject of a training course. || subject || text entry || iHRIS Manage
|-
! training course
| An in-service program offered by a training institution that enables an employee to update or add to skills necessary for performing a job. || course, in-service training, training || selection || iHRIS Manage, iHRIS Qualify
|-
! training funder
| A nonprofit or other funding organization that pays for employees to take a training course. || funder || selection || iHRIS Manage
|-
! training institution
| A school that offers one or more programs to train employees, especially health workers. || institution, institution name, school || selection; text entry (for educational history or foreign training) || iHRIS Manage, iHRIS Qualify
|-
! training manager
| A person who is responsible for managing in-service training programs for employees and updating employee competencies gained by training. || - || value (Role) || iHRIS Manage
|-
! training program
| A pre-service, multi-year educational program offered by a training institution that, when completed, qualifies a person to be registered or licensed in a particular cadre.  || pre-service training, training || selection || iHRIS Qualify
|-
! training requestor
| The person or group who requests that an employee complete a training course. || requestor || selection || iHRIS Manage
|-
! username
| A unique name used by a user to access the system. || - || text entry || all
|-
! verification change
| The type of change made to a health worker's record as a result of verifying the record with an outside source. || changes made, verification || selection || iHRIS Qualify
|-
! verification date
| The date a change was made to a record as a result of verifying the record with an outside source. || - || date || iHRIS Qualify
|-
! view
| A display of data as a table or chart that shows specific fields sorted or aggregated in a pre-specified way; filters may be selected to limit the data displayed in the report view.  || report view || text entry || iHRIS Manage, iHRIS Qualify
|-
! weekly
| An event that occurs once a week. || - || value (Recurrence Frequency) || iHRIS Manage
|-
! work contact
| Refers to a person's work mailing address, telephone number and other contact information. || work || value (Contact Type) || iHRIS Manage, iHRIS Qualify
|-
! writing proficiency
| A person's writing ability in a foreign language. || - || selection (preset values) || iHRIS Manage
|-
! year
| The year for which known data are being entered. || supply year, target year || year || iHRIS Plan
|-
! yearly
| An event that occurs once a year. || annually || value (Recurrence Frequency) || iHRIS Manage
|}

<div class="noprint">{{IHRIS_Qualify_user_manual_index}} {{IHRIS_Manage_user_manual_index}}</div>

[[Category:Implementer Resources]]
