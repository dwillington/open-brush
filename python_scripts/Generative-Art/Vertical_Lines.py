from graphics.Geometry import Line as draw_line
from graphics.Vector import Vector as vec2
import math
import random
import numpy as np
import os
import socket
import sys
sys.path.append("..")
import ob_helper

# Some variables
width, height = 1000, 1000


class Line:
    def __init__(self, p0, dir, id):
        self.id = id
        self.p0 = p0
        self.p1 = p0
        self.dir = dir
        self.intersect = vec2([0.0, 0.0])
        self.count = 0

    def draw(self):
        ob_helper.drawLineOB(self.p0,self.p1)

    def extend_line(self):
        self.p1 = self.p1 + self.dir

    def change_dir(self):
        self.count = self.count + 1

        if self.count % 40 == 0:
            angle = math.radians(random.randint(45, 135))
            dir = vec2([math.sin(angle), math.cos(angle)])
            self.dir = dir
            return True
        else:
            return False

    def edges(self):
        if self.p1[0] >= width or self.p1[0] < 0 or \
                self.p1[1] < 0 or self.p1[1] >= height-50:
            return True

    def line_intersect(self, p2, p3):
        A1 = self.p1[1] - self.p0[1]
        B1 = self.p0[0] - self.p1[0]
        C1 = A1 * self.p0[0] + B1 * self.p0[1]
        A2 = p3[1] - p2[1]
        B2 = p2[0] - p3[0]
        C2 = A2 * p2[0] + B2 * p2[1]
        denom = A1 * B2 - A2 * B1

        if denom == 0:
            return False

        intersect_x = (B2 * C1 - B1 * C2) / denom
        intersect_y = (A1 * C2 - A2 * C1) / denom

        rx0 = (intersect_x - self.p0[0]) / (self.p1[0] - self.p0[0])
        ry0 = (intersect_y - self.p0[1]) / (self.p1[1] - self.p0[1])
        rx1 = (intersect_x - p2[0]) / (p3[0] - p2[0])
        ry1 = (intersect_y - p2[1]) / (p3[1] - p2[1])

        if(((rx0 >= 0 and rx0 <= 1) or (ry0 >= 0 and ry0 <= 1)) and \
                ((rx1 >= 0 and rx1 <= 1) or (ry1 >= 0 and ry1 <= 1))):
            self.intersect = vec2([intersect_x, intersect_y])
            return True
        else:
            return False

    def get_intersect(self):
        return self.intersect

    def get_closest_point(self, p):
        a = np.linalg.norm(self.p0-p)
        b = np.linalg.norm(self.p1-p)

        if a <= b:
            self.p0 = p
        else:
            self.p1 = p


def get_direction():
    num_angles = 2
    r = int(random.uniform(0, num_angles))
    angle_step = [0, 45]

    for i in range(num_angles):
        if i == r:
            angle = math.radians(angle_step[i])

    dirs = vec2([math.sin(angle), math.cos(angle)])
    return dirs

Y_OFFSET = 0
SCALER = .01
def getDPC(point, Z=0):
    return f"{round(point[0]*SCALER,2)},{round((point[1]*SCALER)+Y_OFFSET,2)},{Z}"

def draw_walkers(walkers):
    draw_path = ""
    for walker in walkers:
      draw_path += f"[{getDPC(walker.p0)}],"
      # draw_path += f"[{getDPC(walker.p0)}],[{getDPC(walker.p1)}],"

    draw_path += f"[{getDPC(walkers[-1].p1)}],"
    ob_helper.sendCommands([f"draw.path={draw_path}"])


def draw():

    MIN_WALKERS = 20
    num_walkers = random.randint(MIN_WALKERS, MIN_WALKERS*2)
    # num_walkers = random.randint(100, 200)
    walkers = []
    x_step = float((width-100)) / num_walkers
    amt = random.uniform(0.075, 0.15)
    amt_step = random.randint(15, 80)
    start_dist = random.randint(10, 150)

    index = 0
    count = 0
    walker_count = 0
    for i in range(num_walkers):
        x = float((x_step * i) + 50.0)
        pos = vec2([float(x), float(50.0)])
        angle = math.radians(0)
        dirs = vec2([math.sin(angle), math.cos(angle)])
        walkers.append(Line(pos, dirs, i))

        walk = True
        while walk:
            if count % amt_step == 0:
                r = random.uniform(0, 1)
                if r < amt and walkers[index].p0[1] > start_dist:
                    dirs = get_direction()
                    walkers.append(Line(walkers[index].p1, dirs, i))
                    index = index + 1
                else:
                    angle = math.radians(0)
                    dirs = vec2([math.sin(angle), math.cos(angle)])
                    walkers.append(Line(walkers[index].p1, dirs, i))
                    index = index + 1

            walkers[index].extend_line()

            hit_line = False
            for w in walkers:
                if walkers[index].id != w.id:
                    intersect = walkers[index].line_intersect(w.p0, w.p1)
                    if intersect:
                        hit_line = True

            hit_edge = walkers[index].edges()
            if hit_edge or hit_line:
                walk = False

            count = count + 1
        index = index + 1

        ############################################################
        # DRAW NEWEST WALKER
        ############################################################
        randomColor = format(random.randint(0,16777215),'x')
        ob_helper.sendCommands([f"color.set.html={randomColor}"])
        draw_walkers(walkers[walker_count:])
        walker_count = len(walkers) # SET THE COUNTER AHEAD

    # for walker in walkers:
        # walker.draw()
        # input("Press Enter to continue...")



def main():
    hostname = socket.gethostname()
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,10,10"])

    ob_helper.sendCommands(["brush.type=Light"])
    ob_helper.sendCommands(["brush.size.set=.1"])

    draw()
    ob_helper.sendCommands(["debug.brush"])

# Call the main function
if __name__ == '__main__':
    main()

