Understanding Use Cases
=======================

Before choosing or programming an information system or any other type of software, it is important to identify the functions that the system will perform and document them. Think of these functions as **goals** . What goals do you want to achieve with your system? 

When you install and download Open Source software, you may find that some goals cannot be accomplished in the system as it is installed. In that case, a programmer will need to customize the system to achieve those goals. For example, you may need to build a new report or add a new field to capture additional data. These customizations are the **functional requirements**  of the system.

A simple way to document functional requirements is to write use cases. A **use case**  describes how to achieve a specific goal, or function, using the system. As an example, the iHRIS documentation (available with  `the iHRIS software on our website <http://www.capacityproject.org/hris/suite/>`_ ) includes a full set of use cases for the three systems to help you understand the functions that each HRIS natively supports. If you install the iHRIS software, you may want to modify these use cases to document the customizations needed to achieve your goals, or you may use the template that follows this introduction to write use cases.

Note that use cases will not hold all the requirements, but only describe the behavioral portion, the required functions of the system.



Benefits of Use Cases
^^^^^^^^^^^^^^^^^^^^^

One of the most difficult aspects of system development is figuring out exactly what to build. There is often a gap between the people who understand the problem and the people who understand how to build the solution. Use cases are one of the most effective means of bridging that gap. Written in plain language, with no technical jargon, use cases describe functional requirements in a way that can be understood by the stakeholders and users of the system and by the developers of the system.

Use cases are usually co-written by stakeholders, users and developers. This ensures that the system includes the functions that are truly important to the people who will be using it. Use cases should focus on the goals that users want to achieve. Focusing on action-oriented goals defines the scope of the system and eliminates unnecessary requirements, reducing costs and development time.

Several related use cases may be organized into modules, called *packages* . Development of each module can then be prioritized and scheduled. This helps plan an iterative path for development where core functions can be developed first and enhanced later by lower priority features. The core system can be used even while new functions are being developed.

Use cases should be living documents. Stakeholders, users and developers should constantly review, revise and expand the use cases during the development or customization of a system. At different stages, use cases can be used to: 


* describe a work process
* focus discussion about system actions
* be the functional requirements for a system
* document the design of a system
* generate procedures for testing a system
* write instructions, help and training materials for end users.

Not all requirements have to be known before starting development. Use cases may be edited during development to capture additional functions, and new use cases may be written as needs for the system arise.



Stages of Use Case Development
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Like software development itself, writing use cases is an iterative process. These are the general stages of use case development. Use case software like Case Complete can tag use cases with these stages as the "Use Case Status" to keep track of which tasks have been completed. 

* **Brief:**  The use case is summarized in brief narrative. Generally, the Description and Main Success Scenario fields are completed. This is done in conjunction with generating the Actors & Goals list.
* **Initial:**  The 1st draft of the use case is written. Steps are described at a high level but may not be fleshed out. Use this draft for grouping and prioritizing use cases.
* **Full:**  The 2nd draft of the use case is written. This draft includes all preconditions, detailed steps, extensions and explanatory notes. This draft can be used for development and may be revised many times during development.
* **Tested:**  A testing procedure is generated from the use case. The use case is tested against the developed product. Revisions to the use case are made as discovered during testing.
* **Documented:**  The help text is generated from the use case. The help is tested against the final developed product. Slight revisions to the use case may be made.
* **Released:**  The use case is part of a release version of the software.
* **Updated:**  The use case is revised post-release.

 **Tips** 



* Once the Full version has been complete, document and date any changes in the Notes field, creating a revision history for the use case. Remember that new features of use cases that are already under development should be added to the Project Control List to keep track of them.
* Record any issues with a particular use case in its Issues section. The  `Case Complete use case software <http://www.casecomplete.com/>`_  can generate an Issues Report, which is useful when discussing issues with developers or stakeholders, and eliminates the need to keep a master issues list separately.
* Organize use cases into packages initially to group modules for prioritizing and scheduling development activities. As you near release, you may want to reorganize packages or create "parent" packages to mimic the user flow of the finished product. Use the package description to record standard text that may be reproduced in help, user interface designs, product descriptions, etc.



The Parts of a Use Case
^^^^^^^^^^^^^^^^^^^^^^^

The use case enumerates all of the steps describing the interaction of one user—called the *primary actor* —with the system to achieve a goal. The use case begins at a triggering event and continues until the goal is either successfully achieved or abandoned. It collects all the possible scenarios for how the goal can be achieved and how it may fail.

At minimum, each use case should contain the following information:


