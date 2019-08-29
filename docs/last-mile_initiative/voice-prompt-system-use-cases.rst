Voice Prompt System Use Cases
=============================

 **Overview:** 

<nowiki>The LMI Siscom implementation is a system which allows community health workers working on the Twubakane [detail] project to enter in the community health information via mobile phone instead of the paper-based system that has been implemented. This specification is not complete.</nowiki>This functional specification is designed to give the user perspective of the system. The user in this spec is assumed to be the community health worker using the voice-prompted IVR system. For an overview of the touch-based PDA system please refer to the *LMI PDA Collection Functional Spec*  document. For an overview of the health professional's use of the database please refer to the *LMI Database Functional Spec*  document.

 **Technical Implementation:** 

The voice prompt system will be based on the Asterisk PBX system. Asterisk makes it easy to set up an IVR system allowing voice prompts and user input via touch-tone. The Asterisk system will tie into a Mysql database to store all of the responses. This database should be the same database used for the menu-driven system. Further, the menu system will rely on text messaging which will also be controlled and input by the same Asterisk PBX.


 **Scenario:** 

When a health volunteer arrives at a person's home to collect data for the Twubakane SISCOM she will place a phone call to the LMI IVR system using a designated (toll free) number. The system, running a PBX, will prompt the volunteer for their ID number. Once entered the system will then run through questions which correspond to the indicators which already exist in the paper-based forms.

 **Non-goals:** 

This system will NOT be the form-driven software system which will live on the smart phones. That system will be covered in a separate specification.

 **Prompt-by-prompt Walk-through** 

 **Initial prompt** 

The initial prompt will be a welcome message which identifies the system so that the health workers know that they have dialed the correct number. At any moment during the welcome message there will be an option to press the # key to skip the rest of the message and move to the identification prompt. The welcome message should also include any news that might need to be passed on to the health workers in the field. This prompt will ask:

Welcome to the Twubakane Health Data Collection System. At any time you may skip this message and enter your identification number by pressing the pound key. 


Any timely, local messages may be recorded here in the Intial prompt.Identification:The ID prompt is the gateway to all other prompts. There should not be an option to get to the indicator questions without entering a proper identification number. When creating the database, we will have to generate ID numbers for all health workers who will be using the system.&nbsp; This prompt will ask:


Please enter your identification number.


 **Home menu:** 

The home menu prompt is the default prompt which will lead to the other areas which are associated with each paper form type. This prompt allows the user to go to any of the main three "forms" by pressing the keys 1, 2, or 3. This prompt should always be accessible by a keystroke on the phone so that the user may choose a new form. When any one form is completed it should send the user back to this prompt. This prompt will always ask:

Press 1 to collect Household information.Press 2 to collect women's registration information.Press 3 to collect children's registration information.Press 9 to log out.

After the user selects a number the prompt will then inform the user about the option to return to the home menu:

 **Repeating:** 


The user should always have the option to press a key to repeat the current prompt. This key should be chosen wisely as to not conflict with any data entry. The * is the most likely candidate.


 **Household Form:** 

The following prompts are all identifiable in the household data collection forms from the paper system.

 **Village** 

Our records show that your village is XXX with an identification number of XX. Is this correct? Press 1 for Yes and 2 for No.

If the response is 2, or No:

Please enter the identification number of the village you are working in.

 **Cell** 

Our records show that your cell is XXX with an identification number of XX. Is this correct? Press 1 for Yes and 2 for No. 

If the response is 2, or No:

Please enter the identification number of the Cell you are working in.

 **Sector** 

Our records show that your sector is XXX with an identification number of XX. Is this correct? Press 1 for Yes and 2 for No.

If the response is 2, or No:

Please enter the identification number of the Sector you are working in.

 **Head of Household** Is the Head of the Household male or female? Press 1 for male or 2 for female'''House ID'''

Please enter the identification number of the house you are visiting.

 **Sex** 

Please press 1 if the person you are speaking to is Male. Press 2 if the person is Female.

 **Date of Birth** 

Please enter the Date of Birth of the person you are speaking to. Enter the date as day followed by month followed by 4 digit year.

 **Change of Residence** &nbsp;&nbsp;&nbsp;&nbsp;'''New Residents'''

Are there any new residents in this house? Press 1 for Yes or 2 for No.

If the user presses 1 they should then be asked:

What date did the new person move into the house? Enter the date as day followed by month followed by 4 digit year.Are there anymore new residents in the house? Press 1 for Yes or 2 for No.

If the user presses 1 repeat the new resident date question and continue.&nbsp;&nbsp;'''Residents Leaving'''

Has anyone in the last 6 months moved away from this house? Press 1 for Yes or 2 for No.

If the user presses 1 they should then be asked:

What date did the person move away from the house? Enter the date as day followed by month followed by 4 digit year.


Has anyone else moved away from the house in the last 6 months? Press 1 for Yes or 2 for No.

If the user presses 1 repeat the move date question and continue.'''Number of Mosquito Nets'''

Please enter the number of mosquito nets in the house.

If the user enters any number other than zero, follow up with:

Are the nets chemically treated with an insecticide? Press 1 for Yes or 2 for No.


 **Register of Women Aged 15 and up** '''House ID'''

Please enter the identification number of the house you are visiting.

 **ID Number** 

