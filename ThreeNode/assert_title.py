#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()
driver.get("http://www.imooc.com")
title_name = driver.title
if '慕课网' in title_name:
    print("打开正确")
else:
    print("打开错误")

titl_a = EC.title_is("慕课网")
print(titl_a(driver))
title_b = EC.title_contains("慕课网")
print(title_b(driver))
driver.close()