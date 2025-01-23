
from ShenlunChat.graphs.states.split_points_state import State
from ShenlunChat.graphs.tool_nodes.base import ToolNodeConfig

def check_result(state:State):
    result = state.check_points
    origin_string = state.content
    str_num = 0
    for elem in result:
        if elem in origin_string:
            str_num += len(elem)
    print("str_num",str_num,"total num:",len(origin_string))
    print("rate:",str_num/len(origin_string))
    valid = str_num/len(origin_string) > 0.5
    return {"valid":valid}

class CheckResultToolNodeConfig(ToolNodeConfig):
    tool_name = "check_result"
    tool_type = "tool"
    tool_description = "检查结果是否合理"
    input_state = State
    output_state = State
    tool_node = check_result
