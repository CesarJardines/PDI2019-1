from __future__ import division
from Tkinter import *
from Tkinter import Label,Tk
from PIL import Image, ImageTk, ImageFilter, ImageFont, ImageDraw

import tkFileDialog
import os
import numpy as np
import tkMessageBox
import PIL.Image
import math




ventana = Tk()
ventana.geometry("1000x700")
ventana.title("Menus")
#PILFile = Image.open("image2.jpg")
Imagen = ImageTk.PhotoImage(Image.open('image2.jpg'))
imagenL = Imagen
lblImagen=Label(ventana, image=imagenL).place(x=10,y=10)

'''
Funciones que se encargan de cargar la imagen 
'''
def azul():
	im = Image.open('image2.jpg')
	width, height = im.size 
	pixdata = im.load()

	for i in range(width):
		for j in range(height):
			#im.putpixel( (i, j), (255, 255, 255,) )
			r, g, b = im.getpixel((i, j))
			value = (r) + (g) + (255)
			pixdata[i,j] = (r,g,int(value))

	#im.save('imagenazul.png')
	im.show() 

def verde():
	im = Image.open('image2.jpg')
	width, height = im.size 
	pixdata = im.load()

	for i in range(width):
		for j in range(height):
			#im.putpixel( (i, j), (255, 255, 255,) )
			r, g, b = im.getpixel((i, j))
			value = (r) + (255) + (b)
			pixdata[i,j] = (r,int(value),b)

	#im.save('imagenverde.png')
	im.show() 

def rojo():
	im = Image.open('image2.jpg')
	width, height = im.size 
	pixdata = im.load()

	for i in range(width):
		for j in range(height):
			#im.putpixel( (i, j), (255, 255, 255,) )
			r, g, b = im.getpixel((i, j))
			value = (255) + (g) + (b)
			pixdata[i,j] = (int(value),g,b)

	#im.save('imagenrojo.png')
	im.show() 

'''
Todas estas funciones son auxiliares para escala_grises
'''

#Conseguimos cada pixel de la imagen
def get_pixel(image, i, j):
	#obtenemos el tamano total de la imagen
	width, height = image.size
	if i > width or j > height:
		return None
	pixel = image.getpixel((i, j))
	return pixel

#Creamos la imagen con la cantidad de pixeles dados
def crear_imagen(i, j):
	image = Image.new("RGB", (i, j), "white")
	return image

#ESCALA DE GRISES
#Se crea la imagen a escala de grises usando la formula (R+G+B)/3 o bien 
#dandole valores aleatorios que no rebasen el limite



def escala_grises():
	im = Image.open('image2.jpg')
	width, height = im.size

	#Creamos la nueva imagen a escala 
	new = crear_imagen(width, height)
	#Cargamos los pixeles obtenidos anteriormente 
	pixels = new.load()

	#Recorremos la imagen con un for anidado 
	for i in range(width):
		for j in range(height):
			pixel = get_pixel(im, i, j)

			#Obtenemos los valores Rojo Verde y Azul.   
			rojo =   pixel[0]
			verde = pixel[0]
			azul =  pixel[0]

			#x=(R * .n + G * .m + B * .x)
			gray = (rojo * 0.3) + (verde * 0.59) + (azul * 0.11)

			#Ponemos nuevos pixeles en la imagen 
			pixels[i, j] = (int(gray), int(gray), int(gray))
	#Regresamos la nueva imagen

	return new
	

def altoConttraste():

	im = Image.open('image2.jpg')
	width, height = im.size 
	pixdata = im.load()

	for i in range(width):
		for j in range(height):
			red, green, blue = im.getpixel((i, j))
			value = (red + green + blue) / 3
			if value < 127: 
				pixdata[i,j]=(255,255,255)
			else:
				pixdata[i,j] = (0,0,0)


	#im.save('altocontraste.png')
	im.show() 

def inverso():
	im = Image.open('image2.jpg')
	width, height = im.size 
	pixdata = im.load()

	for i in range(width):
		for j in range(height):
			red, green, blue = im.getpixel((i, j))
			value = (red + green + blue) / 3
			if value > 127: 
				pixdata[i,j]=(255,255,255)
			else:
				pixdata[i,j] = (0,0,0)

	#im.save('inverso.png')
	im.show() 

'''
El valor de x y y para mosaico esta establecido predeterminadamente Por que...
por que ya no me dio tiempo de hacer mas robusta la interfaz jajaja me entere 
que esta cosa tenia que ser ya con interfaz por eso me tarde en entregarla :((
yo todo feliz pensando que era solo los archivos de python
'''
def mosaico():
	im = Image.open("image2.jpg")
	recorreX = 0
	recorreY = 0
	rprom = 0
	gprom = 0
	bprom = 0
	prom = 0
	ancho = im.size[0]
	alto = im.size[1]
	rgb = im.convert('RGB')
	pixels = im.load()
	for i in range(0,ancho,3):
		recorreX = i + 3
		for j in range(0,alto,3):
			recorreY = j + 3
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					r,g,b = rgb.getpixel((k,l))
					rprom += r
					gprom += g
					bprom += b
					prom += 1
			promRojo = (rprom/prom)
			promVerde = (gprom/prom)
			promAzul = (bprom/prom)
			rprom = 0
			gprom = 0
			bprom = 0
			prom = 0
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					pixels[k,l] = (promRojo,promVerde,promAzul)
	#im.show()   
	return im

