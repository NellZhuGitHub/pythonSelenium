import time
import ddt
import os, sys
import unittest
#动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from framework.base_page import BasePage
from framework.read_ini import read_ini
from framework.data_excel import DataExcel
from framework.browser_engine import BrowserEngine
from pages.ganji_login import GanjiLoginProxy
from pages.ganji_home import GanjiHomeProxy

'''
赶集网的登录测试，分下面几种情况
(1) 用户名、密码正确        进入首页
(2) 用户名正确、密码错误    您输入的登录名或密码错误
(3) 用户名正确、密码为空    您输入的密码不能为空，请输入
(4) 用户名错误、密码正确    您输入的登录名或密码错误
(5) 用户名为空、密码正确    您输入的用户名不能为空，请输入
(6) 用户名为空、密码为空    您输入的用户名不能为空，请输入
(5)和(6)相同, 所以无需验证(6)
'''

data = DataExcel("自动化用例",r"D:\autotest\pythonSelenium\exceldata\登录用例.xlsx")
loginData = data.dict_data()
print(loginData)

@ddt.ddt
class TestGanjiLogin(unittest.TestCase):

    url = read_ini.get_ini('serverUrl', "url_home")

    @classmethod
    def setUpClass(self):
        self.driver = BrowserEngine.get_driver()
        self.lp = GanjiLoginProxy()
        self.hp = GanjiHomeProxy()

    def setUp(self):
        self.driver.get(self.url)   # 打开首页
        self.hp.to_link_page("home_login_link")   # 点击注册链接

    def tearDown(self):
        # 清空cookies
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 用户登录
    def user_case_login(self, username, password, text_result):
        self.lp.user_login(username, password)
        if text_result == '':
            print("zhuxh")
            res = self.lp.display_is_element()
            print(res)
            self.assertEqual(res, True)
        else:
            res = self.lp.text_in_element(text_result)
            self.assertEqual(res, True)

    @ddt.data(*loginData)
    def test_user_login(self, data):
        self.user_case_login(data['username'], data['password'], data['errormsg'])

"""
if __name__ == "__main__":
    unittest.main()
"""