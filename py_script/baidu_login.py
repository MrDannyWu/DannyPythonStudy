from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = 'https://passport.baidu.com/v2/?login'

browser = webdriver.Chrome()
browser.get(url)
login_url = browser.find_element_by_id('TANGRAM__PSP_3__footerULoginBtn')
login_url.click()
time.sleep(2)
username = browser.find_element_by_id('TANGRAM__PSP_3__userName')
username.send_keys('18856052344')
password = browser.find_element_by_id('TANGRAM__PSP_3__password')
password.send_keys('############')
submit = browser.find_element_by_id('TANGRAM__PSP_3__submit')
submit.click()
close = browser.find_element_by_id('TANGRAM__22__header_a')
close.click()
submit.click()



