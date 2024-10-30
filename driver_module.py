###after I figure out the search words class, take line 6, 7, 8 and make a different python then import the driver as a module
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


#maybe i need to add object functions to the whole driver then access the methods in a different module, then mutli thread it or async


            
def web_driver(web, driver):
        while driver:
            time.sleep(20)
            driver.quit()
            break

        return web, driver


def website_html():
    while web_driver(website, driver):
        element = driver.find_element(By.NAME, "search")
        for i in element:
            i = element.send_keys("google")
            break
        return i, element.click()
            




class Parser:
    pass



class Storage:
    pass


class Update:
    pass


# soup = BeautifulSoup(html_doc, 'html.parser')
driver = webdriver.Chrome()
website = driver.get("https://www.google.com/")

website_html()
