Class: iHRIS Module Qualify MedicalData
=======================================

Note: This is an orphaned article that appears to have been superseded by later documentation.

This article describes the class *iHRIS_Module_Qualify_MedicalData* .

* Extends the class: [[Class: I2CE_Module | I2CE_Module]].
* Location: Part of the module [[iHRIS Qualify Module List#ihris-qualify-medical-data|ihris-qualify-medical-data]] in the package  `iHRIS Qualify <https://launchpad.net/qualify>`_
* Source: Defined in the file  `modules/MedicalData/iHRIS_Module_Qualify_MedicalData.php <http://bazaar.launchpad.net/~intrahealth+informatics/qualify/4.0.-release/annotate/head:/modules/MedicalData/iHRIS_Module_Qualify_MedicalData.php>`_
* Author: Carl Leitner <litlfred@ibiblio.org>, Luke Duncan <lduncan@intrahealth.org>
* Since: v3.1.0
@copyright Copyright &copy; 2008 IntraHealth International, Inc.

Methods
^^^^^^^

action_initialize()
~~~~~~~~~~~~~~~~~~~
Method called when the module is enabled for the first time. @param boolean -- returns true on success. false on error.

* Signature: public function action_initialize()

Inherited Methods
^^^^^^^^^^^^^^^^^

__construct()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#__construct() | I2CE_Module->__construct()]]

action_configure()
~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#action_configure() | I2CE_Module->action_configure()]]

action_disable()
~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#action_disable() | I2CE_Module->action_disable()]]

action_enable()
~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#action_enable() | I2CE_Module->action_enable()]]

conflict_external()
~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#conflict_external() | I2CE_Module->conflict_external()]]

getCLIHooks()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#getCLIHooks() | I2CE_Module->getCLIHooks()]]

getCLIMethods()
~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#getCLIMethods() | I2CE_Module->getCLIMethods()]]

getConfig()
~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#getConfig() | I2CE_Module->getConfig()]]

getHooks()
~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#getHooks() | I2CE_Module->getHooks()]]

getMethods()
~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#getMethods() | I2CE_Module->getMethods()]]

post_update()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#post_update() | I2CE_Module->post_update()]]

pre_upgrade()
~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#pre_upgrade() | I2CE_Module->pre_upgrade()]]

requirement_external()
~~~~~~~~~~~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#requirement_external() | I2CE_Module->requirement_external()]]

upgrade()
~~~~~~~~~
This public method is inherited from [[Class: I2CE_Module#upgrade() | I2CE_Module->upgrade()]]

_hasMethod()
~~~~~~~~~~~~
This public method is inherited from [[Class: I2CE_Fuzzy#_hasMethod() | I2CE_Fuzzy->_hasMethod()]]

Inherited Fuzzy Methods
^^^^^^^^^^^^^^^^^^^^^^^

launchBackgroundProcess()
~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Module#launchBackgroundProcess() | I2CE_Module->launchBackgroundProcess()]]

launchBackgroundPHPScript()
~~~~~~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Module#launchBackgroundPHPScript() | I2CE_Module->launchBackgroundPHPScript()]]

launchBackgroundPage()
~~~~~~~~~~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Module#launchBackgroundPage() | I2CE_Module->launchBackgroundPage()]]

userMessage()
~~~~~~~~~~~~~
This method is inherited from [[Class: I2CE_Fuzzy#userMessage() | I2CE_Fuzzy->userMessage()]]

