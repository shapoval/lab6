import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
time.sleep(5)
textinput = driver.find_element_by_name("q")
textinput.send_keys("Журенков")
submit_button = driver.find_element_by_css_selector(".gNO89b")
submit_button.click()
time.sleep(10)
driver.quit()
