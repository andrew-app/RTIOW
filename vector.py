import array
import math as m

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

    def sub(self, v):
        return Vec3(e=(self.x() - v.x(), self.y() - v.y(), self.z() - v.z()))

    def divide(self, t):
        return Vec3(e=(round(self.x(), 2)/t, self.y()/t, self.z()/t))

    def multiply(self, v):
        return Vec3(e=(self.x() * v.x(), self.y() * v.y(), self.z() * v.z()))


    def multiply_s(self, t):
        return Vec3(e=(self.x() * t, self.y() * t, self.z() * t))

    def arrlen(self):
        return len(self.e)

    def length(self):
        a = Vec3(e=(self.x() * self.x(), self.y() * self.y(), self.z() * self.z()))
        ls = a.x() + a.y() + a.z()
        return round(m.sqrt(ls), 3)

    def length_s(self):
        a = Vec3(e=(self.x() * self.x(), self.y() * self.y(), self.z() * self.z()))
        return a.x()+a.y()+a.z()

    def dot_p(self, v):
        a = Vec3(e=(self.x() * v.x(), self.y() * v.y(), self.z() * v.z()))
        return a.x()+a.y()+a.z()

    def cross_p(self, v):
        a = Vec3(e=(self.y() * v.z(), self.z() * v.x(), self.x() * v.y()))
        b = Vec3(e=(self.z() * v.y(), self.x() * v.z(), self.y() * v.x()))
        return Vec3(e=(a.x() - b.x(), a.y() - b.y(), a.z() - b.z()))

    def unitvec(self):
        return Vec3(e=(self.x()/self.length(), self.y()/self.length(), self.z()/self.length()))






