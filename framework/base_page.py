# _*_ coding:utf-8 _*_
# @Time: 2020-09-23
# @Author: zhuxh

import os.path
# from selenium import webdriver
from read_ini import read_ini
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os, sys

# 动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from framework.browser_engine import BrowserEngine


# 对象库层 -基类
class BasePage:
    '''
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    '''

    def __init__(self):
        self.driver = BrowserEngine.get_driver()

    def get_page_title(self):
        '''获取网页标题'''
        return self.driver.title

    def forward(self):
        '''浏览器前进操作'''
        self.driver.forward()

    def back(self):
        '''浏览器后退操作'''
        self.driver.back()

    def refresh(self):
        '''浏览器刷新操作'''
        self.driver.refresh()

    def screenshot(self):
        '''截图'''
        rq = time.strftime('%Y%m%d%H%M%S', time.localtime())
        screen_name = os.path.join(r"d:\autotest\pythonSelenium\img", '%s.png' % rq)
        try:
            self.driver.get_screenshot_as_file(screen_name)
        except:
            self.screenshot()

    def get_element(self, selector):
        '''定位元素'''
        by = selector[0]
        value = selector[1]
        element = None
        if by in ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']:
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    print('Not find the element')
                return element
            except NoSuchElementException as e:
                print("NoSuchElementException %s" % e)
                # 调用截图
        else:
            print('please enter a valid type of targeting elements')

    def get_conf_element(self, node_name, key):
        '''如何直接键入值, 点击登录, 不用每次都输入定位方式和定位值。定位方式、定位值(找element), 输入、点击'''
        data = read_ini.get_ini(node_name, key)
        data_info = data.split('>')
        return data_info


# 操作层 -基类
class BaseHandle:

    def __init__(self):
        self.bp = BasePage()
        self.driver = BrowserEngine.get_driver()

    def isdisplayed(self, element):
        '''元素是否存在'''
        value = element.is_displayed()
        return value

    def send_value(self, element, value):
        try:
            self.clear_ele_text(element)
            element.send_keys(value)
        except BaseException:
            self.bp.screenshot()

    def send_value_enter(self, element, value):
        '''输入并确认'''
        try:
            self.clear_ele_text(element)
            element.send_keys(value)
            time.sleep(1)
            element.send_keys(Keys.ENTER)
        except:
            self.bp.screenshot()

    def click_element(self, element):
        '''点击元素'''
        try:
            element.click()
        except BaseException:
            display = self.isdisplayed(element)
            if display is True:
                time.sleep(3)
            else:
                self.bp.screenshot()

    def right_click(self, element):
        '''右击元素'''
        try:
            ActionChains(self.driver).context_click(element).perform()
        except NameError:
            self.bp.screenshot()

    def double_click(self, element):
        '''双击'''
        try:
            ActionChains(self.driver).context_click(element).perform()
        except Exception as e:
            self.bp.screenshot()
            raise

    def move_to_element(self, element):
        '''鼠标移到元素上'''
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except Exception as e:
            self.bp.screenshot()
            raise

    def drag_and_drop(self, element_drag, target_drop):
        '''拖拽'''
        try:
            ActionChains(self.driver).drag_and_drop(element_drag, target_drop).perform()
        except Exception:
            self.bp.screenshot()

    def submit(self, element):
        '''submit'''
        try:
            element.submit()
        except Exception:
            self.bp.screenshot()

    def get_attribute(self, element, attribute):
        '''获取元素属性'''
        try:
            return element.get_attribute(attribute)
        except Exception:
            self.bp.screenshot()
            raise

    def get_text(self, element):
        '''获取元素的文本信息'''
        try:
            return element.text
        except Exception:
            self.bp.screenshot()

    def dismiss_alert(self):
        '''弹窗 alert——取消'''
        self.driver.switch_to.alert.dismiss()

    def clear_ele_text(self, element):
        '''清除文本框'''
        try:
            element.clear()
        except NameError as e:
            print("Failed to clear in input box with %s" % e)
            self.bp.screenshot()

    def use_js(self, js):
        '''调用js'''
        try:
            self.driver.execute_script(js)
            print('successful，js contents is：%s' % js)
        except BaseException:
            print('js error', exc_info=1)

    def switch_menue(self, parentelement, secelement, targetelement):
        '''三级菜单切换'''
        time.sleep(3)
        try:
            self.driver.switch_to_default_content()
            self.click_element(parentelement)
            print('成功点击一级菜单：%s' % parentelement)
            self.click_element(secelement)
            print('成功点击二级菜单：%s' % secelement)
            self.click_element(targetelement)
            print('成功点击三级菜单：%s' % targetelement)
        except BaseException:
            print('切换菜单报错', exc_info=1)

    def switch_ifarme(self, element):
        """切换ifarme"""
        try:
            self.driver.switch_to.frame(element)
            print('Successful to switch_to_frame! ')
        except BaseException:
            print('Failed to  switch_to_frame', exc_info=1)

    def quit_iframe(self):
        """退出当前iframe"""
        self.driver.switch_to_default_content()

    # 获取url
    def get_url(self, url):
        if self.driver != None:
            if 'http://' in url:
                self.driver.get(url)
            else:
                print('你的url有问题')
        else:
            print('case有问题')

    # 浏览器常见操作
    # 最大化(maximize_window())、最小化(minimize_window())、设置大小(set_window_size(x,y))
    # 刷新(refresh())、前进(forward())、后退(back())
    def handle_browser(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == 'max':
                self.driver.maximize_window()
            else:
                self.driver.minimize_window()
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            print('你传递的参数有问题')

    # 判断页面打开是否正确
    # title_name=None，不传默认为None,参数可能为空的时候，必须放在后面，不能放在前面
    def assert_title(self, title_name=None):
        # 获取title
        if title_name != None:
            get_title = EC.title_contains(title_name)
            return get_title(self.driver)

    def open_url_is_true(self, url, title_name=None):
        self.get_url(url)
        return self.assert_title(title_name)

    # 通过title进行多窗口切换方法封装
    def switch_windows(self, title_name=None):
        # 获取所有句柄
        all_h = self.driver.window_handles
        # 获取当前句柄
        curr_h = self.driver.current_window_handle
        for i in all_h:
            if i != curr_h:
                time.sleep(2)
                self.driver.switch_to.window(i)
                # 判断窗口title是否是你想要的窗口
                if self.assert_title(title_name):
                    return True
                    break


"""
if __name__ == "__main__":
    a = BasePage()
    a.get_url("http://zhuhai.ganji.com/")
    a.get_element(a.get_conf_element("ganjiHomePage","home_register_link")).click()
"""
