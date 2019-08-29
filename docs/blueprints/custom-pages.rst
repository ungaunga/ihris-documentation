Custom Pages
============

This is a planned feature for a future version of the software and is the intended basis for [[iHRIS Collect Design Overview|iHRIS Collect]], a data collection/survey tool.

Here is a technical sketch of what needs to be done.


* Modify/subclass i2ce_form_relationships in order to add the ability to specify the number of each type of forms that can be joined (one, two, ... )
* handle evaluating form relationship functions from within PHP -- perhaps by exec the sql function with the form fields as appropriate, or else don't allow sql functions in form relationships for pages.
* determining if a given pair of forms, or a given set of forms satisfies a relationship.
* Select the fields from the forms in the relationship you want in a particular page.    This is already done in the i2ce_swiss_report  you would only need to tweak the UI to remove the limits.
* choose the order that you want the forms displayed on the page.  this functionality could be subclassed from the i2ce_swiss_report
* choose the order that you want to display the fields of a form.  This might simply be a i2ce_swiss_report_view (or subclass for)
* mark the displayed fields as editable or not.  Subclass i2ce_swiss_report_view
* add in a way to mark a page as needing a "confirm" on save or not



