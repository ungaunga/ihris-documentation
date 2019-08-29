Web Service:PR-WS-9
===================

{{WebServicePage|Edit a Post
 |number=PR-WS-9
 |description=Edit details on existing post
 |applications=Interoperability Layer, Point-Of-Care, iHRIS 
 |url=/ws/rest/v2/edit/post
 |params=The following webservice should accept the following parameters:

* ${type} The type of the post.  One of 'PPS' for Paid-Public Sector or 'CHW' for Community Health Worker. Required.
* ${category} The category/cadre of the providerm e.g. Nurse, Doctor. Optional.
* ${foasid} The facility code for this posting. Optional.
* ${orgunit} The organizational unit for this posting.  Optional.
* ${startdate}  The date the post is in effect.  Format is 'YYYY-mm-dd'. Optional.
* ${enddate}  The date the post is no longer in effect.  Format is 'YYYY-mm-dd'. Optional.
* ${respformat}  Describes response format. Optional. Default is 'http', can also be 'json.'
 |example=?category=NURSE&type=PPS&fosaid=12312&orgunit=2133
 |response=HTTP 200 - OK

* If ${repsformat} is 'http' the HTTP response body will contain the id as plain text of the editied posting
* If ${respformat} is 'json' it will contain a JSON object with the field 'id' of the editedpost as well as the URLs to access for further web-service actions to perform on the post.
{
     id: 211312,
     actions: {
       editPost: 'http://rhea-pr.ihris.org/webservices/edit/post?id=992312',
       postDetails: 'http://rhea-pr.ihris.org/webservices/details/post?id=992312',
       viewPost: 'http://rhea-pr.ihris.org/providerregistry/post?id=post%7C992312',       
     } 
}
 |error=*HTTP 500 - Server Error - If the server encountered an error.

* HTTP 400 - Bad Request - If the parameters are malformed.
 |notes= 
|resources=[[Use Case:PR-WS-9]]
}}
