#@Author: guochaoqun  
#@Date: 2024-07-27 20:45:40  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 20:45:40

from typing import List
from langchain.agents import AgentExecutor, create_tool_calling_agent, create_json_chat_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, \
    HumanMessagePromptTemplate, SystemMessagePromptTemplate
# from langgraph.prebuilt import create_react_agent
from ShenlunChat.agents.chats import ChatFactory
import ShenlunChat.agents.tools as ShenLunTools

class AgentConfig():
    model_info = None
    task_info = None
    tool_info = None
    agent = None
    parser =  None
    tools = None
    input_model = None
    ouput_model = None

class AgentFactory:
    @staticmethod
    def create_agent(model_info,task_info,tool_info,llm=False):
        """
        在此处创建llm或者agent
        如果llm为True，则创建llm, tool_info中的工具将不会被使用
        如果llm为False，则创建agent, tool_info中的工具将会被使用
        """
        config = AgentConfig()

        chat = AgentFactory.create_chat(**model_info)
        human_prompt, parser, input_model, output_model = \
            AgentFactory.create_prompt(**task_info)
        if llm:
            prompt = human_prompt
            agent = prompt | chat | parser
            tools = None
        else:
            prompt = ChatPromptTemplate.from_messages([
                    human_prompt,
                    MessagesPlaceholder(variable_name='agent_scratchpad')])
            tools = AgentFactory.create_tools(tool_info)
            agent = create_tool_calling_agent(chat, tools, prompt)
            agent = AgentExecutor(agent=agent,tools=tools)
            
        config.model_info = model_info
        config.task_info = task_info
        config.tool_info = tool_info
        config.agent = agent
        config.parser = parser
        config.tools = tools
        config.input_model = input_model
        config.ouput_model = output_model
        return config
    
    @staticmethod
    def create_chat(chat_name:str,model_name:str,model_config=None):
        return ChatFactory.create_chat(chat_name,model_name,model_config)
    
    @staticmethod
    def create_prompt(task_name:str,prompt_type:str="message"):
        """
        创建prompt
        prompt_type = "message" or "prompt",用于区分 HumanMessage 和 PromptTemplate
        """
        from ShenlunChat.agents.prompts.factory.base import PromptFactoryBase
        factory_cls:PromptFactoryBase = None
        if task_name=="split_points":
            from ShenlunChat.agents.prompts.factory.split_points import SplitPointsPromptFactory
            factory_cls = SplitPointsPromptFactory
        elif task_name=="split_small_points":
            from ShenlunChat.agents.prompts.factory.split_small_points import SplitSmallPointsPromptFactory
            factory_cls = SplitSmallPointsPromptFactory
        elif task_name=="compare_with_standard_answers":
            from ShenlunChat.agents.prompts.factory.compare_with_standard_answers import CompareWithStandardAnswersPromptFactory
            factory_cls = CompareWithStandardAnswersPromptFactory
        else:
            raise ValueError(f"Task name {task_name} is not supported")
        factory =factory_cls()
        prompt = factory.generate_prompt_template(prompt_type)
        parser = factory.get_parser()
        input_model, output_model = factory.get_model()
        return prompt, parser, input_model, output_model
    
    @staticmethod
    def create_model(task_name:str):
        if task_name=="split_points":
            from ShenlunChat.agents.prompts.factory.split_points import SplitPointsPromptFactory
            factory = SplitPointsPromptFactory()
            return factory.get_model()
        elif task_name=="split_small_points":
            from ShenlunChat.agents.prompts.factory.split_small_points import SplitSmallPointsPromptFactory
            factory = SplitSmallPointsPromptFactory()
            return factory.get_model()
        elif task_name=="compare_with_standard_answers":
            from ShenlunChat.agents.prompts.factory.compare_with_standard_answers import CompareWithStandardAnswersPromptFactory
            factory = CompareWithStandardAnswersPromptFactory()
            return factory.get_model()
        else:
            raise ValueError(f"Task name {task_name} is not supported")
    
    @staticmethod
    def create_tools(tool_list:List[str]):
        tools = []
        for tool_name in tool_list:
            if hasattr(ShenLunTools,tool_name):
                print(tool_name)
                tool = getattr(ShenLunTools,tool_name)
                tools.append(tool)
        return tools
    
if __name__=="__main__":
    task = "compare_with_standard_answers"
    model_info = {"chat_name":"openai","model_name":"gpt-4o","model_config":{}}
    task_info = {"task_name":task,"prompt_type":"prompt"}
    tool_info = []
    config = AgentFactory.create_agent(model_info,task_info,tool_info,llm=True)
    print("create agent success")
    if task == "compare_with_standard_answers":
        point = "树立品牌标杆"
        this_point = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
        standard_points = ["设立品牌标杆。强化品牌建设，发挥质量奖示范作用，推广先进经验，将质量文化、品牌理念向全产业链延伸",
                        "创建区域品牌。打造龙头企业，成立行业联盟，制定产业全链条标准，提升全行业质量。",
                        "提供商标品牌服务，设立指导站，提供一站式公共服务平台，开展专题培训。",
                        "打造社会服务平台。开展品牌论坛，发起活动，建设品牌专业组织，为企业提供人才、品牌服务。",
                        "举办高端品牌会议。大力宣传，推动企业竞争从要素向品牌转变。"]
        student_answer = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
        student_answer = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
        input = config.input_model(point=point,this_point=this_point,standard_points=standard_points)
    result = config.agent.invoke(input)
    print(result)