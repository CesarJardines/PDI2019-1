from PIL import ImageTk, Image
import numpy as np

im= Image.open('image2.jpg')

def convierte(im,carga,matriz,factor,aux):
	width = im.size[0]
	height = im.size[1]
	rgb = im.convert('RGB')
	pixels = carga.load()
	x,y = matriz.shape

	for i in range(width):
		for j in range(height):
			rojo = 0.0
			verde = 0.0
			azul = 0.0
			for k in range(x):
				for l in range (y):
					imageX = (i - x / 2 + k + width) % width
					imageY = (j - y / 2 + l + height) % height
					r,g,b = rgb.getpixel((imageX,imageY))
					valor = matriz.item((k,l))
					rojo += r * valor
					verde += g * valor
					azul += b * valor

			red = min(max((factor * rojo + aux),0),255)
			green = min(max((factor * verde + aux),0),255)
			blue = min(max((factor * azul + aux),0),255)
			pixels[i,j] = (int(red),int(green),int(blue))

	return carga


#im = Image.open('image2.jpg')
#pixeldata = im.load()
matriz = np.matrix([[0,0,1,0,0]
					, [0,1,1,1,0]
					, [1,1,1,1,1]
					, [0,1,1,1,0]
					, [0,0,1,0,0]])
factor = 1.0/13.0
aux = 0.0
img = convierte(im,im,matriz,factor,aux)
#return img

#im= Image.open('image2.jpg')

img.show()