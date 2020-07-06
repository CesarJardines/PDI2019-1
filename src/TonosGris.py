from PIL import ImageTk, Image
import src.TonosGris
import src.FiltroBrillo
import src.FiltroWarhol


def filtroGris1(imagen,aplica):
    rgb = imagen.convert('RGB')
    pixels = aplica.load()
    for i in range(imagen.size[0]):
        for j in range(imagen.size[1]):
            r,g,b = rgb.getpixel((i,j))
            gris = int(round((r*0.3) + (g*0.59) + (b*0.11)))
            pixels[i,j] = (gris,gris,gris)
    return aplica

