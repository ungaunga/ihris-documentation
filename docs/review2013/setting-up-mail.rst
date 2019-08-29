Setting Up Mail
===============

With version 4.1 of the software, we have added the possibility of using an SMTP server to send mail rather than requiring that you set up a Mail Transfer Agent (MTA)


Requirements
^^^^^^^^^^^^
We will need the PEAR::Mail module to be installed.  Under Ubuntu, you can do so with:


.. code-block:: bash

     sudo apt-get install php-mail
    



Configuration
^^^^^^^^^^^^^
Suppose you want to send all email via the SMTP server smtp.moh.gov via the user ihris. You can do so by adding the following to your site configuration file.


.. code-block:: xml

      <configurationGroup name='mailer' path='/modules/Mailer'>
          <configuration name='mail_server_backend'>
            <value>smtp</value>
          </configuration>
          <configuration name='mail_server_params' value='many' type='delimited'>
            <value>host:smtp.moh.gov</value>
            <value>port:25</value>
            <value>auth:1</value>
            <value>username:ihris</value>
            <value>password:XXXXXX</value>
          </configuration>
          <configuration name='mail_message_headers' value='many' type='delimited'>
            <value>From:ihris@moh.gov</value>
          </configuration>
    
        </configurationGroup>
    


The section 'mail_server_params' are exactly as defined [ http://pear.php.net/manual/en/package.mail.mail.factory.php here].

The section 'mail_message_headers' are the mail headers that are added by default to every message.  In this case, we are specifying that all message are coming from "ihris@moh.gov"



Very Important Warning
^^^^^^^^^^^^^^^^^^^^^^
 **WARNING**  Your password, XXXXX, is readable in this, so if you commit this to bzr, then you anyone can read your password.

Instead, what you should do is to leave XXXXX as the password in the site configuration file.  Then in the web interface:


* Click "Configure System"
* Click "Magic Data Browser"
* Click "modules"
* Click "Mailer"
* Click "mail_server_params"
* Change the value of "password" from "XXXX" to the correct password and click the "Set" button


