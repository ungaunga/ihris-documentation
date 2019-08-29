LMI Webforms
============

= Why use PHP? =

As of this writing, OpenMRS does not contain a mature platform for using and deploying forms outside of Microsoft's InfoPath.  While there are efforts underway, none are ready for production use.  Because of the short timeframe needed, I decided to create a way to use OpenMRS for administrative operations while using PHP for rapid development of web forms.

While the forms themselves left something to be desired, the time spent working on a the [[OpenMRS PHP Library]] has already paid off.  Other OpenMRS implementers have been looking for way to get around the requirement for Microsoft's Infopath so that OpenMRS would be usable via completely free software.  Hopfully the PHP library will provide users with another way to develop custom forms.

= How are the LMI Webforms set up? =

The webforms rely on a <tt>page</tt> parameter to specify which template and control file to use.  The environment is set up, if a control file is found, the page handler function is called, and then the template is displayed.

This offers a simplistic MVC model for doing web programming.