'''
Funcion que se encarga de mostrar la imagen de mosaico al usuario
'''
def mostrarMosaico():
	mosaico().show()

def mostrarGrises():
	escala_grises().show()



	
'''
Funcion auxiliar que se encarga de acceder a los valores de la imagen 
esta funcion auxiliar es exclusiva para los filtros de convolucion 
-Blur, Motion Blur-
'''
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


#Este filtro tarda un poco en dar la imagen resultante 
def blur():
	im = Image.open('image2.jpg')
	matriz = np.matrix([[0,0,1,0,0]
					, [0,1,1,1,0]
					, [1,1,1,1,1]
					, [0,1,1,1,0]
					, [0,0,1,0,0]])
	factor = 1.0/13.0
	aux = 0.0
	img = convierte(im,im,matriz,factor,aux)
	img.show()

#Este filtro tarda un poco en dar la imagen resultante 
def motionBlur():
	im= Image.open('image2.jpg')
	matriz = np.matrix([[1,0,0,0,0,0,0,0,0]
					, [0,1,0,0,0,0,0,0,0]
					, [0,0,1,0,0,0,0,0,0]
					, [0,0,0,1,0,0,0,0,0]
					, [0,0,0,0,1,0,0,0,0]
					, [0,0,0,0,0,1,0,0,0]
					, [0,0,0,0,0,0,1,0,0]
					, [0,0,0,0,0,0,0,1,0]
					, [0,0,0,0,0,0,0,0,1]])
	factor = 1.0/9.0
	aux = 0.0
	img = convierte(im,im,matriz,factor,aux)
	img.show();

def encuentraBordes():
	im = image.open('image2.jpg')
	'''
	Los valores que se tomaron como referencia en la matriz se sacaron de la 
	pagina de filtros que se vio en clase
	'''
	matriz = np.matrix([[0,0,-1,0,0]
					, [0,0,-1,0,0]
					, [0,0, 2,0,0]
					, [0,0, 0,0,0]
					, [0,0, 0,0,0]])
	factor = 1.0
	aux = 0.0
	img = convierte(im,im,matriz,factor,aux)
	img.show()

def sharpen():
	im= Image.open('image2.jpg')
	matriz = np.matrix([[-1,-1,-1]
					, [-1, 9,-1]
					, [-1,-1,-1]])
	factor = 1.0
	aux = 0.0
	img = convierte(im,im,matriz,factor,aux)
	img.show()

def emboss():
	im= Image.open('image2.jpg')
	matriz = np.matrix([[-1,-1, 0]
					, [-1, 0, 1]
					, [ 0, 1, 1]])
	factor = 1.0
	aux = 128.0
	img = convierte(im,im,matriz,factor,aux)
	img.show()

def mediano():
	im = Image.open('image2.jpg')
	members = [(0,0)] * 9
	width = im.size[0]
	height = im.size[1]
	for i in range(1,width-1):
		for j in range(1,height-1):
			members[0] = im.getpixel((i-1,j-1))
			members[1] = im.getpixel((i-1,j))
			members[2] = im.getpixel((i-1,j+1))
			members[3] = im.getpixel((i,j-1))
			members[4] = im.getpixel((i,j))
			members[5] = im.getpixel((i,j+1))
			members[6] = im.getpixel((i+1,j-1))
			members[7] = im.getpixel((i+1,j))
			members[8] = im.getpixel((i+1,j+1))
			members.sort()
			im.putpixel((i,j),(members[4]))
	im.show()
'''
Hacer bien el menu para que se vea chido
'''
def colorSinLetras():
	im = Image.open('image2.jpg')
	filmosaico = mosaico()
	height = filmosaico.size[0]
	width = filmosaico.size[1]
	rgb = filmosaico.convert('RGB')
	image = open('mariposaColor.html','w')
	for i in range(width):
		for j in range(height):
			r,g,b = rgb.getpixel((j,i))
			image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">@</font>')
		image.write('<br>')
	image.close()

def tonoDeGris():
	im = Image.open('image2.jpg')
	filmosaico = mosaico()
	height = filmosaico.size[0]
	width = filmosaico.size[1]
	rgb = filmosaico.convert('RGB')
	image = open('mariposaGris.html','w')
	for i in range(width):
		for j in range(height):
			r,g,b = rgb.getpixel((j,i))
			image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">@</font>')
		image.write('<br>')
	image.close()

