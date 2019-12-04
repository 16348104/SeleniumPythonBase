#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
driver = webdriver.Chrome()
driver.get('https://www.imooc.com')
time.sleep(3)
element = driver.find_element_by_id("js-signin-btn")
element.click()
time.sleep(3)

driver.find_element_by_name("email").send_keys('mushishi_xu@163.com')
element = driver.find_element_by_name('password')
element.send_keys('xu221168')
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(2)
driver.get('https://www.imooc.com/wenda/save')
driver.switch_to.frame('ueditor_0')
time.sleep(2)
#element = driver.find_element_by_id('ueditor_0')
p_element = driver.find_element_by_tag_name('p')
ActionChains(driver).move_to_element(p_element).click().send_keys('This is test').perform()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(2)
driver.find_elements_by_class_name('save-list-tag')[1].click()
time.sleep(3)
driver.close()