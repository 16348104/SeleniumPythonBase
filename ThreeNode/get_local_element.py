#coding=utf-8
import sys
import time
sys.path.append('E:\\Teacher\\Imooc\\SeleniumPythonBase')
from ThreeNode.read_init import ReadIni
from ThreeNode.open_browser import SeleniumDriver
read_ini = ReadIni()
selenium_driver = SeleniumDriver('chrome')
data = read_ini.get_value('username')
data_info = data.split('>')
print(data_info)
by = data_info[0]
local =data_info[1]
print(by,"-->",local)
selenium_driver.get_url('http://www.imooc.com/user/newlogin/from_url/')
selenium_driver.send_value(by,local,"Mushishi_xu_test")
time.sleep(3)
selenium_driver.close_driver()