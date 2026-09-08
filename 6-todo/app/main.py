from fastapi import FastAPI
from app.routers import task_router

app = FastAPI()

app.include_router(task_router.router)

@app.get("/")
def health():
    return {"message", "Server is Live and Running"}