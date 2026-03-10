from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

TWITTER_EMAIL="your_email"
TWITTER_PASSWORD="your_password"

PROMISED_DOWN=100
PROMISED_UP=20


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver=webdriver.Chrome()
        self.down=0
        self.up=0


    def get_internet_speed(self):

        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)


        go_button = self.driver.find_element(By.CLASS_NAME,"start-text")
        go_button.click()

        time.sleep(60)

        self.down=self.driver.find_element(By.CLASS_NAME,"download-speed").text
        self.up=self.driver.find_element(By.CLASS_NAME,"upload-speed").text


    def tweet_at_provider(self):

        self.driver.get("https://twitter.com/login")

        time.sleep(5)

        email=self.driver.find_element(By.NAME,"text")
        email.send_keys(TWITTER_EMAIL)
        email.send_keys(Keys.ENTER)

        time.sleep(5)

        password=self.driver.find_element(By.NAME,"password")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(5)

        tweet_box=self.driver.find_element(By.CSS_SELECTOR, "div[aria-label='Tweet text']")
        tweet =f"My internet speed is{self.down}down/{self.up}up but I pay for {PROMISED_DOWN}down/{PROMISED_UP}up."

        tweet_box.send_keys(tweet)
        tweet_box.send_keys(Keys.CONTROL, Keys.ENTER)


bot=InternetSpeedTwitterBot()

bot.get_internet_speed()

if float(bot.down)<PROMISED_DOWN or float(bot.up)<PROMISED_UP:
    bot.tweet_at_provider()