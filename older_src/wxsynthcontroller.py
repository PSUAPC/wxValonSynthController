#!/usr/bin/python

#############################################
#Valon Synthesizer Controller using wxPython#
#Maintained by J. Sheldon (jms7085@psu.edu) #
#Date: 2014-06-02                           #
#                                           #
#Tested on Linux Mint 16, assumed working on#
#linux platform in general.                 #
#############################################

import wx
import valon_synth
import os.path #to check for configuration file's existence


USBPORTS = ["[Select a port]","ttyUSB0","ttyUSB1","ttyUSB2","ttyUSB3","ttyUSB4","ttyUSB5","ttyUSB6","ttyUSB7","ttyUSB8","ttyUSB9","ttyUSB10"]
DEFAULTUSBPORT = USBPORTS[0]
setport = "unset"
setbaud = 9600 #bps

#Device Selection window - chooses and saves
#which USB device is the synthesizer. Closes
#after selection, yielding to the actual sy-
#nth control panel.
class DeviceSelection(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(251,100))
        global setport
        #Define controls:
        self.portsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.portpanel = wx.Panel(self)
        self.portlabel = wx.StaticText(self.portpanel,pos=(10,20),label="Port: ", style=wx.ALIGN_RIGHT)
        self.portcombobox = wx.ComboBox(self.portpanel,pos=(40,15),choices=USBPORTS,style=wx.CB_READONLY)
        self.connectbutton = wx.Button(self.portpanel,pos=(10,45),label="Connect")
        self.exitbutton = wx.Button(self.portpanel,pos=(130,45),label="Exit")
        self.portsizer.Add(self.portpanel,1,wx.EXPAND)
        self.statusbar = self.CreateStatusBar()
        
        self.SetSize((250,100))
        self.Center()
        self.Show(True)

        #Check if config file exists and read the old port. If not, create an empty cfg file.      
        if os.path.isfile("config.cfg"):
            #Cfg file exists. Read it.
            cfgfile = open("config.cfg","r+b")
            oldport = cfgfile.read().rstrip()
            cfgfile.close()
            #Tell user that a port was found.
            self.statusbar.SetStatusText("Configuration file found & loaded!")
        else:
            #Cfg file does not exist. Make it.
            cfgfile = open("config.cfg",'w') #Possibly do some error catching if directory or file permissions aren't held.
            #write a default device as a placeholder:
            cfgfile.write("First time Run. You aren't supposed to see me!")
            oldport=USBPORTS[0]
            cfgfile.close()
            self.statusbar.SetStatusText("CFG not found, but created!")

        #set dropdown/combobox to config file's setting:
        self.portcombobox.SetStringSelection(oldport)
        #Control Bindings
        self.exitbutton.Bind(wx.EVT_BUTTON,self.OnExitButton)
        self.connectbutton.Bind(wx.EVT_BUTTON,self.OnConnectButton)
        self.portcombobox.Bind(wx.EVT_COMBOBOX,self.OnPortComboSelection)

    #Event Handling:
    def OnExitButton(self,event):
        self.Destroy()
        #Remove the following after development is over:
        synthcont = SynthController(None,"Valon Synth Controller: DEMO MODE - NO CONNECTION")

    def OnConnectButton(self,event):
        global setport
        #Error handle serial port connections.
        self.statusbar.SetStatusText("Serial Port Invalid!")
        synthcont = SynthController(None,"Valon Synth Controller: " + setport)

        #in event of successful connection, write correct tty device to file.
        cfgfile = open("config.cfg",'w') #Possibly do some error catching if directory or file permissions aren't held.
        #write a default device as a placeholder:
        cfgfile.write(setport)
        cfgfile.close()

    def OnPortComboSelection(self, event):
        global setport
        setport = self.portcombobox.GetValue()


        

class SynthController(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(601,400))

        #Define controls:
        self.synthAsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.synthBsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.synthApanel = wx.Panel(self)
        self.synthBpanel = wx.Panel(self)
        self.synthAlabel = wx.StaticText(self.synthApanel,pos=(10,20),label="Synth A", style=wx.ALIGN_LEFT)
        self.synthBlabel = wx.StaticText(self.synthBpanel,pos=(10,20),label="Synth B", style=wx.ALIGN_LEFT)
        
        
        self.SetSize((600,400))
        self.Center()
        self.Show(True)

        #Control Bindings

        #Event Handling:


app = wx.App(False)
devsel = DeviceSelection(None,"Valon Synth Selection")
app.MainLoop()
