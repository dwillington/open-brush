from graphics.Geometry import Line
from graphics.Vector import Vector as vec2
from graphics.Helpers import map
import os
import sys
sys.path.append("..")  # Add parent directory to Python path
from ob import ob
import random
import math

# Some variables
width, height = 1000, 1000
COORDINATE_SCALE = 0.01  # Scale factor for coordinates

# Main function
def draw():

    border = 50
    border_sQ = border*2
    num_lines = 8
    y_step = float((height-border_sQ)/num_lines)
    x_step = float((width-border_sQ)/num_lines)
    y_offset = y_step/2.0
    x_offset = x_step/2.0
    un_offset = 10
    my_lines = []

    for i in range(num_lines):
        for j in range(num_lines-1):
            if j == 0:
                p1 = vec2([
                    x_step*j+x_offset + random.uniform(-x_offset, x_offset) + border,
                    y_step*i+y_offset + random.uniform(-y_offset, y_offset) + border
                ])
                p2 = vec2([
                    x_step*(j+1)+x_offset + random.uniform(-x_offset, x_offset) + border,
                    y_step*i+y_offset + random.uniform(-y_offset, y_offset) + border
                ])
                my_lines.append(Line(p1[0], p1[1], p2[0], p2[1]))
            else:
                p1 = vec2([
                    my_lines[(j+(num_lines-1)*i)-1].p1[0],
                    my_lines[(j+(num_lines-1)*i)-1].p1[1]
                ])
                p2 = vec2([
                    x_step*(j+1)+x_offset + random.uniform(-x_offset, x_offset) + border,
                    y_step*i+y_offset + random.uniform(-y_offset, y_offset) + border
                ])
                my_lines.append(Line(p1[0], p1[1], p2[0], p2[1]))

    index = 0
    for i in range(num_lines):
        index = index + 1
        for j in range(num_lines-1):
            if i != 0:
                lerp_lines = int(map(i, 0, num_lines, 1, 12))+1
                for k in range(lerp_lines):
                    p0 = my_lines[(j+(num_lines-1)*(i-1))].get_lerp(math.pow(map(k, 0, lerp_lines-1, 0, 1), 1))
                    p1 = my_lines[(j+(num_lines-1)*i)].get_lerp(math.pow(map(k, 0, lerp_lines-1, 0, 1), 1))
                    ob.draw.path(f"[{p0[0]*COORDINATE_SCALE},{p0[1]*COORDINATE_SCALE},0],[{p1[0]*COORDINATE_SCALE},{p1[1]*COORDINATE_SCALE},0]")

    # CHANGE COLOR FOR LERP LINES (THE INNER BORDERS)
    randomColor = format(random.randint(0,16777215),'x')
    ob.color.set.html(randomColor)
    for line in my_lines:
        ob.draw.path(f"[{line.p0[0]*COORDINATE_SCALE},{line.p0[1]*COORDINATE_SCALE},0],[{line.p1[0]*COORDINATE_SCALE},{line.p1[1]*COORDINATE_SCALE},0]")

"""
  curl -v "http://10.0.2.2:40074/api/v1?new"
  curl -v "http://10.0.2.2:40074/api/v1?user.move.to=5,10,10"
  curl -v "http://10.0.2.2:40074/api/v1?brush.size.set=0.5"
  curl -v "http://10.0.2.2:40074/api/v1?brush.type=Icing"

randomColor="$(openssl rand -hex 3)"; curl -v "http://10.0.2.2:40074/api/v1?color.set.html=$randomColor"
"""
def main():
    if "OB_HOST" in os.environ:
        ob.OB_HOST = os.environ['OB_HOST']

    ob.new()
    ob.brush.move.to("0,0,0")
    ob.user.move.to("-5,10,10")

    # ob.brush.type("Icing")
    # ob.brush.size.set(0.4)

    # ob.brush.type("NeonPulse")
    # ob.brush.size.set(1)

    ob.brush.type("Light")
    ob.brush.size.set(.4)

    # ob.brush.type("Electricity")
    # ob.brush.size.set(.1)

    draw()
    ob.debug.brush()

# Call the main function
if __name__ == '__main__':
    main()
