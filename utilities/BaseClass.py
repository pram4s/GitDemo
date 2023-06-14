import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getlogger(self):
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)
        # logger = logging.getLogger(__name__)
        filehandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        filehandler.setFormatter(formatter)
        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(filehandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verifylinkpresence(self, text, time):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def selectoptionbytext(self, locator, text):
        dd = Select(locator)  # homepage.getgender() is replaced with locator
        dd.select_by_visible_text(text)
