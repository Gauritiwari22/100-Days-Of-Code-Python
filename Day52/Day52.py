from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

USERNAME="your_username"
PASSWORD="your_password"

driver=webdriver.Chrome()

driver.get("https://www.instagram.com/accounts/login/")
time.sleep(5)

username_input=driver.find_element(By.NAME,"username")
password_input=driver.find_element(By.NAME,"password")

username_input.send_keys(USERNAME)
password_input.send_keys(PASSWORD)
password_input.send_keys(Keys.ENTER)

time.sleep(5)

driver.get("https://www.instagram.com/instagram/")
time.sleep(5)

followers_button=driver.find_element(By.XPATH,"//a[contains(@href,'followers')]")
followers_button.click()

time.sleep(5)

followers_popup=driver.find_element(By.XPATH,"//div[@role='dialog']//ul")

for i in range(5):
    driver.execute_script(
        "arguments[0].scrollTop = arguments[0].scrollHeight",
        followers_popup
    )
    time.sleep(2)

follow_buttons=driver.find_elements(By.XPATH,"//button[text()='Follow']")

for button in follow_buttons:
    try:
        button.click()
        time.sleep(1)
    except:
        pass

driver.quit()