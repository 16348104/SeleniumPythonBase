#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://www.5itest.cn/login')
driver.find_element_by_id("login_username").send_keys("609037724@qq.com")
driver.find_element_by_id("login_password").send_keys("test1234")
driver.find_element_by_class_name("js-btn-login").click()
time.sleep(5)
driver.get('http://www.5itest.cn/admin/roles')
time.sleep(5)
driver.find_element_by_class_name("btn-success").click()
#driver.switch_to_active_element()
time.sleep(3)
driver.find_element_by_id("tree_1_switch").click()
time.sleep(2)
driver.find_element_by_id("tree_90_check").click()
time.sleep(3)
driver.close()
