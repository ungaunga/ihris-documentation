Class: iHRIS PageViewQualify
============================

Note: This is an orphaned page that appears to have been superseded by later documentation.

This article describes the class *iHRIS_PageViewQualify* .

* Extends the class: [[Class: iHRIS_PageView | iHRIS_PageView]].
* Location: Part of the module [[iHRIS Qualify Module List#ihris-qualify|ihris-qualify]] in the package  `iHRIS Qualify <https://launchpad.net/qualify>`_
* Source: Defined in the file  `lib/iHRIS_PageViewQualify.php <http://bazaar.launchpad.net/~intrahealth+informatics/qualify/4.0.-release/annotate/head:/lib/iHRIS_PageViewQualify.php>`_
* Author: Luke Duncan <lduncan@intrahealth.org>
* Since: v2.0.0
View a person's record.    @copyright Copyright &copy; 2007, 2008 IntraHealth International, Inc.    The page class for displaying the a person's record.

Methods
^^^^^^^

action()
~~~~~~~~
Perform the main actions of the page.

* Signature: protected function action()

Inherited Methods
^^^^^^^^^^^^^^^^^

addChildForms()
~~~~~~~~~~~~~~~
This public method is inherited from [[Class: iHRIS_PageView#addChildForms() | iHRIS_PageView->addChildForms()]]

addLastChildForm()
~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: iHRIS_PageView#addLastChildForm() | iHRIS_PageView->addLastChildForm()]]

appendChildTemplate()
~~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: iHRIS_PageView#appendChildTemplate() | iHRIS_PageView->appendChildTemplate()]]

getPerson()
~~~~~~~~~~~
This public method is inherited from [[Class: iHRIS_PageView#getPerson() | iHRIS_PageView->getPerson()]]

hasChildForm()
~~~~~~~~~~~~~~
This public method is inherited from [[Class: iHRIS_PageView#hasChildForm() | iHRIS_PageView->hasChildForm()]]

__construct()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#__construct() | I2CE_Page->__construct()]]

_flattenRequestVars()
~~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#_flattenRequestVars() | I2CE_Page->_flattenRequestVars()]]

display()
~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#display() | I2CE_Page->display()]]

fixupRequestVariables()
~~~~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#fixupRequestVariables() | I2CE_Page->fixupRequestVariables()]]

flattenRequestVars()
~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#flattenRequestVars() | I2CE_Page->flattenRequestVars()]]

get()
~~~~~
This public method is inherited from [[Class: I2CE_Page#get() | I2CE_Page->get()]]

getAccessedBaseURL()
~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#getAccessedBaseURL() | I2CE_Page->getAccessedBaseURL()]]

getTemplate()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#getTemplate() | I2CE_Page->getTemplate()]]

getUser()
~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#getUser() | I2CE_Page->getUser()]]

get_exists()
~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#get_exists() | I2CE_Page->get_exists()]]

hasPermission()
~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#hasPermission() | I2CE_Page->hasPermission()]]

isGet()
~~~~~~~
This public method is inherited from [[Class: I2CE_Page#isGet() | I2CE_Page->isGet()]]

isPost()
~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#isPost() | I2CE_Page->isPost()]]

module()
~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#module() | I2CE_Page->module()]]

page()
~~~~~~
This public method is inherited from [[Class: I2CE_Page#page() | I2CE_Page->page()]]

pageRemainder()
~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#pageRemainder() | I2CE_Page->pageRemainder()]]

pageRoot()
~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#pageRoot() | I2CE_Page->pageRoot()]]

post()
~~~~~~
This public method is inherited from [[Class: I2CE_Page#post() | I2CE_Page->post()]]

post_exists()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#post_exists() | I2CE_Page->post_exists()]]

redirect()
~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#redirect() | I2CE_Page->redirect()]]

request()
~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#request() | I2CE_Page->request()]]

request_exists()
~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#request_exists() | I2CE_Page->request_exists()]]

rewrittenURLs()
~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#rewrittenURLs() | I2CE_Page->rewrittenURLs()]]

session_req()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#session_req() | I2CE_Page->session_req()]]

session_req_exists()
~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#session_req_exists() | I2CE_Page->session_req_exists()]]

setAccess()
~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#setAccess() | I2CE_Page->setAccess()]]

setIsPost()
~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#setIsPost() | I2CE_Page->setIsPost()]]

setRedirect()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Page#setRedirect() | I2CE_Page->setRedirect()]]

_display()
~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#_display() | I2CE_Page->_display()]]

actionCommandLine()
~~~~~~~~~~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#actionCommandLine() | I2CE_Page->actionCommandLine()]]

getAccess()
~~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#getAccess() | I2CE_Page->getAccess()]]

getTitle()
~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#getTitle() | I2CE_Page->getTitle()]]

initializeTemplate()
~~~~~~~~~~~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#initializeTemplate() | I2CE_Page->initializeTemplate()]]

loadHTMLTemplates()
~~~~~~~~~~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#loadHTMLTemplates() | I2CE_Page->loadHTMLTemplates()]]

setupGetPost()
~~~~~~~~~~~~~~
This protected method is inherited from [[Class: I2CE_Page#setupGetPost() | I2CE_Page->setupGetPost()]]

_hasMethod()
~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Fuzzy#_hasMethod() | I2CE_Fuzzy->_hasMethod()]]

Inherited Variables
^^^^^^^^^^^^^^^^^^^

$person
~~~~~~~
Theis protected variable is inherited from [[Class: iHRIS_PageView#$person | iHRIS_PageView->$person]]

$template
~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$template | I2CE_Page->$template]]

$defaultHTMLFile
~~~~~~~~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$defaultHTMLFile | I2CE_Page->$defaultHTMLFile]]

$role
~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$role | I2CE_Page->$role]]

$user
~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$user | I2CE_Page->$user]]

$post
~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$post | I2CE_Page->$post]]

$get
~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$get | I2CE_Page->$get]]

$page_root
~~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$page_root | I2CE_Page->$page_root]]

$page_remainder
~~~~~~~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$page_remainder | I2CE_Page->$page_remainder]]

$args
~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$args | I2CE_Page->$args]]

$request_remainder
~~~~~~~~~~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$request_remainder | I2CE_Page->$request_remainder]]

