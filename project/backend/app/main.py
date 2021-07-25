from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/ping")
def pong():
    return {"ping": "pong"}
