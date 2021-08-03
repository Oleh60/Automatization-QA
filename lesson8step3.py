from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os



# link = "http://suninjuly.github.io/alert_accept.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)

# def calc(x):
#     return str(math.log(abs(12*math.sin(x))))



# try:
#     browser.find_element_by_xpath('//button[contains(text(),"I want to go")]').click()
#     allert = browser.switch_to.alert
#     allert.accept()
#     x_element = browser.find_element_by_xpath('//span[@id = "input_value"]').text
#     x = int(x_element)
#     a = calc(x)
#     browser.find_element_by_xpath('//input[@id = "answer"]').send_keys(a)
#     browser.find_element_by_xpath('//button[@type = "submit"]').click()
#     allert1 = browser.switch_to.alert
#     allert_text = allert1.text
# finally:
#     print(allert_text.split("quiz: ")[1])
#     browser.quit()



link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

try:
    browser.find_element_by_xpath('//button[@type = "submit"]').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x_element = browser.find_element_by_xpath('//span[@id = "input_value"]').text
    x = int(x_element)
    a = calc(x)
    browser.find_element_by_xpath('//input[@id = "answer"]').send_keys(a)
    browser.find_element_by_xpath('//button[text() = "Submit"]').click()
    allert = browser.switch_to.alert.text
finally:
    print(allert.split("quiz: ")[1])
    browser.quit()
