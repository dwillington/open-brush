
# import sys
# import os
# sys.path.append(os.path.abspath('..'))

# from lib import colors, palettes
# import random
# import socket
# from lib import colors
# from lib import palettes
# import math
# from math import pi

# sys.path.append(os.path.abspath('../../../'))
# import ob_helper
# from ob_helper import Point as ob_Point

import sys
import os
sys.path.append(os.path.abspath('..'))

from lib import colors, palettes
import random
import socket
from lib import colors
from lib import palettes
import math
from math import pi

sys.path.append(os.path.abspath('../../../'))
import ob_helper
from ob_helper import Point as ob_Point

Y_OFFSET = 0


def getDPC(point, Z=0):
    SCALER = 1
    return f"{point[0]*SCALER},{(point[1]*SCALER)+Y_OFFSET},{Z}"


def draw_path(points, X_OFFSET, Y_OFFSET, ORIGIN_COMPRESS, SINGLE_DRAW_PATH=False):
    if SINGLE_DRAW_PATH:
        draw__path = "draw.path="
        for i in range(0, len(points)):
            points[i].origin_compress(ORIGIN_COMPRESS)
            points[i].set_X_offset(X_OFFSET)
            points[i].set_Y_offset(Y_OFFSET)

            draw__path += f"{points[i].get_3d_coordinates()},"
            # TODO: TRIED USING PUT WHICH SHOULD HAVE NO LIMIT, THIS IS PROBABLY HAPPENING AT THE OB LEVEL, SO JUST SEND SMALLER STRINGS
            # SEND DRAW.PATH EVERY X ITERATIONS OR SO OTHERWISE IT BECOMES TOO LONG AND GETS TRUNCATED
            if i > 0 and (i % 10 == 0):
                ob_helper.sendCommands([draw__path])
                draw__path = f"draw.path={points[i].get_3d_coordinates()},"

        if len(points) % 10 != 0:  # DRAW REMAINING POINTS
            ob_helper.sendCommands([draw__path])
        # ob_helper.putCommands({"draw.path": draw__path})
        print(len(draw__path))
    else:
        # DRAW.PATH LINE SEGMENTS
        points[0].origin_compress(ORIGIN_COMPRESS)
        points[0].set_X_offset(X_OFFSET)
        points[0].set_Y_offset(Y_OFFSET)
        for i in range(0, len(points)-1):
            points[i+1].origin_compress(ORIGIN_COMPRESS)
            points[i+1].set_X_offset(X_OFFSET)
            points[i+1].set_Y_offset(Y_OFFSET)
            draw__path = f"draw.path={points[i].get_3d_coordinates()},{points[i+1].get_3d_coordinates()}"
            ob_helper.sendCommands([draw__path])


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
        ob_helper.sendCommands(["brush.type=Light"])
        ob_helper.sendCommands(
            [f"draw.path=[{getDPC(current_position)}],[{getDPC([x,y])}]"])
        del self.position[-1]  # DELETE LAST ELEMENT IN LIST

    def set_line_width(self, width: float):
        ob_helper.sendCommands([f"brush.size.set={width}"])

    def set_source_rgb(self, red: float, green: float, blue: float):
        ob_helper.sendCommands([f"color.set.rgb={red},{blue},{green}"])

    def stroke(self):
        return

    def arc(self, xc: float, yc: float, radius: float, angle1: float, angle2: float, brush_width=0.1):
        print(f"xc:{xc}")
        print(f"yc:{yc}")
        print(f"radius:{radius}")
        # print(f"angle1:{angle1}")
        # print(f"angle2:{angle2}")

        ob_helper.sendCommands([f"brush.transform.push"])
        ob_helper.sendCommands(
            [f"brush.move.to={xc},{yc},0", "brush.look.forwards"])
        ob_helper.sendCommands([f"brush.size.set={brush_width}"])
        ob_helper.sendCommands([f"draw.polygon=12,{radius},0"])
        ob_helper.sendCommands([f"brush.transform.pop"])
        ob_helper.sendCommands([f"brush.size.set=0.1"])


