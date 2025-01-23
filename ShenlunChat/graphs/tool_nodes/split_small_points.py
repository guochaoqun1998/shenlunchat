
from ShenlunChat.graphs.states.split_small_points_state import PointState, State
from ShenlunChat.graphs.tool_nodes.base import ToolNodeConfig
from langgraph.constants import Send

def parallel_split(state:State):
    """
    并行分点
    """
    return [Send("split_small_points_agent", PointState(point=point,index=i)) for i,point in enumerate(state.check_points)]

class ParralelSplitToolNodeConfig(ToolNodeConfig):
    tool_name = "parallel_split"
    tool_type = "tool"
    tool_description = "并行分点"
    input_state = State
    output_state = PointState
    tool_node = parallel_split
