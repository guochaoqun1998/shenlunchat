#@Author: guochaoqun  
#@Date: 2024-08-10 10:43:39  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-10 10:43:39 

from typing import List, Dict, Union, Tuple

from ShenlunChat.datatype.enums import *

class StandardAnswer():
    def __init__(self) -> None:
        """
        每一个答案都包含 该题目的所有信息:
        - question_id: 题目的id （一般由基本信息组成）
        - question: 题目的内容, 包含 题干 要求 字数限制
        - question_order: 题目的序号
        - answer_points: 答案的要点
        - keywords: 关键词, 包含关键词的分数，是否意思相近即可
        """

        ### 基本的标签
        self.province:Province = None
        self.year:Year = None
        self.level:LevelType = None
        self.sub_level:SubLevelType = None
        self.question_type:QuestionType = None
        self.question_sub_type:QuestionSubType = None
        self.labels:List[QuestionLabel] = []

        ### 基本的信息
        self.question_id:str = None
        self.question:Dict[str,str] = None
        self.question_order:int = None
        self.answer_points:List[str] = None
        self.keywords:List[Dict[str,List[Union[int,float,str]]]] = None

        ### 分数
        self.total_score:float = None
        self.logic_score:float = None

        ### 对于每个学生答案会处理的信息
        self._init_variables()
    
    def load_question_info(self):
        pass

    def _init_variables(self):
        """在处理学生答案时会用到的信息
        - student_answer: 学生的答案
        - student_answer_points: 学生的答案要点
        - student_answer_small_points: 学生的答案要点的小要点
        - student_answer_small_points_info: 学生的答案要点的小要点 与标准答案相比的信息
        """
        self.student_answer:str = None
        self.student_answer_points:List[str] = None
        self.student_answer_small_points:List[List[str]] = None
        self.student_answer_small_points_info: List[List[Dict[str,Union[int,str]]]] = None

        # 建立映射关系
        ## 建立学生答案的要点与标准答案的要点的映射关系
        ### 结构: 学生的答案大点 -> [标准答案的要点] # 表示每一个小点对应的标准答案的要点
        self.student_answer_points_index_mapping:List[List[int]] = []
        ### 原因分析: 学生的答案大点 -> [标准答案的要点] # 表示每一个小点对应的标准答案的要点的原因分析
        self.student_answer_points_reason_mapping:List[List[str]] = []
        ### 对应的内容: 学生的答案大点 -> [标准答案的要点] # 表示每一个小点对应的标准答案的要点的对应的内容
        self.student_answer_points_content_mapping:List[List[str]] = []

        ## 建立标准答案的要点与学生答案的要点的映射关系
        ### 结构: 标准答案的要点 -> [学生的答案大点] # 表示每一个小点对应的学生的答案的要点
        self.standard_answer_points_index_mapping:List[List[Tuple[int,int]]] = [] # 表示 学生大点与小点
        
        ## 查看学生答案是否发生了杂糅和切分
        self.student_answer_mixture:List[bool] = []
        self.student_answer_split:List[bool] = []

        # 查看关键词信息





        
        


class StudentAnswer():
    pass