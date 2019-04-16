import os
import re
from PIL import Image

# sqrt(230401) == 480.0010416655364
IMG_PER_ROW = 480
SHARD_SIZE = 12

glued_img = Image.new('RGBA', (IMG_PER_ROW * SHARD_SIZE, IMG_PER_ROW * SHARD_SIZE))

def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(data, key=alphanum_key)

lst = os.listdir("./Thumbs/")
lst.sort()
lst = sorted_aphanumeric(lst)

i = 0
for filename in lst:
    i += 1
    y_offset = (i // IMG_PER_ROW) * SHARD_SIZE
    x_offset = (i % IMG_PER_ROW) * SHARD_SIZE

    im = Image.open('./Thumbs/' + filename)
    glued_img.paste(im, (x_offset, y_offset))

glued_img.save('glue3.png')