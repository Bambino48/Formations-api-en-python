import os

from fastapi import FastAPI # type: ignore

app = FastAPI()

@app.get("/") # api.com/
async def root():
    return {"message": "Hello, world!"}
