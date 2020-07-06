import numpy as np
from PIL import ImageTk, Image

#Dithering Floy-Steineerg
def ditheringFloy(imagen,aplica):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	ancho = imagen.size[0]
	alto = imagen.size[1]
	for i in range(alto):
		errorDif = 0
		k = 1
		for j in range(ancho):
			r,g,b = rgb.getpixel((j,i))
			newByte = errorDif + r
			if (newByte >= 255):
				newByte = 255
				pixels[j,i] = (255,255,255)
				errorDif = 0
			elif(newByte <= 0):
				newByte = 0
				pixels[j,i] = (0,0,0)
				errorDif = 0
			elif((255-newByte) > 127):
				pixels[j,i] = (0,0,0)
				k = 1
				errorDif = newByte * k
			else:
				pixels[j,i] = (255,255,255)
				k = -1
				errorDif = 255 - newByte
				errorDif = errorDif * k
	return aplica

#Dithering Jarvis, Judice & Ninke
def ditheringJarvis():
	imageConvert = Image.open('image2.jpg').convert(mode='1',dither=Image.FLOYDSTEINBERG)
	imageConvert.save('DitheringWithPIL.jpg')
	imageConvert.show()

ditheringJarvis()
