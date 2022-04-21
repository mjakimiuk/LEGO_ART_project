import itertools
from collections import namedtuple
from math import sqrt

from fpdf import FPDF
from PIL import Image

# im = Image.open('joker.jpg')
# im = Image.open('pikachu.png')
im = Image.open("sponge.png")
rgb_im = im.convert("RGB")
size = (48, 48)
resized_im = rgb_im.resize(size)

# print(rgb_im.size)
# print(resized_im.size)
pix = resized_im.load()

tpl_x = range(48)
tpl_y = range(48)


Lego = namedtuple("LEGO", "LEGO_color RGB ID LEGO_part_number")
Lego_colours = [
    Lego("black", (0, 0, 0), 1, 614126),
    Lego("bright_green", (75, 159, 74), 2, 6109808),
    Lego("dark_orange", (169, 85, 0), 3, 6315782),
    Lego("dark_blue", (10, 52, 99), 4, 6021623),
    Lego("nougat", (208, 145, 104), 5, 6391270),
    Lego("red", (201, 26, 9), 6, 614121),
    Lego("reddish_brown", (88, 42, 18), 7, 4216581),
    Lego("blue", (0, 85, 191), 8, 614123),
    Lego("light_bluish_gray", (160, 165, 169), 9, 4211525),
    Lego("dark_bluish_gray", (108, 110, 104), 10, 4210633),
    Lego("pearl_dark_gray", (87, 88, 87), 11, 6038201),
    Lego("medium_azure", (54, 174, 191), 12, 6102986),
    Lego("white", (255, 255, 255), 13, 614101),
    Lego("aqua", (179, 215, 209), 14, 6382504),
    Lego("brick_yellow", (228, 205, 158), 15, 4161734),
    Lego("medium_lavender", (172, 120, 186), 16, 6133802),
]

COLORS = [i.RGB for i in Lego_colours]


def closest_color(rgb):
    r, g, b = rgb
    color_diffs = []
    for color in COLORS:
        cr, cg, cb = color
        color_diff = sqrt((r - cr) ** 2 + (g - cg) ** 2 + (b - cb) ** 2)
        color_diffs.append((color_diff, color))
    return min(color_diffs)[1]


CUBE_1 = []
CUBE_2 = []
CUBE_3 = []
CUBE_4 = []
CUBE_5 = []
CUBE_6 = []
CUBE_7 = []
CUBE_8 = []
CUBE_9 = []
CUBE_TOTAL = []

for x, y in itertools.product(tpl_x, tpl_y):
    pixel = closest_color(resized_im.getpixel((x, y)))
    pix[x, y] = pixel
    CUBE_TOTAL.append(pixel)
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
resized_im.save("output.png")


pdf = FPDF()
CUBES = [CUBE_1, CUBE_2, CUBE_3, CUBE_4, CUBE_5, CUBE_6, CUBE_7, CUBE_8, CUBE_9]

pdf.add_page()
line_grid_start_x = 66.5+6
line_grid_start_y = 66.5+6
line_endpoint = 208
grid_number = [str(i) for i in range(1,4)]
grid_letter = list('ABC')
pdf.line(line_grid_start_x-64, 2, line_grid_start_x-64, line_endpoint) # vertical line
pdf.line(line_grid_start_x, 2, line_grid_start_x, line_endpoint) # vertical line
pdf.line(line_grid_start_x+64, 2, line_grid_start_x+64, line_endpoint) # vertical line
pdf.line(line_grid_start_x+64*2, 2, line_grid_start_x+64*2, line_endpoint) # vertical line
pdf.line(2, line_grid_start_y-64, line_endpoint, line_grid_start_y-64) # horizontal line
pdf.line(2, line_grid_start_y, line_endpoint, line_grid_start_y) # horizontal line
pdf.line(2, line_grid_start_y+64, line_endpoint, line_grid_start_y+64) # horizontal line
pdf.line(2, line_grid_start_y+64*2, line_endpoint, line_grid_start_y+64*2) # horizontal line
for n, (i, text) in itertools.product(range(2), enumerate(grid_number)):
    pdf.set_font("helvetica", "B", 20)
    pdf.text(40+i*64,7+n*200,text)
for n, (i, text) in itertools.product(range(2), enumerate(grid_letter)):
    pdf.set_font("helvetica", "B", 20)
    pdf.text(2+n*200,40+i*64,text)
for row in range(48):
    line = CUBE_TOTAL[0 + row * 48 : 48 + row * 48]
    for q, (n, l) in itertools.product(Lego_colours, enumerate(line)):
        if q.RGB == l:
            if q.RGB == (0, 0, 0):
                pdf.set_text_color(r=255, g=255, b=255)
            else:
                pdf.set_text_color(r=0, g=0, b=0)
            R, G, B = q.RGB
            pdf.set_fill_color(r=R, g=G, b=B)
            pdf.ellipse(y=9 + n * 4, x=9 + row * 4, w=3, h=3, style="FD")
            pdf.set_font("helvetica", "B", 6)
            if q.ID < 10:
                pdf.text(9.9 + row * 4, 11.2 + n * 4, f"{q.ID}")
            else:
                pdf.text(9.2 + row * 4, 11.2 + n * 4, f"{q.ID}")

for cube in CUBES:
    # pdf.set_line_width(1)
    pdf.add_page()
    for row in range(16):
        line = cube[0 + row * 16 : 16 + row * 16]
        for q, (n, l) in itertools.product(Lego_colours, enumerate(line)):
            if q.RGB == l:
                if q.RGB == (0, 0, 0):
                    pdf.set_text_color(r=255, g=255, b=255)
                else:
                    pdf.set_text_color(r=0, g=0, b=0)
                R, G, B = q.RGB
                pdf.set_fill_color(r=R, g=G, b=B)
                pdf.ellipse(y=10 + n * 12, x=10 + row * 12, w=10, h=10, style="FD")
                pdf.set_font("helvetica", "B", 18)
                if q.ID < 10:
                    pdf.text(13.5 + row * 12, 17.5 + n * 12, f"{q.ID}")
                else:
                    pdf.text(11 + row * 12, 17 + n * 12, f"{q.ID}")


pdf.output("output.pdf")
