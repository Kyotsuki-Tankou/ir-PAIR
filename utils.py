import os
import re
import time
from zhipuai import ZhipuAI
from pathlib import Path
import json

def askAI(question,model="glm-4-plus"):
    client = ZhipuAI(api_key="4628e207e641a449e343ac01bd67d389.7uPLdrkjhhh0ABol")
    response = client.chat.asyncCompletions.create(
        model=model,
        messages=[
                {"role": "user", "content": question},
            ],
    )
    task_id=response.id
    task_status=''
    res=""
    get_cnt=0
    while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 4000:
        # time.sleep(10)
        result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
        if result_response.model is not None:
            # print(result_response.choices[0].message.content)
            res=result_response.choices[0].message.content
        task_status = result_response.task_status
        time.sleep(2)
        get_cnt += 1
    return res

def refine(input):
    pattern = r'content=\'```json\n(.*?)\n```\''
    match = re.search(pattern, input, re.DOTALL)
    if match:
        json_content = match.group(1)
        # json_content = json_content.replace('\n', '\\n')
        json_content = json_content
        return json_content
    else:
        # return input.replace('\n','\\n')
        return input.replace('\n\n','\n')
        # return input
        
def compare_output(ans_str,res_str):
    ans=[]
    res=[]
    if ans_str.lower()!='null':
        try:
            ans=eval(ans_str)
        except:
            return "ERROR"
    if res_str.lower()!='null':
        try:
            res=eval(res_str)
        except:
            return "ERROR"
    ans_set=set(ans)
    res_set=set(res)
    intersection = ans_set.intersection(res_set)
    union = ans_set.union(res_set)
    if not union:
        jaccard_similarity=1.0
    else:
        jaccard_similarity=len(intersection)/len(union)
    return jaccard_similarity

def last(text):
    text=text.rstrip('\n') 
    text=text.rstrip('\\n') 
    last_newline_pos = text.rfind('\n')
    last_escaped_newline_pos = text.rfind('\\n')

    res=""
    if last_newline_pos == -1:
        if last_escaped_newline_pos == -1:
            res="ERROR"
        else:
            res=text[last_escaped_newline_pos + 2:]
    elif last_escaped_newline_pos == -1:
        res=text[last_newline_pos + 1:]
    else:
        if last_newline_pos > last_escaped_newline_pos:
            res=text[last_newline_pos + 1:]
        else:
            res=text[last_escaped_newline_pos + 2:]
    if len(res)==0 or res is None:
        res="ERROR"
    if len(res)>=1 and res[-1]=='\n':
        res="ERROR"
    if len(res)>=2 and res[-2:]=='\\n':
        res="ERROR"
    return res

def find_substrings(a, s):
    found_substrings = []
    for substring in s:
        if substring in a:
            found_substrings.append(substring)
    return str(found_substrings)

if __name__ == "__main__":
    # print(last("1111111111\n22\\n3333333\n\\n\n"))
    a = "hello world, this is a test string"
    s = ["hello", "world", "test", "example"]

    result = find_substrings(a, s)
    print(result)