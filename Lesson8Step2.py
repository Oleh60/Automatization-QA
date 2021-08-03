from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os

# link = "http://suninjuly.github.io/file_input.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)
#
# try:
#     browser.find_element_by_xpath('//input[@name = "firstname"]').send_keys("Oleh")
#     browser.find_element_by_xpath('//input[@name = "lastname"]').send_keys("Roman")
#     browser.find_element_by_xpath('//input[@name = "email"]').send_keys("123@gmile")
#
#     current_dir = os.path.abspath(os.path.dirname(__file__))
#     file = os.path.join(current_dir,"text_Test.txt")
#     browser.find_element_by_xpath('//input[@id = "file"]').send_keys(file)
#     browser.find_element_by_xpath('//button[text() = "Submit"]').click()
# finally:
#     time.sleep(8)
#     browser.quit()
# print(os.path.abspath(os.path.dirname(__file__)))