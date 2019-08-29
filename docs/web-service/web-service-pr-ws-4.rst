Web Service:PR-WS-4
===================

{{WebServicePage|Query For Postings
 |number=PR-WS-4
 |description=Fetches details of a provider's postings by their EPID.
 |applications=Interoperability Layer, Point-Of-Care, Facility Registry, iHRIS
 |url=/ws/rest/v2/query/posts
 |params=This contains the following parameters to identify the provider whose details we shall return.  The values of epid, foasid and orgunit are "and"ed together:
*${epid} The provider's EPID. Optional.
*${fosaid} The facility code.  Optional.
*${orgunit} The code for the organizational unit for the posting.  Optional
*${type} The type of the provider, one of PPS or CHW. Optional.
*${category} The category/cadre of the provider.  Optional.
*${format}The response format.  One of 'hl7' or 'json'
*${size} The maximum number number of IDs to return.  Defaults to 50.
*${start} The starting offset for listing IDs.  Defaults to 10. 
 |response=*HTTP 200 - OK
*If the format='hl7' .....
*If the format='json' we return an array of associative arrays.  The associative arrays have keys for the post attributes.  For example:
{ 
  total_size : 2,
  start: 0,
  posts: {
    98798798 : {
       editPost: http://rhea-pr.ihris.org/webservices/edit/post?id=98798798',
       postDetails: http://rhea-pr.ihris.org/webservices/details/post?id=98798798'
    },
    9878799 : {
       editPost: http://rhea-pr.ihris.org/webservices/edit/post?id=98798799',
       postDetails: http://rhea-pr.ihris.org/webservices/details/post?id=98798799'
    }
   }
}
 |error=*HTTP 500 - Server Error - If the server encountered an error.
*HTTP 400 - Bad Request - If the parameters are malformed.
 |resources=[[Use Case:PR-WS-4]]
}}
