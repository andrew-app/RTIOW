from vector import Vec3
import math
import numpy as np
from ray import ray

class hit_record:
    def __init__(self):
        self.p = None
        self.outward_normal = None
        self.normal = None
        self.t = None
        self.front_face = None
        
    
    def set_face_normal(self, r, outward_normal):
        front_face = bool(outward_normal.dot_p(r.dir) < 0)
        normal = outward_normal if front_face else outward_normal.multiply_s(-1)
        return normal

class hittable:
    def __init__(self,center, radius):
        self.radius = radius
        self.center = center
    def hit(self,r,t_min,t_max,rec):
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

        setattr(rec, 't', root)
        setattr(rec, 'p', r.at(rec.t))
        setattr(rec, 'outward_normal', rec.p.sub(self.center).divide(self.radius))
        setattr(rec, 'front_face', bool(rec.outward_normal.dot_p(r.dir) < 0))
        setattr(rec, 'normal', rec.set_face_normal(r, rec.outward_normal))

        if (rec.outward_normal != rec.normal):
            print(rec.outward_normal, rec.normal)

        return True


        

