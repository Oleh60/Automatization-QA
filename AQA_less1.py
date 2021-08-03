import time
from selenium import webdriver

# driver = webdriver.Chrome("C:\\CD\\chromedriver.exe")
#
#
#
# driver.get("https://stepik.org/lesson/25969/step/12")
# time.sleep(5)
#
# textrea = driver.find_element_by_css_selector(".textarea")
#
# textrea.send_keys('get("https://stepik.org/lesson/25969/step/12")')
# time.sleep(5)
#
# submit_button = driver.find_element_by_css_selector(".submit-submission")
#
# submit_button.click()
# time.sleep(5)
#
# driver.quit()
# options = webdriver.ChromeOptions()
# options.add_argument("--start-maximized")
#
# driver = webdriver.Chrome("C:\\CD\\chromedriver.exe",options = options)
#
#
# driver.get("https://developer.mozilla.org/ru/docs/Web/CSS/Attribute_selectors")
# time.sleep(5)
#
# driver.find_element_by_xpath('//summary[text() = "CSS макет"]/../..').click()
#
# driver.find_element_by_xpath('//a[contains(@href ,"Flexbox")]').click()
#
# flexbox = driver.find_element_by_xpath('//h1[text() = "Flexbox"]').text
#
# assert flexbox,"Flexbox1"
#
# driver.quit()


link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
    browser.get(link)

    input1 = browser.find_element_by_tag_name('div:nth-child(1) > input')
    input1.send_keys("Oleh")
    input2 = browser.find_element_by_name('//input[@name="last_name"]')
    input2.send_keys("Romanyshyn")
    input3 = browser.find_element_by_class_name('//input[contains(@class,"form-control city")]')
    input3.send_keys("Lviv")
    input4 = browser.find_element_by_id('//input[@id="country"]')
    input4.send_keys("Ukraine")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()