def masColorMenosColor():
	filgris = escala_grises()
	height = filgris.size[0]
	width = filgris.size[1]
	rgb = filgris.convert('RGB')
	image = open('MariposaMasMenosOscuro.html','w')
	image.write("<PRE>")
	for i in range(width):
		for j in range(height):
			r,g,b = rgb.getpixel((j,i))
			if(r >= 0 and r < 16):
				image.write('<font size="1">M</font>')
			elif(r >= 16 and r < 32):
				image.write('<font size="1">N</font>')
			elif(r >= 32 and r < 48):
				image.write('<font size="1">H</font>')
			elif(r >= 48 and r < 64):
				image.write('<font size="1">#</font>')
			elif(r >= 64 and r < 80):
				image.write('<font size="1">Q</font>')
			elif(r >= 80 and r < 96):
				image.write('<font size="1">U</font>')
			elif(r >= 96 and r < 112):
				image.write('<font size="1">A</font>')
			elif(r >= 112 and r < 128):
				image.write('<font size="1">D</font>')
			elif(r >= 128 and r < 144):
				image.write('<font size="1">O</font>')
			elif(r >= 144 and r < 160):
				image.write('<font size="1">Y</font>')
			elif(r >= 160 and r < 176):
				image.write('<font size="1">2</font>')
			elif(r >= 176 and r < 192):
				image.write('<font size="1">$</font>')
			elif(r >= 192 and r < 208):
				image.write('<font size="1">%</font>')
			elif(r >= 208 and r < 224):
				image.write('<font size="1">+</font>')
			elif(r >= 224 and r < 240):
				image.write('<font size="1">-</font>')
			elif(r >= 240 and r < 256):
				image.write('<font size="1">M</font>')
		image.write('<br>')
	image.close()

def MasMenosGris():
	#filmosaico = mosaico()
	filescalaGrises = escala_grises()
	height = filescalaGrises.size[0]
	width = filescalaGrises.size[1]
	rgb = filescalaGrises.convert('RGB')
	image = open('MariposaMasMenosGris.html','w')
	image.write("<PRE>")
	for i in range(width):
		for j in range(height):
			r,g,b = rgb.getpixel((j,i))
			if(r >= 0 and r < 16):
				image.write('<font size="1">M</font>')
			elif(r >= 16 and r < 32):
				image.write('<font size="1">N</font>')
			elif(r >= 32 and r < 48):
				image.write('<font size="1">H</font>')
			elif(r >= 48 and r < 64):
				image.write('<font size="1">#</font>')
			elif(r >= 64 and r < 80):
				image.write('<font size="1">Q</font>')
			elif(r >= 80 and r < 96):
				image.write('<font size="1">U</font>')
			elif(r >= 96 and r < 112):
				image.write('<font size="1">A</font>')
			elif(r >= 112 and r < 128):
				image.write('<font size="1">D</font>')
			elif(r >= 128 and r < 144):
				image.write('<font size="1">O</font>')
			elif(r >= 144 and r < 160):
				image.write('<font size="1">Y</font>')
			elif(r >= 160 and r < 176):
				image.write('<font size="1">2</font>')
			elif(r >= 176 and r < 192):
				image.write('<font size="1">$</font>')
			elif(r >= 192 and r < 208):
				image.write('<font size="1">%</font>')
			elif(r >= 208 and r < 224):
				image.write('<font size="1">+</font>')
			elif(r >= 224 and r < 240):
				image.write('<font size="1">-</font>')
			elif(r >= 240 and r < 256):
				image.write('<font size="1">M</font>')
		image.write('<br>')
	image.close()


'''
NO 1 + 3
'''
def filtroGris1(imagen):
	im = Image.open('image2.jpg')
	rgb = imagen.convert('RGB')
	pixels = im.load()
	for i in range(imagen.size[0]):
		for j in range(imagen.size[1]):
			r,g,b = rgb.getpixel((i,j))
			gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
			pixels[i,j] = (gris,gris,gris)
	return im

def filtroMosaico(imagen,mosX,mosY):
	im = Image.open('image2.jpg')
	recorreX = 0
	recorreY = 0
	rprom = 0
	gprom = 0
	bprom = 0
	prom = 0
	ancho = imagen.size[0]
	alto = imagen.size[1]
	rgb = imagen.convert('RGB')
	pixels = im.load()
	for i in range(0,ancho,mosX):
		recorreX = i + mosX
		for j in range(0,alto,mosY):
			recorreY = j + mosY
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					r,g,b = rgb.getpixel((k,l))
					rprom += r
					gprom += g
					bprom += b
					prom += 1
			promRojo = (rprom/prom)
			promVerde = (gprom/prom)
			promAzul = (bprom/prom)
			rprom = 0
			gprom = 0
			bprom = 0
			prom = 0
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					pixels[k,l] = (promRojo,promVerde,promAzul)
	   
	return im

