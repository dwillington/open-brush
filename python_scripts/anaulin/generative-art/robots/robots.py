
import sys
import os
sys.path.append(os.path.abspath('..'))

from lib import colors, palettes
import random
import socket
from lib import colors
from lib import palettes
import math
from ob import ob


Y_OFFSET = 0
SCALER = 1
def getDPC(point, Z=0):
    return f"{round(point[0]*SCALER,2)},{round((point[1]*SCALER)+Y_OFFSET,2)},{round(Z*SCALER,2)}"


"""
https://pycairo.readthedocs.io/en/latest/reference/context.html
"""

class Context:

    position = []

    # def __init__(self):
    # self.position = []

    def move_to(self, x: float, y: float):
        self.position.append([x, y])

    def line_to(self, x: float, y: float):
        current_position = self.position[-1]  # LAST ELEMENT IN LIST
        ob.brush.type(f"Light")
        draw__path = f"[{getDPC(current_position)}],[{getDPC([x,y])}]"
        ob.draw.path(f"{draw__path}")
        del self.position[-1]  # DELETE LAST ELEMENT IN LIST

    def set_line_width(self, width: float):
        ob.brush.size.set(f"{width}")

    def stroke(self):
        return

    def arc(self, xc: float, yc: float, radius: float, angle1: float, angle2: float, brush_width=0.1):
        print(f"xc:{xc}")
        print(f"yc:{yc}")
        print(f"radius:{radius}")
        # print(f"angle1:{angle1}")
        # print(f"angle2:{angle2}")

        ob.brush.transform.push()
        ob.brush.move.to(f"{xc},{yc},0")
        ob.brush.look.forwards()
        ob.brush.size.set(f"{brush_width}")
        ob.draw.polygon(12, radius, 0)
        ob.brush.transform.pop()
        ob.brush.size.set(0.1)


def draw_robot(ctx, x, y, x2, y2, palette):

    # print(f"x:{x}")
    # print(f"y:{y}")
    # margin = int(min(x2 - x, y2 - y) / 20)
    margin = int(2)
    antenna_height = draw_antennas(ctx, x, y, x2, y2, margin, palette)
    face_top = y2 - margin - antenna_height
    face_bottom = y + margin
    # print(f"face_top:{face_top}")
    # print(f"face_bottom:{face_bottom}")

    # Face.
    face_hex = random.choice(palette['colors'])
    non_face_palette = [c for c in palette['colors'] if c != face_hex]
    face_color = palettes.hex_to_tuple(face_hex)
    face_radius = 0  # random.randint(margin, 5 * margin)
    ob.brush.type(f"Light")
    draw_rounded_rect(ctx, x + margin, x2 - margin, face_top, face_bottom,
                      face_radius, face_color, outline=True)

    # Eyes. Ensure color different from face.
    eye_color = palettes.hex_to_tuple(random.choice(non_face_palette))
    draw_eyes(ctx, x, x2, face_top, face_bottom, margin, eye_color)

    # Mouth
    mouth_color = palettes.hex_to_tuple(random.choice(non_face_palette))
    ob.brush.type(f"Light")
    draw_mouth(ctx, x, x2, face_top, face_bottom, margin, mouth_color)

    draw_screws(ctx, x, x2, face_top, face_bottom, margin)
    ob.brush.type(f"Light")
    draw_ears(ctx, x, x2, face_top, face_bottom, face_color, margin)


def draw_ears(ctx, x, x2, face_top, face_bottom, face_color, margin):
    # This matches the eye_x
    ear_bottom = face_top - (face_top - face_bottom) / 2.5
    ear_width = random.uniform(0.5, 1.5)
    # ear_height = (face_top - ear_bottom - margin) / random.randint(1, 2)
    ear_height = random.randint(2, 5)
    if True:
        draw_rounded_rect(ctx,
                          x + margin - ear_width,
                          x + margin - 0.1,  # a bit of fuzz to make sure it connects, in case of very rounded faces
                          ear_bottom + ear_height,
                          ear_bottom,
                          0, face_color)
        draw_rounded_rect(ctx,
                          (x2 - margin) + 0.1,
                          (x2 - margin) + ear_width,
                          ear_bottom + ear_height,
                          ear_bottom,
                          0, face_color)


