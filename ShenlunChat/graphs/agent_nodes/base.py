#@Author: guochaoqun  
#@Date: 2024-08-03 10:56:47  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-03 10:56:47  
from ShenlunChat.agents.agent_factory.factory import AgentFactory, AgentConfig
from ShenlunChat.graphs.utils.agent_adaptor import AgentNodeWrapper

class  AgentNodeConfig():
    agent_config = None
    agent_node = None
    input_state = None
    output_state = None
    input_mapping = None
    output_mapping = None

class AgentNodeBase():
    """这是agent node的类"""
    @staticmethod
    def get_agent_node(agent_info,
                       state_info,
                       input_state,
                       output_state,
                       type:str,
                       **kwargs) -> AgentNodeConfig:
        node_config = AgentNodeConfig()
        agent_config = AgentNodeBase.get_agent(agent_info)
        if type == "custom":
            node_wrapper = kwargs["node_wrapper"]
            node = node_wrapper(agent_config.agent)
            input_mapping, output_mapping = None, None
        elif type == "default":
            input_mapping, output_mapping = kwargs["input_mapping"], kwargs["output_mapping"]
            node = AgentNodeWrapper(agent_config.agent, input_state, output_state, input_mapping, output_mapping)
        node_config.agent_config = agent_config
        node_config.agent_node = node
        node_config.input_state = input_state
        node_config.output_state = output_state
        node_config.input_mapping = input_mapping
        node_config.output_mapping = output_mapping
        return node_config

    @staticmethod
    def get_config(self):
        pass

    @staticmethod
    def get_agent(agent_info) -> AgentConfig:
        return AgentFactory.create_agent(**agent_info)
    

