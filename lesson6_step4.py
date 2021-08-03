import time
from selenium import webdriver
import math
# massege1 = str(math.ceil(math.pow(math.pi, math.e)*10000))
# print(massege1)
#
# # link = "http://suninjuly.github.io/simple_form_find_task.html"
# link1 = "http://suninjuly.github.io/find_xpath_form"
#
#
# try:
#     browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
#     browser.get(link1)
#     # input0 = browser.find_element_by_partial_link_text("224592").click()
#     input1 = browser.find_element_by_tag_name('input')
#     input1.send_keys("Oleh")
#     input2 = browser.find_element_by_name('last_name')
#     input2.send_keys("Roman")
#     input3 = browser.find_element_by_class_name('form-control.city')
#     input3.send_keys("Lviv")
#     input4 = browser.find_element_by_id('country')
#     input4.send_keys("Ukraine")
#     button = browser.find_element_by_xpath('//button[text() = "Submit"]')
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()

# try:
#     browser = webdriver.Chrome()
#     browser.get("http://suninjuly.github.io/find_xpath_form.")
#     elements = browser.find_elements_by_tag_name("input")
#     for element in elements:
#         element.send_keys("Мой ответ")
#
#     button = browser.find_element_by_css_selector("button.btn")
#     button.click()
#
# finally:
#     # успеваем скопировать код за 30 секунд
#     time.sleep(30)
#     # закрываем браузер после всех манипуляций
#     browser.quit()
link = "http://suninjuly.github.io/registration1.html"
try:

    browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_class_name("form-control.first")
    input1.send_keys("Oleh")
    input2 = browser.find_element_by_xpath('//input[contains(@placeholder,"last name")]').send_keys("Roman")
    input3 = browser.find_element_by_xpath("//label[text()= 'Email*']/../input").send_keys("123@gmail.com")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
