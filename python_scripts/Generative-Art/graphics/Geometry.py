from numpy import clip
from math import hypot, sqrt
from .Helpers import TWO_PI
from .Vector import Vector as vec2


class Line:
    def __init__(self, x1, y1, x2, y2, draw=True):
        self.p0 = vec2([x1, y1])
        self.p1 = vec2([x2, y2])
        self.id = None

    def get_length(self):
        return sqrt((self.p1.x - self.p0.x)**2 + (self.p1.y - self.p0.y)**2)

    def set_id(self, id):
        self.id = id

    def get_lerp(self, _t):
        x = self.p0.x+(self.p1.x-self.p0.x)*_t
        y = self.p0.y+(self.p1.y-self.p0.y)*_t
        p = vec2([x, y])
        return p

    def get_direction(self):
        d = (self.p0 - self.p1) / self.get_length()
        return d * -1.0
