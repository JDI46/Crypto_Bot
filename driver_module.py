###after I figure out the search words class, take line 6, 7, 8 and make a different python then import the driver as a module
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

#maybe i need to add object functions to the whole driver then access the methods in a different module, then mutli thread it or async
class Driver:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def start_driver(self):
        if self.driver:
            return self.driver
        else:
            raise ValueError("Driver doesn't work")

    def get_website(self, url):
        #this is hardcoded due to me getting errors from creating and element on the get title call at the bottom
        #I only want to use youtube for my research question
        url = "https://www.youtube.com/"
        try:
            self.driver.get(url)
            time.sleep(10)
        except:
            raise ValueError("Time out")

            

    def quit_driver(self):
        return self.driver.quit()


c = Driver()
c.start_driver()
c.get_website()
c.quit_driver()
