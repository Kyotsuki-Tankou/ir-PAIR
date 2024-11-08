import sqlite3
import re
import json
from garbageAbstract import garbage_abstract
        
def unique_list(overlap_list):
    if overlap_list is None:
        return None
    unique_values=set()
    pattern = re.compile(r'[;|/]+')
    values = pattern.split(overlap_list)
    # escaped_values = [value.replace('"', '\\"') for value in values]
    # unique_values.update(escaped_values)
    unique_values.update(values)
    unique_values_list = list(unique_values)
    return unique_values_list

class train_set_data:
    def __init__(self) -> None:
        self.title=""
        self.pmid=""
        self.sex=""
        self.species=[]
        self.tissues=[]
        self.organ_parts=[]
        self.technologies=[]
        self.disease=[]
        self.type=""
    def fix(self,title, species, tissues, organ_parts, sex, technologies, disease, pmid):
        self.title=title
        self.pmid=pmid
        self.sex=sex
        self.species=unique_list(species)
        self.tissues=unique_list(tissues)
        self.organ_parts=unique_list(organ_parts)
        self.technologies=unique_list(technologies)
        self.disease=unique_list(disease)
        
        #'title, species, tissues, organ_parts, sex, technologies, disease, pmid'
    def fix_value(self,value):
        self.title=value[0]
        self.pmid=value[7]
        self.sex=value[4]
        self.species=unique_list(value[1])
        self.tissues=unique_list(value[2])
        self.organ_parts=unique_list(value[3])
        self.technologies=unique_list(value[5])
        self.disease=unique_list(value[6])
    def forward(self):
        # newline='\\n'
        # # str='```json'+newline+'{'+newline
        # str='{'+newline

        # str += f'  "species": {json.dumps(self.species)},' + newline
        # str += f'  "tissues": {json.dumps(self.tissues)},' + newline
        # str += f'  "organ_parts": {json.dumps(self.organ_parts)},' + newline
        # str += f'  "sex": "{self.sex}",' + newline
        # str += f'  "technologies": {json.dumps(self.technologies)},' + newline
        # str += f'  "disease": {json.dumps(self.disease)}' + newline
    
        # str+='}'+newline+'```'
        # print(str)
        str=""
        str+=json.dumps(self.species)+"\n"
        str+=json.dumps(self.tissues)+"\n"
        str+=json.dumps(self.organ_parts)+"\n"
        str+=json.dumps(self.technologies)+"\n"
        str+=json.dumps(self.disease)+"\n"
        # str += f'"species": {json.dumps(self.species)},'
        # str += f'"tissues": {json.dumps(self.tissues)},'
        # str += f'"organ_parts": {json.dumps(self.organ_parts)},'
        # str += f'"sex": "{self.sex}",'
        # str += f'"technologies": {json.dumps(self.technologies)},'
        # str += f'"disease": {json.dumps(self.disease)}'
        return str
        
    
def read_and_deduplicate_column(db_file, table_name, column_name):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    query = f"SELECT {column_name} FROM {table_name}"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    # unique_values = set()
    # pattern = re.compile(r'[;|/]+')
    
    # for row in results:
    #     if None in row:
    #         continue
    #     values = pattern.split(row[0])
    #     unique_values.update(values)
    # unique_values_list = list(unique_values)
    # return unique_values_list
    return results

def row_proc(row):
    result=[]

def garbage_msg_gen(prompt="",abstract="",res=""):
    str='{"messages": [{"role": "system", "content": "'
    str+=prompt
    str+='"},'
    str+='{"role": "user", "content": "'
    str+=abstract
    str+='"},'
    str+='{"role": "assistant", "content": "' 
    str+=res.replace('"','\\"')
    str+='"}]}'
    # str=str
    return str

# 示例用法
db_file = 'STpair.db'
table_name = 'datasets'
column_name = 'title, species, tissues, organ_parts, sex, technologies, disease, pmid, dataset_id'

file0=open("garbage_train_set.json","w",encoding='utf-8')
values = read_and_deduplicate_column(db_file, table_name, column_name)

with open('prompt-woNL.txt',encoding='utf-8') as f:
    prompt=f.read()
    
cnt=0
dir="./abstract/"
for value in values:
    if value[7] is None:
        continue
    if cnt>=240:
        break
    cnt+=1
    
    test=train_set_data()
    test.fix_value(value)
    res=test.forward()
    abstract=garbage_abstract("https://pubmed.ncbi.nlm.nih.gov/"+test.pmid)
    
    # print(garbage_msg_gen(abstract=abstract,prompt=prompt,res=res),file=file0)
    filea=open(dir+test.pmid+".txt","w",encoding='utf-8')
    print(res,abstract,file=filea)
    
print(cnt)
# print(test.forward())


# testunique="114514|1919810;114514/114515"
# print(unique_list(testunique))