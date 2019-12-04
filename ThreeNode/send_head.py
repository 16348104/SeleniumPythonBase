#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
from pykeyboard import PyKeyboard
import time
driver = webdriver.Chrome()
pykey = PyKeyboard()
driver.get('http://www.imooc.com')

element = driver.find_element_by_id("js-signin-btn")
element.click()
time.sleep(3)
driver.find_element_by_name("email").send_keys('mushishi_xu@163.com')
element = driver.find_element_by_name('password')
element.send_keys('xu221168')
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(2)
driver.get("https://www.imooc.com/user/setprofile")
time.sleep(5)
element = driver.find_element_by_xpath("//a[@class='avator-btn-fake']/following-sibling::input[1]")
#driver.find_element_by_id("upload").send_keys("C:\\Users\\KYB\\Desktop\\12.png")
time.sleep(5)
element.send_keys('C:\\Users\\KYB\\Desktop\\12.png')
'''
time.sleep(10)
pykey.tap_key(pykey.shift_key)
pykey.type_string('C:\\Users\\KYB\\Desktop\\12.png')
time.sleep(2)
pykey.tap_key(pykey.enter_key)
'''
time.sleep(2)
driver.close()


