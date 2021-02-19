import os, sys, time
from selenium import webdriver
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from framework.base_page import BasePage, BaseHandle

class GanjiLoginPage(BasePage):

    def __init__(self):
        # 调用基类的构造方法
        BasePage.__init__(self)
        # 定位元素
        self.login_input_username = self.get_conf_element("ganjiLogin", "login_input_username")
        self.login_input_password = self.get_conf_element("ganjiLogin", "login_input_password")
        self.login_btn_submit = self.get_conf_element("ganjiLogin", "login_btn_submit")
        self.login_error_msg = self.get_conf_element("ganjiLogin", "login_error_msg")

    # 获取元素对象
    def get_input_username(self):
        return self.get_element(self.login_input_username)

    def get_input_password(self):
        return self.get_element(self.login_input_password)

    def get_btn_submit(self):
        return self.get_element(self.login_btn_submit)

    def get_error_msg(self):
        return self.get_element(self.login_error_msg)

# 操作层(操作元素)
class GanjiLoginHandle(BaseHandle):

    def __init__(self):
        BaseHandle.__init__(self)
        self.lp = GanjiLoginPage()

    def send_input_username(self, username):
        self.send_value(self.lp.get_input_username(), username)

    def send_input_password(self, password):
        self.send_value(self.lp.get_input_password(), password)

    def click_login_submit(self):
        print(self.lp.get_btn_submit())
        self.click_element(self.lp.get_btn_submit())

    def error_msg_display(self):
        try:
            text = self.get_text(self.lp.get_error_msg())
        except:
            text = None
        return text

    def submit_btn_isdisplayed(self):
        return self.isdisplayed(self.lp.get_btn_submit())

# 业务层
class GanjiLoginProxy:

    def __init__(self):
        self.lh = GanjiLoginHandle()

    # 注册页面表单form填写并提交
    def user_login(self, username, password):
        self.lh.send_input_username(username)
        time.sleep(2)
        self.lh.send_input_password(password)
        time.sleep(2)
        self.lh.click_login_submit()

    def user_logout(self):
        pass

    # 获取错误信息是否与预期一致
    def text_in_element(self, text_result):
        if self.lh.error_msg_display() == text_result:
            return True
        else:
            return False

    # 验证页面元素是否还在
    def display_is_element(self):
        return self.lh.submit_btn_isdisplayed()