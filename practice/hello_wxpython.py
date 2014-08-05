#coding: utf-8

import wx

if __name__ == "__main__":
    application = wx.App()

    frame = wx.Frame(None, wx.ID_ANY, "テストフレーム！",\
                     size = (400, 500), pos = (0, 30))
    frame.SetBackgroundColour("#AAAAAA")

    r_panel = wx.Panel(frame, wx.ID_ANY, pos = (0, 0), size = (80, 500))
    r_panel.SetBackgroundColour("#FFAAAA")
    g_panel = wx.Panel(frame, wx.ID_ANY, pos = (80, 0), size = (80, 500))
    g_panel.SetBackgroundColour("#AAFFAA")
    b_panel = wx.Panel(frame, wx.ID_ANY, pos = (160, 0), size = (80, 500))
    b_panel.SetBackgroundColour("#AAAAFF")


    frame.CreateStatusBar()
    frame.SetStatusText("status text test!")

    frame.Show()

    application.MainLoop()
