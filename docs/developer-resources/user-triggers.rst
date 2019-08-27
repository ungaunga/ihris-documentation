User Triggers
================================================

In the (upcoming) 4.2 release of iHRIS, you can now trigger messages to users.  As an administrator, you can link a trigger to a user and they will be notified when the trigger is called depending on the trigger configuration.

For any triggers that you want to send that are based on hooks, you can simply define that hook in your custom module and call the trigger.


Enable the Module
^^^^^^^^^^^^^^^^^
You will need to enable the UserTriggers module.  You can do this from the **Configure System** page under **Configure Modules**.  It will be under iHRIS Common.  You can also add the requirement to your site configuration as follows:



.. code-block:: xml

    <requirement name="UserTriggers">
      <atLeast version="4.2" />
      <lessThan version="4.3" />
    </requirement>
    


Advanced users can also enable the modules from a terminal by running the following command from your pages directory:



.. code-block:: bash

    php index.php --update=1 --enable=UserTriggers
    


You will need to restart memcached and your server after doing this from the command line to refresh the APC.



.. code-block:: bash

    sudo service memcached restart
    sudo service apache2 restart
    



Defining a Trigger
^^^^^^^^^^^^^^^^^^
The first step is to define your new trigger.  Once defined, you can link the trigger with a user so they will be notified when the trigger is called.


Translatable Messages
~~~~~~~~~~~~~~~~~~~~~
Messages you want to be translatable can be configured under /modules/UserTriggers/triggers.  This allows you to just pass the required message key to the trigger method and it will pull out a translated messaged depending on the settings of the user that causes the trigger.  You can also define some other default messages here, for example **default_email_subject** is used for the email handler.  You can define these messages in your module with the following.  ('''Note:''' The default email subject also appends the display name of the trigger to the subject.)



.. code-block:: xml

        <configurationGroup name="messages" path="/modules/UserTriggers/messages" locale="en_US">
          <configuration name="default_email_subject">
            <value>Automated email for: </value>
          </configuration>
        </configurationGroup>
    



Configuring a Trigger
~~~~~~~~~~~~~~~~~~~~~