def draw_robot(ctx, x, y, x2, y2, palette):
    # print(f"x:{x}")
    # print(f"y:{y}")
    # margin = int(min(x2 - x, y2 - y) / 20)
    margin = int(2)
    antenna_height = draw_antennas(ctx, x, y, x2, y2, margin, palette)
    face_top = y2 - margin - antenna_height
    face_bottom = y + margin

    # Face.
    face_hex = random.choice(palette['colors'])
    non_face_palette = [c for c in palette['colors'] if c != face_hex]
    face_color = palettes.hex_to_tuple(face_hex)
    face_radius = 0  # random.randint(margin, 5 * margin)
    ob_helper.sendCommands(["brush.type=Light"])
    draw_rounded_rect(ctx, x + margin, x2 - margin, face_top, face_bottom,
                      face_radius, face_color)

    # Eyes. Ensure color different from face.
    eye_color = palettes.hex_to_tuple(random.choice(non_face_palette))
    draw_eyes(ctx, x, x2, face_top, face_bottom, margin, eye_color)

    # Mouth
    mouth_color = palettes.hex_to_tuple(random.choice(non_face_palette))
    ob_helper.sendCommands(["brush.type=Light"])
    draw_mouth(ctx, x, x2, face_top, face_bottom, margin, mouth_color)

    draw_screws(ctx, x, x2, face_top, face_bottom, margin)

    draw_ears(ctx, x, x2, face_top, face_bottom, face_color, margin)


def draw_ears(ctx, x, x2, face_top, face_bottom, face_color, margin):
    # This matches the eye_x
    ear_top = face_top + (face_bottom - face_top) / 3
    ear_width = random.uniform(0.5, 1.5)
    # ear_height = (face_top - ear_top - margin) / random.randint(1, 2)
    ear_height = (face_top - ear_top - margin) / random.randint(2, 5)
    if random.randint(1, 10) <= 10:
        draw_rounded_rect(ctx,
                          x + margin - ear_width,
                          x + margin + 0.1,  # a bit of fuzz to make sure it connects, in case of very rounded faces
                          ear_top,
                          ear_top + ear_height,
                          1, face_color)
        draw_rounded_rect(ctx,
                          (x2 - margin) + 0.1,
                          (x2 - margin) + ear_width,
                          ear_top,
                          ear_top + ear_height,
                          1, face_color)


