from vector import Vec3
import math as m
import array
class Ray:
    def __init__(self, orig, direct):
        self.orig = orig
        self.direct = direct


    def pos(self, t):
        return self.origin.add(self.direction.multiply_s(t))



