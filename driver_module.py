###after I figure out the search words class, take line 6, 7, 8 and make a different python then import the driver as a module
from bs4 import BeautifulSoup 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


#maybe i need to add object functions to the whole driver then access the methods in a different module, then mutli thread it or async


# if driver:
#     print(driver)
# else:
#     raise ValueError("Driver doesn't work")


#         #this is hardcoded due to me getting errors from creating and element on the get title call at the bottom
#         #I only want to use youtube for my research question
# try:
#     time.sleep(10)
# except:
#     raise Exception("Sleep didn't work")

            

    

def web_driver(web, driver):
        while driver:
            time.sleep(10)
            driver.quit()
            break

        return web, driver

    
        
            
def website_html():
    pass



class Parser:
    pass



class Storage:
    pass


class Update:
    pass


# soup = BeautifulSoup(html_doc, 'html.parser')
driver = webdriver.Chrome()
website = driver.get("https://coinmarketcap.com/")
web_driver(website, driver)
