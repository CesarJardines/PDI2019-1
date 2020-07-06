import numpy as np
from PIL import Image

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
def escala_grises(image):
  width, height = image.size

  #Creamos la nueva imagen a escala 
  new = crear_imagen(width, height)
  #Cargamos los pixeles obtenidos anteriormente 
  pixels = new.load()

  #Recorremos la imagen con un for anidado 
  for i in range(width):
    for j in range(height):
      pixel = get_pixel(image, i, j)

      #Obtenemos los valores Rojo Verde y Azul.   
      rojo =   pixel[0]
      verde = pixel[1]
      azul =  pixel[0]

      #x=(R * .n + G * .m + B * .x)
      gray = (rojo * 0.299) + (verde * 0.587) + (azul * 0.114)

      #Ponemos nuevos pixeles en la imagen 
      pixels[i, j] = (int(gray), int(gray), int(gray))
    #Regresamos la nueva imagen

    return new

#ROJO


def imagen_rojo(image):
  im = Image.open('image.jpg')
  data = np.array(im)

  r1, g1, b1 = 0, 0, 0 # Original value
  r2, g2, b2 = 255, 0, 0 # Value that we want to replace it with

  red, green, blue = data[:,:,0], data[:,:,1], data[:,:,2]
  mask = (red == r1) & (green == g1) & (blue == b1)
  data[:,:,:3][mask] = [r2, g2, b2]

  im = Image.fromarray(data)
  #im.save('fig1_modified.png')

#encoding: utf-8
#Aqui seleccionamos la imagen
im = Image.open('image.jpg').convert('LA')
img = Image.open('image.jpg').convert('LA')

#escala_grises(im) 

imagen_rojo(img)

#Guardamos la imagen nueva
#im.save('escalagrises.png')
#Mostramos la imagen
#im.show()
img.save('imagenrojo.png')
img.show()
