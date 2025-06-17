from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.emotion import EmotionCreate, EmotionOut
from app.models.emotion import EmotionEntry
from app.db import get_db
from app.routes.auth import get_me  # fonction already define to get the user
from app.ai.emotion_analysis import analyze_emotion

router = APIRouter()

@router.post("/emotions", response_model=EmotionOut)
def create_emotion(entry: EmotionCreate, db: Session = Depends(get_db), user=Depends(get_me)):
    result = analyze_emotion(entry.note or "")
    emotion = EmotionEntry(
        emotion=result["emotion"],
        intensity=result["intensity"],
        note=entry.note,
        user_id=user.id
    )
    db.add(emotion)
    db.commit()
    db.refresh(emotion)
    return emotion

@router.get("/emotions", response_model=List[EmotionOut])
def list_emotions(db: Session = Depends(get_db), user=Depends(get_me)):
    return db.query(EmotionEntry).filter(EmotionEntry.user_id == user.id).order_by(EmotionEntry.created_at.desc()).all()
