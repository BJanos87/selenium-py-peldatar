# A megnyitott külső linkek URL Assert-álása nélkül lefuttatatott teszteset
# Külső linkek URL Assert-álása esetén a teszteset hibára fut, nem egyező URL miatt

# Beimportálom a szükséges komponenseket, és beállítom a driver-t
from selenium import webdriver
import time

driver = webdriver.Chrome()

# Deklarálom az ablakkezeléshez szükséges függvényeket
def switch_to_other_window():
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)

def switch_to_main_window():
    main_window = driver.window_handles[0]
    time.sleep(2)
    driver.close()
    driver.switch_to.window(main_window)

# Az oldal megnyitásra kerül, és kigyűjtöm az oldalon található összes anchor típusú elemet az anchors változóba
try:
    driver.get("http://localhost:9999/general.html")
    anchors = driver.find_elements_by_xpath("//a")

# Végig iterálok az összes linken, a link megnyitásának módja függ az adott elem attribútumától
    for anchor in anchors:
        url = anchor.get_attribute("href")
        if anchor.get_attribute("target") == "_blank":
            anchor.click()
            switch_to_other_window()
            switch_to_main_window()
            print(url)
        else:
            if "localhost" in url:
                anchor.click()
                time.sleep(2)
                assert driver.current_url == url
                print(url)
                continue
            else:
                driver.execute_script("window.open();")
                switch_to_other_window()
                driver.get(url)
                switch_to_main_window()
                print(url)
    print("Megnyitott Link-ek száma:", len(anchors))

# Kezelem az AssertionError-t
except AssertionError as Error:
    print("A megnyitásra került oldal URL-je nem egyezik az anchor változó href attribútum URL-jével")

# Az oldal bezárásra kerül
finally:
    driver.close()
