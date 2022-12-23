# https://py.processing.org/reference/noiseDetail.html
# https://github.com/salaxieb/perlin_noise
from perlin_noise import PerlinNoise
from graphics.Vector import Vector as vec2
from graphics.Helpers import map
import os
import socket
import sys
sys.path.append("..")
import ob_helper
import random
import math

######################
## General Settings ##
######################
width = 1000
height = 1000
pencolor = "White"
    
###########################
## Perlin Noise Settings ##
##    mess with these    ##
###########################
seeded = False  ## Set to true to use seeds for consistant noise
colored = True  ## False for b/w, True for set color selection
blended = False  ## True adds transparancy and blend effect
manipulateAngle = False  ## True will drastically change effect

sca = 0.02          #  noise scalar
mapMin = 0          # minimum y-axis deviation
mapMax = 100        # maximum y-axis deviation
noise_detail = 0.1  # noise detail
noise_seed = 2      # noise seed if seeding
minRadius = 0       # arc inner radius
maxRadius = 700     # arc outer radius
minAngle = 0        # arc start angle
maxAngle = 360      # arc stop angle
radiusStep = 10     # arc density
angleStep = 2       # rotational steps

#################################
## Colors (if colored == true) ##
#################################
pencolor1 = "Crimson"
pencolor2 = "Chartreuse"
pencolor3 = "Black"
rules = [7, 11]  # divisor rules to color noise

##########
## MAIN ##
##########
START_X=5
START_Y=7

def stroke(color):
  ob_helper.sendCommands([f"color.set.html={color}"])

def point(x,y):
  ob_helper.sendCommands([f"brush.move.to={(x/100)+START_X},{(y/100)+START_Y},0", "brush.draw=0.1"])

def setup():
    noise = PerlinNoise(octaves=noise_detail)
    for angle in range(minAngle, maxAngle, angleStep):
        for radius in range(minRadius, maxRadius, radiusStep):
            n = noise([radius*sca, angle*sca])
            m = round(map(n, 0.0, 1.0, mapMin, mapMax))
            if colored == True:
                if m % rules[0] == 0:
                    pencolor = pencolor1
                elif m % rules[1] == 0:
                    pencolor = pencolor2
                else:
                    pencolor = pencolor3

            if (pencolor == pencolor3):
              pass
            else:
              stroke(pencolor)
              x = radius * math.cos(math.radians(angle))
              y = radius * math.sin(math.radians(angle))
              point(x, y)

def main():
    hostname = socket.gethostname()
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,10,14"])
    ob_helper.sendCommands([f"brush.type=Light"])

    setup()
    ob_helper.sendCommands(["debug.brush"])

# Call the main function
if __name__ == '__main__':
    main()
