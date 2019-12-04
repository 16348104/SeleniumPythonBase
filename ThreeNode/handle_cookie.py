#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://order.imooc.com/myorder')
time.sleep(2)
driver.delete_all_cookies()
'''
driver.get('http://www.imooc.com')
element = driver.find_element_by_id("js-signin-btn")
element.click()
time.sleep(3)
driver.find_element_by_name("email").send_keys('mushishi_xu@163.com')
element = driver.find_element_by_name('password')
element.send_keys('xu221168')
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(2)
cookie_list = driver.get_cookies()
'''

time.sleep(2)
print(cookie)
driver.add_cookie(cookie)
time.sleep(2)
driver.get('http://order.imooc.com/myorder')
time.sleep(2)
driver.close()
