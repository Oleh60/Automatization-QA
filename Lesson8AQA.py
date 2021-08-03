from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import math
import os


# def calc(a,b):
#     x = int(a) + int(b)
#     return str(x)



# link = "http://suninjuly.github.io/selects2.html"
# link = "https://SunInJuly.github.io/execute_script.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)

# try:
    # a_element = browser.find_element_by_xpath('//span[@id = "num1"]').text
    # a = a_element
    # b_element = browser.find_element_by_xpath('//span[@id = "num2"]').text
    # b = b_element
    # y = calc(a,b)
    #
    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(y)
    # browser.find_element_by_xpath('//button[text() = "Submit"]').click()

    #
    # button = browser.find_element_by_tag_name("button")
    # button.click()
# finally:
#     time.sleep(8)
#     browser.quit()
# def calc1(x):
#     return str(math.log(abs(12*math.sin(int(x)))))
#
# link = "http://suninjuly.github.io/execute_script.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)
#
#
# try:
#     x = browser.find_element_by_xpath('//span[@id = "input_value"]').text
#     a = calc1(x)
#     b = browser.find_element_by_xpath('//button[text() = "Submit"]')
#     browser.find_element_by_xpath('//*[@id = "answer"]').send_keys(a)
#     browser.execute_script("return arguments[0].scrollIntoView(true);", b)
#     browser.find_element_by_xpath('//*[contains(@type,"checkbox")]').click()
#     browser.find_element_by_xpath('//input[@id = "robotsRule"]').click()
#     b.click()
# finally:
#     time.sleep(8)
#     browser.quit()

