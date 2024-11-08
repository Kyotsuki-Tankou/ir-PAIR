from schemaGen import schema_prompt

def promptgen(type):
    nl="\\n"
    #---basic---
    basic1="You are an expert in extracting items from a paper professionally and precisely. "
    basic2="Please summarize [input] and extract items corresponding to [schema] or return empty list. 

    basic=basic1+basic2+nl

    #---schema--- 
    schema1="###schema###"+nl
    schema2=schema_prompt(type)
    schema=schema1+schema2
    