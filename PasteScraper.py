import argparse
import logging
import threading
from logging import handlers
from time import sleep
import sys

from Pastebin import Pastebin
from config import logfile

# TODO search for PRODUCTION and make fixes before release

def monitor():

    argparser = argparse.ArgumentParser()
    argparser.add_argument("-v", help="more verbose", action="store_true")
    argparser.add_argument("--site", help="site to parse (can be 'all'", action="store")
    arguments = argparser.parse_args()

    log = logging.getLogger('')
    log.setLevel(logging.INFO)
    # PRODUCTION: FIX ME
    #if arguments.v:
    log.setLevel(logging.DEBUG)
    format = logging.Formatter("[*] [%(levelname)s] %(name)s : %(message)s")
    logging.getLogger("requests").setLevel(logging.WARNING)

    consoleHandler = logging.StreamHandler(stream=sys.stdout)
    consoleHandler.setFormatter(format)
    log.addHandler(consoleHandler)

    # PRODUCTION: Consider removing this
    with open(logfile, 'w') as file:
        file.truncate()
    fileHandler = logging.FileHandler(logfile)
    fileHandler.setFormatter(format)
    log.addHandler(fileHandler)

    Pastebin().monitor()

    #pastebin_thread.daemon = True
    #pastebin_thread.start()

    try:
        while True:
            sleep(5)
    except KeyboardInterrupt:
        logging.warn('Caught keyboard interrupt. Stopping!')


if __name__ == "__main__":
    monitor()