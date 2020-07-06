import numpy as np
from PIL import Image

im = Image.open('image.jpg')
width, height = im.size 
pixdata = im.load()

for i in range(width):
	for j in range(height):
		red, green, blue = im.getpixel((i, j))
		value = (red + green + blue) / 3
		if value < 127: 
			#red = pixdata[1]
			#green = pixdata[1]
			#blue =  pixdata[1]
			pixdata[i,j]=(255,255,255)
		else:
			#red = pixdata[0]
			#green = pixdata[0]
			#blue = pixdata[0]
			pixdata[i,j] = (0,0,0)


    	#value = (r) + (255) + (b)
			#pixdata[i,j] = (int(red),int(green),int(blue))

im.save('altocontraste.png')
im.show() 
