from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.db.database import SessionLocal, engine
from backend.db.models import Tasks
from backend.db.schemas import TaskCreate, TaskRead, TaskUpdate


router = APIRouter(prefix = "/tasks", tags = ["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/tasks", response_model = TaskRead)
def create_tasks(tasks: TaskCreate, db: Session = Depends(get_db)):
    new_task = Tasks(
        user = tasks.user,
        task = tasks.task,
        time = tasks.time, 
        status = tasks.status
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("tasks", response_model = List[TaskRead])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(Tasks).all()

@router.put("/tasks/{id}", response_model = TaskRead)
def update_tasks(
    id: int, 
    task_data = TaskUpdate, 
    db: Session = Depends(get_db)
    ): 

    db_id = db.query(Tasks).filter(Tasks.id == id).first()

    if db_id is None:
        raise HTTPException(status_code=404, detail = 'Task with ID doesn`t exist!')
    
    else:
        if task_data.task is not None:
            db_id.task = task_data.task
        
        if task_data.time is not None:
            db_id.time = task_data.time

        if task_data.status is not None: 
            db_id.status = task_data.status

    db.commit()
    db.refresh(db_id)

    return db_id