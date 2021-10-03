from fastapi import FastAPI
from app.routes.text import router as TextRouter
from fastapi.middleware.cors import CORSMiddleware

API_PREFIX = "/api"
PROJECT_NAME="Dong-ju API"
DEBUG = False
VERSION = "0.1"

origins = [
    "http://react.facerain.club",
    "http://dongju.facerain.club"
]

def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    application.include_router(TextRouter, tags=["Text"], prefix="/text")
    return application

app = get_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def read_root():
    return {"Message": "Access Successfully!"}