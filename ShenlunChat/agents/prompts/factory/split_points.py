#@Author: guochaoqun  
#@Date: 2024-07-27 17:54:24  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 17:54:24 

from ShenlunChat.agents.prompts.factory.base import PromptFactoryBase

from ShenlunChat.agents.models.student_answer import StudentAnswer, StudentAnswerPoints
from ShenlunChat.agents.prompts.role import GongWuYuanRole
from ShenlunChat.agents.prompts.task import SplitPointTask
from ShenlunChat.agents.prompts.demonstration import SplitPointsDemonstration

class SplitPointsPromptFactory(PromptFactoryBase):
    role = GongWuYuanRole
    task = SplitPointTask
    demonstration = SplitPointsDemonstration
    input_model = StudentAnswer
    output_model = StudentAnswerPoints
    only_str_input: bool =False

if __name__ == "__main__":
    prompt = SplitPointsPromptFactory.generate_prompt_template()
    # prompt.format_prompt(content="学生在公务员考试中一道题的答案")
    # print(prompt)
    print(prompt.template)