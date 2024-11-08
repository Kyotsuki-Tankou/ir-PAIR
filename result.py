import time
from zhipuai import ZhipuAI
from pathlib import Path
import json

client = ZhipuAI(api_key="43ca81a7056bb688225774ed98bfbb5a.OfIoKk0w5eHbC5OX") # 请填写您自己的APIKey
result_response = client.chat.asyncCompletions.retrieve_completion_result(id='573517303828811799164229856579829970')
print(result_response)