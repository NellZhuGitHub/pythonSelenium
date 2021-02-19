import unittest
import time
import ddt
import os, sys

# 动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pages.ganji_home import GanjiHomeProxy
from pages.ganji_register import GanjiRegisterHandle, GanjiRegisterProxy
from framework.data_excel import DataExcel
from framework.read_ini import read_ini
from framework.base_page import BasePage
from framework.browser_engine import BrowserEngine

data = DataExcel("自动化用例", r"D:\Python-web-selenium\poModel\exceldata\注册用例.xlsx")
testCheckUsernameData = data.dict_data()[0:3]
testCheckPhoneData = data.dict_data()[3:5]
testCheckPhonepwdData = data.dict_data()[5:8]
testCheckPhonepwd2Data = data.dict_data()[8:10]


@ddt.ddt
class TestGanjiRegister(unittest.TestCase):
    url = read_ini.get_ini('serverUrl', "url_home")

    @classmethod
    def setUpClass(self):
        self.driver = BrowserEngine.get_driver()
        self.rp = GanjiRegisterProxy()
        self.rh = GanjiRegisterHandle()
        self.hp = GanjiHomeProxy()

    def setUp(self):
        self.driver.get(self.url)  # 打开首页
        self.hp.to_register_page()  # 点击注册链接

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

    # 用户名验证
    def register_case_username(self, username, text_result):
        # 输入用户名验证
        self.rh.send_input_username(username)
        res = self.rp.text_in_element("username_error_msg", text_result)
        self.assertEqual(res, True)

    # 手机号码验证
    def register_case_phone(self, username, phone, text_result):
        self.rh.send_input_username(username)
        self.rh.send_input_phone(phone)
        # time.sleep(30)
        res = self.rp.text_in_element("phone_error_msg", text_result)
        self.assertEqual(res, True)

    # 密码
    def register_case_phonepwd(self, username, phone, phonepwd, text_result):
        self.rh.send_input_username(username)
        self.rh.send_input_phone(phone)
        # time.sleep(80)
        self.rh.send_input_phonepwd(phonepwd)
        res = self.rp.text_in_element("phonepwd_error_msg", text_result)
        self.assertEqual(res, True)

    # 确认密码
    def register_case_phonepwd2(self, username, phone, phonepwd, phonepwd2, text_result):
        self.rp.user_register(username, phone, phonepwd, phonepwd2)
        res = self.rp.text_in_element("phonepwd2_error_msg", text_result)
        self.assertEqual(res, True)

    @ddt.data(*testCheckUsernameData)
    def test_register_check_username(self, data):
        self.register_case_username(data['username'], data['errormsg'])

    @ddt.data(*testCheckPhoneData)
    def test_register_check_phone(self, data):
        self.register_case_phone(data['username'], data['phone'], data['errormsg'])

    @ddt.data(*testCheckPhonepwdData)
    def test_register_check_phonepwd(self, data):
        self.register_case_phonepwd(data['username'], data['phone'], data['phonepwd'], data['errormsg'])

    @ddt.data(*testCheckPhonepwd2Data)
    def test_register_check_phonepwd2(self, data):
        self.register_case_phonepwd2(data['username'], data['phone'], data['phonepwd'], data['phonepwd2'],
                                     data['errormsg'])


"""
if __name__ == "__main__":
    unittest.main()
"""

"""
def MySuitePrefixAdd(MyClass,cases):
    '''
    根据前缀添加测试用例-可用于ddt数据用例
    :param MyClass:
    :param cases:
    :return:
    '''
    test_list = []
    testdict = MyClass.__dict__
    #print(testdict)
    if isinstance(cases,str):
        cases = [cases]
    for case in cases:
        tmp_cases = filter(lambda cs:cs.startswith(case) and callable(getattr(MyClass,cs)),testdict)
        for tmp_case in tmp_cases:
            test_list.append(MyClass(tmp_case))
    suite = unittest.TestSuite()
    suite.addTests(test_list)
    return suite


if __name__ == "__main__":

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(MySuitePrefixAdd(TestGanjiRegister,["test_register_check_username","test_register_check_phone"]))


    unittest.main()

    suite = unittest.TestSuite()
    #test = [TestGanjiRegister("test_register_check_username"), TestGanjiRegister("test_register_check_phone"), TestGanjiRegister("test_register_check_phonepwd"), TestGanjiRegister("test_register_check_phonepwd2")]
    #tests = map(TestGanjiRegister, test)
    tests = TestGanjiRegister("test_register_check_username")
    print(tests)
    #suite.addTestss(tests)
    #suite.addTests(test)
    #runner1 = unittest.TextTestRunner(verbosity=2)
    #runner1.run(suite) """
