from tkinter import *
from PIL import Image
class Hex(Toplevel):

    def __init__(self, parent, x, y, title="Hex"):

        super(Hex, self).__init__(parent)

        self.parent = parent

        self.image_normal = PhotoImage(file="hexagon_normal.png")
        self.image_move = PhotoImage(file="hexagon_normal_move.png")
        self.image_hover = PhotoImage(file="hexagon_hover.png")
        self.image_click = PhotoImage(file="hexagon_click.png")

        self.x = x
        self.y = y

        self.w = 104
        self.h = 90

        self.config(width=self.w, height=self.h)

        self.title(title)
        self.geometry(self.translateGeometry(x, y, self.w, self.h))

        self.overrideredirect(True)
        self.configure(background='white')
        self.wm_attributes("-topmost", True)
        #self.wm_attributes("-disabled", True)
        self.wm_attributes("-transparentcolor", "white")

        self.hex_img = Label(self, image=self.image_normal, width=self.w, height=self.h, bg='white')
        self.hex_img.place(x=-2, y=-2)

        self.hex_img.bind("<Button 1>", self.on_click)
        self.hex_img.bind("<ButtonRelease 1>", self.mouse_up)
        self.hex_img.bind("<Enter>", self.on_mouse_enter)
        self.hex_img.bind("<Leave>", self.on_mouse_leave)

      #  self.frame.place(x=0, y=0)

    def translateGeometry(self, x, y, w, h):
        #print(str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y))
        return str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)

    def on_mouse_enter(self, evt):
        """
        self.hex_img = Label(self, image=self.image_hover, width=self.w, height=self.h, bg='white')
        self.hex_img.place(x=-2, y=-2)

        self.hex_img.bind("<Button 1>", self.on_click)
        self.hex_img.bind("<ButtonRelease 1>", self.mouse_up)
        self.hex_img.bind("<Enter>", self.on_mouse_enter)
        self.hex_img.bind("<Leave>", self.on_mouse_leave)
        """
    def on_mouse_leave(self, evt):
        """
        hex = 'hexagon.png'
        ico = 's.png'

        hex_img = Image.open(hex)
        ico_img = Image.open(ico)

        hex_img.paste(ico_img, (int(self.w / 2) - 25, int(self.h / 2) - 25), ico_img)
        hex_img.save("tmp.png", "PNG")

       # print("MOUSE LEFT")

        self.hex_img = Label(self, image=hex_img, width=self.w, height=self.h, bg='white')
        self.hex_img.place(x=-2, y=-2)

        self.hex_img.bind("<Button 1>", self.on_click)
        self.hex_img.bind("<ButtonRelease 1>", self.mouse_up)
        self.hex_img.bind("<Enter>", self.on_mouse_enter)
        self.hex_img.bind("<Leave>", self.on_mouse_leave)
        """

    def on_click(self, evt):

        self.hexImg = Label(self, image=self.image_click, width=self.w, height=self.h, bg='white')
        self.hexImg.place(x=-2, y=-2)

        self.hexImg.bind("<Button 1>", self.on_click)
        self.hexImg.bind("<ButtonRelease 1>", self.mouse_up)
        self.hexImg.bind("<Enter>", self.on_mouse_enter)
        self.hexImg.bind("<Leave>", self.on_mouse_leave)


    def mouse_up(self, evt):
        """
        self.hex_img = Label(self, image=self.image_normal, width=self.w, height=self.h, bg='white')
        self.hex_img.place(x=-2, y=-2)

        self.hex_img.bind("<Button 1>", self.on_click)
        self.hex_img.bind("<ButtonRelease 1>", self.mouse_up)
        self.hex_img.bind("<Enter>", self.on_mouse_enter)
        self.hex_img.bind("<Leave>", self.on_mouse_leave)
        """
        if self.parent.move_mode == True:

            move_okay= True

            screenX = self.x + evt.x
            screenY = self.y + evt.y

            newX = screenX - ((screenX - self.parent.offset_x) % int(self.w * 0.75))

            if not ((newX - self.parent.offset_x) / (self.w * 0.75) < 23 and (newX - self.parent.offset_x) / (self.w * 0.75) >= 0):
                move_okay = False

            if int((newX - self.parent.offset_x) / (self.w * 0.75)) % 2 == 0:
                print("Hello")
                newY = screenY - ((screenY - self.parent.offset_y - int(self.h * 0.5)) % self.h)# + int(self.h * 0.5)
                if not (((newY - (self.h * 0.5) - self.parent.offset_y) / self.h < 11) and ((newY - (self.h * 0.5) - self.parent.offset_y) / self.h >= 0)):
                    move_okay = False
            else:
                newY = screenY - ((screenY - self.parent.offset_y) % self.h)
                if not (((newY - self.parent.offset_y) / self.h < 12) and ((newY - self.parent.offset_y) / self.h >= 0)):
                    move_okay = False

            if move_okay:
                self.x = newX
                self.y = newY

                self.geometry(self.translateGeometry(newX, newY, self.w, self.h))