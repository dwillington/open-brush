import os
import sys
sys.path.append("../")
import ob_helper
from ob import ob
import argparse
from xml.dom import minidom
from svg.path import parse_path
import urllib
import re


def letters():

  ob.color.set.html("blue")

  def drawL():
    ob.color.set.html("red")
    ob.draw.path(f"[0,0,0],[{U},0,0]")
    ob.draw.path(f"[0,0,0],[0,{U},0]")
    ob.color.set.html("blue")

  U = 1.0

  letters = {
    "A": [
      [[0, 0, 0], [0.25 * U, 1 * U, 0]],
      [[0, 0.5 * U, 0], [0.5 * U, 0.5 * U, 0]],
      [[0.5 * U, 0, 0], [0.25 * U, 1 * U, 0]],
    ],
    "B": [
      [[0, 0, 0], [0, 1 * U, 0]],
      [[0, 1 * U, 0], [0.5 * U, 1 * U, 0]],
      [[0.5 * U, 1 * U, 0], [0.5 * U, 0.5 * U, 0]],
      [[0, 0.5 * U, 0], [0.5 * U, 0.5 * U, 0]],
      [[0.5 * U, 0.5 * U, 0], [0.5 * U, 0, 0]],
      [[0.5 * U, 0, 0], [0, 0, 0]],
    ],
    "C": [
      # Top curve of "C"
      [[0.7 * U, 0.7 * U, 0], [0.5 * U, 1 * U, 0]],
      [[0.5 * U, 1 * U, 0], [0, 1 * U, 0]],
      # Vertical line of "C"
      [[0, 1 * U, 0], [0, 0 * U, 0]],
      [[0, 0 * U, 0], [0.7 * U, 0 * U, 0]],
    ],
    "D": [
      # Left vertical line of "D"
      [[0, 0, 0], [0, 1 * U, 0]],
      # Top curve of "D"
      [[0, 1 * U, 0], [0.4 * U, 1 * U, 0]],
      [[0.4 * U, 1 * U, 0], [0.6 * U, 0.8 * U, 0]],
      [[0.6 * U, 0.8 * U, 0], [0.6 * U, 0.2 * U, 0]],
      [[0.6 * U, 0.2 * U, 0], [0.4 * U, 0 * U, 0]],
      [[0.4 * U, 0 * U, 0], [0 * U, 0 * U, 0]],
    ]
  }

  x = 0
  ob.new()
  ob.user.move.to("-7,10,10")

  for i in letters:
    ob.brush.move.to(f"{x},0,0")
    drawL()
    letter = letters.get(i)
    if True:
      path = str(letter).replace(" ", "")
      path = path[1:-1]
      ob.draw.paths(path)
    else:
      for i in range(len(letter_b)):
        p = letter[i]
        path = str(p).replace(" ", "")
        ob.draw.paths(path)
    x += U


dpc_helper = ob_helper.DPC(0.0005,0,0,0)
# dpc_helper = ob_helper.DPC(0.001,0,0,0)

def text():
  doc = minidom.parse("LUCON.svg")
  # doc = minidom.parse("/mnt/c/Users/dwill/Downloads/to-delete/fonts/NotoSansZanabazarSquare-Regular.svg")
  # doc = minidom.parse("Aldrich-Regular/Aldrich-Regular.svg")
  glyphs = [path.getAttribute('d') for path in doc.getElementsByTagName('glyph')]
  
  # for g in glyphs:
  for ipath, path in enumerate(doc.getElementsByTagName("glyph")):
    if path.hasAttribute('d') == False: continue

    print('glyph-name:', path.getAttribute('glyph-name'))
    ob.new()
    ob.user.move.to("5,0,20")
    ob.color.set.html("4CCD99")
    ob.draw.text(path.getAttribute('unicode'))
    ob.brush.move.to("0,20,0")
    ob.color.set.html("ff1493")
    # ob.draw.text("Hello")

    # https://stackoverflow.com/questions/65850680/how-to-extract-the-cartesian-coordinates-x-y-of-an-svg-image
    d = path.getAttribute('d')
    parsed = parse_path(d)
    print('Objects:\n', parsed, '\n' + '-' * 20)
    for obj in parsed:
      op = type(obj).__name__
      start = (round(obj.start.real, 3), round(obj.start.imag, 3))
      end = (round(obj.end.real, 3), round(obj.end.imag, 3))
      print(op, ', start/end coords:', start, end)
      # print(type(obj).__name__, ', start/end coords:', ((round(obj.start.real, 3), round(obj.start.imag, 3)), (round(obj.end.real, 3), round(obj.end.imag, 3))))

      if op == "Move":
        continue
        # ob.brush.move.to(f"{start[0]},{start[1]},0")
      # elif op == "Line":
      else:
        ob.draw.path(f"[{dpc_helper.get(start[0],start[1],0)}],[{dpc_helper.get(end[0],end[1],0)}]")

    print('-' * 20)

    # ob.brush.type("Light")
    # ob.brush.size.set(1)
    # ob.brush.move.to("0,0,0")
    ob.color.set.html("blue")
    ob.draw.svg(d.replace(" ", "%20"))
    
    input("Press Enter to continue...")

    # return


def main():
  if "OB_HOST" in os.environ:
    ob.OB_HOST = os.environ['OB_HOST']
  ob.brush.type("Light")
  ob.brush.move.to("0,0,0")
  
  # parser = argparse.ArgumentParser()
  # parser.add_argument("--text", action="store_true")
  # args = parser.parse_args()
  # if args.text:
    # text()

  text()

if __name__ == '__main__':
    main()
