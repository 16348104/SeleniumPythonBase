#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('http://coding.imooc.com')
driver.save_screenshot('test.png')
driver
time.sleep(2)
driver.close()