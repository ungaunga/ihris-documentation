Use Case:PR-WS-2
================

{{UseCasePage|Query for providers
 |number=PR-WS-2
 |description=ueries for HC Professional’s using a variety of possible parameter. This transaction returns a list of all professionals that match the criteria specified in the query parameters. Otherwise, if an error occurred, then an error is returned.
 |actor=Interoperability Layer,  Point Of Care Application?
 |preconditions=The application must be authenticated to the system 
 |success=An list of enterprise ids (EIDs) is returned to the requesting application
 |resources=[[Web Service:PR-WS-2]]
 |mss=

* The actor submits a request with a given query parameters
* The system returns a list of matching EIDs
 |extensions=
:2.a The system does not find the provider and returns an error code.
:2.b The requested search parameters are invalid and returns an error code.
 |notes=Not needed for Sept. 2012
}}
