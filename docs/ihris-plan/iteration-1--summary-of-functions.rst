Iteration 1: Summary of Functions
=================================

We are planning to base the first iteration of iHRIS Plan on John Dewdney's model as presented at the Workforce Planning Model Workshop. The Excel spreadsheet version can be downloaded [http://pcwww.liv.ac.uk/~martinea/hrtools/Dewdney%20demonstration%20Workforce%20Model-Organisation.xls here]. This will be a simple proof-of-concept version of the workforce planning software; later more complex features of the Hall/Hornby models can be added. 

The following is a summary of the functions of Iteration 1 based on the John Dewdney model. This is a summary of the use cases for the software, which are posted on the [http://www.capacityproject.org/hris/suite/ihris_plan.php iHRIS Plan Project Page]. Please feel free to clarify any step, comment on these functions and make suggestions for improving them.


== Target and Demographics ==

# Enter a '''target''' for the projection. ''Note: This is just a text field and doesn't affect any calculations.''
# Enter the '''starting year''' for the projection. ''Note: This should be the most recent year for which there are known data as to the health workforce and pre-service training supply.''
# Enter '''the number of years''' to project. ''Note: This model does not take into account differences between short-term and long-term projections. The number of years can be capped. See [[Questions for Discussion]] #2.''
# Enter the '''population''' at the start of the starting year.
# Enter the '''annual average population growth rate'''.

== Assumptions ==

# Select a '''cadre''' for projections. ''Note: Multiple projections can be created, one for each cadre. All data that follow pertain to the selected cadre for the projection. See [[Questions for Discussion]] #1.''
# Enter the normal '''age of retirement'''. ''Note: Unless ages of health workers are entered as supply data, projections based on retirement age cannot be made. See [[Questions for Discussion]] #10.''
# Enter the expected '''average annual rate of retirement''', for projecting annual losses due to retirement. 
# Enter the expected '''average annual rate of attrition due to illness, injury or death''', for projecting annual losses due to these factors.
# Enter the expected '''average annual rate of attrition due to other factors''', for projecting additional annual losses. ''See [[Questions for Discussion]] #3.''
# Enter the expected '''average percentage of training intake not expected to be available for service''', e.g., due to failure to complete training, for projecting annual losses of pre-service trainees.
# Enter the '''duration of the pre-service training course in years'''. ''Note: This determines how many years actual graduate numbers must be entered at the beginning of the projection period.''

== Requirements ==

# Enter the '''target number of positions''' to be filled in the starting year. ''See [[Questions for Discussion]] #4.'' 
# Calculate the required positions needed for each year in the projection. ''Note: It is not clear how this calculation is made. It can be calculated if based on a standard of total population per position. See [[Questions for Discussion]] #5.''

== Supply: Pre-Service Training ==

# Enter the '''number of new students and the number of re-enrollments''' for the starting year to calculate the total number of students.
# Enter the '''number of graduates''' for the starting year (i.e., for the first 3 years for a 3-year course).
# Enter the '''new student intake''' for each year in the projection. ''Note: There should be a way to enter an assumption and calculate this automatically, but there does not seem to be one in the Dewdney model. See [[Questions for Discussion]] #6.''
# From these data and the pre-service training loss assumption, the system can calculate total number of graduates who go on to enter service (total enrollment of previous year - continuing students and pre-service training losses).

''Note: These calculations for pre-service training, specifically with regard to length of training course, are still unclear to me. Please comment and clarify as needed.''

== Supply: Workforce ==

# Enter the '''number of staff actually employed''' at the start of the year. ''See [Questions for Discussion]] #7, 9 and 10.''
# To determine the year-by-year projected supply, the system calculates the total intake from training and the total exits from staff leaving due to retirement, staff leaving due to illness/death and staff leaving due to other factors. Add the annual intake to and subtract the annual losses from the first-year supply to calculate the next year's supply, and so on for each year in the projection. ''Note: However, the model doesn't seem to account for intakes other than from graduating students; see [[Questions for Discussion]] #8 and 11.''

Now the system can produce a base projection model comparing the year-by-year projected supply of health workers to the year-by-year projected requirements, helping workforce planners visualize the gaps between the two.

== Costs ==

# Enter the '''annual cost of training''' per student.
# Enter the '''average annual salary''' of a health worker.
# The system can calculate the total costs of all students and workers for each year in the projection. ''Note: And also for required positions, although this does not seem to be in the original model; see [[Questions for Discussion]] #12.

== Interventions ==

By changing the assumptions entered, the system can graph the effects of various interventions, either individually or aggregated. For example, changing the assumed retirement rate may be due to an intervention in encouring more retirements or raising the retirement age. The more assumptions that are used, the more interventions can be modeled. This wouldn't change the base assumptions entered used to make the projection, which are presumed to be based on actual data, but would rather be used to posit 'what-if' scenarios, such as "What if pre-service training losses were decreased by some sort of incentive program?"

== Reporting, Planning and Analysis ==

The system should be able to produce a variety of reports based on the data entered. As more cadre projections are created, reports can be aggregated to create a total picture of the health workforce. Here are some examples of reports that can be created:

* Total projected supply on a per-year basis by cadre or aggregated for each year in the projection
* Total projected requirements on a per-year basis by cadre or aggregated for each year in the projection
* Population growth over the projection
* Compare population per position to population per actual health worker
* Actual number of staff increase/decrease and required positions increase/decrease over the term of the projection
* Number of projected staff gains and losses for each year in the projection
* Number of pre-service training student intakes, losses and graduates for each year in the projection
* Annual training and salary projected costs and per-year increase or decrease in projected costs

In addition, the system should generate a workforce plan template similar to the one in the Dewdney model that includes data from the projections.

Once another year of actual data has been collected, that can be entered into the system and compared to the original projection to analyze the accuracy of the projection and make adjustments. ''See [[Questions for Discussion]] #13.''
[[Category:iHRIS Plan]]
