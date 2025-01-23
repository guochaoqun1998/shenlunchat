#@Author: guochaoqun  
#@Date: 2024-08-05 23:33:48  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-05 23:33:48 

#@Author: guochaoqun  
#@Date: 2024-08-03 22:25:00  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-03 22:25:00 

from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase
from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase, AgentNodeConfig

class CompareWithStandardAnswersAgentNode(AgentNodeBase):
    @staticmethod
    def get_agent_node(agent_info,state_info=None) -> AgentNodeConfig:
        input_state, output_state, node_wrapper = CompareWithStandardAnswersAgentNode.get_agent_wrapper_v1()
        return AgentNodeBase.get_agent_node(agent_info=agent_info, 
                                            state_info=state_info, 
                                            input_state=input_state, 
                                            output_state=output_state,
                                            node_wrapper=node_wrapper,
                                            type="custom")
    
    @staticmethod
    def get_agent_wrapper_v1():
        from ShenlunChat.graphs.states.compare_with_standard_answers_state import PointState, State
        def node_wrapper(agent):
            def agent_node(state:PointState) -> State:
                print("=== agent start")
                agent_output = agent.invoke(dict(point=state.point,this_point=state.this_point,standard_points=state.standard_points))
                print("=== agent return")
                state.standard_answer_index = agent_output.standard_answer_index
                state.compare_text = agent_output.compare_text
                state.compare_reason = agent_output.compare_reason
                return {"results":[state]}
            return agent_node
        return PointState, State, node_wrapper

if __name__ == "__main__":
    from ShenlunChat.graphs.states.compare_with_standard_answers_state import State, PointState
    # 创造一个agent node
    agent_info = {
        "model_info":{"chat_name":"openai","model_name":"gpt-4o","model_config":{}},
        "task_info":{"task_name":"compare_with_standard_answers","prompt_type":"prompt"},
        "tool_info":[],
        "llm":True
    }
    config = CompareWithStandardAnswersAgentNode.get_agent_node(agent_info)
    # print(node)
    point = "树立品牌标杆"
    this_point = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
    standard_points = ["设立品牌标杆。强化品牌建设，发挥质量奖示范作用，推广先进经验，将质量文化、品牌理念向全产业链延伸",
                       "创建区域品牌。打造龙头企业，成立行业联盟，制定产业全链条标准，提升全行业质量。",
                       "提供商标品牌服务，设立指导站，提供一站式公共服务平台，开展专题培训。",
                       "打造社会服务平台。开展品牌论坛，发起活动，建设品牌专业组织，为企业提供人才、品牌服务。",
                       "举办高端品牌会议。大力宣传，推动企业竞争从要素向品牌转变。"]
    state = PointState(point=point,index=0,complete_point=this_point,standard_points=standard_points)
    output = config.agent_node(state)
    print(output)
    