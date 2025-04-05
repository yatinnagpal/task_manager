from pydantic import BaseModel
from enum import Enum
from typing import Optional

class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in-progress"
    completed = "completed"


class Task(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum