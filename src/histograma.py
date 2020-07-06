from __future__ import division
from PIL import ImageTk, Image
import math


def filtroGris1(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
            pixels[i,j] = (gris,gris,gris)
    return aplica

#Pasamos la imagen a tonos de gris para ir contando la ocurrencia de pixeles
def histograma(imagen,aplica):
	hist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	grisImage = filtroGris1(imagen,aplica)
	rgb = grisImage.convert('RGB')
	width = grisImage.size[0]
	hight = grisImage.size[1]
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valor = hist[r]
			valor = valor + 1
			hist[r] = valor
	return hist

def histogramaRojo(imagen,aplica):
	hist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	rgb = imagen.convert('RGB')
	width = imagen.size[0]
	hight = imagen.size[1]
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valor = hist[r]
			valor = valor + 1
			hist[r] = valor
	return hist

def histogramaAzul(imagen,aplica):
	hist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	rgb = imagen.convert('RGB')
	width = imagen.size[0]
	hight = imagen.size[1]
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valor = hist[b]
			valor = valor + 1
			hist[b] = valor
	return hist

def histogramaVerde(imagen,aplica):
	hist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	rgb = imagen.convert('RGB')
	width = imagen.size[0]
	hight = imagen.size[1]
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valor = hist[g]
			valor = valor + 1
			hist[g] = valor
	return hist

def sumaHistograma(hist):
	nuevoHist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	nuevoHist[0] = hist[0]
	for i in range(1,len(hist)):
		valor1 = nuevoHist[i-1]
		valor2 = hist[i]
		suma = valor1 + valor2
		nuevoHist[i] = suma
	return nuevoHist

#filtros de histogramas
def ajuste(imagen,aplica):
	hist = histograma(imagen,aplica)
	minimo = min(hist)
	maximo = max(hist)
	factor = maximo - minimo
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	width = imagen.size[0]
	hight = imagen.size[1]
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valor = hist[r]
			op = ((valor-minimo)/factor)*256
			resultado = (int)(math.floor(op))
			pixels[i,j] = (resultado,resultado,resultado)
	aplica.show()

def ajusteColor(imagen,aplica):
	
	histRojo = histogramaRojo(imagen,aplica)
	minimoRojo = min(histRojo)
	maximoRojo = max(histRojo)
	factorRojo = (maximoRojo - minimoRojo) 

	histAzul = histogramaAzul(imagen,aplica)
	minimoAzul = min(histAzul)
	maximoAzul = max(histAzul)
	factorAzul = (maximoAzul - minimoAzul) 

	histVerde = histogramaVerde(imagen,aplica)
	minimoVerde = min(histVerde)
	maximoVerde = max(histVerde)
	factorVerde = (maximoVerde - minimoVerde)
	
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	width = imagen.size[0]
	hight = imagen.size[1]
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valorRojo = histRojo[r]
			valorVerde = histVerde[g]
			valorAzul = histAzul[b]
			opRojo = ((valorRojo - minimoRojo)/factorRojo)*256
			resultadoRojo = (int)(math.floor(opRojo))
			opVerde = ((valorVerde - minimoVerde)/factorVerde)*256
			resultadoVerde = (int)(math.floor(opVerde))
			opAzul = ((valorAzul - minimoAzul)/factorAzul)*256
			resultadoAzul = (int)(math.floor(opAzul))
			pixels[i,j] = (resultadoRojo,resultadoVerde,resultadoAzul)
	aplica.show()

def ecualizacion(imagen,aplica):
	hist = histograma(imagen,aplica)
	nuevoHist = sumaHistograma(hist)
	minimo = min(nuevoHist)
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	width = imagen.size[0]
	hight = imagen.size[1]
	factor = (hight * width) - 1
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valor = nuevoHist[r]
			op = ((valor - minimo)/factor)*256
			resultado = (int)(math.floor(op))
			pixels[i,j] = (resultado,resultado,resultado)
	aplica.show()

def ecualizacionColor(imagen,aplica):
	histRojo = histogramaRojo(imagen,aplica)
	nuevoHistRojo = sumaHistograma(histRojo)
	minimoRojo = min(histRojo)
	
	histAzul = histogramaAzul(imagen,aplica)
	nuevoHistAzul = sumaHistograma(histAzul)
	minimoAzul = min(histAzul)
	
	histVerde = histogramaVerde(imagen,aplica)
	nuevoHistVerde = sumaHistograma(histVerde)
	minimoVerde = min(histVerde)
	
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	width = imagen.size[0]
	hight = imagen.size[1]
	factor = (hight * width) - 1
	
	for i in range(width):
		for j in range(hight):
			r,g,b = rgb.getpixel((i,j))
			valorRojo = nuevoHistRojo[r]
			valorVerde = nuevoHistVerde[g]
			valorAzul = nuevoHistAzul[b]
		 
			opRojo = ((valorRojo - minimoRojo)/factor)*256
			resultadoRojo = (int)(math.floor(opRojo))
			opVerde = ((valorVerde - minimoVerde)/factor)*256
			resultadoVerde = (int)(math.floor(opVerde))
			opAzul = ((valorAzul - minimoAzul)/factor)*256
			resultadoAzul = (int)(math.floor(opAzul))
			pixels[i,j] = (resultadoRojo,resultadoVerde,resultadoAzul)
	
	aplica.show()

image = Image.open("image2.jpg")

ecualizacionColor(image, image)
ecualizacion(image, image)
ajusteColor(image, image)
ajuste(image, image)















