from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List

# Define your desired data structure.
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

class JokeList(BaseModel):
    jokes: str = Field(description="list of jokes")

# print(JokeList.model_json_schema())
model_fields = JokeList.model_fields 
if len(model_fields) == 1 and list(model_fields.values())[0].annotation==str:
    print("str")