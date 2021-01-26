import array
import sys
from PIL import Image, ImageFilter
from vector import Vec3
from ray import Ray


def ray_color(r):
    unit_dir = Vec3

def main():
    aspect_ratio = 16/9
    img_width = 400
    img_height = int(img_width / aspect_ratio)
    max_val = 255
    ppm_h = f'P6 {img_width} {img_height} {max_val}\n'
    image = array.array('B', [0, 0, 0] * img_width * img_height)

    vp_height = 2.
    vp_width = aspect_ratio * vp_height
    focal = 1.0

    origin = Vec3([0, 0, 0])
    horizontal = Vec3([vp_width, 0, 0])
    vertical = Vec3([0, vp_height, 0])
    llc = origin.sub(horizontal.divide(2)).sub(vertical.divide(2)).sub(Vec3([0, 0, focal]))

    print(f'P6 {img_width} {img_height} {max_val}\n')
    j = 0
    i = 0
    k = 0
    for j in range(img_height-1, 0, -1):

        sys.stderr.write(f'\rScanlines remaining: {j}\n')
        sys.stderr.flush()
        if j < 255:
            k = k + 1

        for i in range(0, img_width, 1):
            index = 3 * (k * img_width + i)

            u = i / (img_width - 1)
            v = j / (img_height - 1)
            print(u, v)




    sys.stderr.write(f'\nDone.\n')



