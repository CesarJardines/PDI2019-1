from PIL import Image
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

#Metodo que juega con encontraste de pixeles azul
def contrasteAzul(intensity):
    iI = intensity
    minI = 100
    maxI = 210
    minO = 0
    maxO = 255
    salidaContraste = (iI-minI)*(((maxO-minO)/(maxI-minI))+minO)
    return salidaContraste

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