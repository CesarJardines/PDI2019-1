from PIL import ImageTk, Image
from Tkinter import *
import src.TonosGris
import src.FiltroBrillo
import src.FiltroWarhol

import tkMessageBox

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
