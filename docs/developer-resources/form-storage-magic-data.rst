Form Storage -- Magic Data
================================================


Features
^^^^^^^^
Storing form data in magic data is intended to be used in the following situtations:


* centrally maintained data that does not change frequently
* data that you want translations/localizations for
* data that you do not care to track the history of changes
* data that you want to load in easily for a module


Storage
^^^^^^^
All the data for form $form is stored in the magic data instance at the path
 /I2CE/formsData/forms/$form
with each node underneath corresponding to an instance of the form.  For example,
under 
 /I2CE/formsData/forms/gender
we have
 'F' => Array [
    'last_modified' => '2009-04-27 1:23:45'
    'fields' => Array [
          'name' => 'Female' 
      ]
 ]
 'M' => Array [
     'last_modified' => '2009-04-27 1:23:45'
     'fields' => Array [
          'name' => 'Male' 
       ]
  ]
If there is a parent form for the form, it is saved under 'parent' node for form instance.

[[Category:Developer Resources]]
