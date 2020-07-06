import numpy as np
from PIL import Image

im = Image.open('image.jpg')
width, height = im.size 
pixdata = im.load()

for i in range(width):
    for j in range(height):
    	 #im.putpixel( (i, j), (255, 255, 255,) )
    	 r, g, b = im.getpixel((i, j))
    	 value = (255) + (g) + (b)
    	 pixdata[i,j] = (int(value),g,b)

im.save('imagenrojo.png')
im.show() 
