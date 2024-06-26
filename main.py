from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument('--no-sandbox') # disable chrome sandbox
chrome_options.add_argument('--headless') # run without UI , background
# /dev/shm default memory that will be disabled, /tmp will be used instead
chrome_options.add_argument('--disable-dev-shm-usage') 
 

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://google.com")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "L2AGLb"))
)
element = driver.find_element(By.ID, "L2AGLb")
element.click()


WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("samuel teixeira" + Keys.ENTER)
time.sleep(2)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Samuel Teixeira - HubSpot"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Samuel Teixeira - HubSpot")
link.click()

time.sleep(10)

driver.quit()