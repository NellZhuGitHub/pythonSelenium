import os, sys
from selenium import webdriver

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from framework.base_page import BasePage, BaseHandle
from selenium.webdriver.support import expected_conditions as EC


# 对象库层(获取元素)
class GanjiHomePage(BasePage):

    def __init__(self):
        # 调用基类的构造方法
        BasePage.__init__(self)
        # 定位元素
        self.home_register_link = self.get_conf_element("ganjiHomePage", "home_register_link")

    # 定位元素
    def home_link(self, homelinkkey):
        return self.get_conf_element("ganjiHomePage", homelinkkey)

    # 获取元素对象
    def get_home_register_link(self):
        return self.get_element(self.home_register_link)

    # 获取元素对象--公用link
    def get_home_link(self, homelinkkey):
        return self.get_element(self.home_link(homelinkkey))


# 操作层(操作元素)
class GanjiHomeHandle(BaseHandle):

    def __init__(self):
        BaseHandle.__init__(self)
        self.hp = GanjiHomePage()

    def click_home_register_link(self):
        self.click_element(self.hp.get_home_register_link())

    def click_home_link(self, homelinkkey):
        print(homelinkkey)
        self.click_element(self.hp.get_home_link(homelinkkey))

    def is_right_open_page(self, title):
        return self.assert_title(title)


# 业务层()
class GanjiHomeProxy:

    def __init__(self):
        self.hh = GanjiHomeHandle()

    # 跳转到注册页面
    def to_register_page(self):
        self.hh.click_home_register_link()

    # 跳转到链接相应页面
    def to_link_page(self, homelinkkey):
        print(homelinkkey)
        self.hh.click_home_link(homelinkkey)

    def title_name_page(self, title):
        return self.hh.is_right_open_page(title)
