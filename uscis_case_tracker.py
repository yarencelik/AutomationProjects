# This script automates the process to track applications made to USCIS
# 
#
# PERSONAL USE ONLY

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

chrome_driver_path = r"C:\\Users\\user\\Desktop\\chromedriver-win64\\chromedriver.exe" # Path to local Chrome Driver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")  
chrome_options.add_argument("--no-sandbox")  
chrome_options.add_argument("--disable-dev-shm-usage")  
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  


driver = webdriver.Chrome(options=chrome_options)

driver.get('https://egov.uscis.gov')  


input_element = driver.find_element(By.ID, 'receipt_number')  
input_element.send_keys('') # Input: The receipt number - a unique 13-character identifier that consists of three letters and 10 numbers to track your immigration application to USCIS.


input_element.submit()

time.sleep(15)

page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')

element_id = 'landing-page-header'  

selected_element = soup.find(id=element_id)


if selected_element:
    xml_data = selected_element.text
    print(xml_data)
else:
    print(f"Element with ID '{element_id}' not found on the page.")


driver.quit()

while True:
    user_input = input("x")
    if user_input:
        break
