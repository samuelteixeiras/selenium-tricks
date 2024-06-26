from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import FirefoxOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = FirefoxOptions();
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# why are you doing this? 
driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

driver.get("https://google.com")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "L2AGLb"))
)
element = driver.find_element(By.ID, "L2AGLb")
element.click()


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
time.sleep(5)
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Samuel Teixeira - HubSpot"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Samuel Teixeira - HubSpot")
link.click()

time.sleep(10)
driver.quit()