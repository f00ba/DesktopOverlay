__author__ = 'Apfelkuchen'

import wx

class Hex(wx.Frame):
    def __init__(self, parent, size=(102, 90), pos=(0, 0)):
        super(Hex, self).__init__(parent, size=size, pos=pos, style=(wx.TRANSPARENT_WINDOW))

        #self.SetBackgroundColour("#")
        self.bmp = wx.Bitmap("hex.png", wx.BITMAP_TYPE_PNG)
       # self.hasShape = self.SetShape(self.bmp)
        self.hasShape = False
        self.Bind(wx.EVT_PAINT, self.onPaint)
        self.Bind(wx.EVT_LEFT_DCLICK, self.onClick)
        self.Bind(wx.EVT_WINDOW_CREATE, self.SetWindowShape)
        self.Show()

    def onPaint(self, event):
        print("test")
        bdc = wx.PaintDC(self)
        dc = wx.GCDC(bdc)
        event.Skip()
      #  dc.SetPen(wx.WHITE_PEN)
     #   dc.SetBrush(wx.WHITE_BRUSH)
      #  dc.DrawRectangle(0, 0, 200, 100)
      #  dc.DrawBitmap(self.bmp, 0, 0)

    def SetWindowShape(self, evt):
        # Use the bitmap's mask to determine the region
        r = wx.Region(self.bmp)
        self.hasShape = self.SetShape(r)

    def onClick(self, event):
        print("Hello")
