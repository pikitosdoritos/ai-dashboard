from fastapi import FastAPI
from backend.routers import task
from backend.db.database import SessionLocal

app = FastAPI()

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def get_root():
    return 'Hello!' 

app.include_router(task.router)   