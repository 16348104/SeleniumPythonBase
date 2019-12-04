#coding=utf-8
from selenium import webdriver
import time
driver= webdriver.Chrome()
driver.get('D:/Download/jiaoben6041/jiaoben6041/index.html')
time.sleep(5)
js = 'document.getElementById("laydateInput").removeAttribute("readonly");'
driver.execute_script(js)
element = driver.find_element_by_id("laydateInput")
element.clear()
element.send_keys('2018-10-29')
time.sleep(5)
driver.close()