# Beimportálom a szükséges komponenseket, és beállítom a driver-t
from selenium import webdriver
import datetime
import time

driver = webdriver.Chrome()

# Az oldal megnyitásra kerül
try:
    driver.get("http://localhost:9999/forms.html")

# A teszt során a használandó elemek letárolása változókba
    date = driver.find_element_by_id("example-input-date")
    date_time = driver.find_element_by_id("example-input-date-time")
    date_time_local = driver.find_element_by_id("example-input-date-time-local")
    month = driver.find_element_by_id("example-input-month")
    week = driver.find_element_by_id("example-input-week")
    clock = driver.find_element_by_id("example-input-time")

# Űrlap kitöltése
    var_date = datetime.date(2021, 6, 5)
    date.send_keys(var_date.strftime("00%Y/%m/%d"))
    var_date_time = datetime.datetime(2012, 5, 5, 5, 5, 5, 555)
    date_time.send_keys(var_date_time.strftime("%Y.%m.%d %H:%M:%S:%f"))
    var_date_time_local = datetime.datetime(2000, 5, 12, 12, 1)
    date_time_local.send_keys(var_date_time_local.strftime("00%Y/%m/%d/%Ip/%M"))
    var_month = datetime.date(1995, 12, 10)
    month.send_keys(var_month.strftime("00%Y/%B"))
    var_week = datetime.date(2015, 12, 28)
    week.send_keys(var_week.strftime("%W/00%Y"))
    var_clock = datetime.time(12, 25, 0, 0)
    clock.send_keys(var_clock.strftime("%IH/%M"))
    time.sleep(10)

except Exception as Error:
    print("A teszt lefuttatáse nem sikerült")

# Megnyitott oldal bezárásra kerül
finally:
    driver.close()
