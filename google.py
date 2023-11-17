from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\tushar\Downloads\chromedriver_win32\chromedriver.exe")
driver.get("http://gmail.com")
time.sleep(5)
driver.find_element_by_id("identifierId").send_keys('#########')
time.sleep(2)
driver.find_element_by_id("identifierNext").click()
time.sleep(5)
driver.find_element_by_name("password").send_keys('##########')
driver.find_element_by_id("passwordNext").click()
time.sleep(5)

# driver.get("https://accounts.google.com/SignOutOptions?hl=en&continue=https://mail.google.com/mail&service=mail")
# driver.find_element_by_xpath('//button[normalize-space()="Sign out"]').click()
# driver.close()