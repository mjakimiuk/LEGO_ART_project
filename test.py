import itertools
from PIL import Image
from math import sqrt
from collections import namedtuple

im = Image.open('joker.jpg')
rgb_im = im.convert('RGB')
size = (64,64)
# rgb_im.resize(size).save('alive_parrot.png')
resized_im=rgb_im.resize(size)

print(rgb_im.size)
print(resized_im.size)
pix = resized_im.load()

tpl_x = range(64)
tpl_y = range(64)


Lego = namedtuple('LEGO', "LEGO_color RGB ID LEGO_part_number")
Lego_colours = [Lego('black',(0,0,0),1,614126),
           Lego('bright_green',(75,159,74),2,6109808),
           Lego('dark_orange',(169,85,0),3,6315782),
           Lego('dark_blue',(10,52,99),4,6021623),
           Lego('nougat',(208,145,104),5,6391270),
           Lego('red',(201,26,9),6,614121),
           Lego('reddish_brown',(88,42,18),7,4216581),
           Lego('blue',(0,85,191),8,614123),
           Lego('light_bluish_gray',(160,165,169),9,4211525),
           Lego('dark_bluish_gray',(108,110,104),10,4210633),
           Lego('pearl_dark_gray',(87,88,87),11,6038201),
           Lego('medium_azure',(54,174,191),12,6102986),
           Lego('white',(255,255,255),13,614101),
           Lego('aqua',(179,215,209),14,6382504),
           Lego('brick_yellow',(228,205,158),15,4161734),
           Lego('medium_lavender',(172,120,186),16,6133802)
]

COLORS = [i.RGB for i in Lego_colours]
print(COLORS)
def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr)**2 + (g - cg)**2 + (b - cb)**2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]

for x, y in itertools.product(tpl_x, tpl_y):
    print(x,y)
    print(closest_color(resized_im.getpixel((x, y))))
    pix[x,y] = closest_color(resized_im.getpixel((x, y)))
    
resized_im.save('output.png')