from graphics.Vector import Vector as vec2
import socket
import sys
sys.path.append("..")
import ob_helper
import random
import math

w, h = 1000, 1000

colors_list = [[(127, 199, 175), (218, 216, 167), (167, 219, 216), (237, 118, 112)],
          [(230, 57, 70), (241, 250, 238), (29, 53, 87)],
          [(183, 183, 164), (221, 190, 169), (107, 112, 92), (203, 153, 126)],
          [(212, 224, 155), (246, 244, 210), (203, 223, 189), (241, 156, 121), (164, 74, 63)]] 

colors = []

cube_size = random.uniform(4,15)
DEFORM_FACTOR_MAX = 8 
fill_deform = random.uniform(2,DEFORM_FACTOR_MAX)
outline_deform = random.uniform(2,DEFORM_FACTOR_MAX)

border_size = 40
COUNTER = 0
START_Y = 2
BRUSH_TYPE = "ShinyHull"
# BRUSH_TYPE = "SoftHighlighter"

# getDrawPathCoordinates
def getDPC(point, z=0, originCompress=1):
  SCALER=100; return f"{point.x*originCompress/SCALER},{(point.y*originCompress/SCALER)+START_Y},{z}"
  
def vertex(x, y):
  return vec2([x, y])

def get_random_element(l):
    return l[int(random.uniform(0,len(l)))]

def rgb_to_hex(r, g, b):
  return ('{:X}{:X}{:X}').format(r, g, b)

# Center of the quad, size, deform strength, outline, fill color
def draw_rect(x, y, x_s, y_s, d, o, f):
    # print(f"{f[0]}, {f[1]}, {f[2]}")
    # global COUNTER
    # COUNTER += 1
    # print(COUNTER)
    # return

    A = vertex(x - x_s - random.uniform(-d, d), y - y_s - random.uniform(-d, d))
    B = vertex(x + x_s - random.uniform(-d, d), y - y_s - random.uniform(-d, d))
    C = vertex(x + x_s - random.uniform(-d, d), y + y_s - random.uniform(-d, d))
    D = vertex(x - x_s - random.uniform(-d, d), y + y_s - random.uniform(-d, d))

    Z_OFFSET = 0

    randomColor = rgb_to_hex(f[0], f[1], f[2]) #"Crimson" #format(random.randint(0,16777215),'x')
    ob_helper.sendCommands([f"color.set.html={randomColor}"])
    if ("Hull" in BRUSH_TYPE):
      ob_helper.sendCommands([f"brush.type={BRUSH_TYPE}"])
      ob_helper.sendCommands([f"draw.path=[{getDPC(A)}],[{getDPC(B)}],[{getDPC(C)}],[{getDPC(D)}]"])
      # GET SETTINGS FOR THE BORDER READY
      Z_OFFSET = -0.03
      ob_helper.sendCommands([f"brush.type=HighLighter"])
      ob_helper.sendCommands([f"color.set.html=Crimson"])

    ob_helper.sendCommands([f"draw.paths=" +
      f"[[{getDPC(A,Z_OFFSET)}],[{getDPC(B,Z_OFFSET)}]]," + 
      f"[[{getDPC(B,Z_OFFSET)}],[{getDPC(C,Z_OFFSET)}]]," + 
      f"[[{getDPC(C,Z_OFFSET)}],[{getDPC(D,Z_OFFSET)}]]," + 
      f"[[{getDPC(D,Z_OFFSET)}],[{getDPC(A,Z_OFFSET)}]],"
      ])

    
def setup():
    colors = get_random_element(colors_list)
    
    for r in range(10):
        draw_cube_layer(5, get_random_element(colors))
    
    # Go Outside the border
    # if (random.uniform(1) < .9):
        # for r in range(7):
            # draw_cube_layer(5, get_random_element(colors))
    
def draw_cube_layer(o, layer_color):
    first_cube = [random.uniform(0, h), random.uniform(0, 1000)]
    
    cubes = []
    choose_cubes = []
    drawing_cubes = []
    
    cubes.append(first_cube)
    drawing_cubes.append(first_cube)
    choose_cubes.append(first_cube)
    
    for j in range(250):
        c = cubes[int(random.uniform(0,len(cubes)))]
        
        next_cube = c[:]
        if (random.uniform(0,1) < .5):
            if (random.uniform(0,1) < .5):
                next_cube[0] += cube_size
                next_cube[1] -= cube_size*2
            else:
                next_cube[0] -= cube_size
                next_cube[1] -= cube_size*2
        else:
            if (random.uniform(0,1) < .5):
                next_cube[0] += cube_size
                next_cube[1] += cube_size*2
            else:
                next_cube[0] -= cube_size
                next_cube[1] += cube_size*2
            
        if ((next_cube in drawing_cubes) == False):
            cubes.append(next_cube)
            choose_cubes.append(next_cube)
            drawing_cubes.append(next_cube)
            
            # Symmetry mode?
            if (random.uniform(0,1) < .5):
                sym_cube = next_cube[:]
                sym_cube[0] += (w/2 - next_cube[0])*2
                
                cubes.append(sym_cube)
                choose_cubes.append(sym_cube)
            
                drawing_cubes.append(sym_cube)
                
        if j%2 == 0 and len(cubes) > 3:
            cubes.pop(0)
    
    drawing = True
    for c in drawing_cubes:
        if (drawing == True):
            draw_rect(c[0], c[1], cube_size, cube_size, fill_deform, (0, 0, 0, 0), layer_color)
            # draw_rect(c[0], c[1], cube_size, cube_size, outline_deform, (0, 0, 0, 255), (0, 0, 0, 0))
        if (random.uniform(0,1) < .06):
            drawing = False
        
        if (drawing == False and random.uniform(0,1) < .1):
            drawing = True

def main():
    hostname = socket.gethostname()
    if(hostname == "centos7.linuxvmimages.local"):
      ob_helper.ob_host="10.0.2.2"
    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0","brush.look.up"])
    ob_helper.sendCommands(["user.move.to=-8,8,14"])
    ob_helper.sendCommands([f"brush.type={BRUSH_TYPE}"])

    setup()
    # ob_helper.sendCommands(["debug.brush"])

# Call the main function
if __name__ == '__main__':
    main()
