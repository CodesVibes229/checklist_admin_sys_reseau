from pydantic import BaseModel
from typing import List, Optional


class TaskBase(BaseModel):
    label: str
    checked: bool
    month: str


class TaskCreate(TaskBase):
    pass


class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True


class MonthTasks(BaseModel):
    month: str
    tasks: List[TaskCreate]


class UserCreate(BaseModel):
    username: str
    password: str
