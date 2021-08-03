import time
from selenium import webdriver
import math

# def calc(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/math.html"
#
#
#
#
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)
# try:
#     x_element = browser.find_element_by_xpath('//span[@id="input_value"]')
#     x = x_element.text
#     y = calc(x)
#     browser.find_element_by_xpath('//input[@id = "answer"]').send_keys(y)
#     browser.find_element_by_xpath('//input[@id = "robotCheckbox"]').click()
#     browser.find_element_by_xpath('//input[@id = "robotsRule"]').click()
#     browser.find_element_by_xpath('//button[text() = "Submit"]').click()
# #
#
# finally:
#     time.sleep(10)
#     browser.quit()

# link = "http://suninjuly.github.io/math.html"
#
#
#
#
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)

# people_radio = browser.find_element_by_id("peopleRule")
# people_checked = people_radio.get_attribute("checked")
# print("value of people radio: ", people_checked)
# assert people_checked == "true", "People radio is not selected by default"
# assert people_checked is not None, "People radio is not selected by default"

# robots_radio = browser.find_element_by_id("robotsRule")
# robots_checked = robots_radio.get_attribute("checked")
# assert robots_checked is None
# #
# #
# time.sleep(10)
# browser.quit()


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"




browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
browser.get(link)

try:
    x_element = browser.find_element_by_id('treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)
    browser.find_element_by_xpath('//input[@id="answer"]').send_keys(y)
    browser.find_element_by_class_name('check-input').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_xpath('//button[text() ="Submit"]').click()

finally:
    time.sleep(8)
    browser.quit()