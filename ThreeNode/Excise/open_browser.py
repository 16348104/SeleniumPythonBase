# coding=utf-8
from selenium import webdriver
import time
# 打开浏览器


def open(browse):
    try:
        if browse == 'chrome':
            driver = webdriver.Chrome()
        elif browse == "firefox":
            driver = webdriver.Firefox()
        elif browse == "ie":
            driver = webdriver.Ie()
        else:
            driver = webdriver.Edge()
        return driver
    except:
        print('浏览器打开失败!')
        return None


# 获得URL
def get_url(url):
    driver = open('chrome')
    if driver != None:
        if 'https://' in url:
            driver.get(url)
            time.sleep(10)
        else:
            print('url有错误')
    else:
        print('case失败')

        # driver.quit()
get_url('https://www.imooc.com/')
