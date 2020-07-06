import numpy as np
from PIL import Image

im = Image.open('image.jpg')
width, height = im.size 
pixdata = im.load()

for i in range(width):
    for j in range(height):
    	 #im.putpixel( (i, j), (255, 255, 255,) )
    	 r, g, b = im.getpixel((i, j))
    	 value = (r) + (255) + (b)
    	 pixdata[i,j] = (r,int(value),b)

im.save('imagenverde.png')
im.show() 
