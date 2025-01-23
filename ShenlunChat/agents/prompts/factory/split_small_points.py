#@Author: guochaoqun  
#@Date: 2024-07-27 17:54:24  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 17:54:24 

from ShenlunChat.agents.prompts.factory.base import PromptFactoryBase

from ShenlunChat.agents.models.student_answer import StudentAnswerPoint, StudentAnswerSmallPoints
from ShenlunChat.agents.prompts.role import GongWuYuanRole
from ShenlunChat.agents.prompts.task import SplitSmallPointTask
from ShenlunChat.agents.prompts.demonstration import SplitSmallPointsDemonstration

class SplitSmallPointsPromptFactory(PromptFactoryBase):
    role = GongWuYuanRole
    task = SplitSmallPointTask
    demonstration = SplitSmallPointsDemonstration
    input_model = StudentAnswerPoint
    output_model = StudentAnswerSmallPoints
    only_str_input: bool =False

if __name__ == "__main__": 
    prompt = SplitSmallPointsPromptFactory.generate_prompt_template(prompt_type="prompt")
    # prompt.format_prompt(content="学生在公务员考试中一道题的答案")
    # print(prompt)
    print(prompt.template)