from selenium import webdriver
import time, sys, os

# 动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from framework.base_page import BasePage, BaseHandle
from framework.read_ini import read_ini
from framework.browser_engine import BrowserEngine


class GanjiRegisterPage(BasePage):

    def __init__(self):
        BasePage.__init__(self)
        # 元素定位
        self.register_input_username = self.get_conf_element('ganjiRegister', "register_input_username")
        self.register_input_phone = self.get_conf_element('ganjiRegister', "register_input_phone")
        self.register_input_checkcode = self.get_conf_element('ganjiRegister', "register_input_checkcode")
        self.register_input_phonecode = self.get_conf_element('ganjiRegister', "register_input_phonecode")
        self.register_input_phonepwd = self.get_conf_element('ganjiRegister', "register_input_phonepwd")
        self.register_input_phonepwd2 = self.get_conf_element('ganjiRegister', "register_input_phonepwd2")
        self.register_btn_sendcodebtn = self.get_conf_element('ganjiRegister', "register_btn_sendcodebtn")
        self.register_btn_submit = self.get_conf_element('ganjiRegister', "register_btn_submit")
        self.error_text_username = self.get_conf_element('ganjiRegister', "error_text_username")
        self.error_text_phone = self.get_conf_element('ganjiRegister', "error_text_phone")
        self.error_text_checkcode = self.get_conf_element('ganjiRegister', "error_text_checkcode")
        self.error_text_phonecode = self.get_conf_element('ganjiRegister', "error_text_phonecode")
        self.error_text_phonepwd = self.get_conf_element('ganjiRegister', "error_text_phonepwd")
        self.error_text_phonepwd2 = self.get_conf_element('ganjiRegister', "error_text_phonepwd2")

        # 获取元素对象

    def get_input_username(self):
        ele = self.get_element(self.register_input_username)
        return ele

    def get_input_phone(self):
        ele = self.get_element(self.register_input_phone)
        return ele

    def get_input_checkcode(self):
        ele = self.get_element(self.register_input_checkcode)
        return ele

    def get_input_phonecode(self):
        ele = self.get_element(self.register_input_phonecode)
        return ele

    def get_input_phonepwd(self):
        ele = self.get_element(self.register_input_phonepwd)
        return ele

    def get_input_phonepwd2(self):
        ele = self.get_element(self.register_input_phonepwd2)
        return ele

    def get_btn_sendcodebtn(self):
        ele = self.get_element(self.register_btn_sendcodebtn)
        return ele

    def get_btn_submit(self):
        ele = self.get_element(self.register_btn_submit)
        return ele

    def get_error_text_username(self):
        return self.get_element(self.error_text_username)

    def get_error_text_phone(self):
        return self.get_element(self.error_text_phone)

    def get_error_text_checkcode(self):
        return self.get_element(self.error_text_checkcode)

    def get_error_text_phonecode(self):
        return self.get_element(self.error_text_phonecode)

    def get_error_text_phonepwd(self):
        return self.get_element(self.error_text_phonepwd)

    def get_error_text_phonepwd2(self):
        return self.get_element(self.error_text_phonepwd2)


# 操作层(操作元素)
class GanjiRegisterHandle(BaseHandle):

    def __init__(self):
        BaseHandle.__init__(self)
        self.rp = GanjiRegisterPage()

    def send_input_username(self, username):
        self.send_value_enter(self.rp.get_input_username(), username)

    def send_input_phone(self, phone):
        self.send_value_enter(self.rp.get_input_phone(), phone)

    def send_input_checkcode(self, checkcode):
        self.send_value_enter(self.rp.get_input_checkcode(), checkcode)

    def send_input_phonecode(self, phonecode):
        self.send_value_enter(self.rp.get_input_phonecode(), phonecode)

    def send_input_phonepwd(self, phonepwd):
        self.send_value_enter(self.rp.get_input_phonepwd(), phonepwd)

    def send_input_phonepwd2(self, phonepwd2):
        self.send_value_enter(self.rp.get_input_phonepwd2(), phonepwd2)

    def click_get_phone_code(self):
        self.click_element(self.rp.get_btn_sendcodebtn())

    def click_register_submit(self):
        self.click_element(self.rp.get_btn_submit())

    # 获取文字信息
    def get_register_error_text(self, error_key):
        try:
            if error_key == "username_error_msg":
                text = self.get_text(self.rp.get_error_text_username())
            elif error_key == "phone_error_msg":
                text = self.get_text(self.rp.get_error_text_phone())
            elif error_key == "checkcode_error_msg":
                text = self.get_text(self.rp.get_error_text_checkcode())
            elif error_key == "phonecode_error_msg":
                text = self.get_text(self.rp.get_error_text_phonecode())
            elif error_key == "phonepwd_error_msg":
                text = self.get_text(self.rp.get_error_text_phonepwd())
            else:
                text = self.get_text(self.rp.get_error_text_phonepwd2())
        except:
            text = None
        return text


# 业务层()
class GanjiRegisterProxy:

    def __init__(self):
        self.rh = GanjiRegisterHandle()

        # 注册页面表单form填写并提交

    def user_register(self, username, phone, phonepwd, phonepwd2):
        self.rh.send_input_username(username)
        self.rh.send_input_phone(phone)
        # time.sleep(80)
        self.rh.send_input_phonepwd(phonepwd)
        self.rh.send_input_phonepwd2(phonepwd2)
        self.rh.click_register_submit()

        # 获取错误信息是否与预期一致

    def text_in_element(self, error_key, text_result):
        if self.rh.get_register_error_text(error_key) == text_result:
            return True
        else:
            return False


"""
if __name__ == "__main__":
    driver = BrowserEngine.get_driver()
    driver.get("https://passport.ganji.com/register.php?next=/")
    a = GanjiRegisterHandle()
    a.send_input_username("zhuxh")
    a.send_input_phone("123455")
    b = GanjiRegisterPage()
    #res = b.get_error_text_username().text
    res = a.get_register_error_text("username_error_msg")
    print(res)
    driver.quit()
"""
