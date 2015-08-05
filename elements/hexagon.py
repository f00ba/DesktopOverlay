from tkinter import *

class Hex:

    def __init__(self, parent, x, y, image, title="Test"):

        self.window = Toplevel(parent)
        self.window.config(width=102, height = 90)

        self.window.title(title)

        #self.window.overrideredirect(True)
        self.window.configure(background='white')
        self.window.wm_attributes("-topmost", True)
        #self.window.wm_attributes("-disabled", True)
        self.window.wm_attributes("-transparentcolor", "white")

        self.frame = Frame(self.window, width=102, height=90, bg="#00ff00")

        self.hexImg = Label(self.frame, image=image, width=102, height=90, bg='white')
        self.hexImg.pack()

        self.frame.place(x=x, y=y)

