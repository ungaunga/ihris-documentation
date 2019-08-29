Web Service:PR-WS-7
===================

{{WebServicePage|Get Post Details     
 |number=PR-WS-7
 |description=Show details of a provider's post
 |applications=Interoperability Layer, Point-Of-Care?
 |url=/ws/rest/v2/details/post
 |params=The following query parameters are allowed:
*${id} The id of the post
*{format}The response format.  One of 'json', ?'hl7'?
 |example=?id=12312321312
 |response=HTTP 200 - OK
Example:
{
     type: 'PPS',  #One of PPS or CHW
     category: 'NURSE', 
     fosaid: '012321',
     orgunit: '197834',
     startdate: '1992-12-22'  #year, month, day
     actions: {
        postDetails: 'http://rhea-pr.ihris.org/webservices/details/post?id=211312',
        editPost: 'http://rhea-pr.ihris.org/webservices/edit/post?id=211312'
     }
}
 |error=*HTTP 500 - Server Error - If the server encountered an error.
*HTTP 400 - Bad Request - If the parameters are malformed.
 |notes=Need to good way for limiting response length.  See '''A collection: the list of bugs''' in the [https://help.launchpad.net/API/Hacking Launchpad API]
 |resources=[[Use Case:PR-WS-7]]
}}
