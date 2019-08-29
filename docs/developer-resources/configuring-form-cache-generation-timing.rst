Configuring Form Cache Generation Timing
========================================

Cached forms are used to save forms to a consistent format for exporting and for generating custom reports more quickly.  There are a few settings you can override in your site configuration file to change this behavior.  You can also see how to [[Turn Off Background Processes]] if you wish to not have the form caches update automatically.  You can also read more information about [[Form Caches]].


Configuration Settings
^^^^^^^^^^^^^^^^^^^^^^

; /modules/CachedForms/times/background_time
: Default value: **0** 
: This determines how much time in minutes that must pass before the background process starts to cache all forms if they are stale.  This just causes the background process to spawn, the process itself determines what needs to be updated based on the other timing settings.  If you set this to 0 then the background process will never start.  This is currently the default behavior because the Custom Reports module automatically updates any form caches it needs for each individual report when it runs either by background process, the command line or from generating the report through the Custom Report interface.  This doesn't mean that the caches will be run every X minutes, but if X minutes have passed the next time someone access the site the background process will be launched.
; /modules/CachedForms/times/stale_time
: Default value: **10** 
: This determines how much time must pass in minutes before a form is determined to be stale.  So if a form was cached 5 minutes ago and the setting is 10 then it won't try to cache it when the caching starts.  You can also force the cache generation to ignore this time.  If the setting is 0 then the forms will always be considered stale.
; /modules/CachedForms/times/fail_time
: Default value: **15** 
: This determines how much time must pass in minutes before it's determined that the last cache form background process has failed and can be restarted.  If you have a lot of data and lots of activity you may want to increase this time because it may take a while to run the form caches.  This doesn't have any effect on command line or running caches through the cached forms page.  To get around this you have to force the cache if a previous process got hung or died because the machine restarted or it failed for other reasons.
; /modules/CachedForms/times/recache_time
: Default value: **1440** 
: This determines how much time must pass before the entire form cache is dropped and recreated.  This is to avoid issues with the cache getting out of sync either from manually importing and dropping data or other errors.
; /modules/CachedForms/times/stale_time_by_storage
: Default values: 
:* **entry:10** 
:* **magicadata:30** 
:* **flat:20** 
:* **mutli_flat:20** 
: This overrides the stale_time setting based on the storage mechanism for the form.  Some form storage mechanisms may not be changed as often so the cache won't need to be updated as frequently.  The values can be for any [[Form Storage Mechanisms|storage mechanism]] that you have available in the system.
; /modules/CachedForms/times/stale_time_by_form
: Default values: **person:3** 
: This overrides the stale_time and stale_time_by_storage settings based on the individual form.  Some forms may need to be updated more frequently like the person form since it may be used more frequently.


Manually Caching Forms
^^^^^^^^^^^^^^^^^^^^^^
You can manually cache a form by going to the Configure System section and clicking on Cached Forms.  From there you can individually try to cache a form, force caching the form or dropping the form cache.  You can also do this for all cached forms at once.  You can also run the following commands from the command line from your site pages directory.  The --nocheck option is to keep it from checking for updated files to save processing time.  Note that when running commands like this from the command line you may need to clear the APC so that configuration variables can be updated from the database. You can also restart Apache to do this. 



.. code-block:: bash

    cd <SiteDirectory>/pages
    php index.php --page=/CachedForms/<CacheCommand> --nocheck=1
    


The possible commands you can use are as follows:
; cacheAll
: Cache all forms if they are stale.
; cacheAllForce
: Cache all forms ignoring if they're stale or not
; dropAll
: Drop all form caches.  You'd probably want to follow this with the command to cacheAll forms.
; createCache/''form''
: Create the cache for the given *form*  i.e. createCache/person.
; forceCreateCache/''form''
: Create the cache for the given *form*  ignoring staleness.
; dropCache/''form''
: Drop the cache for the given *form* .  You'd probably want to follow this with the command: createCache/''form''.


Caching Forms Background Process
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Every time a page is accessed the form cache checks to see if it needs to be run in the background.  The following checks are made to determine if the cache needs to run.

* Is background_time greater than 0?

  * If yes, then has background_time in minutes passed since the last time the process was started?

    * If yes, then is the caching status anything other than "done?"

      * If yes, then has more than fail_time minutes passed since it started?

        * If yes, then force caching all the forms.
        * If no, then don't run.

      * If no, then cache all the forms based on the stale times for those forms.

    * If no, then don't run.

  * If no, then don't run.


Caching Forms Process
^^^^^^^^^^^^^^^^^^^^^
When a cache all command is given through either background process, the command line or from the cached forms interface, the following process occurs:

* Is there another process currently "in_progress?"

  * If yes, then was the command forced?

    * If yes, then force running the caches for each form.
    * If no, then do nothing.

  * If no, then run all the caches for each form.

When a cache command is given for an individual form the following process happens.  This can be from a cache all or an individual cache command can be given for a form.


* Has stale_time passed since this form was last cached?  (Using any of the stale settings mentioned above: stale_time, stale_time_by_storage or stale_time_by form.)

  * If yes, then is the form dirty?  (Have any changes been made since the cache was last run?)

    * If yes, then update the cache.
    * If no, then do nothing.

  * If no, was the command forced?

    * If yes, then is the form dirty?

      * If yes, then update the cache.
      * If no, then do nothing.

    * If no, then do nothing.


Configuration Example
^^^^^^^^^^^^^^^^^^^^^

You can add the following to your site config file to override these settings.  You can add in only the settings you wish to change.



.. code-block:: xml

    <configurationGroup name="CachedForm_times" path="/modules/CachedForms/times">
      <displayName>Times</displayName>
      <configuration name="background_time">
        <displayName>Stale Time</displayName>
        <description>The time (in minutes) after which to launch the background page.  
          You can disable the launching of the background page by setting this to be less 
          than or equal to 0
        </description>
        <value>0</value>
      </configuration>
      <configuration name="stale_time">
        <displayName>Stale Time</displayName>
        <description>The time (in minutes) after which a cached table is consider stale.    
          Setting to be less than or equal to zero means that it is always considered stale.
        </description>
        <value>10</value>
      </configuration>
      <configuration name="fail_time">
        <displayName>Fail Time</displayName>
        <description>The time (in minutes) after which generation of a cached table is consider to have failed</description>
        <status>required:true</status>
        <value>15</value>
      </configuration>
      <configuration name="recache_time">
        <displayName>Fail Time</displayName>
        <description>The time (in minutes) after which the cached table is recached</description>
        <status>required:true</status>
        <value>1440</value>
      </configuration>
      <configuration name='stale_time_by_storage' values='many' type='delimited'>	
        <description>The default stale time in minutes for a form based on its storage mechanism.  
          If set, overides the value under times/stale_time.    Setting to be less than or equal to 
          zero means that it is always considered stale.
        </description>
        <value>entry:10</value>
        <value>magicadata:30</value>
        <value>flat:20</value>
        <value>mutli_flat:20</value>
      </configuration>
      <configuration name='stale_time_by_form' values='many' type='delimited'>
        <description>The default stale time in minutes for a specific form.  If set, overides the 
          value under times/stale_time_by_storage and times/stale_time.  Setting to be less than or 
          equal to zero means that it is always considered stale. 
        </description>
        <value>person:3</value>
      </configuration>
    </configurationGroup>
    




