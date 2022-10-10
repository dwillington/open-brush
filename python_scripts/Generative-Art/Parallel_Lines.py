from graphics.Geometry import Line
from graphics.Vector import Vector as vec2
from graphics.Helpers import map
import socket
import sys
sys.path.append("..")
import ob_helper
import random
import math

# Some variables
width, height = 1000, 1000

# Main function
def draw():

    connector_lines = []

    num_lines_x = 20
    num_lines_y = 3
    x_step = float((width-100) // num_lines_x)
    y_step = float(height // num_lines_y)
    x_offset = (x_step // 2) + 50
    y_offset = y_step // 2

    for h in range(num_lines_y):
        randomColor = format(random.randint(0,16777215),'x')
        ob_helper.sendCommands([f"color.set.html={randomColor}"])
        for i in range(num_lines_x):
            x = x_step * i + x_offset
            y = y_step * h + y_offset
            yy = random.randint(25, 125) # HEIGHT "SPACE" BETWEEN INDIVIDUAL LINES
            p0 = vec2([
                x + random.uniform(-(x_step//2)+10, (x_step//2)+10),
                random.uniform(y-50, y+50) + yy
            ])
            p1 = vec2([
                x + random.uniform(-(x_step//2)+10, (x_step//2)+10),
                random.uniform(y-50, y+50) - yy
            ])
            connector_lines.append(Line(p0[0], p0[1], p1[0], p1[1]))

            if i != 0:
                num_lines = 21
                l1 = i+num_lines_x*h
                l2 = (i+num_lines_x*h)+1

                while l2 == l1:
                    l2 = random.randint(0, len(connector_lines))

                for j in range(num_lines+1):
                    p0 = connector_lines[l1-1].get_lerp(math.pow(map(j, 0, num_lines, 0, 1), 1))
                    p1 = connector_lines[l2-1].get_lerp(math.pow(map(j, 0, num_lines, 0, 1), 1))
                    ob_helper.drawLineOB(p0,p1)


def main():
    hostname = socket.gethostname()
    if(hostname == "centos7.linuxvmimages.local"):
      ob_helper.ob_host="10.0.2.2"
    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,10,10"])

    # ob_helper.sendCommands(["brush.type=Light"])
    # ob_helper.sendCommands(["brush.size.set=.4"])

    # ob_helper.sendCommands(["brush.type=Icing"])
    # ob_helper.sendCommands(["brush.size.set=0.2"])

    # ob_helper.sendCommands(["brush.type=Electricity"])
    # ob_helper.sendCommands(["brush.size.set=.1"])

    draw()
    ob_helper.sendCommands(["debug.brush"])

# Call the main function
if __name__ == '__main__':
    main()
