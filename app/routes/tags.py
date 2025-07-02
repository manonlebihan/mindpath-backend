from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.tag import Tag
from app.schemas.tag import TagCreate, TagOut
from app.routes.auth import get_me

router = APIRouter()

@router.post("/tags", response_model=TagOut)
def create_tag(tag: TagCreate, db: Session = Depends(get_db), user=Depends(get_me)):
    existing = db.query(Tag).filter(Tag.name == tag.name, Tag.user_id == user.id).first()
    if existing:
        raise HTTPException(status_code=400, detail="Tag already exists.")
    new_tag = Tag(name=tag.name, user_id=user.id)
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@router.get("/tags", response_model=list[TagOut])
def list_tags(db: Session = Depends(get_db), user=Depends(get_me)):
    return db.query(Tag).filter(Tag.user_id == user.id).all()
