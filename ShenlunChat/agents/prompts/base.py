from typing import List, Union

class PromptBase():
    def get_prompt(self,*args,**kwargs)->str:
        raise NotImplementedError

class PromptListBase(PromptBase):
    def get_promptlist(self,*args,**kwargs)->List[str]:
        raise NotImplementedError