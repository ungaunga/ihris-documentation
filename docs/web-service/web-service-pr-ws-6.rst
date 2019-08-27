Web Service:PR-WS-6
================================================

{{WebServicePage|Edit a Provider
 |number=PR-WS-6
 |description=Edit Provider Details
 |applications=Interoperability Layer, Point-Of-Care, iHRIS
 |url=/ws/rest/v2/edit/provider
 |params=The following webservice should accept the following parameters:


* ${epid} The EPID of the provider. Required.
* ${surname} The surname of the provider. Optional.
* ${nationality}  The nationality of the provider coded according to ISO-3166-1 alpha-3.  Optional.
* ${nid} The national id. Optional.
* ${passport} The passport number.  Optional.
* ${mutuelle} The mutuelle number. Optional.
* ${csr} The CSR number. Optional.
* ${respformat}  Describes response format. Optional. Default is 'http', can also be 'json.'
 |example=?provder=m&reg_body=2
 |response=HTTP 200 - OK


* If ${repsformat} is 'http' the HTTP response body will contain the epid as plain text.
* If ${respformat} is 'json' it will contain a JSON object with the single field 'epid.'
further web-service actions to perform on the provider
  Example:
{
     epid: 211312,
     actions: {
      providerDetails: 'http://rhea-pr.ihris.org/webservices/detials/provider/byid?id_num=211312',
      editProvider: 'http://rhea-pr.ihris.org/webservices/edit/provider?epid=211312',
      addPost: 'http://rhea-pr.ihris.org/webservices/add/post?epid=211312',
      queryPosts: 'http://rhea-pr.ihris.org/webservices/query/posts?epid=211312',
      viewProvider: 'http://rhea-pr.ihris.org/providerregistry/view?id=person%7C23123'
    } 
}
 |error=*HTTP 500 - Server Error - If the server encountered an error.


* HTTP 400 - Bad Request - If the parameters are malformed.
 |notes= 
|resources=[[Use Case:PR-WS-6]]
}}
