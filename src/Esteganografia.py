from PIL import Image,ImageTk

"""
Dada una cadena lo convierte a su representacion en binario
"""
def cadenaBinario(cadena):
    cadenaBin = ""
    for i in cadena:
        cadenaBin = cadenaBin + bin(ord(i))[2:].zfill(8)
    return cadenaBin

"""
Escondemos el mensaje en la imagen dada
Cambiamos a binario el mensaje
Tomamos cada pixel de la imagen
Por cada pixel, tomamos el rgb 
Cambiamos el ultimo de bit del rgb con los bits del mensaje
"""
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

"""
Dada una imagen, obtenemos el mensaje que esta oculto 
Por cada pixel, obtenemos el ultimo bit de cada rgb
Cuando encontramos 8 1's seguidos
Regresamos la cadena binaria y ese es el mensaje oculto
"""
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














