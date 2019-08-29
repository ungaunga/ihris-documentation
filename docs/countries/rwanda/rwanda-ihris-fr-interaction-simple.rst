Rwanda iHRIS FR Interaction Simple
==================================


Transaction Diagram: Simple
^^^^^^^^^^^^^^^^^^^^^^^^^^^

<graphviz border='frame' format='png'>
 digraph "iHRIS + Facility Registry for Rwanda" {
 
   ihris [label="iHRIS\n(Care Services Finder)" shape=box]
   fr [label="Facility Registry\n(Care Services Directory)" shape=box]


   ihris->fr [label="getModificationsRequest"]

}
</graphviz>



[[Category:Rwanda]]
