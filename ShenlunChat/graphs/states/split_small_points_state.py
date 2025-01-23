#@Author: guochaoqun  
#@Date: 2024-08-04 20:38:42  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 20:38:42 

# from pydantic import Field
import operator
from typing import List, Annotated
from langchain_core.pydantic_v1 import BaseModel, Field
from ShenlunChat.agents.models.student_answer import StudentAnswerPoint, StudentAnswerSmallPoints, StudentAnswer, StudentAnswerPoints
# from pydantic import Field

class PointState(StudentAnswerPoint, StudentAnswerSmallPoints):
    index: int = Field(default=0,description="当前分点的索引")

class State(BaseModel):
    content: str = StudentAnswer.__fields__["content"]
    check_points:List[str] = StudentAnswerPoints.__fields__["check_points"]
    small_points:Annotated[List[PointState], operator.add] = Field(default_factory=list,description="分点的结果")