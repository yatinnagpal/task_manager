from fastapi import Depends, Query, HTTPException
from . import schemas, models
from sqlalchemy.orm import Session
from app.database import get_db
from app.logger import logger
from uuid import UUID

def create_task(request:schemas.Task, db : Session = Depends(get_db)):
    try:
        new_task = models.Task(title=request.title, description=request.description, status=request.status)
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        logger.info(f"Created task: {new_task.id}")
        return new_task
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Something went wrong")


def get_task(limit: int = Query(10, ge=0), skip: int = Query(0, ge=0), db: Session = Depends(get_db)):
    try:
        tasks = db.query(models.Task).offset(skip).limit(limit).all()
        logger.info(f"Retrieved {len(tasks)} tasks")
        return tasks
    except Exception as e:
        logger.error(f"Error fetching tasks: {e}")
        raise HTTPException(status_code=500, detail="Error fetching tasks")


def update_task(task_id: UUID, request: schemas.TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        logger.warning(f"Task not found: {task_id}")
        raise HTTPException(status_code=404, detail='Task not found')
    
    task.title = request.title
    task.status = request.status
    db.commit()
    db.refresh(task)
    logger.info(f"Updated task: {task_id}")
    return task


def delete_task(task_id: UUID, db:Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if not task:
        logger.warning(f"Task not found for delete: {task_id}")
        raise HTTPException(status_code=404, detail='Task not found')
    
    db.delete(task)
    db.commit()
    logger.info(f"Deleted task: {task_id}")
    return {"detail: Task deleted successfully"}