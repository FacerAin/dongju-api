from typing import Optional
from pydantic import BaseModel, Field

class TextSchema(BaseModel):
    title: str = Field(...)
    author: str = Field(...)
    year: int = Field(...)
    emotions: Optional[list]
    text: str = Field(...)
        
    class Config:
        schema_extra = {
            "example":{
                "title": "서시",
                "author": "윤동주",
                "year": 1941,
                "emotions": ['tense'],
                "text": "죽는 날까지 하늘을 우러러\n 한 점 부끄럼이 없기를."
            }
        }
        
        
class UpdateTextModel(BaseModel):
    title: Optional[str]
    author: Optional[str]
    year: Optional[int]
    emotions: Optional[list]
    text: Optional[str]
    
    class Config:
        schema_extra = {
            "example":{
                "title": "서시",
                "author": "윤동주",
                "year": 1941,
                "emotions": ['tense'],
                "text": "죽는 날까지 하늘을 우러러\n 한 점 부끄럼이 없기를."
            }
        }

'''
def ResponseModel(data):
    return {
        "data": data,
    }


def ErrorResponseModel(error):
    return {"error": error}
'''