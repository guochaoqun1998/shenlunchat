#@Author: guochaoqun  
#@Date: 2024-08-08 22:26:20  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-08 22:26:20 

from typing import List, Dict

from ShenlunChat.graphs.states.compare_with_standard_answers_state import State, PointState
from ShenlunChat.graphs.tool_nodes.base import ToolNodeConfig

def grade(standard_points:List[str],keywords_list:List[Dict[str]]) -> State:
    return

class GradeToolNodeConfig(ToolNodeConfig):
    tool_name = "grade"
    tool_type = "tool"
    tool_description = "对结果进行评分"
    input_state = State
    output_state = State
    tool_node = grade
