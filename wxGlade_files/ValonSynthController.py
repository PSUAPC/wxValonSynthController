#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.7+ on Thu Jun  5 20:10:23 2014
#

# This is an automatically generated file.
# Manual changes will be overwritten without warning!

import wx
import gettext
from DeviceSelectionFrame import DeviceSelectionFrame

if __name__ == "__main__":
    gettext.install("ValonSynthController") # replace with the appropriate catalog name

    ValonSynthController = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    DeviceSelectorFrame = DeviceSelectionFrame(None, wx.ID_ANY, "")
    ValonSynthController.SetTopWindow(DeviceSelectorFrame)
    DeviceSelectorFrame.Show()
    ValonSynthController.MainLoop()