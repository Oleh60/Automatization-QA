from seleniumbase import BaseCase
from selenium import webdriver

# driver = webdriver.Chrome("C:\\CD\\chromedriver.exe")
#
# driver.get('https://www.youtube.com/')
# seearchbox = driver.find_element_by_xpath('//*[@id="search"]')
# seearchbox.send_keys('natalia qa')
#
# seearchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
#
# seearchButton.click()
#
# driver.quit()


browser = webdriver.Chrome("C:\\CD\\chromedriver.exe")

browser.get('https://www.microsoft.com/uk-ua')
# forBisness = browser.find_element_by_xpath('//*[@id="coreui-contentplacement-r9h8jv2"]/div[2]/div/div[1]/div[1]/'
#                                            'section/picture/img').click()
#
# Xbox = browser.find_element_by_id('shellmenu_3').click()

facebook = browser.find_element_by_xpath('//*[@id="coreui-socialfollow-rm1cuuw"]/section/ul/li[1]/a').click()

# browser.quit()

