from os import system
from sys import argv
import logging

logger = logging.getLogger(__name__)
DEFAULT_VALIDATION_HOSTNAME = "www.google.com"

def get_validation_hostname():
    return argv[1] if len(argv) > 1 else DEFAULT_VALIDATION_HOSTNAME

def get_internet_status():
    response = system(f"ping -c 1 -t 3 {get_validation_hostname()} >/dev/null 2>&1")
    if response == 0: return "OK"
    return "FAIL"