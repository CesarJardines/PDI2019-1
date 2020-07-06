from PIL import ImageTk, Image

def filtroGris1(imagen,aplica):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	for i in range(imagen.size[0]):
		for j in range(imagen.size[1]):
			r,g,b = rgb.getpixel((i,j))
			gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
			pixels[i,j] = (gris,gris,gris)
	return aplica

def filtroAltoContraste(imagen,aplica):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	for i in range(imagen.size[0]):
		for j in range(imagen.size[1]):
			r,g,b = rgb.getpixel((i,j))
			prom = (r+g+b)/3
			if prom >= 128:
				prom  = 255
			elif prom < 128:
				prom = 0
			pixels[i,j] = (prom,prom,prom)
	return aplica

"""
Se pasa a tono de gris la imagen
Luego esa imagen la pasamos a blanco y negro
Dividimos la imagen en renglones
Por cada renglon ahora se recorre por columnas
Se cuenta los pixeles negros de cada columna
Luego se colocan esos pixeles pero desde en medio a los costados
"""
def filtroAtt(imagen,aplica,tam):
	imgGris = filtroGris1(imagen,aplica)
	imgBN = filtroAltoContraste(imgGris,aplica)
	ancho = imagen.size[0]
	alto = imagen.size[1]
	nuevoAlto = alto - tam
	rgb = imgBN.convert('RGB')
	pixels = aplica.load()
	for i in range(ancho):
		for j in range(0,nuevoAlto,tam):
			negros = 0
			salto = j + tam
			for k in range(j,salto):
				r,g,b = rgb.getpixel((i,k))
				if(r == 0):
					negros += 1
			lista = puntosAcumulados(tam,negros)
			for k in range(j,salto):
				if(lista[k-j] == True):
					pixels[i,k] = (0,0,0)
				else:
					pixels[i,k] = (255,255,255)
	#return aplica
	aplica.show()
"""
Funcion para guardar los pixeles negros de la imagen
Se crea una lista del tamanio de la columna que se esta recorriendo en la imagen
Se van guardando de en medio hasta los costados
"""
def puntosAcumulados(tam,pix):
	lista = [None] * tam
	n = pix/2
	if(pix % 2 == 0):
		m = n-1
	else:
		m = n
	inicia = (tam/2)-n
	termina = (tam/2)+m
	for i in range(inicia,termina):
		lista[i] = True
	return lista

im = Image.open("image2.jpg")

nuevaImagen = filtroAtt(im,im,20)
imageAplica = ImageTk.PhotoImage(nuevaImagen)
image = imageAplica
create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")








