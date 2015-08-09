from tkinter import *

class MainFrame(Toplevel):

    def __init__(self, parent, image, title="Test"):

        super(MainFrame, self).__init__(parent)

        self.config(width=735, height=500)

        self.title(title)
        self.geometry(self.translateGeometry(0, 0, 735, 500))

        self.overrideredirect(True)
        self.configure(background='white')
        self.wm_attributes("-topmost", True)
        #self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")

       # self.frame = Frame(self, width=102, height=90, bg="#ffffff")

        self.mfImg = Label(self, image=image, width=735, height=500, bg='white')
        self.mfImg.place(x=-2, y=-2)

      #  self.frame.place(x=0, y=0)

    def translateGeometry(self, x, y, w, h):
        print(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
       # return str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)
    """
    def translateGeometry(self, x, y, w, h, screen_width, screen_height):
        geoString = str(w) + "x" + str(h)
        xCo = screen_width - w - x - 2
        yCo = screen_height - h - y - 2
        geoString = geoString + "+" + str(xCo) + "+" + str(yCo)
        print(geoString)
        return geoString
    """

