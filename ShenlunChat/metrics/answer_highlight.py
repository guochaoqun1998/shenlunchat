

def highlight_answer(parse_result,
                     keywords_info,
                     add_number=True,
                     add_charactor=True) -> str:
    """
    这个函数用于高亮 学生答案中的关键词，进行以下操作：
    1. 遍历每个小点，如果小点中有关键词，那么就高亮 (每一个关键词只高亮一次) 关键词两侧加 <u> </u>, 并在后方加上 <sup>{number}分</sup> 表示分数
    2. 最外侧加上<div> </div>
    """
    def find_substrings_with_find(main_string, sub_string):
        positions = []
        start = 0
        while True:
            pos = main_string.find(sub_string, start)
            if pos == -1:
                break
            positions.append([pos, pos + len(sub_string)])
            start = pos + len(sub_string)
        return positions

    # 先将 keywords_info 按照 standard_answer_index, 字符长度进行排序
    keywords_info = sorted(keywords_info,key=lambda x: (x[0],-len(x[1])))
    student_answer = ""
    answer_point_num = len(parse_result["standard_answer"])
    find_keywords = [ set() for _ in range(answer_point_num)]
    for i, point_info in enumerate(parse_result["small_points_info"]):
        hight_light_sub_answer = point_info["point"]
        find_keywords_indexs = dict()  # 只记录 当前小点中的关键词位置, 用于判断关键词是否重叠
        find_keywords_score = dict()  # 记录关键词的分数
        current_point_index = point_info["point_index"]
        if add_number:
            if i == 0 or current_point_index != parse_result["small_points_info"][i-1]["point_index"]:
                hight_light_sub_answer = f"{current_point_index+1}."+hight_light_sub_answer
        if add_charactor:
            if i == len(parse_result["small_points_info"])-1 or current_point_index != parse_result["small_points_info"][i+1]["point_index"]:
                hight_light_sub_answer = hight_light_sub_answer+"。"
            else:
                hight_light_sub_answer = hight_light_sub_answer+"，"
        for keyword_info in keywords_info:
            standard_answer_index = keyword_info[0]
            keyword = keyword_info[1]
            keyword_score = keyword_info[2]
            if point_info["standard_index"] != standard_answer_index:
                continue
            if keyword in hight_light_sub_answer and keyword not in find_keywords[standard_answer_index]:
                # 找到 关键词出现的所有位置
                keyword_positions = find_substrings_with_find(hight_light_sub_answer,keyword)
                # 找到关键词的位置
                valid_position = None
                for keyword_position in keyword_positions:
                    valid = True
                    for find_keyword_position in find_keywords_indexs.values():
                        if keyword_position[0] < find_keyword_position[1] and keyword_position[1] > find_keyword_position[0]:
                            valid = False
                            break
                    if valid:
                        valid_position = keyword_position
                        break

                if valid_position is None:
                    continue
                find_keywords_indexs[keyword] = valid_position
                find_keywords_score[keyword] = keyword_score
                find_keywords[standard_answer_index].add(keyword)
        # 在此处 统一将 hight_light_sub_answer 中的 关键词进行高亮，并设置分数
        # 根据keywords indexs 的顺序 从后往前进行替换
        find_keywords_indexs = sorted(find_keywords_indexs.items(),key=lambda x: x[1][0],reverse=True)
        for keyword, position in find_keywords_indexs:
            hight_light_sub_answer = hight_light_sub_answer[:position[0]]+f"<u>{keyword}</u>"+f"<sup>{find_keywords_score[keyword]}分</sup>"+hight_light_sub_answer[position[1]:]
        student_answer+=hight_light_sub_answer
    return f"<div>{student_answer}</div>"