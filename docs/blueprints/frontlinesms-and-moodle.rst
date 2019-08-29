FrontlineSMS And Moodle
=======================

This is the beginning of an outline for a FrontlineSMS and Moodle interaction.   `FrontlineSMS <http://www.frontlinesms.com/>`_  is written in Java
while  `moodle <http://www.moodle.org>`_  is written in PHP.

In order to have close interaction, we will need to create/modify two plugins.  One for FrontlineSMS and one for moodle.   Primary end-user interaction will be through Moodle.  The aim is to keep these two programs loosely coupled and to expose needed FrontlineSMS functionality via its Web API (HTTP Triggers).  Development should begin with adding in these triggers


FrontlineSMS and Triggers
^^^^^^^^^^^^^^^^^^^^^^^^^



* Source: http://sourceforge.net/apps/trac/frontlinesms/browser/trunk/src
* HTTP Trigger plugin: http://sourceforge.net/apps/trac/frontlinesms/browser/trunk/src/main/java/net/frontlinesms/plugins/httptrigger
* We will want to add new http triggers to frontline SMS:
* * http://localhost:{port}/groups/list   -- list the available top-level groups  (perhaps JSON encoded string)
* * http://localhost:{port}/groups/list/{groupath}   -- list subgroups of the group indicated by the {grouppath}
* * http://localhost:{port}/groups/create/{grouppath}   -- creates the group {grouppath}
* * http://localhost:{port}/groups/contacts/{grouppath}   -- list the user in the indicated  group {grouppath}
* * http://localhost:{port}/contacts/add   -- adds new contact to frontlineSMS with details from GET variables
* * http://localhost:{port}/contacts/edit/{id}   -- adds new contact to frontlineSMS with details from GET variables
* * http://localhost:{port}/contacts/lookup/{phonenumber}   -- returns the id, if any of a user with the matching phone number
* * http://localhost:{port}/send/groupsms/{grouppath}?content={conent}  -- send the indicate content to each member of the indicated group
* '''Note:''' Groups in FrontlineSMS are hierarchical. If groupB is in groupA its group path is /groupA/groupB.


FrontlineSMS Groups and Moodle Courses
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



* Moodle UI to associate a course in moodle with a group in FrontlineSMS:
* *groups should already be defined in frontline SMS. also have ability to create new group
* * list/create groups should added by via an http trigger as indicated above
                


General Moodle Interaction
^^^^^^^^^^^^^^^^^^^^^^^^^^



* Moodle UI so a user can associate a contact.id from frontline SMS
* * uses puts in their mobile number
* * moodle does a lookup on frontlinesms to see if there is a contact with that number via the contracts/lookup trigger
* ** if there is exactly one contact, the contact id is associated with the user profile
* ** if there are no contacts, moodle will create the contact on frontlinesms via the contacts/add trigger
* ** if there is more than one contact, display a drop-down list where the user can select which contact_id they should be associated to (list display name)
* All posts to SMS messages are sent via FrontLine SMS's existing http trigger  sms/send
* Participants in a course can send a SMS to any/all other partipicpants that
* Administrator in course can send a message to any/all partipants in the course


Moodle Forum interaction
^^^^^^^^^^^^^^^^^^^^^^^^



* Concept: Enable announcements and participation in Moodle forums via Frontline SMS
* Reference:  http://docs.moodle.org/en/Forum_module
* Reference: http://docs.moodle.org/en/News_forum
* Teacher/administrator of a course can choose to enable SMS forwarding of messages "News Forum" to participants that have a mobile number.      defaults to enabled
* Teacher/administrator can mark each forum that they create as SMS-enabled or not. defaults to disabled
* sending a message on a moodle forum will initiate send the message the group registered for the course via http trigger sms/sendgroup
* **More Specification pending for posting**  to a forum via FrontlineSMS.


Moodle Quiz interaction
^^^^^^^^^^^^^^^^^^^^^^^


* **More Specification Pending**
* need to add http triggers to FrontlineSMS to create/edit forms
* need to modify moodle so that creating a question creates the pieces of a frontlineform for the following type of questions
* *http://docs.moodle.org/en/Multiple_Choice_question_type
* *http://docs.moodle.org/en/Short-Answer_question_type
* *http://docs.moodle.org/en/True/False_question_type
* need to modify moodle so that creating a quiz based on the above questions will put all the pieces of the frontline form together
* need to add http trigger to FrontlineSMS to get read forms as answer to questions in a quiz for a specific user




Related Moodle Plugins
^^^^^^^^^^^^^^^^^^^^^^



* http://www.moodletxt.co.uk/download.php  **WARNING:**  NOT OPEN SOURCE
* http://www.pageonejanettxt.com/products/moodlemobile GPL V2
* http://www.clickatell.com/developers/scripts.php  I think the plugin is very out of date
[[Category:Blueprints]]
