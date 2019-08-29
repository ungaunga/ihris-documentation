Guatemala Contracts Module Documentation Alt3
=============================================

<graphviz border='frame' format='png'>
 digraph "Contract Module" {
 
 
   person [shape=box]
   person_partida_perm [shape=box]
   partida_perm [shape=box label="partida_perm\nincremental counter"]
   person_position [shape=box]
   job [shape=box]
   salary [shape=box]
   contract [ shape=box]
   position [shape=box]
   phase_status[shape=box]
   phase_status_decision [shape=box]
   phase_status_stage [shape=box]
   contract_status [shape=box]
   contract_type [shape=box]
   resolution [shape=box label="resolution\ndate(DATE_YMD)\nunidadejectora(MAP)\nfile(FILE)"]
   unidadejectora [shape=box]
   partida_temp [shape=box label="partida_temp\nyear"]
   phase_status_doc [label="phase_status_doc\nfile(FILE)\nnotes(MLINE)" shape=box]

   person->person_position [color=red]
   person->person_partida_perm [color=red]
   person_position->salary [color=red]
   person_position->position
   person_partida_perm->partida_perm
   contract->partida_temp
   position->job
   partida_perm->job
   person_position->contract [color=red]
   contract->phase_status [color=red]
   contract->contract_type
   contract->contract_status
   contract->resolution
   resolution->unidadejectora
   partida_temp->unidadejectora
   partida_perm->unidadejectora
   phase_status->phase_status_doc [color=red]
   phase_status->phase_status_stage
   phase_status->person [label=approver]
   phase_status->phase_status_decision
}
</graphviz>

