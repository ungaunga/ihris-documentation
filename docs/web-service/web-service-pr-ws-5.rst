Web Service:PR-WS-5
===================

{{WebServicePage|Add a Provider
 |number=PR-WS-5
 |description=Add Provider Details
 |applications=Interoperability Layer, Point-Of-Care, iHRIS 
 |url=/ws/rest/v2/add/provider 
 |params=The following webservice should accept the following parameters:
*${firstname} The first name of the provider. Required. 
*${surname} The surname of the provider. Required.
*${nationality}  The nationality of the provider coded according to ISO-3166-1 alpha-3.  Required.
*${nid} The national id. Required.
*${passport} The passport number.  Optional.
*${mutuelle} The mutuelle number. Optional.
*${csr} The CSR number. Optional.
*${respformat}  Describes response format. Optional. Default is 'http', can also be 'json.' 
 |example=?firstname=Bill&surname=Smith&nationality=RW&nid=12312342
 |response=HTTP 200 - OK
*If ${repsformat} is 'http' the HTTP response body will contain the epid as plain text of the newly created provider. 
*If ${respformat} is 'json' it will contain a JSON object with the field 'epid' of the newly created provider as well as the URLs to access for further web-service actions to perform on the provider.   
{
     epid: 211312,
     actions: {
       providerDetails: 'http://rhea-pr.ihris.org/webservices/details/provider?epid=211312',
       editProvider: 'http://rhea-pr.ihris.org/webservices/edit/provider?epid=211312',
       addPost: 'http://rhea-pr.ihris.org/webservices/add/post?epid=211312',
       queryPosts: 'http://rhea-pr.ihris.org/webservices/details/post?id=211312',
       viewProvider: 'http://rhea-pr.ihris.org/providerregistry/view?id=person&#124;23123'
     } 
}
 |error=*HTTP 500 - Server Error - If the server encountered an error.
*HTTP 400 - Bad Request - If the parameters are malformed.
 |notes= 
|resources=[[Use Case:PR-WS-5]]
}}
