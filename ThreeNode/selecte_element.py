#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.get('https://www.imooc.com')
element = driver.find_element_by_id("js-signin-btn")
time.sleep(3)
driver.find_element_by_name("email").send_keys('mushishi_xu@163.com')
element = driver.find_element_by_name('password')
element.send_keys('xu221168')
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(2)
driver.get("https://www.imooc.com/user/setprofile")
time.sleep(5)
#driver.find_elements_by_class_name("moco-form-control")[7].find_elements_by_tag_name('option')[4].click()

select_element = driver.find_elements_by_class_name("moco-form-control")[7]
select_element.send_keys("test.jpg")

#Select(select_element).select_by_index(5)
Select(select_element).select_by_value('13')


Select(select_element).select_by_visible_text('Python工程师')
time.sleep(3)

driver.close()