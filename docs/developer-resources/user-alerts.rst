User Alerts
===========

In the (upcoming) 4.2 release of iHRIS, you can now send alerts to users.  As an administrator, you can manually send alerts from the '''Administer Users''' page under '''Configure System'''.

You can also send alerts manually in your PHP code (or using an external script if desired) to send alerts.  If you want to send alerts based on regular triggers, see the [[User Triggers]] page for more information on configuring that.

==Enable the Module==
You will need to enable the UserAlerts module.  You can do this from the '''Configure System''' page under '''Configure Modules'''.  It will be under iHRIS Common.  You can also add the requirement to your site configuration as follows:

<source lang="xml">
<requirement name="UserAlerts">
  <atLeast version="4.2" />
  <lessThan version="4.3" />
</requirement>
</source>

Advanced users can also enable the modules from a terminal by running the following command from your pages directory:

<source lang="bash">
php index.php --update=1 --enable=UserAlerts
</source>

You will need to restart memcached and your server after doing this from the command line to refresh the APC.

<source lang="bash">
sudo service memcached restart
sudo service apache2 restart
</source>

==Sending Alerts==

To send an alert, you can use the following code fragment:

<source lang="php">
$module_factory = I2CE_ModuleFactory::instance();
if ( $module_factory->isEnabled("UserAlerts") ) {
    $alerts = $module_factory->getClass("UserAlerts");
    $alerts->sendUserAlert('USERNAME', 'notice', 'ALERT MESSAGE', 'OPTIONAL LINK', 'OPTIONAL LINK TEXT');
} else {
    // Do something else since the module isn't enabled, or possibly just log it
    I2CE::raiseError( "Tried to send user alert, but the module isn't enabled.");
}
</source>

For the alert type, you can current use either '''notice''' or '''problem'''.  Problems will be highlighted in red and notices are just displayed.

==Viewing and Acknowledging Alerts==
If a user has any alerts, a link will appear in the top header of the page.  If any haven't been acknowledged, then this will have a red background.  The user can click the alert link to view all pending as well as old alerts.  Once an alert is seen, the user should acknowledge the alert so it will stop being red on every page.  The user can also review any old alerts.  All alerts are displayed based on the time send with the most recent at the top.  Pending alerts are shown with the oldest at the top.

==Advanced Customizations==
The user alerts are intended to show up in the top navigation bar next to the logout button.  You can customize this display if you would like so it can appear anywhere.

You can change any values in magic data (from your module configuration) under /modules/UserAlerts/display.  The following options are available:
; append_id 
: Default: '''sysUser''' 
: This is the HTML DOM ID that the alert content will be appended to.
; append_before
: Default: '''false'''
: If set to true, the alert content will be the first child of the '''append_id''' node.  With default values this will make it appear to the left of the logout link instead of to the right.
; append_file
: Default: '''user_alert_link.html'''
: You can either copy this file and customize it in your site or custom module, or replace it with a new file.
; append_tag
: Default: '''li'''
: If you change the '''append_file''', you may need to change the tag that is the root of that file if it's not longer an <li> element.
; pending_style
: Default: '''alerts_pending'''
: This is the CSS style that is used for pending alerts.  You can change this or just customize the CSS in your own CSS file.
; default_style
: Default: '''alerts_seen'''
: This is the CSS style that is used for acknowledged alerts.  You can change this or just customize the CSS in your own CSS file.

This is how the default options are configured in the module if you want to change them in your site or custom module:

<source lang="xml">
    <configurationGroup name="alert_settings" path="/modules/UserAlerts/display">
      <configuration name="append_id">
        <value>sysUser</value>
      </configuration>
      <configuration name="append_before" type="boolean">
        <value>false</value>
      </configuration>
      <configuration name="append_file">
        <value>user_alert_link.html</value>
      </configuration>
      <configuration name="append_tag">
        <value>li</value>
      </configuration>
      <configuration name="pending_style">
        <value>alerts_pending</value>
      </configuration>
      <configuration name="default_style">
        <value>alerts_seen</value>
      </configuration>
    </configurationGroup>
</source>

[[Category:Developer Resources]]
