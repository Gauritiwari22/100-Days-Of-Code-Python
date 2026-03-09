from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://tinder.com")

time.sleep(5)

login_button = driver.find_element(By.XPATH, '//a[text()="Log in"]')
login_button.click()

time.sleep(5)

for i in range(50):

    try:
        like_button = driver.find_element(By.XPATH, '//button[@aria-label="Like"]')
        like_button.click()
        time.sleep(2)

    except:
        print("Profile not found")

driver.quit()