$permissionParser
~~~~~~~~~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$permissionParser | I2CE_Page->$permissionParser]]

$page
~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$page | I2CE_Page->$page]]

$module
~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$module | I2CE_Page->$module]]

$is_post
~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$is_post | I2CE_Page->$is_post]]

$session_req
~~~~~~~~~~~~
Theis protected variable is inherited from [[Class: I2CE_Page#$session_req | I2CE_Page->$session_req]]

Inherited Fuzzy Methods
^^^^^^^^^^^^^^^^^^^^^^^

action_registration()
~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_registration() | iHRIS_PageView->action_registration()]]

action_person_contact_work()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_contact_work() | iHRIS_PageView->action_person_contact_work()]]

action_person_contact_personal()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_contact_personal() | iHRIS_PageView->action_person_contact_personal()]]

action_person_contact_other()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_contact_other() | iHRIS_PageView->action_person_contact_other()]]

action_person_contact_emergency()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_contact_emergency() | iHRIS_PageView->action_person_contact_emergency()]]

action_demographic()
~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_demographic() | iHRIS_PageView->action_demographic()]]

action_education()
~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_education() | iHRIS_PageView->action_education()]]

action_employment()
~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_employment() | iHRIS_PageView->action_employment()]]

action_person_id()
~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_id() | iHRIS_PageView->action_person_id()]]

action_person_language()
~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_language() | iHRIS_PageView->action_person_language()]]

action_notes()
~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_notes() | iHRIS_PageView->action_notes()]]

action_person_photo_passport()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_photo_passport() | iHRIS_PageView->action_person_photo_passport()]]

action_person_resume()
~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_resume() | iHRIS_PageView->action_person_resume()]]

action_application()
~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_application() | iHRIS_PageView->action_application()]]

action_position_decision()
~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_position_decision() | iHRIS_PageView->action_position_decision()]]

action_position_interview()
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_position_interview() | iHRIS_PageView->action_position_interview()]]

action_benefit()
~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_benefit() | iHRIS_PageView->action_benefit()]]

action_person_position()
~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_position() | iHRIS_PageView->action_person_position()]]

