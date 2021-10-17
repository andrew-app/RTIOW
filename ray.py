from vector import Vec3
import math as m
import numpy as np
class ray:
    def __init__(self, origin, direction):
        self.orig = Vec3(origin)
        self.dir = Vec3(direction)

    
    def at(self, t):
        return self.orig.add(self.dir.multiply_s(t))



