from fastapi import Depends
from . import schemas, models
from sqlalchemy.orm import Session
from app.database import get_db

def create_task(request:schemas.Task, db : Session = Depends(get_db)):
    new_task = models.Task(title=request.title, description=request.description, status=request.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    print(db.query(models.Task).all())
    return new_task