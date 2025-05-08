from RecaptchaSolver import RecaptchaSolver
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


# Initialize the WebDriver options
chrome_options = Options()
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
chrome_options.add_experimental_option('useAutomationExtension', False)


driver_path = ChromeDriverManager().install()
if driver_path:
    driver_name = driver_path.split('/')[-1]
    if driver_name!="chromedriver":
        driver_path = "/".join(driver_path.split('/')[:-1]+["chromedriver"])
        os.chmod(driver_path, 0o755)
driver = webdriver.Chrome(service=Service(driver_path),options=chrome_options)


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
