#@Author: guochaoqun  
#@Date: 2024-08-05 22:22:57  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-05 22:22:57 

from ShenlunChat.agents.prompts import PromptBase
from ShenlunChat.utils.prompt_decorator import get_docstring

class CompareWithStandardAnswersTask(PromptBase):
    """将’给定字段‘与’标准答案‘列表中意思最接近的一个元素进行匹配"""

    def get_prompt(self):
        return self.version1()
    
    @get_docstring
    def version1():
        """在这个任务中你会得到’给定字段‘,’周围信息‘和’标准答案‘。
        - 其中’给定字段‘和’周围信息‘都是字符串，’标准答案‘是一个字符串的列表。
        - ’给定字段‘是’周围信息‘的一部分，’周围信息‘用于让你完整理解’给定字段‘的含义。
        - 请将’给定字段‘与’标准答案‘列表中每一点进行比较，
        - 将’给定字段‘与’标准答案‘列表中意思最接近的一个元素进行匹配。如果没有匹配项，也可以选择不匹配。
        ====== 对比标准如下：
        - 你要按照以下标准将学生答案与标准答案进行对比，寻找意思最为相近的标准答案。
        - 如果给定字段只和标准答案中某一点意思相近，那么该点就是最相近的答案 
        - 如果没有与给定字段意思相近的标准答案，那么该给定字段没有最相近的答案。
        - 如果给定字段与标准答案中多点有相似的意思，请结合’周围信息‘，选出整体意思最为接近的一个答案点。
        """
        pass

if __name__ == "__main__":
    compare_with_standard_answer_task = CompareWithStandardAnswersTask()
    print(compare_with_standard_answer_task.get_prompt())