action_person_competency()
~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_competency() | iHRIS_PageView->action_person_competency()]]

action_person_scheduled_training_course()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: iHRIS_PageView#action_person_scheduled_training_course() | iHRIS_PageView->action_person_scheduled_training_course()]]

launchBackgroundProcess()
~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#launchBackgroundProcess() | I2CE_Page->launchBackgroundProcess()]]

launchBackgroundPHPScript()
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#launchBackgroundPHPScript() | I2CE_Page->launchBackgroundPHPScript()]]

launchBackgroundPage()
~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#launchBackgroundPage() | I2CE_Page->launchBackgroundPage()]]

addColorPickerTriple()
~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addColorPickerTriple() | I2CE_Page->addColorPickerTriple()]]

selectOptionsImmediate()
~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#selectOptionsImmediate() | I2CE_Page->selectOptionsImmediate()]]

setDisplayData()
~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setDisplayData() | I2CE_Page->setDisplayData()]]

setDisplayDataImmediate()
~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setDisplayDataImmediate() | I2CE_Page->setDisplayDataImmediate()]]

addFormWorm()
~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addFormWorm() | I2CE_Page->addFormWorm()]]

getClassValue()
~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#getClassValue() | I2CE_Page->getClassValue()]]

loadClassValues()
~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#loadClassValues() | I2CE_Page->loadClassValues()]]

setClassValue()
~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setClassValue() | I2CE_Page->setClassValue()]]

setClassValues()
~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setClassValues() | I2CE_Page->setClassValues()]]

addOption()
~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addOption() | I2CE_Page->addOption()]]

addOptions()
~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addOptions() | I2CE_Page->addOptions()]]

addAutoCompleteInputTreeById()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAutoCompleteInputTreeById() | I2CE_Page->addAutoCompleteInputTreeById()]]

addAutoCompleteInputTree()
~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAutoCompleteInputTree() | I2CE_Page->addAutoCompleteInputTree()]]

setForm()
~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setForm() | I2CE_Page->setForm()]]

getField()
~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#getField() | I2CE_Page->getField()]]

setReview()
~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setReview() | I2CE_Page->setReview()]]

isReview()
~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#isReview() | I2CE_Page->isReview()]]

setShowForm()
~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setShowForm() | I2CE_Page->setShowForm()]]

showForm()
~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#showForm() | I2CE_Page->showForm()]]

makeJumper()
~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#makeJumper() | I2CE_Page->makeJumper()]]

menuSelect()
~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#menuSelect() | I2CE_Page->menuSelect()]]

addUpdateSelect()
~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addUpdateSelect() | I2CE_Page->addUpdateSelect()]]

addAjaxUpdate()
~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAjaxUpdate() | I2CE_Page->addAjaxUpdate()]]

addAjaxToggle()
~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAjaxToggle() | I2CE_Page->addAjaxToggle()]]

addAjaxRequestFunction()
~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAjaxRequestFunction() | I2CE_Page->addAjaxRequestFunction()]]

addAjaxCompleteFunction()
~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAjaxCompleteFunction() | I2CE_Page->addAjaxCompleteFunction()]]

addAjaxToggleOnFunction()
~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAjaxToggleOnFunction() | I2CE_Page->addAjaxToggleOnFunction()]]

addAjaxToggleOffFunction()
~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#addAjaxToggleOffFunction() | I2CE_Page->addAjaxToggleOffFunction()]]

hasAjax()
~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#hasAjax() | I2CE_Page->hasAjax()]]

setDataTypePriority()
~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setDataTypePriority() | I2CE_Page->setDataTypePriority()]]

setData()
~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#setData() | I2CE_Page->setData()]]

getData()
~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#getData() | I2CE_Page->getData()]]

getDefaultData()
~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#getDefaultData() | I2CE_Page->getDefaultData()]]

removeData()
~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#removeData() | I2CE_Page->removeData()]]

getDataNames()
~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#getDataNames() | I2CE_Page->getDataNames()]]

ensureNode()
~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Page#ensureNode() | I2CE_Page->ensureNode()]]

userMessage()
~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Fuzzy#userMessage() | I2CE_Fuzzy->userMessage()]]

