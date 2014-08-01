#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.6.7+ on Thu Jun  5 20:10:57 2014
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class DeviceSelectionFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: DeviceSelectionFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.DeviceSelectorFrame_statusbar = self.CreateStatusBar(1, 0)
        self.Device_ComboBox = wx.ComboBox(self, wx.ID_ANY, choices=[_("[Select a Device]"), _("ttyUSB0"), _("ttyUSB1"), _("ttyUSB2"), _("ttyUSB3"), _("ttyUSB4"), _("ttyUSB5"), _("ttyUSB6"), _("ttyUSB7"), _("ttyUSB8"), _("ttyUSB9"), _("ttyUSB10")], style=wx.CB_DROPDOWN)
        self.Device_ConnectButton = wx.Button(self, wx.ID_ANY, _("Connect"))
        self.Device_ExitButton = wx.Button(self, wx.ID_ANY, _("Exit"))
        self.sizer_1_staticbox = wx.StaticBox(self, wx.ID_ANY, _("ttyUSB Device Selection:"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: DeviceSelectionFrame.__set_properties
        self.SetTitle(_("Device Selection"))
        self.DeviceSelectorFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        DeviceSelectorFrame_statusbar_fields = [_("DeviceSelectorFrame_statusbar")]
        for i in range(len(DeviceSelectorFrame_statusbar_fields)):
            self.DeviceSelectorFrame_statusbar.SetStatusText(DeviceSelectorFrame_statusbar_fields[i], i)
        self.Device_ComboBox.SetSelection(-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: DeviceSelectionFrame.__do_layout
        self.sizer_1_staticbox.Lower()
        sizer_1 = wx.StaticBoxSizer(self.sizer_1_staticbox, wx.HORIZONTAL)
        sizer_1.Add(self.Device_ComboBox, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.Device_ConnectButton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_1.Add(self.Device_ExitButton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        # end wxGlade

# end of class DeviceSelectionFrame

class SynthControllerFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: SynthControllerFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SynthControllerFrame_statusbar = self.CreateStatusBar(1, 0)
        self.SynthA_Label1 = wx.StaticText(self, wx.ID_ANY, _("Set Frequency (Mhz): "))
        self.SynthA_SpinCtrl = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100)
        self.SynthASet_Button = wx.Button(self, wx.ID_ANY, _("Set"))
        self.SynthA_Label2 = wx.StaticText(self, wx.ID_ANY, _("Read Frequency (Mhz):"))
        self.SynthA_TextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.SynthARead_Button = wx.Button(self, wx.ID_ANY, _("Read"))
        self.SynthA_ToggleButton = wx.ToggleButton(self, wx.ID_ANY, _("Synth Disabled.\nClick to Enable."))
        self.SynthA_sizerV1_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Synth A"))
        self.SynthB_Label1 = wx.StaticText(self, wx.ID_ANY, _("Set Frequency (Mhz):"))
        self.SynthB_SpinCtrl = wx.SpinCtrl(self, wx.ID_ANY, "", min=0, max=100)
        self.SynthBSet_Button = wx.Button(self, wx.ID_ANY, _("Set"))
        self.SynthB_Label2 = wx.StaticText(self, wx.ID_ANY, _("Read Frequency (Mhz):"))
        self.SynthB_TextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.SynthBRead_Button = wx.Button(self, wx.ID_ANY, _("Read"))
        self.SynthB_ToggleButton = wx.ToggleButton(self, wx.ID_ANY, _("Synth Disabled.\nClick to Enable."))
        self.SynthB_SizerV1_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Synth B"))
        self.Reference_Radiobox = wx.RadioBox(self, wx.ID_ANY, _("Reference Settings"), choices=[_("Reference Off"), _("Use External Reference")], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.About_Button = wx.Button(self, wx.ID_ANY, _("About"))
        self.Disconnect_Button = wx.Button(self, wx.ID_ANY, _("Disconnect and Exit"))
        self.MiscOptions_SizerV1_staticbox = wx.StaticBox(self, wx.ID_ANY, _("Misc Options"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: SynthControllerFrame.__set_properties
        self.SetTitle(_("Valon Synth Controller: "))
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("/home/joesheldon/Desktop/SynthController/vscontrolicon.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SynthControllerFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        SynthControllerFrame_statusbar_fields = [_("frame_2_statusbar")]
        for i in range(len(SynthControllerFrame_statusbar_fields)):
            self.SynthControllerFrame_statusbar.SetStatusText(SynthControllerFrame_statusbar_fields[i], i)
        self.SynthA_ToggleButton.SetBackgroundColour(wx.Colour(255, 25, 10))
        self.SynthB_ToggleButton.SetBackgroundColour(wx.Colour(255, 25, 10))
        self.Reference_Radiobox.SetSelection(0)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: SynthControllerFrame.__do_layout
        MainSizer = wx.BoxSizer(wx.VERTICAL)
        self.MiscOptions_SizerV1_staticbox.Lower()
        MiscOptions_SizerV1 = wx.StaticBoxSizer(self.MiscOptions_SizerV1_staticbox, wx.HORIZONTAL)
        MiscOptions_SizerH1 = wx.BoxSizer(wx.VERTICAL)
        self.SynthB_SizerV1_staticbox.Lower()
        SynthB_SizerV1 = wx.StaticBoxSizer(self.SynthB_SizerV1_staticbox, wx.HORIZONTAL)
        SynthB_SizerH1 = wx.BoxSizer(wx.VERTICAL)
        SynthB_SizerV3 = wx.BoxSizer(wx.HORIZONTAL)
        SynthB_SizerV2 = wx.BoxSizer(wx.HORIZONTAL)
        self.SynthA_sizerV1_staticbox.Lower()
        SynthA_sizerV1 = wx.StaticBoxSizer(self.SynthA_sizerV1_staticbox, wx.HORIZONTAL)
        SynthA_SizerH1 = wx.BoxSizer(wx.VERTICAL)
        SynthA_SizerV3 = wx.BoxSizer(wx.HORIZONTAL)
        SynthA_SizerV2 = wx.BoxSizer(wx.HORIZONTAL)
        SynthA_SizerV2.Add(self.SynthA_Label1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthA_SizerV2.Add(self.SynthA_SpinCtrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthA_SizerV2.Add(self.SynthASet_Button, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthA_SizerH1.Add(SynthA_SizerV2, 1, wx.EXPAND, 0)
        SynthA_SizerV3.Add(self.SynthA_Label2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthA_SizerV3.Add(self.SynthA_TextCtrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthA_SizerV3.Add(self.SynthARead_Button, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthA_SizerH1.Add(SynthA_SizerV3, 1, wx.EXPAND, 0)
        SynthA_sizerV1.Add(SynthA_SizerH1, 1, wx.EXPAND, 0)
        SynthA_sizerV1.Add(self.SynthA_ToggleButton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        MainSizer.Add(SynthA_sizerV1, 1, wx.EXPAND, 0)
        SynthB_SizerV2.Add(self.SynthB_Label1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthB_SizerV2.Add(self.SynthB_SpinCtrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthB_SizerV2.Add(self.SynthBSet_Button, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthB_SizerH1.Add(SynthB_SizerV2, 1, wx.EXPAND, 0)
        SynthB_SizerV3.Add(self.SynthB_Label2, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthB_SizerV3.Add(self.SynthB_TextCtrl, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthB_SizerV3.Add(self.SynthBRead_Button, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        SynthB_SizerH1.Add(SynthB_SizerV3, 1, wx.EXPAND, 0)
        SynthB_SizerV1.Add(SynthB_SizerH1, 1, wx.EXPAND, 0)
        SynthB_SizerV1.Add(self.SynthB_ToggleButton, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        MainSizer.Add(SynthB_SizerV1, 1, wx.EXPAND, 0)
        MiscOptions_SizerV1.Add(self.Reference_Radiobox, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        MiscOptions_SizerH1.Add(self.About_Button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        MiscOptions_SizerH1.Add(self.Disconnect_Button, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        MiscOptions_SizerV1.Add(MiscOptions_SizerH1, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
        MainSizer.Add(MiscOptions_SizerV1, 1, wx.EXPAND, 0)
        self.SetSizer(MainSizer)
        MainSizer.Fit(self)
        self.Layout()
        # end wxGlade

# end of class SynthControllerFrame
if __name__ == "__main__":
    gettext.install("ValonSynthController") # replace with the appropriate catalog name

    ValonSynthController = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    DeviceSelectorFrame = DeviceSelectionFrame(None, wx.ID_ANY, "")
    ValonSynthController.SetTopWindow(DeviceSelectorFrame)
    DeviceSelectorFrame.Show()
    ValonSynthController.MainLoop()