#@Author: guochaoqun  
#@Date: 2024-08-04 20:37:31  
#@Last Modified by:   guochaoqun  
#@Last Modified time: 2024-08-04 20:37:31 

from typing import List
from langchain_core.pydantic_v1 import BaseModel, Field
from ShenlunChat.agents.models.student_answer import StudentAnswer, StudentAnswerPoints

class State(StudentAnswer, StudentAnswerPoints):
    valid:bool = Field(default=False,description="检查结果是否合理")

