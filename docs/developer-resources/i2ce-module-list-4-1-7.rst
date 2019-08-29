I2CE Module List (4.1.7)
========================

{{otherversions|I2CE Module List}}
This is a list of all modules available in version 4.1.7-release of the package [https://launchpad.net/i2ce I2CE]
==BackgroundProcess==
This describes version 4.1.4.0 of the module Background Processes (BackgroundProcess) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/BackgroundProcess  i2ce/modules/BackgroundProcess ]
*Module Class: The module class is implemented by [[Class: I2CE_BackgroundProcess (4.1.7)| I2CE_BackgroundProcess]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#launchBackgroundProcess() | I2CE_Page->launchBackgroundProcess() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundProcess() | launchBackgroundProcess()]]
**Implements the method [[Class: I2CE_Module (4.1.7)#launchBackgroundProcess() | I2CE_Module->launchBackgroundProcess() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundProcess() | launchBackgroundProcess()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#launchBackgroundProcess() | I2CE_Template->launchBackgroundProcess() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundProcess() | launchBackgroundProcess()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#launchBackgroundPHPScript() | I2CE_Page->launchBackgroundPHPScript() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundPHPScript() | launchBackgroundPHPScript()]]
**Implements the method [[Class: I2CE_Module (4.1.7)#launchBackgroundPHPScript() | I2CE_Module->launchBackgroundPHPScript() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundPHPScript() | launchBackgroundPHPScript()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#launchBackgroundPHPScript() | I2CE_Template->launchBackgroundPHPScript() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundPHPScript() | launchBackgroundPHPScript()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#launchBackgroundPage() | I2CE_Page->launchBackgroundPage() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundPage() | launchBackgroundPage()]]
**Implements the method [[Class: I2CE_Module (4.1.7)#launchBackgroundPage() | I2CE_Module->launchBackgroundPage() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundPage() | launchBackgroundPage()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#launchBackgroundPage() | I2CE_Template->launchBackgroundPage() ]] via [[Class: I2CE_BackgroundProcess (4.1.7)#launchBackgroundPage() | launchBackgroundPage()]]
*Description: A convenience module to allow the running of process in the background
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/BackgroundProcess/configs modules/BackgroundProcess/configs] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/BackgroundProcess/templates modules/BackgroundProcess/templates] <br/>[[iHRIS Template List (4.1.7)#background_process_menu.html | background_process_menu.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/BackgroundProcess/css modules/BackgroundProcess/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/BackgroundProcess/ modules/BackgroundProcess/] <br/>[[Class: I2CE_BackgroundProcess (4.1.7) | I2CE_BackgroundProcess]], [[Class: I2CE_Page_BackgroundProcess (4.1.7) | I2CE_Page_BackgroundProcess]], [[Class: I2CE_Page_Run_SQL (4.1.7) | I2CE_Page_Run_SQL]]
==BinField==
This describes version 4.1.7.0 of the module Binary Fields (BinField) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Binary_Files  i2ce/modules/Forms/modules/Binary_Files ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_BinaryFiles (4.1.7)| I2CE_Module_BinaryFiles]]
*Description: A module that allows binary files for form fields
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MimeTypes | MimeTypes]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Binary_Files/configs modules/Forms/modules/Binary_Files/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Binary_Files/lib modules/Forms/modules/Binary_Files/lib] <br/>[[Class: I2CE_FormField_BINARY_FILE (4.1.7) | I2CE_FormField_BINARY_FILE]], [[Class: I2CE_FormField_DB_BLOB (4.1.7) | I2CE_FormField_DB_BLOB]], [[Class: I2CE_FormField_DOCUMENT (4.1.7) | I2CE_FormField_DOCUMENT]], [[Class: I2CE_FormField_IMAGE (4.1.7) | I2CE_FormField_IMAGE]], [[Class: I2CE_FormField_PASSPORT (4.1.7) | I2CE_FormField_PASSPORT]], [[Class: I2CE_Module_BinaryFiles (4.1.7) | I2CE_Module_BinaryFiles]], [[Class: I2CE_Page_BinaryField (4.1.7) | I2CE_Page_BinaryField]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Binary_Files/sql modules/Forms/modules/Binary_Files/sql] 
==CachedForms==
This describes version 4.1.7.0 of the module Cached Forms (CachedForms) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/CachedForms  i2ce/modules/Forms/modules/CachedForms ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_CachedForms (4.1.7)| I2CE_Module_CachedForms]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_FormField (4.1.7)#cachedTableReference() | I2CE_FormField->cachedTableReference() ]] via [[Class: I2CE_Module_CachedForms (4.1.7)#cachedTableReference() | cachedTableReference()]]
*Command Line Inteterprecter (CLI) Fuzzy Methods:
**Implements the CLI method [[Class: I2CE_FormField (4.1.7)#cachedTableReference() | I2CE_FormField->cachedTableReference() ]] via [[Class: I2CE_Module_CachedForms (4.1.7)#cachedTableReference() | cachedTableReference()]]
*Description: A module that allow the creation of a cached table corresponding to a form
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-flat | forms-storage-flat]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#BackgroundProcess | BackgroundProcess]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/CachedForms/configs modules/Forms/modules/CachedForms/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/CachedForms/lib modules/Forms/modules/CachedForms/lib] <br/>[[Class: I2CE_CachedForm (4.1.7) | I2CE_CachedForm]], [[Class: I2CE_FormStorage_cached (4.1.7) | I2CE_FormStorage_cached]], [[Class: I2CE_Module_CachedForms (4.1.7) | I2CE_Module_CachedForms]], [[Class: I2CE_Page_CachedForm (4.1.7) | I2CE_Page_CachedForm]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/CachedForms/templates modules/Forms/modules/CachedForms/templates] <br/>[[iHRIS Template List (4.1.7)#cachedforms_menu.html | cachedforms_menu.html]], [[iHRIS Template List (4.1.7)#cachedforms_menu_each.html | cachedforms_menu_each.html]], [[iHRIS Template List (4.1.7)#cachedforms_menu_exportProfile.html | cachedforms_menu_exportProfile.html]], [[iHRIS Template List (4.1.7)#cachedforms_menu_exportProfile_each.html | cachedforms_menu_exportProfile_each.html]]
==ColorPicker==
This describes version 4.1.2.0 of the module Color Picker (ColorPicker) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/ColorPicker  i2ce/modules/MooTools/modules/ColorPicker ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_ColorPicker (4.1.7)| I2CE_Module_ColorPicker]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_MagicDataTemplate (4.1.7)#processValues_color_triple_hex_single() | I2CE_MagicDataTemplate->processValues_color_triple_hex_single() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#processValues_color_triple_hex_single() | processValues_color_triple_hex_single()]]
**Implements the method [[Class: I2CE_MagicDataTemplate (4.1.7)#processValues_color_triple_hex_many() | I2CE_MagicDataTemplate->processValues_color_triple_hex_many() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#processValues_color_triple_hex_many() | processValues_color_triple_hex_many()]]
**Implements the method [[Class: I2CE_MagicDataTemplate (4.1.7)#processValues_color_triple_rgb_single() | I2CE_MagicDataTemplate->processValues_color_triple_rgb_single() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#processValues_color_triple_rgb_single() | processValues_color_triple_rgb_single()]]
**Implements the method [[Class: I2CE_MagicDataTemplate (4.1.7)#processValues_color_triple_rgb_many() | I2CE_MagicDataTemplate->processValues_color_triple_rgb_many() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#processValues_color_triple_rgb_many() | processValues_color_triple_rgb_many()]]
**Implements the method [[Class: I2CE_MagicDataTemplate (4.1.7)#processValues_color_hex_single() | I2CE_MagicDataTemplate->processValues_color_hex_single() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#processValues_color_hex_single() | processValues_color_hex_single()]]
**Implements the method [[Class: I2CE_MagicDataTemplate (4.1.7)#processValues_color_hex_many() | I2CE_MagicDataTemplate->processValues_color_hex_many() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#processValues_color_hex_many() | processValues_color_hex_many()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addColorPickerTriple() | I2CE_Page->addColorPickerTriple() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#addColorPickerTriple() | addColorPickerTriple()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addColorPickerTriple() | I2CE_Template->addColorPickerTriple() ]] via [[Class: I2CE_Module_ColorPicker (4.1.7)#addColorPickerTriple() | addColorPickerTriple()]]
*Description: Uses the MooTools Color Picker written by Kelly Anderson at http://www.sweetvision.com/projects/javascript-color-picker/. Enable some additional functionality for configuration as well
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/ColorPicker/scripts modules/MooTools/modules/ColorPicker/scripts] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/ColorPicker/templates modules/MooTools/modules/ColorPicker/templates] <br/>[[iHRIS Template List (4.1.7)#configuration_color_triple_hex_single.html | configuration_color_triple_hex_single.html]], [[iHRIS Template List (4.1.7)#configuration_color_triple_rgb_single.html | configuration_color_triple_rgb_single.html]], [[iHRIS Template List (4.1.7)#configuration_color_triple_single.html | configuration_color_triple_single.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/ColorPicker/css modules/MooTools/modules/ColorPicker/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/ColorPicker/ modules/MooTools/modules/ColorPicker/] <br/>[[Class: I2CE_Module_ColorPicker (4.1.7) | I2CE_Module_ColorPicker]]
==CustomReports==
This describes version 4.1.7.0 of the module Custom Reports (CustomReports) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports  i2ce/modules/CustomReports ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_CustomReports (4.1.7)| I2CE_Module_CustomReports]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Form (4.1.7)#isNumeric() | I2CE_Form->isNumeric() ]] via [[Class: I2CE_Module_CustomReports (4.1.7)#isNumeric() | isNumeric()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#isNumeric() | I2CE_FormField->isNumeric() ]] via [[Class: I2CE_Module_CustomReports (4.1.7)#isNumericField() | isNumericField()]]
*Description: Custom Reports
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#formRelationships | formRelationships]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#magicDataExport | magicDataExport]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#CachedForms | CachedForms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#jumper | jumper]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/configs modules/CustomReports/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/lib modules/CustomReports/lib] <br/>[[Class: I2CE_CustomReport (4.1.7) | I2CE_CustomReport]], [[Class: I2CE_CustomReport_Display (4.1.7) | I2CE_CustomReport_Display]], [[Class: I2CE_CustomReport_Display_Default (4.1.7) | I2CE_CustomReport_Display_Default]], [[Class: I2CE_CustomReport_Display_DefaultAction (4.1.7) | I2CE_CustomReport_Display_DefaultAction]], [[Class: I2CE_CustomReport_Template (4.1.7) | I2CE_CustomReport_Template]], [[Class: I2CE_Module_CustomReports (4.1.7) | I2CE_Module_CustomReports]], [[Class: I2CE_PageReportAction (4.1.7) | I2CE_PageReportAction]], [[Class: I2CE_Page_CustomReports (4.1.7) | I2CE_Page_CustomReports]], [[Class: I2CE_Page_Report_MagicDataExport (4.1.7) | I2CE_Page_Report_MagicDataExport]], [[Class: I2CE_Page_ShowReport (4.1.7) | I2CE_Page_ShowReport]], [[Class: I2CE_Swiss_CustomReports_Base (4.1.7) | I2CE_Swiss_CustomReports_Base]], [[Class: I2CE_Swiss_CustomReports_Report (4.1.7) | I2CE_Swiss_CustomReports_Report]], [[Class: I2CE_Swiss_CustomReports_ReportView (4.1.7) | I2CE_Swiss_CustomReports_ReportView]], [[Class: I2CE_Swiss_CustomReports_ReportView_Base (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Base]], [[Class: I2CE_Swiss_CustomReports_ReportView_Displays (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Displays]], [[Class: I2CE_Swiss_CustomReports_ReportView_Field (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Field]], [[Class: I2CE_Swiss_CustomReports_ReportView_Fields (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Fields]], [[Class: I2CE_Swiss_CustomReports_ReportView_Meister (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Meister]], [[Class: I2CE_Swiss_CustomReports_ReportView_Merge (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Merge]], [[Class: I2CE_Swiss_CustomReports_ReportView_Merges (4.1.7) | I2CE_Swiss_CustomReports_ReportView_Merges]], [[Class: I2CE_Swiss_CustomReports_ReportViews (4.1.7) | I2CE_Swiss_CustomReports_ReportViews]], [[Class: I2CE_Swiss_CustomReports_Report_Base (4.1.7) | I2CE_Swiss_CustomReports_Report_Base]], [[Class: I2CE_Swiss_CustomReports_Report_Meta (4.1.7) | I2CE_Swiss_CustomReports_Report_Meta]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Limit (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Limit]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Limits (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Limits]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Merge (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Merge]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Merges (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field_Merges]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field_ModuleLimit (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field_ModuleLimit]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Field_ModuleLimits (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Field_ModuleLimits]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForm_Fields (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForm_Fields]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingForms (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingForms]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingFunction (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingFunction]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingFunction_Limits (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingFunction_Limits]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingFunctions (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingFunctions]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingInternal (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingInternal]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingInternal_Limits (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingInternal_Limits]], [[Class: I2CE_Swiss_CustomReports_Report_ReportingInternals (4.1.7) | I2CE_Swiss_CustomReports_Report_ReportingInternals]], [[Class: I2CE_Swiss_CustomReports_Reports (4.1.7) | I2CE_Swiss_CustomReports_Reports]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/css modules/CustomReports/css] 
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/images modules/CustomReports/images] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/scripts modules/CustomReports/scripts] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/templates modules/CustomReports/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_Default.html | customReports_display_control_Default.html]], [[iHRIS Template List (4.1.7)#customReports_display_Default_base.html | customReports_display_Default_base.html]], [[iHRIS Template List (4.1.7)#customReports_display_limit_apply_Default.html | customReports_display_limit_apply_Default.html]], [[iHRIS Template List (4.1.7)#customReports_menu.html | customReports_menu.html]], [[iHRIS Template List (4.1.7)#customReports_nav_menu.html | customReports_nav_menu.html]], [[iHRIS Template List (4.1.7)#customReports_notfound.html | customReports_notfound.html]], [[iHRIS Template List (4.1.7)#customReports_notfound_create.html | customReports_notfound_create.html]], [[iHRIS Template List (4.1.7)#customreports_options.html | customreports_options.html]], [[iHRIS Template List (4.1.7)#customReports_pivot.html | customReports_pivot.html]], [[iHRIS Template List (4.1.7)#customReports_pivot_each.html | customReports_pivot_each.html]], [[iHRIS Template List (4.1.7)#customReports_report.html | customReports_report.html]], [[iHRIS Template List (4.1.7)#customReports_report_form.html | customReports_report_form.html]], [[iHRIS Template List (4.1.7)#customReports_report_form_field.html | customReports_report_form_field.html]], [[iHRIS Template List (4.1.7)#customReports_report_form_field_limit.html | customReports_report_form_field_limit.html]], [[iHRIS Template List (4.1.7)#customReports_report_form_field_module_limit.html | customReports_report_form_field_module_limit.html]], [[iHRIS Template List (4.1.7)#customReports_report_form_fields.html | customReports_report_form_fields.html]], [[iHRIS Template List (4.1.7)#customReports_report_form_fields_each.html | customReports_report_form_fields_each.html]], [[iHRIS Template List (4.1.7)#customReports_report_forms.html | customReports_report_forms.html]], [[iHRIS Template List (4.1.7)#customReports_report_forms_each.html | customReports_report_forms_each.html]], [[iHRIS Template List (4.1.7)#customReports_report_forms_form.html | customReports_report_forms_form.html]], [[iHRIS Template List (4.1.7)#customReports_report_function.html | customReports_report_function.html]], [[iHRIS Template List (4.1.7)#customReports_report_functions_each.html | customReports_report_functions_each.html]], [[iHRIS Template List (4.1.7)#customReports_report_functions_has.html | customReports_report_functions_has.html]], [[iHRIS Template List (4.1.7)#customReports_report_functions_no.html | customReports_report_functions_no.html]], [[iHRIS Template List (4.1.7)#customReports_report_internal.html | customReports_report_internal.html]], [[iHRIS Template List (4.1.7)#customReports_report_internals_each.html | customReports_report_internals_each.html]], [[iHRIS Template List (4.1.7)#customReports_report_internals_has.html | customReports_report_internals_has.html]], [[iHRIS Template List (4.1.7)#customReports_report_limits.html | customReports_report_limits.html]], [[iHRIS Template List (4.1.7)#customReports_report_limits_each.html | customReports_report_limits_each.html]], [[iHRIS Template List (4.1.7)#customReports_report_merge_edit.html | customReports_report_merge_edit.html]], [[iHRIS Template List (4.1.7)#customReports_report_merges.html | customReports_report_merges.html]], [[iHRIS Template List (4.1.7)#customReports_report_merges_each.html | customReports_report_merges_each.html]], [[iHRIS Template List (4.1.7)#customReports_report_meta.html | customReports_report_meta.html]], [[iHRIS Template List (4.1.7)#customReports_report_module_limits.html | customReports_report_module_limits.html]], [[iHRIS Template List (4.1.7)#customReports_report_module_limits_each.html | customReports_report_module_limits_each.html]], [[iHRIS Template List (4.1.7)#customReports_reports.html | customReports_reports.html]], [[iHRIS Template List (4.1.7)#customReports_reports_categories.html | customReports_reports_categories.html]], [[iHRIS Template List (4.1.7)#customReports_reports_category.html | customReports_reports_category.html]], [[iHRIS Template List (4.1.7)#customReports_reports_category_report.html | customReports_reports_category_report.html]], [[iHRIS Template List (4.1.7)#customReports_reports_new.html | customReports_reports_new.html]], [[iHRIS Template List (4.1.7)#customReports_reports_no_new.html | customReports_reports_no_new.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_displays.html | customReports_reportView_displays.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_displays_each.html | customReports_reportView_displays_each.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_edit.html | customReports_reportView_edit.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_field.html | customReports_reportView_field.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_field_numeric.html | customReports_reportView_field_numeric.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_fields.html | customReports_reportView_fields.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_fields_each.html | customReports_reportView_fields_each.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_merge_each.html | customReports_reportView_merge_each.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_merge_edit.html | customReports_reportView_merge_edit.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_merges.html | customReports_reportView_merges.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_merges_each.html | customReports_reportView_merges_each.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_nodisplay.html | customReports_reportView_nodisplay.html]], [[iHRIS Template List (4.1.7)#customReports_reportView_view.html | customReports_reportView_view.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_edit.html | customReports_reportViews_edit.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_existing_reportview.html | customReports_reportViews_existing_reportview.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_reports_edit.html | customReports_reportViews_reports_edit.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_reports_view.html | customReports_reportViews_reports_view.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_view.html | customReports_reportViews_view.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_views_each_edit.html | customReports_reportViews_views_each_edit.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_views_each_view.html | customReports_reportViews_views_each_view.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_views_edit.html | customReports_reportViews_views_edit.html]], [[iHRIS Template List (4.1.7)#customReports_reportViews_views_view.html | customReports_reportViews_views_view.html]], [[iHRIS Template List (4.1.7)#customReports_table.html | customReports_table.html]], [[iHRIS Template List (4.1.7)#customReports_table_data_cell.html | customReports_table_data_cell.html]], [[iHRIS Template List (4.1.7)#customReports_table_data_row.html | customReports_table_data_row.html]], [[iHRIS Template List (4.1.7)#customReports_table_head_cell.html | customReports_table_head_cell.html]], [[iHRIS Template List (4.1.7)#customReports_table_image_cell.html | customReports_table_image_cell.html]], [[iHRIS Template List (4.1.7)#customReports_table_link_cell.html | customReports_table_link_cell.html]], [[iHRIS Template List (4.1.7)#display_report_limit.html | display_report_limit.html]]
**Xml: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/xml modules/CustomReports/xml] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules modules/CustomReports/modules] <br/>[[#CustomReports-PrintedReportsODT |CustomReports-PrintedReportsODT]], [[#CustomReports-Selector |CustomReports-Selector]], [[#CustomReports_CrossTab |CustomReports_CrossTab]], [[#CustomReports_Export |CustomReports_Export]], [[#CustomReports_PDF |CustomReports_PDF]], [[#CustomReports_PieChart |CustomReports_PieChart]], [[#ReportArchiver |ReportArchiver]]
==CustomReports-PrintedReportsODT==
This describes version 4.1.7.0 of the module ODT Reports (CustomReports-PrintedReportsODT) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PrintedReportsODT  i2ce/modules/CustomReports/modules/PrintedReportsODT ]
*Description: Configuration options for reports that use ODT
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#textlayout | textlayout]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#ColorPicker | ColorPicker]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#PrintedFormsODT | PrintedFormsODT]] at least 4.0 and less than 4.2
*Paths:
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PrintedReportsODT/templates modules/CustomReports/modules/PrintedReportsODT/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_ODT.html | customReports_display_control_ODT.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PrintedReportsODT/lib modules/CustomReports/modules/PrintedReportsODT/lib] <br/>[[Class: I2CE_CustomReport_Display_ODT (4.1.7) | I2CE_CustomReport_Display_ODT]]
==CustomReports-Selector==
This describes version 4.1.7.0 of the module Report Selector (CustomReports-Selector) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CustomReportSelector  i2ce/modules/CustomReports/modules/CustomReportSelector ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_ReportSelector (4.1.7)| I2CE_Module_ReportSelector]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#addReportSelector() | I2CE_Page->addReportSelector() ]] via [[Class: I2CE_Module_ReportSelector (4.1.7)#addReportSelector() | addReportSelector()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addReportSelector() | I2CE_Template->addReportSelector() ]] via [[Class: I2CE_Module_ReportSelector (4.1.7)#addReportSelector() | addReportSelector()]]
*Description: Enables Ajax which to select a entry in a report
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CustomReportSelector/configs modules/CustomReports/modules/CustomReportSelector/configs] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CustomReportSelector/templates modules/CustomReports/modules/CustomReportSelector/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_Selector.html | customReports_display_control_Selector.html]], [[iHRIS Template List (4.1.7)#customReports_display_Selector_base.html | customReports_display_Selector_base.html]], [[iHRIS Template List (4.1.7)#customReports_Selector_table_data_cell.html | customReports_Selector_table_data_cell.html]], [[iHRIS Template List (4.1.7)#customReports_Selector_table_data_row.html | customReports_Selector_table_data_row.html]], [[iHRIS Template List (4.1.7)#reportselector.html | reportselector.html]], [[iHRIS Template List (4.1.7)#reportselector_content.html | reportselector_content.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CustomReportSelector/lib modules/CustomReports/modules/CustomReportSelector/lib] <br/>[[Class: I2CE_CustomReport_Display_Selector (4.1.7) | I2CE_CustomReport_Display_Selector]], [[Class: I2CE_Module_ReportSelector (4.1.7) | I2CE_Module_ReportSelector]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CustomReportSelector/css modules/CustomReports/modules/CustomReportSelector/css] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CustomReportSelector/scripts modules/CustomReports/modules/CustomReportSelector/scripts] 
==CustomReports_CrossTab==
This describes version 4.1.7.0 of the module Crosstab reports (CustomReports_CrossTab) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CrossTab  i2ce/modules/CustomReports/modules/CrossTab ]
*Description: Configuration options for reports that use Crosstab reports
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#ColorPicker | ColorPicker]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#maani-charts | maani-charts]] at least 4.7
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CrossTab/configs modules/CustomReports/modules/CrossTab/configs] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CrossTab/templates modules/CustomReports/modules/CrossTab/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_CrossTab.html | customReports_display_control_CrossTab.html]], [[iHRIS Template List (4.1.7)#customReports_display_CrossTab_base.html | customReports_display_CrossTab_base.html]], [[iHRIS Template List (4.1.7)#customReports_display_CrossTab_table.html | customReports_display_CrossTab_table.html]], [[iHRIS Template List (4.1.7)#customReports_display_limit_apply_CrossTab.html | customReports_display_limit_apply_CrossTab.html]], [[iHRIS Template List (4.1.7)#customReports_toomuch.html | customReports_toomuch.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CrossTab/lib modules/CustomReports/modules/CrossTab/lib] <br/>[[Class: I2CE_CustomReport_Display_CrossTab (4.1.7) | I2CE_CustomReport_Display_CrossTab]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CrossTab/css modules/CustomReports/modules/CrossTab/css] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/CrossTab/scripts modules/CustomReports/modules/CrossTab/scripts] 
==CustomReports_Export==
This describes version 4.1.7.0 of the module Export Reports (CustomReports_Export) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/Export  i2ce/modules/CustomReports/modules/Export ]
*Description: Configuration options for exported reports
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
*Paths:
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/Export/templates modules/CustomReports/modules/Export/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_Export.html | customReports_display_control_Export.html]], [[iHRIS Template List (4.1.7)#swiss_exporteditor.html | swiss_exporteditor.html]], [[iHRIS Template List (4.1.7)#swiss_xslt.html | swiss_xslt.html]], [[iHRIS Template List (4.1.7)#swiss_xslts.html | swiss_xslts.html]], [[iHRIS Template List (4.1.7)#swiss_xslts_each.html | swiss_xslts_each.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/Export/lib modules/CustomReports/modules/Export/lib] <br/>[[Class: I2CE_CustomReport_Display_Export (4.1.7) | I2CE_CustomReport_Display_Export]], [[Class: I2CE_Swiss_CustomReport_ReportView_ExportEditor (4.1.7) | I2CE_Swiss_CustomReport_ReportView_ExportEditor]], [[Class: I2CE_Swiss_XSLT (4.1.7) | I2CE_Swiss_XSLT]], [[Class: I2CE_Swiss_XSLTS (4.1.7) | I2CE_Swiss_XSLTS]]
==CustomReports_PDF==
This describes version 4.1.7.0 of the module PDF Reports (CustomReports_PDF) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PDF  i2ce/modules/CustomReports/modules/PDF ]
*Description: Configuration options for reports that use PDF
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#textlayout | textlayout]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#ColorPicker | ColorPicker]] at least 4.1 and less than 4.2
*Paths:
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PDF/templates modules/CustomReports/modules/PDF/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_PDF.html | customReports_display_control_PDF.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PDF/lib modules/CustomReports/modules/PDF/lib] <br/>[[Class: I2CE_CustomReport_Display_PDF (4.1.7) | I2CE_CustomReport_Display_PDF]]
==CustomReports_PieChart==
This describes version 4.1.5.0 of the module Pie and Chart (CustomReports_PieChart) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PieChart  i2ce/modules/CustomReports/modules/PieChart ]
*Description: Configuration options for reports that use Pie and Charts
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#ColorPicker | ColorPicker]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#maani-charts | maani-charts]] at least 4.7
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PieChart/configs modules/CustomReports/modules/PieChart/configs] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PieChart/templates modules/CustomReports/modules/PieChart/templates] <br/>[[iHRIS Template List (4.1.7)#customReports_display_control_PieChart.html | customReports_display_control_PieChart.html]], [[iHRIS Template List (4.1.7)#customReports_display_limit_apply_PieChart.html | customReports_display_limit_apply_PieChart.html]], [[iHRIS Template List (4.1.7)#customReports_display_PieChart_base.html | customReports_display_PieChart_base.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PieChart/lib modules/CustomReports/modules/PieChart/lib] <br/>[[Class: I2CE_CustomReport_Display_PieChart (4.1.7) | I2CE_CustomReport_Display_PieChart]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/PieChart/css modules/CustomReports/modules/PieChart/css] 
==DatePicker==
This describes version 1.17.5 of the module Date Picker (DatePicker) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/DatePicker  i2ce/modules/MooTools/modules/DatePicker ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_DatePicker (4.1.7)| I2CE_Module_DatePicker]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#addDatePicker() | I2CE_Page->addDatePicker() ]] via [[Class: I2CE_Module_DatePicker (4.1.7)#addDatePicker() | addDatePicker()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addDatePicker() | I2CE_Template->addDatePicker() ]] via [[Class: I2CE_Module_DatePicker (4.1.7)#addDatePicker() | addDatePicker()]]
*Description: Uses the MooTools Color Date http://www.monkeyphysics.com/mootools/script/2/datepicker
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/DatePicker/configs modules/MooTools/modules/DatePicker/configs] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/DatePicker/scripts modules/MooTools/modules/DatePicker/scripts] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/DatePicker/css modules/MooTools/modules/DatePicker/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/DatePicker/ modules/MooTools/modules/DatePicker/] <br/>[[Class: I2CE_Module_DatePicker (4.1.7) | I2CE_Module_DatePicker]]
==DisplayData==
This describes version 4.1.4.0 of the module I2CE Display Data (DisplayData) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules/DisplayData  i2ce/modules/TemplateData/modules/DisplayData ]
*Module Class: The module class is implemented by [[Class: I2CE_DisplayData (4.1.7)| I2CE_DisplayData]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Template (4.1.7)#setDisplayData() | I2CE_Template->setDisplayData() ]] via [[Class: I2CE_DisplayData (4.1.7)#setDisplayData() | setDisplayData()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setDisplayDataImmediate() | I2CE_Template->setDisplayDataImmediate() ]] via [[Class: I2CE_DisplayData (4.1.7)#setDisplayDataImmediate() | setDisplayDataImmediate()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#selectOptionsImmediate() | I2CE_Template->selectOptionsImmediate() ]] via [[Class: I2CE_DisplayData (4.1.7)#selectOptionsImmediate() | selectOptionsImmediate()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#selectOptionsImmediate() | I2CE_Page->selectOptionsImmediate() ]] via [[Class: I2CE_DisplayData (4.1.7)#selectOptionsImmediate() | selectOptionsImmediate()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setDisplayData() | I2CE_Page->setDisplayData() ]] via [[Class: I2CE_DisplayData (4.1.7)#setDisplayData() | setDisplayData()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setDisplayDataImmediate() | I2CE_Page->setDisplayDataImmediate() ]] via [[Class: I2CE_DisplayData (4.1.7)#setDisplayDataImmediate() | setDisplayDataImmediate()]]
*Description: Adds display data to the template
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#template-data | template-data]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules/DisplayData/ modules/TemplateData/modules/DisplayData/] <br/>[[Class: I2CE_DisplayData (4.1.7) | I2CE_DisplayData]]
==Fields==
This describes version 4.1.7.0 of the module I2CE Fields (Fields) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields  i2ce/modules/Forms/modules/Fields ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Fields (4.1.7)| I2CE_Module_Fields]]
*Description: Adds a few basic form field types to the system as well as some field container functionality
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#template-data | template-data]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#DisplayData | DisplayData]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Optionally Enables: [[iHRIS Module List (4.1.7)#DatePicker | DatePicker]]
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/configs modules/Forms/modules/Fields/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/lib modules/Forms/modules/Fields/lib] <br/>[[Class: I2CE_Entry (4.1.7) | I2CE_Entry]], [[Class: I2CE_FieldContainer (4.1.7) | I2CE_FieldContainer]], [[Class: I2CE_FieldContainer_Factory (4.1.7) | I2CE_FieldContainer_Factory]], [[Class: I2CE_FormField (4.1.7) | I2CE_FormField]], [[Class: I2CE_FormField_ASSOC_BOOL (4.1.7) | I2CE_FormField_ASSOC_BOOL]], [[Class: I2CE_FormField_ASSOC_FLOAT (4.1.7) | I2CE_FormField_ASSOC_FLOAT]], [[Class: I2CE_FormField_ASSOC_INT (4.1.7) | I2CE_FormField_ASSOC_INT]], [[Class: I2CE_FormField_ASSOC_LIST (4.1.7) | I2CE_FormField_ASSOC_LIST]], [[Class: I2CE_FormField_ASSOC_PERCENT (4.1.7) | I2CE_FormField_ASSOC_PERCENT]], [[Class: I2CE_FormField_BOOL (4.1.7) | I2CE_FormField_BOOL]], [[Class: I2CE_FormField_DATE_HMS (4.1.7) | I2CE_FormField_DATE_HMS]], [[Class: I2CE_FormField_DATE_MD (4.1.7) | I2CE_FormField_DATE_MD]], [[Class: I2CE_FormField_DATE_TIME (4.1.7) | I2CE_FormField_DATE_TIME]], [[Class: I2CE_FormField_DATE_Y (4.1.7) | I2CE_FormField_DATE_Y]], [[Class: I2CE_FormField_DATE_YMD (4.1.7) | I2CE_FormField_DATE_YMD]], [[Class: I2CE_FormField_DB_DATE (4.1.7) | I2CE_FormField_DB_DATE]], [[Class: I2CE_FormField_DB_INT (4.1.7) | I2CE_FormField_DB_INT]], [[Class: I2CE_FormField_DB_STRING (4.1.7) | I2CE_FormField_DB_STRING]], [[Class: I2CE_FormField_DB_TEXT (4.1.7) | I2CE_FormField_DB_TEXT]], [[Class: I2CE_FormField_INT (4.1.7) | I2CE_FormField_INT]], [[Class: I2CE_FormField_INT_GENERATE (4.1.7) | I2CE_FormField_INT_GENERATE]], [[Class: I2CE_FormField_INT_LIST (4.1.7) | I2CE_FormField_INT_LIST]], [[Class: I2CE_FormField_INT_RANGE (4.1.7) | I2CE_FormField_INT_RANGE]], [[Class: I2CE_FormField_STRING_LINE (4.1.7) | I2CE_FormField_STRING_LINE]], [[Class: I2CE_FormField_STRING_MLINE (4.1.7) | I2CE_FormField_STRING_MLINE]], [[Class: I2CE_FormField_STRING_PASS (4.1.7) | I2CE_FormField_STRING_PASS]], [[Class: I2CE_FormField_STRING_TEXT (4.1.7) | I2CE_FormField_STRING_TEXT]], [[Class: I2CE_FormField_TOGGLE (4.1.7) | I2CE_FormField_TOGGLE]], [[Class: I2CE_FormField_YESNO (4.1.7) | I2CE_FormField_YESNO]], [[Class: I2CE_Module_Fields (4.1.7) | I2CE_Module_Fields]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/templates modules/Forms/modules/Fields/templates] <br/>[[iHRIS Template List (4.1.7)#assoc_bool_input.html | assoc_bool_input.html]], [[iHRIS Template List (4.1.7)#assoc_input.html | assoc_input.html]], [[iHRIS Template List (4.1.7)#assoc_input_container.html | assoc_input_container.html]], [[iHRIS Template List (4.1.7)#display_field.html | display_field.html]], [[iHRIS Template List (4.1.7)#form_field.html | form_field.html]], [[iHRIS Template List (4.1.7)#form_field_condensed.html | form_field_condensed.html]], [[iHRIS Template List (4.1.7)#simple_display_field.html | simple_display_field.html]]
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/scripts modules/Forms/modules/Fields/scripts] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/modules modules/Forms/modules/Fields/modules] <br/>[[#Percent |Percent]], [[#fields-enum |fields-enum]]
==FileDump==
This describes version 4.1.0 of the module File Dump (FileDump) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/FileDump  i2ce/modules/Pages/modules/FileDump ]
*Description: File Download Utility
*Requirements:
**[[iHRIS Module List (4.1.7)#MimeTypes | MimeTypes]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/FileDump/configs modules/Pages/modules/FileDump/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/FileDump/ modules/Pages/modules/FileDump/] <br/>[[Class: I2CE_FileDump (4.1.7) | I2CE_FileDump]]
==Float==
This describes version 4.1.7.0 of the module Float (Float) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Float  i2ce/modules/Forms/modules/Float ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Float (4.1.7)| I2CE_Module_Float]]
*Description: A module that allows the float formfield
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Float/lib modules/Forms/modules/Float/lib] <br/>[[Class: I2CE_FormField_DB_FLOAT (4.1.7) | I2CE_FormField_DB_FLOAT]], [[Class: I2CE_FormField_FLOAT (4.1.7) | I2CE_FormField_FLOAT]], [[Class: I2CE_FormField_PERCENT (4.1.7) | I2CE_FormField_PERCENT]], [[Class: I2CE_Module_Float (4.1.7) | I2CE_Module_Float]]
==FormWorm==
This describes version 4.1.7.0 of the module Form Worm (FormWorm) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/FormWorm  i2ce/modules/MooTools/modules/FormWorm ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_FormWorm (4.1.7)| I2CE_Module_FormWorm]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#addFormWorm() | I2CE_Page->addFormWorm() ]] via [[Class: I2CE_Module_FormWorm (4.1.7)#addFormWorm() | addFormWorm()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addFormWorm() | I2CE_Template->addFormWorm() ]] via [[Class: I2CE_Module_FormWorm (4.1.7)#addFormWorm() | addFormWorm()]]
*Description: A collection of javascript utilities to handle form verification and submission of forms with multiple actions
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools-I2CE | MooTools-I2CE]] at least 4.1 and less than 4.2
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/FormWorm/scripts modules/MooTools/modules/FormWorm/scripts] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/FormWorm/css modules/MooTools/modules/FormWorm/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/FormWorm/ modules/MooTools/modules/FormWorm/] <br/>[[Class: I2CE_Module_FormWorm (4.1.7) | I2CE_Module_FormWorm]]
==I2CE==
This describes version 4.1.7.0 of the module I2CE Basic System (I2CE) 
It is the top module of this package
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/  i2ce/ ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Core (4.1.7)| I2CE_Module_Core]]
*Description: The I2CE Core System Configuration
*Paths:
**Misc: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head://I2CE_config.inc.php /I2CE_config.inc.php] ,[http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head://I2CE_structure.sql /I2CE_structure.sql] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head://lib /lib] <br/>[[Class: I2CE (4.1.7) | I2CE]], [[Class: I2CE_CLI (4.1.7) | I2CE_CLI]], [[Class: I2CE_Configurator (4.1.7) | I2CE_Configurator]], [[Class: I2CE_Date (4.1.7) | I2CE_Date]], [[Class: I2CE_Dumper (4.1.7) | I2CE_Dumper]], [[Class: I2CE_FileSearch (4.1.7) | I2CE_FileSearch]], [[Class: I2CE_FileSearch_Caching (4.1.7) | I2CE_FileSearch_Caching]], [[Class: I2CE_Fuzzy (4.1.7) | I2CE_Fuzzy]], [[Class: I2CE_Locales (4.1.7) | I2CE_Locales]], [[Class: I2CE_MagicData (4.1.7) | I2CE_MagicData]], [[Class: I2CE_MagicDataNode (4.1.7) | I2CE_MagicDataNode]], [[Class: I2CE_MagicDataStorage (4.1.7) | I2CE_MagicDataStorage]], [[Class: I2CE_MagicDataStorageAPC (4.1.7) | I2CE_MagicDataStorageAPC]], [[Class: I2CE_MagicDataStorageDB (4.1.7) | I2CE_MagicDataStorageDB]], [[Class: I2CE_MagicDataStorageDBAlt (4.1.7) | I2CE_MagicDataStorageDBAlt]], [[Class: I2CE_MagicDataStorageMem (4.1.7) | I2CE_MagicDataStorageMem]], [[Class: I2CE_MagicDataStorageMemcached (4.1.7) | I2CE_MagicDataStorageMemcached]], [[Class: I2CE_MagicDataStorageMongoDB (4.1.7) | I2CE_MagicDataStorageMongoDB]], [[Class: I2CE_MagicDataTemplate (4.1.7) | I2CE_MagicDataTemplate]], [[Class: I2CE_Module (4.1.7) | I2CE_Module]], [[Class: I2CE_ModuleFactory (4.1.7) | I2CE_ModuleFactory]], [[Class: I2CE_Module_Core (4.1.7) | I2CE_Module_Core]], [[Class: I2CE_Process (4.1.7) | I2CE_Process]], [[Class: I2CE_TemplateMeister (4.1.7) | I2CE_TemplateMeister]], [[Class: I2CE_Updater (4.1.7) | I2CE_Updater]], [[Class: I2CE_UserAccess_Mechanism (4.1.7) | I2CE_UserAccess_Mechanism]], [[Class: I2CE_Util (4.1.7) | I2CE_Util]], [[Class: I2CE_Validate (4.1.7) | I2CE_Validate]], [[Class: I2CE_Error (4.1.7) | I2CE_Error]], [[Class: I2CE_Error (4.1.7) | I2CE_Error]]
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head://modules /modules] <br/>[[#BackgroundProcess |BackgroundProcess]], [[#CustomReports |CustomReports]], [[#ImportExport |ImportExport]], [[#Mailer |Mailer]], [[#MimeTypes |MimeTypes]], [[#MooTools |MooTools]], [[#Timer |Timer]], [[#YAML_spyc |YAML_spyc]], [[#forms |forms]], [[#i2ce-site |i2ce-site]], [[#jumper |jumper]], [[#maani-charts |maani-charts]], [[#magicDataExport |magicDataExport]], [[#messageHandler |messageHandler]], [[#pChart |pChart]], [[#pages |pages]], [[#permissions |permissions]], [[#swissfactory |swissfactory]], [[#template-data |template-data]], [[#user |user]]
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head://scripts /scripts] 
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head://sql /sql] 
==ImportExport==
This describes version 0.9 of the module Import Export Support (ImportExport) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/ImportExport  i2ce/modules/ImportExport ]
*Module Class: The module class is implemented by [[Class: I2CE_Import_Export (4.1.7)| I2CE_Import_Export]]
*Description: Enables an XML Import and Export tool which allows offline access.
*Paths:
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/ImportExport/sql modules/ImportExport/sql] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/ImportExport/lib modules/ImportExport/lib] <br/>[[Class: I2CE_Import_Export (4.1.7) | I2CE_Import_Export]]
==Lists==
This describes version 4.1.7.0 of the module Form Lists (Lists) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists  i2ce/modules/Forms/modules/Lists ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Lists (4.1.7)| I2CE_Module_Lists]]
*Description: Database Lists
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-magicdata | forms-storage-magicdata]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#TreeSelect | TreeSelect]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#jumper | jumper]] at least 4.1 and less than 4.2
*Optionally Enables: [[iHRIS Module List (4.1.7)#tabbed-pages | tabbed-pages]]
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/configs modules/Forms/modules/Lists/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/lib modules/Forms/modules/Lists/lib] <br/>[[Class: I2CE_DataTree (4.1.7) | I2CE_DataTree]], [[Class: I2CE_FormField_MAP (4.1.7) | I2CE_FormField_MAP]], [[Class: I2CE_FormField_MAPPED (4.1.7) | I2CE_FormField_MAPPED]], [[Class: I2CE_FormField_MAP_MULT (4.1.7) | I2CE_FormField_MAP_MULT]], [[Class: I2CE_FormField_MAP_MULTUNION (4.1.7) | I2CE_FormField_MAP_MULTUNION]], [[Class: I2CE_FormField_REMAP (4.1.7) | I2CE_FormField_REMAP]], [[Class: I2CE_List (4.1.7) | I2CE_List]], [[Class: I2CE_Module_Lists (4.1.7) | I2CE_Module_Lists]], [[Class: I2CE_PageAutoList (4.1.7) | I2CE_PageAutoList]], [[Class: I2CE_PageAutoListEdit (4.1.7) | I2CE_PageAutoListEdit]], [[Class: I2CE_PageFormLists (4.1.7) | I2CE_PageFormLists]], [[Class: I2CE_PageRemap (4.1.7) | I2CE_PageRemap]], [[Class: I2CE_PageViewList (4.1.7) | I2CE_PageViewList]], [[Class: I2CE_SimpleCodedList (4.1.7) | I2CE_SimpleCodedList]], [[Class: I2CE_SimpleList (4.1.7) | I2CE_SimpleList]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/templates modules/Forms/modules/Lists/templates] <br/>[[iHRIS Template List (4.1.7)#auto_button_save_return.html | auto_button_save_return.html]], [[iHRIS Template List (4.1.7)#auto_edit_list.html | auto_edit_list.html]], [[iHRIS Template List (4.1.7)#auto_list.html | auto_list.html]], [[iHRIS Template List (4.1.7)#auto_list_type_header.html | auto_list_type_header.html]], [[iHRIS Template List (4.1.7)#auto_lists_type_header_alphabet.html | auto_lists_type_header_alphabet.html]], [[iHRIS Template List (4.1.7)#auto_lists_type_header_alphabet_clear.html | auto_lists_type_header_alphabet_clear.html]], [[iHRIS Template List (4.1.7)#auto_lists_type_header_alphabet_selected.html | auto_lists_type_header_alphabet_selected.html]], [[iHRIS Template List (4.1.7)#auto_lists_type_list.html | auto_lists_type_list.html]], [[iHRIS Template List (4.1.7)#auto_lists_type_mapped.html | auto_lists_type_mapped.html]], [[iHRIS Template List (4.1.7)#auto_view_linked.html | auto_view_linked.html]], [[iHRIS Template List (4.1.7)#auto_view_list.html | auto_view_list.html]], [[iHRIS Template List (4.1.7)#button_confirm_admin.html | button_confirm_admin.html]], [[iHRIS Template List (4.1.7)#list_add_link.html | list_add_link.html]], [[iHRIS Template List (4.1.7)#lists_form_base.html | lists_form_base.html]], [[iHRIS Template List (4.1.7)#lists_form_simple.html | lists_form_simple.html]], [[iHRIS Template List (4.1.7)#lists_form_simple_coded.html | lists_form_simple_coded.html]], [[iHRIS Template List (4.1.7)#lists_type_dual.html | lists_type_dual.html]], [[iHRIS Template List (4.1.7)#lists_type_dual_row.html | lists_type_dual_row.html]], [[iHRIS Template List (4.1.7)#lists_type_header.html | lists_type_header.html]], [[iHRIS Template List (4.1.7)#lists_type_header_alphabet.html | lists_type_header_alphabet.html]], [[iHRIS Template List (4.1.7)#lists_type_header_alphabet_clear.html | lists_type_header_alphabet_clear.html]], [[iHRIS Template List (4.1.7)#lists_type_header_alphabet_selected.html | lists_type_header_alphabet_selected.html]], [[iHRIS Template List (4.1.7)#lists_type_list.html | lists_type_list.html]], [[iHRIS Template List (4.1.7)#lists_type_mapped.html | lists_type_mapped.html]], [[iHRIS Template List (4.1.7)#lists_type_mapped_default.html | lists_type_mapped_default.html]], [[iHRIS Template List (4.1.7)#lists_type_row.html | lists_type_row.html]], [[iHRIS Template List (4.1.7)#lists_type_row_remapped.html | lists_type_row_remapped.html]], [[iHRIS Template List (4.1.7)#lists_type_select.html | lists_type_select.html]], [[iHRIS Template List (4.1.7)#menu_view.html | menu_view.html]], [[iHRIS Template List (4.1.7)#remap.html | remap.html]], [[iHRIS Template List (4.1.7)#view_list.html | view_list.html]], [[iHRIS Template List (4.1.7)#view_list_simple.html | view_list_simple.html]], [[iHRIS Template List (4.1.7)#view_list_simple_coded.html | view_list_simple_coded.html]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/sql modules/Forms/modules/Lists/sql] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules modules/Forms/modules/Lists/modules] <br/>[[#Lists-LinkTo |Lists-LinkTo]]
==Lists-LinkTo==
This describes version 4.1.0 of the module List Link to Data (Lists-LinkTo) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink  i2ce/modules/Forms/modules/Lists/modules/ListLink ]
*Description: Lists that are linked to other data. This module is meant to be extended to defined what type of data this list links to. You can extend the I2CE_ListLink class to add new fields to link to. Alone this class doesn't do much.
*Requirements:
**[[iHRIS Module List (4.1.7)#Lists | Lists]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/configs modules/Forms/modules/Lists/modules/ListLink/configs] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules modules/Forms/modules/Lists/modules/ListLink/modules] <br/>[[#Lists-LinkTo-List |Lists-LinkTo-List]], [[#Lists-LinkTo-String |Lists-LinkTo-String]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/ modules/Forms/modules/Lists/modules/ListLink/] 
==Lists-LinkTo-List==
This describes version 4.1.0 of the module List Link to List (Lists-LinkTo-List) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList  i2ce/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList ]
*Description: Lists that are linked to another list form. Multiple forms are defined here that can be used to link lists to other lists for different storage mechanisms. You must enable the required form storage module yourself to avoid extra modules being loaded. You should use the same form storage that is used for the List form you're linking. Certain storage mechanisms may need extra storage options defined.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage-CSV | forms-storage-CSV]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-flat | forms-storage-flat]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-magicdata | forms-storage-magicdata]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#Lists-LinkTo | Lists-LinkTo]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList/configs modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList/ modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToList/] 
==Lists-LinkTo-String==
This describes version 4.1.0 of the module List Link to String (Lists-LinkTo-String) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString  i2ce/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString ]
*Description: Lists that are linked to a string (id). Multiple forms are defined here that can be used to link lists to strings for different storage mechanisms. You must enable the required form storage module yourself to avoid extra modules being loaded. You should use the same form storage that is used for the List form you're linking. Certain storage mechanisms may need extra storage options defined.
*Requirements:
**[[iHRIS Module List (4.1.7)#Lists-LinkTo | Lists-LinkTo]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-CSV | forms-storage-CSV]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-flat | forms-storage-flat]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-magicdata | forms-storage-magicdata]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString/configs modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString/ modules/Forms/modules/Lists/modules/ListLink/modules/ListLinkToString/] 
==LocaleForm==
This describes version 4.1.0 of the module Locale Form (LocaleForm) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/LocaleForm  i2ce/modules/Forms/modules/LocaleForm ]
*Description: 
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-eval | forms-storage-eval]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/LocaleForm/configs modules/Forms/modules/LocaleForm/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/LocaleForm/ modules/Forms/modules/LocaleForm/] 
==LoginPage==
This describes version 4.1.6.0 of the module Login Page (LoginPage) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Login  i2ce/modules/Pages/modules/Login ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Login (4.1.7)| I2CE_Module_Login]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Wrangler (4.1.7)#manipulateWrangler_I2CE_logout() | I2CE_Wrangler->manipulateWrangler_I2CE_logout() ]] via [[Class: I2CE_Module_Login (4.1.7)#manipulateWrangler() | manipulateWrangler()]]
*Description: The login Page
*Requirements:
**[[iHRIS Module List (4.1.7)#Mailer | Mailer]] at least 1.2 and less than 1.3
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Login/configs modules/Pages/modules/Login/configs] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Login/css modules/Pages/modules/Login/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Login/lib modules/Pages/modules/Login/lib] <br/>[[Class: I2CE_Module_Login (4.1.7) | I2CE_Module_Login]], [[Class: I2CE_PageFeedback (4.1.7) | I2CE_PageFeedback]], [[Class: I2CE_PageForgot (4.1.7) | I2CE_PageForgot]], [[Class: I2CE_PageLogin (4.1.7) | I2CE_PageLogin]], [[Class: I2CE_PageLogout (4.1.7) | I2CE_PageLogout]], [[Class: I2CE_PagePassword (4.1.7) | I2CE_PagePassword]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Login/templates modules/Pages/modules/Login/templates] <br/>[[iHRIS Template List (4.1.7)#feedback.html | feedback.html]], [[iHRIS Template List (4.1.7)#feedback_form.html | feedback_form.html]], [[iHRIS Template List (4.1.7)#feedback_thanks.html | feedback_thanks.html]], [[iHRIS Template List (4.1.7)#forgot.html | forgot.html]], [[iHRIS Template List (4.1.7)#login.html | login.html]], [[iHRIS Template List (4.1.7)#password.html | password.html]], [[iHRIS Template List (4.1.7)#password_cant_change.html | password_cant_change.html]], [[iHRIS Template List (4.1.7)#password_form.html | password_form.html]], [[iHRIS Template List (4.1.7)#password_no_match.html | password_no_match.html]], [[iHRIS Template List (4.1.7)#password_none.html | password_none.html]], [[iHRIS Template List (4.1.7)#password_success.html | password_success.html]], [[iHRIS Template List (4.1.7)#password_wrong.html | password_wrong.html]]
==Mailer==
This describes version 1.2.0.1 of the module Mailer (Mailer) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Mail  i2ce/modules/Mail ]
*Description: Wrapper for PEAR Mail module
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Mail/lib modules/Mail/lib] <br/>[[Class: I2CE_Mailer (4.1.7) | I2CE_Mailer]]
==MimeTypes==
This describes version 4.1.6.0 of the module Mime Types (MimeTypes) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MimeTypes  i2ce/modules/MimeTypes ]
*Description: Adds a in mime type capabilities
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MimeTypes/configs modules/MimeTypes/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MimeTypes/lib modules/MimeTypes/lib] <br/>[[Class: I2CE_MimeTypes (4.1.7) | I2CE_MimeTypes]]
**Mime: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MimeTypes/mime modules/MimeTypes/mime] 
==MooTools==
This describes version 1.4.5 of the module MooTools (MooTools) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools  i2ce/modules/MooTools ]
*Description: MooTools javascript library
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/scripts modules/MooTools/scripts] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules modules/MooTools/modules] <br/>[[#ColorPicker |ColorPicker]], [[#DatePicker |DatePicker]], [[#FormWorm |FormWorm]], [[#MooTools-I2CE |MooTools-I2CE]], [[#StretchPage |StretchPage]], [[#TreeSelect |TreeSelect]], [[#fancyDebug |fancyDebug]], [[#menu_select |menu_select]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/ modules/MooTools/] <br/>[[Class: I2CE_MootoolsCore (4.1.7) | I2CE_MootoolsCore]], [[Class: I2CE_Module_Debugging (4.1.7) | I2CE_Module_Debugging]], [[Class: I2CE_Module_MenuSelect (4.1.7) | I2CE_Module_MenuSelect]], [[Class: I2CE_Module_StretchPage (4.1.7) | I2CE_Module_StretchPage]], [[Class: I2CE_Module_TreeSelect (4.1.7) | I2CE_Module_TreeSelect]], [[Class: I2CE_Page_TreeSelectData (4.1.7) | I2CE_Page_TreeSelectData]]
==MooTools-I2CE==
This describes version 4.1.6.0 of the module I2CE Library (MooTools-I2CE) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Core  i2ce/modules/MooTools/modules/Core ]
*Module Class: The module class is implemented by [[Class: I2CE_MootoolsCore (4.1.7)| I2CE_MootoolsCore]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#getClassValue() | I2CE_Page->getClassValue() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#getClassValue() | getClassValue()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#getClassValue() | I2CE_Template->getClassValue() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#getClassValue() | getClassValue()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#loadClassValues() | I2CE_Page->loadClassValues() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#loadClassValues() | loadClassValues()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#loadClassValues() | I2CE_Template->loadClassValues() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#loadClassValues() | loadClassValues()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setClassValue() | I2CE_Page->setClassValue() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#setClassValue() | setClassValue()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setClassValue() | I2CE_Template->setClassValue() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#setClassValue() | setClassValue()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setClassValues() | I2CE_Page->setClassValues() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#setClassValues() | setClassValues()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setClassValues() | I2CE_Template->setClassValues() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#setClassValues() | setClassValues()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#useDropDown() | I2CE_Page->useDropDown() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#useDropDown() | useDropDown()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#useDropDown() | I2CE_Template->useDropDown() ]] via [[Class: I2CE_MootoolsCore (4.1.7)#useDropDown() | useDropDown()]]
*Description: I2CE MooTools core library
*Requirements:
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Core/scripts modules/MooTools/modules/Core/scripts] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Core/css modules/MooTools/modules/Core/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Core/ modules/MooTools/modules/Core/] 
==Options==
This describes version 4.1.1.0 of the module I2CE Options Data (Options) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules/Options  i2ce/modules/TemplateData/modules/Options ]
*Module Class: The module class is implemented by [[Class: I2CE_Template_Options (4.1.7)| I2CE_Template_Options]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#addOption() | I2CE_Page->addOption() ]] via [[Class: I2CE_Template_Options (4.1.7)#addOption() | addOption()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addOption() | I2CE_Template->addOption() ]] via [[Class: I2CE_Template_Options (4.1.7)#addOption() | addOption()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addOptions() | I2CE_Page->addOptions() ]] via [[Class: I2CE_Template_Options (4.1.7)#addOptions() | addOptions()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addOptions() | I2CE_Template->addOptions() ]] via [[Class: I2CE_Template_Options (4.1.7)#addOptions() | addOptions()]]
*Description: Adds options data to the template
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#template-data | template-data]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules/Options/ modules/TemplateData/modules/Options/] <br/>[[Class: I2CE_Template_Options (4.1.7) | I2CE_Template_Options]]
==Percent==
This describes version 4.1.12.0 of the module Percent (Percent) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/modules/Percent  i2ce/modules/Forms/modules/Fields/modules/Percent ]
*Description: A module that allows the percent formfield
*Requirements:
**[[iHRIS Module List (4.1.7)#Fields | Fields]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/modules/Percent/lib modules/Forms/modules/Fields/modules/Percent/lib] <br/>[[Class: I2CE_FormField_PERCENT_INT (4.1.7) | I2CE_FormField_PERCENT_INT]]
==PrintedForms==
This describes version 4.1.2.0 of the module Printed Forms (PrintedForms) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms  i2ce/modules/Forms/modules/PrintedForms ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_PrintedForms (4.1.7)| I2CE_Module_PrintedForms]]
*Description: Engine used to generated standard printed forms from a form relationship
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#formRelationships | formRelationships]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#textlayout | textlayout]] at least 4.1 and less than 4.2
*Optionally Enables: [[iHRIS Module List (4.1.7)#BinField | BinField]]
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/configs modules/Forms/modules/PrintedForms/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/lib modules/Forms/modules/PrintedForms/lib] <br/>[[Class: I2CE_Module_PrintedForms (4.1.7) | I2CE_Module_PrintedForms]], [[Class: I2CE_Page_PrintedForms (4.1.7) | I2CE_Page_PrintedForms]], [[Class: I2CE_PrintedForm_Render (4.1.7) | I2CE_PrintedForm_Render]], [[Class: I2CE_PrintedForm_Render_PDF (4.1.7) | I2CE_PrintedForm_Render_PDF]]
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/images modules/Forms/modules/PrintedForms/images] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/templates modules/Forms/modules/PrintedForms/templates] <br/>[[iHRIS Template List (4.1.7)#printed_forms_menu.html | printed_forms_menu.html]], [[iHRIS Template List (4.1.7)#printed_forms_menu_archive_each.html | printed_forms_menu_archive_each.html]], [[iHRIS Template List (4.1.7)#printed_forms_menu_each.html | printed_forms_menu_each.html]]
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/modules modules/Forms/modules/PrintedForms/modules] <br/>[[#PrintedFormsODT |PrintedFormsODT]]
==PrintedFormsODT==
This describes version 4.1.7.0 of the module ODT Printed Forms (PrintedFormsODT) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/modules/PrintedFormODT  i2ce/modules/Forms/modules/PrintedForms/modules/PrintedFormODT ]
*Description: Provides Printed/Standardized Forms by ODT document templates
*Requirements:
**[[iHRIS Module List (4.1.7)#PrintedForms | PrintedForms]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/PrintedForms/modules/PrintedFormODT/lib modules/Forms/modules/PrintedForms/modules/PrintedFormODT/lib] <br/>[[Class: I2CE_GlobalSegment (4.1.7) | I2CE_GlobalSegment]], [[Class: I2CE_Odf (4.1.7) | I2CE_Odf]], [[Class: I2CE_PrintedForm_Render_ODT (4.1.7) | I2CE_PrintedForm_Render_ODT]], [[Class: I2CE_Segment (4.1.7) | I2CE_Segment]], [[Class: SegmentIterator (4.1.7) | SegmentIterator]], [[Class: PclZip (4.1.7) | PclZip]]
==ReferenceField==
This describes version 4.1.7.0 of the module Reference Field (ReferenceField) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/ReferenceField  i2ce/modules/Forms/modules/ReferenceField ]
*Description: A module that allows the REFERENCE formfield
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/ReferenceField/lib modules/Forms/modules/ReferenceField/lib] <br/>[[Class: I2CE_FormField_MULT_REFERENCE (4.1.7) | I2CE_FormField_MULT_REFERENCE]], [[Class: I2CE_FormField_REFERENCE (4.1.7) | I2CE_FormField_REFERENCE]]
==ReportArchiver==
This describes version 4.1.0 of the module Custom Reports Archiver (ReportArchiver) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/ReportArchiver  i2ce/modules/CustomReports/modules/ReportArchiver ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_ReportArchiver (4.1.7)| I2CE_Module_ReportArchiver]]
*Description: Custom Reports
*Requirements:
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#CustomReports_Export | CustomReports_Export]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#BinField | BinField]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/ReportArchiver/configs modules/CustomReports/modules/ReportArchiver/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/ReportArchiver/lib modules/CustomReports/modules/ReportArchiver/lib] <br/>[[Class: I2CE_Module_ReportArchiver (4.1.7) | I2CE_Module_ReportArchiver]], [[Class: I2CE_Page_ArchiveReport (4.1.7) | I2CE_Page_ArchiveReport]], [[Class: I2CE_Page_CustomReport_ArchiveMenu (4.1.7) | I2CE_Page_CustomReport_ArchiveMenu]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/CustomReports/modules/ReportArchiver/templates modules/CustomReports/modules/ReportArchiver/templates] <br/>[[iHRIS Template List (4.1.7)#archiveReports_menu.html | archiveReports_menu.html]], [[iHRIS Template List (4.1.7)#reportArchive_menu.html | reportArchive_menu.html]]
==RequestAccount-VerifyEmail==
This describes version 4.1.3.0 of the module User (RequestAccount-VerifyEmail) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/RequestAccountEmail  i2ce/modules/User/modules/RequestAccountEmail ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_UserRequest (4.1.7)| I2CE_Module_UserRequest]]
*Description: Provides Ability To Request Account
*Requirements:
**[[iHRIS Module List (4.1.7)#user | user]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-magicdata | forms-storage-magicdata]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#UserForm | UserForm]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#Mailer | Mailer]] at least 1.2 and less than 1.3
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/RequestAccountEmail/configs modules/User/modules/RequestAccountEmail/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/RequestAccountEmail/lib modules/User/modules/RequestAccountEmail/lib] <br/>[[Class: I2CE_Module_UserRequest (4.1.7) | I2CE_Module_UserRequest]], [[Class: I2CE_PageForm_UserRequestEmail (4.1.7) | I2CE_PageForm_UserRequestEmail]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/RequestAccountEmail/templates modules/User/modules/RequestAccountEmail/templates] <br/>[[iHRIS Template List (4.1.7)#button_request_account.html | button_request_account.html]], [[iHRIS Template List (4.1.7)#button_request_account_resend.html | button_request_account_resend.html]], [[iHRIS Template List (4.1.7)#resend_email.html | resend_email.html]]
==StretchPage==
This describes version 4.1.2.0 of the module Page Stretcher (StretchPage) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/StretchPage  i2ce/modules/MooTools/modules/StretchPage ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_StretchPage (4.1.7)| I2CE_Module_StretchPage]]
*Description: Makes sure that the page is at least as high as the browser window. Use bad adding a div with id='StretchPage' to the containing element that you want stretched.
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/StretchPage/lib modules/MooTools/modules/StretchPage/lib] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/StretchPage/scripts modules/MooTools/modules/StretchPage/scripts] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/StretchPage/css modules/MooTools/modules/StretchPage/css] 
==Tags==
This describes version 4.1.4.0 of the module Tags (Tags) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules/Tags  i2ce/modules/TemplateData/modules/Tags ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Tags (4.1.7)| I2CE_Module_Tags]]
*Description: Adds module and script tag processing to the template
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#template-data | template-data]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#DisplayData | DisplayData]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules/Tags/ modules/TemplateData/modules/Tags/] <br/>[[Class: I2CE_Module_Tags (4.1.7) | I2CE_Module_Tags]], [[Class: I2CE_PluralForms (4.1.7) | I2CE_PluralForms]]
==Timer==
This describes version 4.1.0 of the module I2CE Timer (Timer) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Timer  i2ce/modules/Timer ]
*Module Class: The module class is implemented by [[Class: I2CE_Timer (4.1.7)| I2CE_Timer]]
*Description: Adds a timer class
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Timer/configs modules/Timer/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Timer/ modules/Timer/] <br/>[[Class: I2CE_Timer (4.1.7) | I2CE_Timer]]
==TreeSelect==
This describes version 4.1.7.0 of the module Tree Select (TreeSelect) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/TreeSelect  i2ce/modules/MooTools/modules/TreeSelect ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_TreeSelect (4.1.7)| I2CE_Module_TreeSelect]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#addAutoCompleteInputTreeById() | I2CE_Page->addAutoCompleteInputTreeById() ]] via [[Class: I2CE_Module_TreeSelect (4.1.7)#addAutoCompleteInputTreeById() | addAutoCompleteInputTreeById()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAutoCompleteInputTreeById() | I2CE_Template->addAutoCompleteInputTreeById() ]] via [[Class: I2CE_Module_TreeSelect (4.1.7)#addAutoCompleteInputTreeById() | addAutoCompleteInputTreeById()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addAutoCompleteInputTree() | I2CE_Page->addAutoCompleteInputTree() ]] via [[Class: I2CE_Module_TreeSelect (4.1.7)#addAutoCompleteInputTree() | addAutoCompleteInputTree()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAutoCompleteInputTree() | I2CE_Template->addAutoCompleteInputTree() ]] via [[Class: I2CE_Module_TreeSelect (4.1.7)#addAutoCompleteInputTree() | addAutoCompleteInputTree()]]
*Description: Tree Select
*Requirements:
**[[iHRIS Module List (4.1.7)#MooTools-I2CE | MooTools-I2CE]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/TreeSelect/configs modules/MooTools/modules/TreeSelect/configs] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/TreeSelect/scripts modules/MooTools/modules/TreeSelect/scripts] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/TreeSelect/css modules/MooTools/modules/TreeSelect/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/TreeSelect/ modules/MooTools/modules/TreeSelect/] 
==UserAccess==
This describes version 4.1.4.0 of the module User (UserAccess) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess  i2ce/modules/User/modules/UserAccess ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_UserAccess (4.1.7)| I2CE_Module_UserAccess]]
*Description: Provides Deafult User Access Mechansim
*Requirements:
**[[iHRIS Module List (4.1.7)#user | user]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess/lib modules/User/modules/UserAccess/lib] <br/>[[Class: I2CE_Module_UserAccess (4.1.7) | I2CE_Module_UserAccess]], [[Class: I2CE_UserAccess (4.1.7) | I2CE_UserAccess]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess/sql modules/User/modules/UserAccess/sql] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess/templates modules/User/modules/UserAccess/templates] <br/>[[iHRIS Template List (4.1.7)#user_form.html | user_form.html]], [[iHRIS Template List (4.1.7)#user_form_edit.html | user_form_edit.html]], [[iHRIS Template List (4.1.7)#user_form_view.html | user_form_view.html]]
==UserAccess_DHIS==
This describes version 4.1.4.0 of the module User (UserAccess_DHIS) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_DHIS  i2ce/modules/User/modules/UserAccess_DHIS ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_UserAccess_DHIS (4.1.7)| I2CE_Module_UserAccess_DHIS]]
*Description: Provides DHIS User Access Mechansim
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_DHIS/lib modules/User/modules/UserAccess_DHIS/lib] <br/>[[Class: I2CE_Module_UserAccess_DHIS (4.1.7) | I2CE_Module_UserAccess_DHIS]], [[Class: I2CE_UserAccess_DHIS (4.1.7) | I2CE_UserAccess_DHIS]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_DHIS/sql modules/User/modules/UserAccess_DHIS/sql] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_DHIS/templates modules/User/modules/UserAccess_DHIS/templates] <br/>[[iHRIS Template List (4.1.7)#user_form_DHIS.html | user_form_DHIS.html]], [[iHRIS Template List (4.1.7)#user_form_edit_DHIS.html | user_form_edit_DHIS.html]], [[iHRIS Template List (4.1.7)#user_form_view_DHIS.html | user_form_view_DHIS.html]]
==UserAccess_LDAP==
This describes version 4.1.3.0 of the module User (UserAccess_LDAP) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_LDAP  i2ce/modules/User/modules/UserAccess_LDAP ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_UserAccess_LDAP (4.1.7)| I2CE_Module_UserAccess_LDAP]]
*Description: Provides LDAP User Access Mechansim
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_LDAP/lib modules/User/modules/UserAccess_LDAP/lib] <br/>[[Class: I2CE_Module_UserAccess_LDAP (4.1.7) | I2CE_Module_UserAccess_LDAP]], [[Class: I2CE_UserAccess_LDAP (4.1.7) | I2CE_UserAccess_LDAP]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_LDAP/templates modules/User/modules/UserAccess_LDAP/templates] <br/>[[iHRIS Template List (4.1.7)#user_form_edit_LDAP.html | user_form_edit_LDAP.html]], [[iHRIS Template List (4.1.7)#user_form_LDAP.html | user_form_LDAP.html]], [[iHRIS Template List (4.1.7)#user_form_view_LDAP.html | user_form_view_LDAP.html]]
==UserAccess_LDAP_Hybrid==
This describes version 4.1.2.0 of the module User (UserAccess_LDAP_Hybrid) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_LDAP_Hybrid  i2ce/modules/User/modules/UserAccess_LDAP_Hybrid ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_UserAccess_LDAP_Hybrid (4.1.7)| I2CE_Module_UserAccess_LDAP_Hybrid]]
*Description: Provides a hybrid database and LDAP User Access Mechansim
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_LDAP_Hybrid/lib modules/User/modules/UserAccess_LDAP_Hybrid/lib] <br/>[[Class: I2CE_Module_UserAccess_LDAP_Hybrid (4.1.7) | I2CE_Module_UserAccess_LDAP_Hybrid]], [[Class: I2CE_UserAccess_LDAP_DB (4.1.7) | I2CE_UserAccess_LDAP_DB]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_LDAP_Hybrid/templates modules/User/modules/UserAccess_LDAP_Hybrid/templates] <br/>[[iHRIS Template List (4.1.7)#user_form_edit_LDAP_DB.html | user_form_edit_LDAP_DB.html]], [[iHRIS Template List (4.1.7)#user_form_LDAP_DB.html | user_form_LDAP_DB.html]], [[iHRIS Template List (4.1.7)#user_form_view_LDAP_DB.html | user_form_view_LDAP_DB.html]]
==UserAccess_Single==
This describes version 4.1.1.0 of the module Single User Authentication (UserAccess_Single) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_SingleUser  i2ce/modules/User/modules/UserAccess_SingleUser ]
*Description: Provides Singele User Access Mechansim
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_SingleUser/lib modules/User/modules/UserAccess_SingleUser/lib] <br/>[[Class: I2CE_Module_UserAccess_Single (4.1.7) | I2CE_Module_UserAccess_Single]], [[Class: I2CE_UserAccess_Single (4.1.7) | I2CE_UserAccess_Single]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules/UserAccess_SingleUser/templates modules/User/modules/UserAccess_SingleUser/templates] <br/>[[iHRIS Template List (4.1.7)#user_form_edit_Single.html | user_form_edit_Single.html]], [[iHRIS Template List (4.1.7)#user_form_Single.html | user_form_Single.html]], [[iHRIS Template List (4.1.7)#user_form_view_Single.html | user_form_view_Single.html]]
==UserForm==
This describes version 4.1.7.0 of the module User Form (UserForm) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/UserForm  i2ce/modules/Forms/modules/UserForm ]
*Description: 
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#LocaleForm | LocaleForm]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/UserForm/configs modules/Forms/modules/UserForm/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/UserForm/lib modules/Forms/modules/UserForm/lib] <br/>[[Class: I2CE_FormStorage_userform (4.1.7) | I2CE_FormStorage_userform]], [[Class: I2CE_PageFormParentUser (4.1.7) | I2CE_PageFormParentUser]], [[Class: I2CE_PageFormUser (4.1.7) | I2CE_PageFormUser]], [[Class: I2CE_PageViewUser (4.1.7) | I2CE_PageViewUser]], [[Class: I2CE_User_Form (4.1.7) | I2CE_User_Form]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/UserForm/templates modules/Forms/modules/UserForm/templates] <br/>[[iHRIS Template List (4.1.7)#button_confirm_user.html | button_confirm_user.html]], [[iHRIS Template List (4.1.7)#user_form_base.html | user_form_base.html]], [[iHRIS Template List (4.1.7)#user_form_base_view.html | user_form_base_view.html]], [[iHRIS Template List (4.1.7)#user_list.html | user_list.html]]
==YAML_spyc==
This describes version 0.3.0 of the module YAML (YAML_spyc) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/YAML  i2ce/modules/YAML ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_YAML (4.1.7)| I2CE_Module_YAML]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Configurator (4.1.7)#loadConfigFile_YAML() | I2CE_Configurator->loadConfigFile_YAML() ]] via [[Class: I2CE_Module_YAML (4.1.7)#loadConfigFile_YAML() | loadConfigFile_YAML()]]
*Description: YAML parser provided by spyc.  Also enabled processing of .YAML config files
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/YAML/lib modules/YAML/lib] <br/>[[Class: I2CE_MagicDataTemplate_YAML (4.1.7) | I2CE_MagicDataTemplate_YAML]], [[Class: I2CE_Module_YAML (4.1.7) | I2CE_Module_YAML]], [[Class: Spyc (4.1.7) | Spyc]]
**Xml: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/YAML/xml modules/YAML/xml] 
==admin==
This describes version 4.1.7.0 of the module Modules Administation (admin) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin  i2ce/modules/Pages/modules/Admin ]
*Description: The I2CE module administration system
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
**[[iHRIS Module List (4.1.7)#FormWorm | FormWorm]] at least 4.1 and less than 4.2
*Optionally Enables: [[iHRIS Module List (4.1.7)#swissConfig | swissConfig]]
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/configs modules/Pages/modules/Admin/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/lib modules/Pages/modules/Admin/lib] <br/>[[Class: I2CE_PageAdmin (4.1.7) | I2CE_PageAdmin]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/templates modules/Pages/modules/Admin/templates] <br/>[[iHRIS Template List (4.1.7)#module_category.html | module_category.html]], [[iHRIS Template List (4.1.7)#module_menu.html | module_menu.html]], [[iHRIS Template List (4.1.7)#module_module.html | module_module.html]], [[iHRIS Template List (4.1.7)#module_sub_module.html | module_sub_module.html]], [[iHRIS Template List (4.1.7)#no_configuration.html | no_configuration.html]]
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules modules/Pages/modules/Admin/modules] <br/>[[#cron |cron]], [[#deleteRecord |deleteRecord]], [[#exportReport |exportReport]], [[#modulePrompter |modulePrompter]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/css modules/Pages/modules/Admin/css] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/scripts modules/Pages/modules/Admin/scripts] 
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/images modules/Pages/modules/Admin/images] 
==cron==
This describes version 4.1.7.0 of the module Cron Page (cron) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/Cron  i2ce/modules/Pages/modules/Admin/modules/Cron ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Cron (4.1.7)| I2CE_Module_Cron]]
*Description: The I2CE Cron page for running commands based on timing.
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#admin | admin]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/Cron/configs modules/Pages/modules/Admin/modules/Cron/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/Cron/lib modules/Pages/modules/Admin/modules/Cron/lib] <br/>[[Class: I2CE_Module_Cron (4.1.7) | I2CE_Module_Cron]], [[Class: I2CE_PageCron (4.1.7) | I2CE_PageCron]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/Cron/templates modules/Pages/modules/Admin/modules/Cron/templates] 
==default-locales==
This describes version 4.1.7.0 of the module Default Locales (default-locales) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/modules/DefaultLocales  i2ce/modules/Pages/modules/LocaleSelector/modules/DefaultLocales ]
*Description: Provides List of Defauly Locales that are reasonably translated
*Requirements:
**[[iHRIS Module List (4.1.7)#localeSelector | localeSelector]] at least 4.1.0.2 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/modules/DefaultLocales/ modules/Pages/modules/LocaleSelector/modules/DefaultLocales/] 
==deleteRecord==
This describes version 4.1.2.0 of the module Delete Records (deleteRecord) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/DeleteRecord  i2ce/modules/Pages/modules/Admin/modules/DeleteRecord ]
*Description: Delete Records
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#admin | admin]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/DeleteRecord/lib modules/Pages/modules/Admin/modules/DeleteRecord/lib] <br/>[[Class: I2CE_Page_DeleteRecord (4.1.7) | I2CE_Page_DeleteRecord]]
==exportReport==
This describes version 4.1.2.0 of the module Report Export (exportReport) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/exportReport  i2ce/modules/Pages/modules/Admin/modules/exportReport ]
*Description: Report Export
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#admin | admin]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#CustomReports | CustomReports]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#magicDataExport | magicDataExport]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/exportReport/lib modules/Pages/modules/Admin/modules/exportReport/lib] <br/>[[Class: I2CE_Page_ExportReport (4.1.7) | I2CE_Page_ExportReport]]
==fancyDebug==
This describes version 4.1.2.0 of the module Fancy Debugger (fancyDebug) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Debugger  i2ce/modules/MooTools/modules/Debugger ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Debugging (4.1.7)| I2CE_Module_Debugging]]
*Description: A fancy error displaying system
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Debugger/scripts modules/MooTools/modules/Debugger/scripts] 
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Debugger/images modules/MooTools/modules/Debugger/images] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Debugger/css modules/MooTools/modules/Debugger/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/Debugger/ modules/MooTools/modules/Debugger/] 
==field-limits==
This describes version 4.1.7.0 of the module Field Limits (field-limits) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FieldLimits  i2ce/modules/Forms/modules/FieldLimits ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_FieldLimits (4.1.7)| I2CE_Module_FieldLimits]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitStyles() | I2CE_FormField->getLimitStyles() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#getFieldLimitStyles() | getFieldLimitStyles()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit() | I2CE_FormField->generateLimit() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateFieldLimit() | generateFieldLimit()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#describeLimit() | I2CE_FormField->describeLimit() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#describeFieldLimit() | describeFieldLimit()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_null() | I2CE_FormField->generateLimit_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_null() | generateLimit_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_not_null() | I2CE_FormField->generateLimit_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_not_null() | generateLimit_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_null_not_null() | I2CE_FormField->generateLimit_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_not_null() | generateLimit_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#checkLimit_null() | I2CE_FormField->checkLimit_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_null() | checkLimit_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#checkLimit_not_null() | I2CE_FormField->checkLimit_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_not_null() | checkLimit_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#checkLimit_null_not_null() | I2CE_FormField->checkLimit_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_not_null() | checkLimit_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#checkLimitString_null() | I2CE_FormField->checkLimitString_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_null() | checkLimitString_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#checkLimitString_not_null() | I2CE_FormField->checkLimitString_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_not_null() | checkLimitString_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#checkLimitString_null_not_null() | I2CE_FormField->checkLimitString_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_null_not_null() | checkLimitString_null_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_null() | I2CE_FormField->getLimitMenu_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_null() | I2CE_FormField_DISPLAYFIELDSTYLE_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_not_null() | I2CE_FormField->getLimitMenu_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_not_null() | I2CE_FormField_DISPLAYFIELDSTYLE_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_null_not_null() | I2CE_FormField->getLimitMenu_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_null_not_null() | I2CE_FormField_DISPLAYFIELDSTYLE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_null() | I2CE_FormField->processLimitMenu_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_null() | I2CE_FormField_PROCESSFIELDSTYLE_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_not_null() | I2CE_FormField->processLimitMenu_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_not_null() | I2CE_FormField_PROCESSFIELDSTYLE_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_null_not_null() | I2CE_FormField->processLimitMenu_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_null_not_null() | I2CE_FormField_PROCESSFIELDSTYLE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#generateLimit_null() | I2CE_FormField_DB_DATE->generateLimit_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_DATE_null() | generateLimit_DB_DATE_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#generateLimit_not_null() | I2CE_FormField_DB_DATE->generateLimit_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_DATE_not_null() | generateLimit_DB_DATE_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#generateLimit_null_not_null() | I2CE_FormField_DB_DATE->generateLimit_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_DATE_null_not_null() | generateLimit_DB_DATE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimit_null() | I2CE_FormField_DB_DATE->checkLimit_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_DATE_null() | checkLimit_DB_DATE_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimit_not_null() | I2CE_FormField_DB_DATE->checkLimit_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_DATE_not_null() | checkLimit_DB_DATE_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimit_null_not_null() | I2CE_FormField_DB_DATE->checkLimit_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_DATE_null_not_null() | checkLimit_DB_DATE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimitString_null() | I2CE_FormField_DB_DATE->checkLimitString_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_DATE_null() | checkLimitString_DB_DATE_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimitString_not_null() | I2CE_FormField_DB_DATE->checkLimitString_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_DATE_not_null() | checkLimitString_DB_DATE_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimitString_null_not_null() | I2CE_FormField_DB_DATE->checkLimitString_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_DATE_null_not_null() | checkLimitString_DB_DATE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_max_parent() | I2CE_FormField->generateLimit_max_parent() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_max_parent() | generateLimit_max_parent()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_min_parent() | I2CE_FormField->generateLimit_min_parent() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_min_parent() | generateLimit_min_parent()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_max_parent_form() | I2CE_FormField->generateLimit_max_parent_form() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_max_parent_form() | generateLimit_max_parent_form()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#generateLimit_min_parent_form() | I2CE_FormField->generateLimit_min_parent_form() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_min_parent_form() | generateLimit_min_parent_form()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_max_parent() | I2CE_FormField->getLimitMenu_max_parent() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_max_parent() | I2CE_FormField_DISPLAYFIELDSTYLE_max_parent()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_min_parent() | I2CE_FormField->getLimitMenu_min_parent() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_min_parent() | I2CE_FormField_DISPLAYFIELDSTYLE_min_parent()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_max_parent_form() | I2CE_FormField->getLimitMenu_max_parent_form() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_max_parent_form() | I2CE_FormField_DISPLAYFIELDSTYLE_max_parent_form()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#getLimitMenu_min_parent_form() | I2CE_FormField->getLimitMenu_min_parent_form() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DISPLAYFIELDSTYLE_min_parent_form() | I2CE_FormField_DISPLAYFIELDSTYLE_min_parent_form()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_max_parent() | I2CE_FormField->processLimitMenu_max_parent() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_max_parent() | I2CE_FormField_PROCESSFIELDSTYLE_max_parent()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_min_parent() | I2CE_FormField->processLimitMenu_min_parent() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_min_parent() | I2CE_FormField_PROCESSFIELDSTYLE_min_parent()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_max_parent_form() | I2CE_FormField->processLimitMenu_max_parent_form() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_max_parent_form() | I2CE_FormField_PROCESSFIELDSTYLE_max_parent_form()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#processLimitMenu_min_parent_form() | I2CE_FormField->processLimitMenu_min_parent_form() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_PROCESSFIELDSTYLE_min_parent_form() | I2CE_FormField_PROCESSFIELDSTYLE_min_parent_form()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#generateLimit_truefalse() | I2CE_FormField_BOOL->generateLimit_truefalse() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_BOOL_truefalse() | generateLimit_BOOL_truefalse()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#generateLimit_true() | I2CE_FormField_BOOL->generateLimit_true() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_BOOL_true() | generateLimit_BOOL_true()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#generateLimit_false() | I2CE_FormField_BOOL->generateLimit_false() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_BOOL_false() | generateLimit_BOOL_false()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#generateLimit_yesno() | I2CE_FormField_YESNO->generateLimit_yesno() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_YESNO_yesno() | generateLimit_YESNO_yesno()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#generateLimit_yes() | I2CE_FormField_YESNO->generateLimit_yes() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_YESNO_yes() | generateLimit_YESNO_yes()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#generateLimit_no() | I2CE_FormField_YESNO->generateLimit_no() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_YESNO_no() | generateLimit_YESNO_no()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_in() | I2CE_FormField_DB_INT->generateLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_in() | generateLimit_DB_INT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_in() | I2CE_FormField_DB_FLOAT->generateLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_in() | generateLimit_DB_FLOAT_in()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#generateLimit_in() | I2CE_FormField_MAP_MULT->generateLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_MAP_MULT_in() | generateLimit_MAP_MULT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_in() | I2CE_FormField_DB_STRING->generateLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_in() | generateLimit_DB_STRING_in()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_in() | I2CE_FormField_DB_TEXT->generateLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_in() | generateLimit_DB_TEXT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#generateLimit_in() | I2CE_FormField_DB_DATE->generateLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_DATE_in() | generateLimit_DB_DATE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_equals() | I2CE_FormField_DB_INT->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_equals() | generateLimit_DB_INT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_equals() | I2CE_FormField_DB_FLOAT->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_equals() | generateLimit_DB_FLOAT_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#generateLimit_equals() | I2CE_FormField_MAP_MULT->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_MAP_MULT_equals() | generateLimit_MAP_MULT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_equals() | I2CE_FormField_DB_STRING->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_equals() | generateLimit_DB_STRING_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_equals() | I2CE_FormField_DB_TEXT->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_equals() | generateLimit_DB_TEXT_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP (4.1.7)#generateLimit_within() | I2CE_FormField_MAP->generateLimit_within() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_MAP_within() | generateLimit_MAP_within()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DB_INT->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_greaterthan() | generateLimit_DB_INT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DB_FLOAT->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_greaterthan() | generateLimit_DB_FLOAT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DB_STRING->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_greaterthan() | generateLimit_DB_STRING_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DB_TEXT->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_greaterthan() | generateLimit_DB_TEXT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DB_INT->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_lessthan() | generateLimit_DB_INT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DB_FLOAT->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_lessthan() | generateLimit_DB_FLOAT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DB_STRING->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_lessthan() | generateLimit_DB_STRING_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DB_TEXT->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_lessthan() | generateLimit_DB_TEXT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DB_INT->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_greaterthan_equals() | generateLimit_DB_INT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DB_FLOAT->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_greaterthan_equals() | generateLimit_DB_FLOAT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DB_STRING->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_greaterthan_equals() | generateLimit_DB_STRING_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DB_TEXT->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_greaterthan_equals() | generateLimit_DB_TEXT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DB_INT->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_lessthan_equals() | generateLimit_DB_INT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DB_FLOAT->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_lessthan_equals() | generateLimit_DB_FLOAT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DB_STRING->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_lessthan_equals() | generateLimit_DB_STRING_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DB_TEXT->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_lessthan_equals() | generateLimit_DB_TEXT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#generateLimit_between() | I2CE_FormField_DB_INT->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_INT_between() | generateLimit_DB_INT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#generateLimit_between() | I2CE_FormField_DB_FLOAT->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_FLOAT_between() | generateLimit_DB_FLOAT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_between() | I2CE_FormField_DB_STRING->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_between() | generateLimit_DB_STRING_between()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_between() | I2CE_FormField_DB_TEXT->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_between() | generateLimit_DB_TEXT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#generateLimit_greaterthan_now() | I2CE_FormField_DB_DATE->generateLimit_greaterthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_greaterthan_now() | generateLimit_greaterthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#generateLimit_lessthan_now() | I2CE_FormField_DB_DATE->generateLimit_lessthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_lessthan_now() | generateLimit_lessthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_like() | I2CE_FormField_DB_STRING->generateLimit_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_like() | generateLimit_DB_STRING_like()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_like() | I2CE_FormField_DB_TEXT->generateLimit_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_like() | generateLimit_DB_TEXT_like()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_lowerlike() | I2CE_FormField_DB_STRING->generateLimit_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_lowerlike() | generateLimit_DB_STRING_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_lowerlike() | I2CE_FormField_DB_TEXT->generateLimit_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_lowerlike() | generateLimit_DB_TEXT_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_lowerequals() | I2CE_FormField_DB_STRING->generateLimit_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_lowerequals() | generateLimit_DB_STRING_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_lowerequals() | I2CE_FormField_DB_TEXT->generateLimit_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_lowerequals() | generateLimit_DB_TEXT_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_contains() | I2CE_FormField_DB_STRING->generateLimit_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_contains() | generateLimit_DB_STRING_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_contains() | I2CE_FormField_DB_TEXT->generateLimit_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_contains() | generateLimit_DB_TEXT_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#generateLimit_startswith() | I2CE_FormField_DB_STRING->generateLimit_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_STRING_startswith() | generateLimit_DB_STRING_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#generateLimit_startswith() | I2CE_FormField_DB_TEXT->generateLimit_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#generateLimit_DB_TEXT_startswith() | generateLimit_DB_TEXT_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#getLimitMenu_null() | I2CE_FormField_DB_DATE->getLimitMenu_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_null() | I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#processLimitMenu_null() | I2CE_FormField_DB_DATE->processLimitMenu_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_null() | I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#getLimitMenu_not_null() | I2CE_FormField_DB_DATE->getLimitMenu_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_not_null() | I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#processLimitMenu_not_null() | I2CE_FormField_DB_DATE->processLimitMenu_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_not_null() | I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#getLimitMenu_null_not_null() | I2CE_FormField_DB_DATE->getLimitMenu_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_null_not_null() | I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#processLimitMenu_null_not_null() | I2CE_FormField_DB_DATE->processLimitMenu_null_not_null() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_null_not_null() | I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_null_not_null()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#checkLimit_truefalse() | I2CE_FormField_BOOL->checkLimit_truefalse() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_BOOL_truefalse() | checkLimit_BOOL_truefalse()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#checkLimitString_truefalse() | I2CE_FormField_BOOL->checkLimitString_truefalse() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_BOOL_truefalse() | checkLimitString_BOOL_truefalse()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#getLimitMenu_truefalse() | I2CE_FormField_BOOL->getLimitMenu_truefalse() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_BOOL_DISPLAYFIELDSTYLE_truefalse() | I2CE_FormField_BOOL_DISPLAYFIELDSTYLE_truefalse()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#processLimitMenu_truefalse() | I2CE_FormField_BOOL->processLimitMenu_truefalse() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_BOOL_PROCESSFIELDSTYLE_truefalse() | I2CE_FormField_BOOL_PROCESSFIELDSTYLE_truefalse()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#checkLimit_true() | I2CE_FormField_BOOL->checkLimit_true() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_BOOL_true() | checkLimit_BOOL_true()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#checkLimitString_true() | I2CE_FormField_BOOL->checkLimitString_true() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_BOOL_true() | checkLimitString_BOOL_true()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#getLimitMenu_true() | I2CE_FormField_BOOL->getLimitMenu_true() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_BOOL_DISPLAYFIELDSTYLE_true() | I2CE_FormField_BOOL_DISPLAYFIELDSTYLE_true()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#processLimitMenu_true() | I2CE_FormField_BOOL->processLimitMenu_true() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_BOOL_PROCESSFIELDSTYLE_true() | I2CE_FormField_BOOL_PROCESSFIELDSTYLE_true()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#checkLimit_false() | I2CE_FormField_BOOL->checkLimit_false() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_BOOL_false() | checkLimit_BOOL_false()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#checkLimitString_false() | I2CE_FormField_BOOL->checkLimitString_false() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_BOOL_false() | checkLimitString_BOOL_false()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#getLimitMenu_false() | I2CE_FormField_BOOL->getLimitMenu_false() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_BOOL_DISPLAYFIELDSTYLE_false() | I2CE_FormField_BOOL_DISPLAYFIELDSTYLE_false()]]
**Implements the method [[Class: I2CE_FormField_BOOL (4.1.7)#processLimitMenu_false() | I2CE_FormField_BOOL->processLimitMenu_false() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_BOOL_PROCESSFIELDSTYLE_false() | I2CE_FormField_BOOL_PROCESSFIELDSTYLE_false()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#checkLimit_yesno() | I2CE_FormField_YESNO->checkLimit_yesno() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_YESNO_yesno() | checkLimit_YESNO_yesno()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#checkLimitString_yesno() | I2CE_FormField_YESNO->checkLimitString_yesno() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_YESNO_yesno() | checkLimitString_YESNO_yesno()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#getLimitMenu_yesno() | I2CE_FormField_YESNO->getLimitMenu_yesno() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_YESNO_DISPLAYFIELDSTYLE_yesno() | I2CE_FormField_YESNO_DISPLAYFIELDSTYLE_yesno()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#processLimitMenu_yesno() | I2CE_FormField_YESNO->processLimitMenu_yesno() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_YESNO_PROCESSFIELDSTYLE_yesno() | I2CE_FormField_YESNO_PROCESSFIELDSTYLE_yesno()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#checkLimit_yes() | I2CE_FormField_YESNO->checkLimit_yes() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_YESNO_yes() | checkLimit_YESNO_yes()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#checkLimitString_yes() | I2CE_FormField_YESNO->checkLimitString_yes() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_YESNO_yes() | checkLimitString_YESNO_yes()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#getLimitMenu_yes() | I2CE_FormField_YESNO->getLimitMenu_yes() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_YESNO_DISPLAYFIELDSTYLE_yes() | I2CE_FormField_YESNO_DISPLAYFIELDSTYLE_yes()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#processLimitMenu_yes() | I2CE_FormField_YESNO->processLimitMenu_yes() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_YESNO_PROCESSFIELDSTYLE_yes() | I2CE_FormField_YESNO_PROCESSFIELDSTYLE_yes()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#checkLimit_no() | I2CE_FormField_YESNO->checkLimit_no() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_YESNO_no() | checkLimit_YESNO_no()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#checkLimitString_no() | I2CE_FormField_YESNO->checkLimitString_no() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_YESNO_no() | checkLimitString_YESNO_no()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#getLimitMenu_no() | I2CE_FormField_YESNO->getLimitMenu_no() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_YESNO_DISPLAYFIELDSTYLE_no() | I2CE_FormField_YESNO_DISPLAYFIELDSTYLE_no()]]
**Implements the method [[Class: I2CE_FormField_YESNO (4.1.7)#processLimitMenu_no() | I2CE_FormField_YESNO->processLimitMenu_no() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_YESNO_PROCESSFIELDSTYLE_no() | I2CE_FormField_YESNO_PROCESSFIELDSTYLE_no()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_in() | I2CE_FormField_DB_INT->checkLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_in() | checkLimit_DB_INT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_in() | I2CE_FormField_DB_INT->checkLimitString_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_in() | checkLimitString_DB_INT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_in() | I2CE_FormField_DB_INT->getLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_in() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_in() | I2CE_FormField_DB_INT->processLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_in() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_in() | I2CE_FormField_DB_FLOAT->checkLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_in() | checkLimit_DB_FLOAT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_in() | I2CE_FormField_DB_FLOAT->checkLimitString_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_in() | checkLimitString_DB_FLOAT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_in() | I2CE_FormField_DB_FLOAT->getLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_in() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_in() | I2CE_FormField_DB_FLOAT->processLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_in() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#checkLimit_in() | I2CE_FormField_MAP_MULT->checkLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_MAP_MULT_in() | checkLimit_MAP_MULT_in()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#checkLimitString_in() | I2CE_FormField_MAP_MULT->checkLimitString_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_MAP_MULT_in() | checkLimitString_MAP_MULT_in()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#getLimitMenu_in() | I2CE_FormField_MAP_MULT->getLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_MAP_MULT_DISPLAYFIELDSTYLE_in() | I2CE_FormField_MAP_MULT_DISPLAYFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#processLimitMenu_in() | I2CE_FormField_MAP_MULT->processLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_MAP_MULT_PROCESSFIELDSTYLE_in() | I2CE_FormField_MAP_MULT_PROCESSFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_in() | I2CE_FormField_DB_STRING->checkLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_in() | checkLimit_DB_STRING_in()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_in() | I2CE_FormField_DB_STRING->checkLimitString_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_in() | checkLimitString_DB_STRING_in()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_in() | I2CE_FormField_DB_STRING->getLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_in() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_in() | I2CE_FormField_DB_STRING->processLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_in() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_in() | I2CE_FormField_DB_TEXT->checkLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_in() | checkLimit_DB_TEXT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_in() | I2CE_FormField_DB_TEXT->checkLimitString_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_in() | checkLimitString_DB_TEXT_in()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_in() | I2CE_FormField_DB_TEXT->getLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_in() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_in() | I2CE_FormField_DB_TEXT->processLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_in() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimit_in() | I2CE_FormField_DB_DATE->checkLimit_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_DATE_in() | checkLimit_DB_DATE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimitString_in() | I2CE_FormField_DB_DATE->checkLimitString_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_DATE_in() | checkLimitString_DB_DATE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#getLimitMenu_in() | I2CE_FormField_DB_DATE->getLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_in() | I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#processLimitMenu_in() | I2CE_FormField_DB_DATE->processLimitMenu_in() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_in() | I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_in()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_equals() | I2CE_FormField_DB_INT->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_equals() | checkLimit_DB_INT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_equals() | I2CE_FormField_DB_INT->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_equals() | checkLimitString_DB_INT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DB_INT->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_equals() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DB_INT->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_equals() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_equals() | I2CE_FormField_DB_FLOAT->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_equals() | checkLimit_DB_FLOAT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_equals() | I2CE_FormField_DB_FLOAT->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_equals() | checkLimitString_DB_FLOAT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DB_FLOAT->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_equals() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DB_FLOAT->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_equals() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#checkLimit_equals() | I2CE_FormField_MAP_MULT->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_MAP_MULT_equals() | checkLimit_MAP_MULT_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#checkLimitString_equals() | I2CE_FormField_MAP_MULT->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_MAP_MULT_equals() | checkLimitString_MAP_MULT_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#getLimitMenu_equals() | I2CE_FormField_MAP_MULT->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_MAP_MULT_DISPLAYFIELDSTYLE_equals() | I2CE_FormField_MAP_MULT_DISPLAYFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP_MULT (4.1.7)#processLimitMenu_equals() | I2CE_FormField_MAP_MULT->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_MAP_MULT_PROCESSFIELDSTYLE_equals() | I2CE_FormField_MAP_MULT_PROCESSFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_equals() | I2CE_FormField_DB_STRING->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_equals() | checkLimit_DB_STRING_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_equals() | I2CE_FormField_DB_STRING->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_equals() | checkLimitString_DB_STRING_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DB_STRING->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_equals() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DB_STRING->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_equals() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_equals() | I2CE_FormField_DB_TEXT->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_equals() | checkLimit_DB_TEXT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_equals() | I2CE_FormField_DB_TEXT->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_equals() | checkLimitString_DB_TEXT_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DB_TEXT->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_equals() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DB_TEXT->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_equals() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_equals()]]
**Implements the method [[Class: I2CE_FormField_MAP (4.1.7)#checkLimit_within() | I2CE_FormField_MAP->checkLimit_within() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_MAP_within() | checkLimit_MAP_within()]]
**Implements the method [[Class: I2CE_FormField_MAP (4.1.7)#checkLimitString_within() | I2CE_FormField_MAP->checkLimitString_within() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_MAP_within() | checkLimitString_MAP_within()]]
**Implements the method [[Class: I2CE_FormField_MAP (4.1.7)#getLimitMenu_within() | I2CE_FormField_MAP->getLimitMenu_within() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_MAP_DISPLAYFIELDSTYLE_within() | I2CE_FormField_MAP_DISPLAYFIELDSTYLE_within()]]
**Implements the method [[Class: I2CE_FormField_MAP (4.1.7)#processLimitMenu_within() | I2CE_FormField_MAP->processLimitMenu_within() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_MAP_PROCESSFIELDSTYLE_within() | I2CE_FormField_MAP_PROCESSFIELDSTYLE_within()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DB_INT->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_greaterthan() | checkLimit_DB_INT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DB_INT->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_greaterthan() | checkLimitString_DB_INT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DB_INT->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_greaterthan() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DB_INT->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_greaterthan() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DB_FLOAT->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_greaterthan() | checkLimit_DB_FLOAT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DB_FLOAT->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_greaterthan() | checkLimitString_DB_FLOAT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DB_FLOAT->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_greaterthan() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DB_FLOAT->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_greaterthan() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DB_STRING->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_greaterthan() | checkLimit_DB_STRING_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DB_STRING->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_greaterthan() | checkLimitString_DB_STRING_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DB_STRING->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_greaterthan() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DB_STRING->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_greaterthan() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DB_TEXT->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_greaterthan() | checkLimit_DB_TEXT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DB_TEXT->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_greaterthan() | checkLimitString_DB_TEXT_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DB_TEXT->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_greaterthan() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DB_TEXT->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_greaterthan() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DB_INT->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_lessthan() | checkLimit_DB_INT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DB_INT->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_lessthan() | checkLimitString_DB_INT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DB_INT->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_lessthan() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DB_INT->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_lessthan() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DB_FLOAT->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_lessthan() | checkLimit_DB_FLOAT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DB_FLOAT->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_lessthan() | checkLimitString_DB_FLOAT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DB_FLOAT->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_lessthan() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DB_FLOAT->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_lessthan() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DB_STRING->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_lessthan() | checkLimit_DB_STRING_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DB_STRING->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_lessthan() | checkLimitString_DB_STRING_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DB_STRING->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lessthan() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DB_STRING->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lessthan() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DB_TEXT->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_lessthan() | checkLimit_DB_TEXT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DB_TEXT->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_lessthan() | checkLimitString_DB_TEXT_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DB_TEXT->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lessthan() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DB_TEXT->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lessthan() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DB_INT->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_greaterthan_equals() | checkLimit_DB_INT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DB_INT->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_greaterthan_equals() | checkLimitString_DB_INT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DB_INT->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DB_INT->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DB_FLOAT->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_greaterthan_equals() | checkLimit_DB_FLOAT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DB_FLOAT->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_greaterthan_equals() | checkLimitString_DB_FLOAT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DB_FLOAT->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DB_FLOAT->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DB_STRING->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_greaterthan_equals() | checkLimit_DB_STRING_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DB_STRING->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_greaterthan_equals() | checkLimitString_DB_STRING_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DB_STRING->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DB_STRING->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DB_TEXT->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_greaterthan_equals() | checkLimit_DB_TEXT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DB_TEXT->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_greaterthan_equals() | checkLimitString_DB_TEXT_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DB_TEXT->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DB_TEXT->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_greaterthan_equals() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DB_INT->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_lessthan_equals() | checkLimit_DB_INT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DB_INT->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_lessthan_equals() | checkLimitString_DB_INT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DB_INT->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DB_INT->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DB_FLOAT->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_lessthan_equals() | checkLimit_DB_FLOAT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DB_FLOAT->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_lessthan_equals() | checkLimitString_DB_FLOAT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DB_FLOAT->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DB_FLOAT->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DB_STRING->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_lessthan_equals() | checkLimit_DB_STRING_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DB_STRING->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_lessthan_equals() | checkLimitString_DB_STRING_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DB_STRING->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DB_STRING->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DB_TEXT->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_lessthan_equals() | checkLimit_DB_TEXT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DB_TEXT->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_lessthan_equals() | checkLimitString_DB_TEXT_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DB_TEXT->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DB_TEXT->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lessthan_equals() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimit_between() | I2CE_FormField_DB_INT->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_INT_between() | checkLimit_DB_INT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#checkLimitString_between() | I2CE_FormField_DB_INT->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_INT_between() | checkLimitString_DB_INT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#getLimitMenu_between() | I2CE_FormField_DB_INT->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_between() | I2CE_FormField_DB_INT_DISPLAYFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_INT (4.1.7)#processLimitMenu_between() | I2CE_FormField_DB_INT->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_between() | I2CE_FormField_DB_INT_PROCESSFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimit_between() | I2CE_FormField_DB_FLOAT->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_FLOAT_between() | checkLimit_DB_FLOAT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#checkLimitString_between() | I2CE_FormField_DB_FLOAT->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_FLOAT_between() | checkLimitString_DB_FLOAT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#getLimitMenu_between() | I2CE_FormField_DB_FLOAT->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_between() | I2CE_FormField_DB_FLOAT_DISPLAYFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_FLOAT (4.1.7)#processLimitMenu_between() | I2CE_FormField_DB_FLOAT->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_between() | I2CE_FormField_DB_FLOAT_PROCESSFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_between() | I2CE_FormField_DB_STRING->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_between() | checkLimit_DB_STRING_between()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_between() | I2CE_FormField_DB_STRING->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_between() | checkLimitString_DB_STRING_between()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_between() | I2CE_FormField_DB_STRING->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_between() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_between() | I2CE_FormField_DB_STRING->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_between() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_between() | I2CE_FormField_DB_TEXT->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_between() | checkLimit_DB_TEXT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_between() | I2CE_FormField_DB_TEXT->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_between() | checkLimitString_DB_TEXT_between()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_between() | I2CE_FormField_DB_TEXT->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_between() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_between() | I2CE_FormField_DB_TEXT->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_between() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_between()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimit_greaterthan_now() | I2CE_FormField_DB_DATE->checkLimit_greaterthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_DATE_greaterthan_now() | checkLimit_DB_DATE_greaterthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimitString_greaterthan_now() | I2CE_FormField_DB_DATE->checkLimitString_greaterthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_DATE_greaterthan_now() | checkLimitString_DB_DATE_greaterthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#getLimitMenu_greaterthan_now() | I2CE_FormField_DB_DATE->getLimitMenu_greaterthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_greaterthan_now() | I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_greaterthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#processLimitMenu_greaterthan_now() | I2CE_FormField_DB_DATE->processLimitMenu_greaterthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_greaterthan_now() | I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_greaterthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimit_lessthan_now() | I2CE_FormField_DB_DATE->checkLimit_lessthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_DATE_lessthan_now() | checkLimit_DB_DATE_lessthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#checkLimitString_lessthan_now() | I2CE_FormField_DB_DATE->checkLimitString_lessthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_DATE_lessthan_now() | checkLimitString_DB_DATE_lessthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#getLimitMenu_lessthan_now() | I2CE_FormField_DB_DATE->getLimitMenu_lessthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_lessthan_now() | I2CE_FormField_DB_DATE_DISPLAYFIELDSTYLE_lessthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_DATE (4.1.7)#processLimitMenu_lessthan_now() | I2CE_FormField_DB_DATE->processLimitMenu_lessthan_now() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_lessthan_now() | I2CE_FormField_DB_DATE_PROCESSFIELDSTYLE_lessthan_now()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_like() | I2CE_FormField_DB_STRING->checkLimit_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_like() | checkLimit_DB_STRING_like()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_like() | I2CE_FormField_DB_STRING->checkLimitString_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_like() | checkLimitString_DB_STRING_like()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_like() | I2CE_FormField_DB_STRING->getLimitMenu_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_like() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_like()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_like() | I2CE_FormField_DB_STRING->processLimitMenu_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_like() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_like()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_like() | I2CE_FormField_DB_TEXT->checkLimit_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_like() | checkLimit_DB_TEXT_like()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_like() | I2CE_FormField_DB_TEXT->checkLimitString_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_like() | checkLimitString_DB_TEXT_like()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_like() | I2CE_FormField_DB_TEXT->getLimitMenu_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_like() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_like()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_like() | I2CE_FormField_DB_TEXT->processLimitMenu_like() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_like() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_like()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_lowerlike() | I2CE_FormField_DB_STRING->checkLimit_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_lowerlike() | checkLimit_DB_STRING_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_lowerlike() | I2CE_FormField_DB_STRING->checkLimitString_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_lowerlike() | checkLimitString_DB_STRING_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_lowerlike() | I2CE_FormField_DB_STRING->getLimitMenu_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lowerlike() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_lowerlike() | I2CE_FormField_DB_STRING->processLimitMenu_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lowerlike() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_lowerlike() | I2CE_FormField_DB_TEXT->checkLimit_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_lowerlike() | checkLimit_DB_TEXT_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_lowerlike() | I2CE_FormField_DB_TEXT->checkLimitString_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_lowerlike() | checkLimitString_DB_TEXT_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_lowerlike() | I2CE_FormField_DB_TEXT->getLimitMenu_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lowerlike() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_lowerlike() | I2CE_FormField_DB_TEXT->processLimitMenu_lowerlike() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lowerlike() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lowerlike()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_lowerequals() | I2CE_FormField_DB_STRING->checkLimit_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_lowerequals() | checkLimit_DB_STRING_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_lowerequals() | I2CE_FormField_DB_STRING->checkLimitString_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_lowerequals() | checkLimitString_DB_STRING_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_lowerequals() | I2CE_FormField_DB_STRING->getLimitMenu_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lowerequals() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_lowerequals() | I2CE_FormField_DB_STRING->processLimitMenu_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lowerequals() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_lowerequals() | I2CE_FormField_DB_TEXT->checkLimit_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_lowerequals() | checkLimit_DB_TEXT_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_lowerequals() | I2CE_FormField_DB_TEXT->checkLimitString_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_lowerequals() | checkLimitString_DB_TEXT_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_lowerequals() | I2CE_FormField_DB_TEXT->getLimitMenu_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lowerequals() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_lowerequals() | I2CE_FormField_DB_TEXT->processLimitMenu_lowerequals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lowerequals() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_lowerequals()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_contains() | I2CE_FormField_DB_STRING->checkLimit_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_contains() | checkLimit_DB_STRING_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_contains() | I2CE_FormField_DB_STRING->checkLimitString_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_contains() | checkLimitString_DB_STRING_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_contains() | I2CE_FormField_DB_STRING->getLimitMenu_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_contains() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_contains() | I2CE_FormField_DB_STRING->processLimitMenu_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_contains() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_contains() | I2CE_FormField_DB_TEXT->checkLimit_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_contains() | checkLimit_DB_TEXT_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_contains() | I2CE_FormField_DB_TEXT->checkLimitString_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_contains() | checkLimitString_DB_TEXT_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_contains() | I2CE_FormField_DB_TEXT->getLimitMenu_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_contains() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_contains() | I2CE_FormField_DB_TEXT->processLimitMenu_contains() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_contains() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_contains()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimit_startswith() | I2CE_FormField_DB_STRING->checkLimit_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_STRING_startswith() | checkLimit_DB_STRING_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#checkLimitString_startswith() | I2CE_FormField_DB_STRING->checkLimitString_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_STRING_startswith() | checkLimitString_DB_STRING_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#getLimitMenu_startswith() | I2CE_FormField_DB_STRING->getLimitMenu_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_startswith() | I2CE_FormField_DB_STRING_DISPLAYFIELDSTYLE_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_STRING (4.1.7)#processLimitMenu_startswith() | I2CE_FormField_DB_STRING->processLimitMenu_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_startswith() | I2CE_FormField_DB_STRING_PROCESSFIELDSTYLE_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimit_startswith() | I2CE_FormField_DB_TEXT->checkLimit_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimit_DB_TEXT_startswith() | checkLimit_DB_TEXT_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#checkLimitString_startswith() | I2CE_FormField_DB_TEXT->checkLimitString_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#checkLimitString_DB_TEXT_startswith() | checkLimitString_DB_TEXT_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#getLimitMenu_startswith() | I2CE_FormField_DB_TEXT->getLimitMenu_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_startswith() | I2CE_FormField_DB_TEXT_DISPLAYFIELDSTYLE_startswith()]]
**Implements the method [[Class: I2CE_FormField_DB_TEXT (4.1.7)#processLimitMenu_startswith() | I2CE_FormField_DB_TEXT->processLimitMenu_startswith() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_startswith() | I2CE_FormField_DB_TEXT_PROCESSFIELDSTYLE_startswith()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#generateLimit_equals() | I2CE_FormField_DATE_YMD->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_YMD_equals() | DATE_generateLimit_DATE_YMD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimit_equals() | I2CE_FormField_DATE_YMD->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_equals() | DATE_checkLimit_DATE_YMD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimitString_equals() | I2CE_FormField_DATE_YMD->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_equals() | DATE_checkLimit_DATE_YMD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DATE_YMD->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_YMD_equals() | DATE_getLimitMenu_DATE_YMD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DATE_YMD->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_YMD_equals() | DATE_processLimitMenu_DATE_YMD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#generateLimit_equals() | I2CE_FormField_DATE_MD->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_MD_equals() | DATE_generateLimit_DATE_MD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimit_equals() | I2CE_FormField_DATE_MD->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_equals() | DATE_checkLimit_DATE_MD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimitString_equals() | I2CE_FormField_DATE_MD->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_equals() | DATE_checkLimit_DATE_MD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DATE_MD->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_MD_equals() | DATE_getLimitMenu_DATE_MD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DATE_MD->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_MD_equals() | DATE_processLimitMenu_DATE_MD_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#generateLimit_equals() | I2CE_FormField_DATE_Y->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_Y_equals() | DATE_generateLimit_DATE_Y_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimit_equals() | I2CE_FormField_DATE_Y->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_equals() | DATE_checkLimit_DATE_Y_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimitString_equals() | I2CE_FormField_DATE_Y->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_equals() | DATE_checkLimit_DATE_Y_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DATE_Y->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_Y_equals() | DATE_getLimitMenu_DATE_Y_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DATE_Y->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_Y_equals() | DATE_processLimitMenu_DATE_Y_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#generateLimit_equals() | I2CE_FormField_DATE_HMS->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_HMS_equals() | DATE_generateLimit_DATE_HMS_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimit_equals() | I2CE_FormField_DATE_HMS->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_equals() | DATE_checkLimit_DATE_HMS_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimitString_equals() | I2CE_FormField_DATE_HMS->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_equals() | DATE_checkLimit_DATE_HMS_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DATE_HMS->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_HMS_equals() | DATE_getLimitMenu_DATE_HMS_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DATE_HMS->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_HMS_equals() | DATE_processLimitMenu_DATE_HMS_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#generateLimit_equals() | I2CE_FormField_DATE_TIME->generateLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_TIME_equals() | DATE_generateLimit_DATE_TIME_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimit_equals() | I2CE_FormField_DATE_TIME->checkLimit_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_equals() | DATE_checkLimit_DATE_TIME_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimitString_equals() | I2CE_FormField_DATE_TIME->checkLimitString_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_equals() | DATE_checkLimit_DATE_TIME_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#getLimitMenu_equals() | I2CE_FormField_DATE_TIME->getLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_TIME_equals() | DATE_getLimitMenu_DATE_TIME_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#processLimitMenu_equals() | I2CE_FormField_DATE_TIME->processLimitMenu_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_TIME_equals() | DATE_processLimitMenu_DATE_TIME_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DATE_YMD->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_YMD_greaterthan() | DATE_generateLimit_DATE_YMD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DATE_YMD->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_greaterthan() | DATE_checkLimit_DATE_YMD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DATE_YMD->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_greaterthan() | DATE_checkLimit_DATE_YMD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DATE_YMD->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_YMD_greaterthan() | DATE_getLimitMenu_DATE_YMD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DATE_YMD->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_YMD_greaterthan() | DATE_processLimitMenu_DATE_YMD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DATE_MD->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_MD_greaterthan() | DATE_generateLimit_DATE_MD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DATE_MD->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_greaterthan() | DATE_checkLimit_DATE_MD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DATE_MD->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_greaterthan() | DATE_checkLimit_DATE_MD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DATE_MD->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_MD_greaterthan() | DATE_getLimitMenu_DATE_MD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DATE_MD->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_MD_greaterthan() | DATE_processLimitMenu_DATE_MD_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DATE_Y->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_Y_greaterthan() | DATE_generateLimit_DATE_Y_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DATE_Y->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_greaterthan() | DATE_checkLimit_DATE_Y_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DATE_Y->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_greaterthan() | DATE_checkLimit_DATE_Y_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DATE_Y->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_Y_greaterthan() | DATE_getLimitMenu_DATE_Y_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DATE_Y->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_Y_greaterthan() | DATE_processLimitMenu_DATE_Y_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DATE_HMS->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_HMS_greaterthan() | DATE_generateLimit_DATE_HMS_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DATE_HMS->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_greaterthan() | DATE_checkLimit_DATE_HMS_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DATE_HMS->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_greaterthan() | DATE_checkLimit_DATE_HMS_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DATE_HMS->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_HMS_greaterthan() | DATE_getLimitMenu_DATE_HMS_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DATE_HMS->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_HMS_greaterthan() | DATE_processLimitMenu_DATE_HMS_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#generateLimit_greaterthan() | I2CE_FormField_DATE_TIME->generateLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_TIME_greaterthan() | DATE_generateLimit_DATE_TIME_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimit_greaterthan() | I2CE_FormField_DATE_TIME->checkLimit_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_greaterthan() | DATE_checkLimit_DATE_TIME_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimitString_greaterthan() | I2CE_FormField_DATE_TIME->checkLimitString_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_greaterthan() | DATE_checkLimit_DATE_TIME_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#getLimitMenu_greaterthan() | I2CE_FormField_DATE_TIME->getLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_TIME_greaterthan() | DATE_getLimitMenu_DATE_TIME_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#processLimitMenu_greaterthan() | I2CE_FormField_DATE_TIME->processLimitMenu_greaterthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_TIME_greaterthan() | DATE_processLimitMenu_DATE_TIME_greaterthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DATE_YMD->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_YMD_lessthan() | DATE_generateLimit_DATE_YMD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DATE_YMD->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_lessthan() | DATE_checkLimit_DATE_YMD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DATE_YMD->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_lessthan() | DATE_checkLimit_DATE_YMD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DATE_YMD->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_YMD_lessthan() | DATE_getLimitMenu_DATE_YMD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DATE_YMD->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_YMD_lessthan() | DATE_processLimitMenu_DATE_YMD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DATE_MD->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_MD_lessthan() | DATE_generateLimit_DATE_MD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DATE_MD->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_lessthan() | DATE_checkLimit_DATE_MD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DATE_MD->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_lessthan() | DATE_checkLimit_DATE_MD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DATE_MD->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_MD_lessthan() | DATE_getLimitMenu_DATE_MD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DATE_MD->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_MD_lessthan() | DATE_processLimitMenu_DATE_MD_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DATE_Y->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_Y_lessthan() | DATE_generateLimit_DATE_Y_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DATE_Y->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_lessthan() | DATE_checkLimit_DATE_Y_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DATE_Y->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_lessthan() | DATE_checkLimit_DATE_Y_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DATE_Y->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_Y_lessthan() | DATE_getLimitMenu_DATE_Y_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DATE_Y->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_Y_lessthan() | DATE_processLimitMenu_DATE_Y_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DATE_HMS->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_HMS_lessthan() | DATE_generateLimit_DATE_HMS_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DATE_HMS->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_lessthan() | DATE_checkLimit_DATE_HMS_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DATE_HMS->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_lessthan() | DATE_checkLimit_DATE_HMS_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DATE_HMS->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_HMS_lessthan() | DATE_getLimitMenu_DATE_HMS_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DATE_HMS->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_HMS_lessthan() | DATE_processLimitMenu_DATE_HMS_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#generateLimit_lessthan() | I2CE_FormField_DATE_TIME->generateLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_TIME_lessthan() | DATE_generateLimit_DATE_TIME_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimit_lessthan() | I2CE_FormField_DATE_TIME->checkLimit_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_lessthan() | DATE_checkLimit_DATE_TIME_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimitString_lessthan() | I2CE_FormField_DATE_TIME->checkLimitString_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_lessthan() | DATE_checkLimit_DATE_TIME_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#getLimitMenu_lessthan() | I2CE_FormField_DATE_TIME->getLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_TIME_lessthan() | DATE_getLimitMenu_DATE_TIME_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#processLimitMenu_lessthan() | I2CE_FormField_DATE_TIME->processLimitMenu_lessthan() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_TIME_lessthan() | DATE_processLimitMenu_DATE_TIME_lessthan()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DATE_YMD->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_YMD_greaterthan_equals() | DATE_generateLimit_DATE_YMD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DATE_YMD->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_greaterthan_equals() | DATE_checkLimit_DATE_YMD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DATE_YMD->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_greaterthan_equals() | DATE_checkLimit_DATE_YMD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_YMD->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_YMD_greaterthan_equals() | DATE_getLimitMenu_DATE_YMD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_YMD->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_YMD_greaterthan_equals() | DATE_processLimitMenu_DATE_YMD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DATE_MD->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_MD_greaterthan_equals() | DATE_generateLimit_DATE_MD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DATE_MD->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_greaterthan_equals() | DATE_checkLimit_DATE_MD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DATE_MD->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_greaterthan_equals() | DATE_checkLimit_DATE_MD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_MD->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_MD_greaterthan_equals() | DATE_getLimitMenu_DATE_MD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_MD->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_MD_greaterthan_equals() | DATE_processLimitMenu_DATE_MD_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DATE_Y->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_Y_greaterthan_equals() | DATE_generateLimit_DATE_Y_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DATE_Y->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_greaterthan_equals() | DATE_checkLimit_DATE_Y_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DATE_Y->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_greaterthan_equals() | DATE_checkLimit_DATE_Y_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_Y->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_Y_greaterthan_equals() | DATE_getLimitMenu_DATE_Y_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_Y->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_Y_greaterthan_equals() | DATE_processLimitMenu_DATE_Y_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DATE_HMS->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_HMS_greaterthan_equals() | DATE_generateLimit_DATE_HMS_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DATE_HMS->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_greaterthan_equals() | DATE_checkLimit_DATE_HMS_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DATE_HMS->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_greaterthan_equals() | DATE_checkLimit_DATE_HMS_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_HMS->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_HMS_greaterthan_equals() | DATE_getLimitMenu_DATE_HMS_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_HMS->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_HMS_greaterthan_equals() | DATE_processLimitMenu_DATE_HMS_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#generateLimit_greaterthan_equals() | I2CE_FormField_DATE_TIME->generateLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_TIME_greaterthan_equals() | DATE_generateLimit_DATE_TIME_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimit_greaterthan_equals() | I2CE_FormField_DATE_TIME->checkLimit_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_greaterthan_equals() | DATE_checkLimit_DATE_TIME_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimitString_greaterthan_equals() | I2CE_FormField_DATE_TIME->checkLimitString_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_greaterthan_equals() | DATE_checkLimit_DATE_TIME_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#getLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_TIME->getLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_TIME_greaterthan_equals() | DATE_getLimitMenu_DATE_TIME_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#processLimitMenu_greaterthan_equals() | I2CE_FormField_DATE_TIME->processLimitMenu_greaterthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_TIME_greaterthan_equals() | DATE_processLimitMenu_DATE_TIME_greaterthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DATE_YMD->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_YMD_lessthan_equals() | DATE_generateLimit_DATE_YMD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DATE_YMD->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_lessthan_equals() | DATE_checkLimit_DATE_YMD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DATE_YMD->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_lessthan_equals() | DATE_checkLimit_DATE_YMD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DATE_YMD->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_YMD_lessthan_equals() | DATE_getLimitMenu_DATE_YMD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DATE_YMD->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_YMD_lessthan_equals() | DATE_processLimitMenu_DATE_YMD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DATE_MD->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_MD_lessthan_equals() | DATE_generateLimit_DATE_MD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DATE_MD->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_lessthan_equals() | DATE_checkLimit_DATE_MD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DATE_MD->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_lessthan_equals() | DATE_checkLimit_DATE_MD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DATE_MD->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_MD_lessthan_equals() | DATE_getLimitMenu_DATE_MD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DATE_MD->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_MD_lessthan_equals() | DATE_processLimitMenu_DATE_MD_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DATE_Y->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_Y_lessthan_equals() | DATE_generateLimit_DATE_Y_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DATE_Y->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_lessthan_equals() | DATE_checkLimit_DATE_Y_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DATE_Y->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_lessthan_equals() | DATE_checkLimit_DATE_Y_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DATE_Y->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_Y_lessthan_equals() | DATE_getLimitMenu_DATE_Y_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DATE_Y->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_Y_lessthan_equals() | DATE_processLimitMenu_DATE_Y_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DATE_HMS->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_HMS_lessthan_equals() | DATE_generateLimit_DATE_HMS_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DATE_HMS->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_lessthan_equals() | DATE_checkLimit_DATE_HMS_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DATE_HMS->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_lessthan_equals() | DATE_checkLimit_DATE_HMS_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DATE_HMS->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_HMS_lessthan_equals() | DATE_getLimitMenu_DATE_HMS_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DATE_HMS->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_HMS_lessthan_equals() | DATE_processLimitMenu_DATE_HMS_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#generateLimit_lessthan_equals() | I2CE_FormField_DATE_TIME->generateLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_TIME_lessthan_equals() | DATE_generateLimit_DATE_TIME_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimit_lessthan_equals() | I2CE_FormField_DATE_TIME->checkLimit_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_lessthan_equals() | DATE_checkLimit_DATE_TIME_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimitString_lessthan_equals() | I2CE_FormField_DATE_TIME->checkLimitString_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_lessthan_equals() | DATE_checkLimit_DATE_TIME_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#getLimitMenu_lessthan_equals() | I2CE_FormField_DATE_TIME->getLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_TIME_lessthan_equals() | DATE_getLimitMenu_DATE_TIME_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#processLimitMenu_lessthan_equals() | I2CE_FormField_DATE_TIME->processLimitMenu_lessthan_equals() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_TIME_lessthan_equals() | DATE_processLimitMenu_DATE_TIME_lessthan_equals()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#getLimitMenu_between() | I2CE_FormField_DATE_YMD->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_YMD_between() | DATE_getLimitMenu_DATE_YMD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#generateLimit_between() | I2CE_FormField_DATE_YMD->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_YMD_between() | DATE_generateLimit_DATE_YMD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimit_between() | I2CE_FormField_DATE_YMD->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_YMD_between() | DATE_checkLimit_DATE_YMD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#checkLimitString_between() | I2CE_FormField_DATE_YMD->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimitString_DATE_YMD_between() | DATE_checkLimitString_DATE_YMD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_YMD (4.1.7)#processLimitMenu_between() | I2CE_FormField_DATE_YMD->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_YMD_between() | DATE_processLimitMenu_DATE_YMD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#getLimitMenu_between() | I2CE_FormField_DATE_MD->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_MD_between() | DATE_getLimitMenu_DATE_MD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#generateLimit_between() | I2CE_FormField_DATE_MD->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_MD_between() | DATE_generateLimit_DATE_MD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimit_between() | I2CE_FormField_DATE_MD->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_MD_between() | DATE_checkLimit_DATE_MD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#checkLimitString_between() | I2CE_FormField_DATE_MD->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimitString_DATE_MD_between() | DATE_checkLimitString_DATE_MD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_MD (4.1.7)#processLimitMenu_between() | I2CE_FormField_DATE_MD->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_MD_between() | DATE_processLimitMenu_DATE_MD_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#getLimitMenu_between() | I2CE_FormField_DATE_Y->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_Y_between() | DATE_getLimitMenu_DATE_Y_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#generateLimit_between() | I2CE_FormField_DATE_Y->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_Y_between() | DATE_generateLimit_DATE_Y_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimit_between() | I2CE_FormField_DATE_Y->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_Y_between() | DATE_checkLimit_DATE_Y_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#checkLimitString_between() | I2CE_FormField_DATE_Y->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimitString_DATE_Y_between() | DATE_checkLimitString_DATE_Y_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_Y (4.1.7)#processLimitMenu_between() | I2CE_FormField_DATE_Y->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_Y_between() | DATE_processLimitMenu_DATE_Y_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#getLimitMenu_between() | I2CE_FormField_DATE_HMS->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_HMS_between() | DATE_getLimitMenu_DATE_HMS_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#generateLimit_between() | I2CE_FormField_DATE_HMS->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_HMS_between() | DATE_generateLimit_DATE_HMS_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimit_between() | I2CE_FormField_DATE_HMS->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_HMS_between() | DATE_checkLimit_DATE_HMS_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#checkLimitString_between() | I2CE_FormField_DATE_HMS->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimitString_DATE_HMS_between() | DATE_checkLimitString_DATE_HMS_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_HMS (4.1.7)#processLimitMenu_between() | I2CE_FormField_DATE_HMS->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_HMS_between() | DATE_processLimitMenu_DATE_HMS_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#getLimitMenu_between() | I2CE_FormField_DATE_TIME->getLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_getLimitMenu_DATE_TIME_between() | DATE_getLimitMenu_DATE_TIME_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#generateLimit_between() | I2CE_FormField_DATE_TIME->generateLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_generateLimit_DATE_TIME_between() | DATE_generateLimit_DATE_TIME_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimit_between() | I2CE_FormField_DATE_TIME->checkLimit_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimit_DATE_TIME_between() | DATE_checkLimit_DATE_TIME_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#checkLimitString_between() | I2CE_FormField_DATE_TIME->checkLimitString_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_checkLimitString_DATE_TIME_between() | DATE_checkLimitString_DATE_TIME_between()]]
**Implements the method [[Class: I2CE_FormField_DATE_TIME (4.1.7)#processLimitMenu_between() | I2CE_FormField_DATE_TIME->processLimitMenu_between() ]] via [[Class: I2CE_Module_FieldLimits (4.1.7)#DATE_processLimitMenu_DATE_TIME_between() | DATE_processLimitMenu_DATE_TIME_between()]]
*Description: A module that enables limits for fields.
*Requirements:
**[[iHRIS Module List (4.1.7)#Fields | Fields]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FieldLimits/configs modules/Forms/modules/FieldLimits/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FieldLimits/lib modules/Forms/modules/FieldLimits/lib] <br/>[[Class: I2CE_Module_FieldLimits (4.1.7) | I2CE_Module_FieldLimits]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FieldLimits/templates modules/Forms/modules/FieldLimits/templates] <br/>[[iHRIS Template List (4.1.7)#limit_choice_between.html | limit_choice_between.html]], [[iHRIS Template List (4.1.7)#limit_choice_contains.html | limit_choice_contains.html]], [[iHRIS Template List (4.1.7)#limit_choice_equals.html | limit_choice_equals.html]], [[iHRIS Template List (4.1.7)#limit_choice_false.html | limit_choice_false.html]], [[iHRIS Template List (4.1.7)#limit_choice_greaterthan.html | limit_choice_greaterthan.html]], [[iHRIS Template List (4.1.7)#limit_choice_greaterthan_equals.html | limit_choice_greaterthan_equals.html]], [[iHRIS Template List (4.1.7)#limit_choice_greaterthan_now.html | limit_choice_greaterthan_now.html]], [[iHRIS Template List (4.1.7)#limit_choice_in.html | limit_choice_in.html]], [[iHRIS Template List (4.1.7)#limit_choice_lessthan.html | limit_choice_lessthan.html]], [[iHRIS Template List (4.1.7)#limit_choice_lessthan_equals.html | limit_choice_lessthan_equals.html]], [[iHRIS Template List (4.1.7)#limit_choice_lessthan_now.html | limit_choice_lessthan_now.html]], [[iHRIS Template List (4.1.7)#limit_choice_like.html | limit_choice_like.html]], [[iHRIS Template List (4.1.7)#limit_choice_lowerequals.html | limit_choice_lowerequals.html]], [[iHRIS Template List (4.1.7)#limit_choice_lowerlike.html | limit_choice_lowerlike.html]], [[iHRIS Template List (4.1.7)#limit_choice_max_parent.html | limit_choice_max_parent.html]], [[iHRIS Template List (4.1.7)#limit_choice_max_parent_form.html | limit_choice_max_parent_form.html]], [[iHRIS Template List (4.1.7)#limit_choice_min_parent.html | limit_choice_min_parent.html]], [[iHRIS Template List (4.1.7)#limit_choice_min_parent_form.html | limit_choice_min_parent_form.html]], [[iHRIS Template List (4.1.7)#limit_choice_no.html | limit_choice_no.html]], [[iHRIS Template List (4.1.7)#limit_choice_not_null.html | limit_choice_not_null.html]], [[iHRIS Template List (4.1.7)#limit_choice_null.html | limit_choice_null.html]], [[iHRIS Template List (4.1.7)#limit_choice_null_not_null.html | limit_choice_null_not_null.html]], [[iHRIS Template List (4.1.7)#limit_choice_startswith.html | limit_choice_startswith.html]], [[iHRIS Template List (4.1.7)#limit_choice_true.html | limit_choice_true.html]], [[iHRIS Template List (4.1.7)#limit_choice_truefalse.html | limit_choice_truefalse.html]], [[iHRIS Template List (4.1.7)#limit_choice_yes.html | limit_choice_yes.html]], [[iHRIS Template List (4.1.7)#limit_choice_yesno.html | limit_choice_yesno.html]], [[iHRIS Template List (4.1.7)#limit_date_choice.html | limit_date_choice.html]], [[iHRIS Template List (4.1.7)#limit_date_choice_between.html | limit_date_choice_between.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_between.html | limit_mapped_choice_between.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_equals.html | limit_mapped_choice_equals.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_greaterthan.html | limit_mapped_choice_greaterthan.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_greaterthan_equals.html | limit_mapped_choice_greaterthan_equals.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_in.html | limit_mapped_choice_in.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_lessthan.html | limit_mapped_choice_lessthan.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_lessthan_equals.html | limit_mapped_choice_lessthan_equals.html]], [[iHRIS Template List (4.1.7)#limit_mapped_choice_within.html | limit_mapped_choice_within.html]]
==fields-enum==
This describes version 4.1.7.0 of the module Enumeration (fields-enum) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/modules/Enum  i2ce/modules/Forms/modules/Fields/modules/Enum ]
*Description: A module that allows the enum formfield
*Requirements:
**[[iHRIS Module List (4.1.7)#Fields | Fields]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/Fields/modules/Enum/lib modules/Forms/modules/Fields/modules/Enum/lib] <br/>[[Class: I2CE_FormField_ENUM (4.1.7) | I2CE_FormField_ENUM]]
==form-limits==
This describes version 4.1.2.0 of the module Form Limits (form-limits) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormLimits  i2ce/modules/Forms/modules/FormLimits ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_FormLimits (4.1.7)| I2CE_Module_FormLimits]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Form (4.1.7)#getLimitStyles() | I2CE_Form->getLimitStyles() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#getLimitStyles() | getLimitStyles()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#checkLimit() | I2CE_Form->checkLimit() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#checkLimit() | checkLimit()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#checkWhereClause() | I2CE_Form->checkWhereClause() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#checkWhereClause() | checkWhereClause()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#createCheckFunction() | I2CE_Form->createCheckFunction() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#createCheckFunction() | createCheckFunction()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#createCheckLimitString() | I2CE_Form->createCheckLimitString() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#createCheckLimitString() | createCheckLimitString()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#generateLimit() | I2CE_Form->generateLimit() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#generateLimit() | generateLimit()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#generateWhereClause() | I2CE_Form->generateWhereClause() ]] via [[Class: I2CE_Module_FormLimits (4.1.7)#generateWhereClause() | generateWhereClause()]]
*Description: A module that enables limits for forms.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#field-limits | field-limits]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormLimits/lib modules/Forms/modules/FormLimits/lib] <br/>[[Class: I2CE_Module_FormLimits (4.1.7) | I2CE_Module_FormLimits]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormLimits/templates modules/Forms/modules/FormLimits/templates] 
==form-relationship-based-permission==
This describes version 4.1.0 of the module Form Relationship Based Permission (form-relationship-based-permission) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationshipBasedPermission  i2ce/modules/Forms/modules/FormRelationshipBasedPermission ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_FormRelationshipBasedPermissions (4.1.7)| I2CE_Module_FormRelationshipBasedPermissions]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_PermissionParser (4.1.7)#hasPermission_satisfies() | I2CE_PermissionParser->hasPermission_satisfies() ]] via [[Class: I2CE_Module_FormRelationshipBasedPermissions (4.1.7)#hasPermission_satisfies() | hasPermission_satisfies()]]
*Description: A module that enables permission for based on form relationships
*Requirements:
**[[iHRIS Module List (4.1.7)#formRelationships | formRelationships]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationshipBasedPermission/lib modules/Forms/modules/FormRelationshipBasedPermission/lib] <br/>[[Class: I2CE_Module_FormRelationshipBasedPermissions (4.1.7) | I2CE_Module_FormRelationshipBasedPermissions]]
==form-task-log==
This describes version 4.1.4.0 of the module Form Task Logger (form-task-log) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageTaskLog  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageTaskLog ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)| I2CE_Module_TaskLog_FormStorage]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#setTask() | I2CE_FormFactory->setTask() ]] via [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)#setTask() | setTask()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#setTaskID() | I2CE_FormFactory->setTaskID() ]] via [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)#setTaskID() | setTaskID()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#getTask() | I2CE_FormFactory->getTask() ]] via [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)#getTask() | getTask()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#getTaskID() | I2CE_FormFactory->getTaskID() ]] via [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)#getTaskID() | getTaskID()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#pauseTaskLog() | I2CE_FormFactory->pauseTaskLog() ]] via [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)#pauseTaskLog() | pauseTaskLog()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#resumeTaskLog() | I2CE_FormFactory->resumeTaskLog() ]] via [[Class: I2CE_Module_TaskLog_FormStorage (4.1.7)#resumeTaskLog() | resumeTaskLog()]]
*Description: A module that enables logging of data changes related to tasks
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageTaskLog/lib modules/Forms/modules/FormStorage/modules/FormStorageTaskLog/lib] <br/>[[Class: I2CE_Module_TaskLog_FormStorage (4.1.7) | I2CE_Module_TaskLog_FormStorage]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageTaskLog/sql modules/Forms/modules/FormStorage/modules/FormStorageTaskLog/sql] 
==formBrowser==
This describes version 4.1.7.0 of the module Form Browser (formBrowser) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormBrowser  i2ce/modules/Forms/modules/FormBrowser ]
*Description: Enables Browsing of Forms
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormBrowser/configs modules/Forms/modules/FormBrowser/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormBrowser/lib modules/Forms/modules/FormBrowser/lib] <br/>[[Class: I2CE_FormBrowser (4.1.7) | I2CE_FormBrowser]], [[Class: I2CE_PageFormBrowser (4.1.7) | I2CE_PageFormBrowser]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormBrowser/templates modules/Forms/modules/FormBrowser/templates] <br/>[[iHRIS Template List (4.1.7)#formBrowse_menu.html | formBrowse_menu.html]], [[iHRIS Template List (4.1.7)#formBrowser.html | formBrowser.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details.html | formBrowser_form_details.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details_edit.html | formBrowser_form_details_edit.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details_no_record.html | formBrowser_form_details_no_record.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details_record.html | formBrowser_form_details_record.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details_record_edit.html | formBrowser_form_details_record_edit.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details_record_edit_link.html | formBrowser_form_details_record_edit_link.html]], [[iHRIS Template List (4.1.7)#formBrowser_form_details_record_link.html | formBrowser_form_details_record_link.html]], [[iHRIS Template List (4.1.7)#formBrowser_menu.html | formBrowser_menu.html]], [[iHRIS Template List (4.1.7)#formBrowser_menu_form.html | formBrowser_menu_form.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormBrowser/css modules/Forms/modules/FormBrowser/css] 
==formDocumentor==
This describes version 4.1.0 of the module Form Documentor (formDocumentor) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormDocumentor  i2ce/modules/Forms/modules/FormDocumentor ]
*Description: Enables Documenting of existing forms and their relationship from the command line
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormDocumentor/lib modules/Forms/modules/FormDocumentor/lib] <br/>[[Class: I2Ce_Page_FormDocumentor (4.1.7) | I2Ce_Page_FormDocumentor]]
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormDocumentor/images modules/Forms/modules/FormDocumentor/images] 
==formRelationship-viewer==
This describes version 4.1.7.0 of the module Form Relationship Viewer (formRelationship-viewer) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationshipViewer  i2ce/modules/Forms/modules/FormRelationshipViewer ]
*Description: Provides Viewing and Edit of instances of a Form Relationships for use by a Swiss Factory
*Requirements:
**[[iHRIS Module List (4.1.7)#formRelationships | formRelationships]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#swissfactory | swissfactory]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationshipViewer/lib modules/Forms/modules/FormRelationshipViewer/lib] <br/>[[Class: I2CE_PageEditRelationship (4.1.7) | I2CE_PageEditRelationship]], [[Class: I2CE_Swiss_ViewRelationship_Forms (4.1.7) | I2CE_Swiss_ViewRelationship_Forms]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationshipViewer/templates modules/Forms/modules/FormRelationshipViewer/templates] <br/>[[iHRIS Template List (4.1.7)#auto_view_configure.html | auto_view_configure.html]], [[iHRIS Template List (4.1.7)#auto_view_tree.html | auto_view_tree.html]]
==formRelationships==
This describes version 4.1.7.0 of the module Form Relationships (formRelationships) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationship  i2ce/modules/Forms/modules/FormRelationship ]
*Description: Provides Form Relationships for use by a Swiss Factory
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#form-limits | form-limits]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#swissfactory | swissfactory]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationship/configs modules/Forms/modules/FormRelationship/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationship/lib modules/Forms/modules/FormRelationship/lib] <br/>[[Class: I2CE_FormRelationship (4.1.7) | I2CE_FormRelationship]], [[Class: I2CE_FormRelationship_Template (4.1.7) | I2CE_FormRelationship_Template]], [[Class: I2CE_PageActionRelationship (4.1.7) | I2CE_PageActionRelationship]], [[Class: I2CE_PageGenerateRelationshipTemplate (4.1.7) | I2CE_PageGenerateRelationshipTemplate]], [[Class: I2CE_PageViewRelationship (4.1.7) | I2CE_PageViewRelationship]], [[Class: I2CE_RelationshipData (4.1.7) | I2CE_RelationshipData]], [[Class: I2CE_Swiss_FormRelationship (4.1.7) | I2CE_Swiss_FormRelationship]], [[Class: I2CE_Swiss_FormRelationship_AncestralCondition (4.1.7) | I2CE_Swiss_FormRelationship_AncestralCondition]], [[Class: I2CE_Swiss_FormRelationship_AncestralConditions (4.1.7) | I2CE_Swiss_FormRelationship_AncestralConditions]], [[Class: I2CE_Swiss_FormRelationship_Base (4.1.7) | I2CE_Swiss_FormRelationship_Base]], [[Class: I2CE_Swiss_FormRelationship_Join (4.1.7) | I2CE_Swiss_FormRelationship_Join]], [[Class: I2CE_Swiss_FormRelationship_Joins (4.1.7) | I2CE_Swiss_FormRelationship_Joins]], [[Class: I2CE_Swiss_FormRelationship_ReportingFunctions (4.1.7) | I2CE_Swiss_FormRelationship_ReportingFunctions]], [[Class: I2CE_Swiss_FormRelationship_Where (4.1.7) | I2CE_Swiss_FormRelationship_Where]], [[Class: I2CE_Swiss_FormRelationship_Where_Operands (4.1.7) | I2CE_Swiss_FormRelationship_Where_Operands]], [[Class: I2CE_Swiss_FormRelationships (4.1.7) | I2CE_Swiss_FormRelationships]], [[Class: I2CE_Swiss_SQLFunction (4.1.7) | I2CE_Swiss_SQLFunction]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationship/templates modules/Forms/modules/FormRelationship/templates] <br/>[[iHRIS Template List (4.1.7)#auto_view_relationship_form.html | auto_view_relationship_form.html]], [[iHRIS Template List (4.1.7)#formRelationship_condition.html | formRelationship_condition.html]], [[iHRIS Template List (4.1.7)#formRelationship_conditions_container.html | formRelationship_conditions_container.html]], [[iHRIS Template List (4.1.7)#formRelationship_edit.html | formRelationship_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_condition.html | formRelationship_existing_condition.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_conditions.html | formRelationship_existing_conditions.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_function_edit.html | formRelationship_existing_function_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_function_view.html | formRelationship_existing_function_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_join.html | formRelationship_existing_join.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_joins.html | formRelationship_existing_joins.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_limit.html | formRelationship_existing_limit.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_operand.html | formRelationship_existing_operand.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_operand_list.html | formRelationship_existing_operand_list.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_operand_list_member_edit.html | formRelationship_existing_operand_list_member_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_existing_operand_list_member_view.html | formRelationship_existing_operand_list_member_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_join.html | formRelationship_join.html]], [[iHRIS Template List (4.1.7)#formRelationship_join_container.html | formRelationship_join_container.html]], [[iHRIS Template List (4.1.7)#formRelationship_join_displaystyle_edit.html | formRelationship_join_displaystyle_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_join_displaystyle_view.html | formRelationship_join_displaystyle_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_join_drop_empty_edit.html | formRelationship_join_drop_empty_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_join_drop_empty_view.html | formRelationship_join_drop_empty_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_join_meta.html | formRelationship_join_meta.html]], [[iHRIS Template List (4.1.7)#formRelationship_menu_form.html | formRelationship_menu_form.html]], [[iHRIS Template List (4.1.7)#formRelationship_menu_relation_copy.html | formRelationship_menu_relation_copy.html]], [[iHRIS Template List (4.1.7)#formRelationship_meta_edit.html | formRelationship_meta_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_meta_view.html | formRelationship_meta_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_new_condition.html | formRelationship_new_condition.html]], [[iHRIS Template List (4.1.7)#formRelationship_new_limit_choice.html | formRelationship_new_limit_choice.html]], [[iHRIS Template List (4.1.7)#formRelationship_new_limit_style.html | formRelationship_new_limit_style.html]], [[iHRIS Template List (4.1.7)#formRelationship_new_limit_styles.html | formRelationship_new_limit_styles.html]], [[iHRIS Template List (4.1.7)#formRelationship_new_limits.html | formRelationship_new_limits.html]], [[iHRIS Template List (4.1.7)#formRelationship_new_operand.html | formRelationship_new_operand.html]], [[iHRIS Template List (4.1.7)#formRelationship_relationship.html | formRelationship_relationship.html]], [[iHRIS Template List (4.1.7)#formRelationship_relationship_each.html | formRelationship_relationship_each.html]], [[iHRIS Template List (4.1.7)#formRelationship_reporting_functions_edit.html | formRelationship_reporting_functions_edit.html]], [[iHRIS Template List (4.1.7)#formRelationship_reporting_functions_view.html | formRelationship_reporting_functions_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_view.html | formRelationship_view.html]], [[iHRIS Template List (4.1.7)#formRelationship_view_relation.html | formRelationship_view_relation.html]], [[iHRIS Template List (4.1.7)#formRelationship_where_container.html | formRelationship_where_container.html]], [[iHRIS Template List (4.1.7)#formrelationships_options.html | formrelationships_options.html]], [[iHRIS Template List (4.1.7)#swiss_sqlfunction_edit.html | swiss_sqlfunction_edit.html]], [[iHRIS Template List (4.1.7)#swiss_sqlfunction_view.html | swiss_sqlfunction_view.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormRelationship/css modules/Forms/modules/FormRelationship/css] 
==forms==
This describes version 4.1.7.0 of the module I2CE Forms (forms) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms  i2ce/modules/Forms ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Forms (4.1.7)| I2CE_Module_Forms]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_PermissionParser (4.1.7)#hasPermission_form() | I2CE_PermissionParser->hasPermission_form() ]] via [[Class: I2CE_Module_Forms (4.1.7)#hasPermission_form() | hasPermission_form()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setForm() | I2CE_Template->setForm() ]] via [[Class: I2CE_Module_Forms (4.1.7)#setForm() | setForm()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#getForm() | I2CE_Template->getForm() ]] via [[Class: I2CE_Module_Forms (4.1.7)#getForm() | getForm()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#getField() | I2CE_Template->getField() ]] via [[Class: I2CE_Module_Forms (4.1.7)#getField() | getField()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setReview() | I2CE_Template->setReview() ]] via [[Class: I2CE_Module_Forms (4.1.7)#setReview() | setReview()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#isReview() | I2CE_Template->isReview() ]] via [[Class: I2CE_Module_Forms (4.1.7)#isReview() | isReview()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setForm() | I2CE_Page->setForm() ]] via [[Class: I2CE_Module_Forms (4.1.7)#setForm() | setForm()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#getForm() | I2CE_Page->getForm() ]] via [[Class: I2CE_Module_Forms (4.1.7)#getForm() | getForm()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#getField() | I2CE_Page->getField() ]] via [[Class: I2CE_Module_Forms (4.1.7)#getField() | getField()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setReview() | I2CE_Page->setReview() ]] via [[Class: I2CE_Module_Forms (4.1.7)#setReview() | setReview()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#isReview() | I2CE_Page->isReview() ]] via [[Class: I2CE_Module_Forms (4.1.7)#isReview() | isReview()]]
*Description: Adds a few basic forms to the system as well as some form functionality to the template
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#Fields | Fields]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#template-data | template-data]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#DisplayData | DisplayData]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/configs modules/Forms/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/lib modules/Forms/lib] <br/>[[Class: I2CE_Form (4.1.7) | I2CE_Form]], [[Class: I2CE_FormFactory (4.1.7) | I2CE_FormFactory]], [[Class: I2CE_ModuleAccess (4.1.7) | I2CE_ModuleAccess]], [[Class: I2CE_Module_Forms (4.1.7) | I2CE_Module_Forms]], [[Class: I2CE_PageForm (4.1.7) | I2CE_PageForm]], [[Class: I2CE_PageFormAuto (4.1.7) | I2CE_PageFormAuto]], [[Class: I2CE_PageFormBase (4.1.7) | I2CE_PageFormBase]], [[Class: I2CE_PageFormCSV (4.1.7) | I2CE_PageFormCSV]], [[Class: I2CE_PageFormParent (4.1.7) | I2CE_PageFormParent]], [[Class: I2CE_PageMultiForm (4.1.7) | I2CE_PageMultiForm]], [[Class: I2CE_PageViewChildren (4.1.7) | I2CE_PageViewChildren]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/templates modules/Forms/templates] <br/>[[iHRIS Template List (4.1.7)#auto_edit_form.html | auto_edit_form.html]], [[iHRIS Template List (4.1.7)#auto_edit_parent_form.html | auto_edit_parent_form.html]], [[iHRIS Template List (4.1.7)#auto_view_child_form.html | auto_view_child_form.html]], [[iHRIS Template List (4.1.7)#auto_view_parent_form.html | auto_view_parent_form.html]], [[iHRIS Template List (4.1.7)#button_confirm.html | button_confirm.html]], [[iHRIS Template List (4.1.7)#button_confirm_notchild.html | button_confirm_notchild.html]], [[iHRIS Template List (4.1.7)#button_return_only.html | button_return_only.html]], [[iHRIS Template List (4.1.7)#button_save.html | button_save.html]], [[iHRIS Template List (4.1.7)#button_save_only.html | button_save_only.html]], [[iHRIS Template List (4.1.7)#button_save_return.html | button_save_return.html]], [[iHRIS Template List (4.1.7)#form_error.html | form_error.html]]
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/scripts modules/Forms/scripts] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules modules/Forms/modules] <br/>[[#BinField |BinField]], [[#CachedForms |CachedForms]], [[#Fields |Fields]], [[#Float |Float]], [[#Lists |Lists]], [[#LocaleForm |LocaleForm]], [[#PrintedForms |PrintedForms]], [[#ReferenceField |ReferenceField]], [[#UserForm |UserForm]], [[#field-limits |field-limits]], [[#form-limits |form-limits]], [[#form-relationship-based-permission |form-relationship-based-permission]], [[#formBrowser |formBrowser]], [[#formDocumentor |formDocumentor]], [[#formRelationship-viewer |formRelationship-viewer]], [[#formRelationships |formRelationships]], [[#forms-storage |forms-storage]]
==forms-storage==
This describes version 4.1.7.0 of the module Form Storage (forms-storage) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage  i2ce/modules/Forms/modules/FormStorage ]
*Module Class: The module class is implemented by [[Class: I2CE_FormStorage (4.1.7)| I2CE_FormStorage]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Form (4.1.7)#isComponentized() | I2CE_Form->isComponentized() ]] via [[Class: I2CE_FormStorage (4.1.7)#isComponentizedForm() | isComponentizedForm()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#addChild() | I2CE_Form->addChild() ]] via [[Class: I2CE_FormStorage (4.1.7)#addChild() | addChild()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#getChildIds() | I2CE_Form->getChildIds() ]] via [[Class: I2CE_FormStorage (4.1.7)#getChildIds() | getChildIds()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#getStorage() | I2CE_Form->getStorage() ]] via [[Class: I2CE_FormStorage (4.1.7)#getStorage() | getStorage()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#isWritable() | I2CE_Form->isWritable() ]] via [[Class: I2CE_FormStorage (4.1.7)#isWritable() | isWritable()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#populate() | I2CE_Form->populate() ]] via [[Class: I2CE_FormStorage (4.1.7)#populate() | populate()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#duplicate() | I2CE_Form->duplicate() ]] via [[Class: I2CE_FormStorage (4.1.7)#duplicate() | duplicate()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#storeHistory() | I2CE_Form->storeHistory() ]] via [[Class: I2CE_FormStorage (4.1.7)#storeHistory() | storeHistory()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#populateChild() | I2CE_Form->populateChild() ]] via [[Class: I2CE_FormStorage (4.1.7)#populateChild() | populateChild()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#populateChildren() | I2CE_Form->populateChildren() ]] via [[Class: I2CE_FormStorage (4.1.7)#populateChildren() | populateChildren()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#populateFirst() | I2CE_Form->populateFirst() ]] via [[Class: I2CE_FormStorage (4.1.7)#populateFirst() | populateFirst()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#populateHistory() | I2CE_Form->populateHistory() ]] via [[Class: I2CE_FormStorage (4.1.7)#populateHistory() | populateHistory()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#populateLast() | I2CE_Form->populateLast() ]] via [[Class: I2CE_FormStorage (4.1.7)#populateLast() | populateLast()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#delete() | I2CE_Form->delete() ]] via [[Class: I2CE_FormStorage (4.1.7)#delete() | delete()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#save() | I2CE_Form->save() ]] via [[Class: I2CE_FormStorage (4.1.7)#save() | save()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#setChangeType() | I2CE_Form->setChangeType() ]] via [[Class: I2CE_FormStorage (4.1.7)#setChangeType() | setChangeType()]]
**Implements the method [[Class: I2CE_Form (4.1.7)#changeID() | I2CE_Form->changeID() ]] via [[Class: I2CE_FormStorage (4.1.7)#changeID() | changeID()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#save() | I2CE_FormField->save() ]] via [[Class: I2CE_FormStorage (4.1.7)#FF_save() | FF_save()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#globalFieldUpdate() | I2CE_FormField->globalFieldUpdate() ]] via [[Class: I2CE_FormStorage (4.1.7)#globalFieldUpdate() | globalFieldUpdate()]]
**Implements the method [[Class: I2CE_FormField_INT_GENERATE (4.1.7)#save() | I2CE_FormField_INT_GENERATE->save() ]] via [[Class: I2CE_FormStorage (4.1.7)#FF_IG_save() | FF_IG_save()]]
**Implements the method [[Class: I2CE_FormField_STRING_PASS (4.1.7)#save() | I2CE_FormField_STRING_PASS->save() ]] via [[Class: I2CE_FormStorage (4.1.7)#FF_SP_save() | FF_SP_save()]]
**Implements the method [[Class: I2CE_FormField (4.1.7)#populateHistory() | I2CE_FormField->populateHistory() ]] via [[Class: I2CE_FormStorage (4.1.7)#FF_populateHistory() | FF_populateHistory()]]
**Implements the method [[Class: I2CE_FormField_INT_GENERATE (4.1.7)#setSequence() | I2CE_FormField_INT_GENERATE->setSequence() ]] via [[Class: I2CE_FormStorage (4.1.7)#FF_IG_setSequence() | FF_IG_setSequence()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#getRecords() | I2CE_FormFactory->getRecords() ]] via [[Class: I2CE_FormStorage (4.1.7)#getRecords() | getRecords()]]
**Implements the method [[Class: I2CE_FormFactory (4.1.7)#hasRecord() | I2CE_FormFactory->hasRecord() ]] via [[Class: I2CE_FormStorage (4.1.7)#hasRecord() | hasRecord()]]
*Description: A module that enables storage of Forms. Sub modules will enable the specific storage and retrieval options.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms | forms]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/lib modules/Forms/modules/FormStorage/lib] <br/>[[Class: I2CE_FormStorage (4.1.7) | I2CE_FormStorage]], [[Class: I2CE_FormStorage_DB (4.1.7) | I2CE_FormStorage_DB]], [[Class: I2CE_FormStorage_Mechanism (4.1.7) | I2CE_FormStorage_Mechanism]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/sql modules/Forms/modules/FormStorage/sql] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules modules/Forms/modules/FormStorage/modules] <br/>[[#form-task-log |form-task-log]], [[#forms-storage-CSV |forms-storage-CSV]], [[#forms-storage-LDAP |forms-storage-LDAP]], [[#forms-storage-SDMXHD |forms-storage-SDMXHD]], [[#forms-storage-entry |forms-storage-entry]], [[#forms-storage-eval |forms-storage-eval]], [[#forms-storage-file |forms-storage-file]], [[#forms-storage-flat |forms-storage-flat]], [[#forms-storage-magicdata |forms-storage-magicdata]], [[#forms-storage-multiflat |forms-storage-multiflat]], [[#forms-storage-xml |forms-storage-xml]]
==forms-storage-CSV==
This describes version 4.1.0 of the module Form Storage - CSV (forms-storage-CSV) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageCSV  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageCSV ]
*Description: A module that enables reading storage of Forms from a CSV file
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage-file | forms-storage-file]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageCSV/lib modules/Forms/modules/FormStorage/modules/FormStorageCSV/lib] <br/>[[Class: I2CE_FormStorage_CSV (4.1.7) | I2CE_FormStorage_CSV]]
==forms-storage-LDAP==
This describes version 4.1.4.0 of the module Form Storage - LDAP (forms-storage-LDAP) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageLDAP  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageLDAP ]
*Description: A module that enables reading storage of Forms from a LDAP server
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageLDAP/lib modules/Forms/modules/FormStorage/modules/FormStorageLDAP/lib] <br/>[[Class: I2CE_FormStorage_LDAP (4.1.7) | I2CE_FormStorage_LDAP]]
==forms-storage-SDMXHD==
This describes version 4.1.0 of the module Form Storage - SDMX-HD (forms-storage-SDMXHD) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageSDMXHD  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageSDMXHD ]
*Description: A module that enables reading storage of Forms from a SDMX CodeList or CrossSectionalData
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#forms-storage-xml | forms-storage-xml]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageSDMXHD/lib modules/Forms/modules/FormStorage/modules/FormStorageSDMXHD/lib] <br/>[[Class: I2CE_FormStorage_SDMXHD (4.1.7) | I2CE_FormStorage_SDMXHD]], [[Class: I2CE_FormStorage_SDMX_CrossSectional (4.1.7) | I2CE_FormStorage_SDMX_CrossSectional]]
==forms-storage-entry==
This describes version 4.1.7.0 of the module Form Storage - Entry (forms-storage-entry) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageEntry  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageEntry ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_FormStorageEntry (4.1.7)| I2CE_Module_FormStorageEntry]]
*Description: A module that enables storage of Forms to a entry database structure that enables historical tracking and automatic extension for new fields.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageEntry/lib modules/Forms/modules/FormStorage/modules/FormStorageEntry/lib] <br/>[[Class: I2CE_FormStorage_entry (4.1.7) | I2CE_FormStorage_entry]], [[Class: I2CE_Module_FormStorageEntry (4.1.7) | I2CE_Module_FormStorageEntry]]
**Sql: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageEntry/sql modules/Forms/modules/FormStorage/modules/FormStorageEntry/sql] 
==forms-storage-eval==
This describes version 4.1.0 of the module Form Storage - Eval (forms-storage-eval) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageEval  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageEval ]
*Description: A module that enables storage of Forms based on evalualtion of php functions
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageEval/lib modules/Forms/modules/FormStorage/modules/FormStorageEval/lib] <br/>[[Class: I2CE_FormStorage_eval (4.1.7) | I2CE_FormStorage_eval]]
==forms-storage-file==
This describes version 4.1.5.0 of the module Form Storage - File (forms-storage-file) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageFile  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageFile ]
*Description: A module that for file based access form storage mechanisms
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageFile/lib modules/Forms/modules/FormStorage/modules/FormStorageFile/lib] <br/>[[Class: I2CE_FormStorage_File_Base (4.1.7) | I2CE_FormStorage_File_Base]]
==forms-storage-flat==
This describes version 4.1.4.0 of the module Form Storage - Flat (forms-storage-flat) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageFlat  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageFlat ]
*Description: A module that enables storage of Forms to a flat fixed database structure.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageFlat/lib modules/Forms/modules/FormStorage/modules/FormStorageFlat/lib] <br/>[[Class: I2CE_FormStorage_Flat (4.1.7) | I2CE_FormStorage_Flat]]
==forms-storage-magicdata==
This describes version 4.1.7.0 of the module Form Storage - Magic Data (forms-storage-magicdata) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageMagicData  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageMagicData ]
*Description: A module that enables storage of Forms to MagicData Storage.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageMagicData/lib modules/Forms/modules/FormStorage/modules/FormStorageMagicData/lib] <br/>[[Class: I2CE_FormStorage_magicdata (4.1.7) | I2CE_FormStorage_magicdata]], [[Class: I2CE_FormStorage_magicdata (4.1.7) | I2CE_FormStorage_magicdata]], [[Class: I2CE_FormStorage_magicdata (4.1.7) | I2CE_FormStorage_magicdata]]
==forms-storage-multiflat==
This describes version 4.1.4.0 of the module Form Storage - Multi Flat (forms-storage-multiflat) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageMultiFlat  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageMultiFlat ]
*Description: A module that enables aggregated storage of Forms from a flat fixed database structure.
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage | forms-storage]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#Lists | Lists]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageMultiFlat/lib modules/Forms/modules/FormStorage/modules/FormStorageMultiFlat/lib] <br/>[[Class: I2CE_FormStorage_multi_flat (4.1.7) | I2CE_FormStorage_multi_flat]]
==forms-storage-xml==
This describes version 4.1.7.0 of the module Form Storage - XML (forms-storage-xml) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageXML  i2ce/modules/Forms/modules/FormStorage/modules/FormStorageXML ]
*Description: A module that enables reading storage of Forms from a XML file
*Requirements:
**[[iHRIS Module List (4.1.7)#forms-storage-file | forms-storage-file]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Forms/modules/FormStorage/modules/FormStorageXML/lib modules/Forms/modules/FormStorage/modules/FormStorageXML/lib] <br/>[[Class: I2CE_FormStorage_XML (4.1.7) | I2CE_FormStorage_XML]], [[Class: I2CE_FormStorage_XML_BASE (4.1.7) | I2CE_FormStorage_XML_BASE]]
==i2ce-site==
This describes version 4.1.2.0 of the module Site (i2ce-site) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Site  i2ce/modules/Site ]
*Description: Marker for I2CE Site
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Site/ modules/Site/] 
==jumper==
This describes version 4.1.0 of the module Page Jumper (jumper) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Jumper  i2ce/modules/Jumper ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_Jumper (4.1.7)| I2CE_Module_Jumper]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#makeJumper() | I2CE_Page->makeJumper() ]] via [[Class: I2CE_Module_Jumper (4.1.7)#makeJumper() | makeJumper()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#makeJumper() | I2CE_Template->makeJumper() ]] via [[Class: I2CE_Module_Jumper (4.1.7)#makeJumper() | makeJumper()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#makeScalingJumper() | I2CE_Page->makeScalingJumper() ]] via [[Class: I2CE_Module_Jumper (4.1.7)#makeScalingJumper() | makeScalingJumper()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#makeScalingJumper() | I2CE_Template->makeScalingJumper() ]] via [[Class: I2CE_Module_Jumper (4.1.7)#makeScalingJumper() | makeScalingJumper()]]
*Description: Creates a page jumper for elements of a page.
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Optionally Enables: [[iHRIS Module List (4.1.7)#stub | stub]]
*Paths:
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Jumper/images modules/Jumper/images] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Jumper/css modules/Jumper/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Jumper/ modules/Jumper/] <br/>[[Class: I2CE_Module_Jumper (4.1.7) | I2CE_Module_Jumper]]
==localeSelector==
This describes version 4.1.7.0 of the module Locale Selector (localeSelector) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector  i2ce/modules/Pages/modules/LocaleSelector ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_LocaleSelector (4.1.7)| I2CE_Module_LocaleSelector]]
*Description: Provides Locale Selector for a page as well information for locales
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#swissfactory | swissfactory]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/lib modules/Pages/modules/LocaleSelector/lib] <br/>[[Class: I2CE_Module_LocaleSelector (4.1.7) | I2CE_Module_LocaleSelector]], [[Class: I2CE_Page_LocaleAdmin (4.1.7) | I2CE_Page_LocaleAdmin]], [[Class: I2CE_Swiss_Locale (4.1.7) | I2CE_Swiss_Locale]], [[Class: I2CE_Swiss_Locales (4.1.7) | I2CE_Swiss_Locales]]
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/images modules/Pages/modules/LocaleSelector/images] 
**Misc: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/Flags.xml modules/Pages/modules/LocaleSelector/Flags.xml] 
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/configs modules/Pages/modules/LocaleSelector/configs] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/templates modules/Pages/modules/LocaleSelector/templates] <br/>[[iHRIS Template List (4.1.7)#language_choice.html | language_choice.html]], [[iHRIS Template List (4.1.7)#language_choice_icon.html | language_choice_icon.html]], [[iHRIS Template List (4.1.7)#locale_edit.html | locale_edit.html]], [[iHRIS Template List (4.1.7)#locale_view.html | locale_view.html]], [[iHRIS Template List (4.1.7)#site_locale_add.html | site_locale_add.html]], [[iHRIS Template List (4.1.7)#site_locale_base.html | site_locale_base.html]], [[iHRIS Template List (4.1.7)#site_locale_base_edit.html | site_locale_base_edit.html]], [[iHRIS Template List (4.1.7)#site_locale_each.html | site_locale_each.html]]
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/LocaleSelector/modules modules/Pages/modules/LocaleSelector/modules] <br/>[[#default-locales |default-locales]]
==maani-charts==
This describes version 4.7 of the module Charted Reports (maani-charts) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/FlashCharts  i2ce/modules/FlashCharts ]
*Description: Configuration options for the Maani chart reporting software http://www.maani.us/charts
*Requirements:
**[[iHRIS Module List (4.1.7)#FileDump | FileDump]] at least 4.1 and less than 4.2
*Paths:
**Maani_chart_files: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/FlashCharts/maani_charts modules/FlashCharts/maani_charts] 
**Swf: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/FlashCharts/maani_charts modules/FlashCharts/maani_charts] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/FlashCharts/scripts modules/FlashCharts/scripts] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/FlashCharts/ modules/FlashCharts/] 
==magicDataBrowser==
This describes version 4.1.7.0 of the module Magic Data Browser (magicDataBrowser) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/MagicDataBrowser  i2ce/modules/Pages/modules/MagicDataBrowser ]
*Description: Browse Magic Data
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#FormWorm | FormWorm]] at least 4.1 and less than 4.2
*Optionally Enables: [[iHRIS Module List (4.1.7)#magicDataExport | magicDataExport]]
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/MagicDataBrowser/configs modules/Pages/modules/MagicDataBrowser/configs] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/MagicDataBrowser/scripts modules/Pages/modules/MagicDataBrowser/scripts] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/MagicDataBrowser/templates modules/Pages/modules/MagicDataBrowser/templates] <br/>[[iHRIS Template List (4.1.7)#browser.html | browser.html]], [[iHRIS Template List (4.1.7)#browser_add_node.html | browser_add_node.html]], [[iHRIS Template List (4.1.7)#browser_binary_node.html | browser_binary_node.html]], [[iHRIS Template List (4.1.7)#browser_binary_node_mini.html | browser_binary_node_mini.html]], [[iHRIS Template List (4.1.7)#browser_node.html | browser_node.html]], [[iHRIS Template List (4.1.7)#browser_node_mini.html | browser_node_mini.html]], [[iHRIS Template List (4.1.7)#browser_value_node.html | browser_value_node.html]], [[iHRIS Template List (4.1.7)#browser_value_node_mini.html | browser_value_node_mini.html]], [[iHRIS Template List (4.1.7)#browser_value_node_notset.html | browser_value_node_notset.html]], [[iHRIS Template List (4.1.7)#browser_value_node_notset_mini.html | browser_value_node_notset_mini.html]], [[iHRIS Template List (4.1.7)#magicdata_export_controls.html | magicdata_export_controls.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/MagicDataBrowser/css modules/Pages/modules/MagicDataBrowser/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/MagicDataBrowser/ modules/Pages/modules/MagicDataBrowser/] <br/>[[Class: I2CE_Page_MagicDataBrowser (4.1.7) | I2CE_Page_MagicDataBrowser]]
==magicDataExport==
This describes version 4.1.6.0 of the module Magic Data Export (magicDataExport) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MagicDataExport  i2ce/modules/MagicDataExport ]
*Description: Export Magic Data
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Xml: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MagicDataExport/xml modules/MagicDataExport/xml] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MagicDataExport/ modules/MagicDataExport/] <br/>[[Class: I2CE_MagicDataExport_Template (4.1.7) | I2CE_MagicDataExport_Template]], [[Class: I2CE_Page_MagicDataExport (4.1.7) | I2CE_Page_MagicDataExport]]
==menu_select==
This describes version 4.1.2.0 of the module Menu Select (menu_select) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/MenuSelect  i2ce/modules/MooTools/modules/MenuSelect ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_MenuSelect (4.1.7)| I2CE_Module_MenuSelect]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#menuSelect() | I2CE_Page->menuSelect() ]] via [[Class: I2CE_Module_MenuSelect (4.1.7)#menuSelect() | menuSelect()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#menuSelect() | I2CE_Template->menuSelect() ]] via [[Class: I2CE_Module_MenuSelect (4.1.7)#menuSelect() | menuSelect()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addUpdateSelect() | I2CE_Page->addUpdateSelect() ]] via [[Class: I2CE_Module_MenuSelect (4.1.7)#addUpdateSelect() | addUpdateSelect()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addUpdateSelect() | I2CE_Template->addUpdateSelect() ]] via [[Class: I2CE_Module_MenuSelect (4.1.7)#addUpdateSelect() | addUpdateSelect()]]
*Description: Handles Nested Select Options
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/MenuSelect/scripts modules/MooTools/modules/MenuSelect/scripts] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MooTools/modules/MenuSelect/ modules/MooTools/modules/MenuSelect/] 
==messageBox==
This describes version 4.1.2.0 of the module Message Box (messageBox) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageBox  i2ce/modules/MessageHandler/modules/MessageBox ]
*Module Class: The module class is implemented by [[Class: I2CE_MessageBox (4.1.7)| I2CE_MessageBox]]
*Description: Displays the default message in a box
*Requirements:
**[[iHRIS Module List (4.1.7)#messageHandler | messageHandler]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageBox/scripts modules/MessageHandler/modules/MessageBox/scripts] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageBox/css modules/MessageHandler/modules/MessageBox/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageBox/ modules/MessageHandler/modules/MessageBox/] <br/>[[Class: I2CE_MessageBox (4.1.7) | I2CE_MessageBox]]
==messageHandler==
This describes version 4.1.0 of the module Message Handler (messageHandler) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler  i2ce/modules/MessageHandler ]
*Module Class: The module class is implemented by [[Class: I2CE_MessageHandler (4.1.7)| I2CE_MessageHandler]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Fuzzy (4.1.7)#userMessage() | I2CE_Fuzzy->userMessage() ]] via [[Class: I2CE_MessageHandler (4.1.7)#addUserMessage() | addUserMessage()]]
*Description: A handler for user messages
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules modules/MessageHandler/modules] <br/>[[#messageBox |messageBox]], [[#messageNotice |messageNotice]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/ modules/MessageHandler/] <br/>[[Class: I2CE_MessageHandler (4.1.7) | I2CE_MessageHandler]], [[Class: I2CE_MessageNotice (4.1.7) | I2CE_MessageNotice]]
==messageNotice==
This describes version 4.1.7.0 of the module Message Notices (messageNotice) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageNotice  i2ce/modules/MessageHandler/modules/MessageNotice ]
*Module Class: The module class is implemented by [[Class: I2CE_MessageNotice (4.1.7)| I2CE_MessageNotice]]
*Description: Displays any messages taggged with 'notice' in a notice box box
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#messageHandler | messageHandler]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageNotice/scripts modules/MessageHandler/modules/MessageNotice/scripts] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageNotice/templates modules/MessageHandler/modules/MessageNotice/templates] <br/>[[iHRIS Template List (4.1.7)#message_notice.html | message_notice.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageNotice/css modules/MessageHandler/modules/MessageNotice/css] 
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageNotice/images modules/MessageHandler/modules/MessageNotice/images] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/MessageHandler/modules/MessageNotice/ modules/MessageHandler/modules/MessageNotice/] 
==modDocumentor==
This describes version 4.1.0 of the module Mod Documentor (modDocumentor) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/ModDocumentor  i2ce/modules/Pages/modules/ModDocumentor ]
*Description: Enables Documenting of existing mods and their relationship from the command line
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/ModDocumentor/lib modules/Pages/modules/ModDocumentor/lib] <br/>[[Class: I2Ce_Page_ModDocumentor (4.1.7) | I2Ce_Page_ModDocumentor]]
==modulePrompter==
This describes version 4.1.0 of the module Module Prompter (modulePrompter) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/ModulePrompter  i2ce/modules/Pages/modules/Admin/modules/ModulePrompter ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_ModulePrompter (4.1.7)| I2CE_Module_ModulePrompter]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Wrangler (4.1.7)#manipulateWrangler_I2CE_home() | I2CE_Wrangler->manipulateWrangler_I2CE_home() ]] via [[Class: I2CE_Module_ModulePrompter (4.1.7)#changeHomePage() | changeHomePage()]]
*Description: Module to prompt the enable/disable of specific modules upon login
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#admin | admin]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Admin/modules/ModulePrompter/lib modules/Pages/modules/Admin/modules/ModulePrompter/lib] <br/>[[Class: I2CE_Module_ModulePrompter (4.1.7) | I2CE_Module_ModulePrompter]]
==pChart==
This describes version 2.1.3.0 of the module pChart Charting (pChart) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/pChart  i2ce/modules/pChart ]
*Description: Configuration options for the pChart chart reporting software http://www.pchart.net/
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 5.0
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/pChart/configs modules/pChart/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/pChart/lib modules/pChart/lib] <br/>[[Class: I2CE_PagePChart (4.1.7) | I2CE_PagePChart]], [[Class: I2CE_PagePChartFile (4.1.7) | I2CE_PagePChartFile]], [[Class: pBarcode128 (4.1.7) | pBarcode128]], [[Class: pBarcode39 (4.1.7) | pBarcode39]], [[Class: pBubble (4.1.7) | pBubble]], [[Class: pCache (4.1.7) | pCache]], [[Class: pData (4.1.7) | pData]], [[Class: pDraw (4.1.7) | pDraw]], [[Class: pImage (4.1.7) | pImage]], [[Class: pIndicator (4.1.7) | pIndicator]], [[Class: pPie (4.1.7) | pPie]], [[Class: pRadar (4.1.7) | pRadar]], [[Class: pScatter (4.1.7) | pScatter]], [[Class: pSplit (4.1.7) | pSplit]], [[Class: pSpring (4.1.7) | pSpring]], [[Class: pStock (4.1.7) | pStock]], [[Class: pSurface (4.1.7) | pSurface]]
**Pchart_fonts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/pChart/fonts modules/pChart/fonts] 
**Pchart_palettes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/pChart/palettes modules/pChart/palettes] 
**Pchart_data: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/pChart/data modules/pChart/data] 
==pages==
This describes version 4.1.7.0 of the module Pages (pages) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages  i2ce/modules/Pages ]
*Description: Provides pages, Users and Templates
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#user | user]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#permissions | permissions]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/configs modules/Pages/configs] 
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules modules/Pages/modules] <br/>[[#FileDump |FileDump]], [[#LoginPage |LoginPage]], [[#admin |admin]], [[#localeSelector |localeSelector]], [[#magicDataBrowser |magicDataBrowser]], [[#modDocumentor |modDocumentor]], [[#stub |stub]], [[#tabbed-pages |tabbed-pages]], [[#tasks-roles |tasks-roles]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/templates modules/Pages/templates] <br/>[[iHRIS Template List (4.1.7)#main.html | main.html]], [[iHRIS Template List (4.1.7)#noaccess.html | noaccess.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/lib modules/Pages/lib] <br/>[[Class: I2CE_Page (4.1.7) | I2CE_Page]], [[Class: I2CE_Template (4.1.7) | I2CE_Template]], [[Class: I2CE_Wrangler (4.1.7) | I2CE_Wrangler]]
==permissions==
This describes version 4.1.1.0 of the module Permission System (permissions) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Permissions  i2ce/modules/Permissions ]
*Description: A module that enables role and task based permissions
*Requirements:
**[[iHRIS Module List (4.1.7)#user | user]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Permissions/lib modules/Permissions/lib] <br/>[[Class: I2CE_PermissionParser (4.1.7) | I2CE_PermissionParser]]
==stub==
This describes version 4.1.2.0 of the module Page Stubs (stub) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Stub  i2ce/modules/Pages/modules/Stub ]
*Module Class: The module class is implemented by [[Class: I2CE_Stub (4.1.7)| I2CE_Stub]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#addAjaxUpdate() | I2CE_Page->addAjaxUpdate() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxUpdate() | addAjaxUpdate()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAjaxUpdate() | I2CE_Template->addAjaxUpdate() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxUpdate() | addAjaxUpdate()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addAjaxToggle() | I2CE_Page->addAjaxToggle() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxToggle() | addAjaxToggle()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAjaxToggle() | I2CE_Template->addAjaxToggle() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxToggle() | addAjaxToggle()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addAjaxRequestFunction() | I2CE_Page->addAjaxRequestFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxRequestFunction() | addAjaxRequestFunction()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAjaxRequestFunction() | I2CE_Template->addAjaxRequestFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxRequestFunction() | addAjaxRequestFunction()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addAjaxCompleteFunction() | I2CE_Page->addAjaxCompleteFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxCompleteFunction() | addAjaxCompleteFunction()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAjaxCompleteFunction() | I2CE_Template->addAjaxCompleteFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxCompleteFunction() | addAjaxCompleteFunction()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addAjaxToggleOnFunction() | I2CE_Page->addAjaxToggleOnFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxToggleOnFunction() | addAjaxToggleOnFunction()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAjaxToggleOnFunction() | I2CE_Template->addAjaxToggleOnFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxToggleOnFunction() | addAjaxToggleOnFunction()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#addAjaxToggleOffFunction() | I2CE_Page->addAjaxToggleOffFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxToggleOffFunction() | addAjaxToggleOffFunction()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#addAjaxToggleOffFunction() | I2CE_Template->addAjaxToggleOffFunction() ]] via [[Class: I2CE_Stub (4.1.7)#addAjaxToggleOffFunction() | addAjaxToggleOffFunction()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#hasAjax() | I2CE_Page->hasAjax() ]] via [[Class: I2CE_Stub (4.1.7)#hasAjaxFuzzy() | hasAjaxFuzzy()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#hasAjax() | I2CE_Template->hasAjax() ]] via [[Class: I2CE_Stub (4.1.7)#hasAjaxFuzzy() | hasAjaxFuzzy()]]
*Description: Request only the stub of a page -- intended for ajax use.
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Stub/configs modules/Pages/modules/Stub/configs] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Stub/scripts modules/Pages/modules/Stub/scripts] 
**Images: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Stub/images modules/Pages/modules/Stub/images] 
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Stub/css modules/Pages/modules/Stub/css] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Stub/ modules/Pages/modules/Stub/] <br/>[[Class: I2CE_Page_Stub (4.1.7) | I2CE_Page_Stub]], [[Class: I2CE_Page_Stub_Ajax_Test (4.1.7) | I2CE_Page_Stub_Ajax_Test]], [[Class: I2CE_Stub (4.1.7) | I2CE_Stub]]
==swissConfig==
This describes version 4.1.5.0 of the module Swiss Config (swissConfig) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules/SwissConfig  i2ce/modules/SwissFactory/modules/SwissConfig ]
*Description: The Swiss Factory Module to display configuration files
*Requirements:
**[[iHRIS Module List (4.1.7)#swissfactory | swissfactory]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules/SwissConfig/configs modules/SwissFactory/modules/SwissConfig/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules/SwissConfig/lib modules/SwissFactory/modules/SwissConfig/lib] <br/>[[Class: I2CE_Page_SwissConfig (4.1.7) | I2CE_Page_SwissConfig]], [[Class: I2CE_SwissConfigFactory (4.1.7) | I2CE_SwissConfigFactory]]
==swissMagic==
This describes version 4.1.5.0 of the module Swiss Magic (swissMagic) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules/SwissMagic  i2ce/modules/SwissFactory/modules/SwissMagic ]
*Description: The Swiss Factory Module to display magic data directly
*Requirements:
**[[iHRIS Module List (4.1.7)#swissfactory | swissfactory]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules/SwissMagic/configs modules/SwissFactory/modules/SwissMagic/configs] 
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules/SwissMagic/lib modules/SwissFactory/modules/SwissMagic/lib] <br/>[[Class: I2CE_Page_SwissMagic (4.1.7) | I2CE_Page_SwissMagic]]
==swissfactory==
This describes version 4.1.7.0 of the module Swiss Factory (swissfactory) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory  i2ce/modules/SwissFactory ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_SwissFactory (4.1.7)| I2CE_Module_SwissFactory]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_string_single() | I2CE_Swiss_Default_Leaf->editValue_string_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_string_single() | editValue_string_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_string_many() | I2CE_Swiss_Default_Leaf->editValue_string_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_string_many() | editValue_string_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_delimited_single() | I2CE_Swiss_Default_Leaf->editValue_delimited_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_delimited_single() | editValue_delimited_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_delimited_many() | I2CE_Swiss_Default_Leaf->editValue_delimited_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_delimited_many() | editValue_delimited_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_boolean_single() | I2CE_Swiss_Default_Leaf->editValue_boolean_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_boolean_single() | editValue_boolean_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_boolean_many() | I2CE_Swiss_Default_Leaf->editValue_boolean_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_boolean_many() | editValue_boolean_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_list_single() | I2CE_Swiss_Default_Leaf->editValue_list_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_list_single() | editValue_list_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#editValue_list_many() | I2CE_Swiss_Default_Leaf->editValue_list_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#editValue_list_many() | editValue_list_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_string_single() | I2CE_Swiss_Default_Leaf->viewValue_string_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_string_single() | viewValue_string_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_string_many() | I2CE_Swiss_Default_Leaf->viewValue_string_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_string_many() | viewValue_string_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_delimited_single() | I2CE_Swiss_Default_Leaf->viewValue_delimited_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_delimited_single() | viewValue_delimited_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_delimited_many() | I2CE_Swiss_Default_Leaf->viewValue_delimited_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_delimited_many() | viewValue_delimited_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_boolean_single() | I2CE_Swiss_Default_Leaf->viewValue_boolean_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_boolean_single() | viewValue_boolean_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_boolean_many() | I2CE_Swiss_Default_Leaf->viewValue_boolean_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_boolean_many() | viewValue_boolean_many()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_list_single() | I2CE_Swiss_Default_Leaf->viewValue_list_single() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_list_single() | viewValue_list_single()]]
**Implements the method [[Class: I2CE_Swiss_Default_Leaf (4.1.7)#viewValue_list_many() | I2CE_Swiss_Default_Leaf->viewValue_list_many() ]] via [[Class: I2CE_Module_SwissFactory (4.1.7)#viewValue_list_many() | viewValue_list_many()]]
*Description: The Swiss Factory Magic Data Editing System
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#FormWorm | FormWorm]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#menu_select | menu_select]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/lib modules/SwissFactory/lib] <br/>[[Class: I2CE_Module_SwissFactory (4.1.7) | I2CE_Module_SwissFactory]], [[Class: I2CE_Swiss (4.1.7) | I2CE_Swiss]], [[Class: I2CE_SwissFactory (4.1.7) | I2CE_SwissFactory]], [[Class: I2CE_SwissMagicFactory (4.1.7) | I2CE_SwissMagicFactory]], [[Class: I2CE_Swiss_Default (4.1.7) | I2CE_Swiss_Default]], [[Class: I2CE_Swiss_Default_Base (4.1.7) | I2CE_Swiss_Default_Base]], [[Class: I2CE_Swiss_Default_Leaf (4.1.7) | I2CE_Swiss_Default_Leaf]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/templates modules/SwissFactory/templates] <br/>[[iHRIS Template List (4.1.7)#configuration_boolean_single.html | configuration_boolean_single.html]], [[iHRIS Template List (4.1.7)#configuration_boolean_single_view.html | configuration_boolean_single_view.html]], [[iHRIS Template List (4.1.7)#configuration_delimited_individual.html | configuration_delimited_individual.html]], [[iHRIS Template List (4.1.7)#configuration_delimited_individual_view.html | configuration_delimited_individual_view.html]], [[iHRIS Template List (4.1.7)#configuration_delimited_many.html | configuration_delimited_many.html]], [[iHRIS Template List (4.1.7)#configuration_delimited_single.html | configuration_delimited_single.html]], [[iHRIS Template List (4.1.7)#configuration_delimited_single_individual.html | configuration_delimited_single_individual.html]], [[iHRIS Template List (4.1.7)#configuration_list_many.html | configuration_list_many.html]], [[iHRIS Template List (4.1.7)#configuration_list_many_view.html | configuration_list_many_view.html]], [[iHRIS Template List (4.1.7)#configuration_list_single.html | configuration_list_single.html]], [[iHRIS Template List (4.1.7)#configuration_list_single_view.html | configuration_list_single_view.html]], [[iHRIS Template List (4.1.7)#configuration_main.html | configuration_main.html]], [[iHRIS Template List (4.1.7)#configuration_noindex_string_many.html | configuration_noindex_string_many.html]], [[iHRIS Template List (4.1.7)#configuration_noindex_string_many_individual.html | configuration_noindex_string_many_individual.html]], [[iHRIS Template List (4.1.7)#configuration_noindex_string_many_individual_view.html | configuration_noindex_string_many_individual_view.html]], [[iHRIS Template List (4.1.7)#configuration_options.html | configuration_options.html]], [[iHRIS Template List (4.1.7)#configuration_string_many.html | configuration_string_many.html]], [[iHRIS Template List (4.1.7)#configuration_string_many_individual.html | configuration_string_many_individual.html]], [[iHRIS Template List (4.1.7)#configuration_string_many_individual_view.html | configuration_string_many_individual_view.html]], [[iHRIS Template List (4.1.7)#configuration_string_single.html | configuration_string_single.html]], [[iHRIS Template List (4.1.7)#configuration_string_single_view.html | configuration_string_single_view.html]], [[iHRIS Template List (4.1.7)#configurationGroup_default.html | configurationGroup_default.html]], [[iHRIS Template List (4.1.7)#configurationGroups.html | configurationGroups.html]], [[iHRIS Template List (4.1.7)#configurations.html | configurations.html]], [[iHRIS Template List (4.1.7)#swiss_factory_edit.html | swiss_factory_edit.html]], [[iHRIS Template List (4.1.7)#swiss_factory_view.html | swiss_factory_view.html]]
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/modules modules/SwissFactory/modules] <br/>[[#swissConfig |swissConfig]], [[#swissMagic |swissMagic]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/SwissFactory/css modules/SwissFactory/css] 
==tabbed-pages==
This describes version 4.1.6.0 of the module Tabbed Pages (tabbed-pages) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Tabbed  i2ce/modules/Pages/modules/Tabbed ]
*Description: The I2CE module pages system
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
**[[iHRIS Module List (4.1.7)#MooTools | MooTools]] at least 1.4 and less than 1.5
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Tabbed/lib modules/Pages/modules/Tabbed/lib] <br/>[[Class: I2CE_PageTabbed (4.1.7) | I2CE_PageTabbed]]
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Tabbed/templates modules/Pages/modules/Tabbed/templates] <br/>[[iHRIS Template List (4.1.7)#tab_container.html | tab_container.html]]
**Css: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Tabbed/css modules/Pages/modules/Tabbed/css] 
**Scripts: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/Tabbed/scripts modules/Pages/modules/Tabbed/scripts] 
==tasks-roles==
This describes version 4.1.7.0 of the module Tasks and Roles (tasks-roles) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/TasksAndRoles  i2ce/modules/Pages/modules/TasksAndRoles ]
*Description: Provides administator interface to define tasks and role
*Requirements:
**[[iHRIS Module List (4.1.7)#pages | pages]] at least 4.1 and less than 4.2
*Paths:
**Configs: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/TasksAndRoles/configs modules/Pages/modules/TasksAndRoles/configs] 
**Templates: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/TasksAndRoles/templates modules/Pages/modules/TasksAndRoles/templates] <br/>[[iHRIS Template List (4.1.7)#roles_and_tasks_edit_role.html | roles_and_tasks_edit_role.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_edit_task.html | roles_and_tasks_edit_task.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_menu.html | roles_and_tasks_menu.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_view_all.html | roles_and_tasks_view_all.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_view_all_roles.html | roles_and_tasks_view_all_roles.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_view_all_roles_each.html | roles_and_tasks_view_all_roles_each.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_view_all_roles_no_edit.html | roles_and_tasks_view_all_roles_no_edit.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_view_all_tasks.html | roles_and_tasks_view_all_tasks.html]], [[iHRIS Template List (4.1.7)#roles_and_tasks_view_all_tasks_each.html | roles_and_tasks_view_all_tasks_each.html]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/Pages/modules/TasksAndRoles/lib modules/Pages/modules/TasksAndRoles/lib] <br/>[[Class: I2CE_Page_TasksAndRoles (4.1.7) | I2CE_Page_TasksAndRoles]]
==template-data==
This describes version 4.1.7.0 of the module Template Data (template-data) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData  i2ce/modules/TemplateData ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_TemplateData (4.1.7)| I2CE_Module_TemplateData]]
*Fuzzy Methods:
**Implements the method [[Class: I2CE_Page (4.1.7)#setDataTypePriority() | I2CE_Page->setDataTypePriority() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#setDataTypePriority() | setDataTypePriority()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setDataTypePriority() | I2CE_Template->setDataTypePriority() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#setDataTypePriority() | setDataTypePriority()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#setData() | I2CE_Page->setData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#setData() | setData()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#setData() | I2CE_Template->setData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#setData() | setData()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#getData() | I2CE_Page->getData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#getData() | getData()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#getData() | I2CE_Template->getData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#getData() | getData()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#getDefaultData() | I2CE_Page->getDefaultData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#getDefaultData() | getDefaultData()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#getDefaultData() | I2CE_Template->getDefaultData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#getDefaultData() | getDefaultData()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#removeData() | I2CE_Page->removeData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#removeData() | removeData()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#removeData() | I2CE_Template->removeData() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#removeData() | removeData()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#getDataNames() | I2CE_Page->getDataNames() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#getDataNames() | getDataNames()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#getDataNames() | I2CE_Template->getDataNames() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#getDataNames() | getDataNames()]]
**Implements the method [[Class: I2CE_Page (4.1.7)#ensureNode() | I2CE_Page->ensureNode() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#ensureNode() | ensureNode()]]
**Implements the method [[Class: I2CE_Template (4.1.7)#ensureNode() | I2CE_Template->ensureNode() ]] via [[Class: I2CE_Module_TemplateData (4.1.7)#ensureNode() | ensureNode()]]
*Description: A module that allows you to associate arbitray types of data to any node of the template DOM
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/modules modules/TemplateData/modules] <br/>[[#DisplayData |DisplayData]], [[#Options |Options]], [[#Tags |Tags]]
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/TemplateData/ modules/TemplateData/] <br/>[[Class: I2CE_Module_TemplateData (4.1.7) | I2CE_Module_TemplateData]]
==user==
This describes version 4.1.6.0 of the module User (user) 
*Source: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User  i2ce/modules/User ]
*Module Class: The module class is implemented by [[Class: I2CE_Module_User (4.1.7)| I2CE_Module_User]]
*Description: Provides Users
*Requirements:
**[[iHRIS Module List (4.1.7)#I2CE | I2CE]] at least 4.1 and less than 4.2
*Paths:
**Classes: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/lib modules/User/lib] <br/>[[Class: I2CE_Module_User (4.1.7) | I2CE_Module_User]], [[Class: I2CE_User (4.1.7) | I2CE_User]]
**Modules: [http://bazaar.launchpad.net/~intrahealth+informatics/i2ce/4.1.7-release/files/head:/modules/User/modules modules/User/modules] <br/>[[#RequestAccount-VerifyEmail |RequestAccount-VerifyEmail]], [[#UserAccess |UserAccess]], [[#UserAccess_DHIS |UserAccess_DHIS]], [[#UserAccess_LDAP |UserAccess_LDAP]], [[#UserAccess_LDAP_Hybrid |UserAccess_LDAP_Hybrid]], [[#UserAccess_Single |UserAccess_Single]]

[[Category:Developer Resources]]
