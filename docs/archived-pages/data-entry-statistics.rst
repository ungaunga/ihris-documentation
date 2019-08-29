Data entry statistics
=====================

This article is deprecated.

All data entry and changes for forms with the "entry" form storage mechanism are tracked.  However, there is no web interface to look at this data.  Instead, we suggest that you run specialized SQL queries in phpmyadmin.  

We give some examples below

==Tables==
The following tables are relevant for making these queries:
===user===
This table contains a list of usernames and ids.  The user's id is what is used to record data changes.  Example is:
<pre>
id 	username 	password 	firstname 	lastname 	email 	                        creator
4      cleitner 	XXXXX 	        Carl 	        Leitner 	cleitner@intrahealth.org 	2
</pre>
====Lookup id by user name====
<source lang='sql'>
SELECT id FROM `user` WHERE username='cleitner'
</source>
which will return '4'.

===form===
This table is used to associate a numeric id to every form stored in the entry tables.  Example is:
<pre>
id      name            type
1 	marital_status 	0
2 	person 	        0
</pre>
====Lookup if by form name====
<source lang='sql'>
SELECT id FROM `form` WHERE name='person'
</source>
will return '2'
===record===
This table is used to track new instances of all forms stored in the entry form storage mechanism.
===entry===
This table is used to record all edits to all forms stored in the entry form storage mechanism.

==Data Entry Queries==
===How many new person records added===
Suppose we want to get the number new people (e.g. new person forms)  added since May 22, 2012 we would do something like:
<source lang='sql'>
SELECT count(*) FROM `record` WHERE 
form = (select id from form where name='person')
AND
last_modified >= '2012-05-22 00:00:00'
</source>
===How many person records have person edited===
Suppose we want to get the number person forms haven been modified added since Jan 1, 2012 we would do something like:
<pre>
SELECT count(distinct(record)) FROM `entry` 
WHERE 
record in (select id from record where form = (select id from form where name='person'))
AND
date >= '2012-01-01 00:00:00'
</pre>
Note:  this does not include changes to child forms of the person form , such as the person_position_form.

===How many records have been edited by a user===
Suppose we want to get the number new people (e.g. new person forms)  added since Jan 1, 2012 by the user cleitner we would do something like:
<pre>
SELECT count(distinct(record)) FROM `entry` 
WHERE 
date >= '2012-01-01 00:00:00'
AND
who = (select id from user where username='cleitner' )
</pre>

===How many person records have been edited by a user===
Suppose we want to get the number new people (e.g. new person forms)  added since Jan 1, 2012 by the user cleitner we would do something like:
<pre>
SELECT count(distinct(record)) FROM `entry` 
WHERE 
record in (select id from record where form = (select id from form where name='person'))
AND
date >= '2012-01-01 00:00:00'
AND
who = (select id from user where username='cleitner' )
</pre>

Note:  this does not include changes to child forms of the person form , such as the person_position form.

===How many person or person_position records have been edited by a user===
Suppose we want to get the number person forms haven been modified added since Jan 1, 2012 we would do something like:
<pre>
SELECT count(distinct(record)) FROM `entry` 
WHERE 
record in (select id from record where form in (select id from form where name='person' or name='person_position'))
AND
date >= '2012-01-01 00:00:00'
AND
who = (select id from user where username='cleitner' )
</pre>
[[Category:Archived Pages]]
