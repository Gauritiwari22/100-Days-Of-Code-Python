from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&keywords=python%20developer")

time.sleep(3)

email = driver.find_element(By.ID, "username")
email.send_keys("your_email")

password = driver.find_element(By.ID, "password")
password.send_keys("your_password")
password.send_keys(Keys.ENTER)

time.sleep(5)

jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container")

for job in jobs:

    job.click()
    time.sleep(2)

    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button")
        apply_button.click()

        time.sleep(2)

        submit_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Submit application']")
        submit_button.click()

        print("Application submitted")

    except:
        print("Skipped job")

driver.quit()