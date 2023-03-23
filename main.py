from fastapi import FastAPI
import requests

from utils.baseurl import PROJECT_API
from utils.proxy import PROXY

app = FastAPI()


@app.get("/")
async def root():
    return {"status": "ready"}


@app.get("/project/view")
async def project(id: int):
    with requests.get(f"{PROXY[0]}{PROJECT_API}{id}/") as request:
        try:
            response = request.json()["stats"]
        except KeyError:
            return {"error": "not found"}

    return response
