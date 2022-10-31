import cairo
import math
import random

import sys
import os
sys.path.append(os.path.abspath('..'))
from lib import palettes
from lib import colors

import socket
sys.path.append(os.path.abspath('../../../'))
import ob_helper

def pyramid(ctx, x, y, width, height, color, random_center=True):
    if random_center:
        center = ( random.randint(x + 3, x + width - 3), random.randint(y + 3, y + height - 3))
    else:
        center = (x + width // 2, y + height // 2)
    tl = (x, y)
    tr = (x + width, y)
    bl = (x, y + height)
    br = (x + width, y + height)
    color=color.replace("#", "")
    # print(color)

   # https://stackoverflow.com/questions/1787124/programmatically-darken-a-hex-colour
    DARKEN_FACTOR = 0xfefefe
    cols = []
    colorI=int(color, 16)
    cols.append(colorI)
    colorI=(colorI & DARKEN_FACTOR) >> 1
    cols.append(colorI)
    colorI=(colorI & DARKEN_FACTOR) >> 1
    cols.append(colorI)
    colorI=(colorI & DARKEN_FACTOR) >> 1
    cols.append(colorI)

    triangle(ctx, tl, tr, center, cols[0])
    triangle(ctx, tr, br, center, cols[1])
    triangle(ctx, br, bl, center, cols[2])
    triangle(ctx, bl, tl, center, cols[3])

def getDPC(point,Z=0):
  SCALER = 100
  return f"{point[0]/SCALER},{point[1]/SCALER},{Z}"

def triangle(ctx, p1, p2, p3, color):

    # ob_helper.drawLineOB(p1,p2)
    # ob_helper.drawLineOB(p2,p3)
    # ob_helper.drawLineOB(p3,p1)

    randomColor = f"{color:x}" # CONVERT TO HEX STRING

    ob_helper.sendCommands([f"color.set.html={randomColor}"])
    ob_helper.sendCommands([f"draw.path=[{getDPC(p1)}]," + 
      f"[{getDPC(p2)}]," + 
      f"[{getDPC(p3)}]"])


def main(filename="output.png", img_width=1000, img_height=1000, palette=random.choice(palettes.PALETTES), columns=15, rows=10):
    hostname = socket.gethostname()
    if(hostname == "centos7.linuxvmimages.local"):
      ob_helper.ob_host="10.0.2.2"
    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,8,15"])
    ob_helper.sendCommands(["brush.type=UnlitHull"])
    ctx = None

    for x in range(0, img_width, img_width // columns):
        for y in range(0, img_height, img_height // rows):
            # pyramid(ctx, x, y, img_width // columns, img_height // rows, palettes.hex_to_tuple(random.choice(palette['colors'])))
            pyramid(ctx, x, y, img_width // columns, img_height // rows, random.choice(palette['colors']))

def make_random(filename="output.png", p=random.choice(palettes.PALETTES), img_width=1000, img_height=1000):
    MAX_SQUARES = 5
    c = random.randint(5, MAX_SQUARES)
    r = random.randint(5, MAX_SQUARES) if random.random() < 0.5 else c
    if img_width != img_height:
        img_width = img_height = max(img_width, img_height)
    # print(filename, c, r, p, img_width, img_height)
    main(filename=filename.format(1), palette=p, columns=c, rows=r, img_height=img_height, img_width=img_width)

if __name__ == "__main__":
    for idx in range(1):
        make_random(filename="output-{}.png".format(idx))
