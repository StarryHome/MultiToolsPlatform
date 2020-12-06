# -*- coding:utf-8 -*-
import wx

from MidFrame.mid_frame import MidFrame


class MidFrameController(MidFrame):
    def __init__(self, parent):
        MidFrame.__init__(self, parent)
        self.SetTitle('多工具平台')

        self.Bind(wx.EVT_MENU, self.show_test, self.m_menuItem_test)
        self.Bind(wx.EVT_MENU, self.show_test2, self.m_menuItem_test2)


    def show_frame(self, event, frame, text):
        for child in self.GetChildren():
            if child.Title == text:
                print(dir(child))
                child.Activate()
                event.Skip()
        print(dir(frame))
        frame.Maximize(True)
        frame.Show(True)

    def show_test(self, event):
        from Project.TestProject.Control.test_controller import TestController
        frame = TestController(self, 'Test')
        return self.show_frame(event, frame, 'Test')

    def show_test2(self, event):
        from Project.TestProject.Control.test_controller import TestController
        frame = TestController(self, 'Test2')
        return self.show_frame(event, frame, 'Test2')