# for pydantic model
from pydantic import BaseModel, validator


class Prompt(BaseModel):
    question: str

    @validator('question')
    def question_max_len(cls, v):
        if len(v) > 1024:
            raise ValueError('question is too long')
        return v
