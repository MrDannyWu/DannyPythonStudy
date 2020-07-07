from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path="D:\Program\chromedriver\chromedriver.exe")
browser.get('https://www.baidu.com')
search = browser.find_element_by_id('kw')
search.send_keys('python')
search.send_keys(Keys.ENTER)
#submit = browser.find_element_by_id('su')
#submit.click()


