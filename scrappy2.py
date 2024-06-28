from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


options = Options()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')
# why are you doing this? 
driver = webdriver.Remote("http://selenium:4444/wd/hub", options=options)

driver.get("https://google.com")
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, "L2AGLb"))
)
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.ID, "L2AGLb"))
)
driver.get_screenshot_as_file('google1.png') 
element = driver.find_element(By.ID, "L2AGLb")
element.click()
driver.get_screenshot_as_file('google2.png') 


WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("samuel teixeira" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Samuel Teixeira - HubSpot"))
)

link = driver.find_element(By.PARTIAL_LINK_TEXT, "Samuel Teixeira - HubSpot")
link.click()
time.sleep(3)
body = driver.find_element(By.XPATH, "/html/body")
WebDriverWait(body, 5).until(
    EC.presence_of_element_located((By.XPATH, "/html/body"))
)

print(body.get_attribute('innerHTML'))
driver.get_screenshot_as_file('link.png') 
time.sleep(3)

driver.quit()