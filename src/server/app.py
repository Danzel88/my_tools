from fastapi import FastAPI
from . import api


fast_app = FastAPI()


fast_app.include_router(api.router)