Please enter the Identity Card Number of the person. Please enter the numbers followed by the pound sign (#).

 **Date of Birth** 

Please enter the Date of Birth of the person you are speaking to. Enter the date as day followed by month followed by 4 digit year.

 **Number of Children living** 

Please enter the number of living children this woman has.

 **Number under 5** 

Please enter the number of children under 5 years old this woman has.

 **Dates of vaccination against Tetanus** *question - what is more important to know? the date of all vaccinations or the date of the *last* vaccine?* '''Dates of last Mensus'''Please enter the date of the last Mensus vaccine. Enter the two digit month followed by four digit year'''Dates of Prenatal Consultations (PNC)'''''question - are the dates important or the number of visits? or date of last visit?'''''Date of last consultation after delivery'''Please enter the date of the last consultation after the delivery of the child. Enter the two digit month followed by the four digit year

 **Results** &nbsp;&nbsp;&nbsp; *question - what is this?* '''Place of delivery'''''question - do we need a *specific* place or choices like home or clinic?''

 **Did nursing occur immediately after delivery?** 

Did this woman nurse immediately after giving birth? Press 1 for Yes and 2 for No.


 **Date of first food supplements** Please enter the date of the first food supplements. Enter two digit month followed by four digit year. 

 **Date of weaning** Please enter the date of weaning. Enter the two digit month followed by the four digit year **Vitamin A date** Please enter the date Vitamin A was taken or administered. Enter the two digit month followed by the four digit year.'''Women's Health Card'''

Does this woman possess a Women's Health Card? Press 1 for Yes and 2 for No.

 **Pregnancy Malaria Treatment** 

Please enter the dates malaria medication was taken the first time during pregnancy. Enter month followed by 4 digit year.


Please enter the dates malaria medication was taken the second time during pregnancy. Enter month followed by 4 digit year.


Please enter the dates malaria medication was taken the third time during pregnancy. Enter month followed by 4 digit year.

 **Anti-parasite Dates** 

Please enter the dates that anti-parasite medication was taken. Please enter month followed by 4 digit year.

 **Malaria Net Dates** 

Please enter the date a mosquito net was received. Please enter month followed by 4 digit year.

 **HIV Screening Date** 

Please enter the date HIV screening took place. Please enter month followed by 4 digit year.

 **Contraceptive methods** *question:*  *this could be tricky - what is the most important information to know here?* 


<nowiki>[Optional Voice Record name?]</nowiki>


 **Register of Children up to 60 MonthsOpen Issues** :Do we want to have the village/cell/sector information separated so that no matter which set of prompts the worker calls up they can add this information. What if someone calls up the Women's register and the household form has not been filled out for that house ID? Do we force them to do the household form?


Backend:


The child record should be identified through the parent's ID number. The Child's ID number may be arbitrary as long as it does not match that of another child parented by the parents the child is associated with. 


 **Child identification number** 


Please enter the child's ID number. This may be any number you choose as long as it does not match another child's number in this household.


 **Date of Birth** 


Please enter the child's date of birth. Enter the two digit day, followed by the two digit month, followed by the four digit year.

 **Sex** 


Please enter the sex of the child. Press 1 for male and 2 for female.


 **Survival of parents** 


How many surviving parents does the child have. Press 0, 1, or 2 for the number surviving.


 **Vaccines:** 


 **BCG** 

Please enter the date the child received the BCG Vaccination. Enter the two digit day, followed by the two digit month, followed by the four digit year.


 **Polio** 

Please enter the date the child received the Polio Vaccination. Enter the two digit day, followed by the two digit month, followed by the four digit year.


 **DTP** 

Please enter the date the child received the DTP Vaccination. Enter the two digit day, followed by the two digit month, followed by the four digit year.


 **Measles** 

Please enter the date the child received the Measles Vaccination. Enter the two digit day, followed by the two digit month, followed by the four digit year.


Weight:


 **General:** 


 **Referred to Health Center** 

Press 1 to enter a date the child was referred to a Health Center. Press 2 to skip to the next question.


If the user presses 1:


Please enter the date the child was referred to a Health Center. Enter the two digit day, followed by the two digit month, followed by the four digit year.


Press 1 to enter another Health Center referral date. Press 2 to skip to the next question.


 **Vitamin A dates** 


Press 1 to enter a date the child was given Vitamin A. Press 2 to skip to the next question.


If the user presses 1:


Please enter the date the child was given Vitamin A. Enter the two digit day, followed by the two digit month, followed by the four digit year.


Press 1 to enter another Vitamin A administration date. Press 2 to skip to the next question.


 **Mebendazole dates** 


Press 1 to enter a date the child was given Vitamin A. Press 2 to skip to the next question.


If the user presses 1:


Please enter the date the child was given Mebendazole. Enter the two digit day, followed by the two digit month, followed by the four digit year.


Press 1 to enter another Mebendazole administration date. Press 2 to skip to the next question.


 **zinc/ORS dates** 


Press 1 to enter a date the child was given zinc/ORS Press 2 to skip to the next question.


If the user presses 1:


Please enter the date the child was given zinc/ORS. Enter the two digit day, followed by the two digit month, followed by the four digit year.


Press 1 to enter another zinc/ORS administration date. Press 2 to skip to the next question.


 **Anti-malaria Medicine** 


 *question: this could be huge, a lot of medicine can be administered over time. do we care more about how many times a child has taken it as compared to their age or are dates important?* 
[[Category:Last Mile Initiative]]
