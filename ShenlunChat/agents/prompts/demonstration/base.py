#@Author: guochaoqun  
#@Date: 2024-07-27 11:23:39  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 11:23:39 
from typing import List
from ShenlunChat.agents.prompts import PromptListBase, PromptBase
from ShenlunChat.utils.prompt_decorator import get_docstring

class ExampleBase(PromptListBase):
    def get_promptlist(self,example_list:list)->List[str]:
        result = []
        for example in example_list:
            if getattr(self,example,None) is not None and callable(getattr(self,example)) and hasattr(getattr(self,example), "is_prompt_doc"):
                result.append(getattr(self,example)())
        return result
    
    def get_all_promptlist(self)->List[str]:
        # 检查函数是否被 @get_docstring 装饰器装饰
        result = []
        for attr in dir(self):
            # 检查函数是否被 @get_docstring 装饰器装饰
            if callable(getattr(self, attr)) and hasattr(getattr(self, attr), "is_prompt_doc"):
                result.append(getattr(self, attr)())
        return result

class DemonstrationBase(PromptBase):
    example_cls = ExampleBase
    def get_prompt(self) -> str:
        NotImplementedError("Please implement the get_prompt method in the subclass.")

    def _get_prompt(self,example_list:List[str]=[],all:bool=False)->str:
        from ShenlunChat.agents.prompts.charactors import SUBPART_SPLITTER, SUBPART_HALF_SPLITTER, SUBPART_SPLITTER
        if all is False:
            example_list = self.example_cls().get_promptlist(example_list)
        else:
            example_list = self.example_cls().get_all_promptlist()
        if len(example_list) == 0:
            return """本次未提供任何示例，请根据其他信息完成任务。"""
        else:
            example_list = [example.strip() for example in example_list if example.strip() != ""]
            # example_split:str = SUBPART_SPLITTER
            example_index = SUBPART_HALF_SPLITTER
            text_footer:str = SUBPART_HALF_SPLITTER
            final_text_list = []
            for example_i, example in enumerate(example_list):
                final_text_list.append(f"{example_index}示例{example_i+1}：")
                final_text_list.append(example)
            final_text_list.append(text_footer)
            return "\n".join(final_text_list)

    