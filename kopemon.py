import sys
from PIL import Image

resolutions = sys.argv[1].split(",")

monitors = [
    tuple(map(int, res.split("x"))) for res in resolutions
]

image = Image.open(sys.argv[2])
images = [image for monitor in monitors]

width = 0
height = 0

i = 0

while i < len(monitors):
    (mon_width, mon_height) = monitors[i]
    images[i] = image.resize((mon_width, mon_height), Image.ANTIALIAS) 
    width += mon_width
    if mon_height > height:
        height = mon_height
    i += 1

new_img = Image.new(mode='RGBA', size=(width, height))

x_offset = 0

for im in images:
    new_img.paste(im, (x_offset, 0))
    x_offset += im.size[0]

new_img.save("output.png")
