Web Service:PR-WS-2
================================================

{{WebServicePage|Query For Providers
 |number=PR-WS-2
 |description=Fetches a HC Professional Enterprise ID for the professional specified by the professional ID parameter.
 |applications=Interoperability Layer, Point-Of-Care?
 |url=/ws/rest/v2/query/providers
 |params=The following query parameters are allowed:


* ${size} The maximum number number of EPIDs to return.  Defaults to 50.
* ${start} The starting offset for listing EPIDs.  Defaults to 10.
* The following search possible parameters will be "and"ed together
* *${firstname} The provider's  given name.
* *${surname} The professional’s family name.
* *${fosaid} The FOSAID for the facility a provider is posted to.
* *${location} The code for the organizational unit under which the provider is posted.
* *${category} The category (or cadre) of the provider.
* *${type} The type of the provider 'PPS' for paid-public sector or 'CHW' for community health worker.
* {format}The response format.  One of 'hl7' or 'json'.
 |example=?foasid=123&size=2&start=10
 |response=HTTP 200 - OK
The HTTP response body will contain a list of matching EIDSs as specified by the ${format} parameter:


* If ${format}=json.  Example:
{
     providers: {
       211312: {
         providerDetails : 'http://rhea-pr.ihris.org/webservices/details/provider?epid=211312',
         editProvider : 'http://rhea-pr.ihris.org/webservices/edit/provider?epid=211312',
         addPost : 'http://rhea-pr.ihris.org/webservices/add/post?epid=211312',
         queryPosts : 'http://rhea-pr.ihris.org/webservices/details/post?epid=211312',
         viewProvider : 'http://rhea-pr.ihris.org/providerregistry/view?id=person%7C23123123
       },
       131241241: {
         providerDetails : 'http://rhea-pr.ihris.org/webservices/details/provider?epid=131241241',
         editProvider : 'http://rhea-pr.ihris.org/webservices/edit/provider?epid=131241241',
         addPost : 'http://rhea-pr.ihris.org/webservices/add/post?epid=131241241',
         queryPosts : 'http://rhea-pr.ihris.org/webservices/details/post?epid=131241241',
         viewProvider : 'http://rhea-pr.ihris.org/providerregistry/view?id=person%7C31234
       },
     },
     total_size : 300,
     start: 10
}


* ${format}=hl7. one per professional that matches the criteria, that contains the details of that professional. These messages will be contained within a RSS feed XML message. HL7v2 message specification and mapping:
* * The RSS XML will contain a list of HL7 message in each item element.   See `QueryProfessionalRSS.xml <http://www.google.com/url?q=http%3A%2F%2Fjira.jembi.org%2Fwiki%2Fdownload%2Fattachments%2F8912902%2FQueryProfessionalRSS.xml&sa=D&sntz=1&usg=AFQjCNEYi8ytZRJPvq8fWsoqQ1VqAToIAg>`_
* * The HL7 v2.5 PMU_B01 messages for each professional will be specified as in  `Register-or-Query-Professional <https://docs.google.com/spreadsheet/ccc?key=0Ah8KVMJr8h4pdFlQMjNyMDh0dzhUSlJkWVgyd3lUZGc>`_
 |error=*HTTP 500 - Server Error - If the server encountered an error.


* HTTP 400 - Bad Request - If the parameters are malformed.
 |notes=Need to good way for limiting response length.  See **A collection: the list of bugs** in the `Launchpad API <https://help.launchpad.net/API/Hacking>`_
 |resources=[[Use Case:PR-WS-2]]
}}
