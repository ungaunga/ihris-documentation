Web Service:PR-WS-3
===================

{{WebServicePage|Get Provider Detail
 |number=PR-WS-3
 |description=Fetches details of a provider by their EPID or other identification type.
 |applications=Interoperability Layer, Point-Of-Care? Facility Registry?
 |url=/ws/rest/v2/details/provider
 |params=This contains the followng parameters to identify the provider whose details we shall return:
$epid.  The providers EPID.  Required.


* ${format}The response format. One of 'json' or 'hl7'.  Defaults to 'json',
 |
 |response=*HTTP 200 - OK


* For HL7  See  `QueryProfessionalRSS.xml <http://www.google.com/url?q=http%3A%2F%2Fjira.jembi.org%2Fwiki%2Fdownload%2Fattachments%2F8912902%2FQueryProfessionalRSS.xml&sa=D&sntz=1&usg=AFQjCNEYi8ytZRJPvq8fWsoqQ1VqAToIAg>`_
* * The HL7 v2.5 PMU_B01 messages for each professional will be specified as in   `Register-or-Query-Professional <https://docs.google.com/spreadsheet/ccc?key=0Ah8KVMJr8h4pdFlQMjNyMDh0dzhUSlJkWVgyd3lUZGc>`_
* For JSON we return an associative array containing the provider's details as well as URLs related to various actions to perform on the provider:
{
  firstname: "Bill",
  surname:  "Smith",
  cadre: "Nurse",
  email: "bsmith@example.org",
  passport: "12312312",
  mutuelle: "123123444",
  csr:  "123123",
  nid:  "333",
  actions: {
    providerDetails: 'http://rhea-pr.ihris.org/webservices/details/provider?epid=211312',
    editProvider: 'http://rhea-pr.ihris.org/webservices/edit/provider?epid=211312',
    addPost: 'http://rhea-pr.ihris.org/webservices/add/post?epid=211312',
    queryPosts: 'http://rhea-pr.ihris.org/webservices/details/post?id=211312',
    viewProvider: 'http://rhea-pr.ihris.org/providerregistry/view?id=person%7C23123'
  }
}
 |error=*HTTP 500 - Server Error - If the server encountered an error.


* HTTP 400 - Bad Request - If the parameters are malformed.
 |resources=[[Use Case:PR-WS-3]]
}}
