Technical Overview: Form Storage -- LDAP
========================================

Form Storage Options
^^^^^^^^^^^^^^^^^^^^

The options specifying a LDAP storage for $form are stored at:
 /modules/forms/forms/$form/storage_options/LDAP
It is generally assumed that entryUUID will serve as ID of the form and that child forms correspond to child nodes in LDAP.

It has the following structure:

* connect: required parent node which contains connection information to the ldap server
* *port: Optional scalar node. The port to connect to.  Defaults to 389.
* *host: Optional scalar node.  The server to connect to.  Defaults to localhost.
* *user: Optional scalar node.  The user node to bind on.  Defaults to admin.
* *pass: Required scalar node.  The password user to bind the user with.
* *bind_dn: Optional scalar node. DN to bind to.  Defaults to 'dc=localhost'  Results in a bind query of the form "cn=$user,$bind_dn"
* save: Optional parent node.  Need to define if you want this to be writable form.
* *objectClass: Required scalar node.  The object class to save this form data as.
* *parent_dn: optional scalar node.  If evaluates to true, we look at the parent  form to see if it is stored in LDAP.  If so, we determine the parent id from the (assumed to be already saved) parent form.
* *dn: Required scalar node.  The base dn to save this form under.
* *rdn: required parent node.  Used to define the rdn under the base dn in terms of the form fields
* **printf:required scalar node.  the printf substitution string
* **printf_args: required parent node.  ordered children have keys integers and values the field names whose db value we wish to substitute into the printf string
* *attributes. Required scalar node.  Children names are the LDAP attribute fields we are writing to.  Values specify (in one of three ways) how to produce the attribute from the db values of the fields.  There are three possible structures for the child nodes which are checked in the following order:
* *#scalar node.  In this case, it names a field
* *#parent node with child node 'eval'
* *#*eval: required scalar node. which is php code to evaluate on the array $data whose keys are fields and values are the db values.
* *#parent node with child node 'printf'
* *#*printf: child scalar node.  the printf substitution string
* *#*printf_args: required parent node.  ordered children have keys integers and values the field names whose db value we wish to substitute into the printf string
* list: Required parent node containing named list queries.  The names are the names of the child nodes.  There is one required child node, populate which is defined below.  Other optional child nodes are defined using the same structure.
* *populate:  Required parent node.  The list query for retrieving data from LDAP.  Children are the options passed to the  `ldap_list <http://php.net/manual/en/function.ldap-list.php>`_  call:
* **base_dn: Required scalar node. the base dn to do the listing on
* **filter: Required scalar node. The filter
* **scope: Optional scale node. defaults to 'ONELEVEL'.  Can be one of 'ONELEVEL', 'SUBTREE','BASE'
* **attributes. Required scalar node.  Children names are fields names in the forms.  Values specify (in one of three ways) how to produce the db values of the fields from attributes in LDAP.  There are three possible structures for the child nodes which are checked in the following order:
* **#scalar node.  In this case, it names an attribute.  In the case where the field name is 'parent'  you can prefix this string with any number of "../"s to indicate you should walk up the LDAP data tree and get the indicated value.  For example "../entryUUID" will get the entryUUID attribute of the parent node in the LDAP tree.
* **#parent node with child node 'eval'
* **#*eval: required scalar node. which is php code to evaluate on the array $data whose keys are attributes and values are the the values of those attributes
* **#parent node with child node 'printf'
* **#*printf: child scalar node.  the printf substitution string
* **#*printf_args: required parent node.  ordered children have keys integers and values the attributes whose value we wish to substitute into the printf string

