from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new Safari session
driver = webdriver.Chrome()

driver.get("https://www.google.com")

#WebDriverWait(driver, 5).until(
#    EC.presence_of_all_elements_located((By.NAME, "gLFyf"))
#)

input_element = driver.find_element(By.NAME, "q")
input_element.send_keys("testing" + Keys.ENTER)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "search"))
)

links = driver.find_elements(By.PARTIAL_LINK_TEXT, "COVID")

time.sleep(5)

for link in links:
    print(link.get_attribute('href'))

driver.quit()