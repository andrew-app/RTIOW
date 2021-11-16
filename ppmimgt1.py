import array
import sys
from PIL import Image, ImageFilter
from flask import Flask
app = Flask(__name__)




@app.route('/')
def draw():
    img_width = 256
    img_height = 256
    max_val = 255

    ppm_h = f'P6 {img_width} {img_height} {max_val}\n'

    


    image = array.array('B', [0, 0, 0] * img_width * img_height)

    index = 0
    for j in range(img_height-1, 0, -1):

        # sys.stderr.write(f'\rScanlines remaining: {j}\n')
        # sys.stderr.flush()

        for i in range(img_width):
            

            ir = i / (img_width - 1)
            ig = j / (img_height - 1)
            ib = 0.25

            r = 255 * ir
            g = 255 * ig
            b = 255 * ib
           

            image[index] = int(r)
            image[index+1] = int(g)
            image[index+2] = int(b)
            index = index + 3
            retval = f'{int(r)} {int(g)} {int(g)}\n'
            return f"{retval}\n"
    # sys.stderr.write(f'\nDone.\n')

    with open("img_t1.ppm", 'wb') as f:
        f.write(bytearray(ppm_h, 'ascii'))
        image.tofile(f)
    

if __name__ == '__main__':
    app.run()



