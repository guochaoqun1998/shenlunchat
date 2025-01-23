#@Author: guochaoqun  
#@Date: 2024-07-27 17:58:39  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 17:58:39 

import json
# from pydantic import BaseModel
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
from ShenlunChat.utils.prompt_decorator import get_docstring
from ShenlunChat.agents.prompts.charactors import SUBPART_SPLITTER

class PromptFactoryBase():
    """在这个类中，采用建造者方式，我们将定义一个基类，该基类将用于所有的PromptFactory类。
    在这个类中，会将不同部分的prompt拼接起来，生成一个完整的prompt。
    然后使用PromptTemplate类，将prompt进行格式化，生成最终的prompt
    """
    role = None
    task = None
    demonstration = None
    input_model:BaseModel = None
    output_model:BaseModel = None
    only_str_input: bool =False

    @classmethod
    def check_valid(cls):
        for attr in ["role", "task", "demonstration"]:
            if not getattr(cls, attr):
                raise ValueError(f"Please set {attr} in the class")
        for attr in ["input_model", "output_model"]:
            if not getattr(cls, attr):
                raise ValueError(f"Please set {attr} in the class")
            ## 检查是否是pydantic的model
            if not issubclass(getattr(cls, attr), BaseModel):
                raise ValueError(f"{attr} should be a pydantic model")

    @classmethod
    def generate_prompt_template(cls,prompt_type:str="prompt"):
        """请按照建造者模式，将不同部分的prompt拼接起来，生成一个完整的prompt。
        prompt_type = "message" or "prompt",用于区分 HumanMessage 和 PromptTemplate
        包含的部分有: role, input, task, demonstration, output, current_input
        然后使用PromptTemplate类，将prompt进行格式化，生成最终的prompt
        """
        cls.check_valid()
        template = cls.template()
        "在末尾添加本次输入"
        template = template.replace("{current_input_content}",cls.current_input())
        partial_dict = {}
        for attr in ["role", "input_format", "task", "demonstration", "output_format"]:
            content_cls = getattr(cls, attr)
            # 查看是类还是函数
            if hasattr(content_cls, "get_prompt"):
                content = content_cls().get_prompt()
            else:
                content = content_cls()
            partial_dict[f"{attr}_content"] = content
        # print("partial_dict:  ",partial_dict)
        if prompt_type == "prompt":
            return PromptTemplate(template=template, partial_variables=partial_dict)
        elif prompt_type == "message":
            return HumanMessagePromptTemplate.from_template(template, partial_variables=partial_dict)
        return template
    
    @classmethod
    def get_parser(cls):
        return PydanticOutputParser(pydantic_object=cls.output_model)
    
    @classmethod
    def get_model(cls):
        return cls.input_model, cls.output_model

    @classmethod
    def input_format(cls):
        model_fields = cls.input_model.__fields__
        if len(model_fields) == 1 and list(model_fields.values())[0].annotation==str:
            cls.only_str_input = True
        else:
            cls.only_str_input = False
        if cls.only_str_input:
            return "输入为纯字符串，用于描述:{}".format(list(model_fields.values())[0].annotation.__doc__)
        model_json_schema = json.dumps(json.loads(cls.input_model.schema_json()), ensure_ascii=False)
        return model_json_schema

    @classmethod
    def current_input(cls):
        result = []
        for field_name, field in cls.input_model.__fields__.items():
            # 我希望写入:  field_name: {field_name}. 其中 field_name 被代替为变量 field_name
            result.append("{}: ".format(field_name)+"{"+"{}".format(field_name)+"}")
            # result.append("{}: \{".format(field_name)+"{}".format(field_name)+"\}")
            result.append(SUBPART_SPLITTER)
        return "\n".join(result)
    
    @classmethod
    def output_format(cls):
        return cls.get_parser().get_format_instructions()

    @classmethod
    @get_docstring
    def template(cls):
        """
        角色: 
        {role_content}
        ======
        输入格式: 
        {input_format_content}
        ======
        任务: 
        {task_content}
        ======
        示例: 
        {demonstration_content}
        ======
        输出格式:
        {output_format_content}
        ======
        本次输入:
        {current_input_content}
        """
        pass


