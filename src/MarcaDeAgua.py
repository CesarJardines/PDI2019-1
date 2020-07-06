from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageFilter
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