#将根目录加入sys.path中,解决命令行找不到包的问题
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))