def draw_screws(ctx, x, x2, face_top, face_bottom, margin):
    screw_count = random.randint(2, 4)
    screw_x = random.choice([x + 2 * margin, x2 - 2 * margin])
    screw_radius = random.uniform(0.05, 0.75)
    for i in range(screw_count):
        screw_y = (face_top - face_bottom) // 3 + \
            face_bottom + i * screw_radius * 3
        draw_screw(ctx, screw_x, screw_y, screw_radius, margin)


def draw_screw(ctx, x, y, radius, margin):
    line_width = margin // 12
    # ctx.save()
    # ctx.translate(x, y)
    # ctx.rotate(pi / 4)

    # Grey circle
    ob.color.set.html("acb4bf")
    ctx.arc(x, y, radius, 0, 2 * math.pi)
    # ctx.fill()

    # Outline
    ob.color.set.rgb(f"0,0,0")
    ctx.arc(x, y, radius+0.2, 0, 2 * math.pi)
    ctx.set_line_width(0.2)
    # ctx.stroke()

    # Cross-threads
    # space_from_edge = 2 + line_width
    # draw_line(ctx, x+0, y+-radius + space_from_edge, x+0, y+radius -
    # space_from_edge, line_width, (0, 0, 0))
    # draw_line(ctx, -radius + space_from_edge, 0, radius -
    # space_from_edge, 0, line_width, (0, 0, 0))

    # ctx.restore()


