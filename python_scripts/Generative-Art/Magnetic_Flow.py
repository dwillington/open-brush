from graphics.Geometry import Line
import os
import socket
import sys
sys.path.append("..")
import ob_helper
import math
import random

# Some variables
height, width = 1000, 1000
grid_size = 100
border, mag_border = 50, 450
step_x, step_y = (width//grid_size), (height//grid_size)
EDGE_LIMIT_MODIFIER = 2 # HAS A BEARING ON THE LENGTH OF "LINES" COMING OUT THE CIRCLE, LARGER MEANS LARGER "LINES", TRY INCREMENTING THIS VALUE BY 1, AT A TIME
EDGE_LIMIT = 200 + EDGE_LIMIT_MODIFIER
PARTICLE_SIGNATURE_SIZE = 1.02 # MULTIPLIER ON THE LENGTH OF INDIVIDUAL SEGMENTS OF "LINES" COMING OUT THE CIRCLE
START_NUM = 182 # CONTROLS HOW MANY "LINES" SHOOTING OUT THE CIRCLE

# Particle class
class Particle:
    def __init__(self, x, y, vel_x, vel_y):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.frc_x = 0
        self.frc_y = 0
        self.lx, self.ly = self.x, self.y
        self.draw_stroke = True

    def update(self):

        self.x = self.x + self.frc_x
        self.y = self.y + self.frc_y

        self.vel_x = self.vel_x * 0.9
        self.vel_y = self.vel_y * 0.9

        self.x = self.x + self.vel_x
        self.y = self.y + self.vel_y

    def edges(self):
        if self.x <= EDGE_LIMIT or self.x >= width-EDGE_LIMIT or self.y <= EDGE_LIMIT or self.y >= height-EDGE_LIMIT:
            self.draw_stroke = False
        else:
            self.draw_stroke = True

    def reset_force(self):
        self.frc_x = 0
        self.frc_y = 0

    def set_force(self, fx, fy):
        self.frc_x = self.frc_x + fx
        self.frc_y = self.frc_y + fy

    def set_last_pos(self):
        self.lx, self.ly = self.x, self.y

    def calculate_force(self, mx, my, mp):
        dy = mx - self.x
        dx = my - self.y
        angle = math.atan2(dy, dx) * mp
        sx = math.sin(angle)
        sy = math.cos(angle)
        return [sx, sy]

    def draw(self):
        if self.draw_stroke is not False:
            line = Line(self.lx, self.ly, self.x, self.y)
            ob_helper.drawLineOB([self.x,self.y],[self.lx*PARTICLE_SIGNATURE_SIZE,self.ly*PARTICLE_SIGNATURE_SIZE])
            # ob_helper.drawLineOB([self.x,self.y],[self.lx,self.ly], 80)


# Magnet Class
class magnet:
    def __init__(self, x, y, pole):
        self.x = x
        self.y = y
        self.p = pole


def draw():

    magnets = []
    my_particles = []
    # num_magnets = random.randint(2, 8)
    num_magnets = random.randint(1, 2)
    sum_x, sum_y = 0, 0
    sums = 0

    print("Number of Magnets: " + str(num_magnets))

    for m in range(num_magnets):
        pole = 1
        if random.uniform(0, 1) < 0.5:
            pole = -1

        magnets.append(magnet(
                random.randint(100, width-100),
                random.randint(100, height-100),
                pole
        ))

    a = (math.pi*2)/START_NUM

    for x in range(100, width-100, (width-200)//1):
        for y in range(100, height-100, (height-200)//1):
            for i in range(START_NUM):
                xx = x + (math.sin(a*i)*250) + ((width-200)//2)
                yy = y + (math.cos(a*i)*250) + ((height-200)//2)
                vx = random.uniform(-1, 1)*0.5
                vy = random.uniform(-1, 1)*0.5
                my_particles.append(Particle(xx, yy, vx, vy))

    for p in my_particles:
        randomColor = format(random.randint(0,16777215),'x')
        ob_helper.sendCommands([f"color.set.html={randomColor}"])
        for t in range(100):
            for m in magnets:
                sums = p.calculate_force(m.x, m.y, m.p*4)
                sum_x = sum_x + sums[0]
                sum_y = sum_y + sums[1]

            sum_x = sum_x / len(magnets)
            sum_y = sum_y / len(magnets)

            p.reset_force()
            p.set_force(sum_x, sum_y)
            p.update()
            p.edges()
            if t % 8 == 0:
                p.draw()
                p.set_last_pos()


def main():
    hostname = socket.gethostname()
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,10,10"])
    
    ob_helper.sendCommands(["brush.type=Icing"])
    ob_helper.sendCommands(["brush.size.set=0.2"])

    draw()
    ob_helper.sendCommands(["debug.brush"])

if __name__ == '__main__':
    main()
