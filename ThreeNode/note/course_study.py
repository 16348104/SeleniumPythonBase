#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.imooc.com/user/newlogin/from_url/')
driver.find_element_by_name('email').send_keys('609037724@qq.com')
driver.find_element_by_name('password').send_keys('ansqz3701')
driver.find_element_by_class_name('moco-btn').click()
time.sleep(5)
driver.get('https://www.imooc.com/user/setbindsns')
driver.find_elements_by_class_name("inner-i-box")[1].find_element_by_class_name('moco-btn-normal').click()
hadnle = driver.window_handles
driver.switch_to.window(hadnle[1])
driver.find_element_by_id('userId').send_keys('te')
time.sleep(2)
driver.close()