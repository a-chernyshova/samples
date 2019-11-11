import datetime
import configparser
import json
import unittest
import random

import logging

LOG_PATH = ".\\logs\\"
today_weekday = datetime.datetime.today().strftime('%A')
today_date = datetime.datetime.today().strftime('%B') + " " + str(datetime.datetime.today().date())[-2:]

# read config file
config = configparser.ConfigParser()
config.read("config_example.cfg")

# retrieve credentials
USER1 = config["LOGIN_CREDS"]["USER#1"]
USER2 = config["LOGIN_CREDS"]["USER#2"]
PASSWORD = config["LOGIN_CREDS"]["PASSWORD"]

# get list from config file
DATA_LIST = json.loads(config.get("TEST_DATA", "DATA_LIST"))


class SmokeTest(unittest.TestCase):
    # define log format
    logging.basicConfig(filename=LOG_PATH + str(datetime.datetime.now())[:10] + ".txt", level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s', handler=logging.FileHandler)

    logger = logging.getLogger()
    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    @classmethod
    def set_up_class(cls):
        logging.info("Setting up class")
        logging.info("NEW SMOKE TEST RUN " + str(datetime.datetime.now())[:16])

    def test_case1(self):
        self.assertEqual("expected results", DATA_LIST[0])
        logging.info("Test case#1 PASSED")
