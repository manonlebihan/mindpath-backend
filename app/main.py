from fastapi import FastAPI

app = FastAPI(title="MindPath – Journal émotionnel intelligent")

@app.get("/ping")
def ping():
    return {"message": "pong 🧠"}
