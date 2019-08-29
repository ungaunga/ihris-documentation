Use Case:PR-WS-1
================

{{UseCasePage|Query from a provider’s enterprise ID 
 |number=PR-WS-1
 |description=This query takes in a unique ID for a provider and returns the enterprise ID associated with the provider who matches the given ID.
 |actor=Interoperability Layer, potentially Point Of Care Application
 |preconditions=The application must be authenticated to the system 
 |success=An enterprise id (EID) is returned to the requesting application
 |resources=[[Web Service:PR-WS-1]]
 |mss=
#The actor submits a request with a given ID type and ID number
#The system returns the EID
 |extensions=
:2.a The system does not find the provider and returns an error code.
}}
