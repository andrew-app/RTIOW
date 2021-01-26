from vector import Vec3
import math as m

class Ray:
    def __init__(self, orig, direct):
        self.orig = orig
        self.direct = direct


    def point3(self, t):
        return self.orig + t*self.direct

