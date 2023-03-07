import logging

from pydantic import BaseModel
logger = logging.getLogger("helloworld")
class MessageResponse(BaseModel):
    message: str

class HelloWorld:

    @staticmethod
    def getMessage():
        logger.info("request to helloworld.getmessage")
        return MessageResponse(message="Hello World!!")
