from graphics.Geometry import Line
from graphics.Helpers import map
from graphics.Generators import NoiseLoop
import os
import socket
import sys
sys.path.append("..")
import ob_helper
import math
import random

width, height = 1000, 1000
num_layers = 16

# getDrawPathCoordinates
def getDPC(point):
  return f"{point.x/110},{point.y/110},0"

# lineA is current, lineB is previous
def drawMosiacPiece(lineA, lineB, layer):
  randomColor = format(random.randint(0,16777215),'x')
  ob_helper.sendCommands([f"color.set.html={randomColor}"])

  # UNCOMMENT IF USING NON HULL BRUSH
  # ob_helper.drawLineOB(lineA.p0,lineA.p1)
  # if lineB is not None: # DRAW THE CIRCLE AT THE FLOOR OF THE "MINUTE" HANDS ON THE CLOCK
    # ob_helper.drawLineOB(lineA.p0,lineB.p0)
    # if layer == (num_layers-1): # DRAW THE CIRCLE AT THE CEILING OF THE "MINUTE" HANDS ON THE CLOCK
        # ob_helper.drawLineOB(lineA.p1,lineB.p1)

  if lineB is not None:
    randomColor = format(random.randint(0,16777215),'x')
    ob_helper.sendCommands([f"color.set.html={randomColor}"])

    # draw.path=A,B,C,D gives flush surface vs draw.path=A,B,C which gives more interesting texture

    ob_helper.sendCommands([f"draw.path=[{getDPC(lineA.p0)}]," +
                            f"[{getDPC(lineB.p0)}]," + 
                            f"[{getDPC(lineB.p1)}]," +
                            f"[{getDPC(lineA.p1)}]," +
                            # f"[{getDPC(lineA.p0)}]" +
                            ""])

def draw():

    grid_x, grid_y = 1, 1
    x_step, y_step = width//grid_x, height//grid_y
    x_offset, y_offset = x_step//2, y_step//2

    n_loop = []
    offset = []
    s = (x_offset // num_layers)

    x0 = x_offset
    y0 = y_offset
    for xxx in range(grid_x):
        for yyy in range(grid_y):
            center_x = xxx * x_step + x_offset
            center_y = yyy * y_step + y_offset
            for layer in range(num_layers):
                offset = random.randint(0, 360)
                n_loop.append(NoiseLoop(map(layer, 0, num_layers, 1, 4), s*layer, s*layer+s))
                num_points = 360
                # for i in range(num_points):
                  # if layer > 5:
                    # r = n_loop[layer].get_value(i)
                    # x = r * math.cos(math.radians(i)) + center_x
                    # y = r * math.sin(math.radians(i)) + center_y
                    # line = Line(x0, y0, x, y)
                    # ob_helper.drawLineOB(line.p0,line.p1)
                    # x0=x
                    # y0=y
                      # Think of a better way to do this
                    # config.Context.line_to(x, y)
                # config.Context.close_path()
                # stroke()

                line0 = None
                line1 = None
                if layer != 0:
                    num_lines = map(layer, 0, num_layers, 16, 2)
                    num_points = 360 / num_lines
                    for i in range(int(num_points)):
                        r = n_loop[layer].get_value(i*num_lines+offset)
                        x = r * math.cos(math.radians(i*num_lines+offset)) + center_x
                        y = r * math.sin(math.radians(i*num_lines+offset)) + center_y

                        r = n_loop[layer-1].get_value(i*num_lines+offset)
                        xx = r * math.cos(math.radians(i*num_lines+offset)) + center_x
                        yy = r * math.sin(math.radians(i*num_lines+offset)) + center_y
                        line = Line(xx, yy, x, y)
                        
                        drawMosiacPiece(line, line0, layer)

                        if line0 is not None:
                          pass
                        else:
                          line1 = line
                        line0 = line

                    # OOOPS, ALMOST FORGOT ABOUT CONNECTING THE 11 HOUR TO THE 12 HOUR HAND, YOU SNEAKY BUGGER. line1 STORES THE "HOUR HAND" FIRST DRAWN IN THE LAYER
                    drawMosiacPiece(line, line1, layer)




def main():
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,10,10"])
    # ACHIEVE SHAPE FILL WITH brush.type ShinyHull MatteHull UnlitHull Diamond
    ob_helper.sendCommands(["brush.type=ShinyHull"])

    draw()
    ob_helper.sendCommands(["debug.brush"])

if __name__ == '__main__':
    main()
