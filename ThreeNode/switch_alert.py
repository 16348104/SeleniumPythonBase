#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('file:///C:/Users/KYB/Desktop/test.html')
time.sleep(2)
'''
driver.find_element_by_id('alert').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.find_element_by_id('sure').click()
time.sleep(2)
driver.switch_to.alert.accept()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.find_element_by_id('sure').click()
time.sleep(2)
driver.switch_to.alert.dismiss()
time.sleep(2)
driver.refresh()
'''
time.sleep(1)
driver.find_element_by_id('three').click()
time.sleep(1)
alert_element = driver.switch_to.alert
print(alert_element.text)
alert_element.send_keys('test')
alert_element.accept()
time.sleep(2)
driver.close()