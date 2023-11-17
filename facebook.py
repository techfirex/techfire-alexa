from selenium import webdriver
import time
import re

driver = webdriver.Chrome(executable_path=r"C:\Users\tushar\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://facebook.com")

driver.find_element_by_id("email").send_keys('########')
time.sleep(5)
driver.find_element_by_id("pass").send_keys('#######')
time.sleep(5)
driver.find_element_by_name("login").click()
time.sleep(5)