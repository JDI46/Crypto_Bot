from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

#calls driver to start working
driver = webdriver.Chrome()
url = 'https://www.youtube.com/'

if driver:
    driver.get(url)
    title = driver.title
    print(title)
