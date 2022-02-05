import logging
from internet_checker.services.io_service import get_status, set_status
from internet_checker.services.network_service import get_internet_status
from internet_checker.services.aws_service import send_notification

logger = logging.getLogger(__name__)

def run():
    logger.info("Process STARTED")
    previous_status = get_status()
    current_status = get_internet_status()

    if previous_status == current_status:
        logger.info(f"Nothing has changed. Current status: {current_status}")
    else:
        message = "WE LOST CONNECTION"
        if current_status == "OK":
            message = "INTERNETS BACK, BABY"
            send_notification("Home Notif: INTERNETS BACK, BABY")
        logger.info(message)
        set_status(current_status)
    logger.info("Process COMPLETED")