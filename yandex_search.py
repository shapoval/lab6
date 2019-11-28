import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://yandex.ru/")
time.sleep(5)
textinput = driver.find_element_by_css_selector(".input__input")
textinput.send_keys("Журенков")
submit_button = driver.find_element_by_css_selector(".search2__button")
submit_button.click()
time.sleep(10)
driver.quit()