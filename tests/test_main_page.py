import os
import time
from selenium import webdriver

BASE_DIR=os.path.dirname(os.path.dirname(__file__))
DRIVER_PATH=os.path.join(BASE_DIR, 'chromedriver.exe')
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('http//demoqa.com')
time.sleep(2)
driver.quit()
