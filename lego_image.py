import itertools
from math import sqrt

from PIL import Image

from lego_tuple import Lego_return_tuple

im = Image.open("joker.jpg") # what is a good way to pass argument from main project.py file?
# rgb_im = im.convert("RGB")
size = (48, 48)


tpl_x = range(48)
tpl_y = range(48)
COLORS = [i.RGB for i in Lego_return_tuple()]


im = Image.open('joker.jpg') 
rgb_im = im.convert("RGB")
resized_im = rgb_im.resize(size)
pix = resized_im.load()



def closest_color(rgb):
    """Function returns closest matching colour from a list of given colours"""
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

for x, y in itertools.product(tpl_x, tpl_y):
        pixel = closest_color(resized_im.getpixel((x, y)))
        pix[x, y] = pixel

resized_im.save("output.png")



def return_cubes():
    """Function returns a list with 9 cubes. Each cubes consits of 16x16 tuples with closest matching colour for each pixel from resized image"""
    CUBE_1 = []
    CUBE_2 = []
    CUBE_3 = []
    CUBE_4 = []
    CUBE_5 = []
    CUBE_6 = []
    CUBE_7 = []
    CUBE_8 = []
    CUBE_9 = []
    for x, y in itertools.product(tpl_x, tpl_y):
        pixel = closest_color(resized_im.getpixel((x, y)))
        pix[x, y] = pixel
        if (x, y) in itertools.product(range(16), range(16)):
            CUBE_1.append(pixel)
        elif (x, y) in itertools.product(range(16, 32), range(16)):
            CUBE_2.append(pixel)
        elif (x, y) in itertools.product(range(32, 48), range(16)):
            CUBE_3.append(pixel)
        elif (x, y) in itertools.product(range(16), range(16, 32)):
            CUBE_4.append(pixel)
        elif (x, y) in itertools.product(range(16, 32), range(16, 32)):
            CUBE_5.append(pixel)
        elif (x, y) in itertools.product(range(32, 48), range(16, 32)):
            CUBE_6.append(pixel)
        elif (x, y) in itertools.product(range(16), range(32, 48)):
            CUBE_7.append(pixel)
        elif (x, y) in itertools.product(range(16, 32), range(32, 48)):
            CUBE_8.append(pixel)
        elif (x, y) in itertools.product(range(32, 48), range(32, 48)):
            CUBE_9.append(pixel)
    return [CUBE_1, CUBE_2, CUBE_3, CUBE_4, CUBE_5, CUBE_6, CUBE_7, CUBE_8, CUBE_9]


def return_cube_total():
    """Function returns a list with 48x48 tuples with closest matching colour for each pixel from resized image"""
    CUBE_TOTAL = []
    for x, y in itertools.product(tpl_x, tpl_y):
        pixel = closest_color(resized_im.getpixel((x, y)))
        pix[x, y] = pixel
        CUBE_TOTAL.append(pixel)
    return CUBE_TOTAL



