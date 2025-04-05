from fastapi import APIRouter, Depends
from . import schemas, models, crud
from sqlalchemy.orm import Session
from app.database import get_db, engine
from uuid import UUID

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/create_task", response_model=schemas.Task, status_code=201)
def create_task(request:schemas.Task, db : Session = Depends(get_db)):
    return crud.create_task(request, db)


@router.get("/get_task", response_model=list[schemas.Task])
def get_tasks(limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    return crud.get_task(limit, skip, db)

@router.put("/update_task/{task_id}")
def update_task(task_id: UUID, request: schemas.TaskUpdate, db: Session = Depends(get_db)):
    return crud.update_task(task_id, request, db)


@router.delete('/delete_task/{task_id}', status_code=204)
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    return crud.delete_task(task_id, db)
