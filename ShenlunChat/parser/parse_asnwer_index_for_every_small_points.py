

def parse(result):
    output = {}    
    # 标准答案
    output["standard_answer"] = result["standard_points"]
    # 解析出大点
    output["points"] = result['check_points']
    # 解析出小点
    output["small_points"] = [ small_points.points for small_points in result['small_points']]
    # 解析出每一个小点对应的分析
    small_points_info = []
    for point_state in result["results"]:
        small_points_info.append({
            "point": point_state.point,
            "standard_index": point_state.standard_answer_index,
            "compare_text": point_state.compare_text,
            "compare_reason": point_state.compare_reason,
            "point_index": int(point_state.index.split("_")[0]),
            "small_point_index": int(point_state.index.split("_")[1]),
        })
    output["small_points_info"] = small_points_info
    return output