def draw_mouth(ctx, x, x2, face_top, face_bottom, margin, color):
    # mouth_y = face_top + 2 * (face_bottom - face_top) / 3 + margin
    mouth_y = (face_top - face_bottom) / 3.5 + margin
    mouth_margin = random.randint(
        int((x2 - x - 2 * margin) / 4), int((x2 - x - 2 * margin) / 3))
    mouth_x_left = x + margin + mouth_margin
    mouth_x_right = x2 - margin - mouth_margin
    mouth_line_width = random.randint(margin // 2, margin)

    if random.randint(1, 10) <= 5:
        draw_line(
            ctx,
            mouth_x_left, mouth_y,
            mouth_x_right, mouth_y,
            mouth_line_width,
            color
        )
        smile = random.choice([True, False])
        if smile:
            corner_left = (mouth_x_left - mouth_line_width,
                           mouth_y - mouth_line_width)
            corner_right = (mouth_x_right + mouth_line_width,
                            mouth_y - mouth_line_width)
        else:
            corner_left = (mouth_x_left, mouth_y - mouth_line_width)
            corner_right = (mouth_x_right, mouth_y - mouth_line_width)
        draw_line(
            ctx,
            mouth_x_left, mouth_y,
            *corner_left,
            mouth_line_width, color
        )
        draw_line(
            ctx,
            mouth_x_right, mouth_y,
            *corner_right,
            mouth_line_width, color
        )
    else:
        fine_line_width = mouth_line_width // 9
        #TODO: ONE LONGER CORNER GIVES THE MOUTH A FUNNY LOOK, CAN ADD WITH RANDOMIZATION
        draw_rounded_rect(
            ctx, mouth_x_left, mouth_x_right, mouth_y + mouth_line_width, mouth_y - mouth_line_width, 
            0, color, outline=True, outline_width=fine_line_width
        )
        tooth_interval = (mouth_x_right - mouth_x_left) // 5
        for x in range(int(mouth_x_left + tooth_interval), int(mouth_x_right - tooth_interval + 2), int(tooth_interval)):
            draw_line(
                ctx,
                x, mouth_y - mouth_line_width,
                x, mouth_y + mouth_line_width,
                fine_line_width,
                (0, 0, 0))
        draw_line(ctx, mouth_x_left, mouth_y, mouth_x_right,
                  mouth_y, fine_line_width, (0, 0, 0))


def draw_eyes(ctx, x, x2, face_top, face_bottom, margin, color):
    eye_y = face_top - (face_top - face_bottom) / 3
    eye_x1 = (x2 - x - 2 * margin) / 3 + x + margin
    eye_x2 = 2 * (x2 - x - 2 * margin) / 3 + x + margin
    eye_radius_base = random.uniform(margin * 0.5, int(margin * 1.2))
    if random.randint(1, 10) <= 5:
        draw_line(ctx, eye_x1, eye_y, eye_x2,
                  eye_y, eye_radius_base / 3, color)
    pupil_radius_factor = random.uniform(2, 5)
    make_pupil = random.randint(1, 10) >= 5
    make_double_pupil = random.randint(1, 10) >= 5
    ob.brush.type("ShinyHull")
    if random.randint(1, 10) <= 10:
      for x in [eye_x1, eye_x2]:
          modified_eye_radius = random.uniform(
              0.8 * eye_radius_base, 1.5 * eye_radius_base)
          ob.color.set.rgb(','.join(map(str, color)))
          ctx.arc(x, eye_y, modified_eye_radius, 0, 2 * math.pi, brush_width=1)
          # ctx.fill()
          if make_pupil:
              ob.color.set.rgb("0,0,0")
              ctx.arc(x, eye_y, modified_eye_radius *
                      (1 - 1 / pupil_radius_factor), 0, 2 * math.pi, brush_width=1)
              # ctx.fill()
          if make_double_pupil:
              ob.color.set.rgb("1,1,1")
              ctx.arc(x, eye_y, (modified_eye_radius *
                      (1 - 1 / pupil_radius_factor)) / 2, 0, 2 * math.pi, brush_width=1)
              # ctx.fill()
      if make_double_pupil == False:
        ob.brush.type("Icing")
        randomColor = format(random.randint(0, 16777215), 'x')
        ob.color.set.html(randomColor)
        for x in [eye_x1, eye_x2]:
          x0 = x
          y0 = eye_y
          ob.brush.transform.push()
          ob.brush.move.to(f"{x0},{y0},0")
          ob.brush.look.right()
          cone(eye_radius_base)
          ob.brush.transform.pop()


def draw_antennas(ctx, x, y, x2, y2, margin, palette):
    print(f"x,y:{x},{y}")
    print(f"x2,y2:{x2},{y2}")
    antenna_color = palettes.hex_to_tuple(random.choice(palette['colors']))
    antenna_height = random.randint(
        (y2 - y - 2 * margin) // 6, (y2 - y - 2 * margin) // 3)
    antenna_count = random.randint(1, 4)
    antenna_bottom = y2 - margin - antenna_height
    antenna_interval = (x2 - x - 2 * margin) / (antenna_count + 1)
    for i in range(antenna_count):
        antenna_width = random.uniform(0.1, 0.5)
        antenna_x = x + margin + antenna_interval * (i + 1)
        ob.color.set.rgb(','.join(map(str, antenna_color)))
        # ctx.move_to(antenna_x, antenna_bottom)
        # ctx.line_to(antenna_x, antenna_bottom + antenna_height + margin)
        ob.brush.type(f"Light")
        draw_line(ctx, antenna_x, antenna_bottom, antenna_x, antenna_bottom + antenna_height + margin, random.uniform(3, 5), antenna_color)
        ctx.set_line_width(antenna_width)
        # ctx.stroke()
        if random.randint(1, 10) <= 10:
            ob.brush.type(f"MatteHull")
            ctx.arc(
                antenna_x,
                antenna_bottom + antenna_height + margin,
                random.uniform(antenna_width * 2, antenna_width * 5)*0.25,
                0, 2*math.pi, brush_width=(antenna_width*2)
            )
            ob.brush.type(f"Waveform")
            ctx.arc(
                antenna_x,
                antenna_bottom + antenna_height + margin,
                random.uniform(antenna_width * 2, antenna_width * 5),
                0, 2*math.pi, brush_width=(antenna_width*2)
            )
            # ctx.set_source_rgb(*antenna_color)
            # ctx.fill()
    return antenna_height


def draw_line(ctx, x1, y1, x2, y2, line_width, color):
    ob.color.set.rgb(','.join(map(str, color)))
    ob.brush.size.set(f"{line_width}")
    Z_OFFSET = 0
    A = getDPC([x1, y1], Z_OFFSET)
    B = getDPC([x2, y2], Z_OFFSET)
    ob.draw.path(f"[{A}],[{B}]")


CONE_X_ROTATION = 0
CONE_Y_ROTATION = 0
CONE_Z_ROTATION = 0
def cone(radius, rotations=30):
  ob.brush.turn.x(CONE_X_ROTATION)
  ob.brush.turn.y(CONE_Y_ROTATION)
  ob.brush.turn.z(CONE_Z_ROTATION)
  for i in range(rotations):
    ob.draw.polygon(3, radius, 0)
    ob.brush.turn.x(6)


"""
https://lydxlx1.github.io/blog/2020/05/16/circle-passing-2-pts-with-fixed-r/
"""
def centers_of_circles(x1, y1, x2, y2, r):
    q = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    x3 = (x1 + x2) / 2
    y3 = (y1 + y2) / 2

    xx = (r ** 2 - (q / 2) ** 2) ** 0.5 * (y1 - y2) / q
    yy = (r ** 2 - (q / 2) ** 2) ** 0.5 * (x2 - x1) / q
    return ((x3 + xx, y3 + yy), (x3 - xx, y3 - yy))

def draw_rounded_corner(left, right, top, bottom, rounded=True):
    points = []
    if (rounded != True) or (abs(right - left) <= 1) or (abs(top - bottom) <= 1): # TOO CLOSE, DRAW SHARP SQUARE
      points = [[left,top],[right,top],[right,bottom],[left,bottom]]
    else:
      x = left
      y = top
      A1 = [x      , y-0.5]
      A2 = [x+0.125, y-0.25]
      A3 = [x+0.25 , y-0.125]
      A4 = [x+0.5  , y]
      points.append(A1)
      points.append(A2)
      points.append(A3)
      points.append(A4)

      #########################
      # CONVERT B,C,D TO ROUNDED
      #########################
      
      x = right
      y = top
      points.append([x,y])
      x = right
      y = bottom
      points.append([x,y])
      x = left
      y = bottom
      points.append([x,y])

    return points

    # ob.brush.transform.push()
    # ob.brush.move.to(f"{getDPC(A1)}")
    # ob.brush.draw(1)
    # ob.brush.move.to(f"{getDPC(A2)}")
    # ob.brush.draw(1)
    # c1, c2 = centers_of_circles(A1[0],A1[1],A2[0],A2[1], 5)
    # ob.brush.move.to(f"{getDPC(c1)}")
    # ob.brush.draw(1)
    # print(c1)
    # print(c1)
    # angle1 = math.degrees(math.atan2(float(c1[1]-A1[1]), float(c1[0]-A1[0])))
    # angle2 = math.degrees(math.atan2(float(c1[1]-A2[1]), float(c1[0]-A2[0])))
    # print(f"angle1:{angle1}")
    # print(f"angle2:{angle2}")
    # ob.brush.transform.pop()

def draw_rounded_rect(ctx, left, right, top, bottom, radius, color, outline=False, outline_width=0.1):
    # print(left, right, top, bottom)
    """ draws rectangles with rounded (circular arc) corners """
    # ctx.arc(left + radius, top + radius, radius, 2*(pi/2), 3*(pi/2))
    # ctx.arc(right - radius, top + radius, radius, 3*(pi/2), 4*(pi/2))
    # ctx.arc(right - radius, bottom - radius, radius, 0*(pi/2), 1*(pi/2))
    # ctx.arc(left + radius, bottom - radius, radius, 1*(pi/2), 2*(pi/2))
    # ctx.close_path()
    # ctx.fill()
    ob.color.set.rgb(','.join(map(str, color)))

    Z_OFFSET = 0.0
    POINTS = draw_rounded_corner(left + radius, right - radius, top - radius, bottom + radius, True)
    ROUNDED_POINTS = ""
    for point in POINTS:
      ROUNDED_POINTS += f"[{getDPC(point, Z_OFFSET)}],"
    # print(ROUNDED_POINTS)

    # A = getDPC([left + radius, top - radius], Z_OFFSET)
    # B = getDPC([right - radius, top - radius], Z_OFFSET)
    # C = getDPC([right - radius, bottom + radius], Z_OFFSET)
    # D = getDPC([left + radius, bottom + radius], Z_OFFSET)

    ob.brush.type(f"Diamond")
    ROUNDED_POINTS += f"[{getDPC(POINTS[0], Z_OFFSET)}],"
    draw__path = (f"{ROUNDED_POINTS}")
    print(draw__path)
    ob.draw.path(f"{draw__path}")

    if outline:
        # ctx.arc(left + radius, top + radius, radius, 2*(pi/2), 3*(pi/2))
        # ctx.arc(right - radius, top + radius, radius, 3*(pi/2), 4*(pi/2))
        # ctx.arc(right - radius, bottom - radius, radius, 0*(pi/2), 1*(pi/2))
        # ctx.arc(left + radius, bottom - radius, radius, 1*(pi/2), 2*(pi/2))
        # ctx.close_path()
        # ctx.set_line_width(outline_width)
        ob.color.set.rgb("0,0,0")

        radius = 0.2
        Z_OFFSET = 0.0
        A = getDPC([left + radius, top - radius], Z_OFFSET)
        B = getDPC([right - radius, top - radius], Z_OFFSET)
        C = getDPC([right - radius, bottom + radius], Z_OFFSET)
        D = getDPC([left + radius, bottom + radius], Z_OFFSET)

        ob.brush.type(f"Light")
        ob.draw.path(f"[{A}],[{B}]")
        ob.draw.path(f"[{B}],[{C}]")
        ob.draw.path(f"[{C}],[{D}]")
        ob.draw.path(f"[{D}],[{A}]")

        # ctx.stroke()


def main(filename="output.png", img_width=2000, img_height=2000, count=5, palette=random.choice(palettes.PALETTES)):
    if "OB_HOST" in os.environ:
      ob.OB_HOST = os.environ['OB_HOST']
    ob.new()
    ob.brush.move.to(f"0,0,0")
    ob.brush.look.up()
    if "OB_HOST" in os.environ:
      ob.user.move.to(f"-10,5,20")
    else:
      ob.user.move.to(f"-25,5,30")
    ob.brush.size.set(0.1)
    ob.brush.type(f"Light")

    while len(palette['colors']) < 3:
        print(f"Palette {palette} has too few colors. Choosing another one.")
        palette = random.choice(palettes.PALETTES)

    ctx = Context()

    # ims = cairo.ImageSurface(cairo.FORMAT_ARGB32, img_width, img_height)
    # ctx = cairo.Context(ims)

    # Make background solid color
    # ctx.rectangle(0, 0, img_width, img_height)
    # ctx.set_source_rgb(*palettes.hex_to_tuple(palette['background']))
    # ctx.fill()

    x_size = img_width // count
    y_size = img_width // count
    for x in range(count):
        for y in range(count):
            draw_robot(ctx, x * x_size, y * y_size, (x+1)
                       * x_size, (y+1) * y_size, palette)

    # ims.write_to_png(filename)


def make_random(filename="output.png", p=random.choice(palettes.PALETTES), img_width=2000, img_height=2000):
    c = random.randint(3, 10)
    print(filename, os.path.basename(__file__), c, p)
    main(filename=filename, count=1, palette=p, img_height=10, img_width=25)


if __name__ == "__main__":
    for idx in range(1):
        make_random(filename="output-{}.png".format(idx),
                    p=random.choice(palettes.PALETTES))
