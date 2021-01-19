import numpy as np


class Vec3:
    def __init__(self, e=np.array((0.0, 1.0, 3.0))):

        self.e = np.array(e)

    def x(self): return self.e[0]


    def y(self): return self.e[1]
    def z(self): return self.e[2]
    def r(self): return self.e[0]
    def g(self): return self.e[1]
    def b(self): return self.e[2]




x = Vec3.x

print(x)




