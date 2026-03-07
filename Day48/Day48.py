# "Day 48"

# Library used:
# Selenium - control a real browser

# Selenium allows Python to:
# Open a browser
# Click buttons
# Type into inputs
# Navigate pages
# Extract information


# Finding Elements
# Selenium can locate elements using different strategies.
# example : By ID	            find_element(By.ID, "name")
#           By Class	        find_element(By.CLASS_NAME, "class")


# Clicking Elements
# Example:
# button = driver.find_element(By.ID, "submit")
# button.click()
# This simulates a real user click.


# Typing Into Inputs
# Example:
# search = driver.find_element(By.NAME, "q")
# search.send_keys("Python")
# Equivalent to typing on keyboard.


# Closing the Browser
# Always close the browser when done.
# driver.quit()