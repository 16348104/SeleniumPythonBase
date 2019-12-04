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
    # driver.maximize_window()
    if driver != None:
        if 'https://' in url:
            driver.get(url)
            time.sleep(5)
        else:
            print('url有错误')
    else:
        print('case失败')

        # driver.quit()


def handle_windows(*args):
    driver = open('chrome')
    # get_url('https://www.imooc.com/')
    val = len(args)
    if val == 1:
        if args[0] == 'max':
            driver.maximize_window()
        else:
            driver.minimize_window()
    elif val == 2:
        driver.set_window_size(args[0], args[1])
    else:
        print('浏览器传参错误')
handle_windows('max')
