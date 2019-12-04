#coding = utf-8
import sys
import time

sys.path.append('E:\\Teacher\\Imooc\\SeleniumPythonBase')
from selenium import webdriver
from pykeyboard import PyKeyboard
from ThreeNode.read_init import read_ini
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from ThreeNode.handle_json import handle_json


class SeleniumDriver:
    def __init__(self,browser):
        self.driver = self.open_browser(browser)

    def open_browser(self,browser):
        if browser == 'chrome':
            options = webdriver.ChromeOptions()
            prefs = {'download.default_directory':'D:\Download\\','profile.default_content_settings.popups':0}
            options.add_experimental_option('prefs',prefs)
            driver = webdriver.Chrome(chrome_options=options)

        elif browser == 'firefox':
            profile = webdriver.FirefoxProfile()
            profile.set_preference('browser.download.dir','D:\Download\\')
            profile.set_preference('browser.download.folderList',2)
            profile.set_preference('browser.helperApps.neverAsk.saveToDisk','application/zip')
            driver = webdriver.Firefox(firefox_profile=profile)
        elif browser == 'ie':
            driver = webdriver.Ie()
        else:
            driver = webdriver.Edge()
        return driver

    def get_url(self,url):
        if self.driver !=None:
            time.sleep(1)
            self.driver.maximize_window() 
            if 'http' in url:
                self.driver.get(url)
            elif 'D' in url:
                self.driver.get(url)
            else:
                print("你的URL有问题")
        else:
            print("case失败")
        #self.driver.quit()

    def handle_windows(self,*args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            elif args[0] == 'min':
                self.driver.minimize_window()
            elif args[0] == 'back':
                self.driver.back()
            elif args[0] == 'go':
                self.driver.forward()
            else:
                self.driver.refresh()
        elif value ==2:
            self.driver.set_window_size(args[0],args[1])
        else:
            print("你传递的参数有问题")
        time.sleep(5)
        self.driver.quit()

    def assert_title(self,title_name=None):
        '''
        判断title是否正确
        '''
        if title_name !=None:
            get_title = EC.title_contains(title_name) 
            return get_title(self.driver)

    def open_url_is_true(self,url,title_name=None):
        '''
        通过title判断页面是否正确

        '''
        self.get_url(url)
        return self.assert_title(title_name)
    
    def close_driver(self):
        self.driver.close()

    def switch_windows(self,title_name=None):
        '''
        切换windows
        '''
        handl_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in handl_list:
            if i != current_handle:
                time.sleep(1)
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break

    def element_isdisplay(self,element):
        flag = element.is_displayed()
        if flag == True:
            return element
        else:
            return False
                
    def get_element(self,info):
        '''
        获取元素element
        @parame by 定位方式
        @parame value 定位置
        @return element 返回一个元素
        '''
        by,value = self.get_local_element(info)
        element = None
        if by == 'id':
            element = self.driver.find_element_by_id(value)
        elif by == 'name':
            element = self.driver.find_element_by_name(value)
        elif by == 'css':
            element = self.driver.find_element_by_css_selector(value)
        elif by == 'class':
            element = self.driver.find_element_by_class_name(value)
        else:
            element = self.driver.find_element_by_xpath(value)
        #except:
            #print("定位方式：",by,"定位值:",value,"定位出现错误，没有定位成功")
        
        return self.element_isdisplay(element)

    def get_elements(self,info):
        '''
        获取元素elements
        @parame by 定位方式
        @parame value 定位置
        @return elements 返回一个元素
        '''
        elements = None
        element_list = []
        by,value = self.get_local_element(info)
        if by == 'id':
            elements = self.driver.find_elements_by_id(value)
        elif by == 'name':
            elements = self.driver.find_elements_by_name(value)
        elif by == 'css':
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == 'class':
            elements = self.driver.find_elements_by_class_name(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)
            
        for element in elements:
            if self.element_isdisplay(element) ==False:
                continue
            else:
                element_list.append(element)
        return element_list

    def get_level_element(self,info_level,node_info):
        '''
        层级定位
        有一个父节点
        父节点找子节点
        '''
        element = self.get_element(info_level)
        node_by,node_value = node_info
        if element == False:
            return False
        if node_by == 'id':
            node_element = element.find_element_by_id(node_value)
        elif node_by == 'name':
            node_element = element.find_element_by_name(node_value)
        elif node_by == 'css':
            node_element = element.find_element_by_css_selector(node_value)
        elif node_by == 'class':
            node_element = element.find_element_by_class_name(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)
        return self.element_isdisplay(node_element)

    def get_list_element(self,info,index):
        '''
        通过list定位我们得元素
        #2
        #1
        '''
        elements = self.get_elements(info)
        if index>len(elements):
            return None
        return elements[index]

    def assert_element(self,element):
        pass

    def send_value(self,info,key):
        '''
        输入值
        '''
        element = self.get_element(info)
        if element == False:
            print("输入失败，定位没有展现出来。")
        else:
            if element !=None:
                element.send_keys(key)
            else:
                print("输入失败，定位元素没找到。")
        
    def click_element(self,info):
        '''
        点击元素
        '''
        element = self.get_element(info)
        if element !=False:
            if element !=None:
                element.click()
            else:
                print("点击失败，定位元素没找到")
        else:
            print("点击失败，元素不可见")
        
    def check_box_isselected(self,info,check=None):
        '''
        判断元素是否选中
        如果没选中就选中，如果选中就补选中，根据参数来
        '''
        element = self.get_element(info)
        if element !=False:
            flag = element.is_selected()
            if flag == True:
                if check != 'check':
                    self.click_element(info)
            else:
                if check == 'check':
                    self.click_element(info)
        else:
            print("元素不可见，没办法选中")
        
    def get_local_element(self,info):
        data = read_ini.get_value(info)
        data_info = data.split('>')
        #[name,email]
        return data_info
        #return self.get_element(by,local)

    def get_selected(self,info,value_index,index=None):
        '''
        通过index获取我们selected，然后选择我们selected
        '''
        selected_element = None
        if index != None:
            selected_element = self.get_list_element(info,index)
        else:
            selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value_index)

    def upload_file(self,file_name):
        '''
        非input类型上传文件
        @parame filename
        '''
        pykey = PyKeyboard()
        #pykey.tap_key(pykey.shift_key)
        pykey.type_string(file_name)
        time.sleep(2)
        pykey.tap_key(pykey.enter_key)
    
    def upload_file_function(self,file_name,info,send_info=None):
        
        #先获取到你上传文件的元素的标签类型 （input、file） send_keys上传文件
        #不是，那么直接通过upload——file上传
        element = self.get_element(info)
        if element.tag_name == 'a':
            #element = driver.find_element_by_xpath("//div[@class='showhide-search']/preceding-sibling::div[1]/input[1]")
            #self.get_element(info)
            self.send_value(send_info,file_name)
        else:
            self.click_element(info)
            self.upload_file(file_name)
    
    def download_file(self,info):
        '''
        下载文件
        '''
        self.click_element(info)
    
    def js_excute_calendar(self,info):
        '''
        执行js
        '''
        local = self.get_local_element(info)
        by = local[0]
        value = local[1]
        if by == 'id':
            by_key = 'getElementById'
            js = 'document.%s("%s").removeAttribute("readonly");' %(by_key,value)
        else:
            by_key = 'getElementsByClassName'
            js = 'document.%s("%s")[1].removeAttribute("readonly");' %(by_key,value)  
        self.driver.execute_script(js)
    
    def caledar(self,info,value):
        '''
        修改日历
        '''
        element = self.get_element(info)
        try:
            element.get_attribute('readonly')
            self.js_excute_calendar(info)
        except:
            print("这个不是只读属性的日历")
        element.clear()
        self.send_value(info,value)

    def moveto_element_mouse(self,info):
        '''
        移动鼠标到某个元素上
        '''
        element = self.get_element(info)
        ActionChains(self.driver).move_to_element(element).perform()
    
    def refresh_f5(self):
        '''
        强制刷新
        '''
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()


    def switch_iframe(self,info=None):
        '''
        切换iframe
        '''
        if info != None:
            iframe_element = self.get_element(info)
            self.driver.switch_to.frame(iframe_element)
        else:
            self.driver.switch_to.default_content()
        
    def switch_alert(self,info,value=None):
        '''
        系统级弹窗
        @parame info 确认or取消
        @parame value 是否需要输入的值
        '''
        windows_alert = self.driver.switch_to.alert
        if info == 'accept':
            if value == None:
                windows_alert.accept()
            else:
                windows_alert.send_keys(value)
                windows_alert.accept()
        else:
            windows_alert.dismiss()
    
    def scroll_get_element(self,list_info,str_info):
        '''
        通过滚动条 ，滚动查找元素
        '''
        t = True
        list_element = self.get_elements(list_info)
        js = 'document.documentElement.scrollTop=100000;'
        while t:
            for element in list_element:
                title_name = element.find_element_by_tag_name('p').text
                if title_name in str_info:
                    element.click()
                    t = False
            self.driver.execute_script(js)
            time.sleep(3) 

    def scroll_element(self,info):
        js = 'document.documentElement.scrollTop=100000;'
        t = True
        while t:
            try:
                self.get_element(info)
                t = False
            except:
                self.driver.execute_script(js)
                time.sleep(3)
            
    def get_cookie(self):
        #接口
        #依赖
        
        cookie = self.driver.get_cookies()
        handle_json.write_data(cookie)

    def set_cookie(self):
        '''
        植入cookie
        '''
        cookie = handle_json.get_data()
        self.driver.delete_all_cookies()
        time.sleep(1)
        self.driver.add_cookie(cookie)
        time.sleep(2)

    def save_png(self):
        now_time = time.strftime("%Y%m%d.%H.%M.%S")
        self.driver.get_screenshot_as_file('%s.png' %now_time)

if __name__ == '__main__':


    selenium_driver = SeleniumDriver('chrome')
    #selfnium_driver.handle_windows('max')
    selenium_driver.open_url_is_true('http://www.imooc.com/article','慕课网')
    #time.sleep(30)
    #selfnium_driver.switch_windows('网站连接')
    #selfnium_driver.get_element('id','username')
    #selenium_driver.js_excute_calendar('calendar')
    #selenium_driver.send_value('calendar','2018-10-20')
    #selenium_driver.send_value('username','mushishi_xu@163.com')
    #selenium_driver.send_value('password','xu221168')
    #selenium_driver.click_element('loginbutton')
    time.sleep(5)
    selenium_driver.save_png()
    #selenium_driver.close_driver()
    #selenium_driver.scroll_element('js_element')

