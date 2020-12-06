# -*- coding:utf-8 -*-
import wx
from MidFrame.mid_frame_controller import MidFrameController

if __name__ == '__main__':
    app = wx.App()
    frame = MidFrameController(None)
    frame.SetMinSize((800,600))
    frame.Show(True)
    app.MainLoop()