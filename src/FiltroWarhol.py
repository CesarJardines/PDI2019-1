from PIL import ImageTk, Image
import src.TonosGris
import src.FiltroBrillo
import src.FiltroWarhol

import tkMessageBox

def filtroWarhol(imagen,aplica,rojo,verde,azul):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	for i in range(imagen.size[0]):
		for j in range(imagen.size[1]):
			r,g,b = rgb.getpixel((i,j))
			andRojo = (rojo & r)
			andVerde = (verde & g)
			andAzul = (azul & b)
			pixels[3,3] = (andRojo,andVerde,andAzul)
	return aplica