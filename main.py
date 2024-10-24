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
        time.sleep(10)
        return self.driver

    def quit_driver(self):
        return self.driver.quit()



class SearchWeb:
    def __init__(self, search_website):
        self.search_website = search_website

    #pass self to it, then take in a search button object, string
    def activate_search_button(self):
        pass
    
    #takes in search word parameters after activating previous function
    #also needs to have a sleep time in order to have enough time to find the words
    def search_words(self):
        pass



driver = Driver()
title = driver.get_title()
print(title)


find_button = driver.find_eleme