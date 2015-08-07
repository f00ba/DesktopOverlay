from tkinter import *

class Hex(Toplevel):

    def __init__(self, parent, x, y, title="Hex"):

        super(Hex, self).__init__(parent)

        self.parent = parent

        self.image_normal = PhotoImage(file="hexagon_normal.png")
        self.image_hover = PhotoImage(file="hexagon_hover.png")

        self.x = x
        self.y = y

        self.w = 104
        self.h = 90

        self.config(width=104, height=90)

        self.title(title)
        self.geometry(self.translateGeometry(x, y, self.w, self.h))

        self.overrideredirect(True)
        self.configure(background='white')
        self.wm_attributes("-topmost", True)
        #self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")

       # self.frame = Frame(self, width=102, height=90, bg="#ffffff")

        self.hexImg = Label(self, image=self.image_normal, width=self.w, height=self.h, bg='white')
        self.hexImg.place(x=-2, y=-2)

        self.hexImg.bind("<Button 1>", self.on_click)
        self.hexImg.bind("<ButtonRelease 1>", self.mouse_up)
        self.hexImg.bind("<Enter>", self.on_mouse_enter)
        self.hexImg.bind("<Leave>", self.on_mouse_leave)

      #  self.frame.place(x=0, y=0)

    def translateGeometry(self, x, y, w, h):
        print(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
        return str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)

    def on_mouse_enter(self, evt):
        self.hexImg = Label(self, image=self.image_hover, width=self.w, height=self.h, bg='white')
        self.hexImg.place(x=-2, y=-2)

        self.hexImg.bind("<Button 1>", self.on_click)
        self.hexImg.bind("<ButtonRelease 1>", self.mouse_up)
        self.hexImg.bind("<Enter>", self.on_mouse_enter)
        self.hexImg.bind("<Leave>", self.on_mouse_leave)

    def on_mouse_leave(self, evt):
        self.hexImg = Label(self, image=self.image_normal, width=self.w, height=self.h, bg='white')
        self.hexImg.place(x=-2, y=-2)

        self.hexImg.bind("<Button 1>", self.on_click)
        self.hexImg.bind("<ButtonRelease 1>", self.mouse_up)
        self.hexImg.bind("<Enter>", self.on_mouse_enter)
        self.hexImg.bind("<Leave>", self.on_mouse_leave)

    def on_click(self, evt):
        print("You have clicked me")

    def mouse_up(self, evt):
        if self.parent.move_mode == True:

            move_okay= True

            screenX = self.x + evt.x
            screenY = self.y + evt.y

            newX = screenX - ((screenX - int(self.w * 0.5)) % int(self.w * 0.75))

            if not ((newX - (self.w * 0.5)) / (self.w * 0.75) < 23 and (newX - (self.w * 0.5)) / (self.w * 0.75) >= 0):
                move_okay = False

            if ((newX - self.w * 0.5) / (self.w * 0.75)) % 2 == 0:
                newY = screenY - ((screenY - int(self.h * 0.5)) % self.h)
                if not (((newY - (self.h * 0.5)) / self.h < 11) and ((newY - (self.h * 0.5)) / self.h >= 0)):
                    move_okay = False
            else:
                newY = screenY - (screenY % self.h)
                if not (((newY - self.h ) / self.h < 12) and ((newY - self.h) / self.h >= 0)):
                    move_okay = False

            print(str(int((newX - self.w * 0.5) / (self.w * 0.75))) + " / " + str(int((newY - self.h) / self.h)))

            if move_okay:
                self.x = newX
                self.y = newY

                self.geometry(self.translateGeometry(newX, newY, self.w, self.h))