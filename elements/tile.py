__author__ = 'Apfelkuchen'

from tkinter import *

class Tile(Toplevel):

    def __init__(self, parent, id, x, y, w, h):

        super(Tile, self).__init__(parent)

        self.parent = parent
        self.id = id

        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.img_normal = PhotoImage(file="hexagon_normal.png")
        self.img_hover = PhotoImage(file="hexagon_hover.png")


        self.config(width=self.w, height=self.h)
        self.title(str(id))


        self.geometry(self.translateGeometry(x, y, self.w, self.h))

        self.overrideredirect(True)
        self.configure(background='white')
        self.wm_attributes("-transparentcolor", "white")

        if parent.debug:
            self.wm_attributes("-topmost", True)

        self.tile_img = Label(self, image=self.img_normal, width=self.w, height=self.h, bg='white')
        self.tile_img.place(x=-2, y=-2)

        #self.tile_img.bind("<Button 1>", self.on_click)
        self.tile_img.bind("<ButtonRelease 1>", self.mouse_up)
        self.tile_img.bind("<Enter>", self.on_mouse_enter)
        self.tile_img.bind("<Leave>", self.on_mouse_leave)


#--- END DEF --------------------------------------------

    def translateGeometry(self, x, y, w, h):
        return str(w) + "x" + str(h) + "+" + str(x) + "+" + str(y)

#--- END DEF --------------------------------------------

    def change_hover_image(self, image):
        self.tile_img = Label(self, image=image, width=self.w, height=self.h, bg='white')
        self.tile_img.place(x=-2, y=-2)

       # self.tile_img.bind("<Button 1>", self.on_click)
        self.tile_img.bind("<ButtonRelease 1>", self.mouse_up)
        self.tile_img.bind("<Enter>", self.on_mouse_enter)
        self.tile_img.bind("<Leave>", self.on_mouse_leave)

#--- END DEF --------------------------------------------

    def on_mouse_enter(self, evt):
        self.change_hover_image(self.img_hover)

#--- END DEF --------------------------------------------

    def on_mouse_leave(self, evt):
        self.change_hover_image(self.img_normal)

#--- END DEF --------------------------------------------

    # Rewrite please
    def mouse_up(self, evt):

        if self.parent.move_mode == True:

            move_okay= True

            screenX = self.x + evt.x
            screenY = self.y + evt.y

            newX = screenX - ((screenX - self.parent.tile_offset_x) % int(self.w * self.parent.tile_distance_x))

            if not ((newX - self.parent.tile_offset_x) / int(self.w * self.parent.tile_distance_x) < 23 and newX - self.parent.tile_offset_x / int(self.w * self.parent.tile_distance_x) >= 0):
                move_okay = False


            if int((newX - self.parent.tile_offset_x) / (self.w * self.parent.tile_distance_x)) % 2 == 0:
                print("Hello")
                newY = screenY - ((screenY - self.parent.tile_offset_y + int(self.h * self.parent.tile_distance_y_2nd)) % int(self.parent.tile_distance_y * self.h))
                if not (((newY - int(self.h * self.parent.tile_distance_y_2nd) - self.parent.tile_offset_y) / int(self.parent.tile_distance_y * self.h) < 11) and ((newY - int(self.h * self.parent.tile_distance_y_2nd) - self.parent.tile_offset_y) / int(self.parent.tile_distance_y * self.h) >= 0)):
                    move_okay = False
            else:
                newY = screenY - ((screenY - self.parent.tile_offset_y) % int(self.parent.tile_distance_y * self.h))
                if not (((newY - self.parent.tile_offset_y) / (self.h * self.parent.tile_distance_y) < 12) and ((newY - self.parent.tile_offset_y) / (self.h * self.parent.tile_distance_y) >= 0)):
                    move_okay = False

            print(move_okay, screenX, screenY)

            print((newX - self.parent.tile_offset_x) / (self.w * self.parent.tile_distance_x))

            #if move_okay:
            self.x = newX
            self.y = newY

            print((newX - self.parent.tile_offset_x) / self.w)

            self.geometry(self.translateGeometry(newX, newY, self.w, self.h))

#--- END DEF --------------------------------------------