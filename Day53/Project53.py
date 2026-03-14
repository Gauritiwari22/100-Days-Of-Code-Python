import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

URL="https://appbrewery.github.io/Zillow-Clone/"
FORM_URL="YOUR_GOOGLE_FORM_LINK"

response=requests.get(URL)

soup=BeautifulSoup(response.text,"html.parser")


addresses=[address.getText().strip() for address in soup.select(".StyledPropertyCardDataWrapper address")]
prices=[price.getText().split("+")[0] for price in soup.select(".StyledPropertyCardDataWrapper span")]
links=[link["href"] for link in soup.select(".StyledPropertyCardDataWrapper a")]

driver=webdriver.Chrome()

for n in range(len(addresses)):

    driver.get(FORM_URL)
    time.sleep(2)


    address_input=driver.find_element(By.XPATH,"XPATH_ADDRESS")
    price_input=driver.find_element(By.XPATH,"XPATH_PRICE")
    link_input=driver.find_element(By.XPATH,"XPATH_LINK")

    address_input.send_keys(addresses[n])
    price_input.send_keys(prices[n])
    link_input.send_keys(links[n])



    submit_button=driver.find_element(By.XPATH,"XPATH_SUBMIT")
    submit_button.click()


    time.sleep(2)