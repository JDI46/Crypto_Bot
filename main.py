from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


driver = webdriver.Chrome()
driver.get("http://youtube.com")
title = driver.title
driver.get("https://www.youtube.com/")


def get_title(title):
    website_title = []
    website_title.append(title)
    for word in website_title:
        print(word)

def search_videos():
    elem = driver.find_element(By.NAME, "Coding Advice")
    time.sleep(10)
    print(elem)

search_videos()
    

# get_title(title)



        