
from ShenlunChat.graphs.states.split_points_state import State
from ShenlunChat.graphs.agent_nodes.split_points_agent import SplitPointsAgentNode
# 创造一个agent node
agent_info = {
    "model_info":{"chat_name":"openai","model_name":"gpt-4o","model_config":{}},
    "task_info":{"task_name":"split_points","prompt_type":"prompt"},
    "tool_info":["split_points"],
    "llm":True
}
config = SplitPointsAgentNode.get_agent_node(agent_info)
# print(node)
content = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。2.成立行业联盟，制定行业标准，成为区域品牌，3打造一站示公共服务平台。设立指导站，进行专题培训、内容辅导等4.承办先行论坛。发起多项品牌活动。5提供品牌服务。品牌专业组织为制造业企业提供人才培养、品牌培育、战略升维等服务、6、举办高端品牌会议、宣传广东制造，推动企业从“要素竞争”向“品牌竞争“转变"
state = State(content=content)
output = config.agent_node(state)
print(output)