#@Author: guochaoqun  
#@Date: 2024-08-07 22:59:52  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-07 22:59:52 
import os
import json
from typing import List, Tuple, Dict, Union
from ShenlunChat.graphs import GraphFactory
from ShenlunChat.parser.parse_asnwer_index_for_every_small_points import parse
from ShenlunChat.metrics.cal_score import cal_single_question_score
from ShenlunChat.metrics.answer_highlight import highlight_answer

class GradeMacroGraph:
    """该图用于评分"""
    def __init__(self,
                 config_path:Union[None,str]=None):
        # if config_path is None:
        #     config_dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"config")
        #     config_path = os.path.join(config_dir_path,"grade_macrograph_config.json")
        # with open(config_path, "r") as f:
        #     self.config = json.load(f)
        self.build_macrograph()
    
    def build_macrograph(self):
        # 首先先建立分隔graph
        print("=== build macrograph")
        print("=== build split_points_config")
        self.split_points_config = GraphFactory.create_graph("split_points")
        print("=== build split_small_points_config")
        self.split_small_points_config = GraphFactory.create_graph("split_small_points")
        print("=== build compare_config")
        self.compare_config = GraphFactory.create_graph("compare_with_standard_answers")
        print("=== build macrograph done")
        self.cal_score_fn = cal_single_question_score
        self.answer_highlight = highlight_answer

    def __call__(self,student_answer:str, standard_answer:List[str], keywords:List[List[any]],):
        """评分"""
        # 首先经过 split_points graph
        split_points_graph = self.split_points_config.graph
        split_points_state = self.split_points_config.input_cls(content=student_answer)
        split_points_result = split_points_graph.invoke(split_points_state)
        # 然后经过 split_small_points graph
        split_small_points_graph = self.split_small_points_config.graph
        split_small_points_state = self.split_small_points_config.input_cls(content=split_points_result["content"],
                                                                            check_points=split_points_result["check_points"])
        split_small_points_result = split_small_points_graph.invoke(split_small_points_state)
        # 最后经过 compare graph
        compare_graph = self.compare_config.graph
        compare_state = self.compare_config.input_cls(content=split_small_points_result["content"],
                                                      check_points=split_small_points_result["check_points"],
                                                      small_points=split_small_points_result["small_points"],
                                                      standard_points=standard_answer)
        compare_result = compare_graph.invoke(compare_state)
        # 解析出每个小点对应的点
        parse_result = parse(compare_result)
        # 与标准答案和关键词进行比较 
        score_info = self.cal_score_fn(parse_result,keywords)
        # 对答案进行分析
        highlight_answer = self.answer_highlight(parse_result,keywords)
        # 说明分析结果
        return {
            "score":score_info,
            "highlight_answer":highlight_answer
            }

if __name__ == "__main__":
    from datetime import datetime
    import json
    paper_path = "/Users/guochaoqun/Documents/code/aishenlun/auto_label/标准答案打标/parsed_data/2023_广东_省考_县级_1.json"
    with open(paper_path, "r") as f:
        paper = json.load(f)
    start_time = datetime.now()
    student_answer = "1.树立品牌标杆,强化品牌建设，设立质量奖、推广先进经验，将质量文化、品牌理念向全产业链延伸。2.成立行业联盟，制定行业标准，成为区域品牌，3打造一站示公共服务平台。设立指导站，进行专题培训、内容辅导等4.承办先行论坛。发起多项品牌活动。5提供品牌服务。品牌专业组织为制造业企业提供人才培养、品牌培育、战略升维等服务、6、举办高端品牌会议、宣传广东制造，推动企业从“要素竞争”向“品牌竞争“转变"
    
    grade_macrograph = GradeMacroGraph()
    grade_macrograph_result = grade_macrograph(student_answer,paper["answers"],paper["keywords"])
    end_time = datetime.now()
    seconds = (end_time-start_time).total_seconds()
    print(f"seconds: {seconds}")
    result = grade_macrograph_result
    print(result["score"])
    print(result["highlight_answer"]) 