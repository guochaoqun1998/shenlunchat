#@Author: guochaoqun  
#@Date: 2024-07-25 23:45:05  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-25 23:45:05 

from ShenlunChat.agents.prompts import PromptBase
from ShenlunChat.utils.prompt_decorator import get_docstring

class SplitSmallPointTask(PromptBase):
    """该任务是： 将学生答案按照分点标准分成多个点"""

    def get_prompt(self):
        return self.version1()
    
    @get_docstring
    def version1():
        """在这个任务中，你需要将学生答案按照分点标准分成多个点。
        拆分的判断标准如下:
        - 在分点的过程中只能根据标点符号拆分内容，不可以改变，删减，合并，分开内容 
        - 如果文字采用总分 或者 分总的形式。那么 总领句要单独拆分成点，分句采用以下标准进行拆分
        - 每一个小点要意思完整。对于对策内容，一般将每个动宾结构 拆分成一个小点。
        - 对于'、'分隔的文字，不进行拆分。"
        """
        pass

if __name__ == "__main__":
    split_point_task = SplitSmallPointTask()
    print(split_point_task.get_prompt())