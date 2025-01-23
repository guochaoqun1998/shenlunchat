#@Author: guochaoqun  
#@Date: 2024-08-04 16:01:57  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 16:01:57 

from langgraph.graph import START, END

from ShenlunChat.graphs.graph_factory.base import GraphBase
from ShenlunChat.graphs.tool_nodes.split_small_points import ParralelSplitToolNodeConfig

class SplitSmallPointsGraph(GraphBase):
    agentnode_config_dict = { 
        "split_small_points_agent": {
            "node_name": "split_small_points",
            "agent_info": {
                "model_info": {"chat_name": "openai", "model_name": "gpt-4o", "model_config": {}},
                "task_info": {"task_name": "split_small_points", "prompt_type": "prompt"},
                "tool_info": [],
                "llm": True
            },
            "state_info": None
        }
    }
    tool_node_dict = {
    }
    build_config = {
        "agent_nodes": ["split_small_points_agent"],
        "tool_nodes": [],
        "edges": [
            ("split_small_points_agent", END)
        ],
        "conditional_edge":[
            (START,ParralelSplitToolNodeConfig.tool_node,["split_small_points_agent"])
        ],
        "state":{
            "state_schema": ("agent:split_small_points_agent", "output_state")
        }
    }

if __name__=="__main__":
    from ShenlunChat.graphs.states.split_small_points_state import State
    graph_config = SplitSmallPointsGraph().create_graph()
    content = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。2.成立行业联盟，制定行业标准，成为区域品牌，3打造一站示公共服务平台。设立指导站，进行专题培训、内容辅导等4.承办先行论坛。发起多项品牌活动。5提供品牌服务。品牌专业组织为制造业企业提供人才培养、品牌培育、战略升维等服务、6、举办高端品牌会议、宣传广东制造，推动企业从“要素竞争”向“品牌竞争“转变"
    state = graph_config.input_cls(content=content,
                                   check_points=['1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。', '2.成立行业联盟，制定行业标准，成为区域品牌，', '3打造一站示公共服务平台。设立指导站，进行专题培训、内容辅导等', '4.承办先行论坛。发起多项品牌活动。', '5提供品牌服务。品牌专业组织为制造业企业提供人才培养、品牌培育、战略升维等服务、', '6、举办高端品牌会议、宣传广东制造，推动企业从“要素竞争”向“品牌竞争“转变'])
    result = graph_config.graph.invoke(state)
    print(result)