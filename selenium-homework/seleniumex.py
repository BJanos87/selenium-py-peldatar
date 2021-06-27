from selenium import webdriver

driver = webdriver.Chrome()

def not_exist_element():
    print("A keresett elem az oldalon nem létezik")

driver.get("https://w3schools.com")

try:
    driver.find_element_by_id("nemletezik")

except:
    not_exist_element()

driver.close()

