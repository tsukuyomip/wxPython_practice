#coding: utf-8

import wx

if __name__ == "__main__":
    application = wx.App()

    frame = wx.Frame(None, wx.ID_ANY, "テストフレーム！",\
                     size = (400, 500), pos = (0, 30))
    frame.SetBackgroundColour("#AAAAAA")

    panel = wx.Panel(frame, wx.ID_ANY)
    panel.SetBackgroundColour("#AFAFAF")

    button_1 = wx.Button(panel, wx.ID_ANY, "Button1")
    button_2 = wx.Button(panel, wx.ID_ANY, "Button2")
    button_3 = wx.Button(panel, wx.ID_ANY, "Button3")

    layout = wx.BoxSizer(wx.HORIZONTAL)
    layout.Add(button_1, proportion = 1)
    layout.Add(button_2, proportion = 1)
    layout.Add(button_3, proportion = 1)

    panel.SetSizer(layout)

    frame.Show()

    application.MainLoop()
