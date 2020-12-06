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
## Class MainFrame
###########################################################################

class MainFrame(wx.MDIChildFrame):

    def __init__(self, parent):
        wx.MDIChildFrame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(500, 300), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        # self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.m_notebook = wx.Notebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
        main_sizer.Add(self.m_notebook, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(main_sizer)
        self.Centre(wx.BOTH)

    def addPanel(self, panel, title, show=False):
        self.m_notebook.AddPage(panel, title, show)
        # return new_panel

    def __del__(self):
        pass
