import array
import sys
from PIL import Image, ImageFilter



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

            ir = i / (img_width - 1)
            ig = j / (img_height - 1)
            ib = 0.25

            r = 255 * ir
            g = 255 * ig
            b = 255 * ib
           

            image[index] = int(r)
            image[index+1] = int(g)
            image[index+2] = int(b)
            print(f'{int(r)} {int(g)} {int(g)}\n')

    sys.stderr.write(f'\nDone.\n')

    with open("img_t1.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii'))
        image.tofile(f)




main()

original_image = Image.open("img_t1.ppm")
original_image.show()

