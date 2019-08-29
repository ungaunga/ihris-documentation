Using Previously Collected HRH Data to Create a Data Coding Scheme
==================================================================

'''How Can We Use Previously Collected HRH Data to Create a Data Coding Scheme?'''

In some of the countries where the Capacity Project has aided in HRIS strengthening, HRH data at the facility, district or country level have already been collected and digitized.  These data provide a useful foundation for the development of an HRH data coding system.  Nevertheless, the existence of a prior source of HRH data does not indicate that a country can skip the step of creating a standardized HRIS data coding scheme.

Existing lists of values may be a helpful starting point, but such lists invariably require editing before being useful for a broader system.  Certainly, the temptation exists to copy the variables in the different fields of an available database, such as Job Title, Department Name, etc., and paste those values into a data collection tool, using the existing fields as the drop-down menus for the future HRIS.  However, the values in each field need to be carefully assessed to ensure that they are appropriate for use in the new system.  If the values are not reviewed, the quality of the data entered into the new system may be compromised.  

We recommend the following steps to clean existing health workforce data for use in data collection tool drop-down menus.  We describe this process based on Microsoft Excel software, but these steps can be adapted for use with other spreadsheet software programs.

#Format the spreadsheet so that all data categories, or fields, are positioned as ‘headers’ in the first row of the spreadsheet, at the top of each column.  All of the values in each field should be listed below the header to which they correspond.  
#Use the “Remove Duplicates” tool in the Data Tools bar to eliminate all exact duplicates from each list.  Remember that this tool will only remove duplicate values that are exactly the same.  Even an additional space will prevent the tool from recognizing a value as a duplicate. ''[Add screenshot]''
#Use the “Sort” tool in the Sort and Filter bar to sort the list of values in alphabetical order.
## If the list did not seem to successfully alphabetize all of the values, check to make sure that there are no spaces before the text entered in the cells.  
## Delete any extra beginning spaces and repeat steps 2 and 3 above until all of the values in the list are in alphabetical order.
#Carefully review each value on the list to ensure that there are no duplicates.  Duplicates can exist due to abbreviations, misspellings and even inconsistent spacing. 
## If a duplicate exists, remove it from the list and note the duplicate in the data dictionary.
## If there is a question about whether two values are duplicates, mark them both for later review.
### Follow up with someone knowledgeable about the source of the data to confirm duplicate status.  
## If a value contains text or a number for which the meaning is unclear, mark it for later review.
### Follow up with someone knowledgeable about the source of the data.  Determine whether the meaning of the text or number is relevant to the purpose of the database.  If so, decide how to incorporate the meaning into the coding scheme so that it is clear for data entry clerks and data analysts and note the meaning in the data dictionary.  If not, remove the text or number from the value and note the omission in the data dictionary.

Once the initial list of values has been edited to this point, it is time to edit the codes in the list for use in the final drop-down menus of the data collection tool.  Depending on the field, the values may require review from HRIS stakeholders.  For example, if the field in question is District Name and there are 50 districts in the country, one person can review the list to make sure all 50 districts are included and that they are spelled correctly.  However, if the field is specific to the health system, HRIS stakeholders need to provide input and guidance to ensure that the right data are collected to answer health workforce questions.  Training institutions, Facilities, Facility Types, Departments and Job Titles are examples of these more complex data fields.
[[Category:Implementer Resources]]
