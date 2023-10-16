import logging
import os

class Loggen():
    @staticmethod
    def loggen():
        path = os.path.abspath(os.curdir) + "\\Logs\\" + "automation.log"
        logging.basicConfig(filename=path,
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        return logger