def draw_screws(ctx, x, x2, face_top, face_bottom, margin):
    screw_count = random.randint(5, 5)
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
    ctx.set_source_rgb(*palettes.hex_to_tuple('#acb4bf'))
    ctx.arc(x, y, radius, 0, 2 * pi)
    # ctx.fill()

    # Outline
    ctx.set_source_rgb(0, 0, 0)
    ctx.arc(x, y, radius+0.2, 0, 2 * pi)
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
        draw_rounded_rect(
            ctx, mouth_x_left, mouth_x_right, mouth_y -
            mouth_line_width, mouth_y + mouth_line_width, 0, color,
            outline=True, outline_width=fine_line_width
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


def draw_line(ctx, x1, y1, x2, y2, line_width, color):
    ctx.set_source_rgb(*color)
    ctx.move_to(x1, y1)
    ctx.set_line_width(0.1)
    ctx.line_to(x2, y2)
    # ctx.set_line_cap(cairo.LINE_CAP_ROUND)
    # ctx.stroke()


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
    ob_helper.sendCommands(["brush.type=ShinyHull"])
    for x in [eye_x1, eye_x2]:
        modified_eye_radius = random.uniform(
            0.8 * eye_radius_base, 1.5 * eye_radius_base)
        ctx.set_source_rgb(*color)
        ctx.arc(x, eye_y, modified_eye_radius, 0, 2 * pi, brush_width=1)
        # ctx.fill()
        if make_pupil:
            ctx.set_source_rgb(0, 0, 0)
            ctx.arc(x, eye_y, modified_eye_radius *
                    (1 - 1 / pupil_radius_factor), 0, 2 * pi, brush_width=1)
            # ctx.fill()
        if make_double_pupil:
            ctx.set_source_rgb(1, 1, 1)
            ctx.arc(x, eye_y, (modified_eye_radius *
                    (1 - 1 / pupil_radius_factor)) / 2, 0, 2 * pi, brush_width=1)
            # ctx.fill()


def draw_antennas(ctx, x, y, x2, y2, margin, palette):
    antenna_color = palettes.hex_to_tuple(random.choice(palette['colors']))
    antenna_height = random.randint(
        (y2 - y - 2 * margin) // 6, (y2 - y - 2 * margin) // 3)
    antenna_count = random.randint(1, 4)
    antenna_bottom = y2 - margin - antenna_height
    antenna_interval = (x2 - x - 2 * margin) / (antenna_count + 1)
    antenna_width = random.uniform(0.1, 0.5)
    for i in range(antenna_count):
        antenna_x = x + margin + antenna_interval * (i + 1)
        ctx.move_to(antenna_x, antenna_bottom)
        ctx.set_source_rgb(*antenna_color)
        ctx.line_to(antenna_x, antenna_bottom + antenna_height + margin)
        # ctx.set_line_cap(cairo.LINE_CAP_ROUND)
        ctx.set_line_width(antenna_width)
        # ctx.stroke()
        if random.randint(1, 10) <= 10:
            ob_helper.sendCommands(["brush.type=Waveform"])
            ctx.arc(
                antenna_x,
                antenna_bottom + antenna_height + margin,
                random.uniform(antenna_width * 2, antenna_width * 5),
                0, 2*pi, brush_width=0.1
            )
            # ctx.set_source_rgb(*antenna_color)
            # ctx.fill()
    return antenna_height


def draw_rounded_rect(ctx, left, right, top, bottom, radius, color, outline=False, outline_width=0.1):
    """ draws rectangles with rounded (circular arc) corners """
    # ctx.arc(left + radius, top + radius, radius, 2*(pi/2), 3*(pi/2))
    # ctx.arc(right - radius, top + radius, radius, 3*(pi/2), 4*(pi/2))
    # ctx.arc(right - radius, bottom - radius, radius, 0*(pi/2), 1*(pi/2))
    # ctx.arc(left + radius, bottom - radius, radius, 1*(pi/2), 2*(pi/2))
    # ctx.close_path()
    # ctx.fill()
    ctx.set_source_rgb(*color)

    Z_OFFSET = 0.0
    A = getDPC([left + radius, top - radius], Z_OFFSET)
    B = getDPC([right - radius, top - radius], Z_OFFSET)
    C = getDPC([right - radius, bottom + radius], Z_OFFSET)
    D = getDPC([left + radius, bottom + radius], Z_OFFSET)

    ob_helper.sendCommands(["brush.type=Diamond"])
    ob_helper.sendCommands([f"draw.path=[{A}]," +
                            f"[{B}]," +
                            f"[{C}]," +
                            f"[{D}]," +
                            f"[{A}]"])

    if outline:
        # ctx.arc(left + radius, top + radius, radius, 2*(pi/2), 3*(pi/2))
        # ctx.arc(right - radius, top + radius, radius, 3*(pi/2), 4*(pi/2))
        # ctx.arc(right - radius, bottom - radius, radius, 0*(pi/2), 1*(pi/2))
        # ctx.arc(left + radius, bottom - radius, radius, 1*(pi/2), 2*(pi/2))
        # ctx.close_path()
        # ctx.set_line_width(outline_width)
        ctx.set_source_rgb(0, 0, 0)

        radius = 0.2
        Z_OFFSET = 0.0
        A = getDPC([left + radius, top - radius], Z_OFFSET)
        B = getDPC([right - radius, top - radius], Z_OFFSET)
        C = getDPC([right - radius, bottom + radius], Z_OFFSET)
        D = getDPC([left + radius, bottom + radius], Z_OFFSET)

        ob_helper.sendCommands(["brush.type=Light"])
        ob_helper.sendCommands([f"draw.path=[{A}],[{B}]"])
        ob_helper.sendCommands([f"draw.path=[{B}],[{C}]"])
        ob_helper.sendCommands([f"draw.path=[{C}],[{D}]"])
        ob_helper.sendCommands([f"draw.path=[{D}],[{A}]"])

        # ctx.stroke()


def main(filename="output.png", img_width=2000, img_height=2000, count=5, palette=random.choice(palettes.PALETTES)):
    if "OB_HOST" in os.environ:
        ob_helper.ob_host = os.environ['OB_HOST']
    ob_helper.sendCommands(["new"])
    ob_helper.sendCommands(["brush.move.to=0,0,0", "brush.look.up"])
    # ob_helper.sendCommands(["user.move.to=-5,8,18"])
    ob_helper.sendCommands(["user.move.to=-10,5,30"])
    ob_helper.sendCommands(["brush.size.set=0.1"])
    ob_helper.sendCommands(["brush.type=Light"])

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
