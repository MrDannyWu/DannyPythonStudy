import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

browser = webdriver.PhantomJS()
#browser = webdriver.Chrome()
browser.get('http://10.23.202.37/webAuth/index.htm')
username = browser.find_element_by_id('username')
username.send_keys("yushumei")
password = browser.find_element_by_id('password')
password.send_keys("office3!")
rember = browser.find_element_by_id('rememberPwd')
rember.click()
submit = browser.find_element_by_class_name('button')
submit.click()

print("successful!")

os.system('start firefox')
