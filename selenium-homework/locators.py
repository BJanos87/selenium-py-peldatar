from selenium import webdriver
driver = webdriver.Chrome()

driver.get("http://localhost:9999/kitchensink.html")

bmw_radio_button = driver.find_element_by_xpath("//fieldset/label[@for='bmw']/input[@id='bmwradio']")
honda_select = driver.find_element_by_xpath("html/body/div[2][@class='block large-row-spacer']/div[@class='cen-left-align']/fieldset/select[@id='carselect']/option[3][@value='honda']")
open_window = driver.find_element_by_xpath("html//div[@class='block large-row-spacer']//fieldset/button[contains(text(),'Open Window')]")
enter_your_name = driver.find_element_by_xpath("//div[3][contains(@class,'cen-right-align')]//input[1][contains(@placeholder,'Enter Your Name') and contains(@name,'enter-name')]")
python_programming = driver.find_element_by_xpath("//div[@class='left-align']/fieldset/table[contains (@id,'product') and contains (@border,'1')]//tr[3]/td[contains (text(),'Python Programming')]")

print(bmw_radio_button.get_attribute("value"))
print(honda_select.text)
print(open_window.tag_name)
print(enter_your_name.get_attribute("class"))
print(python_programming.text)

driver.close()

