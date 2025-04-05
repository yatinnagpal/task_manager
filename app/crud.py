from fastapi import Depends, Query, HTTPException
from . import schemas, models
from sqlalchemy.orm import Session
from app.database import get_db
from uuid import UUID

def create_task(request:schemas.Task, db : Session = Depends(get_db)):
    new_task = models.Task(title=request.title, description=request.description, status=request.status)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    print(db.query(models.Task).all())
    return new_task


def get_task(limit: int = Query(10, ge=0), skip: int = Query(0, ge=0), db: Session = Depends(get_db)):
    task = db.query(models.Task).offset(skip).limit(limit).all()
    return task


def update_task(task_id: UUID, request: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    
    task.title = request.title
    task.status = request.status
    db.commit()
    db.refresh(task)
    return task


def delete_task(task_id: UUID, db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail='Task not found')
    
    db.delete(task)
    db.commit()
    return {"detail: Task deleted successfully"}