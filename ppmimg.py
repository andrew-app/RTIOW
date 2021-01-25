import array
import sys
from PIL import Image, ImageFilter
from vector import Vec3


def main():
    img_width = 256
    img_height = 256
    max_val = 255

    ppm_h = f'P6 {img_width} {img_height} {max_val}\n'

    j = 0
    i = 0
    k = 0

    image = array.array('B', [0, 0, 63] * img_width * img_height)


    for j in range(img_height-1, 0, -1):

        sys.stderr.write(f'\rScanlines remaining: {j}\n')
        sys.stderr.flush()
        if j < 255:
            k = k + 1

        for i in range(0, img_width, 1):
            index = 3 * (k * img_width + i)

            col = Vec3([i / (img_width - 1), j / (img_height - 1), 0.25])

            ncol = col.multiply_s(255)

            image[index] = int(ncol.x())
            image[index+1] = int(ncol.y())
            image[index+2] = int(ncol.z())
            print(f'{int(ncol.x())} {int(ncol.y())} {int(ncol.z())}\n')

    sys.stderr.write(f'\nDone.\n')

    with open("img.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii'))
        image.tofile(f)




main()

original_image = Image.open("img.ppm")
original_image.show()

