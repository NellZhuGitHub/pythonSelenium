# coding = utf-8
import configparser

class ReadIni:
    def __init__(self, file_name=None):
        if file_name == None:
            file_name = 'D:/autotest/pythonSelenium/config/config.ini'
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        """读取配置文件"""
        cf = configparser.ConfigParser()
        cf.read(file_name, encoding='utf-8')
        return cf

    def get_ini(self, node_name, key):
        return self.cf.get(node_name, key)

# 初始化实例，后面引入直接使用，无需初始化实例了，单例模式
read_ini = ReadIni()