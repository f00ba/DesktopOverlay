import wx

class Hex(wx.Frame):

    def __init__(self, parent, id, title, pos):
        wx.Frame.__init__(self, parent, id, title, pos, size=(102, 90))

        self.panel = wx.Panel(self, -1)
        self.bitmap = wx.Bitmap("hex.png")
        self.image = wx.StaticBitmap(self.panel, -1, self.bitmap)

        self.image.SetPosition((0,0))

        self.SetTransparent(255)
