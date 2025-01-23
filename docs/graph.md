
## CompareWithStandardAnswers

PointState:
- 标准答案(List[str])
- point (str)
- this_point (str)

PointsResult(PointState):
- standard_answer_index
- compare_text
- compare_reason

OverallState:
- 标准答案(List[str])
- 小点的列表(List[SmallPoints])
- 比较结果的列表(List[List[PointsResult]])

graph:

OverllState -> START -> parral_compare(tool_node) -> agent_node -> END
