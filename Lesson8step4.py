import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from selenium.webdriver.support.ui import Select
import math
import os

# link = "http://suninjuly.github.io/wait1.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.implicitly_wait(5)
#
# browser.get(link)
#
#
# browser.find_element_by_xpath('//button[@id = "verify"]').click()
#
# massage = browser.find_element_by_xpath('//div[contains(text(), "Verification")]')
# assert "successful" in massage.text
#
# browser.quit()


# link = "http://suninjuly.github.io/cats.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
#
# try:
#     browser.find_element_by_id("button")
#
# finally:
#     browser.quit()

#browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# link = "http://suninjuly.github.io/wait2.html"
#
# browser.implicitly_wait(5)
#
# browser.get(link)
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text

# link = "http://suninjuly.github.io/wait2.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
# browser.get(link)

# try:
#     button = WebDriverWait(browser, 5).until(
#         EC.element_to_be_clickable((By.ID, "verify"))
#     )
#
#     button.click()
#     massage = browser.find_element_by_id("verify_message")
#
#     assert "successful" in massage.text
# finally:
#     browser.quit()


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
browser.get(link)


try:
    value = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), '$100')
    )
    if value == True:
        browser.find_element_by_xpath('//button[@id = "book"]').click()

        x = browser.find_element_by_xpath('//span[@id = "input_value"]').text
        y = str(math.log(abs(12*math.sin(int(x)))))

        browser.find_element_by_xpath('//input[@id = "answer"]').send_keys(y)
        browser.execute_script("window.scrollBy(0,100);")
        browser.find_element_by_xpath('//button[@id = "solve"]').click()

        allert = browser.switch_to.alert.text
finally:
    print(allert.split("quiz: ")[1])
    browser.quit()





