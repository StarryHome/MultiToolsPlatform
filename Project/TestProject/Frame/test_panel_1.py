# -*- coding: utf-8 -*-
from Common.Template.common_panel import CommonPanel


class TestPanel1(CommonPanel):
    def __init__(self, parent):
        CommonPanel.__init__(self, parent)

        sizer = self.add_box_sizer()
        self.add_lable_textctrl(sizer, '姓名')