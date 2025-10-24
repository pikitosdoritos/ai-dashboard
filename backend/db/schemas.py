from pydantic import BaseModel
from typing import Optional

class TaskCreate(BaseModel):
    user: str
    task: str
    time: int
    status: str

    class Config:
        orm_mode = True

class TaskRead(BaseModel):
    id: int
    user: str
    task: str
    time: int
    status: str 

    class Config:
        orm_mode = True

class TaskUpdate(BaseModel):
    task: Optional[str] = None
    time: Optional[int] = None
    status: Optional[str] = None

    class Config:
        orm_mode = True