
from ShenlunChat.agents.prompts import PromptBase
from ShenlunChat.utils.prompt_decorator import get_docstring
import langchain
from langchain.output_parsers import PydanticOutputParser

class TextInput(PromptBase):
    def get_prompt(self):
        return self.version1()
    
    @get_docstring
    def version1(self):
        """输入采用纯文本形式"""
        pass