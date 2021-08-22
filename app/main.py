from fastapi import FastAPI
from app.routes.text import router as TextRouter

API_PREFIX = "/api"
PROJECT_NAME="Dong-ju API"
DEBUG = False
VERSION = "0.1"


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(TextRouter, tags=["Text"], prefix="/text")
    return application

app = get_application()

@app.get("/", tags=["Root"])
async def read_root():
    return {"Message": "Access Successfully!"}