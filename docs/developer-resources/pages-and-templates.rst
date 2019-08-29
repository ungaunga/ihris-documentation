Pages and Templates
===================

This tutorial describes the role of Pages and Templates in iHRIS.

A page handles each URL request. It is the basic functional unit of the system in which a URL request is processed and displayed.  If you wish to add new functionality to iHRIS, you may very likely need to add a new page.  An example page would be "Edit/add a scanned document."

A template is used to access the HTML elements of a page.  It is based on the  `PHP Document Object Model <http://php.net/manual/en/book.dom.php>`_ . 

=Pages=
Pages can be established to live directly under the base URL of the site, or under a module and all requests are delegated to the appropriate page class by the [[#Wrangler|wrangler]].  

The logic of a page is handled by the [[#Page Classes|page class]] which subclasses I2CE_Page via the *[[#The action() Method|action()]]*  method.  

The GET and POST variables are (by-default) [[#Variable Conversion|pre-processed]] by the page class.  All pages, again by default,  make use of a [[#Templates|templating]] which acts as a wrapper for the  `Document Object Model <http://en.wikipedia.org/wiki/Document_Object_Model>`_  (DOM).  There is also a built in [[#Tasks and Roles|task and role]] based permission system.

There are also, by abuse of language, pages for the PHP CLI.   We will only describe the pages which URL Requests in this article.

Page Classes
^^^^^^^^^^^^
All requests are eventually delegated by the wrangler to a sub-class of I2CE_Page.  This class handles all the business logic of the page.  It should determine the appropriate action to take based on whether it is a POST or GET request.   Multiple pages can be handled by one page class.  On construction, the page is passed an array of arguments that is defined by [[#Page Styles|page style]] and  a *[[#Converting a URL to a Page|request remainder]].*    One can optionally over-ride what gets sent as the array of POST and GET variables.  

Page Logic
^^^^^^^^^^
Here is an overview of the underlying default page logic:

* The POST and GOT variables are (usually) [[#Variable Conversion|pre-processed]].
* The array of arguments is produced by the wrangler as it process the page's [[#Page Styles|style]].
* The root or main template files, if any are loaded.   This is specified as the 'templates' argument.
* Optionally included in this page's arguments are [[Tasks and Roles|task and role]] restrictions for the page:
* *The roles allowed to view the page are stored under the key 'access'
* *The tasks that a user/role must have in order to view the page are stored under the key 'tasks'
* Once the user has passed the access restrictions for the page the following occurs:
* *The 'pre_page_action' [[Module Structure#Hooked Methods|hook]] is called
* *Any default html files are loaded for a page into the [[#Templates|template]] that was created for the page <br/> The default html file(s) are stored under the argument 'defaultHTMLFile'
* *The [[#The action() Method|''action()'']] method is called
* *If the *action()*  method did not return false then the 'post_page_action' [[Module Structure#Hooked Methods|hook]] is called
* *If the *action()*  method returns false then a user error message is generated.
* *If the page requested a redirect, the redirect is performed and execution halts.
* *If the page did not request a redirect then:
* **Any echo, print_r, etc. statements are appended to the bottom of the template's DOM.  These echo's, etc. should only be present for debugging purposes and should not be present in production code.
* **Unless the page was requested to supress its output, the template displays it's (HTML) output.  <br/>This is the only echo statement that <span style='color:tomato>should</span> be used on a production site to display html.

The action() Method
^^^^^^^^^^^^^^^^^^^
A sub-class of I2CE_Page should usually implement all of its logic by over-riding the *action()*  method.

Variable Conversion
^^^^^^^^^^^^^^^^^^^
The POST and GET variables, unless specifically requested not to, are pre-processed.  In addition to the POST and GET variables, REQUEST variables are created which are (usually) any variables that exist as either POST or GET variables. There are a few things that (usually) occur:

* If the GET variable 'req_query' exists, it parses the value and stores it as REQUEST variables
* Any variables names with ':'s are processed to defined multi-dimension arrays. For example:
 $_GET = array(
   'some:thing'] => '5'
   'some:otherthing' => '6'
  )
becomes:
 $_GET = array(
    'some'=>array(
        'thing'=>'5'
        'otherthing'=>'6'
    )
 )

* If a variable is named 'i2ce_json' it is *json_decode()* d and merged back in the variables.

=Wrangler=
The wranger is the main software component which delegates URL Request first to a pair of a *page name*  and module and then to the appropriate page class.  Let us suppose for this section that our site lives at the following base URL: 
 <nowiki>http://my.site.org/manage</nowiki>

Converting a URL to a Page
^^^^^^^^^^^^^^^^^^^^^^^^^^
Pages can live directly under the base URL, or under a module.  The wrangler processes the URL via the *I2CE_Wrangler->processPath()*  method and returns a *page name* , the module the *page name*  is registered with,  and a *request remainder* .  The module that a *page name*  is registered under is often not the module that provides the *page class* .  Let us outline the logic for the example:
 <nowiki>http://my.site.org/manage/some/thing/is/here</nowiki>

* If there is nothing after the base URL, then the module is 'I2CE' and the *page name*  is 'home'.  <br/>  There is no *request remainder* . <br/>  This is not the case in the above example.
* If 'some' is registered as a *page name*  provided by 'I2CE', then the module is 'I2CE' and the *page name*  is 'some'.  <br/>  The *request remainder*  is then *thing/is/here.*  <br/>  *some*  is considered to be a *page name*  registered under 'I2CE' if the [[Configuration (Magic) Data|magic data path]] */I2CE/page/some*  exists.
* Otherwise the module is 'some' and the following rules apply:
* *If there is nothing after the 'some', then the module is 'some' and the *page name*  is 'home' <br/>  There is no *request remainder* <br/>  This is not the case in the above example.
* *If 'thing' is a registered as a *page name*  for 'some' then, the module is 'some' and the *page name*  is 'some.'.  <br/>   The *request remainder*  is then *is/here*
Once the path has been processed, we verify that the returned page exists for the given module. If it does not, we try to handle the request by looking for a *default page name*  for the module.  The *default page name,*  if defined exists at the magic data path */modules/$module/default_page* .

The registered module, the *page name* , and the *request remainder*  call all be accessed through I2CE_Pages's API.

Page Styles
^^^^^^^^^^^
Once we have a valid module and page name associated to a URL, we begin processing the page's styles.  A page style can consist of three components:

* Another page style which this page style inherits the properties of
* A page class to associate to a page
* A nested array of arguments to pass the the page class constructor.  These are merged into any inherited arguments by *I2CE_Util::merge_recursive()*

=Templates=
Each page instance is assigned a template which is an instance of I2CE_TemplateMeister, and usually an instance of the sub-class I2CE_Template.  

The Template is essentially a wrapper class for a DOMDocument object with some useful convenience methods built in.  Although the additional functionality provided by I2CE_TemplateMeister and I2CE_Template  is initially very limited, it is greatly augmented by making use of [[Module Structure#Fuzzy Methods|fuzzy methods]].

The page will display the DOM contained in the template as html after the page has finished processing.  

Template Data
^^^^^^^^^^^^^
The most significant way the I2CE_Template case is augemented is to provide "Template Data."  The module *template-data*  provides the ability to assign arbitrary data to any node in the DOM.  The data exists in categories, such as 'FORM' or 'OPTION' and applies to all sub-nodes of the given node.  Each piece of data is assigned a name.

If the node is an given by specifying an *id*  (rather than giving an explict instanceof DOMNode) the data will be held in a cache until a node with the given *id*  is added to the template.

When looking for a piece of data assigned to a particular node, we start at the given node and walk up the DOM until the named data is found.  

For each category of template data, a default bit of data may be assigned which applies for the whole DOM.

There are several modules which make explicit use of the template data structure.

<span style='color:red'>Warning:</span>  The template data mechanism assumes that there is only one template in use per request.  Be very careful if you are using multiple templates in one page each making use of template data.

Display Data
~~~~~~~~~~~~
Display data are template data in the category 'DISPLAY' which can be set with the setDisplayData() and setDisplayDataImmediate() methods and provide a convenient way of manipulating the template files loaded. The template will look for any DOMElements with the name attribute set and process them according to their tag name and the template data, if any,  stored under the name attribute. Here is a list of the commonly used tags that are processed and their rules:

* div,  pre, span, textarea: the value of the template data is appended to the next content of the element
* input: If the template data is an array, is is considered to be an array or attribute=>value pairs which are set on the element.  <br/> If it is scalar valued, is is processed according to the value of the attribute type as follows::::
* *input: the attribute value is set to the value of the template data
* *checkbox: if it evaluates to true, then the attribute 'checked' is set.  otherwise it is removed
* select: If the value of the template data is an array, <option> tags are added with value attribute set to be the array key and the text content set to the corresponding array value
* a: if the template data is of scalar type then:
* *if the href value is not set, it is set to be the value of the template data.
* *if the href is set the value template date is appended with either a ? or a & as appropriate to the href attribute
* img:  If the template data is an array, it is used as a set of attribute=>value pairs.  If it is scalar, then the src attribute is set
* form:  If the template data is an array, it is used as a set of attribute=>value pairs.  If it is scalar, then the action attribute is set
* meta: If the template data is a scalar the content attribute is set
* If the element has the attribute ifset with (case insensitive) value 'true' or 't' or '1' and the template data is not set, then it is removed.
* If the element has the attribute ifset with (case insensitive) value other than 'true' or 't' or '1' and the template data is set, then it not removed.

Options
~~~~~~~
Closely related to the Display Data module is the Options module which saves template data in the category 'OPTIONS.'  It process tags of the form:
 <nowiki><select id='some_id'/></nowiki>
and if it finds an OPTION template data named 'some_id' it will append a <select> tag for each of these bits of data.

Form Data
~~~~~~~~~
A form can be set on any node and can be referenced as
 <nowiki><span type='form' name='form:field'/></nowiki>
where you would substitute 'form' and 'field' as appropriate.  If the 'form' is not specified it uses the default form, if any, set for the page.

Module Attribute
~~~~~~~~~~~~~~~~
Any DOM Elements with the attribute type set to be 'module' and 'name' attribute are processed according to certain rules. The value of the name attribute is  the name of a module.  The following attributes are recognized:

* ifenabled: can be t, true, !t or !true.  If true and the module is not enabled, or false and the module is enabled the the node is removed.
* if: Tries to call the module's function with the value of the attribute 'if.'  If the module returns (something which casts to) false the node is removed.  Prepending  the value with a ! causes the opposite behavior.
* call:  The value is used as the value of a method to call in the module's class.
Suppose we have
 <span type='module' name='my_module' call='someMethod([arg1],....[argN])
and that $module is the instance of the module class associated to my_module.  Then the results is the following call:
 $module->someMethod($node,$template,$args)
where $node is the  <nowiki><span></nowiki> node,  $template is the template object and the argument is the array of arguments $args = ($arg1,..,$argN)
where [argM] is turned into $argM according to the following rules:

* if [argM] starts with a $ then it refers to template data and the following rules apply:
* *The string has the form $abcd. The value of $argM becomes the template display data with name 'abcd.'
* *The string has the form ${WXYZ}abcd.  The value of $argM becomes the template data with category XYZ and with name 'abcd.'
* <NODE> becomes the instance of DOMNode (if any) that the permission string was called on
* <TEMPLATE> becomes the instance of I2CE_Template (if any) that the permission parser was called on
* <USER> becomes the instance of I2CE_User that is this session
* if [argM] starts with a single quote ' then it is a string until the next non-escaped ' is found
* if [argM] starts with a double quote " then is is a string until the next non-escaped " is found. <br/>In addition the following substitution rules apply:
* *any substring starting with $ and consisting of alpha-numeric characters, - or _ is interpreted as template display data to be substituted<br> For example "my name is $name" becomes "my name is Joe" if the template data named 'name' and with type DISPLAY is "Joe"
* *any substring starting with {$ is read until an enclosing } is found.  The string between the ${ and } is the name of DISPLAY template data which is then substituted.
* *To prevent the above, { and $ may be escaped with a \
* any string of of alpha-numeric character (and a few permitted punctuation marks) are interpreted as follows:
* *if is is of the form abcd(, then it is interpreted as another method to call on $module as:<br/> $module->abcd($subargs)<br/> where sub-args are processed (recursively) according to the same rules and bounded by the next enclosing )
* *otherwise if is is of the form wxyz->abcd(, then it is interpreted as another method to call on $sub_module as:<br/> $sub_module->abcd($subargs)<br/> where sub-args are processed (recursively) according to the same rules and bounded by the next enclosing ) and $sub_module is the module class instance associated with wxyz
* otherwise it is interpreted as a string

Arguments are separated by spaces or commas

Tags
^^^^
As "special cases" of moudle functions, following attributes are scanned for and processed:

* printf attribute: Appends to the node the results of printf substitution of the string with the specified arguments.  It also is locale aware and can make use of plural forms.  <br/> printf="'this is something %s',$data'

Scripts
^^^^^^^
Any scripts tags found in the body of the HTML  are moved to the header.

=Tasks and Roles=
[[Tasks and Roles|Tasks and roles]] are used to limit page access as well as the data displayed in the DOM.

