"""Selenium Base Page"""

# Selenium
from selenium.webdriver import Firefox
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains

# Utilities
import os
import sys
import time


class BasePage:
    """Base Page class for Selenium"""

    def __init__(self, timeout):
        """Constructor with specific timeout"""
        PROFILE = FirefoxProfile()

        FIREFOX_OPTS = Options()
        FIREFOX_OPTS.headless = False

        dir_path = os.path.dirname(os.path.realpath(__file__))
        if 'linux' in sys.platform:
            EXECUTABLE_PATH = os.path.join(dir_path, "../../drivers/linux/geckodriver")
        else:
            EXECUTABLE_PATH = os.path.join(dir_path, "../../drivers/windows/geckodriver")
        ff_opt= {
            "firefox_profile": PROFILE,
            "options": FIREFOX_OPTS,
            "executable_path": EXECUTABLE_PATH
        }
        self.driver = Firefox(**ff_opt)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout=timeout)
        self.actions = ActionChains(self.driver)

    def open_url(self, url):
        """Open an specific url"""
        self.driver.get(url)

    def find(self, locator) -> WebElement:
        """Find an element using an specific Xpath"""
        time.sleep(0.15)
        element = self.wait.until(expected_conditions.presence_of_element_located(locator=(By.XPATH, locator)))
        time.sleep(0.15)
        return element

    def find_elements(self, locator) -> list:
        """Find an element list using an specific Xpath"""
        time.sleep(0.15)
        elements = self.wait.until(expected_conditions.presence_of_all_elements_located(locator=(By.XPATH, locator)))
        time.sleep(0.15)
        return elements

    def click_element(self, locator):
        """Click an specific element"""
        self.actions.click(self.find(locator)).perform()

    def right_click_element(self, locator):
        """Right click an specific element"""
        self.actions.context_click(self.find(locator)).perform()

    def write(self, locator, text):
        """Write in specific element"""
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def close(self):
        """Close the browser"""
        self.driver.close()
