# Task Manager
A simple and efficient Task Management System built using FastAPI, SQLAlchemy, and PostgreSQL, designed to manage tasks with CRUD operations and pagination.


## Features

- Create a task
- Get all tasks
- Update a task
- Delete a task
- Health check endpoint


## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- PostgreSQL (or SQLite for local)
- Pydantic (for data validation)
- SQLAlchemy (for ORM)
- Uvicorn (ASGI server)


2. Create and activate virtual environment
   
    python -m venv task-env
    source task-env/bin/activate  # For Windows: task-env\Scripts\activate


4. Install dependencies

    pip install -r requirements.txt

5. Run the app
   
    uvicorn app.main:app --reload



