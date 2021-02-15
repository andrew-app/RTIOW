import array
import sys
from PIL import Image
from vector import Vec3
from ray import Ray
import math




def main():
    aspect_ratio = 16 / 9
    img_width = 400
    img_height = int(img_width / aspect_ratio)
    max_val = 255
    ppm_h = f'P6 {img_width} {img_height} {max_val}\n'
    image = array.array('B', [217, 232, 255] * img_width * img_height)

    vp_height = 2.0
    vp_width = round(aspect_ratio * vp_height)
    focal = 1.0

    origin = Vec3([0, 0, 0])
    horizontal = Vec3([vp_width, 0, 0])
    vertical = Vec3([0, vp_height, 0])
    hlc = horizontal.multiply_s(0.5)
    vlc = vertical.multiply_s(0.5)
    fl = Vec3([0, 0, focal])

    llc = origin.sub(hlc) #origin - horizontal/2 - vertical/2 - vec3(0, 0, focal_length);
    llc = llc.sub(vlc)
    llc = llc.sub(fl)
    sphere = [255, 0, 0]
    print(f'P6 {img_width} {img_height} {max_val}\n')
    print(vp_width)
    k = 0
    for j in range(img_height - 1, 0, -1):

        sys.stderr.write(f'\rScanlines remaining: {j}\n')
        sys.stderr.flush()
        if j < 255:
            k = k + 1

        for i in range(0, img_width, 1):
            index = 3 * (k * img_width + i)
            col1 = [1.0, 1.0, 1.0]
            col2 = [0.5, 0.7, 1.0]
            u = i / (img_width - 1)
            v = j / (img_height - 1)

            r = llc.add(horizontal.multiply_s(u)).add(vertical.multiply_s(v)).sub(origin)

            center = Vec3([0, 0, -1])
            oc = origin.sub(center)
            da = r.dot_p(r)
            db = oc.dot_p(r)
            db = 2.0 * db
            dc = oc.dot_p(oc)
            dc = dc - 0.5 * 0.5
            discrim = (db ** 2) - 4 * da * dc

            if discrim < 0:
                t = -1.0

            else:
                t = (-db - math.sqrt(discrim)) / (2.0 * da)



            # Red Circle
            if t > 0:
                N = r.multiply_s(t)
                N = N.sub(center)
                N = N.unitvec()
                p = Vec3([1, 1, 1])

                rayN = N.add(p)
                rayN = rayN.multiply_s(0.5)
                image[index] = round(255.0*rayN.x())
                image[index + 1] = round(255.0*rayN.y())
                image[index + 2] = round(255.0*rayN.z())

            else:
                unit_direction = r.unitvec()
                t = 0.5 * (unit_direction.y() + 1.0)
                l = 0

                for x in col1:
                    col1[l] = (1.0 - t) * x
                    l = l + 1

                m = 0

                for y in col2:
                    col2[m] = t * y
                    m = m + 1

                ray_color = [x + y for x, y in zip(col1, col2)]
                retray = Vec3(ray_color)
                rayr = round(255 * retray.x())
                rayg = round(255 * retray.y())
                rayb = round(255 * retray.z())
                image[index] = rayr
                image[index + 1] = rayg
                image[index + 2] = rayb

            print(image[index], image[index + 1], image[index + 2])


    sys.stderr.write(f'\nDone.\n')
    with open("rayimg.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii'))
        image.tofile(f)


main()

original_image = Image.open("rayimg.ppm")
original_image.show()
