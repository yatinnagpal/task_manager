from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .database import get_db

def health_check(db: Session = Depends(get_db)):
    try:
        db.query(None).first()
        return {"status": "ok"}
    except SQLAlchemyError as e:
        raise HTTPException(status_code=503, detail=f"Database is not reachable: {str(e)}")
