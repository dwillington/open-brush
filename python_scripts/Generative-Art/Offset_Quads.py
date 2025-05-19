# https://py.processing.org/reference/
from graphics.Vector import Vector as vec2
import os
import socket
import sys
sys.path.append("..")
import ob_helper
import random
import math

w, h = 1000, 1000

#colors = [(127, 199, 175, 110), (218, 216, 167, 110), (167, 219, 216, 110), (237, 118, 112, 110)]
colors = [(92,97,130, 110), (79,164,165, 110), (202,166,122, 110), (212,117,100, 110)]
#colors = [(139,169,135, 150), (244,107,99, 150), (100,161,165, 150)]

# Number of quads
grid_x = 30
grid_y = 30

# Seperation between the bricks
diff = 6
base_deform = 3
back_deform = 0
offset = 2

# Nature of the grid changes
horizontal_length = 2

# The quads will draw inside this rectangle
grid_x_pixels = .9 * w
grid_y_pixels = .9 * h

# Distance between the birds
sep_x = float(grid_x_pixels) / (grid_x - 1)
sep_y = float(grid_y_pixels) / (grid_y - 1)

def get_random_element(l):
    return l[int(random.uniform(0,len(l)))]

# getDrawPathCoordinates
def getDPC(point, z=0, originCompress=1):
  return f"{point.x*originCompress/100},{point.y*originCompress/100},{z}"
  
def vertex(x, y):
  return vec2([x, y])

# Center of the quad, size, deform strength, rotation, outline, fill color
def draw_rect(x, y, x_s, y_s, d, r, o, f):

    # stroke(*o)
    # fill(*f)
    # strokeJoin(ROUND)
    # beginShape()

    A = vertex(x - x_s - random.uniform(-d, d), y - y_s - random.uniform(-d, d))
    B = vertex(x + x_s - random.uniform(-d, d), y - y_s - random.uniform(-d, d))
    C = vertex(x + x_s - random.uniform(-d, d), y + y_s - random.uniform(-d, d))
    D = vertex(x - x_s - random.uniform(-d, d), y + y_s - random.uniform(-d, d))

    if (o[3] == 255):
      # pass
      Z_OFFSET = -0.03
      randomColor = "Crimson" #format(random.randint(0,16777215),'x')
      ob_helper.sendCommands([f"color.set.html={randomColor}"])
      ob_helper.sendCommands(["brush.type=Highlighter"])
      ob_helper.sendCommands([f"draw.paths=" +
        f"[[{getDPC(A,Z_OFFSET)}],[{getDPC(B,Z_OFFSET)}]]," + 
        f"[[{getDPC(B,Z_OFFSET)}],[{getDPC(C,Z_OFFSET)}]]," + 
        f"[[{getDPC(C,Z_OFFSET)}],[{getDPC(D,Z_OFFSET)}]]," + 
        f"[[{getDPC(D,Z_OFFSET)}],[{getDPC(A,Z_OFFSET)}]],"
        ])
    else: # FILL
      Z_OFFSET = 0 # random.uniform(0, 4)
      OC = 1
      randomColor = format(random.randint(0,16777215),'x')
      ob_helper.sendCommands([f"color.set.html={randomColor}"])
      ob_helper.sendCommands(["brush.type=UnlitHull"])
      ob_helper.sendCommands([f"draw.path=[{getDPC(A)}],[{getDPC(B)}],[{getDPC(C)}],[{getDPC(D)}]," + 
        f"[{getDPC(B,Z_OFFSET,OC)}],[{getDPC(C,Z_OFFSET,OC)}]," + 
        f"[{getDPC(D,Z_OFFSET,OC)}],[{getDPC(A,Z_OFFSET,OC)}],"])

# ,[{getDPC(A)}]
    # endShape(CLOSE)
    
def setup():
    
    grid = []
    
    for i in range(grid_x):
        grid.append([])
        for j in range(grid_y):
            grid[i].append(1)
            
    for i in range(grid_x):
        for j in range(grid_y):
            if (i < grid_x - 1):
                if (random.uniform(0,1) < .3 and grid[i][j] == 1):
                    grid[i][j] = 2
                    grid[i + 1][j] = 0
            if (j < grid_y - 1):
                if (random.uniform(0,1) < .3 and grid[i][j] == 1 and grid[i][j + 1] != 0):
                    grid[i][j] = 3
                    grid[i][j + 1] = 0
            if (i < grid_x - 1 and j < grid_y - 1):
                if (random.uniform(0,1) < .2 and grid[i][j] == 1 and grid[i][j + 1] == 1 and grid[i + 1][j] == 1 and grid[i + 1][j + 1] == 1):
                    grid[i][j] = 4
                    grid[i + 1][j] = 0
                    grid[i][j + 1] = 0
                    grid[i + 1][j + 1] = 0
    
    current_x = w/2.0 - grid_x_pixels/2.0
    current_y = h/2.0 - grid_y_pixels/2.0
    for i in range(grid_x):
        for j in range(grid_y):
            o = (0, 0, 0, 255)
            f = (0, 0, 255, 0)
            
            cell = grid[i][j]
            
            short_x = sep_x/2 - diff
            long_x = sep_x - diff
            short_y = sep_y/2 - diff
            long_y = sep_y - diff
            
            if (cell == 1):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + random.uniform(-offset, offset), current_y + random.uniform(-offset, offset), short_x, short_y, back_deform, -1, o, f)
            
                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x, current_y, short_x, short_y, base_deform, -1, o, f)
            if (cell == 2):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + sep_x/2 + random.uniform(-offset, offset), current_y + random.uniform(-offset, offset), long_x, short_y, back_deform, -1, o, f)
            
                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x + sep_x/2, current_y, long_x, short_y, base_deform, -1, o, f)
            if (cell == 3):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + random.uniform(-offset, offset), current_y + sep_y/2 + random.uniform(-offset, offset), short_x, long_y, back_deform, -1, o, f)

                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x, current_y + sep_y/2, short_x, long_y, base_deform, -1, o, f)
            if (cell == 4):
                
                o = (0, 0, 0, 0)
                f = get_random_element(colors)
                draw_rect(current_x + sep_x/2 + random.uniform(-offset, offset), current_y + sep_y/2 + random.uniform(-offset, offset), long_x, long_y, back_deform, -1, o, f)

                o = (0, 0, 0, 255)
                f = (0, 0, 255, 0)
                draw_rect(current_x + sep_x/2, current_y + sep_y/2, long_x, long_y, base_deform, -1, o, f)
            
            current_y += sep_y
        current_y = h/2.0 - grid_y_pixels/2.0
        current_x += sep_x

def main():
    hostname = socket.gethostname()
    if "OB_HOST" in os.environ:
      ob_helper.ob_host=os.environ['OB_HOST']

    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-5,10,10"])
    ob_helper.sendCommands(["brush.size.set=0.01"])

    setup()
    ob_helper.sendCommands(["debug.brush"])

# Call the main function
if __name__ == '__main__':
    main()
