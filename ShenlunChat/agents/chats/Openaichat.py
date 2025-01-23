#@Author: guochaoqun  
#@Date: 2024-07-27 19:03:19  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 19:03:19 
from langchain_openai import ChatOpenAI

class OpenAIChatFactory():
    """使用工厂模式，生成openai的chat"""

    def set_key(key):
        OpenAIChatFactory.openai_key = key
    
    def get_chat(chat_name,temp=0.2,max_retires=2):
        if chat_name=="gpt-4o":
            model_name = "gpt-4o"
        elif chat_name=="gpt-3.5":
            model_name = "gpt-3.5-turbo-0125"
        else:
            raise ValueError(f"Chat name {chat_name} is not supported")
        return ChatOpenAI(
            model=model_name,
            temperature=temp,
            max_tokens=None,
            timeout=None,
            max_retries=max_retires,
            api_key=OpenAIChatFactory.openai_key
        )
