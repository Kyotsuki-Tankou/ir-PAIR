from testGen import read_file_content,shuffle_file,input_gen
from utils import askAI,refine,compare_output,last
import os
import json

"""
param:
model（从强到弱）<- glm-4-plus / glm-4-airx / glm-4-flash
n_values: CoT数量
"""
def rundemo(model="glm-4-plus",n_values=2):
    print("这是一个demo，但是调API有点烧钱，请省着点用或者把模型换成flask")
    print("API会在2024.11.20失效")
    print("请将输入文本放置在demo/abstract.txt中，完毕后输入任意字符。")
    input()
    
    filepath="./demo/"
    filename="abstract.txt"
    if "abstract.txt" not in os.listdir(filepath):
        print("请确认是否存在输入")
        
    file=open(filepath+filename,encoding="utf-8")
    abstract=file.read()
    types=["species","tissues","organ_parts","technologies","disease","type"]
    output=dict()
    for i in range(len(types)):
        print(f"正在获取：{types[i]}")
        input_str=input_gen(abstract=abstract,type=types[i],n_value=n_values)
        res=askAI(input_str,model=model)
        refined=refine(res)
        lastword=last(refined)
        if lastword=="ERROR":
            print("-----------")
            print("ERROR in type=",types[i])
            print("with output",lastword)
            print("-----------")
            output[types[i]]=[]
        else:
            try:
                output[types[i]]=eval(lastword)
            except:
                print("-----------")
                print("ERROR in type=",types[i])
                print("with output",lastword)
                print("-----------")
                output[types[i]]=[]
            print(f"type:{types[i]}, return:{lastword}")
    json_data=json.dumps(output,indent=4)
    with open('./demo/output.json',"w") as js:
        js.write(json_data)
    print("生成完毕，文件位于demo/output.json")
    return json_data
    
    # print(abstract)
    
if __name__=="__main__":
    rundemo(model="glm-4-plus")
