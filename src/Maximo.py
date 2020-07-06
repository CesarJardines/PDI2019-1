from PIL import Image
from PIL import ImageFilter
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