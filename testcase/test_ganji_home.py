import time
import unittest
import os, sys

# 动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from framework.browser_engine import BrowserEngine
from framework.read_ini import read_ini
from pages.ganji_home import GanjiHomeProxy


class TestGanjiHome(unittest.TestCase):
    url = read_ini.get_ini('serverUrl', "url_home")
    registerTitle = read_ini.get_ini('windowTitle', "title_register")
    homeTitle = read_ini.get_ini('windowTitle', "title_home")
    loginTitle = read_ini.get_ini('windowTitle', "title_login")

    def setUp(self):
        self.driver = BrowserEngine.get_driver()
        self.homeProxy = GanjiHomeProxy()
        self.driver.get(self.url)

    def tearDown(self):
        self.driver.quit()

    def test_open_home(self):
        res = self.homeProxy.title_name_page(self.homeTitle)
        self.assertEqual(res, True)

    def test_register_link(self):
        self.homeProxy.to_register_page()
        time.sleep(5)
        res = self.homeProxy.title_name_page(self.registerTitle)
        self.assertEqual(res, True)

    # 此处可以使用
    def test_link(self):
        self.homeProxy.to_link_page("home_login_link")
        time.sleep(5)
        res = self.homeProxy.title_name_page(self.loginTitle)
        self.assertEqual(res, True)


"""
if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    test = ["test_open_home", "test_register_link", "test_link"]
    tests = map(TestGanjiHome, test)
    print(tests)
    suite.addTests(tests)
    runner1 = unittest.TextTestRunner(verbosity=2)
    runner1.run(suite) 
"""