def masMenosColor():
	im = Image.open('image2.jpg')
	mosaico = filtroMosaico(im,15,15)
	rgbMos = mosaico.convert('RGB')
	anchoM = mosaico.size[0]
	altoM = mosaico.size[1]

	gris = filtroGris1(mosaico)
	height2 = gris.size[0]
	width2 = gris.size[1]
	#grisrgb = gris.convert('RGB')
	grisA = Image.open('image2.jpg')
	image = open('MariposaMasMenosColor.html','w')
	image.write("<PRE>")
	for i in range(height2):
		for j in range(width2):
			rg,gg,bg = grisA.getpixel((j,i))
			r,g,b = rgbMos.getpixel((j,i))
			if(rg >= 0 and rg < 16):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>M</font>')
			elif(rg >= 16 and rg < 32):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>N</font>')
			elif(rg >= 32 and rg < 48):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>H</font>')
			elif(rg >= 48 and rg < 64):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>#</font>')
			elif(rg >= 64 and rg < 80):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>Q</font>')
			elif(rg >= 80 and rg < 96):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>U</font>')
			elif(rg >= 96 and rg < 112):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>A</font>')
			elif(rg >= 112 and rg < 128):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>D</font>')
			elif(rg >= 128 and rg < 144):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>O</font>')
			elif(rg >= 144 and rg < 160):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>Y</font>')
			elif(rg >= 160 and rg < 176):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>2</font>')
			elif(rg >= 176 and rg < 192):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>$</font>')
			elif(rg >= 192 and rg < 208):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>%</font>')
			elif(rg >= 208 and rg < 224):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>+</font>')
			elif(rg >= 224 and rg < 240):
				image.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');>-</font>')
			elif(rg >= 240 and rg < 256):
				image.write('<font size="1" style="color:rgb(0,0,0);">M</font>')
		image.write('<br>')
	image.close()
'''
La palabra se da por default y es Prueba ProcesoDI
'''
def palabra():
	im = Image.open('image2.jpg')
	cadena = "Prueba ProcesoDI "
	mosaico = filtroMosaico(im,15,15)
	width = mosaico.size[0]
	height = mosaico.size[1]
	contador = 0;
	rgb = mosaico.convert('RGB')
	f = open('CADENA.html','w')
	f.write("<PRE>")
	for i in range(height):
		for j in range(width):
			r,g,b = rgb.getpixel((j,i))
			if(contador < len(cadena)):
				f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">'+cadena[contador]+'</font>')
				contador = contador + 1
			else:
				contador = 0
				f.write('<font size="1" style="color:rgb('+str(r)+','+str(g)+','+str(b)+');">'+cadena[contador]+'</font>')
				contador = contador + 1
		f.write('<br>')
	f.close()

def cartaNaipes():
	im = Image.open('image2.jpg')
	mosaico = filtroMosaico(im,15,15)
	gris = filtroGris1()
	ancho = gris.size[0]
	alto = gris.size[1]
	rgb = gris.convert('RGB')
	image = open('Cartas.html','w')
	image.write("<PRE><style>@font-face{font-family: 'Playcrds';src: url('dominos-cartas_FILES/Playcrds.TTF') format('truetype');}font{font-family: 'Playcrds'}</style>")
	for i in range(alto):
		for j in range(ancho):
			r,g,b = rgb.getpixel((j,i))
			if(r >= 0 and r < 19):
				image.write('<font size="1">A</font>')
			elif(r >= 19 and r < 38):
				image.write('<font size="1">B</font>')
			elif(r >= 38 and r < 57):
				image.write('<font size="1">C</font>')
			elif(r >= 57 and r < 76):
				image.write('<font size="1">D</font>')
			elif(r >= 76 and r < 95):
				image.write('<font size="1">E</font>')
			elif(r >= 95 and r < 114):
				image.write('<font size="1">F</font>')
			elif(r >= 114 and r < 133):
				image.write('<font size="1">G</font>')
			elif(r >= 133 and r < 152):
				image.write('<font size="1">H</font>')
			elif(r >= 152 and r < 171):
				image.write('<font size="1">I</font>')
			elif(r >= 171 and r < 190):
				image.write('<font size="1">J</font>')
			elif(r >= 190 and r < 209):
				image.write('<font size="1">K</font>')
			elif(r >= 209 and r < 228):
				image.write('<font size="1">L</font>')
			elif(r >= 228 and r < 256):
				image.write('<font size="1">M</font>')
		image.write('<br>')
	image.close()

#Funcion auxiliar de maximo
def maximoAuxConvert(imagen):
	return imagen.filter(ImageFilter.MaxFilter);

def maximo():
	#Cargamos la imagen desde donde se encutra la interfaz
	image   = "image2.jpg";
	imageFil = Image.open(image);

	#Iteramos aplicando el filtro maximo
	imagenFiltroMaximo = imageFil;
	for i in range(0, 10):
		print(i);
		imagenFiltroMaximo = maximoAuxConvert(imagenFiltroMaximo);

	#imageFil.show();
	imagenFiltroMaximo.show();

#Funcion auxiliar para filtro minimo
def minimoAuxConverter(imagen):
	return imagen.filter(ImageFilter.MinFilter)

def minimo():
	image = "image2.jpg"
	imageFil = Image.open(image)

	imagenFiltroMinimo = imageFil
	filtroMinimo = minimoAuxConverter(imagenFiltroMinimo)

	filtroMinimo.show()

