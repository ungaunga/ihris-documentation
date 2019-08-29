Template:UseCasePage
====================

__NOEDITSECTION__
{{UseCase|{{#ifexist: Use Case:{{{number}}} |  [[Use Case:{{{number}}} | {{StripWhitespace|{{{1}}}}}]] |  {{StripWhitespace|{{{1}}}}} }}
 |number={{{number}}}
 |description={{{description}}} 
 |actor={{{actor}}} 
 |preconditions={{{preconditions}}}
 |success={{{success}}}
 |mss={{{mss}}}
 |stakeholders{{#ifeq:{{{stakeholders|+}}}|{{{stakeholders|-}}}||stakeholders_dummy}}={{{stakeholders}}} 
 |extensions{{#ifeq:{{{extensions|+}}}|{{{extensions|-}}}||extensions_dummy}}={{{extensions}}} 
 |notes{{#ifeq:{{{notes|+}}}|{{{notes|-}}}||notes_dummy}}={{{notes}}} 
 |resources{{#ifeq:{{{resources|+}}}|{{{resources|-}}}||resources_dummy}}={{{resources}}} 
}}


