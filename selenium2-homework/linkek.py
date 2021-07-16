# Beimportálom a szükséges komponenseket, és beállítom a driver-t
from selenium import webdriver

driver = webdriver.Chrome()

# Az oldal megnyitásra kerül, és kigyűjtöm az oldalon található összes anchor típusú elemet az anchors változóba
try:
    driver.get("http://localhost:9999")
    anchors = driver.find_elements_by_tag_name("a")
    url_list = []

# Végig iterálok az anchor elemeken és kigyűjtöm egy listába az url-eket (href attribútum)
    for anchor in anchors:
        href = anchor.get_attribute("href")
        url_list.append(href)

# Létrehozok egy új fájlt és beleírom az előzőleg kigyűjtött url-eket
    with open("url_list.txt", "w") as file:
        for link in url_list:
            file.write(f'{link} \n')
    file.close()

# A teszt végén kiiratom a talált linkek számát a kimenetre
    url_counter = len(url_list)
    print(f'Az oldalon talált linkek száma: {url_counter}')

except Exception as Error:
    print("A teszt lefuttatáse nem sikerült")

# Megnyitott oldal bezárásra kerül
finally:
    driver.close()
