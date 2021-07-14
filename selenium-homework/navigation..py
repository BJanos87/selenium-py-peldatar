from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get("http://localhost:9999/general.html")

anchors = driver.find_elements_by_xpath("//a")
home_window = driver.current_window_handle

for anchor in anchors:
    url = anchor.get_attribute("href")
    print(url)
    if anchor.get_attribute("target") == "_blank":
        anchor.click()
        driver.switch_to.window(driver.window_handles[1])
        driver.close()
        driver.switch_to.window(home_window)
    else:
        anchor.click()
        if driver.current_url.__contains__("localhost"):
            continue
        else:
            js = "window.open('https://www.google.com','_blank','width=1080,height=800,menubar=no,toolbar=no, status=no,scrollbars=yes')"
            driver.execute_script(js)
            driver.back()
            driver.switch_to.window(driver.window_handles[1])
            driver.close()
            driver.switch_to.window(home_window)

#driver.close()




