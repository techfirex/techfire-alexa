from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gmail_sign_in(email, password):
    driver = webdriver.Chrome(executable_path=r"C:\Users\tushar\Downloads\chromedriver_win32\chromedriver.exe")

    driver.get('https://stackoverflow.com/users/signup?ssrc=head&returnurl=%2fusers%2fstory%2fcurrent')

    driver.find_element_by_xpath('//*[@id="openid-buttons"]/button[1]').click()

    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(email)

    input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="identifierNext"]/span/span'))
    )
    input.click()

    driver.implicitly_wait(1)

    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)

    input = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="passwordNext"]/span/span'))
    )
    input.click()
    driver.implicitly_wait(1)
    driver.get('https://www.google.com/')

email = "##########@gmail.com"
password = "#######"
gmail_sign_in(email, password)