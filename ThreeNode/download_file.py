#coding=utf-8
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
prefs = {'download.default_directory':'D:\Download\\','profile.default_content_settings.popups':0}
options.add_experimental_option('prefs',prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get('https://www.imooc.com/mobile/app')
driver.find_elements_by_class_name("mobile-btn-download")[1].click()
time.sleep(5)
driver.close()