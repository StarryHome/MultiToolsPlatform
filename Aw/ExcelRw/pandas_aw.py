# -*- coding: utf-8 -*-
import pandas


class PandasAw(object):
    instance = None

    def __init__(self):
        self.excel = None

    @staticmethod
    def get_instance():
        if PandasAw.instance is None:
            PandasAw.instance = PandasAw()
        return PandasAw.instance

    def read(self, file_name, sheet_name=0):
        """
        @summary: 读取sheet页
        """
        self.excel = pandas.read_excel(file_name, sheet_name)
        return self.excel

    def get_title(self):
        """
        @summary: 获取当前页面标题
        """
        return self.excel.columns.values

    def get_data(self):
        """
        @summary: 获取当前页面数据
        """
        return self.excel.values


if __name__ == '__main__':
    pd = PandasAw.get_instance()
    file = r'C:\Users\Administrator\Desktop\test\数据源.xlsx'
    pd.read(file)
    titles = pd.get_title()
    print(titles)
    data = pd.get_data()
    print(data)
