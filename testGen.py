from utils import askAI,refine,compare_output,last
from schemaGen import schema_prompt
import os
import random

def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def shuffle_file(n_value=2):
    ret=""
    cases_folder = "./CoTs/"
    all_files = [f for f in os.listdir(cases_folder) if os.path.isfile(os.path.join(cases_folder, f))]
    # print(all_files)
    if len(all_files) < 2:
        print("The folder does not contain enough files.")
        return

    selected_files = random.sample(all_files, n_value)

    for file_name in selected_files:
        file_path = os.path.join(cases_folder, file_name)
        content = read_file_content(file_path).replace("### Keywords ###","Let's think step by step.\n ### Keywords ###")
        ret=ret+content
        # print(content)
    return ret

# shuffle_file()

def input_gen(abstract,type,n_value=2):
    nl="\n"
    basic1="You are an expert in extracting items from a paper professionally and precisely. "
    basic2="Please summarize [input] and extract items corresponding to [schema] or return empty list, if it is an empty list, please return \'null\' without quote."
    cot1='You need to answer with "Keywords", "Verify", "Conclusion" and "Result" step by step. '
    cot2='If the answer in "Keywords" and "Verify" are not the same, it is required to find more clues from the context and append "Context" part before drawing a "Conclusion".'
    cot2+='Now I will give you some examples about it.'
    basic=basic1+basic2+cot1+cot2+nl
    cot_prompt=shuffle_file(n_value)
    basic3=nl+"Now I will give you the schema and input and result. "+nl+nl
    schema1=schema_prompt(type)
    basic4="###input###"+nl
    
    res=basic+cot_prompt+basic3+schema1+basic4+abstract+"Let's think step by step.\n"
    return res

def test_main(n_values=2):
    cnt=0
    total_score=0
    class_score=[0,0,0,0,0]
    class_cnt=[0,0,0,0,0]
    filepath="./abstract/"
    if "TestOutput" not in os.listdir():
        os.mkdir("./TestOutput")
    output_file="./TestOutput/"
    types=["species","tissues","organ_parts","technologies","disease","type"]
    for root,dir,files in os.walk(filepath):
        for file in files:
            if cnt>=100:
                break
            if not (file.startswith("2")  or file.startswith("30")):
            # if file.startswith("2")  or file.startswith("30"):
                # print(os.path.join(root,file))
                lines=[]
                with open(os.path.join(root,file),encoding='utf-8') as f:
                    for line in f:
                        lines.append(line.strip('\n'))
                abstract=lines[5]
                for i in range(5):
                    cnt+=1
                    print(cnt)
                    input_str=input_gen(abstract,type=types[i],n_value=n_values)
                    res=askAI(input_str,model="glm-4-plus")
                    refined=refine(res)
                    testfile=open(output_file+file[:-3]+types[i]+".txt","w",encoding="utf-8")
                    print(refined,file=testfile)
                    testfile.close()
                    lastword=last(refined)
                    # 查询标答并比较
                    if lastword=="ERROR":
                        errfile=open("error.txt","a+",encoding="utf-8")
                        print("ERROR in ",file,"type=",types[i])
                        print(f"-----{file}-----",file=errfile)
                        print("ERROR in ",file,"type=",types[i],file=errfile)
                        print("-----------",file=errfile)
                        errfile.close()
                    else:
                        
                        print(f"-----{file}-----")
                        print(f"lastword={lastword}")
                        print(f"ans:{lines[i]}")
                        score=compare_output(lastword,lines[i])
                        if score=="ERROR":
                            errfile=open("error.txt","a+",encoding="utf-8")
                            print(f"-----{file}-----",file=errfile)
                            print("ERROR in ",file,"type=",types[i])
                            print("ERROR in ",file,"type=",types[i],file=errfile)
                            print(f"lastword={lastword}",file=errfile)
                            print(f"ans:{lines[i]}",file=errfile)
                            print("-----------",file=errfile)
                            errfile.close()
                            continue
                        class_cnt[i]+=1
                        class_score[i]+=score
                        total_score+=score
                        print(f"score:{score}")

                        ansfile=open("./Ans"+str(i)+".txt","a+",encoding="utf-8")
                        print(score,file=ansfile)
                        ansfile.close()
                        print("-----------")
                    # 计算平均杰卡德相似度
                    
    print(f"total_score:{total_score}, cnt:{cnt}")  
    print(f"average:{total_score/cnt}")                  
                        
    for i in range(5):
        print(f"type: {types[i]}, class_score{class_score}, class_cnt{class_cnt}")
        
if __name__ == "__main__":
    test_main(2)
                        
# print(input_gen(abstract="AAAAAAAAAAA",type="species"))