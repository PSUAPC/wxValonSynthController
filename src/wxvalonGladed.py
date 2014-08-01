#!/usr/bin/python

#############################################
#Valon Synthesizer Controller using wxPython#
#Maintained by J. Sheldon (jms7085@psu.edu) #
#Date: 2014-06-05                           #
#                                           #
#Tested on Linux Mint 16, assumed working on#
#linux platform in general.                 #
#############################################
#************
#*UNFINISHED*
#************

import wx
import valon_synth
import wx.lib.agw.floatspin as FS
import os.path #to check for configuration file's existence

USBPORTS = ["[Select a port]","ttyUSB0","ttyUSB1","ttyUSB2","ttyUSB3","ttyUSB4","ttyUSB5","ttyUSB6","ttyUSB7","ttyUSB8","ttyUSB9","ttyUSB10"]
DEFAULTUSBPORT = USBPORTS[0]
setport = "unset"
setbaud = 9600 #bps

#Device Selection window - chooses and saves
#which USB device is the synthesizer. Closes
#after selection, yielding to the actual sy-
#nth control panel.
class DeviceSelectionFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(251,100))
	global setport
        # begin wxGlade: DeviceSelectionFrame.__init__


        self.DeviceSelectorFrame_statusbar = self.CreateStatusBar(1, 0)
        self.Device_ComboBox = wx.ComboBox(self, wx.ID_ANY, choices=USBPORTS, style=wx.CB_DROPDOWN)
        self.Device_ConnectButton = wx.Button(self, wx.ID_ANY, ("Connect"))
        self.Device_ExitButton = wx.Button(self, wx.ID_ANY, ("Exit"))
        self.sizer_1_staticbox = wx.StaticBox(self, wx.ID_ANY, ("ttyUSB Device Selection:"))

        self.__set_properties()
        self.__do_layout()
	self.__read_config()
        # end wxGlade
	self.Show(True)

	

    def __set_properties(self):
        # begin wxGlade: DeviceSelectionFrame.__set_properties
        self.SetTitle(("Device Selection"))
        self.DeviceSelectorFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        DeviceSelectorFrame_statusbar_fields = [("Waiting on Input")]
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

    def __read_config(self):
	#Check if config file exists and read the old port. If not, create an empty cfg file.      
        if os.path.isfile("config.cfg"):
            #Cfg file exists. Read it.
            cfgfile = open("config.cfg","r+b")
            oldport = cfgfile.read().rstrip()
            cfgfile.close()
            #Tell user that a port was found.
            self.DeviceSelectorFrame_statusbar.SetStatusText("Configuration file found & loaded!")
        else:
            #Cfg file does not exist. Make it.
            cfgfile = open("config.cfg",'w') #Possibly do some error catching if directory or file permissions aren't held.
            #write a default device as a placeholder:
            cfgfile.write("First time Run. You aren't supposed to see me!")
            oldport=USBPORTS[0]
            cfgfile.close()
            self.DeviceSelectorFrame_statusbar.SetStatusText("CFG not found, but created!")

        #set dropdown/combobox to config file's setting:
        self.Device_ComboBox.SetStringSelection(oldport)
        #Control Bindings
        self.Device_ExitButton.Bind(wx.EVT_BUTTON,self.OnExitButton)
        self.Device_ConnectButton.Bind(wx.EVT_BUTTON,self.OnConnectButton)
        self.Device_ComboBox.Bind(wx.EVT_COMBOBOX,self.OnPortComboSelection)

    #Event Handling:
    def OnExitButton(self,event):
        self.Destroy()
        #Remove the following after development is over:
        synthcont = SynthControllerFrame(None,"Valon Synth Controller: DEMO MODE - NO CONNECTION")

    def OnConnectButton(self,event):
        global setport
        #Error handle serial port connections.
        self.DeviceSelectorFrame_statusbar.SetStatusText("Serial Port Invalid!")


        #in event of successful connection, write correct tty device to file.
        cfgfile = open("config.cfg",'w') #Possibly do some error catching if directory or file permissions aren't held.
        #write a default device as a placeholder:
	setport = self.Device_ComboBox.GetValue()
        cfgfile.write(setport)
        cfgfile.close()
	synthcont = SynthControllerFrame(None,"Valon Synth Controller: " + setport)

    def OnPortComboSelection(self, event):
        global setport
        setport = self.Device_ComboBox.GetValue()
# end of class DeviceSelectionFrame

class SynthControllerFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(251,100))


        self.SynthControllerFrame_statusbar = self.CreateStatusBar(1, 0)
        self.SynthA_Label1 = wx.StaticText(self, wx.ID_ANY, ("Set Frequency (Mhz): "))
        #self.SynthA_SpinCtrl = wx.SpinCtrl(self, wx.ID_ANY, "", min=137.5, max=4400)
	self.SynthA_SpinCtrl = FS.FloatSpin(self,wx.ID_ANY,min_val=137.5, max_val=4400,increment=0.0025)
        self.SynthASet_Button = wx.Button(self, wx.ID_ANY, ("Set"))
        self.SynthA_Label2 = wx.StaticText(self, wx.ID_ANY, ("Read Frequency (Mhz):"))
        self.SynthA_TextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.SynthARead_Button = wx.Button(self, wx.ID_ANY, ("Read"))
        self.SynthA_ToggleButton = wx.ToggleButton(self, wx.ID_ANY, ("Synth Disabled.\nClick to Enable."))
        self.SynthA_sizerV1_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Synth A"))
        self.SynthB_Label1 = wx.StaticText(self, wx.ID_ANY, ("Set Frequency (Mhz):"))
        #self.SynthB_SpinCtrl = wx.SpinCtrl(self, wx.ID_ANY, "", min=137.5, max=4400)
	self.SynthB_SpinCtrl = FS.FloatSpin(self,wx.ID_ANY,min_val=137.5, max_val=4400,increment=0.0025)
        self.SynthBSet_Button = wx.Button(self, wx.ID_ANY, ("Set"))
        self.SynthB_Label2 = wx.StaticText(self, wx.ID_ANY, ("Read Frequency (Mhz):"))
        self.SynthB_TextCtrl = wx.TextCtrl(self, wx.ID_ANY, "")
        self.SynthBRead_Button = wx.Button(self, wx.ID_ANY, ("Read"))
        self.SynthB_ToggleButton = wx.ToggleButton(self, wx.ID_ANY, ("Synth Disabled.\nClick to Enable."))
        self.SynthB_SizerV1_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Synth B"))
        self.Reference_Radiobox = wx.RadioBox(self, wx.ID_ANY, ("Reference Settings"), choices=[("Reference Off"),("Use External Reference")], majorDimension=1, style=wx.RA_SPECIFY_COLS)
        self.About_Button = wx.Button(self, wx.ID_ANY, ("About"))
        self.Disconnect_Button = wx.Button(self, wx.ID_ANY, ("Disconnect and Exit"))
        self.MiscOptions_SizerV1_staticbox = wx.StaticBox(self, wx.ID_ANY, ("Misc Options"))

        self.__set_properties()
        self.__do_layout()
        # end wxGlade
	self.Show(True)

    def __set_properties(self):
        # begin wxGlade: SynthControllerFrame.__set_properties
        self.SetTitle(("Valon Synth Controller: "))
        self.SynthControllerFrame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        SynthControllerFrame_statusbar_fields = [("frame_2_statusbar")]
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
#end of Device Selection Class

app = wx.App(False)
devsel = DeviceSelectionFrame(None,"Valon Synth Controller. Device Selection")

app.MainLoop()
