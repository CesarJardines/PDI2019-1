from PIL import ImageTk, Image

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

image = Image.open("ejemplo.jpg")

quitarMarca(image,image)
    
