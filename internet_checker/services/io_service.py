import logging

logger = logging.getLogger(__name__)
CURRENT_STATUS_FILE_NAME = "currentstatus"
VALID_STATUSES = ["OK", "FAIL"]

def get_status():
    with open(CURRENT_STATUS_FILE_NAME, 'r') as file:
        data = file.read()
    return data

def set_status(status):
    if status not in VALID_STATUSES:
        logger.error(f"Trying to set an invalid status: {status}. Valid are {', '.join(VALID_STATUSES)}")
        return
    with open(CURRENT_STATUS_FILE_NAME, 'w') as file:
        file.write(f"{status}")
