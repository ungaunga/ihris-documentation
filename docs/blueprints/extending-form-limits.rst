Extending Form Limits
=====================

*rework generateLimit() so that allows for adding in new operators types.
*Hook in COMPARE operator to generateLimit() to make comparisons for form fields to be used in limits
**Example: 'form+start_year' lessThan 'form+end_year' will cause the following code to be executed:
***$start_date->COMPAREAS_lessthan_TO_I2CE_FormField_YEAR($end_date) -- will not exist
***$start_date->COMPAREAS_lessthan_TO_I2CE_FormField_DB_DATE($end_date) -- will exist and return true/false
**In otherwords ($class = get_ COMPAREAS_$operator_TO_$class where $class runs over parent cass of end_date



*allow for general binary (or n-ary) operations among form fields where the result is another form field to be used in limit clauses.  such as
**$end_date->OPERATOR_minus_DB_DATE($start_date)
**$start_salary->OPERATOR_plus_CURRENCY($end_salary)
*allow for "parametrized" 1-ary operations for form fields such as:
**$start_date->next_year()  (no parameters )  -- returns class of $start_date
**$start_date->increment_ymd($y,$m,$d)  (3 paramaters) -- returns class of $start_date
**$start_date->increment_year($y) (1 paramater) -- returns class of $start_date
**$start_date->increment_time($h,$m,$s) -- returns class of $start_date
**$start_date->increment_hour($h) -- returns class of $start_date
**$salary->divide($divisor) -- returns CURRENCY
**$salary->multiply($factor)-- returns CURRENCY
*allow for constant-like form fields in limiting values such as:
**DB_DATETIME::now() -- returns DATE_TIME
**DB_YEAR::next_year() -- returns DATE_YEAR
**DB_YMD::next_year() -- returns DATE_YMD

[[Category:Blueprints]]
