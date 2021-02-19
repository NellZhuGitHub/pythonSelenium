import os
import sys
#动态添加D:\Python-web-selenium路径作为模块加载路径
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class DynamicImportCase(object):

    def find_pyfile_and_Import(self, rootDir):
        # 遍历rootDir下所有目录, import所有test_*.py
        '判断传入的路径下是否有"__init__.py"这个文件，如果没有则创建，否则import会认为没有这个module'
        if os.path.exists(rootDir):
            arr = rootDir.split("/")
            pathDir = ""
            for path in arr:
                pathDir = pathDir + path + "/"
                if not os.path.exists(pathDir + "/__init__.py"):
                    f = open(pathDir + "/__init__.py", "wb")
                    f.close()
        # 遍历文件找出test_开头的py文件，导入，注意globals，否则作用域只是在这个函数下
        list_dirs = os.walk(rootDir)
        exe_strs = []
        for dirPath, dirNames, filenames in list_dirs:
            for f in filenames:
                print(filenames)
                file_name = f
                if file_name[0:5] == "test_" and file_name[-3:] == ".py":
                    if dirPath[-1:] != "/":
                        impPath = dirPath.replace("/",".")[2:].replace("\\",".")
                    else:
                        impPath = dirPath.replace("/",".")[2:-1]
                    if impPath != "":
                        exe_str = "from " + impPath + " import " + file_name[0:-3]
                    else:
                        exe_str = "import " + file_name[0:-3]
                    print(exe_str)
                    exe_strs.append(exe_str)
                    #exec(exe_str, globals())
        return exe_strs

'''
find_pyfile_and_Import("./learn")
a = test_mathfunc.TestMathFunc()
a.test_add()
test_mathfunc.TestMathFunc().test_minus()
#test_loader.test_loader()


exe_strs = DynamicImportCase().find_pyfile_and_Import("./poModel")
print(exe_strs)
'''