#funcion auxiliar de marca de agua
def marcaDeAguaAux(imagen, imageDescription, textSize, textX, textY, font):
	imagen = imagen.convert('RGBA');   
	textImage = Image.new('RGBA', imagen.size, (255,255,255,0));
	# Select a font for the text
	font = ImageFont.truetype(font, textSize);
	draw = ImageDraw.Draw(textImage);
	draw.text((textX,textY), imageDescription, font=font, fill=(255,0,0,255));
	# Do an alpha composite of the two images and return
	return Image.alpha_composite(imagen, textImage);   

def marcaDeAgua():
	textSize = 50;
	textX    = 10;
	textY    = 30;
	font    = "/opt/X11/share/fonts/TTF/luxirr.ttf";
	imageFilePath       = "./image2.jpg";
	imageText           = "Marca de agua";
	# Create an image object from a file
	imageInstance = Image.open(imageFilePath);
	MarcaImagen = marcaDeAguaAux(imageInstance, imageText, textSize, textX, textY, font);
	MarcaImagen = marcaDeAguaAux(imageInstance, imageText, textSize, 400, 200, font);
	MarcaImagen.show();


"""
Funcion para generar las imagenes en tono de gris con distinto brillo
"""
def generaImagenesGris(imagen,aplica):
	gris = filtroGris1(imagen,aplica)
	brillo = -128
	contador = 1
	while(brillo < 129):
		im = filtroBrillo(gris,imagen,brillo)
		im.save("imagen"+str(contador)+".png","PNG")
		brillo = brillo + 9
		contador = contador + 1

"""
Funcion para eliminar las imagenes generadas
"""
def eliminaImagenesGris():
	for i in range(1,30):
		os.remove("imagen"+str(i)+".png")

