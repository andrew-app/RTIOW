from vector import Vec3
import math as m
import numpy as np
class ray:
    def __init__(self, origin, direction):
        self.orig = origin
        self.dir = direction
        

    def at(self,t):
        dir = self.dir
        tdir = dir.multiply_s(t)
        return tdir.add(self.orig)



