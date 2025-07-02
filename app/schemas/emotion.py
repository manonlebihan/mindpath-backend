from pydantic import BaseModel
from datetime import datetime
from app.schemas.tag import TagOut

class EmotionCreate(BaseModel):
    emotion: str | None = None
    note: str = None
    tag_ids: list[int] = []

class EmotionOut(BaseModel):
    id: int
    emotion: str
    note: str | None
    intensity: int | None
    created_at: datetime
    tags: list[TagOut] = []

    class Config:
        from_attributes = True
