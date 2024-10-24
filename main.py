from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#calls driver to start working


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start_driver(self):
        if self.driver:
            return self.driver
        else:
            raise ValueError("Driver doesn't work")

    def get_title(self):
        self.driver.get('https://www.youtube.com/')
        title = self.driver.title
        print(title)

    def quit_driver(self):
        return self.driver.quit()


driver = Driver()
title = driver.get_title()
print(title)
