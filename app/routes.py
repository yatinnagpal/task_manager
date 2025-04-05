from fastapi import APIRouter, Depends
from . import schemas, models, crud
from sqlalchemy.orm import Session
from app.database import get_db, engine

router = APIRouter()

models.Base.metadata.create_all(bind=engine)

@router.post("/create_task", response_model=schemas.Task, status_code=201)
def create_task(request:schemas.Task, db : Session = Depends(get_db)):
    return crud.create_task(request, db)


@router.get("/get_task", response_model=list[schemas.Task])
def get_tasks(limit: int = 10, skip: int = 0, db: Session = Depends(get_db)):
    return crud.get_task(limit, skip, db)