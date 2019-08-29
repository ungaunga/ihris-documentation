Guatemala Contracts Module Documentation Alt
============================================

Data Model
^^^^^^^^^^

<graphviz border='frame' format='png'>
 digraph "Contract Module" {
 
   phase_status_doc [label="phase_status_doc\nfile(FILE)\nnotes(MLINE)" shape=box]
   person [shape=box]
   person_position [shape=box]
   position [shape=box]
   salary [shape=box]
   contract [ shape=box]
   phase_status[shape=box]
   phase_status_decision [shape=box]
   phase_status_stage [shape=box]
   contract_status [shape=box]
   contract_type [shape=box]
   resolution [shape=box label="resolution\ndate(DATE_YMD)\nunidadejectora(MAP)\nfile(FILE)"]
   unidadejectora [shape=box]
   partida [shape=box label="partida\nyear"]
   partida_perm [shape=box label="partida_perm\nincremental counter"]

   person->person_position
   person_position->salary [color=red]
   person_position->position
   person_position->partida
   person_position->partida_perm
   position->contract
   contract->phase_status [color=red]
   contract->contract_type
   contract->contract_status
   contract->resolution
   resolution->unidadejectora
   partida->unidadejectora
   partida_perm->unidadejectora
   phase_status->phase_status_doc [color=red]
   phase_status->phase_status_stage
   phase_status->person [label=approver]
   phase_status->phase_status_decision
}
</graphviz>

