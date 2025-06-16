from fastapi import FastAPI
from app.routes import auth
from app.routes import auth, emotions

app = FastAPI(title="MindPath – Journal émotionnel intelligent")

app.include_router(auth.router)
app.include_router(emotions.router)