Triggers are defined in magic data under /modules/UserTriggers/triggers.  There are currently three types of [[#Trigger Handlers|handlers]] available:  alert, email, hook.  Arguments can be customized depending on the handler in the configuration or when the trigger is called.  Each trigger can enable any of these handlers that are desired so some triggers may only sent alerts, some only email and some may send both.  See [[#Hook Handler]] for a more advanced way to notify your users.

The structure of a trigger configuration is as follows:



* $trigger: [array] This is what you will use to call the trigger when desired.
* * display: [string] This is the value of the display name of the trigger.  It should be set with a locale so it can be translated.
* * handler: [array] The enabled handlers for this trigger.
* ** alert: [true|false] This is a boolean if you want to enable the alert handler for this trigger.
* ** email: [true|false] This is a boolean if you want to enable the email handler for this trigger.
* ** hook: [true|false] This is a boolean if you want to enable the hook handler for this trigger.
* * message: [array] The default messages for this trigger.
* ** prefix: [string] Any text you want prepended to the triggered message.
* ** suffix: [string] Any text you want appended to the triggered message.
* ** link: [url] A default URL to be sent with the message.  It may be overridden by the trigger call.
* ** link_text: [string] The text to go along with the link.  It may be overridden by the trigger call.
* * args: [array] Any arguments to pass along to the handlers.
* ** alert: [array] Any custom alert arguments.
* *** alert_type: [notice|problem] Set the alert type for this trigger. The default is **notice**.
* ** email: [array] Any custom email arguments.
* *** subject: [string] You can override the default email subject for this handler.
* ** hook: [array] Any custom hook arguments.
* *** hooks: [array] The list of hooks to be called.
* **** 0: [string] The hook to be called.

An example trigger may be defined in your module as follows:



.. code-block:: xml

    <configurationGroup name="my_trigger" path="/modules/UserTriggers/triggers/my_trigger">
      <configuration name="display" locale="en_US">
        <value>My Trigger</value>
      </configuration>
      <configurationGroup name="handler">
        <configuration name="alert" type="boolean">
          <value>true</value>
        </configuration>
        <configuration name="email" type="boolean">
          <value>true</value>
        </configuration>
      </configurationGroup>
      <configurationGroup name="message">
        <configuration name="prefix" locale="en_US">
          <value>This is my trigger: </value>
        </configuration>
        <configuration name="link">
          <value>http://demo.ihris.org/iHRIS/Manage/</value>
        </configuration>
        <configuration name="link_text" locale="en_US">
          <value>iHRIS Manage Demo</value>
        </configuration>
      </configurationGroup>
      <configurationGroup name="args">
        <configurationGroup name="email">
          <configuration name="subject" locale="en_US">
            <value>My Custom Subject</value>
          </configuration>
        </congurationGroup>
        <configurationGroup name="alert">
          <configuration name="alert_type">
            <value>problem</value>
          </configuration>
        </configurationGroup>
      </configurationGroup>
    </configurationGroup>
    



Calling a Trigger
^^^^^^^^^^^^^^^^^

In your code where you want to send off a trigger, you can use the following code:



.. code-block:: php

    $module_factory = I2CE_ModuleFactory::instance();
    if ( $module_factory->isEnabled("UserTriggers") ) {
        $triggers= $module_factory->getClass("UserTriggers");
        $args = array( 'email' => array( 'subject' => 'OPTIONAL TRIGGERED SUBJECT' ) );
        $triggers->trigger('my_trigger', 'MESSAGE_KEY', 'MESSAGE', true, 'OPTIONAL URL ADDITION', 'OPTIONAL LINK TEXT', $args );
    } else {
        // Do something else since the module isn't enabled, or possibly just log it
        I2CE::raiseError( "Tried to call a trigger, but the module isn't enabled.");
    }
    


When this is called, every user that is linked with the trigger will be notified based on the handlers, in this case the alert and email handlers.  The MESSAGE_KEY and MESSAGE are optional and if not included it will use the defined prefix and suffix of the trigger.  The argument after the message is the link.  If set to true, then the link defined for the trigger will be used with the **OPTIONAL URL ADDITION** appended to it.  Instead of being true, this can be a string with a different URL if desired.  The **$args** array will override any default arguments for the handlers defined by the trigger.

You can put this trigger code as part of an existing hook that you can define.  See [[#Hook Handler]] for more details on defining a hook in your module.


Advanced Customization
^^^^^^^^^^^^^^^^^^^^^^


Trigger Handlers
~~~~~~~~~~~~~~~~
There are currently three types of handlers available:  alert, email, hook.  The hook option is there so you can more easily customize what happens with the trigger, but you can also add additional handlers under /modules/UserTriggers/handlers.  You can also add more function calls to an existing handler so both would be called when the trigger uses the given handler.

The default handlers are defined in the module as:



.. code-block:: xml

        <configurationGroup name="handlers">
          <configuration name="email" type="delimited">
            <value>UserTriggers:triggerEmail</value>
          </configuration>
          <configuration name="hook" type="delimited">
            <value>UserTriggers:triggerHook</value>
          </configuration>
        </configurationGroup>
    


Additionally, the [[User Alerts]] module adds the following handler:


.. code-block:: xml

        <configuration name="Triggers" path="/modules/UserTriggers/handlers/alert" type="delimited">
          <value>UserAlerts:triggerAlert</value>
        </configuration>
    


What these mean is that when the **email** handler is enabled for a trigger, then the method triggerEmail will be called on the UserTriggers module class.  So if you defined a new module that could handle SMS, you could add an SMS handler and set up your own trigger method.

All the trigger handler methods must be defined to accept the following arguments:



.. code-block:: php

        /**
         * Handler method for triggers
         * @param string $username The username to be notified
         * @param string $trigger The trigger being called
         * @param string $message The message to send
         * @param string $link The optional link to include
         * @param string $link_text The link text for the link
         * @param array $args Any option arguments for this trigger handler
         * @return boolean
         */
        public function triggerMethod( $username, $trigger, $message, $link=false, $link_text='', $args=array() ) {
        }
    



Hook Handler
------------

If you want to have a custom trigger without having to create a new handler, you can use the hook handler and then define a custom hook for your notification.  You first define the hooks to be called in the trigger arguments or it can be overridden by the trigger call if desired.  The hook will be passed the same arguments as the triggerMethod above.

You can also call a trigger from an existing hook.  The concept is the same if you're creating a new hook that is defined in your trigger hook handler or if you want to add some hook code for an existing hook in the site.  To create a new hook for your trigger handler, you would add the following code to your module class.  For example we'll create a hook called ''''my_trigger_hook'''' that you could add as part of your trigger definition.  We'll also define a hook for when a person form is saved and call our trigger so you can see how that would be done.  The arguments for hooks will depend on the hook so you may need to refer to the calling hook to determine what is needed.  This hook is named 'form_post_save_person' and takes an array as an argument with the iHRIS_Person and I2CE_User objects defined as 'form' and 'user'.



.. code-block:: php

        /**
         * Retrn the array of hooks available in this module.
         * @return array
         */
        public static function getHooks() {
            return array(
                    "my_trigger_hook" => "my_trigger_method",
                    "form_post_save_person" => "person_saved",
                    );
        }
    
        /**
         * Handle the hook my_trigger_hook
         * @param string $username The username to be notified
         * @param string $trigger The trigger being called
         * @param string $message The message to send
         * @param string $link The optional link to include
         * @param string $link_text The link text for the link
         * @param array $args Any option arguments for this trigger handler
         */
        public function my_trigger_method( $username, $trigger, $message, $link, $link_text, $args ) {
            // Add your special handling for your hook here.
        }
    
        /**
         * Call a trigger after a person is saved.
         * @param array $details
         */
        public function person_saved( $details ) {
            $person = $details['form'];
            $user = $details['user'];
    
            $message = $person->firstname . " " . $person->surname . " was modified by " . $user->username;
            $link = 'http://MYSITE/iHRIS/Manage/view?id=' . $person->getNameId();
            $module_factory = I2CE_ModuleFactory::instance();
            if ( $module_factory->isEnabled("UserTriggers") ) {
                $triggers= $module_factory->getClass("UserTriggers");
                $triggers->trigger('my_trigger', null, $message, $link, null, 'Person Record' );
            } else {
                // Do something else since the module isn't enabled, or possibly just log it
                I2CE::raiseError( "Tried to call a trigger, but the module isn't enabled.");
            }
        }
    
    
    


[[Category:Developer Resources]]
