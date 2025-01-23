#@Author: guochaoqun  
#@Date: 2024-07-27 20:54:14  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 20:54:14 
import os
import json
file_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(file_dir,"config.json")

from ShenlunChat.agents.chats.Openaichat import OpenAIChatFactory

class ChatFactory:
    config = json.load(open(config_path))

    @classmethod
    def set_config(cls,config):
        cls.config = config
    
    @classmethod
    def create_chat(cls,chat_name:str,model_name:str,model_config=None):
        if chat_name=="openai":
            OpenAIChatFactory.set_key(cls.config["openai_key"])
            return OpenAIChatFactory.get_chat(model_name,**model_config)
        else:
            raise ValueError(f"Chat name {chat_name} is not supported")
