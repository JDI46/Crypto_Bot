from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

def get_website():
    browser = Driver()
    return browser("https://docs.google.com/document/d/1lX8PWat-ipOWKfJr95QCCmvLM0R6WdnrzL7noaMDJHI/edit?tab=t.0")

get_website()

    
class GetHTML:
    video_data = {}
    def __init__(self, video_html):
        pass

    def title_html(self):
        pass

    def looped_data():
        pass


