#@Author: guochaoqun  
#@Date: 2024-07-27 17:48:25  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-07-27 17:48:25 

# from pydantic import BaseModel, Field
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List

class StudentAnswer(BaseModel):
    """学生答案
    """
    content: str = Field(default="",description="学生在公务员考试中一道题的答案")

class StudentAnswerPoints(BaseModel):
    """学生答案的分点结果
    """
    check_points: List[str] = Field(default=[""],description="学生在公务员考试中一道题的答案，分点结果")

class StudentAnswerPoint(BaseModel):
    point: str = Field(default="",description="学生在公务员考试的一道题中的一个点")

class StudentAnswerSmallPoint(BaseModel):
    point: str = Field(default="",description="学生在公务员考试的一道题中的一个点的一部分")

class StudentAnswerSmallPoints(BaseModel):
    points: List[str] = Field(default=[""],description="学生在公务员考试中一道题的答案，分点结果")

class StandardAnswer(BaseModel):
    standard_points : List[str] = Field(default_factory=list,description="标准答案")

class CompareStudentSmallPoints(BaseModel):
    """每个点的比较输入
    """
    point: str = Field(default_factory=str,description="学生在公务员考试的一道题中的一个点的一部分")
    this_point: str = Field(default_factory=str,description="学生该点的答案")
    # standard_points: List[str] = StandardAnswer.__fields__["points"]
    standard_points: List[str] = Field(default_factory=list,description="标准答案")

class CompareStudentSmallPointsResult(CompareStudentSmallPoints):
    """每个点的比较结果
    """
    standard_answer_index: int = Field(default=-1,description="匹配的’标准答案‘的序号（从0开始计数）。如果没有匹配的点，那就返回-1")
    compare_text : str = Field(default="",description="’给定字段‘具体匹配的该标准答案点中的字段，请不要匹配整个标准答案点。如果没有匹配的点，那就返回空字符串")
    compare_reason: str = Field(default="",description="匹配的原因。 如果没有匹配的点，也说明原因。")