"""
Funcion para crear una imagen a partir de la misma imagen
Se saca el filtro mosaico y se verifica que imagen colocar
Dependiendo del valor del promedio
"""
def aplicaRecursivaGris(imagen,aplica,mosX,mosY):
	gris = filtroGris1(imagen,aplica)
	size = mosX,mosY
	posX = 0
	posY = 0
	recorreX = 0
	recorreY = 0
	grisProm = 0
	promedio = 0
	ancho = gris.size[0]
	alto = gris.size[1]
	rgb = gris.convert('RGB')
	pixels = aplica.load()
	for i in range(0,ancho,mosX):
		recorreX = i + mosX
		for j in range(0,alto,mosY):
			recorreY = j + mosY
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					r,g,b = rgb.getpixel((k,l))
					grisProm += r
					promedio += 1
			promRec = (grisProm/promedio)
			grisProm = 0
			promedio = 0
			if(promRec >= 0 and promRec < 9):
				img = PIL.Image.open('imagen1.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 9 and promRec < 18):
				img = PIL.Image.open('imagen2.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 18 and promRec < 27):
				img = PIL.Image.open('imagen3.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 27 and promRec < 36):
				img = PIL.Image.open('imagen4.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 36 and promRec < 45):
				img = PIL.Image.open('imagen5.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 45 and promRec < 54):
				img = PIL.Image.open('imagen6.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 54 and promRec < 63):
				img = PIL.Image.open('imagen7.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 63 and promRec < 72):
				img = PIL.Image.open('imagen8.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 72 and promRec < 81):
				img = PIL.Image.open('imagen9.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 81 and promRec < 90):
				img = PIL.Image.open('imagen10.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 90 and promRec < 99):
				img = PIL.Image.open('imagen11.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 99 and promRec < 108):
				img = PIL.Image.open('imagen12.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 108 and promRec < 117):
				img = PIL.Image.open('imagen13.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 117 and promRec < 126):
				img = PIL.Image.open('imagen14.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 126 and promRec < 135):
				img = PIL.Image.open('imagen15.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 135 and promRec < 144):
				img = PIL.Image.open('imagen16.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 144 and promRec < 153):
				img = PIL.Image.open('imagen17.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 153 and promRec < 162):
				img = PIL.Image.open('imagen18.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 162 and promRec < 171):
				img = PIL.Image.open('imagen19.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 171 and promRec < 180):
				img = PIL.Image.open('imagen20.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 180 and promRec < 189):
				img = PIL.Image.open('imagen21.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 189 and promRec < 198):
				img = PIL.Image.open('imagen22.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 198 and promRec < 207):
				img = PIL.Image.open('imagen23.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 207 and promRec < 216):
				img = PIL.Image.open('imagen24.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 216 and promRec < 225):
				img = PIL.Image.open('imagen25.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 225 and promRec < 234):
				img = PIL.Image.open('imagen26.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 234 and promRec < 243):
				img = PIL.Image.open('imagen27.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 243 and promRec < 252):
				img = PIL.Image.open('imagen28.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 252 and promRec < 256):
				img = PIL.Image.open('imagen29.png')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			posY += mosY
		posX += mosX
		posY = 0
	return aplica

"""
Generamos el filtro mosaico
Por cada mosaico creamos una mica para aplicarsela a la imagen original
La imagen resultante la ponemos en la zona del mosaico que esta recorriendo
"""

def aplicaRecursivaColor(imagen,aplica,mosX,mosY):
	size = mosX,mosY
	posX = 0
	posY = 0
	recorreX = 0
	recorreY = 0
	rprom = 0
	gprom = 0
	bprom = 0
	promedio = 0
	ancho = imagen.size[0]
	alto = imagen.size[1]
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	for i in range(0,ancho,mosX):
		recorreX = i + mosX
		for j in range(0,alto,mosY):
			recorreY = j + mosY
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					r,g,b = rgb.getpixel((k,l))
					rprom += r
					gprom += g
					bprom += b
					promedio += 1
			promRojo = (rprom/promedio)
			promVerde = (gprom/promedio)
			promAzul = (bprom/promedio)
			rprom = 0
			gprom = 0
			bprom = 0
			promedio = 0
			pinta = PIL.Image.new('RGB',(500,500))
			img = filtroWarhol(imagen,pinta,promRojo,promVerde,promAzul)
			img = img.resize(size)
			aplica.paste(img,(posX,posY))
			posY += mosY
		posX += mosX
		posY = 0
	aplica.show()

def crear_imagen2(i, j):
	image = Image.new("RGB", (i, j))
	return image
	
def filtroGris1(imagen,aplica):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	for i in range(imagen.size[0]):
		for j in range(imagen.size[1]):
			r,g,b = rgb.getpixel((i,j))
			gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
			pixels[i,j] = (gris,gris,gris)
	return aplica

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

def filtroBrillo(imagen,aplica,entrada):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()
	brillo = entrada
	if brillo >= -128 and brillo <= 128:
		for i in range(imagen.size[0]):
			for j in range(imagen.size[1]):
				r,g,b = rgb.getpixel((i,j))
				r = r+brillo
				g = g+brillo
				b = b+brillo
				r = min(max(r,0),255)
				g = min(max(g,0),255)
				b = min(max(b,0),255)
				pixels[i,j] = (r,g,b)
		return aplica
	else:
		tkMessageBox.showwarning("Error","Escoge un valor valido entre -128 y 128")
		return aplica

def recursiveColor():
	im = Image.open("image2.jpg")
	width, height = im.size
	new = crear_imagen2(width,height)
	#Aqui puedes cambiar los valores de 30
	aplicaRecursivaColor(im,im,5,5)

def recursiveGray():
	im = Image.open("image2.jpg")
	width, height = im.size
	new = crear_imagen2(width,height)
	#Aqui puedes cambiar los valores de 30 
	aplicaRecursivaGris(im,im,30,30)

#Metodo que juega con encontraste de pixeles rojos
def contrasteRojo(intensity):
	iI = intensity
	minI = 86
	maxI = 230
	minO = 0
	maxO = 255
	salidaContraste = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
	return salidaContraste

#Metodo que juega con encontraste de pixeles verde
def contrasteVerde(intensity):
	iI = intensity
	minI = 90
	maxI = 225
	minO = 0
	maxO = 255
	salidaContraste = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
	return salidaContraste

def contrasteAzul(intensity):
	iI = intensity
	minI = 100
	maxI = 210
	minO = 0
	maxO = 255
	salidaContraste = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
	return salidaContraste	

def contrasteHS():
	imageObject = Image.open("./image2.jpg")
	#Hacemos la operacion de la formula vista en clase (Salida = (Ii-Mini)*(((Maxo-Mino)/(Maxi-Mini))+Mino))
	multiBands = imageObject.split()
	#Normalizamos todos los colores
	normalizedRedBand = multiBands[0].point(contrasteRojo)
	normalizedGreenBand = multiBands[1].point(contrasteVerde)
	normalizedBlueBand = multiBands[2].point(contrasteAzul)
	#creamos la nueva imagen con los pixeles de contraste 
	normalizedImage = Image.merge("RGB", (normalizedRedBand, normalizedGreenBand, normalizedBlueBand))
	normalizedImage.show()

def semitonos9Cuad(imagen,aplica,mosX,mosY):
	gris = filtroGris1(imagen,aplica)
	size = mosX,mosY
	posX = 0
	posY = 0
	recorreX = 0
	recorreY = 0
	grisProm = 0
	promedio = 0
	ancho = gris.size[0]
	alto = gris.size[1]
	rgb = gris.convert('RGB')
	pixels = aplica.load()
	for i in range(0,ancho,mosX):
		recorreX = i + mosX
		for j in range(0,alto,mosY):
			recorreY = j + mosY
			for k in range(i,recorreX):
				if (k >= ancho):
					break
				for l in range(j,recorreY):
					if (l >= alto):
						break
					r,g,b = rgb.getpixel((k,l))
					grisProm += r
					promedio += 1
			promRec = (grisProm/promedio)
			grisProm = 0
			promedio = 0
			if(promRec >= 0 and promRec < 25):
				img = PIL.Image.open('semitonos/9cuad/9.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 25 and promRec < 50):
				img = PIL.Image.open('semitonos/9cuad/8.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 50 and promRec < 75):
				img = PIL.Image.open('semitonos/9cuad/7.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 75 and promRec < 100):
				img = PIL.Image.open('semitonos/9cuad/6.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 100 and promRec < 125):
				img = PIL.Image.open('semitonos/9cuad/5.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 125 and promRec < 150):
				img = PIL.Image.open('semitonos/9cuad/4.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 150 and promRec < 175):
				img = PIL.Image.open('semitonos/9cuad/3.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 175 and promRec < 200):
				img = PIL.Image.open('semitonos/9cuad/2.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 200 and promRec < 225):
				img = PIL.Image.open('semitonos/9cuad/1.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			elif(promRec >= 225 and promRec < 255):
				img = PIL.Image.open('semitonos/9cuad/0.jpg')
				img = img.resize(size)
				aplica.paste(img,(posX,posY))
			posY += mosY
		posX += mosX
		posY = 0
	#return aplica
	imagen.show()

def semitonos():
	im = Image.open("image2.jpg")
	#width, height = im.size
	#new = crear_imagen2(width,height)

	nuevaImagen = semitonos9Cuad(im,im,30,30)
	imageAplica = ImageTk.PhotoImage(nuevaImagen)
	image = imageAplica
	create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

#Funcion auxiliar del filtro ATT
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

#Se crea una lista del tamanio de la columna que se esta recorriendo en la imagen
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
	aplica.show()

def ATT():
	im = Image.open("image2.jpg")
	nuevaImagen = filtroAtt(im,im,20)
	imageAplica = ImageTk.PhotoImage(nuevaImagen)
	image = imageAplica
	create_image(imageAplica.width()/2, imageAplica.height()/2, anchor=CENTER, image=imageAplica, tags="bg_img")

#Funcion auxiliar de estecanografica
def cadenaBinario(cadena):
	cadenaBin = ""
	for i in cadena:
		cadenaBin = cadenaBin + bin(ord(i))[2:].zfill(8)
	return cadenaBin

def cifrar(imagen,mensaje,nombre):
	rgb = imagen.convert('RGB')
	ancho = imagen.size[0]
	alto = imagen.size[1]
	nueva = Image.new("RGB",(ancho,alto),"white")
	pixels = nueva.load()
	mensajeBin = cadenaBinario(mensaje)
	contador = 0
	for i in range(ancho):
		for j in range(alto):
			r,g,b = rgb.getpixel((i,j))
			rbyte = "{0:b}".format(r)
			rbyte = list(rbyte)
			gbyte = "{0:b}".format(g)
			gbyte = list(gbyte)
			bbyte = "{0:b}".format(b)
			bbyte = list(bbyte)
			if(contador < len(mensajeBin)):
				if(contador < len(mensajeBin)):
					rbyte[len(rbyte)-1] = mensajeBin[contador]
					contador += 1
				if(contador < len(mensajeBin)):
					gbyte[len(gbyte)-1] = mensajeBin[contador]
					contador += 1
				if(contador < len(mensajeBin)):
					bbyte[len(bbyte)-1] = mensajeBin[contador]
					contador += 1
			else:
				rbyte[len(rbyte)-1] = "1"
				gbyte[len(gbyte)-1] = "1"
				bbyte[len(bbyte)-1] = "1"
			r = "".join(rbyte)
			r = int(r,2)
			g = "".join(gbyte)
			g = int(g,2)
			b = "".join(bbyte)
			b = int(b,2)
			pixels[i,j] = (r,g,b)
	nueva.save(nombre + ".png","PNG")
	return imagen

def descifrar(imagen):
	rgb = imagen.convert("RGB")
	ancho = imagen.size[0]
	alto = imagen.size[1]
	mensajeBin = ""
	mensaje = ""
	for i in range(ancho):
		for j in range(alto):
			r,g,b = rgb.getpixel((i,j))
			rbyte = "{0:b}".format(r)
			rbyte = list(rbyte)
			gbyte = "{0:b}".format(g)
			gbyte = list(gbyte)
			bbyte = "{0:b}".format(b)
			bbyte = list(bbyte)
			mensajeBin = mensajeBin + rbyte[len(rbyte)-1] + gbyte[len(gbyte)-1] + bbyte[len(bbyte)-1]
	for i in range(0,len(mensajeBin),8):
		sub = mensajeBin[i:i+8]
		if(sub == "11111111"):
			break
		else:
			mensaje = mensaje + sub
	mensaje = ''.join(chr(int(mensaje[i:i+8], 2)) for i in xrange(0, len(mensaje), 8))
	print(mensaje)

def estecanografia():
	im = Image.open("image2.jpg")
	nomIma = raw_input("Ingresa el mensaje a esconder \n")
	nomSal = raw_input("Ingresa nombre de la salida de la imagen\n")
	a = cifrar(im,nomIma,nomSal)
	i = int(input("Si quieres decifrar la imagen preciona 1 de no ser presiona 2 \n"))
	if i == 1:
		im = Image.open(nomSal + ".png")
		descifrar(im)
	if i == 2:
		print("ADIOS")

#Algoritmo de quitar marca de agua con imagenes vistas en clase (ajedrecistas animados)
def quitarMarca(imagen,aplica):
	rgb = imagen.convert('RGB')
	pixels = aplica.load()    
	for i in range(imagen.size[0]):
		for j in range(aplica.size[1]):
			r,g,b = rgb.getpixel((i,j))
			nr = (r - g)
			if(nr < 10):
				pass
			else:
				prom = (int)((1.3475)*((r+g+b)/3))
				pixels[i,j] = (prom,prom,prom,0)
	aplica.show()

def aplicaQuitarMarca():
	image = Image.open("ejemplo.jpg")
	quitarMarca(image,image)


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

def aplicaEcualizacionColor():
	image = Image.open("image2.jpg")
	ecualizacionColor(image, image)

def aplicaEcualizacion():
	image = Image.open("image2.jpg")
	ecualizacion(image, image)

def aplicaAjusteColor():
	image = Image.open("image2.jpg")
	ajusteColor(image, image)

def aplicaAjuste():
	image = Image.open("image2.jpg")
	ajuste(image, image)

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
	aplica.show()

#Dithering Jarvis, Judice & Ninke
def ditheringJarvis():
	imageConvert = Image.open('image2.jpg').convert(mode='1',dither=Image.FLOYDSTEINBERG)
	imageConvert.save('DitheringWithPIL.jpg')
	imageConvert.show()

def aplicaDithering():
	image = Image.open("image2.jpg")
	ditheringFloy(image,image)







im = Image.open("image2.jpg")
width, height = im.size
new = crear_imagen2(width,height)

#Se crea la barra de menus 
barraMenu = Menu(ventana)

#Se agregan las menu bar
mnuFiltros = Menu(barraMenu)

#Se crean los comandos de archivos
mnuFiltros.add_command(label="Escala de grises", command=mostrarGrises)
mnuFiltros.add_command(label="Rojo", command = rojo)
mnuFiltros.add_command(label="Verde",command=verde)
mnuFiltros.add_command(label="Azul", command=azul)
mnuFiltros.add_command(label="Mosaico",command = mostrarMosaico)
mnuFiltros.add_command(label="Inverso",command=inverso)
mnuFiltros.add_command(label="Alto Contraste",command=altoConttraste)
mnuFiltros.add_command(label="Blur",command=blur)
mnuFiltros.add_command(label="Motion Blur",command=motionBlur)
mnuFiltros.add_command(label="Encontrar Bordes",command=encuentraBordes)
mnuFiltros.add_command(label="Sharpen",command=sharpen)
mnuFiltros.add_command(label="Emboss",command=emboss)
mnuFiltros.add_command(label="Mediano",command=mediano)
#Aqui empiezan los filtros de la practica 3
mnuFiltros.add_command(label="Color",command=colorSinLetras)
mnuFiltros.add_command(label="Tono de Grises",command=tonoDeGris)
mnuFiltros.add_command(label="Mas o menos oscuros",command=masColorMenosColor)
mnuFiltros.add_command(label="Mas o menos grises",command=MasMenosGris)
mnuFiltros.add_command(label="Mas o menos Color",command=masMenosColor)
mnuFiltros.add_command(label="Cadena color",command=palabra)
mnuFiltros.add_command(label="Naipes",command=cartaNaipes)
#Filtro practica 4
mnuFiltros.add_command(label="Maximo",command=maximo)
mnuFiltros.add_command(label="Minimo",command=minimo)
mnuFiltros.add_command(label="Marca De Agua",command=marcaDeAgua)
#Filtros tarea 5
mnuFiltros.add_command(label="Recursivo Gris",command=recursiveGray)
mnuFiltros.add_command(label="Recursivo Color",command=recursiveColor)
#filtros tarea 6
mnuFiltros.add_command(label="Contraste Stretching",command=contrasteHS)
mnuFiltros.add_command(label="Semitonos",command=semitonos)
#filtros de la tarea 7
mnuFiltros.add_command(label="ATT",command=ATT)
mnuFiltros.add_command(label="Estecanografia",command=estecanografia)
#Filtro quitar marca de agua tarea 8
mnuFiltros.add_command(label="Quitar marca de agua",command=aplicaQuitarMarca)
#Filtros de histogramas tarea 9
histogramaMenu = Menu(mnuFiltros, tearoff=0)
histogramaMenu.add_command(label="Equalizacion", command = aplicaEcualizacion)
histogramaMenu.add_command(label="Equalizacion color", command = aplicaEcualizacionColor)
histogramaMenu.add_command(label="Ajuste", command = aplicaAjuste)
histogramaMenu.add_command(label="Ajuste color", command = aplicaAjusteColor)
mnuFiltros.add_cascade(label="Histograma", menu=histogramaMenu)
#filtros de Dithering tarea 10
DitheringMenu = Menu(mnuFiltros, tearoff=0)
DitheringMenu.add_command(label= "Dithering Floy-Steineerg", command = aplicaDithering)
DitheringMenu.add_command(label= "Dithering Jarvis", command = ditheringJarvis)
mnuFiltros.add_cascade(label="Dithering", menu=DitheringMenu)

#Se anaden al menu 
barraMenu.add_cascade(label="Filtros",menu = mnuFiltros )

#Agregamos ventana al menu
ventana.config(menu = barraMenu)




ventana.mainloop()