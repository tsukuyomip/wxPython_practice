#coding: utf-8

import wx

if __name__ == "__main__":
    application = wx.App()

    frame = wx.Frame(None, wx.ID_ANY, "テストフレーム！",\
                     size = (400, 500), pos = (0, 30))
    frame.CreateStatusBar()
    frame.SetStatusText("status text test!")

    frame.Show()

    application.MainLoop()
