#@Author: guochaoqun  
#@Date: 2024-08-04 14:38:22  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 14:38:22 

from typing import Dict

from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase, AgentNodeConfig
from ShenlunChat.graphs.agent_nodes.split_points_agent import SplitPointsAgentNode
from ShenlunChat.graphs.agent_nodes.split_small_points_agent import SplitSmallPointsAgentNode
from ShenlunChat.graphs.agent_nodes.compare_with_standard_answers_agent import CompareWithStandardAnswersAgentNode

class AgentNodeFactory():
    @staticmethod
    def create_agent_node(node_name:str,agent_info:Dict,state_info:Dict=None)->AgentNodeConfig:
        if node_name == "split_points":
            return SplitPointsAgentNode.get_agent_node(agent_info,state_info)
        elif node_name == "split_small_points":
            return SplitSmallPointsAgentNode.get_agent_node(agent_info,state_info)
        elif node_name == "compare_with_standard_answers":
            return CompareWithStandardAnswersAgentNode.get_agent_node(agent_info,state_info)
        else:
            raise ValueError("agent node name is not supported")