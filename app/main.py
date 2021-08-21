from fastapi import FastAPI

API_PREFIX = "/api"
PROJECT_NAME="Dong-ju API"
DEBUG = False
VERSION = "0.0.0.0"


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)
    return application

app = get_application()