#@Author: guochaoqun  
#@Date: 2024-07-26 00:02:55  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-26 00:02:55 

from langchain_community.chat_models import QianfanChatEndpoint

class QianfanChatFactory():
    """使用工厂模式，生成erine的chat"""

    def set_key(ak,sk):
        QianfanChatFactory.ak = ak
        QianfanChatFactory.sk = sk
    
    def get_chat(chat_name,temp=0.2):
        if chat_name=="gpt-4o":
            model_name = "gpt-4o"
        elif chat_name=="gpt-3.5":
            model_name = "gpt-3.5-turbo-0125"
        else:
            raise ValueError(f"Chat name {chat_name} is not supported")
        return QianfanChatEndpoint(
            model=model_name,
            temperature=temp,
            max_tokens=None,
            timeout=None,
            api_key=QianfanChatFactory.ak,
            secret_key=QianfanChatFactory.sk
        )