import array
import sys
from PIL import Image
from vector import Vec3



def main():
    aspect_ratio = 16/9
    img_width = 400
    img_height = int(img_width / aspect_ratio)
    max_val = 255
    ppm_h = f'P6 {img_width} {img_height} {max_val}\n'
    image = array.array('B', [255, 255, 255] * img_width * img_height)
    col1 = Vec3([1.0, 1.0, 1.0])
    col2 = Vec3([0.5, 0.7, 1.0])
    vp_height = 2.0
    vp_width = aspect_ratio * vp_height
    focal = 1.0

    origin = Vec3([0, 0, 0])
    horizontal = Vec3([vp_width, 0, 0])
    vertical = Vec3([0, vp_height, 0])
    llc = origin.sub(horizontal.divide(2)).sub(vertical.divide(2)).sub(Vec3([0, 0, focal]))

    print(f'P6 {img_width} {img_height} {max_val}\n')
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
            r = llc.add(horizontal.multiply_s(u)).add(vertical.multiply_s(v)).sub(origin)
            unit_direction = r.unitvec()
            udir = Vec3(unit_direction)
            a = udir.y()
            b = a + 1.0
            t = 0.5*b
            c = 1.0 - t

            ray_color = col1.multiply_s(c).add(col2.multiply_s(t))
            image[index] = 255 * int(ray_color.x())
            image[index + 1] = 255 * int(ray_color.y())
            image[index + 2] = 255 * int(ray_color.z())
            print(ray_color)


    sys.stderr.write(f'\nDone.\n')
    with open("rayimg.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii'))
        image.tofile(f)



main()


original_image = Image.open("rayimg.ppm")
original_image.show()
