#@Author: guochaoqun  
#@Date: 2024-07-27 17:54:24  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 17:54:24 

from ShenlunChat.agents.prompts.factory.base import PromptFactoryBase

from ShenlunChat.agents.models.student_answer import CompareStudentSmallPoints, CompareStudentSmallPointsResult
from ShenlunChat.agents.prompts.role import GongWuYuanRole
from ShenlunChat.agents.prompts.task import CompareWithStandardAnswersTask
from ShenlunChat.agents.prompts.demonstration import CompareWithStandardAnswersDemonstration

class CompareWithStandardAnswersPromptFactory(PromptFactoryBase):
    role = GongWuYuanRole
    task = CompareWithStandardAnswersTask
    demonstration = CompareWithStandardAnswersDemonstration
    input_model = CompareStudentSmallPoints
    output_model = CompareStudentSmallPointsResult
    only_str_input: bool =False

if __name__ == "__main__": 
    prompt = CompareWithStandardAnswersPromptFactory.generate_prompt_template(prompt_type="prompt")
    prompt.format_prompt(point="学生在公务员考试中一道题的答案",standard_points=["标准答案1","标准答案2","标准答案3"],this_point="学生该点的答案")
    print(prompt)
    # print(prompt.template)