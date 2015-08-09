from tkinter import *
from elements.hexagon import Hex
from elements.tile import Tile
from elements.main_frame import MainFrame

def add_hex_at_grid_location(x, y, w, h):
    trueX = int(w * root.tile_distance_x) * x + root.tile_offset_x
    if x % 2 == 0:
        trueY = int(h * root.tile_distance_y) * y + root.tile_offset_y + (h * root.tile_distance_y_2nd)
    else:
        trueY = int(h * root.tile_distance_y) * y + root.tile_offset_y

    return Tile(root, 0, int(trueX), int(trueY), 104, 90)

#--- END DEF --------------------------------------------

def setup_grid():
    root.grid_max_x = root.screen_width - root.tile_offset_x
    root.grid_max_x = root.grid_max_x - (root.grid_max_x % int(root.tile_width * root.tile_distance_x))
    root.grid_max_x = int(root.grid_max_x / int(root.tile_width * root.tile_distance_x))

    if root.grid_max_x * (int(root.tile_width * root.tile_distance_x)) + root.tile_offset_x > 1920:
        root.grid_max_x = root.grid_max_x - 1

    if root.tile_distance_y_2nd >= 0:
        root.grid_max_y = root.screen_height - root.tile_offset_y - int(root.tile_distance_y_2nd * root.tile_height)
        root.grid_max_y = root.grid_max_y - (root.grid_max_y % int(root.tile_height * root.tile_distance_y))
        root.grid_max_y = int(root.grid_max_y / int(root.tile_height * root.tile_distance_y))
    else:
        root.grid_max_y = root.screen_height - root.tile_offset_y
        root.grid_max_y = root.grid_max_y - (root.grid_max_x % int(root.tile_height * root.tile_distance_y))
        root.grid_max_y = int(root.grid_max_y / int(root.tile_height * root.tile_distance_y))

#--- END DEF --------------------------------------------


root = Tk()

root.debug = False

root.screen_width = 1920
root.screen_height = 1080

root.tile_offset_x = 30
root.tile_offset_y = 24

root.tile_width = 104
root.tile_height = 90

root.tile_distance_x = 0.75
root.tile_distance_y = 1.00
root.tile_distance_y_2nd = 0.50

setup_grid()

root.move_mode = True

root.hex_image = PhotoImage(file='tmp.png')
root.mf_image = PhotoImage(file='hex_main-01.png')

mf = MainFrame(root, root.mf_image)
"""
hex1 = Hex(root, 94, 55, root.image)
hex2 = Hex(root, 94, 165, root.image)
hex3 = Hex(root, 188, 220, root.image)
"""

#Clock(root, 200, 200)


add_hex_at_grid_location(0,0, 104, 90)
add_hex_at_grid_location(1,0, 104, 90)
add_hex_at_grid_location(1,1, 104, 90)
add_hex_at_grid_location(1,2, 104, 90)
add_hex_at_grid_location(2,2, 104, 90)
add_hex_at_grid_location(3,2, 104, 90)

root.configure(background='white')
root.geometry("1920x1080+0+0")
root.overrideredirect(True)
root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")


root.mainloop()



#94, 55 - 0 / 0
#94, 165 - 0 / 1 (+110)
#188, 220 - 1 / 0  (+94 / +110)
