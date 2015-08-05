from tkinter import *
from elements.hexagon import Hex

root = Tk()

root.image = PhotoImage(file='hex.png')
"""
clear_screen = Label(root, image=None, width=1920, height=1080)
fr = Frame(root, width=102, height=90, bg="#00ff00")
label1 = Label(fr, image=root.image, width=102, height=90, bg='white')
label1.pack()
newWindow = Toplevel(root)
fr.place(x=0, y=0, width=102, height=90)
fr2 = Frame(newWindow, width=102, height=90, bg="#0000ff")
label2 = Label(fr2, image=root.image, width=102, height=90, bg='white')
label2.pack()
fr2.place(x=80, y=0, width=102, height=90)
"""

hex1 = Hex(root, 0, 0, root.image)
hex2 = Hex(root, 102, 90, root.image, "faggot")

root.configure(background='white')
root.geometry("1920x1080+0+0")
#root.overrideredirect(True)
root.wm_attributes("-topmost", True)
#root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "white")


root.mainloop()