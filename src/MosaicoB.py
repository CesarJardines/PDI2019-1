from PIL import ImageTk, Image

"""
Recibe dos valores, mosX y mosY que definen el tamanio del mosaico
Recorre la imagen de mosaico en mosaico
Por cada mosaico se saca el promedio de los valores rojo,verde y azul de cada pixel
Ya que se obtiene cada promedio, se aplica ese valor a cada componente correspondiente de los pixeles del mosaico
"""
def filtroMosaico(imagen,aplica,mosX,mosY):
    recorreX = 0
    recorreY = 0
    rprom = 0
    gprom = 0
    bprom = 0
    prom = 0
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
       
    return aplica

im = Image.open("image.jpg")
filtroMosaico(im,im,15,15)
im.show()