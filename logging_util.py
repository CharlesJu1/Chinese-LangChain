import logging
import os
import sys

def loggingSetup(logfile_name):
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)

    # console handler
    logFormatter = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
    consoleHandler = logging.StreamHandler(sys.stdout)
    consoleHandler.setFormatter(logFormatter)
    consoleHandler.setLevel(logging.DEBUG)
    rootLogger.addHandler(consoleHandler)

    # file handler
    os.makedirs(os.path.dirname(logfile_name), exist_ok=True)
    fileHandler = logging.FileHandler(logfile_name)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

if __name__ == '__main__':
    loggingSetup("./logs/log1.txt")
    logging.info("this is a test logging message")