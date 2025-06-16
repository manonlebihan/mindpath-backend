from pydantic import BaseModel
from datetime import datetime

class EmotionCreate(BaseModel):
    emotion: str
    note: str = None

class EmotionOut(BaseModel):
    id: int
    emotion: str
    note: str | None
    created_at: datetime

    class Config:
        orm_mode = True
