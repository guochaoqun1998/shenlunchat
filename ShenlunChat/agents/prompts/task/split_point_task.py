#@Author: guochaoqun  
#@Date: 2024-07-25 23:45:05  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-25 23:45:05 

from ShenlunChat.agents.prompts import PromptBase
from ShenlunChat.utils.prompt_decorator import get_docstring

class SplitPointTask(PromptBase):
    """该任务是： 将学生的答案拆分成多个点，形成list列表输出"""

    def get_prompt(self):
        return self.version1()
    
    @get_docstring
    def version1():
        """在这个任务中，你需要对学生答案进行拆分成多个点。
        分点的判断标准如下:
        - 学生的答案可能会按照数字或者'。' ';'等字符进行分点。 
        - 如果学生答案中的数字不在句子开头，在句子中，可以认为是事实论证的一部分，那么忽略该数字。
        - 如果学生答案不能分点，那么就不分点。
        """
        pass

if __name__ == "__main__":
    split_point_task = SplitPointTask()
    print(split_point_task.get_prompt())