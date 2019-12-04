#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get('https://www.imooc.com')
#print(driver.find_element_by_id("auto-signin").is_displayed())

LOCATOR = (By.ID,'username')

EC.visibility_of_element_located(LOCATOR)
EC.visibility_of_all_elements_located(LOCATOR)


element = driver.find_element_by_id("js-signin-btn")
print(dir(element))

element.click()


time.sleep(3)
driver.find_element_by_name("email").send_keys('mushishi_xu@163.com')
element = driver.find_element_by_name('password')
element.send_keys('xu221168')
print(dir(element))
driver.find_element_by_class_name("moco-btn-lg").click()
time.sleep(2)
#//*[@id="nav"]/div[3]/div[2]/input[1]
#标签（input）    id（#）     class（.）
#element = driver.find_element_by_xpath("//div[@class='showhide-search']/preceding-sibling::div[1]/input[1]")
#element.send_keys("appium 自动化测试")
driver.get("https://www.imooc.com/user/setprofile")
time.sleep(5)
#driver.find_elements_by_xpath("//input[@id='nick']")[1].send_keys("teset")
time.sleep(2)
#node_element = driver.find_element_by_id("profile")
element_user = driver.find_element_by_name("nickname").is_displayed()
print("-------->")
print(element_user)
'''
print(node_element.is_selected())

driver.find_elements_by_id("nick")[1].send_keys("Mushishi_test")
'''
time.sleep(3)

driver.close()


