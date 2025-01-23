#@Author: guochaoqun  
#@Date: 2024-08-03 22:25:00  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-03 22:25:00 

from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase
from ShenlunChat.graphs.agent_nodes.base import AgentNodeBase, AgentNodeConfig

class SplitPointsAgentNode(AgentNodeBase):
    @staticmethod
    def get_agent_node(agent_info,state_info=None) -> AgentNodeConfig:
        input_state, output_state, input_mapping, output_mapping = SplitPointsAgentNode.get_state_and_mapping_v1()
        return AgentNodeBase.get_agent_node(agent_info=agent_info, 
                                            state_info=state_info, 
                                            input_state=input_state, 
                                            output_state=output_state, 
                                            input_mapping=input_mapping, 
                                            output_mapping=output_mapping,
                                            type="default")
    @staticmethod
    def get_state_and_mapping_v1():
        """创建从state到mapping的映射"""
        # ！ 需要注意的是 如果tuple是一个元素，请在后面加上逗号
        from ShenlunChat.graphs.states.split_points_state import State
        input_mapping = {("content",):("content",)}
        output_mapping = {("check_points",):("check_points",)}
        return State, State, input_mapping, output_mapping

if __name__ == "__main__":
    from ShenlunChat.graphs.states.split_points_state import State
    # 创造一个agent node
    agent_info = {
        "model_info":{"chat_name":"openai","model_name":"gpt-4o","model_config":{}},
        "task_info":{"task_name":"split_points","prompt_type":"prompt"},
        "tool_info":["split_points"],
        "llm":True
    }
    node = SplitPointsAgentNode.get_agent_node(agent_info)
    # print(node)
    content = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。2.成立行业联盟，制定行业标准，成为区域品牌，3打造一站示公共服务平台。设立指导站，进行专题培训、内容辅导等4.承办先行论坛。发起多项品牌活动。5提供品牌服务。品牌专业组织为制造业企业提供人才培养、品牌培育、战略升维等服务、6、举办高端品牌会议、宣传广东制造，推动企业从“要素竞争”向“品牌竞争“转变"
    state = State(content=content)
    output = node(state)
    print(output)
    