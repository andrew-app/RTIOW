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

    def add(self, v=[]):
        v = array.array('f', v)
        return Vec3(data=(self.x() + v.x(), v.y() + v.y(), v.z() + v.z()))




test = Vec3([253])


print(test.add([1]))



