from hittable import hit_record,hittable
from vector import Vec3
from ray import ray
import math
import numpy as np
import array

class hittable:

    

    def hit(r,t_min,t_max,rec):
        temp_rec = hit_record()
        hit_anything = False
