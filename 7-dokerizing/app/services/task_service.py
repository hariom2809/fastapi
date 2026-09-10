from uuid import UUID

from fastapi import HTTPException, status

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.task_model import Task
from app.schemas import task_schema

def list_tasks(db: Session):
    query = select(Task) # select * from Task
    result = db.execute(query)
    tasks = result.scalars().all()
    return tasks

def get_task(task_id: UUID, db: Session):
    query = select(Task).where(Task.id == task_id)
    result = db.execute(query)
    task = result.scalar_one_or_none()
    return task

def create_task(payload: task_schema.CreateTask, db: Session):
    task = Task(
        title = payload.title,
        description = payload.description
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task

def update_task(task_id: UUID, payload: task_schema.UpdateTask, db: Session):
    query = select(Task).where(Task.id == task_id)
    result = db.execute(query)
    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task Not Found"
        )

    update_data = payload.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)

    return task

def replace_task(task_id: UUID, payload: task_schema.ReplaceTask, db: Session):
    query = select(Task).where(Task.id == task_id)
    result = db.execute(query)
    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task Not Found"
        )

    task.title = payload.title
    task.description = payload.description
    task.completed_at = payload.completed_at

    db.commit()
    db.refresh(task)

    return task

def delete_task(task_id: UUID, db: Session):
    query = select(Task).where(Task.id == task_id)
    result = db.execute(query)
    task = result.scalar_one_or_none()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task Not Found"
        )

    db.delete(task)
    db.commit()

    return