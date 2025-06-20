# test_inventory_ui.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_amazon_inventory_search():
    # Set up the browser
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.amazon.com")

    # Search for "laptop"
    search_box = driver.find_element(By.ID, "twotabsearchtextbox")
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    # Check if the search results page title contains the keyword
    assert "laptop" in driver.title.lower()

    # Close the browser
    driver.quit()
