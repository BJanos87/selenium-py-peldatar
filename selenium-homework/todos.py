from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://localhost:9999/todo.html")

todos = driver.find_elements_by_xpath("//span [@class='done-false']")

for to_do in todos:
    print(to_do.text)

driver.close()

