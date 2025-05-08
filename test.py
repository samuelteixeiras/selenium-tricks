from RecaptchaSolver import RecaptchaSolver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Initialize the WebDriver options
# options = webdriver.ChromeOptions()
chrome_options = Options()

chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--headless')

chrome_options.add_argument("--log-level=3")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.binary_location = '/usr/bin/chromium' 

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.google.com/recaptcha/api2/demo")
recaptchaSolver = RecaptchaSolver(driver)

try:
    # Perform CAPTCHA solving
    t0 = time.time()
    recaptchaSolver.solveCaptcha()
    print(f"Time to solve the captcha: {time.time() - t0:.2f} seconds")

except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
