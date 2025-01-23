#@Author: guochaoqun  
#@Date: 2024-08-04 16:01:57  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 16:01:57 

from langgraph.graph import START, END

from ShenlunChat.graphs.graph_factory.base import GraphBase
from ShenlunChat.graphs.tool_nodes.compare_with_standard_answers import ParralelCompareToolNodeConfig

class CompareWithStandardAnswersGraph(GraphBase):
    agentnode_config_dict = { 
        "compare_with_standard_answers_agent": {
            "node_name": "compare_with_standard_answers",
            "agent_info": {
                "model_info": {"chat_name": "openai", "model_name": "gpt-4o", "model_config": {}},
                "task_info": {"task_name": "compare_with_standard_answers", "prompt_type": "prompt"},
                "tool_info": [],
                "llm": True
            },
            "state_info": None
        }
    }
    tool_node_dict = {
    }
    build_config = {
        "agent_nodes": ["compare_with_standard_answers_agent"],
        "tool_nodes": [],
        "edges": [
            ("compare_with_standard_answers_agent", END)
        ],
        "conditional_edge":[
            (START,ParralelCompareToolNodeConfig.tool_node,["compare_with_standard_answers_agent"])
        ],
        "state":{
            "state_schema": ("agent:compare_with_standard_answers_agent", "output_state")
        }
    }

if __name__=="__main__":
    from ShenlunChat.graphs.states.compare_with_standard_answers_state import State, PointState
    graph_config = CompareWithStandardAnswersGraph().create_graph()
    point = "树立品牌标杆"
    content = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"
    check_points= ["1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。"]
    small_points = [["树立品牌标杆", "强化品牌建设", "设立质量奖", "推广先进经验", "将质量文化、品牌理念向全产业链延伸"]]
    standard_points = ["设立品牌标杆。强化品牌建设，发挥质量奖示范作用，推广先进经验，将质量文化、品牌理念向全产业链延伸",
                       "创建区域品牌。打造龙头企业，成立行业联盟，制定产业全链条标准，提升全行业质量。",
                       "提供商标品牌服务，设立指导站，提供一站式公共服务平台，开展专题培训。",
                       "打造社会服务平台。开展品牌论坛，发起活动，建设品牌专业组织，为企业提供人才、品牌服务。",
                       "举办高端品牌会议。大力宣传，推动企业竞争从要素向品牌转变。"]
    # state = PointState(point=point,index=0,complete_point=this_point,standard_points=standard_points)
    state = State(content=content,
                  check_points=check_points,
                  small_points=small_points,
                  standard_points=standard_points)
    result = graph_config.graph.invoke(state)
    print(result)