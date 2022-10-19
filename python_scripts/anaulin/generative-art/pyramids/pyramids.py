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
    cols = colors.shades(color, 5)
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

    # I DON'T QUITE HAVE SHADING RIGHT, I DON'T UNDERSTAND THESE VALUES BEING BETWEEN 0 AND 1
    while True:
      for i in range(3):
        if color[i] < 0.1:
          print(color)
          color_list = list(color)
          color_list[i] = color_list[i]*10
          color = tuple(color_list)
      if color[0] >= 0.1 and color[1] >= 0.1 and color[2] >= 0.1:
        break
    
    # I THINK THIS IS THE RIGHT THING TO DO, I WILL NOTE THAT COLORS SEEM TO APPEAR IN THE RIGHT ORDER OF SHADING, I.E. STARTING FROM BOTTOM FACE, ROTATING COUNTER CLOCKWISE FROM LIGHT TO DARK
    randomColor = ob_helper.rgb_to_hex(round(color[0]*255), round(color[1]*255), round(color[2]*255))


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
            pyramid(ctx, x, y, img_width // columns, img_height // rows, palettes.hex_to_tuple(random.choice(palette['colors'])))

def make_random(filename="output.png", p=random.choice(palettes.PALETTES), img_width=1000, img_height=1000):
    MAX_SQUARES = 10
    c = random.randint(5, MAX_SQUARES)
    r = random.randint(5, MAX_SQUARES) if random.random() < 0.5 else c
    if img_width != img_height:
        img_width = img_height = max(img_width, img_height)
    # print(filename, c, r, p, img_width, img_height)
    main(filename=filename.format(1), palette=p, columns=c, rows=r, img_height=img_height, img_width=img_width)

if __name__ == "__main__":
    for idx in range(1):
        make_random(filename="output-{}.png".format(idx))
