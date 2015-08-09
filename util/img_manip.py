__author__ = 'Apfelkuchen'

from PIL import Image

def merge_images_centered(back_image, front_image, save_path):

    bg = back_image
    fg = front_image

    bg = Image.open(bg)
    fg = Image.open(fg)

    w, h = fg.size

    bg.paste(fg, (int(w / 2) - 25, int(h / 2) - 25), fg)
    bg.save(save_path, "PNG")