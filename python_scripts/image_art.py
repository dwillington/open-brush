# PATH=/c/tools/python-3.11.0rc2-embed-amd64:$PATH
import os
from ob import ob
import argparse
import urllib
import random
from PIL import Image
import socket   
import ob_helper
import imageio
import matplotlib
import sys


def drawMindMap():
  ob_helper.sendCommands(["user.move.to=0,0,20"])
  START_X = -15
  START_Y = 22
  START_Z = 0
  commandStrings = []
  mind_map_ideas = [
    "Mind Map in OB", 
    "more powerful scripting: explore Python or Node/JavaScript?", 
    "Understanding RGB and Colors for iteration",
    "Crossword Puzzle in OB anyone?",
    "Word Search Puzzles in OB anyone?",
    "Sudoku in OB anyone?",
    ]
  ob.brush.move.to(f"{str(START_X)},{str((START_Y - (i*2)))},{str(START_Z)}")
  for i in range(0, len(mind_map_ideas)):
    text = urllib.parse.quote_plus(mind_map_ideas[i])
    print(text)
    # randomColor = str(hex(random.randint(0,16777215)))
    randomColor = format(random.randint(0,16777215),'x')
    ob.color.set.html(randomColor)
    ob.draw.text(text)

# def rgb_to_hex(r, g, b):
  # return ('{:X}{:X}{:X}').format(r, g, b)

def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb

########################################
# 
########################################
def drawImage(img_filename):
  START_X = -2
  START_Y = 17.5
  START_Z = 0

  # CANVAS_SIZE = 10; ob_helper.sendCommands(["user.move.to=1.8,-2,2"])
  CANVAS_SIZE = 50; ob_helper.sendCommands(["user.move.to=0,0,5"])

  # img_filename = "../scripts/images/red.jpg"
  im = Image.open(img_filename)
  im = im.resize((CANVAS_SIZE, CANVAS_SIZE))
  rgb_im = im.convert('RGB')

  commandStrings = []
  for x in range(CANVAS_SIZE):
    for y in range(CANVAS_SIZE):
      r, g, b = rgb_im.getpixel((x, y))
      if not (r == 0 and g == 0 and b == 0): # skip drawing black
        # print(r, g, b)
        rgbToHex = rgb_to_hex((r, g, b))
        # print(rgbToHex)
        commandStrings.append("brush.move.to=" + str((START_X + (x/10))) + "," + str((START_Y - (y/10))) + "," + str(START_Z) + 
          "&color.set.html=" + str(rgbToHex) + "&brush.draw=0.1");
    ob_helper.sendCommands(commandStrings)
    commandStrings = []
  ob_helper.sendCommands(["debug.brush"])

########################################
# 
########################################
def drawRandomPath():
  START_X = 0
  START_Y = 0
  START_Z = 0
  ob_helper.sendCommands(["user.move.to=-3,10,10"])

  commandStrings = []
  MAX_XY = 10
  x0 = round(random.uniform(0, MAX_XY),2)
  y0 = round(random.uniform(0, MAX_XY),2)
  z0 = round(random.uniform(0, MAX_XY),2)
  z0 = 0
  cs = "draw.path=[0,0,0]"
  for i in range(30):
    x = round(random.uniform(0, MAX_XY),2);
    y = round(random.uniform(0, MAX_XY),2)
    z = round(random.uniform(0, MAX_XY),2)
    z = 0
    randomColor = format(random.randint(0,16777215),'x')
    commandStrings.append("color.set.html=" + randomColor + "&draw.path=["+str(x0)+","+str(y0)+","+str(z0)+"],["+str(x)+","+str(y)+","+str(z)+"]")
    ob_helper.sendCommands(commandStrings); commandStrings = []
    # input("Press Enter to continue...")
    # cs += ",["+str(x0)+","+str(y0)+","+str(z0)+"]"
    # x0=x; y0=y; z0=z

  ob_helper.sendCommands([cs])


def pipa():
  poem = [
    "See the Turtle of enormous girth!",
    "On his shell he holds the earth,",
    "His though is slow but always kind,",
    "He holds us all within his mind."
  ]
  
  y = 14
  ob.brush.move.to(f"0,{y},10")
  ob.model.import_("animal_turtle_loggerhead_sea_turtle.glb")
  y = 20
  for i in range(len(poem)):
    verse = urllib.parse.quote_plus(poem[i])

    print(verse)
    v = len(verse)
    x = -v/2
    y = y - 2
    ob.brush.move.to(f"{x},{y},24")
    ob.draw.text(verse)


def main():
  if "OB_HOST" in os.environ:
    ob.OB_HOST = os.environ['OB_HOST']
  ob.new()
  ob.brush.type("Light")

  START_X = -15
  START_Y = 22
  START_Z = 0

  hostname = socket.gethostname()
  if(hostname == "centos7.linuxvmimages.local"):
    ob_helper.ob_host="10.0.2.2"

  parser = argparse.ArgumentParser()
  parser.add_argument("--drawImage")
  parser.add_argument("--drawRandomPath", action="store_true")
  parser.add_argument("--drawMindMap", action="store_true")
  parser.add_argument("--pipa", action="store_true")

  args = parser.parse_args()
  # print(args)
  if args.drawImage is not None:
    drawImage(args.drawImage)
  elif args.drawRandomPath:
    drawRandomPath()
  elif args.drawMindMap:
    drawMindMap()
  elif args.pipa:
    pipa()

  return


if __name__ == '__main__':
    main()


# sendCommands(["http://127.0.0.1:40074/api/v1?draw.text=a"]);


# python3 -m virtualenv env

