from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/trickyelements.html")

element_1 = driver.find_element_by_id("element1")
element_2 = driver.find_element_by_id("element2")
element_3 = driver.find_element_by_id("element3")
element_4 = driver.find_element_by_id("element4")
element_5 = driver.find_element_by_id("element5")
result = driver.find_element_by_id("result")
button_element_exist = 0

for i in (element_1, element_2, element_3, element_4, element_5):
    if i.tag_name == "button":
        button_element_exist = 1
        i.click()
        if i.text in result.text:
            print("A vizsgált elemben az elvárt felirat jelenik meg:", "\n",  i.text.strip(), "was clicked")
            break
        else:
            print("A vizsgált elemben nem jó felirat jelenik meg:", "\n", i.text.strip(), "was clicked")
            break
    else:
        continue

if button_element_exist == 0:
    print("Az oldalon nem jelenik meg gomb típusú elem")
else:
    pass
