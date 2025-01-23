#@Author: guochaoqun  
#@Date: 2024-08-03 22:25:00  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-03 22:25:00 

from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase
from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase, AgentNodeConfig

class SplitSmallPointsAgentNode(AgentNodeBase):
    @staticmethod
    def get_agent_node(agent_info,state_info=None) -> AgentNodeConfig:
        input_state, output_state, node_wrapper = SplitSmallPointsAgentNode.get_agent_wrapper_v1()
        return AgentNodeBase.get_agent_node(agent_info=agent_info, 
                                            state_info=state_info, 
                                            input_state=input_state, 
                                            output_state=output_state,
                                            node_wrapper=node_wrapper,
                                            type="custom")
    
    @staticmethod
    def get_agent_wrapper_v1():
        from ShenlunChat.graphs.states.split_small_points_state import State, PointState
        def node_wrapper(agent):
            def agent_node(state:PointState) -> State:
                print("=== agent start")
                agent_output = agent.invoke(state)
                print("=== agent return")
                return {"small_points":[agent_output]}
            return agent_node
        return PointState, State, node_wrapper

if __name__ == "__main__":
    from ShenlunChat.graphs.states.split_small_points_state import State, PointState
    # 创造一个agent node
    agent_info = {
        "model_info":{"chat_name":"openai","model_name":"gpt-4o","model_config":{}},
        "task_info":{"task_name":"split_small_points","prompt_type":"prompt"},
        "tool_info":["split_points"],
        "llm":True
    }
    config = SplitSmallPointsAgentNode.get_agent_node(agent_info)
    # print(node)
    point = "树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
    state = PointState(point=point,index=0)
    output = config.agent_node(state)
    print(output)
    