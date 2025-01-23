#@Author: guochaoqun  
#@Date: 2024-08-04 20:38:42  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 20:38:42 

# from pydantic import Field
import operator
from typing import List, Annotated, Union
from langchain_core.pydantic_v1 import BaseModel, Field
from ShenlunChat.agents.models.student_answer import StudentAnswerSmallPoints, StudentAnswerSmallPoint, \
    StudentAnswer, StudentAnswerPoints, StandardAnswer, CompareStudentSmallPointsResult, \
    CompareStudentSmallPoints
# from pydantic import Field

class PointState(CompareStudentSmallPointsResult,CompareStudentSmallPoints):
    index: str = Field(default="",description="当前分点的索引")

class State(StudentAnswer,StudentAnswerPoints,StandardAnswer):
    small_points:Union[List,List[StudentAnswerSmallPoints]] = Field(default=[],description="分点的结果")
    results:Annotated[Union[List,List[PointState]], operator.add] = Field(default=[],description="分点的结果")