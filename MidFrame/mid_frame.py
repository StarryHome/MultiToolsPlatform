# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class MyFrame1
###########################################################################

class MidFrame(wx.MDIParentFrame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.m_menubar = wx.MenuBar(0)
        self.m_menu = wx.Menu()
        self.m_menuItem_system_setting = wx.MenuItem(self.m_menu, wx.ID_ANY, u"系统设置1", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu.Append(self.m_menuItem_system_setting)

        self.m_menubar.Append(self.m_menu, u"设置")

        self.m_menu = wx.Menu()
        self.m_menuItem_test = wx.MenuItem(self.m_menu, wx.ID_ANY, u"测试工具1", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu.Append(self.m_menuItem_test)
        self.m_menuItem_test2 = wx.MenuItem(self.m_menu, wx.ID_ANY, u"测试工具2", wx.EmptyString, wx.ITEM_NORMAL)
        self.m_menu.Append(self.m_menuItem_test2)

        self.m_menubar.Append(self.m_menu, u"测试")

        self.SetMenuBar(self.m_menubar)

        self.Centre(wx.BOTH)

    def __del__(self):
        pass


