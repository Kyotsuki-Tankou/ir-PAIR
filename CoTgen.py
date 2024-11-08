from schemaGen import schema_prompt
from utils import askAI,refine
import os
#---abstract---
#---keywords---
#---verify---
#---content---
#---conclusion---
#---result---
nl="\\n"

def cotgen(abstract,type,res,isres=True):
    #positive
    #---basic---
    basic1="You are an expert in extracting items from a paper professionally and precisely. "
    basic2="Please summarize [input] and extract items corresponding to [schema] or return empty list."
    cot1='You need to answer with "Keywords", "Verify", "Conclusion" and "Result" step by step. '
    cot2='If the answer in "Keywords" and "Verify" are not the same, it is required to find more clues from the context and append "Context" part before drawing a "Conclusion".'
    cot2+='Now I will give you three examples about its.'
    basic=basic1+basic2+cot1+cot2+nl
    #---CoT---
    with open('./cases/CoTpos.txt',encoding='utf-8') as f:
        prompt=f.read().replace('\n','\\n')
    basic3=nl+"Now I will give you the schema, input and result, please give the Keywords, verify ,context(if requied) and conclusion."+nl
    schema1=schema_prompt(type)
    basic4="###input###"+nl
    basic5="###result###"+nl
    if isres:
        output=basic+prompt+basic3+schema1+basic4+abstract+basic5+res+"Let's think step by step."+nl
    else:
        output=schema1+basic4+abstract+"Let's think step by step."+nl
        output=output.replace("\\n","\n")
    return output


filepath="./abstract/"
types=["species","tissues","organ_parts","technologies","disease","type"]
cnt=0
for root,dir,files in os.walk(filepath):
    for file in files:
        # if not (file.startswith("2")  or file.startswith("30")):
        if file.startswith("2")  or file.startswith("30"):
            # print(os.path.join(root,file))
            lines=[]
            with open(os.path.join(root,file),encoding='utf-8') as f:
                for line in f:
                    lines.append(line.strip('\n'))
                species=lines[0]
                tissues=lines[1]
                organ_parts=lines[2]
                technologies=lines[3]
                disease=lines[4]
                abstract=lines[5]
                for i in range(5):
                    cnt+=1
                    file1=open("./CoTs/"+str(cnt)+".txt","w",encoding='utf-8')
                    res=cotgen(abstract,types[i],lines[i])
                    # print(res)
                    ret=askAI(res)
                    refined=refine(ret)
                    newres=cotgen(abstract,types[i],lines[i],isres=False)
                    print(newres+refined,file=file1)
                    print(cnt)
                    # print(refine(ret))
                    # exit()
                    