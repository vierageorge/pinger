from boto3 import client
from dotenv import load_dotenv
from os import getenv
import logging

load_dotenv()

TOPIC_ARN = getenv("AWS_SNS_TOPIC_ARN")
client = client(
    "sns",
    aws_access_key_id=getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=getenv("AWS_SECRET_ACCESS_KEY"),
    region_name=getenv("AWS_REGION")
)

logger = logging.getLogger(__name__)

def send_notification(message):
    client.publish(Message=message, TopicArn=TOPIC_ARN)
    logger.debug("Message sent to AWS SNS Service")