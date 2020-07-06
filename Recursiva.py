import os
import math
from PIL import ImageTk, Image
import PIL.Image
from TonosGris import *
from FiltroBrillo import *
from FiltroWarhol import *

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

def crear_imagen(i, j):
    image = Image.new("RGB", (i, j))
    return image

im = Image.open("image2.jpg")
width, height = im.size
new = crear_imagen(width,height)

aplicaRecursivaColor(im,im,30,30)
