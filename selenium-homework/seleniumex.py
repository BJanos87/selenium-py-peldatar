from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()

def not_exist_element():
    print("A keresett elem az oldalon nem létezik")

driver.get("https://w3schools.com")

try:
    driver.find_element_by_id("nemletezik")

except NoSuchElementException:
    not_exist_element()

driver.close()

