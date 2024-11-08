import time
from zhipuai import ZhipuAI
from pathlib import Path
import json

client = ZhipuAI(api_key="43ca81a7056bb688225774ed98bfbb5a.OfIoKk0w5eHbC5OX") # 请填写您自己的APIKey

def ask_zhipu_ai(question,prompt="你是一个乐于解答各种问题的助手，你的任务是为用户提供专业、准确、有见地的建议。"):
    msg=prompt+question
    response = client.chat.asyncCompletions.create(
        model="glm-4-flash",  # 请填写您要调用的模型名称
        
        messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question},
            ],
    )
    task_id = response.id
    return task_id

task_status = ''
get_cnt = 0
with open('prompt.txt',encoding='utf-8') as f:
    prompt=f.read()
with open('question.txt',encoding='utf-8') as f:
    question=f.read()
# prompt="你是智谱AI的API调用和微调领域的专家，请对我调用智谱AI的API的相关问题做出详细答复："  
# question="请对\n{file_content}\n的内容进行分析，并撰写一份论文摘要。"
# question="The developing brain has a well-organized anatomical structure comprising different types of neural and non-neural cells. Stem cells, progenitors and newborn neurons tightly interact with their neighbouring cells and tissue microenvironment, and this intricate interplay ultimately shapes the output of neurogenesis. Given the relevance of spatial cues during brain development, we acknowledge the necessity for a spatial transcriptomics map accessible to the neurodevelopmental community. To fulfil this need, we generated spatially resolved RNA sequencing (RNAseq) data from embryonic day 13.5 mouse brain sections immunostained for mitotic active neural and vascular cells. Unsupervised clustering defined specific cell type populations of diverse lineages and differentiation states. Differential expression analysis revealed unique transcriptional signatures across specific brain areas, uncovering novel features inherent to particular anatomical domains. Finally, we integrated existing single-cell RNAseq datasets into our spatial transcriptomics map, adding tissue context to single-cell RNAseq data. In summary, we provide a valuable tool that enables the exploration and discovery of unforeseen molecular players involved in neurogenesis, particularly in the crosstalk between different cell types."
task_id=ask_zhipu_ai(question=question,prompt=prompt)
print("task_id",task_id)

while task_status != 'SUCCESS' and task_status != 'FAILED' and get_cnt <= 4000:
    result_response = client.chat.asyncCompletions.retrieve_completion_result(id=task_id)
    if result_response.model is not None:
        print(result_response.choices[0].message.content)
    task_status = result_response.task_status

    time.sleep(2)
    get_cnt += 1
    
