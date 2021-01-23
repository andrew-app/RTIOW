import array


class Vec3:
    def __init__(self, e=[]):

        self.e = array.array('f', e)


    def __str__(self): return str(self.e)

    def x(self): return round(self.e[0], 2)
    def y(self): return round(self.e[1], 2)
    def z(self): return round(self.e[2], 2)
    def r(self): return int(self.e[0])
    def g(self): return int(self.e[1])
    def b(self): return int(self.e[2])

    def add(self, v):
        return Vec3(e=(self.x() + v.x(), self.y() + v.y(), self.z() + v.z()))

    def multiply(self, t):
        return Vec3(e=(self.x()*t, self.y()*t, self.z()*t))

    def divide(self, t):
        return Vec3(e=(round(self.x(), 2)/t, self.y()/t, self.z()/t))



t1 = Vec3([250, 1, 1])

t2 = Vec3([2, 0, 0])

t3 = t1.divide(3)

print(t3)




