import json
import logging


def lambda_handler(event, context):
    name = event.get("name", "World")
    
    LOG_FORMAT = ("%(asctime)s | %(levelname)s | %(funcName)s:%(lineno)d | %(message)s")
    logging.basicConfig(
    level=logging.DEBUG,
    format=LOG_FORMAT,
    handlers=[
        logging.StreamHandler(),              # console
        ]
    )
    logger = logging.getLogger(__name__)
    logger.debug('Lambda Started')

    return {
        "statusCode": 200,
        "body": f"Hello, {name}!"
    }
