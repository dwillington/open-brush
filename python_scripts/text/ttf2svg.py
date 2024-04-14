#!python3
# Convert character of TTF to SVG.
# Author: "Gary Lee" <garywlee@gmail.com>

# Usage: ttf2svg.py [char] [OUTPUT_FILE] [TTF_FONT]
# Example: ttf2svg.py A A.svg /Library/Fonts/arial.ttf'
#
# Requirement:
# - pip3 install freetype-py
# - pip3 install svgpathtools
#
# References:
# - https://www.freetype.org/freetype2/docs/reference/ft2-outline_processing.html#ft_outline_decompose
# - https://gist.github.com/p3t3r67x0/a35e9e0e9f6f22053e8f7a5543b59724

import sys
from freetype import Face, FT_Curve_Tag, FT_Curve_Tag_On, FT_Vector
from svgpathtools import (wsvg, Line, CubicBezier, QuadraticBezier, Path)

class TtfSvgConverter:
    VERBOSE = False
    STROKE_WIDTHS = 10
    CHAR_WIDTH = 48
    CHAR_HEIGHT = 64
    CHAR_SIZE = CHAR_WIDTH * CHAR_HEIGHT
    def __init__(self, ttfPath=None):
        self.ttfPath = ttfPath
        self.reset()

    def reset(self):
        self.svgPath = []
        self._lastX = 0
        self._lastY = 0

    def _verbose(self, *args):
        if self.VERBOSE:
            print(*args)

    def lastXyToComplex(self):
        return self.tupleToComplex((self._lastX, self._lastY))

    def tupleToComplex(self, xy):
        return xy[0] + xy[1] * 1j

    def vectorToComplex(self, v):
        return v.x + v.y * 1j

    def vectorsToPoints(self, vectors):
        return [(v.x, v.y) for v in vectors if v is not None]

    def callbackMoveTo(self, *args):
        self._verbose('MoveTo ', len(args), self.vectorsToPoints(args))
        self._lastX, self._lastY = args[0].x, args[0].y

    def callbackLineTo(self, *args):
        self._verbose('LineTo ', len(args), self.vectorsToPoints(args))
        line = Line(self.lastXyToComplex(), self.vectorToComplex(args[0]))
        self.svgPath.append(line)
        self._lastX, self._lastY = args[0].x, args[0].y

    def callbackConicTo(self, *args):
        self._verbose('ConicTo', len(args), self.vectorsToPoints(args))
        curve = QuadraticBezier(self.lastXyToComplex(), self.vectorToComplex(args[0]), self.vectorToComplex(args[1]))
        self.svgPath.append(curve)
        self._lastX, self._lastY = args[1].x, args[1].y

    def callbackCubicTo(self, *args):
        self._verbose('CubicTo', len(args), self.vectorsToPoints(args))
        curve = CubicBezier(self.lastXyToComplex(), self.vectorToComplex(args[0]), self.vectorToComplex(args[1]), self.vectorToComplex(args[2]))
        self.svgPath.append(curve)
        self._lastX, self._lastY = args[2].x, args[2].y

    def calcViewBox(self, path):
        xmin, xmax, ymin, ymax = path.bbox()
        xmin, xmax, ymin, ymax = xmin - self.CHAR_WIDTH, xmax + self.CHAR_WIDTH, ymin - self.CHAR_HEIGHT, ymax + self.CHAR_HEIGHT
        dx = xmax - xmin
        dy = ymax - ymin
        viewbox = '{} {} {} {}'.format(xmin, ymin, dx, dy)
        return viewbox

    def generate(self, text, CHAR_SIZE, output):
        self.reset()
        face = Face(self.ttfPath)
        face.set_char_size(int(CHAR_SIZE))
        for ch in text:
            face.load_char(ch)
            outline = face.glyph.outline
            outline.decompose(context=None, move_to=self.callbackMoveTo, line_to=self.callbackLineTo, conic_to=self.callbackConicTo, cubic_to=self.callbackCubicTo)
            path = Path(*self.svgPath).scaled(1, -1)
            viewbox = self.calcViewBox(path)
            attr = {
                'width': '100%',
                'height': '100%',
                'viewBox': viewbox,
                'preserveAspectRatio': 'xMidYMid meet'
            }
            wsvg(paths=path, colors=['#016FB9'], svg_attributes=attr, stroke_widths=[self.STROKE_WIDTHS], filename=output)
            break # Only handle the first character.
        
def main():
    if len(sys.argv) <= 3:
        print('Usage: ttf2svg.py [char] [SIZE] [TTF_FONT]')
        print('Example: ttf2svg.py A 64 /Library/Fonts/arial.ttf')
        sys.exit()
    
    fullfile = sys.argv[3]
    import os
    filename = os.path.basename(fullfile)
    name = os.path.splitext(f"{filename}")[0]
    if False == os.path.isdir(name): os.mkdir(name)
    
    converter = TtfSvgConverter(ttfPath=sys.argv[3])
    out_filename = name+"/"+sys.argv[1]+".svg"
    converter.generate(sys.argv[1], sys.argv[2], out_filename)

if __name__ == '__main__':
    main()

# fc-list> /mnt/c/temp/tmp/fonts.txt
# for i in {0..9}
# do
  # python ttf2svg.py $i 64 /usr/share/fonts/truetype/ubuntu/UbuntuMono-RI.ttf
# done
