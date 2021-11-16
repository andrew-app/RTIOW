import sys
from PIL import Image
from vector import Vec3
from ray import ray
import math
import numpy as np
import array
from tqdm import tqdm
from hittable import hit_record,hittable



def ray_color(r):
    #linear interpolation to get blended color between blue and white
    r = np.array(r)
    direction = Vec3(r)
    unit_direction = direction.unitvec()
    center = Vec3([0,0,-1])
    origin = Vec3([0,0,0])
    temp = ray(origin,direction)
    tst = hittable(center, 0.5)
    rechit = hit_record()
    check_hit = tst.hit(temp, 0, 1, rechit)
    N = rechit.normal #vec3 N = unit_vector(r.at(t) - vec3(0,0,-1))
    if check_hit is True:
        N = Vec3([N.x()+1,N.y()+1,N.z()+1]) #color according to normals
        N = N.multiply_s(0.5) 
        return N
    t = 0.5*(unit_direction.y() + 1.0) #color blend depends on height of y coordinate(blue at top white at bottom of screen)
    color1 = Vec3([1.0,1.0,1.0])
    color2 = Vec3([0.5,0.7,1.0])
    retval = color1.multiply_s(1.0-t).add(color2.multiply_s(t)) #blended value = (1-t) * startValue + t*endValue
    return retval


def main():

    #Render Image Dimensions

    aspect_ratio = 16.0 / 9.0

    #aspect ratio = image_width/image_height

    image_width = 400

    image_height = image_width / aspect_ratio

    #Viewport Camera

    viewport_height = 2.0
    viewport_width = aspect_ratio * viewport_height
    focal_length = 1.0

    origin = Vec3([0,0,0]) 
    horizontal = Vec3([viewport_width,0,0])
    vertical = Vec3([0,viewport_height,0])

    # Next 4 lines: lower_left_corner = origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length)
    lower_left_corner = origin.sub(horizontal.divide(2))
    lower_left_corner = lower_left_corner.sub(vertical.divide(2))
    temp = Vec3([0,0, focal_length])
    lower_left_corner = lower_left_corner.sub(temp)

    #Render
    max_val = 255
    ppm_h = f"P6 {image_width} {int(image_height)} {max_val}\n" #!!!Remember to cast to int for image height otherwise error when writing to file
    image = array.array('B', [0, 0, 0] * image_width * int(image_height))
    index = 0
    
    
    for j in tqdm(range(int(image_height)-1,0,-1)):
        
        for i in range(0,image_width):
            
            u = i / (image_width-1)
            v = j / (image_height-1)

            # Next 3 lines: ray_direction = lower_left_corner + u*horizontal + v*vertical - origin
            direction = lower_left_corner.add(horizontal.multiply_s(u))
            direction = direction.add(vertical.multiply_s(v))
            direction = direction.sub(origin)
            pixel_color = ray_color([direction.x(),direction.y(),direction.z()])
            
            pixel_color = pixel_color.multiply_s(255) # get lerp values to RGB colorspace
            px = np.array([pixel_color.r(),pixel_color.g(),pixel_color.b()])
            px[px>max_val]=255 #force max val if needed
            image[index] = px[0]
            image[index + 1] = px[1]
            image[index + 2] = px[2]
            index = index+3 #traverse to next 3 RGB pixels in array
    with open("surfnormalsv2.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii')) 
        image.tofile(f)
    print("Render Complete.")
    view_image = Image.open("surfnormalsv2.ppm")
    view_image.show()


    

main()
