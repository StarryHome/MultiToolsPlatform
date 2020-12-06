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
## Class CommonTestPanel
###########################################################################

class CommonPanel(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id=wx.ID_ANY, pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.TAB_TRAVERSAL)

        self.mian_size = wx.BoxSizer(wx.VERTICAL)
        self.m_notebook = None
        self.SetSizer(self.mian_size)
        self.Layout()

    def add_page(self, page, title, **kwargs):
        if self.m_notebook is None:
            self.m_notebook = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
            self.mian_size.Add( self.m_notebook, 1, wx.EXPAND |wx.ALL, 5 )
        if 'status' in kwargs:
            status = True
        else:
            status = False
        self.m_notebook.AddPage(page, title, status)

    def add_box_sizer(self):
        bSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.mian_size.Add( bSizer, 0, wx.EXPAND, 5 )
        return bSizer

    def add_lable_textctrl(self, sizer, label, **kwargs):
        if 'lable_with' in kwargs:
            lable_with = kwargs['lable_with']
        else:
            lable_with = -1
        staticText = wx.StaticText(self, wx.ID_ANY, label, wx.DefaultPosition, wx.Size( lable_with,-1 ), 0)
        staticText.Wrap(-1)
        textCtrl = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
        sizer.Add(staticText, 0, wx.ALL, 5)
        if 'proportion' in kwargs:
            proportion = kwargs['proportion']
        else:
            proportion = 1
        sizer.Add(textCtrl, proportion, wx.ALL, 5)
        return textCtrl

    def __del__(self):
        pass