* a goal to achieve
* the primary actor who is attempting to achieve the goal; the actor should be identified by a role in interacting with the system, not by a name or the name of a group
* a condition under which the scenario runs; this may include any preconditions that must be true before the scenario can start and a triggering event that starts the scenario
* an end condition that must be true after the use case is finished if the goal is successfully achieved, called the *success guarantee*
* a set of action steps, forming the body of the scenario; these are called the *main success scenario*
* a possible set of *extensions* , or alternate scenarios, leading toward either the success or failure of the goal



Writing Use Cases
^^^^^^^^^^^^^^^^^
 
Use these guidelines to write your own use cases. You should write a use case for each function or goal that has been identified for your system. A completed example is given following the guidelines.

 **1A. Use Case Number:**  Assign a number to the use case for reference. It is helpful to number use cases in order of implementation or priority. 

 **1B. Use Case Title:**  Assign a title to the use case, generally a shortened form of the goal in action-verb-noun format.

 **2. Level:**  Select *summary*  for a use case that summarizes a number of activities or is outside the scope of the system; *user-level*  for a use case that describes one complete activity in the system; or *subfunction*  for a use case that depends on a user-level use case but is too long to include in the user-level use case.

 **3. Primary Actor:**  Write the role of the user performing the use case. It is often helpful to brainstorm and list all the possible actors on a system before beginning to write use cases.

 **4. Brief Description/Goal:**  Write a goal statement that is longer and more detailed than the use case title. This statement describes the function that the primary actor wants to accomplish.

 **5. Preconditions:**  List any preconditions for the use case. Preconditions specify what the system will ensure is true before letting the use case start. Generally, a precondition indicates that some other use case has been run to set it up.

 **6. Success Guarantee:**  State the successful result that the primary actor wants. It should satisfy the stated goal and ensure that the stakeholders’ interests are met.

 **7. Main Success Scenario (MSS):**  Write the action steps of a typical scenario in which the goal is delivered. The first step is the trigger that initiates the use case. Each following step describes an action that the user or the system takes in reaction to the previous step to accomplish the use case goal. Ideally, there should be 3-12 steps; number each step. 

 **8. Extensions:**  Brainstorm and list the conditions that may cause the system behavior to branch from the steps that occur in the Main Success Scenario. An extension must be detectable by the system, and the system must take some action to handle it. Number each extension to link to the MSS step in this format: 1a, 1b… If the extension can happen at any time, precede it with an asterisk (*) and list it first: *a, *b… Indent extensions to extensions and restart numbering: 1a1, 1b1… Under each extension, indent and write how the system responds, the extension-handling steps. Each extension-handling step should end back in the main success scenario, at an alternative successful exit or in failure (a system error) that stops the use case before the goal is accomplished. 

 **9. Notes/Issues/Reviewer Comments:**  Add any comments on the use case or explanatory notes needed. This is also a good place to note any issues that have arisen regarding the use case or its implementation in the system. 
 


Example Use Case
^^^^^^^^^^^^^^^^

 **1A. Use Case Number:**  9

 **1B. Use Case Title:**  Log in

 **2. Level:**  User-level

 **3. Primary Actor:**   Any user

 **4. Context of Use:**  The user logs in to authenticate his or her role in the system and to perform a task in the system.

 **5. Preconditions:**  A user account has been created for the user. 

 **6. Success Guarantee:**  The user can successfully access the system and perform actions appropriate for his or her role.

 **7. Main Success Scenario (MSS):**  
	

* The user connects to the system.
* The user enters his/her username and password.
* The system validates the username and password.
* The system determines the user’s role.
* The system displays a list of actions the user can perform based on the user’s role.

 **8. Extensions:** 


.. code-block::

    3a. The system determines that the password is incorrect for the username entered.
        1. The system prompts the user to re-enter the password.
           3a1. The system determines that the re-entered password is incorrect.
                2. The system provides the option for the user to retrieve a forgotten password.
    
    3b. The system determines that the username does not match a username for any account.
        1. The system displays an error message.
    
    4a. The system determines that the user has no role assigned in the system.
        1. The system does not allow the user to access the system.
    


 **9. Notes/ Issues/ Reviewer Comments:**  This use case is the same for iHRIS Manage, Qualify and Plan.

 **Completed by:**  Use case writer
 **Date:**  October 25, 2008

 **Reviewed by:**  Use case reviewer
 **Date:**  November 4, 2008



