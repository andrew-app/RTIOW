from vector import Vec3
import math
import numpy as np
from ray import ray

class hit_record:
    def __init__(self):
        self.p = None
        self.normal = None
        self.t = None
        

class hittable:
    def __init__(self,center, radius):
        self.radius = radius
        self.center = center
    def hit(self,r,t_min,t_max,hit_record):
        oc = r.orig.sub(self.center)
        a = r.dir.length_s()
        half_b = oc.dot_p(r.dir)
        c = oc.length_s() - self.radius**2

        discriminant = half_b**2-a*c

        if discriminant < 0:
            return False

        sqrtd = math.sqrt(discriminant)
        root = (-half_b - sqrtd) / a

        if root < t_min or root > t_max:
            root = (-half_b + sqrtd) / a
            if root < t_min or root > t_max:
                return False

        setattr(hit_record, 't', root)
        setattr(hit_record, 'p', r.at(hit_record.t))
        setattr(hit_record, 'normal', hit_record.p.sub(self.center).divide(self.radius))
        return True


        

