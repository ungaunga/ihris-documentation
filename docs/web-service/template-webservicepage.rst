Template:WebServicePage
=======================

__NOEDITSECTION__
{{WebService|{{#ifexist: Web Service:{{{number}}} |  [[Web Service:{{{number}}} | {{StripWhitespace|{{{1}}}}}]] |  {{StripWhitespace|{{{1}}}}} }}
 |number={{{number}}}
 |description={{{description}}} 
 |url={{{url}}}
 |params={{{params}}}
 |response={{{response}}}
 |error={{{error}}}
 |example{{#ifeq:{{{example|+}}}|{{{example|-}}}||example_dummy}}={{{example}}} 
 |postparams{{#ifeq:{{{postparams|+}}}|{{{postparams|-}}}||postparams_dummy}}={{{postparams}}} 
 |postreponse{{#ifeq:{{{postresponse|+}}}|{{{postresponse|-}}}||postresponse_dummy}}={{{postresponse}}} 
 |posterror{{#ifeq:{{{posterror|+}}}|{{{posterror|-}}}||posterror_dummy}}={{{posterror}}} 
 |postexample{{#ifeq:{{{postexample|+}}}|{{{postexample|-}}}||postexample_dummy}}={{{postexample}}} 
 |notes{{#ifeq:{{{notes|+}}}|{{{notes|-}}}||notes_dummy}}={{{notes}}} 
 |resources{{#ifeq:{{{resources|+}}}|{{{resources|-}}}||resources_dummy}}={{{resources}}} 
}}


