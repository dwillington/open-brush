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
import math
import svg_path_transform as svg_path_transform
import svgutils
import svgpathtools as svgpathtools 

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
    ob.user.move.to("0,0,20")
    ob.color.set.html("4CCD99")
    ################################################################################
    # USE DRAW.TEXT IN HTTP API
    ################################################################################
    ob.draw.text(path.getAttribute('unicode'))

    ob.brush.move.to("0,20,0")
    ob.color.set.html("ff1493")

    ################################################################################
    # https://stackoverflow.com/questions/65850680/how-to-extract-the-cartesian-coordinates-x-y-of-an-svg-image
    # USE DRAW.TEXT IN HTTP API TO DRAW AN SVG PATH ONLY IN LINES
    ################################################################################
    d = path.getAttribute('d')
    parsed = parse_path(d)
    print('Path:', d, '\n' + '-' * 20)
    # print('Objects:\n', parsed, '\n' + '-' * 20)
    for obj in parsed:
      op = type(obj).__name__
      start = (round(obj.start.real, 3), round(obj.start.imag, 3))
      end = (round(obj.end.real, 3), round(obj.end.imag, 3))
      print(op, ', start/end coords:', start, end)
      # print(type(obj).__name__, ', start/end coords:', ((round(obj.start.real, 3), round(obj.start.imag, 3)), (round(obj.end.real, 3), round(obj.end.imag, 3))))

      if op == "Move":
        continue
      else:
        p0 = dpc_helper.get(start[0],start[1],0) # THESE ARE STRINGS
        p1 = dpc_helper.get(end[0],end[1],0)     # THESE ARE STRINGS
        p0_l = dpc_helper.get_as_list(p0)
        p1_l = dpc_helper.get_as_list(p1)
        if math.dist(p0_l,p1_l) == 0:
          continue
        elif dpc_helper.below_threshold(p0_l,p1_l,printout=True):
          True
        dp = f"[{p0}],[{p1}]"
        print(dp)
        ob.draw.path(dp)

    print('-' * 20)

    ################################################################################
    # USE DRAW.SVG IN HTTP API
    ################################################################################
    ob.color.set.html("blue")
    ob.draw.svg(d.replace(" ", "%20"))
    
    input("Press Enter to continue...")

    # return


svgDict = {}
def parseSVGs():
  doc = minidom.parse("LUCON.svg")
  for ipath, path in enumerate(doc.getElementsByTagName("glyph")):
    if path.hasAttribute('d') == False: continue
    u = path.getAttribute('unicode')
    d = path.getAttribute('d')
    svgDict[u] = d
    # if ipath > 10: return


def testDraw():
  parseSVGs()
  def getSvg(text):
    counter = 0.0
    for c in text:
      path = svgDict[c]
      print(path)
      path = svg_path_transform.parse_path(path)
      path = svg_path_transform.translate_and_scale(path, s=(0.05, 0.05))
      path = svg_path_transform.path_to_string(path)
      # path = ''.join(sum(path, []))
      print(path)
      ob.draw.svg(path.replace(" ", "%20"))
      counter += 0.5
      ob.brush.move.by(f"{counter},0,0")
      input("Press Enter to continue...")
      

  # text = svgutils.transform.TextElement(0,0,"hello")
  # text = text.tostr().decode("utf-8")
  # text = svgutils.transform.fromstring(text)
  # text = text.to_str().decode("utf-8")
  # print(text)
  # ob.draw.svg(text.replace(" ", "%20"))

  getSvg("hello")


def main():
  if "OB_HOST" in os.environ:
    ob.OB_HOST = os.environ['OB_HOST']
  ob.new()
  ob.brush.type("Light")
  ob.brush.size.set(0.01)
  ob.brush.move.to("0,0,0")
  ob.user.move.to("0,0,20")
  
  # parser = argparse.ArgumentParser()
  # parser.add_argument("--text", action="store_true")
  # args = parser.parse_args()
  # if args.text:
    # text()

  testDraw()
  # text()

if __name__ == '__main__':
    main()