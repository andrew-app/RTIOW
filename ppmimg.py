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

            r = i / (img_width - 1)
            g = j / (img_height - 1)
            b = 0.25

            ir = 255 * r
            ig = 255 * g
            ib = 255 * b
            image[index] = int(ir)
            image[index+1] = int(ig)
            image[index+2] = int(ib)
            print(f'{int(ir)} {int(ig)} {int(ib)}\n')
    sys.stderr.write(f'\nDone.\n')

    with open("img.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii'))
        image.tofile(f)




main()

original_image = Image.open("img.ppm")
original_image.show()

