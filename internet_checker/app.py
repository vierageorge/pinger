import logging
from internet_checker.services.io_service import get_status, set_status
from internet_checker.services.network_service import get_internet_status

logger = logging.getLogger(__name__)

def run():
    logger.info("Process STARTED")
    previous_status = get_status()
    current_status = get_internet_status()

    if previous_status == current_status:
        logger.info(f"Nothing has changed. Current status: {current_status}")
    else:
        logger.info("INTERNETS BACK, BABY" if current_status == "OK" else "WE LOST CONNECTION")
        set_status(current_status)
    logger.info("Process COMPLETED")