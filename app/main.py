from fastapi import FastAPI
from app.routes import auth
from app.routes import auth, emotions
from app.db import Base, engine
from app.models import user, emotion

app = FastAPI(title="MindPath – Journal émotionnel intelligent")

app.include_router(auth.router)
app.include_router(emotions.router)

Base.metadata.create_all(bind=engine)