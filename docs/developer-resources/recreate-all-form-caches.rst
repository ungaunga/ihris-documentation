Recreate All Form Caches
========================

If you've imported data multiple times, the form cache will include some of that old data.  To completely recreate all the form caches follow these steps.  These instructions are for iHRIS version 3.1.x.  These are advanced instructions and should only be done if you know what you are doing.  You should back up your database before doing this in case anything goes wrong.

# Open up two browser windows.  One to the site and one on phpmyadmin.
# Go to Configure System then Browse Magic Data.
# Click modules
# Click CachedForms
# Click times
# Click generation
# This should list all the forms on the site with a number.  Click the Erase button at the bottom of the page.  Make sure the path at the top is: /modules/CachedForms/times/generation
# With PHPMyAdmin drop all the tables that start with hippo_.  You can check them all in the table list and then select “Drop” from the dropdown at the bottom.  It’ll display a confirmation message.  Just make sure it’s only the hippo_* tables.
# Back on the site go to Configure System then Cached Forms.
# At the bottom of the page click the link at Generate Cache for all forms.
# That should be it when it finishes redoing the form caches.
# You can then wait for the reports to regenerate automatically or go to Create Reports -> Reports and click the generate link next to them all.

[[Category:Developer Resources]]
