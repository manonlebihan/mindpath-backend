from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class EmotionEntry(Base):
    __tablename__ = "emotions"

    id = Column(Integer, primary_key=True, index=True)
    emotion = Column(String, nullable=False)
    note = Column(String)
    intensity = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="emotions")
