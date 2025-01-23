
from typing import List, Dict, Any

def cal_single_question_score(parse_result,keywords_info) -> Dict[str,float]:
    """这个函数用于计算单一题的分数
    计算的方式:
    每一个keyword都对应一个标准答案 和 分数。
    parse_results中 每一个点 如果 对应 标准答案点， keyword也在该点中，那么该点得分。否则不得分
    """
    score = 0
    total_score = 0
    answer_point_num = len(parse_result["standard_answer"])
    find_keywords = [ set() for _ in range(answer_point_num)]
    for keyword_info in keywords_info:
        keyword = keyword_info[1]
        standard_answer_index = keyword_info[0]
        keyword_score = keyword_info[2]
        for point_info in parse_result["small_points_info"]:
            if point_info["standard_index"] != standard_answer_index:
                continue
            if keyword in point_info["point"] and keyword not in find_keywords[standard_answer_index]:
                score += keyword_score
                find_keywords[standard_answer_index].add(keyword)
        total_score += keyword_score
    return {"score":score,"total_score":total_score}

