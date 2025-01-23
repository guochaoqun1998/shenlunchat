

from typing import List
from langgraph.constants import Send
from ShenlunChat.graphs.states.compare_with_standard_answers_state import PointState, State
from ShenlunChat.graphs.tool_nodes.base import ToolNodeConfig


def parallel_compare(state:State) -> List[Send]:
    """
    并行比较
    """
    point_states = []
    for parga_i, smal_point_list in enumerate(state.small_points):
        for i,point in enumerate(smal_point_list.points):
            point_states.append(PointState(point=point,
                                           index=f"{parga_i}_{i}",
                                           complete_point=state.check_points[parga_i],
                                           standard_points=state.standard_points))
    return [Send("compare_with_standard_answers_agent", point) for point in point_states]

class ParralelCompareToolNodeConfig(ToolNodeConfig):
    tool_name = "parallel_compare"
    tool_type = "tool"
    tool_description = "并行比较"
    input_state = State
    output_state = PointState
    tool_node = parallel_compare
