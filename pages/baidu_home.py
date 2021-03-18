from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from framework.base_page import BasePage, BaseHandle
from framework.browser_engine import BrowserEngine

# 对象库层(获取元素)
class BaiduHomePage(BasePage):

    def __init__(self):
        # 调用基类的构造方法
        BasePage.__init__()

        # 定位元素""
        self.top_left_news = self.get_conf_element("baiduHomePage","top_left_news")
        self.top_left_hao123 = self.get_conf_element("baiduHomePage","top_left_hao123")
        self.top_left_map = self.get_conf_element("baiduHomePage","top_left_map")
        self.top_left_live = self.get_conf_element("baiduHomePage","top_left_live")
        self.top_left_haokan = self.get_conf_element("baiduHomePage","top_left_haokan")
        self.top_left_tieba = self.get_conf_element("baiduHomePage","top_left_tieba")
        self.top_left_xueshu= self.get_conf_element("baiduHomePage", "top_left_xueshu")
        self.home_setting_dropdown = self.get_conf_element("baiduHomePage", "home_setting_dropdown")

    # 获取元素对象
    def get_top_left_news(self):
        return self.get_element(self.top_left_news)

    def get_top_left_hao123(self):
        return self.get_element(self.top_left_hao123)

    def get_top_left_map(self):
        return self.get_element(self.top_left_map)

    def get_top_left_live(self):
        return self.get_element(self.top_left_live)

    def get_top_left_haokan(self):
        return self.get_element(self.top_left_haokan)

    def get_top_left_tieba(self):
        return self.get_element(self.top_left_tieba)

    def get_top_left_xueshu(self):
        return self.get_element(self.top_left_xueshu)

    def get_setting_dropdown(self):
        return self.get_element(self.home_setting_dropdown)

# 操作层(操作元素)
class BaiduHomeHandle(BaseHandle):

    def __init__(self):
        # 调用基类的构造方法
        BaseHandle.__init__()

        # 调用对象库层类
        self.hp = BaiduHomePage()

    def click_top_left_news(self):
        self.click_element(self.hp.get_top_left_news())

    def click_top_left_hao123(self):
        self.click_element(self.hp.get_top_left_hao123())

    def click_top_left_map(self):
        self.click_element(self.hp.get_top_left_map())

    def click_top_left_live(self):
        self.click_element(self.hp.get_top_left_live())

    def click_top_left_haokan(self):
        self.click_element(self.hp.get_top_left_haokan())

    def click_top_left_tieba(self):
        self.click_element(self.hp.get_top_left_tieba())

    def click_top_left_xueshu(self):
        self.click_element(self.hp.get_top_left_xueshu())

    # 鼠标悬浮操作
    def hover_setting_dropdown(self):
        self.move_to_element(self.hp.home_setting_dropdown)
        # s = Select(self.hp.home_setting_dropdown)


