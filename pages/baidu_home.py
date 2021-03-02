from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from framework.base_page import BasePage, BaseHandle
from framework.browser_engine import BrowserEngine

# 对象库层(获取元素)
class BaiduHomePage(BasePage):

    def __init__(self):
        # 调用基类的构造方法
        BasePage.__init__()

        # 定位元素
        self.home_setting_dropdown = self.get_conf_element("baiduHomePage", "home_setting_dropdown")

    # 获取元素对象
    def get_setting_dropdown(self):
        return self.get_element(self.home_setting_dropdown)

# 操作层(操作元素)
class BaiduHomeHandle(BaseHandle):

    def __init__(self):
        # 调用基类的构造方法
        BaseHandle.__init__()

        # 调用对象库层类
        self.hp = BaiduHomePage()

    # 鼠标悬浮操作
    def hover_setting_dropdown(self):
        self.move_to_element(self.hp.home_setting_dropdown)
        s = Select(self.hp.home_setting_dropdown)

    def
