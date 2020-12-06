# -*- coding: utf-8 -*-
from .pandas_aw import PandasAw


class AuditAw(object):
    """
    @summary: 审核AW类，负责审核规则整体流程
    """
    def __init__(self):
        self.result = []

    def audit_report(self, visit_data_path, visit_demand_path, outliers_path):
        """
        @summary: 审核报告入口
        """
        # 1.获取数据源
        visit_data_title, visit_data_list, visit_demand = self.read_excel(visit_data_path, visit_demand_path)
        # 2.审核数据
        for data in visit_data_list:
            res = self.audit_process(data)
            self.result.append(res)
        # 3.写入异常值清单
        return self.write_outliers(self.result, outliers_path)

    def read_excel(self, visit_data_path, visit_demand_path):
        """
        @summary: 读取excel数据
        @param visit_data_path: 走访数据excel路径
        @param visit_demand_path: 走访要求excel路径
        """
        pd = PandasAw.get_instance()
        pd.read(visit_data_path)
        visit_data_title = pd.get_title()
        visit_data_list = pd.get_data()

        pd.read(visit_demand_path)
        visit_demand = pd.get_data()
        return visit_data_title, visit_data_list, visit_demand

    def audit_process(self, data):
        return 0

    def write_outliers(self, result, outliers_path):
        return True


if __name__ == '__main__':
    audit = AuditAw()
    visit_data_path = r'C:\Users\Administrator\Desktop\test\数据源.xlsx'
    visit_demand_path = r'C:\Users\Administrator\Desktop\test\走访要求.xlsx'
    outliers_path = r'C:\Users\Administrator\Desktop\test\异常值清单.xlsx'
    audit.audit_report(visit_data_path, visit_demand_path, outliers_path)