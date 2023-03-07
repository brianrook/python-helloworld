from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class MessageResponse(BaseModel):
    message: str

@app.get("/helloWorld")
async def root():
    return MessageResponse(message="Hello World!!!")
