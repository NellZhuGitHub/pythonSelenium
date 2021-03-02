import sys
import time
import os.path
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
# from __init__ import *    #解决命令行python搜索包向下搜索的问题
# 动态添加D:\Python-web-selenium路径作为模块加载路径
# sys.path.append('D:\\Python-web-selenium\\poModel')  #解决命令行python搜索包向下搜索的问题
# 动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
# 加载D:\Python-web-selenium路径下的readIni模块
from read_ini import read_ini
from framework.logger import Logger

#logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine(object):

    __driver = None

    dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    print(dir)
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    @classmethod
    def get_driver(self):
        if self.__driver is None:
            browser = read_ini.get_ini('browserType', 'browser_name_chrome')
            if browser == "Firefox":
                self.__driver = webdriver.Firefox()
            elif browser == "Chrome":
                self.__driver = webdriver.Chrome(self.chrome_driver_path)
            elif browser == "IE":
                self.__driver = webdriver.Ie()
            else:
                self.__driver = webdriver.Edge()
            time.sleep(5)
            self.__driver.maximize_window()

            # imlicitlyWait(隐式等待), 在指定的时间范围内, 不断查找元素, 直到查到元素或者超时, 特点是必须等待整个页面加载完成
            self.__driver.implicitly_wait(10)
        return self.__driver

    @classmethod
    def quit_driver(self):
        if self.__driver:
            self.__driver.quite()
            self.__driver = None
"""
if __name__ == "__main__":
    c = BrowserEngine
    d = c.get_driver()
    print(d)
"""
