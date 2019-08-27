ISCO Classification Mapping
================================================


The Issue
^^^^^^^^^

There is a need to support standard ISCO classification codes and descriptions in the iHRIS Manage software, and to provide a way to map them to existing country classifications. This will enable countries to standardize their classifications and provide a standard way of looking at HR data across countries.

 **Done!** This has been release with version 4.0.2 of the software.


The Process
^^^^^^^^^^^

The ISCO classifications will be available on the **Job Classification** form. There will be three options:

 **1. The user can enter a custom job classification name, code and description.**

In this situation, the user is not using the ISCO standards, but instead prefers to use their own job classifications. This is the way the software currently functions.

With the new functionality, the user will be able to link the custom classifications to the ISCO standards at some later point.


 **2. The user can select an ISCO standard job classification name and code from a separate dropdown menu.**

In this situation, the user is already using the ISCO standards for the job classifications. This will populate the ISCO classification name, code and description for the selection. The user will not have to enter any additional information. (See the end of this document for a reference of all ISCO codes.) 


 **3. The user enters a custom job classification and then links it to the corresponding ISCO standard.**

In this situation, the user is using their own job classifications but has identified a corresponding ISCO standard for each job classification. The user enters the custom job classification name, code and description as for option #1. The user then selects the standard ISCO job name/code from the dropdown, as for option #2. 

This links the custom job classification to the ISCO standard so that either may be used in reports for the same job classification and corresponding jobs.



Documentation and Resources
^^^^^^^^^^^^^^^^^^^^^^^^^^^

These changes are documented in use case UC-PT18, Add or update a job classification. 

ISCO website with full list of job classifications: http://www.ilo.org/public/english/bureau/stat/isco/index.htm


An Example Definition
~~~~~~~~~~~~~~~~~~~~~
  	
classification code: 2221 

classification title: MEDICAL DOCTORS 
 
classification definition:

      Medical doctors conduct research, improve or develop concepts, theories and operational methods, and apply preventive or curative measures.
      Tasks include -
      (a) conducting research into human disorders and illnesses and preventive or curative methods;
      (b) conducting medical examinations and making diagnoses;
      (c) prescribing and giving treatment for diagnosed illnesses, disorders or injuries;
      (d) giving specialised medical or surgical treatment for particular types of illnesses, disorders or injuries;
      (e) giving advice on and applying preventive medicine methods and treatments;
      (f) participating in the development and implementation of public health laws and regulations for safeguarding and promoting the health of a community;
      (g) preparing scientific papers and reports;
      (h) performing related tasks;
      (i) supervising other workers.
      Examples of the occupations classified here:
    * Doctor, medical
    * Ophthalmologist
    * Physician
    * Psychiatrist
    * Surgeon
[[Category:Blueprints]][[Category:iHRIS Manage]]
