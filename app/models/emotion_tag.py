from sqlalchemy import Table, Column, Integer, ForeignKey
from app.db import Base

emotion_tags = Table(
    'emotion_tags',
    Base.metadata,
    Column('emotion_id', Integer, ForeignKey('emotions.id')),
    Column('tag_id', Integer, ForeignKey('tags.id'))
)