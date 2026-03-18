from fastapi import FastAPI
from src.app.routers.stats import stats
from src.app.routers.shorten import shorten

app = FastAPI()

app.include_router(shorten)
app.include_router(stats)