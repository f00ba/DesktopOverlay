__author__ = 'Apfelkuchen'

from tkinter import *
import time

class Clock(Toplevel):

    def __init__(self, parent, x, y, title="Clock"):
        super(Clock, self).__init__(parent)

        self.parent = parent

        self.x = x
        self.y = y

        self.w = 174
        self.h = 215

        self.image = PhotoImage(file="clock.png")

        self.config(width=self.w, height=self.h)
        self.title(title)

        self.geometry(self.translateGeometry(x, y, self.w, self.h))

        #self.overrideredirect(True)
        self.configure(background='white')
        self.wm_attributes("-topmost", True)
        #self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")

        self.clockImg = Label(self, image=self.image, width=self.w, height=self.h, bg='white')
        self.clockImg.place(x=-2, y=-2)

        hours = time.strftime("%H", time.localtime())

        hour1 = int((int(hours) - (int(hours) % 10)) / 10)
        hour2 = int(hours) % 10


        NumberLetter(self, self.x + 50, self.y + 45, number=hour1)

    def translateGeometry(self, x, y, w, h):
        print(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
        return str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)




class NumberLetter(Toplevel):

    def __init__(self, parent, x, y, number=0 , title="Letter"):
        super(NumberLetter, self).__init__(parent)

        self.parent = parent

        self.x = x
        self.y = y

        self.w = 40
        self.h = 80

        self.config(width=self.w, height=self.h)
        self.title(title)

        self.geometry(self.translateGeometry(x, y, self.w, self.h))

        self.overrideredirect(True)
        self.configure(background='white')
        self.wm_attributes("-topmost", True)
        #self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")

        self.hour2 = Label(self, text=str(number), width=5, height=5, bg='white')
        self.hour2.place(x=-2, y=-2)


    def translateGeometry(self, x, y, w, h):
        print(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
        return str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)