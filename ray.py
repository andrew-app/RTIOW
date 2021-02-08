from vector import Vec3
import math as m
import array
class Ray:
    def __init__(self, orig, direct):
        self.orig = Vec3(orig)
        self.direct = Vec3(direct)


    def pos(self, t):
        return Vec3([self.orig.x() + t*self.direct.x(), self.orig.y() + t*self.direct.y(), self.orig.z()+t*self.direct.z()])



