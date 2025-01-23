#@Author: guochaoqun  
#@Date: 2024-07-27 22:28:52  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 22:28:52 

from typing import Type, List
# from pydantic import BaseModel
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool, BaseTool, Tool
from ShenlunChat.agents.models.student_answer import StudentAnswerPoints, StudentAnswer

@tool
def check_string_list_in_content(student_answer:str, output:List[str]) -> str:
    """检查字符串列表是否在内容中，返回检查结果"""
    wrong_points = []
    print(f"In check_string_list_in_content: output: {output} | answer: {student_answer}")
    # 根据以上注释进行修改
    if not isinstance(output,list):
        result = "output不是列表，请修改"
    else:
        for point in output:
            if point not in student_answer:
                wrong_points.append(point)
        if len(wrong_points)!=0:
            result = f"答案中不包含{wrong_points}，请修改"
        else:
            if "".join(output) == student_answer:
                result = "答案正确"
            else:
                result = "答案不完整，请修改"
    print("result: ",result)
    return result

# class CheckStringListInContent(Tool):
#     """检查字符串列表是否在内容中，返回检查结果"""
#     name = "CheckStringInContent"
#     func = check
#     description = "检查字符串列表是否在内容中，返回检查结果"
#     args_schema = CheckStringListInContentInput
#     return_direct = False

#     def __init__(self,check_str:str):
#         self.check_str = check_str