Guidelines for Finding Actors and Goals
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* List every possible human and non-human primary actor, over the life of the system.
* Brainstorm and exhaustively list all possible user goals for each actor.
* Write a short description of use case behavior for each goal--the *use case brief* --mentioning only the most significant activity and failures. This summarizes what is going on in the use case.
* Re-evaluate the goals for each primary actor. Add, subtract and merge goals as necessary.
* Identify all business use cases--those that have the organization as the scope, rather than the system--and separate. These may be written to clarify business processes, assumptions and preconditions, but probably will not be included in the specifications.
* Write user-level use cases for each goal using the use case template above.
* Prioritize and assign goals to development teams and software releases.

You may find it helpful to use the  `Actors and Goals Template <http://spreadsheets.google.com/pub?key=rq3k2zguXd68aJYwfpEv7gA&output=xls>`_  to organize all actors and goals before writing full use cases.



Writing Summary-Level Use Cases
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Summary-level goals involve multiple user goals. The purpose of summary-level use cases is to:


* Show the context in which the user goals operate
* Show life-cycle sequencing of related goals
* Provide a table of contents for the lower-level use cases.

Summary use cases tie together, and thus refer to, a number of user-level use cases. There are typically only four or five summary-level use cases for a system. Summary use cases typically execute over hours, days, weeks, months or years. They do not provide functional requirements.
To find a summary-level use case, ask "what does the primary actor really want?" or "why is the actor doing this?" The answer will be a goal one level higher than the goal stated in the user-level use case. To write a summary-level use case, remove the user interface details; show the actor's intent, not their movement. 

I prefer to write summary-level use cases in narrative rather than numbered step format. I also find it helpful to write an example scenario for each summary-level use case telling a story about how the users will interact with the system.

Written this way, summary-level use cases provide a helpful tool for quickly communicating with executives, stakeholders and customers the broad scope of what the system will do.



Definitions
^^^^^^^^^^^

 **User goals** : Goals that the system will support, revealing the scope of the system and its purpose; each user goal should be expanded into a separate use case.

 **Usage narrative:**  A situated example of the use case in operation; a single, highly specific example of an actor using the system.

 **Use case:**  describes a system's behavior under various conditions as the system responds to a request from one of the stakeholders, called the primary actor. 

 **Package** : a cluster of related use cases.

 **Use case brief:**  A short paragraph describing the use case behavior, mentioning only the most significant activity and failures.

 **Scope** : identifies the system under discussion; may be an organization (business use cases), a system (system use cases) or a subsystem, a piece of the main system (component use cases).

 **Design scope:**  The extent of the system to be designed, including systems, hardware and software.

 **Functional scope:**  the services offered by the system that will be captured by the use cases.

 **Actor** : anyone or anything with behavior.

 **Actor-goal list:**  names all the user goals that the system supports.

 **Primary actor:**  wants to accomplish a goal within the system that is captured by the use case.

 **Supporting actor:**  An actor needed to help carry out subgoals, such as a subsystem or another organization.

 **Offstage actor:**  A stakeholder with interest in the outcome that must be satisfied, but who is not playing an active role in the use case.

 **Stakeholder** : someone with a vested interest in the behavior of the system.

 **Summary-level goal:**  a use case or a goal that takes more than one sitting.

 **User-level goal** : a use case or goal that can be achieved at one sitting.

 **Subfunction** : part of a user-level goal.

 **Precondition** : what must be true before the use case runs.

 **Guarantee** : what must be true after the use case runs.

 **Minimal guarantee:**  the fewest promises the system makes to the stakeholders, particularly when the primary actor's goal cannot be delivered.
Scenario: description of one set of circumstances with one outcome in a use case, resulting in either success or failure of the goal.

 **Main success scenario:**  a case in which nothing goes wrong.

 **Extensions** : what can happen differently during a scenario.

 **Trigger** : event that gets a use case started.

 **Black box** : use case that does not discuss the inner workings of the system.

 **White box** : use case that shows internal processes.



Recommended Resources
^^^^^^^^^^^^^^^^^^^^^


Books
~~~~~


* *Writing Effective Use Cases*  by Alistair Cockburn
* *Use Cases: Requirements in Context*  by Daryl Kulak and Eamonn Guiney


Websites
~~~~~~~~


* Understanding Use Case Modeling: http://www.methodsandtools.com/archive/archive.php?id=24
* Use Case Fundamentals: http://alistair.cockburn.us/index.php/Use_case_fundamentals
* Use Case Tutorials: http://www.parlezuml.com/tutorials/usecases.htm
[[Category:Use Cases]]
