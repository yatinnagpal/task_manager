from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from .database import get_db
from app.logger import logger

def health_check(db: Session = Depends(get_db)):
    try:
        db.query(None).first()
        logger.info("Health check successful")
        return {"status": "ok"}
    except SQLAlchemyError as e:
        logger.error(f"Health check failed: {e}")
        raise HTTPException(status_code=503, detail=f"Database is not reachable: {str(e)}")
