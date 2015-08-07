from tkinter import *
from elements.hexagon import Hex
from elements.main_frame import MainFrame

def add_hex_at_grid_location(x, y, w, h):
    trueX = (w*0.5) + (w*0.75) * x
    if x % 2 == 0:
        trueY = (h*0.5) + h * y
    else:
        trueY = h + h * y

    print(str(trueX) + ", " + str(trueY))
    return Hex(root, int(trueX), int(trueY), root.hex_image)
#END DEF=======================================================================



root = Tk()

root.move_mode = True

root.hex_image = PhotoImage(file='hexagon_normal.png')
root.mf_image = PhotoImage(file='main_frame.png')

#mf = MainFrame(root, root.mf_image)
"""
hex1 = Hex(root, 94, 55, root.image)
hex2 = Hex(root, 94, 165, root.image)
hex3 = Hex(root, 188, 220, root.image)
"""

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
