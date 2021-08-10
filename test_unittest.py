from selenium import webdriver
import unittest
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
# browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")



class Unnittest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")
        self.browser.maximize_window()
        self.browser.implicitly_wait(4)

    def tearDown(self):
        self.browser.quit()

    def test_1(self):
        self.browser.get(link1)

        input1 = self.browser.find_element_by_class_name("form-control.first")
        input1.send_keys("Oleh")
        self.browser.find_element_by_xpath('//input[contains(@placeholder,"last name")]').send_keys("Roman")
        self.browser.find_element_by_xpath("//label[text()= 'Email*']/../input").send_keys("123@gmail.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()



        welcome_text_elt = self.browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text



        self.assertEqual("Congratulations! You have successfully registered!",welcome_text,"not correct text")


    def test_2(self):
        self.browser.get(link2)

        input1 = self.browser.find_element_by_class_name("form-control.first")
        input1.send_keys("Oleh")
        self.browser.find_element_by_xpath('//input[contains(@placeholder,"last name")]').send_keys("Roman")
        self.browser.find_element_by_xpath("//label[text()= 'Email*']/../input").send_keys("123@gmail.com")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = self.browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "not correct text")


if __name__ == "__main__":
    unittest.main()

