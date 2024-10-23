from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#calls driver to start working
class Driver:
    def __init__(self):
        self.driver = None

    def start_driver(self, driver="chrome"):
        if not self.driver:
            if self.driver == "chrome":
                self.driver == webdriver.Chrome()
            else:
                raise ValueError("Invalid Browser")

    def stop_driver(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
    
    def navigate_url(self, url):
        if not self.driver:
            return
        self.driver.get(url)

    def get_title(self):
        if not self.driver:
            return None
        return self.driver.title
    

Driver()
#needs to get website name



class GetHTML:
    video_data = {}
    def __init__(self, video_html):
        pass

    def title_html(self):
        pass

    def looped_data():
        pass


