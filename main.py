from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver.title


def get_title():
    test = Driver()
    my_title = test.get_driver()
    print(my_title)

get_title()