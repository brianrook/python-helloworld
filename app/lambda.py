import logging
import sys

from app.helloworld import HelloWorld

logger = logging.getLogger("main")

def handler(event, context):
    logger.info("handler request in")
    return HelloWorld.getMessage()
