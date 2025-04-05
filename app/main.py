from fastapi import FastAPI
from . import routes
from app.utils import health_check

app = FastAPI()
app.include_router(routes.router)
app.add_api_route("/health", health_check, methods=["GET"])
