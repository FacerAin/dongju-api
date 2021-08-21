from typing import Optional
from pydantic import BaseModel, Field

class TextSchema(BaseModel):
    author: str = Field(...)
    year: int = Field(...)
    emotions: Optional[list]
    text: str = Field(...)
        
    class Config:
        schema_extra = {
            "example":{
                "author": "윤동주",
                "year": 1941,
                "emotions": ['tense'],
                "text": "죽는 날까지 하늘을 우러러\n 한 점 부끄럼이 없기를."
            }
        }
        
        
class UpdateTextModel(BaseModel):
    author: Optional(str)
    year: Optional(int)
    emotions: Optional(list)
    text: Optional(str)
    
    class Config:
        schema_extra = {
            "example":{
                "author": "윤동주",
                "year": 1941,
                "emotions": ['tense'],
                "text": "죽는 날까지 하늘을 우러러\n 한 점 부끄럼이 없기를."
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
    
    