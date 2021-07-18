# Beimportálom a szükséges komponenseket, és beállítom a driver-t
from selenium import webdriver
import time
import csv

driver = webdriver.Chrome()

# Az input mezők törlésére használt függvény deklarálása
def clear_input():
    name.clear()
    email.clear()
    dob.clear()
    phone.clear()

# Az oldal megnyitásra kerül
try:
    driver.get("http://localhost:9999/another_form.html")

# A teszt során a használandó elemek letárolása változókba
    name = driver.find_element_by_id("fullname")
    email = driver.find_element_by_id("email")
    dob = driver.find_element_by_id("dob")
    phone = driver.find_element_by_id("phone")
    send = driver.find_element_by_id("submit")
    button = driver.find_element_by_xpath("/html/body/main/div/button")

# Az űrlap kitöltése a megnyitott CSV file adatokkal
    with open("table_in.csv", 'r', encoding="UTF-8") as orig_file:
        read_file = csv.reader(orig_file, delimiter=",")
        next(read_file)
        for line in read_file:
            clear_input()
            name.send_keys(line[0].strip())
            email.send_keys(line[1].strip())
            dob.send_keys(line[2].strip())
            phone.send_keys(line[3].strip())
            send.click()
        button.click()
        time.sleep(3)
    orig_file.close()

# Az eredeti és a letöltött fájl tartalmának összeshasonlítása
    with open ("C:\\Users\\JANNA\\Downloads\\table.csv", 'r', encoding="UTF-8") as downloaded_file, \
            open ("table_in.csv", 'r', encoding="UTF-8") as orig_file:
        file_one = orig_file.readlines()
        file_two = downloaded_file.readlines()
        for i in range(5):
            assert file_one[i].replace(", ", ",").replace("Phone,", "Phone") == \
                   file_two[i].replace(", ", ",").replace("Phone,", "Phone"), "A két file tartalma nem egyezik"
        print("A két file tartalma egyezik (kisebb formai változtatással)")
    orig_file.close()
    downloaded_file.close()

except Exception as Error:
    print("A teszt lefuttatáse nem sikerült")

# Megnyitott oldal bezárásra kerül
finally:
    driver.close()






