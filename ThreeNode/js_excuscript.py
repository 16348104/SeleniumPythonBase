#coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get('https://www.imooc.com/article')

js = 'document.documentElement.scrollTop=100000;'
driver.execute_script(js)
t=True
while t:
    element_list = driver.find_elements_by_class_name('article-lwrap')
    for element in element_list:
        course_name = element.find_element_by_tag_name('p').text
        print(course_name)
        if course_name == 'Spring Boot实战系列(1)项目构建':
            element.click()
            t = False
    driver.execute_script(js)

driver.close()