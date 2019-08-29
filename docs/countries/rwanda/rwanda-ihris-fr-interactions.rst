Rwanda iHRIS FR Interactions
============================




Transaction Diagram: With InfoMan
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

<graphviz border='frame' format='png'>
 digraph "iHRIS + Facility Registry for Rwanda" {
 
   ihris [label="iHRIS\n(Care Services Finder)" shape=box]
   fr [label="Facility Registry\n(Care Services Directory)" shape=box]
   him [label="OpenHIM\n(Access Control)" shape=box]
   infoman [label="InfoManager\n(caching)" shape=box]


   ihris->him [label="Facility Search"]
   him->infoman [label="pass-thru Facility Search"]
   infoman->fr [label="getModificationsRequest"]

}
</graphviz>



