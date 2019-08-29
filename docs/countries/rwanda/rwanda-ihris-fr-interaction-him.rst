Rwanda iHRIS FR Interaction HIM
===============================


==Transaction Diagram: With OpenHIM==

<graphviz border='frame' format='png'>
 digraph "iHRIS + Facility Registry for Rwanda" {
 
   ihris [label="iHRIS\n(Care Services Finder)" shape=box]
   fr [label="Facility Registry\n(Care Services Directory)" shape=box]
   him [label="OpenHIM\n(Access Control)" shape=box]

   ihris->him [label="getModificationsRequest"]
   him->fr [label="pass-thru getModificationsRequest"]

}


</graphviz>

[[Category:Rwanda]]
