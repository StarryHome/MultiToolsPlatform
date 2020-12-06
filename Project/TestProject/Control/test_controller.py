from Common.Template.main_frame import MainFrame
from Project.TestProject.Frame.test_panel_1 import TestPanel1


class TestController(MainFrame):
    def __init__(self, parent, title):
        MainFrame.__init__(self, parent)
        self.SetTitle(title)

        self.test_panel_1 = TestPanel1(self.m_notebook)
        self.addPanel(self.test_panel_1, '测试页1', True)
        self.test_panel_2 = TestPanel1(self.m_notebook)
        self.addPanel(self.test_panel_2, '测试页2')
