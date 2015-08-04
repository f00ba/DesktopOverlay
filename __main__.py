import wx
from elements.hexagon import Hex

app = wx.App()

one_hex = Hex(None, -1, 'test', (0, 0))
one_hex.Show()
app.MainLoop()