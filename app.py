import logging
import sys
from pydantic import BaseModel

logger = logging.getLogger("main")


class MessageResponse(BaseModel):
    message: str


class HelloWorld:

    @staticmethod
    def getMessage():
        logger.info("request to helloworld.getmessage")
        msg_response = MessageResponse(message="Hello World!!")
        logger.debug("returning msg: %s", msg_response.json())
        return msg_response


def handler(event, context):
    logger.info("handler request in")
    return {
        'statusCode': 200,
        'body': HelloWorld.getMessage().json()
    }
