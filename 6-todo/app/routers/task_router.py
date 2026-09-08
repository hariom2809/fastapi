from uuid import UUID
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.databse import get_db
from app.schemas import task_schema
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Task"])

@router.get("/", response_model=list[task_schema.ListTask], status_code=status.HTTP_200_OK)
def list_tasks(db: Session = Depends(get_db)):
    return task_service.list_tasks(db=db)

@router.get("/{task_id}", response_model=task_schema.GetTask, status_code=status.HTTP_200_OK)
def get_task(task_id: UUID, db: Session = Depends(get_db)):
    return task_service.get_task(task_id=task_id, db=db)

@router.post("/", response_model=task_schema.GetTask, status_code=status.HTTP_201_CREATED)
def create_task(payload: task_schema.CreateTask, db: Session = Depends(get_db)):
    return task_service.create_task(payload, db)

@router.put("/{task_id}", response_model=task_schema.GetTask, status_code=status.HTTP_200_OK)
def replace_task(task_id: UUID, payload: task_schema.ReplaceTask, db: Session = Depends(get_db)):
    return task_service.replace_task(task_id, payload, db)

@router.patch("/{task_id}", response_model=task_schema.GetTask, status_code=status.HTTP_200_OK)
def update_task(task_id: UUID, payload: task_schema.UpdateTask, db: Session = Depends(get_db)):
    return task_service.update_task(task_id, payload, db)