# coding=utf-8

import xlrd, time, os, sys, unittest

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class DataExcel(object):
    def __init__(self, sheet_name, excel_path=None):
        if excel_path == None:
            excel_path = r"D:\autotest\pythonSelenium\exceldata\注册用例.xlsx"
        self.de = xlrd.open_workbook(excel_path)
        self.table = self.de.sheet_by_name(sheet_name)
        # 获取总行数
        self.nrows = self.table.nrows
        # 获取总列数
        self.ncols = self.table.ncols
        # 获取第一行作为key值
        self.keys = self.table.row_values(0)

    def open_excel(self, excel_path):
        try:
            self.data = xlrd.open_workbook(excel_path)
            return self.data
        except:
            print(excel_path)

    # 获取excel行数据
    def dict_data(self):
        if self.nrows <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.nrows - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.ncols):
                    ctype = self.table.cell(j, x).ctype
                    cell = self.table.cell_value(j, x)
                    if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
                        cell = int(cell)  # 浮点转成整型
                        cell = str(cell)  # 转成整型后再转成字符串，如果想要整型就去掉该行
                    elif ctype == 3:
                        data = datetime(*xldate_as_tuple(cell, 0))
                        cell = data.strftime('%Y/%m/%d %H:%M:%S')
                    elif ctype == 4:
                        cell = True if cell == 1 else False
                    # s[self.keys[x]] = values[x]
                    s[self.keys[x]] = cell
                r.append(s)
                j += 1
            return r

    # 获取excel单元格数据
    def get_cell_data(self):
        for j in range(self.ncols):
            cell_value = self.table.cell_value(0, j)
            # 获取fileName,className,caseName列名的列数
            if cell_value == "fileName":
                col1 = j
            elif cell_value == "className":
                col2 = j
            elif cell_value == "caseName":
                col3 = j
        caseList = []
        for i in range(1, self.nrows):
            # 取出ready状态的行数据，ready状态表示执行
            if str(self.table.row_values(i)[0]).lower().strip() == "ready":
                fileName = self.table.cell_value(i, col1)
                className = self.table.cell_value(i, col2)
                caseName = self.table.cell_value(i, col3)
                # 组装测试用例名称为格式：文件名.类名('方法名')
                case = '%s.%s("%s")' % (fileName.strip(), className.strip(), caseName.strip())
                caseList.append(case)

        return caseList


'''
if __name__ == "__main__":
    #caseList = DataExcel("排序用例",r"D:\Python-web-selenium\poModel\exceldata\caseOrderExcel.xlsx")
    aa = DataExcel("自动化用例",r"D:\Python-web-selenium\poModel\exceldata\登录用例.xlsx")
    #aa = DataExcel("自动化用例", r"D:\Python-web-selenium\poModel\exceldata\注册用例.xlsx")
    print(aa.dict_data())
'''




