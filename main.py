from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        self.driver.get("http://youtube.com")

    def title(self):
       print(self.driver.title())

# def search_videos():
#     elem = driver.find_element(By.NAME, "Coding Advice")
#     time.sleep(10)
#     print(elem)

# search_videos()

Driver()