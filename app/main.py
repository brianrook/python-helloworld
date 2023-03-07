from fastapi import FastAPI
from app.helloworld import HelloWorld
import logging

app = FastAPI()
logger = logging.getLogger("main")
@app.get("/helloWorld")
async def root():
    logger.info("request in")
    return HelloWorld.getMessage()
